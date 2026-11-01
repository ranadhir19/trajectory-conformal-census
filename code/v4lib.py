"""Area 2, V4 programme — core frozen-rule implementations.

Every function here implements a rule frozen in EXPERIMENTS_V4.md
Part I. Section references (§R#) are to that registration. Nothing in
this module reads data files; it is pure rule machinery, unit-tested
by validate.py Stage F.
"""
from __future__ import annotations

import numpy as np
from scipy import stats

SEED_BASE = 20261031

# §R2 population order: index j used by every RNG stream.
POPULATIONS = [
    ("CF-1", "CF", "SWE_Rebench"),
    ("CF-2", "CF", "SWE_Smith"),
    ("CF-3", "CF", "R2E_Gym"),
    ("SS-1", "SS", "tool/claude-3-7"),
    ("SS-2", "SS", "xml/claude-3-7"),
    ("SS-3", "SS", "ticks/claude-3-7"),
    ("SS-4", "SS", "tool/claude-3-5"),
    ("SS-5", "SS", "xml/claude-3-5"),
    ("SS-6", "SS", "ticks/claude-3-5"),
]
POP_INDEX = {pid: i + 1 for i, (pid, _, _) in enumerate(POPULATIONS)}

# Stream ids (§R4): 1 sample, 2 split, 3 stacking folds, 4 gate
# bootstrap, 5 monitor/descriptive resampling.
STREAM_SAMPLE, STREAM_SPLIT, STREAM_FOLD, STREAM_BOOT, STREAM_MISC = 1, 2, 3, 4, 5


def rng(pop_index: int, stream_id: int) -> np.random.Generator:
    """The only RNG constructor allowed in V4 code (§R4, defect N3)."""
    return np.random.default_rng(np.random.SeedSequence([SEED_BASE, pop_index, stream_id]))


# ---------------------------------------------------------------- §R3(v)
def binarise_cf_reward(distinct_values):
    """Frozen CF binarisation: a deterministic function of the set V
    of distinct non-null `reward` values (§R3(v), defect N2 repair).

    Returns (rule, success_fn) where rule is 'clause1' | 'clause2' |
    'ineligible'. Values take the artefact's type (Gate 9 note X4):
    booleans and numeric values coerce to float; anything else
    (including numeric-looking strings) is non-numeric -> clause 3.
    """
    vals = list(distinct_values)
    if len(vals) == 0:
        # V empty: no usable trajectories can exist (leg (a) fails);
        # recorded as ineligible at registration level (note X4).
        return "ineligible", None
    numeric = []
    for v in vals:
        if isinstance(v, bool):
            numeric.append(1.0 if v else 0.0)
        elif isinstance(v, (int, float, np.integer, np.floating)):
            if v != v:  # NaN is not a value; treat as non-numeric
                return "ineligible", None
            numeric.append(float(v))
        else:
            return "ineligible", None
    if all(x in (0.0, 1.0) for x in numeric):
        return "clause1", (lambda r: float(r) == 1.0)
    if all(0.0 <= x <= 1.0 for x in numeric):
        return "clause2", (lambda r: float(r) == 1.0)
    return "ineligible", None


def binarise_ss_resolved(distinct_values):
    """SS rule (§R3(v)): success iff `resolved` is true; any
    non-boolean value in the observed set -> ineligible."""
    for v in distinct_values:
        if not isinstance(v, (bool, np.bool_)):
            return "ineligible", None
    return "boolean", (lambda r: bool(r) is True)


# ------------------------------------------------------------- §R3 legs
def eligibility(base_failure, usable_n, split_class_counts):
    """§R3 eligibility. split_class_counts: dict split->(n_succ, n_fail)
    for gate/cal/test. Returns 'confirmatory' | 'descriptive' |
    'ineligible:<leg>'."""
    if usable_n < 800:
        return "ineligible:leg-a"
    if base_failure is None or not (0.10 <= base_failure <= 0.50):
        return "ineligible:leg-b"
    for split in ("cal", "test"):
        ns, nf = split_class_counts[split]
        if ns + nf < 160:
            return "ineligible:leg-c-size"
    for split in ("gate", "cal", "test"):
        ns, nf = split_class_counts[split]
        if ns < 40 or nf < 40:
            return "ineligible:leg-c-class"
    if base_failure <= 0.40:
        return "confirmatory"
    return "descriptive"


def cp_halfwidth(n, p, conf=0.95):
    """Exact Clopper-Pearson interval half-width at count k=round(p*n)."""
    k = int(round(p * n))
    lo, hi = stats.beta.ppf([(1 - conf) / 2, 1 - (1 - conf) / 2],
                            [k, k + 1], [n - k + 1, n - k])
    if k == 0:
        lo = 0.0
    if k == n:
        hi = 1.0
    return (hi - lo) / 2.0, lo, hi


# ---------------------------------------------------------------- §R4
def draw_sample(group_sizes: dict, pop_index: int, cap: int = 4000):
    """§R4 study sample: task groups (task_id -> n trajectories)
    ordered by the sample stream (stream 1); whole groups included
    until cumulative trajectories first reach >= cap; whole
    population if usable <= cap. Group list order before the
    permutation: sorted by task id (build-log interpretation X5).
    Returns the ordered list of sampled task ids."""
    ids = sorted(group_sizes.keys())
    if sum(group_sizes.values()) <= cap:
        return ids
    g = rng(pop_index, STREAM_SAMPLE)
    order = [ids[i] for i in g.permutation(len(ids))]
    out, cum = [], 0
    for tid in order:
        out.append(tid)
        cum += group_sizes[tid]
        if cum >= cap:
            break
    return out


