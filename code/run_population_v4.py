"""Area 2, V4 — per-population execution under the frozen V4
registration (§§R4-R8), run only after the §R3 census + eligibility
record for the population exists.

Usage: venv/bin/python run_population_v4.py <POP>
Phases (each checkpointed under results/v4/):
  sample   — re-stream artefact; retain canonical trajectories of
             the §R4 sampled task groups only -> sample_<POP>.jsonl
  splits   — §R4 greedy-deficit assignment -> splits_<POP>.json,
             formation checks recorded
  run      — featurise, fit (fit split), gate (gate split); if the
             gate passes and the population is confirmatory: cal
             frontier + ONE test evaluation; descriptive arms.
             -> result_<POP>.json
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tcrc
import v4lib
import v4parse
import v4signal
from run_census_v4 import (CACHE, CF_REPO, CF_REV, POP_FILE_SPLIT,
                           RES, SS_MODEL_CLASS, SS_REPO, SS_REV,
                           list_files)
from v4features import prefix_features


def load_census(pop):
    return json.load(open(os.path.join(RES, f"census_{pop}.json")))


def phase_sample(pop, census):
    """Re-stream the artefact and retain sampled trajectories."""
    sample_path = os.path.join(RES, f"sample_{pop}.jsonl")
    if os.path.exists(sample_path):
        return sample_path
    fam = pop.split("-")[0]
    repo, rev = (CF_REPO, CF_REV) if fam == "CF" else (SS_REPO, SS_REV)
    # task groups over trajectories WITH task ids (build-log note)
    groups = build_groups(pop, census)  # task_id -> n usable traj
    j = v4lib.POP_INDEX[pop]
    sampled = set(v4lib.draw_sample(groups, j))
    json.dump(sorted(sampled),
              open(os.path.join(RES, f"sampled_tasks_{pop}.json"), "w"))
    files = list_files(repo, rev, POP_FILE_SPLIT[pop])
    tmp = sample_path + ".tmp"
    n_kept = 0
    with open(tmp, "w") as fh:
        for f in files:
            local = hf_hub_download(repo, f, repo_type="dataset",
                                    revision=rev, local_dir=CACHE)
            pf = pq.ParquetFile(local)
            cols = (["trajectory_id", "image", "messages", "reward"]
                    if fam == "CF" else
                    ["instance_id", "messages", "resolved", "model"])
            for batch in pf.iter_batches(batch_size=100, columns=cols):
                for row in batch.to_pylist():
                    if fam == "SS":
                        model = str(row.get("model") or "")
                        if SS_MODEL_CLASS[pop] not in model:
                            continue
                        outcome = row.get("resolved")
                        if outcome is None:
                            continue
                        success = bool(outcome)
                    else:
                        outcome = row.get("reward")
                        if outcome is None:
                            continue
                        success = float(outcome) == 1.0  # set by census clause; see run()
                    tid, _ = v4parse.extract_task_id(row, fam)
                    if tid is None or tid not in sampled:
                        continue
                    try:
                        steps, tlevel = v4parse.parse_messages(row["messages"])
                    except Exception:
                        continue
                    if len(steps) < 1:
                        continue
                    fh.write(json.dumps({
                        "task_id": tid, "success": success,
                        "token_level": tlevel, "steps": steps}) + "\n")
                    n_kept += 1
            try:
                os.remove(local)
            except OSError:
                pass
    os.rename(tmp, sample_path)
    print(f"{pop}: sampled trajectories kept = {n_kept}", flush=True)
    return sample_path


def build_groups(pop, census):
    """Task groups over USABLE trajectories, written by the census
    itself (run_census_v4 pass) — the §R4 sampling input."""
    groups_path = os.path.join(RES, f"groups_{pop}.json")
    if not os.path.exists(groups_path):
        raise SystemExit(f"groups file missing for {pop}: census "
                         f"must complete first")
    return json.load(open(groups_path))


def load_sample(pop):
    trajs = []
    with open(os.path.join(RES, f"sample_{pop}.jsonl")) as fh:
        for line in fh:
            trajs.append(json.loads(line))
    return trajs


def run(pop):
    census = load_census(pop)
    fam = pop.split("-")[0]
    j = v4lib.POP_INDEX[pop]
    result = {"population": pop, "census": census}
    # --- outcome binarisation from the census distinct-value set
    if fam == "CF":
        vals = []
        for k in census["outcome_values"]:
            vals.append(float(k))
        rule, _ = v4lib.binarise_cf_reward(vals)
        result["cf_reward_rule"] = rule
        if rule == "ineligible":
            result["verdict"] = "census-ineligible: binarisation clause 3"
            json.dump(result, open(os.path.join(RES, f"result_{pop}.json"), "w"), indent=1)
            print(f"{pop}: CF binarisation ineligible (V recorded in census)")
            return result
        base_fail = 1.0 - sum(c for k, c in census["outcome_values"].items()
                              if float(k) == 1.0) / max(1, census["n_usable"])
    else:
        rule, _ = v4lib.binarise_ss_resolved(
            [k == "True" for k in census["outcome_values"]])
        result["ss_resolved_rule"] = rule
        nfail = census["outcome_values"].get("False", 0)
        base_fail = nfail / max(1, census["n_usable"])
    result["base_failure"] = base_fail
    if census["n_usable"] < 800 or not (0.10 <= base_fail <= 0.50):
        result["verdict"] = "ineligible: census legs (a)/(b)"
        json.dump(result, open(os.path.join(RES, f"result_{pop}.json"), "w"), indent=1)
        print(f"{pop}: ineligible at census legs, base_fail={base_fail}")
        return result

    build_groups(pop, census)
    phase_sample(pop, census)
    trajs = load_sample(pop)
    # --- group composition from the sampled trajectories themselves
    comp = {}
    for tr in trajs:
        c = comp.setdefault(tr["task_id"], [0, 0])
        c[0] += 1
        c[1] += 0 if tr["success"] else 1
    groups = {tid: (c[0], c[1]) for tid, c in comp.items()}
    assign = v4lib.assign_splits(groups, j)
    ok, counts = v4lib.split_proportions_ok(assign, groups)
    split_counts = {}
    for s in v4lib.SPLIT_ORDER:
        members = [tr for tr in trajs if assign[tr["task_id"]] == s]
        split_counts[s] = (sum(1 for tr in members if tr["success"]),
                           sum(1 for tr in members if not tr["success"]))
    json.dump(assign, open(os.path.join(RES, f"splits_{pop}.json"), "w"))
    result["split_sizes"] = counts
    result["split_class_counts"] = split_counts
    result["proportion_check_ok"] = ok
    tier = v4lib.eligibility(base_fail, census["n_usable"], split_counts)
    result["eligibility"] = tier
    if not ok or tier.startswith("ineligible"):
        result["verdict"] = "ineligible: split realisation (leg c / proportions)"
        json.dump(result, open(os.path.join(RES, f"result_{pop}.json"), "w"), indent=1)
        print(f"{pop}: split realisation ineligible: {tier}, prop_ok={ok}")
        return result

    # --- featurise
    feat_path = os.path.join(RES, f"features_{pop}.npz")
    by_split = {s: [] for s in v4lib.SPLIT_ORDER}
    for tr in trajs:
        s = assign[tr["task_id"]]
        by_split[s].append({"X": prefix_features(tr["steps"]),
                            "y": 0 if tr["success"] else 1,
                            "task_id": tr["task_id"], "steps": tr["steps"]})
    # --- I2: fit + gate
    model = v4signal.SignalModel().fit(by_split["fit"], j)
    gate = v4signal.gate_quantities(model, by_split["gate"], j)
    result["gate"] = gate
    print(f"{pop}: gate AUC_haz={gate['auc_haz']:.3f} AUC_len={gate['auc_len']:.3f} "
          f"delta={gate['delta']:.3f} CI=[{gate['ci_lo']:.3f},{gate['ci_hi']:.3f}] "
          f"passed={gate['passed']}", flush=True)

    cal_S = np.array([model.traj_score(t["X"]) for t in by_split["cal"]])
    cal_y = np.array([t["y"] for t in by_split["cal"]])
    if tier == "descriptive":
        if gate["passed"]:
            fr = {}
            for a in (0.05, 0.10, 0.20):
                lam, _ = tcrc.crc_threshold(cal_S, cal_y, a)
                ev = tcrc.evaluate(cal_S, cal_y, lam)
                fr[str(a)] = {"lambda": None if lam == -np.inf else float(lam),
                              "calibration_split": ev}
            result["descriptive_frontier_CALIBRATION_SPLIT"] = fr
        else:
            result["descriptive_note"] = "gate failed: no lambda calibrated (X7)"
        result["verdict"] = "descriptive-only (no verdict)"
        json.dump(result, open(os.path.join(RES, f"result_{pop}.json"), "w"), indent=1)
        return result

    if not gate["passed"]:
        result["state"] = "FAIL (gate)"
        json.dump(result, open(os.path.join(RES, f"result_{pop}.json"), "w"), indent=1)
        print(f"{pop}: gate FAILED -> state FAIL", flush=True)
        return result

    # --- I5 rehearsal complete (gate/cal only); test evaluated once
    test_S = np.array([model.traj_score(t["X"]) for t in by_split["test"]])
    test_y = np.array([t["y"] for t in by_split["test"]])
    frontier = v4signal.crc_frontier(cal_S, cal_y, test_S, test_y)
    result["frontier"] = {str(k): v for k, v in frontier.items()}
    primary = frontier[0.10]
    result["ub_arm"] = v4signal.ub_arm(by_split["cal"], by_split["test"])
    losses = []
    lam10 = primary["lambda"]
    if lam10 is not None:
        losses = [float(y) * float(S <= lam10)
                  for S, y in zip(test_S, test_y)]
    result["monitor"] = v4signal.monitor(losses) if losses else None
    alert = bool(primary["alert"])
    state = v4lib.population_state(True, primary["test"]["risk"],
                                   primary["test"]["abstention"],
                                   alpha=0.10, alert=alert)
    result["state"] = state
    json.dump(result, open(os.path.join(RES, f"result_{pop}.json"), "w"), indent=1)
    print(f"{pop}: state={state} risk={primary['test']['risk']:.4f} "
          f"abst={primary['test']['abstention']:.3f} alert={alert}", flush=True)
    return result


if __name__ == "__main__":
    run(sys.argv[1])
