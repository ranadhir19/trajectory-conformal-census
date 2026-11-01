"""Trajectory-level conformal risk control (T-CRC) — core library.

Implements SOLUTION_DESIGN.md for Area 2 (trajectory-conformal-risk-
control) of the Research Orchestration Program.

Sampling unit: one trajectory. Calibration points are trajectories;
steps inside a trajectory are arbitrarily dependent and the method
never assumes their independence.

Primary endpoint loss (binary trajectory failure, unconditional
deployment risk):
    L(i, lam) = 1{trajectory i failed} * 1{S(i) <= lam}
where S(i) is a frozen trajectory risk score from per-step signals.

CRC threshold (Angelopoulos et al. 2024, trajectory-lifted):
    lam_hat = max { lam in unique calibration scores :
                    (sum_i L(i, lam) + 1) / (n + 1) <= alpha }
with the convention lam_hat = -inf (accept nothing) if no candidate
satisfies the bound. Evaluation is over sorted UNIQUE scores, so ties
are handled exactly (all trajectories sharing a score are accepted or
rejected together).

Dependencies: Python 3 stdlib + numpy only (so validate.py runs under
system python3).
"""

from __future__ import annotations

import math

import numpy as np

# Frozen failure-marker list for the behavioural step-signal rung
# (SOLUTION_DESIGN.md §7.2, rung 2). Matched case-insensitively on the
# step text digest.
FAILURE_MARKERS = ("error", "failed", "exception", "traceback",
                   "timeout", "invalid", "not found", "cannot")


def step_signal(step, include_error=True):
    """Per-step risk signal s in [0, 1] from one canonical step record.

    Ladder (SOLUTION_DESIGN.md §7.2): native error rung (1.0) then the
    behavioural rung (max of components: retry 0.5, failure-marker
    0.5). `include_error=False` returns the behavioural composite only
    (used by the union-bound arm, where the native error bit is the
    step label and must not also be the score).
    """
    if include_error and step.get("is_error"):
        return 1.0
    sig = 0.0
    if step.get("is_retry"):
        sig = max(sig, 0.5)
    text = (step.get("text_digest") or "").lower()
    if text and any(m in text for m in FAILURE_MARKERS):
        sig = max(sig, 0.5)
    return sig


def trajectory_scores(steps, include_error=True):
    """Return (S_max, S_haz) for one trajectory's step list.

    S_max = max step signal ("worst step").
    S_haz = 1 - prod_t (1 - s_t) (cumulative-hazard aggregation).
    Empty step list -> (0.0, 0.0).
    """
    if not steps:
        return 0.0, 0.0
    sigs = [step_signal(s, include_error=include_error) for s in steps]
    s_max = max(sigs)
    s_haz = 1.0
    for s in sigs:
        s_haz *= (1.0 - s)
    return s_max, 1.0 - s_haz


def crc_threshold(scores, failed, alpha):
    """Conformal risk control threshold for trajectory scores.

    scores: sequence of S(i); failed: sequence of 0/1 failure flags.
    Returns (lam_hat, n_cal). lam_hat = -inf means accept nothing
    (no candidate satisfies the corrected-risk bound).
    """
    scores = np.asarray(scores, dtype=float)
    failed = np.asarray(failed, dtype=float)
    n = len(scores)
    if n == 0:
        return -math.inf, 0
    order = np.argsort(scores)
    s_sorted = scores[order]
    f_sorted = failed[order]
    lam_hat = -math.inf
    for lam in np.unique(s_sorted):
        risk = (float(np.sum(f_sorted[s_sorted <= lam])) + 1.0) / (n + 1.0)
        if risk <= alpha:
            lam_hat = float(lam)
    return lam_hat, n


