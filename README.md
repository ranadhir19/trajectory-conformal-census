# No Eligible Populations — reproducibility deposit

**A pre-registered feasibility census for trajectory-level conformal
risk control on public agent traces.**

This repository is the public reproducibility deposit for the
manuscript *"No Eligible Populations: A Pre-Registered Feasibility
Census for Trajectory-Level Conformal Risk Control on Public Agent
Traces"* (Ranadhir Ghosh, FIS Global; submitted to TMLR). It contains
the frozen pre-registrations, the census code, the census records,
and the independent tester reports behind the paper, so that every
number in the paper can be recomputed from what is here.

## What the census found — H-DATA

Under a pre-registration frozen before any census quantity existed
(`EXPERIMENTS_V4.md`, frozen 2026-10-31T17:33:20Z), all nine public
software-engineering agent populations that had survived a
counted-evidence screen were censused in full — **332,499
trajectories, zero parse failures** — and **no population was
eligible** for confirmatory trajectory-level conformal risk control.
The programme verdict, by the registration's own decision table
(§R8, row 1: both families NO-TEST), is **H-DATA**. No eligibility
criterion was relaxed at any point. Two distinct data-side barriers
bind:

1. **Outcome encoding (CoderForge family, CF-1/2/3).** The
   `reward` field of `togethercomputer/CoderForge-Preview` takes
   three values — 1.0, 0.0, and **−1.0** — and no definition of
   −1.0 appears anywhere in the artefact documentation. It occurs
   on 255 / 367 / 278 rows (0.33% / 0.25% / 0.84%) of the three
   source populations. The registration's outcome binarisation was
   frozen as a deterministic function of the observed value set
   with no clause covering values outside [0, 1] (§R3(v),
   clause 3), precisely so that an undocumented value could not be
   interpreted post hoc. All three populations are therefore
   census-ineligible. (Exploratory counterfactuals, reported in
   the paper and recomputed by `validate.py` from the deposited
   records: excluding the −1.0 rows, the failure shares are
   0.4183 / 0.3938 / 0.3605; counting −1.0 as failure gives
   0.4202 / 0.3953 / 0.3659 — the same band assignment either way.
   For CF-2 and CF-3 the binding barrier is the encoding, not the
   band.)
2. **Base-rate concentration (SWE-smith family, SS-1…SS-6).** All
   six Claude (format × model) populations of
   `SWE-bench/SWE-smith-trajectories` have base failure rates of
   0.5447–0.6102, above the registered 0.50 ceiling (leg (b)).
   Leg (a) (≥ 800 usable trajectories) passed for all six; leg (b)
   alone binds.

Because no population was eligible, no gate, split, or test
quantity was ever realised: the confirmatory programme did not
run, and the census is the finding. The guarantee machinery itself
was verified separately on synthetic anchors with planted signal
(see `REPORT.md` §3 and `results_validate_v4_stage6.log`); it is
not the bottleneck this census hit.

## Contents

