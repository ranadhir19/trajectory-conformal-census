"""Area 2, V4 — census (§R3), the frozen first execution step.

Usage: venv/bin/python run_census_v4.py <POP> [<POP> ...]
  POP in CF-1..CF-3, SS-1..SS-6 (SS populations sharing a format
  split are aggregated in the same file pass).

Streams each artefact file at the §R2 frozen revision, aggregates
the §R3(i)-(vii) census quantities, checkpoints per file under
results/v4/, deletes each raw file after processing (§R13).
No gate, signal, or split quantity is computed here.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

import numpy as np
import pyarrow.parquet as pq
from huggingface_hub import HfApi, hf_hub_download

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4lib
import v4parse

AREA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(AREA, "results", "v4")
CACHE = os.path.join(AREA, "results", "v4", "_cache")
os.makedirs(RES, exist_ok=True)
os.makedirs(CACHE, exist_ok=True)

CF_REPO, CF_REV = "togethercomputer/CoderForge-Preview", \
    "060fca96cf723b2ebab3181e9e59fafd273df3cb"
SS_REPO, SS_REV = "SWE-bench/SWE-smith-trajectories", \
    "08e109b4a59eaeebf80e4675cd125d42e7ac99a4"

POP_FILE_SPLIT = {  # population -> artefact split name in file paths
    "CF-1": "SWE_Rebench", "CF-2": "SWE_Smith", "CF-3": "R2E_Gym",
    "SS-1": "tool", "SS-2": "xml", "SS-3": "ticks",
    "SS-4": "tool", "SS-5": "xml", "SS-6": "ticks",
}
SS_MODEL_CLASS = {"SS-1": "3-7", "SS-2": "3-7", "SS-3": "3-7",
                  "SS-4": "3-5", "SS-5": "3-5", "SS-6": "3-5"}


def list_files(repo, rev, split, exclude_tokenized=True):
    api = HfApi()
    files = api.list_repo_files(repo, repo_type="dataset", revision=rev)
    out = []
    for f in files:
        if not f.endswith(".parquet"):
            continue
        if exclude_tokenized and "tokenized" in f:
            continue
        if split in f:
            out.append(f)
    return sorted(out)


def blank_agg():
    return {"n_in_file": 0, "n_usable": 0, "n_parse_fail": 0,
            "outcome_values": Counter(), "n_with_task": 0,
            "task_ids": set(), "task_rule": Counter(),
            "n_steps": [], "n_ge3": 0, "token_levels": Counter(),
            "models": Counter(), "group_n": Counter(),
            "group_fail": Counter()}


def agg_add_file(agg, fagg):
    for k in ("n_in_file", "n_usable", "n_parse_fail", "n_with_task", "n_ge3"):
        agg[k] += fagg[k]
    agg["outcome_values"].update(fagg["outcome_values"])
    agg["task_ids"] |= fagg["task_ids"]
    agg["group_n"].update(fagg["group_n"])
    agg["group_fail"].update(fagg["group_fail"])
    agg["task_rule"].update(fagg["task_rule"])
    agg["n_steps"].extend(fagg["n_steps"])
    agg["token_levels"].update(fagg["token_levels"])
    agg["models"].update(fagg["models"])


def process_file_cf(path, agg):
    pf = pq.ParquetFile(path)
    for batch in pf.iter_batches(batch_size=100,
                                 columns=["trajectory_id", "image",
                                          "messages", "reward"]):
        rows = batch.to_pylist()
        for row in rows:
            agg["n_in_file"] += 1
            rew = row.get("reward")
            if rew is None:
                continue
            try:
                steps, tlevel = v4parse.parse_messages(row["messages"])
            except Exception:
                agg["n_parse_fail"] += 1
                continue
            if len(steps) < 1:
                continue
            agg["n_usable"] += 1
            agg["outcome_values"][repr(float(rew))] += 1
            agg["n_steps"].append(len(steps))
            if len(steps) >= 3:
                agg["n_ge3"] += 1
            agg["token_levels"][str(tlevel)] += 1
            tid, rule = v4parse.extract_task_id(row, "CF")
            if tid is not None:
                agg["n_with_task"] += 1
                agg["task_ids"].add(tid)
                agg["task_rule"][rule] += 1
                agg["group_n"][tid] += 1
                if float(rew) != 1.0:
                    agg["group_fail"][tid] += 1


def process_file_ss(path, aggs):
    """aggs: {pop: agg} for the two populations of this format split."""
    pf = pq.ParquetFile(path)
    for batch in pf.iter_batches(batch_size=100,
                                 columns=["instance_id", "messages",
                                          "resolved", "model"]):
        for row in batch.to_pylist():
            model = str(row.get("model") or "")
            target = None
            for pop, agg in aggs.items():
                if SS_MODEL_CLASS[pop] in model:
                    target = agg
                    break
            if target is None:
                continue
            target["n_in_file"] += 1
            target["models"][model] += 1
            res = row.get("resolved")
            if res is None:
                continue
            try:
                steps, tlevel = v4parse.parse_messages(row["messages"])
            except Exception:
                target["n_parse_fail"] += 1
                continue
            if len(steps) < 1:
                continue
            target["n_usable"] += 1
            target["outcome_values"][repr(bool(res))] += 1
            target["n_steps"].append(len(steps))
            if len(steps) >= 3:
                target["n_ge3"] += 1
            target["token_levels"][str(tlevel)] += 1
            tid, rule = v4parse.extract_task_id(row, "SS")
            if tid is not None:
                target["n_with_task"] += 1
                target["task_ids"].add(tid)
                target["task_rule"][rule] += 1
                target["group_n"][tid] += 1
                if not res:
                    target["group_fail"][tid] += 1


def agg_to_json(agg):
    steps = np.array(agg["n_steps"], dtype=float)
    return {"n_in_file": agg["n_in_file"], "n_usable": agg["n_usable"],
            "n_parse_fail": agg["n_parse_fail"],
            "outcome_values": dict(agg["outcome_values"]),
            "n_with_task": agg["n_with_task"],
            "n_distinct_tasks": len(agg["task_ids"]),
            "task_rule": dict(agg["task_rule"]),
            "median_n_steps": float(np.median(steps)) if len(steps) else None,
            "mean_n_steps": float(np.mean(steps)) if len(steps) else None,
            "step_cov_ge3": (agg["n_ge3"] / agg["n_usable"]
                             if agg["n_usable"] else None),
            "token_levels": dict(agg["token_levels"]),
            "models": dict(agg["models"])}


def run_pop(pop):
    fam = pop.split("-")[0]
    repo, rev = (CF_REPO, CF_REV) if fam == "CF" else (SS_REPO, SS_REV)
    split = POP_FILE_SPLIT[pop]
    prog_path = os.path.join(RES, f"census_progress_{pop}.json")
    done_files = []
    agg = blank_agg()
    if os.path.exists(prog_path):
        prog = json.load(open(prog_path))
        done_files = prog["done_files"]
        agg = blank_agg()
        saved = prog["agg"]
        agg.update({k: saved[k] for k in
                    ("n_in_file", "n_usable", "n_parse_fail",
                     "n_with_task", "n_ge3")})
        agg["outcome_values"] = Counter(saved["outcome_values"])
        agg["task_ids"] = set(saved["task_ids"])
        agg["task_rule"] = Counter(saved["task_rule"])
        agg["n_steps"] = saved["n_steps"]
        agg["token_levels"] = Counter(saved["token_levels"])
        agg["models"] = Counter(saved["models"])
        agg["group_n"] = Counter(saved.get("group_n", {}))
        agg["group_fail"] = Counter(saved.get("group_fail", {}))
    files = list_files(repo, rev, split)
    print(f"{pop}: {len(files)} files, {len(done_files)} already done",
          flush=True)
    for f in files:
        if f in done_files:
            continue
        local = hf_hub_download(repo, f, repo_type="dataset",
                                revision=rev, local_dir=CACHE)
        fagg = blank_agg()
        if fam == "CF":
            process_file_cf(local, fagg)
            agg_add_file(agg, fagg)
        else:
            # SS files serve two populations; process this pop's slice
            # by filtering inside a single-population shim.
            shim = {pop: fagg}
            process_file_ss(local, shim)
            agg_add_file(agg, fagg)
        if fagg["n_in_file"] == 0:
            print(f"{pop}: WARNING file yielded 0 rows: {f}", flush=True)
        try:
            os.remove(local)
        except OSError:
            pass
        done_files.append(f)
        saved = {"n_in_file": agg["n_in_file"], "n_usable": agg["n_usable"],
                 "n_parse_fail": agg["n_parse_fail"],
                 "n_with_task": agg["n_with_task"], "n_ge3": agg["n_ge3"],
                 "outcome_values": dict(agg["outcome_values"]),
                 "task_ids": sorted(agg["task_ids"]),
                 "task_rule": dict(agg["task_rule"]),
                 "n_steps": agg["n_steps"],
                 "token_levels": dict(agg["token_levels"]),
                 "models": dict(agg["models"]),
                 "group_n": dict(agg["group_n"]),
                 "group_fail": dict(agg["group_fail"])}
        json.dump({"done_files": done_files, "agg": saved},
                  open(prog_path, "w"))
        print(f"{pop}: file done {f} usable={agg['n_usable']}", flush=True)
    json.dump(dict(agg["group_n"]),
              open(os.path.join(RES, f"groups_{pop}.json"), "w"))
    json.dump({t: [agg["group_n"][t], agg["group_fail"][t]]
               for t in agg["group_n"]},
              open(os.path.join(RES, f"groupcomp_{pop}.json"), "w"))
    out = agg_to_json(agg)
    out["population"] = pop
    out["artefact"] = repo
    out["revision"] = rev
    out["files"] = files
    json.dump(out, open(os.path.join(RES, f"census_{pop}.json"), "w"),
              indent=1)
    print(f"{pop}: CENSUS COMPLETE usable={out['n_usable']} "
          f"tasks={out['n_distinct_tasks']}", flush=True)
    return out


if __name__ == "__main__":
    pops = sys.argv[1:]
    if not pops:
        print("usage: run_census_v4.py POP [POP ...]")
        sys.exit(2)
    for p in pops:
        run_pop(p)
