"""Synthetic trajectories with PLANTED dependence (validate.py anchor).

Each trajectory has a latent frailty theta_i shared by all its steps,
so step badness events are positively dependent WITHIN a trajectory
and independent ACROSS trajectories — the exact structure T-CRC is
designed for. Ground truth is known by construction: a step is "bad"
with probability p(theta_i); the trajectory fails iff at least 2 bad
steps occur (compounding loss: a single bad step is tolerated).

Step records are written so the LIBRARY's own derivation
(tcrc.step_signal) recovers a monotone signal of badness:
  - bad step, severe (prob ~0.22 given bad): is_error=True  -> s = 1.0
  - bad step, mild:                          marker text    -> s = 0.5
  - good step:                               neither        -> s = 0.0
So the method is tested through exactly the channel it will use on
real traces (design §7.2 ladder), never through oracle values.

With `dependent=False`, theta_i is fixed at its mean for every
trajectory (step events independent within trajectories) — the
control variant. T-CRC must control risk in both.
"""

from __future__ import annotations

import numpy as np


def gen_trajectories(rng, n, dependent=True):
    """Return a list of (steps, failed) with canonical step dicts."""
    out = []
    for _ in range(n):
        theta = float(rng.beta(2.0, 5.0)) if dependent else 2.0 / 7.0
        p_bad = 0.02 + 0.55 * theta
        n_steps = int(rng.poisson(6)) + 2
        steps = []
        n_bad = 0
        for t in range(n_steps):
            if rng.random() < p_bad:
                n_bad += 1
                severe = rng.random() < 0.22
                steps.append({"idx": t, "kind": "model_call", "tool": None,
                              "is_error": bool(severe),
                              "is_retry": False, "n_tokens": 100,
                              "text_digest": "" if severe
                                             else "error occurred"})
            else:
                steps.append({"idx": t, "kind": "model_call", "tool": None,
                              "is_error": False, "is_retry": False,
                              "n_tokens": 100, "text_digest": ""})
        failed = 1 if n_bad >= 2 else 0
        out.append((steps, failed))
    return out
