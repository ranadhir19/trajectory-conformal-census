"""Area 2, V4 — Approach-C signal (§R5) and evaluation (§§R6-R7).

Heads: (i) L2 logistic (C=1.0) on the 22 structured features,
standardised by fit-split weighted mean/SD; (ii) gradient-boosted
trees (max_depth 3, n_estimators 100, lr 0.05, min_samples_leaf 20)
on all 150. Stacking: 5-fold cross-fitting by task group (stream 3);
logistic meta-learner (C=1.0, intercept, weights 1/T_i) on OOF
scores; base heads refit on the full fit split; meta NOT refit.
Primary aggregation S_haz = 1 - prod(1 - s(i,t)).
"""
from __future__ import annotations

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

import tcrc
import v4lib
from v4features import aggregate_haz


def _stack_examples(trajs):
    """trajs: list of dicts with X (T,150), y (0/1), task_id.
    Returns stacked prefix arrays with per-example weights 1/T_i."""
    Xs, ys, ws, tids = [], [], [], []
    for tr in trajs:
        T = tr["X"].shape[0]
        Xs.append(tr["X"])
        ys.append(np.full(T, tr["y"], dtype=float))
        ws.append(np.full(T, 1.0 / T))
        tids.append(np.full(T, tr["task_id"], dtype=object))
    return (np.vstack(Xs), np.concatenate(ys), np.concatenate(ws),
            np.concatenate(tids))


class SignalModel:
    def __init__(self):
        self.mu = None
        self.sd = None
        self.head_lr = None
        self.head_gbm = None
        self.meta = None

    def _fit_heads(self, X, y, w):
        mu = np.average(X[:, :22], axis=0, weights=w)
        var = np.average((X[:, :22] - mu) ** 2, axis=0, weights=w)
        sd = np.sqrt(var)
        sd[sd == 0] = 1.0
        lr = LogisticRegression(C=1.0, max_iter=1000)
        lr.fit((X[:, :22] - mu) / sd, y, sample_weight=w)
        gbm = GradientBoostingClassifier(max_depth=3, n_estimators=100,
                                         learning_rate=0.05,
                                         min_samples_leaf=20,
                                         random_state=v4lib.SEED_BASE)
        gbm.fit(X, y, sample_weight=w)
        return mu, sd, lr, gbm

    def _head_scores(self, mu, sd, lr, gbm, X):
        p1 = lr.predict_proba((X[:, :22] - mu) / sd)[:, 1]
        p2 = gbm.predict_proba(X)[:, 1]
        return np.column_stack([p1, p2])

    def fit(self, fit_trajs, pop_index):
        X, y, w, tids = _stack_examples(fit_trajs)
        fold_of = v4lib.stacking_folds(sorted(set(tids.tolist())), pop_index)
        folds = np.array([fold_of[t] for t in tids])
        oof = np.zeros((len(y), 2))
        for k in range(5):
            tr_m = folds != k
            te_m = folds == k
            if te_m.sum() == 0 or len(np.unique(y[tr_m])) < 2:
                continue
            mu, sd, lr, gbm = self._fit_heads(X[tr_m], y[tr_m], w[tr_m])
            oof[te_m] = self._head_scores(mu, sd, lr, gbm, X[te_m])
        self.meta = LogisticRegression(C=1.0, max_iter=1000)
        self.meta.fit(oof, y, sample_weight=w)
        self.mu, self.sd, self.head_lr, self.head_gbm = self._fit_heads(X, y, w)
        return self

    def step_scores(self, X):
        hs = self._head_scores(self.mu, self.sd, self.head_lr,
                               self.head_gbm, X)
        return self.meta.predict_proba(hs)[:, 1]

    def traj_score(self, X):
        return aggregate_haz(self.step_scores(X))


