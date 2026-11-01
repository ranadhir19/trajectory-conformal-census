#!/usr/bin/env python3
"""validate.py — verification harness for the trajectory-conformal
census deposit (companion to the manuscript "No Eligible
Populations", TMLR submission).

Stages:
  1. compile check of every deposited Python file;
  2. import check of the deposited library modules (the two census
     runner scripts are compile-checked only: importing them would
     create their results cache directory, and executing them is
     Tier 2 in README.md);
  3. registration hash chains (PREREGISTRATION_V3.sha256 in full;
     PREREGISTRATION_V4.sha256 non-registration members — the
     EXPERIMENTS_V4.md entry is reported as information, since its
     Part II execution record was appended under the registration's
     own §R13 rule after the freeze hash was taken);
  4. results reproduction: every headline census number (the
     332,499 total, per-population usable counts, the CoderForge
     -1.0 counts, the SWE-smith base failure rates, the exploratory
     CoderForge counterfactual shares) recomputed from the
     deposited JSON records, with the deposited frozen-rule
     functions (v4lib.binarise_cf_reward / binarise_ss_resolved /
     eligibility / programme_verdict) probed on the deposited data;
  5. coverage statement (printed, not a check).

Run: python3 validate.py   (numpy, scipy, scikit-learn required —
see requirements.txt). Exit code 0 iff every check PASSes.
"""

import hashlib
import json
import os
import py_compile
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "code"))

FAILURES = []


