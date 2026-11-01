"""Area 2, V4 — prefix features, exactly the frozen §R5 list.

Input: a canonical trajectory's step list. Each step is a dict with
keys: action_text, obs_text, is_error, is_retry, tool, n_tokens,
text_digest, marker_hits (distinct FAILURE_MARKERS in observation).

Output: prefix feature matrix (T x 150) — 22 structured + 128 hashed
unigram buckets (cumulative counts, log1p). All features use steps
<= t only (PREFIX-SAFE); the final length T never enters.
"""
from __future__ import annotations

import hashlib
import re

import numpy as np

N_BUCKETS = 128
STRUCT_NAMES = [
    # (a) behavioural, 10
    "a_is_error", "a_err_sofar", "a_err_rate", "a_is_retry",
    "a_retries_sofar", "a_loop_count", "a_distinct_tools",
    "a_recoveries", "a_marker_hits_sofar", "a_marker_hits_now",
    # (b) position/length, 6
    "b_t", "b_tok_total", "b_tok_mean", "b_tok_mad",
    "b_since_err", "b_since_retry",
    # (c) cross-step, 6
    "c_err_recovered", "c_repeat_maxrun", "c_tool_switches",
    "c_tool_entropy", "c_err_frac_5", "c_err_frac_10",
]
_WORD = re.compile(r"[a-z0-9]+")


def _bucket(token: str) -> int:
    h = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
    return int.from_bytes(h, "little") % N_BUCKETS


def prefix_features(steps):
    """steps: list of step dicts. Returns (T, 150) float array."""
    T = len(steps)
    X = np.zeros((T, 22 + N_BUCKETS), dtype=np.float64)
    errs = np.array([s["is_error"] for s in steps], dtype=float)
    retries = np.array([s["is_retry"] for s in steps], dtype=float)
    toks = np.array([s["n_tokens"] for s in steps], dtype=float)
    tools = [s["tool"] for s in steps]
    actions = [s["action_text"] for s in steps]
    markers = np.array([s["marker_hits"] for s in steps], dtype=float)

    seen_actions = {}
    hash_counts = np.zeros(N_BUCKETS, dtype=np.float64)
    last_err_idx = 0   # 1-based step index of last error; 0 = none
    last_retry_idx = 0
    for t in range(1, T + 1):
        i = t - 1
        # hashed text: cumulative over steps <= t
        for w in _WORD.findall(steps[i]["text_digest"].lower()):
            hash_counts[_bucket(w)] += 1.0
        if errs[i]:
            last_err_idx = t
        if retries[i]:
            last_retry_idx = t
        # (a)
        err_sofar = errs[:t].sum()
        rec = sum(1 for j in range(1, t) if errs[j - 1] and not errs[j])
        # loop/repeat count: steps j<=t whose action equals an earlier one
        seen = set()
        loop = 0
        for j in range(t):
            if actions[j] in seen:
                loop += 1
            seen.add(actions[j])
        # (c) recovered error steps: errors not in the trailing error run
        trail = 0
        for j in range(t - 1, -1, -1):
            if errs[j]:
                trail += 1
            else:
                break
        err_recovered = err_sofar - trail
        # repeated-action max run
        maxrun, run = 0, 0
        prev = None
        for j in range(t):
            run = run + 1 if actions[j] == prev else 1
            prev = actions[j]
            maxrun = max(maxrun, run)
        switches = sum(1 for j in range(1, t) if tools[j] != tools[j - 1])
        # tool entropy
        from collections import Counter
        cnt = Counter(tools[:t])
        ent = 0.0
        for c in cnt.values():
            p = c / t
            ent -= p * np.log(p)
        w5 = errs[max(0, t - 5):t]
        w10 = errs[max(0, t - 10):t]
        row = [
            errs[i], err_sofar, err_sofar / t, retries[i],
            retries[:t].sum(), float(loop), float(len(cnt)), float(rec),
            markers[:t].sum(), markers[i],
            float(t), toks[:t].sum(), toks[:t].mean(),
            float(np.median(np.abs(toks[:t] - np.median(toks[:t])))),
            float(min(32, t - last_err_idx)), float(min(32, t - last_retry_idx)),
            float(err_recovered), float(maxrun), float(switches), float(ent),
            float(w5.mean()), float(w10.mean()),
        ]
        X[i, :22] = row
        X[i, 22:] = np.log1p(hash_counts)
    return X


def aggregate_haz(step_scores):
    """S_haz = 1 - prod_t (1 - s_t) (§R5 primary aggregation)."""
    s = np.clip(np.asarray(step_scores, dtype=float), 0.0, 1.0)
    return float(1.0 - np.prod(1.0 - s))