def gate_quantities(model, gate_trajs, pop_index):
    """§R6 gate on the GATE split: AUC(S_haz), AUC(S_len), delta,
    percentile bootstrap 95% CI (1,000 resamples, stream 4)."""
    S = np.array([model.traj_score(tr["X"]) for tr in gate_trajs])
    y = np.array([tr["y"] for tr in gate_trajs], dtype=int)
    L = np.array([tr["X"].shape[0] for tr in gate_trajs], dtype=float)
    auc_h = v4lib.rank_auc(S, y)
    auc_l = v4lib.rank_auc(L, y)
    g = v4lib.rng(pop_index, v4lib.STREAM_BOOT)
    n = len(y)
    deltas = []
    for _ in range(1000):
        idx = g.integers(0, n, n)
        if len(np.unique(y[idx])) < 2:
            continue
        deltas.append(v4lib.rank_auc(S[idx], y[idx]) -
                      v4lib.rank_auc(L[idx], y[idx]))
    deltas = np.array(deltas)
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    return {"auc_haz": auc_h, "auc_len": auc_l, "delta": auc_h - auc_l,
            "ci_lo": float(lo), "ci_hi": float(hi),
            "n_boot": int(len(deltas)),
            "passed": v4lib.gate_decision(auc_h, auc_l, float(lo))}


def crc_frontier(cal_S, cal_y, test_S, test_y, alphas=(0.05, 0.10, 0.20)):
    """Per-alpha: lambda_hat from calibration; test risk/abstention
    pair; guarantee-alert flag (test risk CP CI entirely above a)."""
    from run_pilot import clopper_pearson
    out = {}
    for a in alphas:
        lam, _ = tcrc.crc_threshold(cal_S, cal_y, a)
        ev = tcrc.evaluate(test_S, test_y, lam)
        k = int(round(ev["risk"] * ev["n"]))
        lo, hi = clopper_pearson(k, ev["n"]) if ev["n"] else (0.0, 1.0)
        out[a] = {"lambda": (None if lam == -np.inf else float(lam)),
                  "abstain_all": bool(lam == -np.inf),
                  "test": ev, "risk_ci": [float(lo), float(hi)],
                  "alert": bool(lo > a)}
    return out


def ub_arm(cal_trajs, test_trajs, alpha=0.10):
    """HV3/SQ1 descriptive arm (§R6): union-bound per-step screen."""
    cal_step_scores, cal_step_bad = [], []
    for tr in cal_trajs:
        for s in tr["steps"]:
            cal_step_scores.append(tcrc.step_signal(s, include_error=False))
            cal_step_bad.append(s["is_error"])
    tbar = float(np.mean([len(tr["steps"]) for tr in cal_trajs])) \
        if cal_trajs else 1.0
    tau = tcrc.ub_arm_threshold(cal_step_scores, cal_step_bad, alpha, tbar)
    ev = tcrc.ub_evaluate([(tr["steps"], tr["y"]) for tr in test_trajs], tau)
    return {"tau": (None if tau == -np.inf else float(tau)), "test": ev}


def stratified_arm(cal, test, alpha=0.10):
    """SQ3 descriptive: per-stratum T-CRC with Bonferroni across
    strata. cal/test: lists of (stratum, S, y). Exercised only by
    the caller when the §R1 size rule holds."""
    strata = sorted(set(s for s, _, _ in cal))
    m = len(strata)
    out = {}
    for st in strata:
        cS = np.array([S for s, S, _ in cal if s == st])
        cy = np.array([y for s, _, y in cal if s == st])
        tS = np.array([S for s, S, _ in test if s == st])
        ty = np.array([y for s, _, y in test if s == st])
        lam, _ = tcrc.crc_threshold(cS, cy, alpha / m)
        out[st] = {"lambda": (None if lam == -np.inf else float(lam)),
                   "test": tcrc.evaluate(tS, ty, lam)}
    return out


def monitor(cal_lam_losses, alpha=0.10):
    """SQ2 descriptive: betting-CS monitor over the accepted-stream
    loss sequence; alarm when the CS lower bound exceeds alpha."""
    lo, hi = tcrc.betting_cs_bounds(cal_lam_losses, delta=0.05)
    return {"cs_lo": float(lo), "cs_hi": float(hi), "alarm": bool(lo > alpha)}