SPLIT_PROPS = {"fit": 0.40, "gate": 0.20, "cal": 0.20, "test": 0.20}
SPLIT_ORDER = ["fit", "gate", "cal", "test"]


def assign_splits(groups: dict, pop_index: int):
    """§R4 split assignment (frozen greedy-deficit algorithm).
    groups: task_id -> (n_traj, n_fail). Strata by composition
    (all-failure, mixed, all-success processed in that order);
    within a stratum, groups in stream-2 permutation order of the
    sorted task-id list; each group goes whole to the split with
    the largest remaining trajectory deficit; ties break fit >
    gate > cal > test. Returns task_id -> split name."""
    total = sum(n for n, _ in groups.values())
    targets = {s: SPLIT_PROPS[s] * total for s in SPLIT_ORDER}
    assigned = {s: 0 for s in SPLIT_ORDER}
    strata = {"allfail": [], "mixed": [], "allsucc": []}
    for tid, (n, nf) in groups.items():
        if nf == n:
            strata["allfail"].append(tid)
        elif nf == 0:
            strata["allsucc"].append(tid)
        else:
            strata["mixed"].append(tid)
    g = rng(pop_index, STREAM_SPLIT)
    out = {}
    for sname in ("allfail", "mixed", "allsucc"):
        ids = sorted(strata[sname])
        for i in g.permutation(len(ids)):
            tid = ids[i]
            n = groups[tid][0]
            best, best_def = None, None
            for s in SPLIT_ORDER:
                d = targets[s] - assigned[s]
                if best_def is None or d > best_def:
                    best, best_def = s, d
            out[tid] = best
            assigned[best] += n
    return out


def split_proportions_ok(assign: dict, groups: dict, tol_pp: float = 3.0):
    """§R4 formation check: every realised split share within
    +/- tol percentage points of its target proportion."""
    total = sum(n for n, _ in groups.values())
    counts = {s: 0 for s in SPLIT_ORDER}
    for tid, s in assign.items():
        counts[s] += groups[tid][0]
    for s in SPLIT_ORDER:
        share = 100.0 * counts[s] / total
        if abs(share - 100.0 * SPLIT_PROPS[s]) > tol_pp:
            return False, counts
    return True, counts


def stacking_folds(group_ids, pop_index: int, k: int = 5):
    """§R5 stacking: 5-fold cross-fitting by task group; folds from
    stream 3 (build-log interpretation X5: groups in stream-3
    permutation order of the sorted id list, assigned round-robin).
    Returns task_id -> fold index."""
    ids = sorted(group_ids)
    g = rng(pop_index, STREAM_FOLD)
    order = [ids[i] for i in g.permutation(len(ids))]
    return {tid: i % k for i, tid in enumerate(order)}


# ------------------------------------------------------------- §R6 gate
def rank_auc(scores, labels):
    """Rank AUC with average ties (v1 helper semantics)."""
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    n1 = int(labels.sum())
    n0 = len(labels) - n1
    if n1 == 0 or n0 == 0:
        return float("nan")
    ranks = stats.rankdata(scores)
    return float((ranks[labels == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def gate_decision(auc_haz, auc_len, ci_lo):
    """§R6 mechanical gate: all three clauses."""
    return bool(auc_haz >= 0.65 and (auc_haz - auc_len) >= 0.10 and ci_lo > 0.0)


# ---------------------------------------------------------------- §R8
def population_state(gate_passed, test_risk, test_abst, alpha=0.10,
                     alert=False, rerun_state=None):
    """§R8 population states. alert=True means the guarantee-alert
    condition fired on the (final) run; rerun_state is used only
    when an invalid run was re-executed once (note X3: a re-run
    that itself alerts ends FAIL(ALERT))."""
    if rerun_state is not None:
        return rerun_state
    if alert:
        return "FAIL(ALERT)"
    if not gate_passed:
        return "FAIL"
    if test_risk is not None and test_risk <= alpha and test_abst <= 0.40:
        return "PASS"
    return "FAIL"


def programme_verdict(cf_verdict, ss_verdict, cf_repl_pass=False,
                      ss_repl_pass=False):
    """§R8 decision table (exhaustive, mutually exclusive). Family
    verdicts: 'PASS' | 'FAIL' | 'FAIL(ALERT)' | 'NO-TEST'. FAIL and
    FAIL(ALERT) count identically. Replication PASSes matter ONLY
    in row 2 (single-family), per the frozen table's own terms
    (Gate 9 note X1: the ordered table governs)."""
    def is_fail(v):
        return v in ("FAIL", "FAIL(ALERT)")

    fams = [cf_verdict, ss_verdict]
    if all(v == "NO-TEST" for v in fams):
        return "H-DATA"
    if sum(v == "NO-TEST" for v in fams) == 1:
        # Row 2: single-family reading on the tested family.
        if cf_verdict == "NO-TEST":
            primary, repl = ss_verdict, ss_repl_pass
        else:
            primary, repl = cf_verdict, cf_repl_pass
        if primary == "PASS" and repl:
            return "SINGLE-FAMILY SUPPORT"
        if primary == "PASS":
            return "SINGLE-FAMILY MIXED"
        return "SINGLE-FAMILY FAILURE"
    # Row 3: both families tested.
    if cf_verdict == "PASS" and ss_verdict == "PASS":
        return "SUPPORTED"
    if is_fail(cf_verdict) and is_fail(ss_verdict):
        return "KILL"
    return "MIXED"