def check(stage, name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        FAILURES.append(f"stage {stage}: {name}")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stage_compile():
    print("STAGE 1: compile checks")
    files = [os.path.join(ROOT, "validate.py")]
    code_dir = os.path.join(ROOT, "code")
    files += [os.path.join(code_dir, f) for f in sorted(os.listdir(code_dir))
              if f.endswith(".py")]
    for path in files:
        try:
            py_compile.compile(path, doraise=True)
            check(1, f"compiles: {os.path.relpath(path, ROOT)}", True)
        except Exception as e:  # pragma: no cover
            check(1, f"compiles: {os.path.relpath(path, ROOT)}", False, str(e))


def stage_imports():
    print("STAGE 2: import checks (library modules)")
    mods = {}
    for name in ("tcrc", "synth", "v4lib", "v4parse", "v4features",
                 "v4signal"):
        try:
            mods[name] = __import__(name)
            check(2, f"import {name}", True)
        except Exception as e:  # pragma: no cover
            check(2, f"import {name}", False, str(e))
    return mods


def _hash_entries(fname):
    entries = {}
    with open(os.path.join(ROOT, fname)) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, name = line.split(None, 1)
            entries[name.strip()] = digest
    return entries


def stage_hashes():
    print("STAGE 3: registration hash chains")
    v3 = _hash_entries("PREREGISTRATION_V3.sha256")
    for name, digest in sorted(v3.items()):
        got = sha256_of(os.path.join(ROOT, name))
        check(3, f"V3 chain: {name}", got == digest,
              f"sha256 {got[:12]}…")
    v4 = _hash_entries("PREREGISTRATION_V4.sha256")
    for name, digest in sorted(v4.items()):
        got = sha256_of(os.path.join(ROOT, name))
        if name == "EXPERIMENTS_V4.md":
            print(f"  [INFO] V4 chain: {name} — current sha256 "
                  f"{got[:12]}… differs from the freeze record "
                  f"{digest[:12]}…: EXPECTED. Part II (the execution "
                  "record) was appended under the registration's own "
                  "§R13 rule; Part I was hash-verified at the "
                  "pre-execution Gate 9 check. Not a check.")
        else:
            check(3, f"V4 chain: {name}", got == digest,
                  f"sha256 {got[:12]}…")


# Tester-verified headline values (REPORT.md Table, §2;
# TESTING_REPORT_V4_RESULTS.md verdict chain).
EXPECTED_USABLE = {"CF-1": 77169, "CF-2": 148001, "CF-3": 32964,
                   "SS-1": 17715, "SS-2": 18457, "SS-3": 18457,
                   "SS-4": 5751, "SS-5": 7091, "SS-6": 6894}
EXPECTED_TOTAL = 332499
CF_MINUS1 = {"CF-1": 255, "CF-2": 367, "CF-3": 278}
CF_EXPL_EXCL = {"CF-1": 0.4183, "CF-2": 0.3938, "CF-3": 0.3605}
CF_EXPL_ASFAIL = {"CF-1": 0.4202, "CF-2": 0.3953, "CF-3": 0.3659}
SS_BASE_FAILURE = {"SS-1": 0.6102, "SS-2": 0.5447, "SS-3": 0.5447,
                   "SS-4": 0.5921, "SS-5": 0.5875, "SS-6": 0.5863}
POPS = sorted(EXPECTED_USABLE)


def _load(pop, kind):
    path = os.path.join(ROOT, "results", "v4", f"{kind}_{pop}.json")
    with open(path) as f:
        return json.load(f)


def stage_results(v4lib):
    print("STAGE 4: results reproduction from deposited JSONs")
    total = 0
    for pop in POPS:
        try:
            census = _load(pop, "census")
            result = _load(pop, "result")
            check(4, f"{pop}: census + result records present", True)
        except Exception as e:  # pragma: no cover
            check(4, f"{pop}: census + result records present", False, str(e))
            continue
        usable = census["n_usable"]
        total += result["census"]["n_usable"]
        check(4, f"{pop}: usable count",
              usable == EXPECTED_USABLE[pop]
              and result["census"]["n_usable"] == usable,
              f"= {usable}")
        check(4, f"{pop}: zero parse failures",
              census["n_parse_fail"] == 0
              and result["census"]["n_parse_fail"] == 0)
        ov = census["outcome_values"]
        if pop.startswith("CF"):
            vals = {float(k): v for k, v in ov.items()}
            check(4, f"{pop}: -1.0 count",
                  vals.get(-1.0) == CF_MINUS1[pop],
                  f"= {vals.get(-1.0)}")
            rule, _ = v4lib.binarise_cf_reward(set(vals))
            check(4, f"{pop}: frozen binarisation on observed values",
                  rule == "ineligible"
                  and result["cf_reward_rule"] == "ineligible")
            check(4, f"{pop}: verdict is clause 3",
                  "clause 3" in result["verdict"])
            n_fail, n_pass, n_neg = vals[0.0], vals[1.0], vals[-1.0]
            excl = n_fail / (n_fail + n_pass)
            asfail = (n_fail + n_neg) / (n_fail + n_pass + n_neg)
            check(4, f"{pop}: exploratory share excl. -1.0",
                  abs(excl - CF_EXPL_EXCL[pop]) < 1e-4,
                  f"= {excl:.4f} (paper: {CF_EXPL_EXCL[pop]})")
            check(4, f"{pop}: exploratory share -1.0-as-failure",
                  abs(asfail - CF_EXPL_ASFAIL[pop]) < 1e-4,
                  f"= {asfail:.4f} (paper: {CF_EXPL_ASFAIL[pop]})")
        else:
            n_true, n_false = ov["True"], ov["False"]
            bf = n_false / (n_true + n_false)
            check(4, f"{pop}: base failure recomputed",
                  abs(bf - result["base_failure"]) < 1e-9
                  and round(bf, 4) == SS_BASE_FAILURE[pop],
                  f"= {bf:.4f}")
            check(4, f"{pop}: base failure above the 0.50 ceiling",
                  bf > 0.50)
            rule, _ = v4lib.binarise_ss_resolved([True, False])
            dummy = {"gate": (0, 0), "cal": (0, 0), "test": (0, 0)}
            check(4, f"{pop}: frozen rules bind at leg (b)",
                  rule == "boolean"
                  and result["ss_resolved_rule"] == "boolean"
                  and v4lib.eligibility(bf, usable, dummy)
                  == "ineligible:leg-b")
    check(4, "programme total over the nine populations",
          total == EXPECTED_TOTAL, f"= {total}")
    check(4, "§R8 row 1: programme_verdict(NO-TEST, NO-TEST)",
          v4lib.programme_verdict("NO-TEST", "NO-TEST") == "H-DATA")
    rule1, _ = v4lib.binarise_cf_reward({0.0, 1.0})
    rule2, _ = v4lib.binarise_cf_reward({0.0, 0.5, 1.0})
    check(4, "binarisation sanity: {0,1} -> clause 1, [0,1] -> clause 2",
          rule1 == "clause1" and rule2 == "clause2")


def stage_coverage():
    print("STAGE 5: coverage statement (informational)")
    print("""  This harness verifies the deposit's INTERNAL consistency:
  the code compiles and imports, the freeze hash chains verify as
  documented, and every headline census number in the paper
  recomputes from the deposited JSON records through the deposited
  frozen-rule functions. It does NOT re-run the census from the raw
  Hugging Face artefacts (Tier 2, README.md — network, pinned
  revisions), and it does not re-run the programme's synthetic
  anchor suite: that is the programme harness's 48-check run, whose
  log is deposited as results_validate_v4_stage6.log. The two
  census runner scripts are compile-checked, not executed.""")


def main():
    stage_compile()
    mods = stage_imports()
    stage_hashes()
    if "v4lib" in mods and mods["v4lib"] is not None:
        stage_results(mods["v4lib"])
    else:  # pragma: no cover
        check(4, "results reproduction (needs v4lib import)", False)
    stage_coverage()
    if FAILURES:
        print(f"OVERALL: FAIL ({len(FAILURES)} failed checks)")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print("OVERALL: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