| Path | What it is |
|---|---|
| `EXPERIMENTS_V4.md` | The frozen V4 pre-registration (Part I) and its execution record (Part II, appended under the registration's own §R13 rule) |
| `EXPERIMENTS_V3.md` | The predecessor V3 registration (byte-identical to its freeze; its Gate 9 route-back motivated V4) |
| `SOLUTION_DESIGN_V3.md`, `COUNTING_PASS_O3.md` | The design executed by V3/V4 and the counted-evidence screen that selected the nine populations; both are members of the recorded hash chains |
| `PREREGISTRATION_V3.sha256`, `PREREGISTRATION_V4.sha256` | The freeze hash records |
| `code/` | The census code: `run_census_v4.py` / `run_population_v4.py` (entry points), `v4lib.py` / `v4parse.py` / `v4features.py` / `v4signal.py` (V4 library), `tcrc.py` / `synth.py` (the v1 library the V4 code builds on, unchanged), `BUILD_LOG_V4.md` (build log with the pinned environment) |
| `results/v4/census_*.json` | Per-population census records (9) |
| `results/v4/result_*.json` | Per-population formal result records with verdicts (9) |
| `TESTING_REPORT_V4_DESIGN.md` | Gate 9 fresh-tester report on the frozen V4 registration (Design 7/10; Editor Screen pre-score 9/12 LOW at TMLR) |
| `TESTING_REPORT_V4_RESULTS.md` | Stage 8 fresh-tester report on the realised results (verdict chain verified; Quality 6/10; Editor Screen 7/12 MEDIUM at TMLR) |
| `REPORT.md` | The programme's final report, including falsifier bookkeeping and the decision record |
| `results_validate_v4_stage6.log` | The programme harness run on record (validate.py, 48 checks, OVERALL PASS) from the Stage 6 build |
| `paper/manuscript.tex`, `paper/manuscript.pdf` | The manuscript source and compiled PDF (8 pages) |
| `validate.py` | This deposit's verification harness (see below) |
| `requirements.txt` | The pinned programme environment |

## Reproducing

**Tier 1 — verify the deposit (no network, under a minute).**

```bash
pip install -r requirements.txt   # or use any env with numpy/scipy/scikit-learn
python3 validate.py
```

`validate.py` compiles and imports the deposited code, verifies
the registration hash chains, and recomputes every headline census
number — the 332,499 total, each population's usable count, the
−1.0 counts, the SWE-smith base failure rates, the exploratory
CoderForge counterfactuals — from the deposited JSON records,
probing the deposited frozen-rule functions themselves
(`binarise_cf_reward` on the observed value sets returns clause-3
ineligibility; `programme_verdict("NO-TEST", "NO-TEST")` returns
`H-DATA`). It prints an honest coverage statement: what it does
not check is a re-census from the raw artefacts (Tier 2) and the
full synthetic-anchor suite (that is the programme harness's
48-check run, whose log is deposited).

**Tier 2 — re-run the census from the raw artefacts (network).**

```bash
python3 code/run_census_v4.py        # per-population census
python3 code/run_population_v4.py    # formal result records
```

The runners download the two artefacts from Hugging Face at the
pinned revisions recorded in the census JSONs
(CoderForge-Preview `060fca96…`; SWE-smith-trajectories
`08e109b4…`) and write to `results/v4/`. The CoderForge artefact is
large (224 files); budget download time and disk accordingly. The
runners were executed under the pinned environment in
`requirements.txt` / `code/BUILD_LOG_V4.md`.

## Freeze integrity, stated precisely

`sha256sum -c PREREGISTRATION_V3.sha256` verifies in full.
In `PREREGISTRATION_V4.sha256`, the two non-registration members
(`SOLUTION_DESIGN_V3.md`, `COUNTING_PASS_O3.md`) verify;
`EXPERIMENTS_V4.md` itself no longer matches its freeze hash
because its Part II execution record was appended after execution
under the registration's own §R13 rule — Part I was hash-verified
at the pre-execution Gate 9 check. `validate.py` checks exactly
this and reports it in exactly these terms.

## Data provenance and licences

This deposit contains **no trajectory data** — only aggregate
census records (counts, outcome-value tallies, rates). The
underlying corpora are not redistributed here.

- **CoderForge-Preview** — `togethercomputer/CoderForge-Preview`
  (Hugging Face), revision `060fca96cf723b2ebab3181e9e59fafd273df3cb`.
  OpenHands trajectories driven by Qwen3-Coder-480B over tasks
  from three sources (SWE_Rebench, SWE_Smith, R2E_Gym). The
  dataset card states no dataset-level licence; a per-row
  `license` field is present in the artefact. Documented by Hu &
  Chong, *SWE-Critix*, arXiv:2610.13356.
- **SWE-smith trajectories** — `SWE-bench/SWE-smith-trajectories`
  (Hugging Face), revision `08e109b4a59eaeebf80e4675cd125d42e7ac99a4`.
  SWE-agent trajectories; licence **MIT** per the dataset card.

## Scores, on the record

The paper is a negative-result census and is presented as one.
Independent fresh-tester scores: Gate 9 design stage — Design
Quality 7/10, Editor Screen 9/12 LOW at TMLR; Stage 8 on the
realised results — **Quality 6/10** (below the programme's 8/10
bar), **Editor Screen 7/12 MEDIUM** at TMLR. The author's decision
to submit on these scores, with the scores on record, is
documented in `REPORT.md` §11 and in the programme's `STATE.md`.

## Author

Ranadhir Ghosh (FIS Global), sole author. The code and records in
this deposit are the author's own work products of the programme
described above.