def evaluate(scores, failed, lam):
    """Test-split (risk, abstention) pair at a frozen threshold.

    risk = mean(failed * accepted) over ALL incoming trajectories
    (unconditional deployment risk, the controlled quantity);
    abstention = fraction not accepted; also returns risk among
    accepted for interpretation and the counts.
    """
    scores = np.asarray(scores, dtype=float)
    failed = np.asarray(failed, dtype=float)
    accepted = scores <= lam
    n = len(scores)
    n_acc = int(np.sum(accepted))
    risk = float(np.mean(failed * accepted)) if n else 0.0
    abst = float(1.0 - n_acc / n) if n else 0.0
    risk_acc = float(np.sum(failed * accepted) / n_acc) if n_acc else 0.0
    return {"n": n, "n_accepted": n_acc, "risk": risk,
            "abstention": abst, "risk_among_accepted": risk_acc}


def ub_arm_threshold(cal_step_scores, cal_step_bad, alpha, tbar):
    """Union-bound-composed per-step screen (SQ1 baseline arm).

    Per-step CRC at level alpha / tbar on pooled calibration steps:
    step loss l_j(tau) = bad_j * 1{s_j <= tau}; step threshold tau_hat
    by the same corrected-risk rule. A trajectory is accepted iff ALL
    its steps pass (s_j <= tau_hat). Returns tau_hat (or -inf).
    """
    return crc_threshold(cal_step_scores, cal_step_bad,
                         alpha / max(tbar, 1.0))[0]


def ub_evaluate(trajs, tau):
    """Apply the UB screen to test trajectories.

    trajs: list of (steps, failed) with steps as canonical step dicts.
    Step score = behavioural composite only (error bit is the label).
    Returns the same dict shape as evaluate().
    """
    failed = []
    accepted = []
    for steps, f in trajs:
        sigs = [step_signal(s, include_error=False) for s in steps]
        accepted.append(all(s <= tau for s in sigs))
        failed.append(f)
    failed = np.asarray(failed, dtype=float)
    accepted = np.asarray(accepted, dtype=bool)
    n = len(failed)
    n_acc = int(np.sum(accepted))
    return {"n": n, "n_accepted": n_acc,
            "risk": float(np.mean(failed * accepted)) if n else 0.0,
            "abstention": float(1.0 - n_acc / n) if n else 0.0,
            "risk_among_accepted":
                float(np.sum(failed * accepted) / n_acc) if n_acc else 0.0}


def betting_cs_bounds(losses, delta=0.05, lam_grid=(0.05, 0.1, 0.2, 0.4, 0.8),
                      m_grid=None):
    """Time-uniform confidence sequence for the mean of bounded losses.

    Fixed-lambda mixture betting CS (Ville's inequality): for each
    candidate mean m, wealth K_t(m) = mean over lambda in lam_grid of
    prod_j (1 + lambda * (x_j - m)), with lambda clipped so every
    factor stays non-negative. CS_t = {m : K_t(m) < 1/delta};
    returns (lower, upper) of the CS after the full stream. Valid
    simultaneously at every t under E[x_j | past] = m (the null for
    that m). Used for the SQ2 anytime-valid monitor: alarm when the
    lower bound exceeds alpha.
    """
    x = np.asarray(losses, dtype=float)
    if m_grid is None:
        m_grid = np.linspace(0.01, 0.99, 99)
    m_grid = np.asarray(m_grid, dtype=float)
    # log-wealth per (m, lambda); updated per observation.
    lam = np.asarray(lam_grid, dtype=float)
    # clip lambda per m: lambda <= 0.99 / max(m, 1 - m)
    lam_eff = np.minimum(lam[None, :],
                         0.99 / np.maximum(m_grid[:, None],
                                           1.0 - m_grid[:, None]))
    logw = np.zeros((len(m_grid), len(lam)))
    for xj in x:
        logw += np.log1p(lam_eff * (xj - m_grid[:, None]))
    # K(m) = mean over lambda of exp(logw)
    mx = np.max(logw, axis=1, keepdims=True)
    K = np.mean(np.exp(logw - mx), axis=1) * np.exp(mx[:, 0])
    inside = K < 1.0 / delta
    if not np.any(inside):
        return 1.0, 1.0
    return float(m_grid[inside].min()), float(m_grid[inside].max())
