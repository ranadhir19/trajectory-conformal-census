# SOLUTION DESIGN V3 — Area 2: Trajectory-Level Conformal Risk Control
## Stage 5 revision R2 after Gate 9 route-back (defects D1–D6)

**Stage:** 5 (Solutioning) — SECOND RETURN, under FRAMEWORK's loop rule
(a failed check routes back to the responsible stage — never forward
on hope).
**Route-back basis:** `TESTING_REPORT_V2_DESIGN.md` (Gate 9 fresh
tester, 2026-10-31): Design Quality pre-score **5/10** (< 6) and
Editor Screen pre-score **5/12 HIGH** at JMLR — both route-back rules
fired. Its defects **D1–D6** are this revision's specification; §9 of
this document maps each defect to its fix.
**V2 status:** `SOLUTION_DESIGN_V2.md` and `EXPERIMENTS_V2.md` and
their freeze (`PREREGISTRATION_V2.sha256`, 2026-10-31T15:38:14Z) stay
on record **UNTOUCHED**. This is a new design (V3), not an edit of V2.
The v1 registration and pilot verdict likewise stand exactly as
recorded.
**Scope of this stage:** DESIGN ONLY. No coding, no experiments, no
gate evaluations, no signal computation, and no base-rate computation
from trace outcomes. The only data contact in this pass is
**metadata-level counting** (trajectory / task / agent / run counts
and file inventories — never outcome values), plus base rates that
are **documented facts** in published sources, cited as such.
**Date:** 2026-10-31. **Discipline:** sole author; zero-fee venues;
$0 autonomous spend.

---

## 0. Headline outcome of this revision

**H-DATA at the design stage.** The corrected floor (§2) requires
**≥ 800 usable trajectories in one exchangeable population** per
confirmatory corpus (fit 320 / gate 160 / calibration 160 / test 160
under the D3 split-hygiene repair). The pre-freeze feasibility pass
that V2 skipped was run first this time (§3, counted before anything
was frozen): **no public corpus at $0 spend survives** — every
candidate fails on counted n in a single population, on documented
base-rate facts, on outcome-filtering by construction, or on absent
step-level traces (§3, §4). Per the standing rule, the floor and the
criterion were **not** lowered to fit the data. Consequently:

- **No `EXPERIMENTS_V3.md` pre-registration is frozen.** There is
  nothing honest to freeze it over.
- The D2–D6 design repairs are nevertheless fully specified (§5), so
  the design is activation-ready: if a corpus ever clears §3's table
  at the §2 floor, the registration can be written from §5 without
  further design work, and Gate 9 re-run on this V3 design is the
  next step either way (§8).
- The decision this creates belongs to Ranadhir; §7 prices the
  options.

---

## 1. The order V2 got wrong, fixed (D1 — procedural)

V2 froze the floor and the corpora together, uncounted. V3 derives
and freezes in exactly this order, and §3's table was produced
**before** any V3 choice that depends on it:

1. **Criterion first** — the resolution the calibration must achieve
   (§2; unchanged from V2 §5.1: a corpus must in principle be able
   to distinguish risk at α from risk at α/2 or 3α/2).
2. **Floor second** — the smallest split sizes meeting the criterion
   under **one** stated method (exact Clopper–Pearson; §2), plus the
   split-hygiene cost of D3 (§5.2) counted into the total.
3. **Corpora third** — a corpus enters the design only if it was
   **counted** in §3's feasibility pass and the §2 arithmetic is
   possible for it. A corpus that was not counted does not enter,
   however promising its reputation.

This is the area's own pre-freeze gate (`INTAKE_MEMO.md` §3:
"feasibility-of-input checks (signal existence, corpus n, base
rate) are pre-freeze gates for any future pre-registration in this
area"), applied this time.

---

## 2. Corrected n-floor — exact Clopper–Pearson, one method (D6)

**Criterion (unchanged from V2, now evaluated under one method):**
the two-sided 95% confidence interval for the risk estimate at
p = α = 0.10 must have half-width ≤ α/2 = 0.05.

**Method (the only one used in this section):** exact
Clopper–Pearson interval for Binomial(n, k), evaluated at the
realisable observed count k = n/10 (n a multiple of 10, so the
observed rate is exactly 0.10). Half-width = (upper − lower)/2.

| n | k | Exact CP 95% interval | Half-width | Criterion |
|---|---|---|---|---|
| 139 (V2 normal-approx floor) | 14* | ≈ [0.056, 0.163] | ≈ 0.054 | FAIL |
| 150 (V2 frozen floor) | 15 | [0.0571, 0.1596] | **0.0513** | FAIL |
| 159 | 16 | [0.0586, 0.1583] | 0.0498 | pass (smallest integer n at k = round(0.1n)) |
| **160** | **16** | **[0.0583, 0.1573]** | **0.0495** | **PASS — frozen** |

*V2's own reported value at n = 139 (k = 14, rate 0.101). The Gate 9
tester independently recomputed the n = 139 / 150 half-widths
(0.0535 / 0.0513); this pass recomputed n = 150 / 159 / 160 with the
same exact method (beta-quantile CP bounds) and agrees.

**Frozen floor (V3): n_cal ≥ 160 AND n_test ≥ 160 per corpus.**
n = 160 is frozen rather than 159 because the criterion is defined
at an exactly-realisable observed rate (k = n/10); 159 is recorded
so the choice is seen to cost one trajectory, not to hide one. The
CRC finite-sample correction at n = 160 is 1/(n+1) = 0.0062 ≈ α/16,
still fine enough not to dominate the threshold (V2 §5.1's reasoning,
carried).

**Split-hygiene cost (D3, §5.2) counted into the total.** V3 uses
four disjoint roles — fit / gate / calibration / test — so the gate
no longer shares the calibration split. The gate split carries the
same resolution floor (n_gate ≥ 160: it must estimate an AUC
difference with a bootstrap CI, a measurement of the same order as
the calibration it protects), and the fit split is sized by the D4
feature budget (§5.3) at n_fit ≥ 320. Frozen proportions:
**fit 40% / gate 20% / calibration 20% / test 20%**, giving the
per-corpus usable floor:

> **≥ 800 usable trajectories per confirmatory corpus**
> (fit 320, gate 160, calibration 160, test 160 at the floor).

**Class-count rule (carried from V2, interaction now stated).**
Each of gate / calibration / test must contain ≥ 40 successes and
≥ 40 failures (V2 required this of calibration; V3 extends it to the
gate split, which cannot judge ranking on a one-class sample). At
n = 160 per split, ≥ 40 failures means a realised per-split failure
fraction ≥ 0.25; combined with the §5.5 eligibility band
[0.10, 0.40], the **operative confirmatory window is a realised
base failure rate in [0.25, 0.40]** — recorded here so no future
reader mistakes the band's low end for reachable at the floor.
Corpora with larger n relax the 0.25 edge proportionally
(40/n_split); the band itself does not move.

**What did not change:** α = 0.10 primary; frontier grid
{0.05, 0.10, 0.20}; δ = 0.05; ≤ 40% abstention ceiling; binary
trajectory failure under unconditional accepted-risk loss; the
perfect-ranker abstention floor p_fail − α and the eligibility
band derived from it (§5.5). No v1 or V2 bar is relaxed anywhere in
this document (the Gate 9 tester's §4d verification list was
re-checked line by line against this section and §5).

---

## 3. Feasibility first — the counted table (D1)

**Counting discipline.** Counts below come from (a) artefacts on
disk in this program (direct counts, metadata fields only), or
(b) documented counts in the source's own publication / dataset
card (labelled DOCUMENTED, with the source named). Outcome values
were never read, parsed, or summarised by this pass, except where a
base rate is itself a documented published fact (§3.3). "Split
possible?" is judged against §2: ≥ 800 usable trajectories in **one
exchangeable population** (one benchmark × one scaffold × one
model configuration, trajectories over distinct tasks — the unit
discipline of v1 §8 / design v1 §7), with the four-way split
arithmetically satisfiable.

### 3.1 HAL family (`agent-evals/hal_traces`, HF, pinned revision `1bf4166d052cdd3445127e17c15139cbb5505ca5`, 2025-10-08)

Population inventory counted from the flagship program's frozen
population file (`flagship_work/data/hal_population_frozen.json`,
frozen mechanically and pre-outcome at the pinned revision):
**280 run zips / 81.4 GB** across 9 benchmark families. The V2
assumption that "full" variants exist in this release is **false**:
there is no `swebench_verified` (full) run and no `corebench`
(full) run in the population — only the mini / hard variants.

| HAL family | Run zips (counted) | Trajectories per single run | Source of per-run count | ≥ 800 in one population? |
|---|---|---|---|---|
| swebench_verified_mini | 37 | ≤ 50 (50 distinct task ids in logging; only 18 top-level eval entries — discrepancy unresolved at metadata level, Gate 9 report §2) | DIRECT (Gate 9 tester count of the local zip) | **NO** (~6% of floor) |
| corebench_hard | 54 | 45 (45 eval entries = 45 distinct task ids, consistent) | DIRECT (Gate 9 tester count) | **NO** |
| taubench_airline | 35 | 50 | DIRECT (v1 pilot, on record) | **NO** — and excluded on principle (§5.6) regardless |
| gaia | 34 | 165 (HAL evaluates the GAIA validation split: 165 questions, levels 53/86/26) | DOCUMENTED (HAL GAIA leaderboard materials; GAIA validation composition) | **NO** |
| usaco | 15 | 307 (USACO benchmark task count) | DOCUMENTED (USACO benchmark paper) | **NO** — largest verified HAL family, still 38% of floor |
| scicode | 37 | 80 main problems (338 sub-problems; trajectory unit = main problem) | DOCUMENTED (SciCode paper) | **NO** |
| assistantbench | 34 | not verified in this pass | — | **NOT ENTERED** (uncounted at task level) |
| scienceagentbench | 21 | not verified in this pass | — | **NOT ENTERED** |
| seeact (Online Mind2Web) | 13 | not verified in this pass | — | **NOT ENTERED** |

**Pooled-across-runs construction — considered and rejected, with
the arithmetic shown.** Pooling all runs of one family multiplies
trajectories (gaia 34 × 165 = 5,610; corebench_hard 54 × 45 = 2,430;
swebench_verified_mini 37 × 50 = 1,850; taubench_airline 35 × 50 =
1,750) but the trajectories are **repeated attempts on the same
165 / 45 / 50 / 50 tasks by different models/scaffolds** — not one
exchangeable population (packet §1.6 risk #4, named in 2026-10-30).
The two honest repairs both fail the floor: (i) split by task group
(all runs of a task in one split) makes the independent-unit count
the **task** count (165 / 45 / 50 / 50), all < 800 and indeed
< 160 per split role; (ii) split by trajectory lets the same task
appear in fit and test under different models, so the head can
memorise task identity (hashed n-grams of the task text) and the
gate would certify task-difficulty memorisation, not step-risk
ranking — exactly the leakage the split discipline exists to
prevent. Pooling is therefore not a corpus; it is a different
method question (cluster/group-level calibration), priced as
option O2 in §7 for Ranadhir, not adopted here. The Gate 9 tester's
suggestion of pooling is answered by this paragraph: it was
examined, and it does not survive the area's own split discipline.

**Full-variant check (the tasking's explicit example).** Full
SWE-bench Verified (500 tasks, DOCUMENTED) and full CORE-Bench
(270 tasks, DOCUMENTED) exist as benchmarks, but **no HAL run on
either full variant exists in the pinned population** (only mini /
hard were ever run by HAL). Even if one did, 500 and 270 are both
< 800 — a full-variant HAL run would still fail the V3 floor,
though it would have passed V2's 429. This is the honest cost of
the D3 + D6 repairs, stated rather than negotiated away.

### 3.2 METR run data (packet Corpus C)

| Candidate | Counted | Structure | Split possible? |
|---|---|---|---|
| METR `eval-analysis-public` run files, local copies in `flagship_work/data/metr/` (`runs_v1_0.jsonl`, `runs_v1_1.jsonl`; repository pinned at the flagship freeze) | v1.0: **41,629 run records**, 170 distinct task_ids, 50 task families, 35 models; v1.1: **24,008 run records**, 228 distinct task_ids, 79 task families, 21 models (DIRECT counts of metadata fields only: task_id, task_family, model, scaffold) | Run-level **summary** records (score, tokens, cost, timing fields). **No step-level transcripts** in this artefact | **NO** — two independent reasons: (i) the Approach-C signal is a per-step scorer; a corpus without steps cannot featurise it (v1 §7.2 rung-3 degradation would leave trajectory-level features only, on a corpus whose runs are repeated attempts clustered on ≤ 228 tasks); (ii) clustered by task exactly as in §3.1's rejected pooling. METR transcripts (Vivaria logs) are not part of the public artefact counted here |

### 3.3 Large public SWE-agent trajectory corpora (non-HAL)

| Candidate | Counted n (provenance) | Population | Verdict |
|---|---|---|---|
| `nebius/SWE-agent-trajectories` (HF, CC-BY-4.0) | **80,036 trajectories** (DOCUMENTED, dataset card); 3 model_name values; tasks from `nebius/SWE-bench-extra` (6,411 instances, DOCUMENTED) + SWE-bench dev split; per-trajectory step lists and a binary target field present | One scaffold (SWE-agent), 3 open-weight action-generator models | **n arithmetic: PASS. NOT FROZEN — documented base-rate evidence.** The source's own comparison table (in `nebius/SWE-rebench-openhands-trajectories` card) records **838 resolved** for this dataset against 80,036 trajectories: on any reading of that documented count, success is a small minority and failure sits far above the band's 0.50 descriptive ceiling. Freezing it as confirmatory would repeat D1 in the base-rate dimension — a foreseeably ineligible corpus. Excluded on documented facts, not on a computed outcome |
| `nebius/SWE-rebench-openhands-trajectories` (HF) | **67.1k rows** (DOCUMENTED, dataset card); single model (Qwen3-Coder-480B-A35B-Instruct) × single scaffold (OpenHands v0.54.0); step-by-step traces + resolved field | Cleanest population definition of the large corpora | **n arithmetic: PASS. NOT FROZEN — same documented reason:** the card's own table records **3,792 resolved** against 67.1k trajectories; failure is foreseeably ≥ 0.50 by a wide margin. Excluded on documented facts |
| Scale-SWE trajectories (AweAI-Team; arXiv:2602.09892) | **71,498 trajectories** (DOCUMENTED, paper) from 25,000 instances × 5 sampling trials, DeepSeek-V3.2 | Single teacher model | **EXCLUDED BY CONSTRUCTION (documented):** the paper states a trajectory "was considered valid only if it culminated in a submission that passed all unit tests" — the released set is **success-filtered**; its base failure rate is ~0 by construction, outside the band at the low end and not a natural population at all |
| R2E-Gym SFT trajectories (`R2E-Gym/R2EGym-SFT-Trajectories`) | **3,321 trajectories from 2,048 unique task environments** (DOCUMENTED, R2E-Gym paper) | Single scaffold, Claude Sonnet 3.5 v2 | **EXCLUDED BY CONSTRUCTION (documented):** the paper states they collected "the **successful** agent trajectories" for SFT — success-filtered, same defect as Scale-SWE; n also < 800 after any honest accounting |
| SWE-Gym OpenHands sampled trajectories | **491 trajectories** (DOCUMENTED, SWE-Gym paper / comparison tables) | — | **EXCLUDED:** success-filtered SFT set and n < 800 |
| `nvidia/Open-SWE-Traces` | v2.0 subset **489k rows** (DOCUMENTED, dataset card) | Aggregate of multiple source datasets (incl. Scale-SWE), mixed scaffolds/models, per-row `resolved` field | **NOT ENTERED:** aggregate mixes outcome-filtered and natural sources; per-source-subset counts were not established in this pass, and an uncounted sub-population cannot be frozen ( §1 rule 3). Named as the first candidate for a future counting pass (§7, O3) |
| CoderForge trajectories (via SWE-Critix, arXiv:2610.13356) | Paper reports 258K trajectories (155K pass / 103K fail) over 51K issues — a documented failure fraction ≈ 0.40, at the band's edge | OpenHands × Qwen3-Coder-480B | **NOT ENTERED:** a public, downloadable artefact with a verified row count could not be established in this pass (no dataset card located). Uncounted ⇒ not frozen. Named in §7, O3 |
| SWE-smith trajectories (`SWE-bench/SWE-smith-trajectories`) | Resolved count 7,270 documented in the comparison table; **total trajectory count not established** in this pass | SWE-agent × Claude 3.7 / 3.5 Sonnet + GPT-4o | **NOT ENTERED** (total uncounted) |
| Own-lab traces (packet Corpus B) | Trajectory-level completeness **unverified** (packet §1.2 Needed #3 — the audit was never completed; systems log final results in many cases) | — | **NOT ENTERED** (uncounted). Generation is a different, priced study — §7, O1 |

### 3.4 What the table establishes

Every candidate fails at least one **structural** test that is
decidable without touching an outcome: single-population n at the
corrected floor (all HAL, METR transcripts), documented base-rate
ineligibility (both nebius corpora), outcome-filtering by
construction (Scale-SWE, R2E-Gym, SWE-Gym), absent step records
(METR summaries), or uncounted status (Open-SWE-Traces subsets,
CoderForge, SWE-smith trajectories, own-lab). No candidate's
failure requires lowering the floor to repair; each is a property
of the corpus, not of the criterion.

---

## 4. H-DATA verdict (the design-stage finding)

**Constraint.** A confirmatory test of the V2/V3 question — does a
learned per-step signal restore a non-vacuous trajectory-level CRC
frontier? — requires, per corpus, ≥ 800 usable trajectories from
one exchangeable population with a natural (unfiltered) outcome
distribution whose base failure rate can fall in [0.10, 0.40],
with step-level records for every trajectory (§§2, 5).

**Counted evidence.** §3: the largest verified single-population
public run is 307 trajectories (HAL USACO); HAL's full-variant
runs do not exist and would not reach 800 if they did; the only
corpora with n ≫ 800 are SWE-agent training collections that are
either success-filtered by construction or foreseeably
failure-dominated (≥ 0.50) on their own published counts; METR's
public artefact has runs but no steps; the remaining large
collections are uncounted at the population level and therefore
inadmissible under §1 rule 3.

**Verdict.** The V3 confirmatory study **cannot be populated at
$0 spend from currently public, counted artefacts**. This is
recorded as an H-DATA state at Stage 5 — the honest outcome the
V2 registration's §V7 reserved for its execution stage, reached
here at design time instead, which is precisely what the
pre-freeze feasibility gate (INTAKE_MEMO §3) was adopted to
achieve: the load-bearing input was checked before the freeze,
not discovered inside a frozen run. **No V3 pre-registration is
frozen, no floor or criterion was lowered, and no corpus was
admitted on reputation.** §7 gives Ranadhir the priced options;
§5 freezes the design machinery so that any option he picks that
produces a corpus activates a registration without redesign.

---

## 5. The design repairs (frozen as design, activated with a corpus)

Everything in this section is specified to the standard Gate 9
demanded of V2 — no load-bearing choice is left for a later stage
to invent — and takes effect only inside a future registration
written over a corpus that has cleared §3.

### 5.1 Prefix-scoring training protocol (D2 — fully specified)

V2 never said what the head trains on. V3 freezes it:

1. **Split first, expand second.** Trajectories are assigned to
   splits (§5.2) as whole trajectories. Only then is each fit-split
   trajectory expanded into **prefix examples**: one example per
   prefix length t = 1 … T_i (every step boundary; no subsampling
   grid, so training and scoring see the same t distribution).
2. **Training objects.** Example (i, t) has features computed
   **only from steps 1 … t** of trajectory i, and the trajectory's
   binary outcome as its label. The head therefore learns
   P(failure | prefix), which is exactly the quantity prefix
   scoring needs at every t. Train-on-full / apply-to-prefix is
   prohibited.
3. **n_steps under truncation.** The final trajectory length T_i
   is **future information at time t and is banned** from per-step
   features. The position/length features at prefix t are:
   current length t; running token total over steps ≤ t; running
   mean tokens/step; and t-relative running statistics only. (The
   trajectory-level baseline S_len uses final length, legitimately:
   it is a trajectory score evaluated after completion, at gate
   time — it is not an input to s(i, t).) Any feature whose value
   at t requires a step > t — including V2's "token outliers within
   the trajectory" computed on the full trajectory — is either
   recomputed on the running prefix (running median/MAD over
   steps ≤ t, frozen) or dropped; the frozen feature list in
   §5.3 marks each feature PREFIX-SAFE or TRAJECTORY-ONLY, and
   TRAJECTORY-ONLY features never enter the head.
4. **Weighting.** Prefix examples of trajectory i carry weight
   1/T_i, so every trajectory contributes total weight 1 to the
   fit regardless of length (long trajectories must not dominate
   the loss merely by having more prefixes).
5. **Heads and stacking.** Two base heads on the identical prefix
   example set: (i) L2 logistic regression, C = 1.0; (ii)
   gradient-boosted trees, max_depth = 3, 100 trees,
   learning_rate = 0.05, min_samples_leaf = 20 (sized in §5.3).
   Stacking: 5-fold cross-fitting **by whole trajectory** inside
   the fit split (seed §5.7); out-of-fold prefix scores from both
   heads train a logistic meta-learner (L2, C = 1.0, intercept
   included). The meta-learner and both heads are then refit /
   retained per the frozen rule: base heads are refit on the full
   fit split; the meta-learner is **not** refit (it is trained on
   out-of-fold scores only, so its inputs stay honest).
6. **Scoring.** For any trajectory in any split, s(i, t) =
   meta-learner output on prefix-(i, t) features, for every
   t = 1 … T_i. Aggregation is V2's, unchanged: primary
   S_haz = 1 − Π_t (1 − s(i, t)); descriptive S_max, S_mean.
7. **Hygiene.** Gate / calibration / test labels are never used in
   fitting, stacking, feature capping, or any selection. Prefix
   examples never straddle splits (rule 1). The v1 leakage guard
   (features read steps only, never the outcome or post-outcome
   records) carries over and is strengthened by rule 3.

### 5.2 Split hygiene — gate and threshold never share data (D3)

1. **Four disjoint splits** by whole trajectory, stratified by
   outcome: **fit 40% / gate 20% / calibration 20% / test 20%**
   (seed §5.7). The **gate is evaluated on the gate split only**;
   the CRC threshold λ̂ is selected on the **calibration split
   only**; the two splits share no trajectory.
2. **Why this repairs the guarantee.** CRC's finite-sample
   statement covers a score fixed independently of the calibration
   sample. Under V2, the gate event {AUC ≥ 0.65 ∧ ΔAUC ≥ +0.10 ∧
   CI excludes 0} was measurable w.r.t. the same sample that chose
   λ̂, making the gated pipeline's guarantee a selection-conditioned
   claim the design did not state. Under V3 the gate event is
   measurable w.r.t. fit + gate splits, which are **independent of
   the calibration and test splits** (disjoint draws from the same
   population). Conditioning on an independent event does not alter
   the calibration sample's distribution, so the CRC statement for
   the gated pipeline is the **unconditional** one, exactly as the
   design claims — and the claim is now true as stated, not
   approximately. This paragraph is part of the frozen design: any
   future change that lets gate information touch calibration
   re-opens the conditioning and must re-state the guarantee as
   conditional, on the record.
3. **Cost, counted.** The repair is why §2's floor is 800 and not
   458: gate 160 + calibration 160 + test 160 at 20% each, fit 320
   at 40%. The cost was paid in the floor, in the open (§3.1 shows
   what it does to HAL), not hidden in a shared split.
4. **Gate mechanics carried forward unchanged** (Gate 9 tester
   §4a: sound in construction): evaluated per corpus; baseline
   S_len = final n_steps on the same split with the same AUC
   estimator; pass = AUC ≥ 0.65 **and** AUC − AUC(S_len) ≥ +0.10
   **and** bootstrap 95% CI for the difference excludes 0;
   per-stratum AUCs reported pass or fail. One underspecification
   the tester noted is now closed: the bootstrap CI is the
   **percentile** interval from 1,000 trajectory-level resamples
   (seed §5.7). Failure consequence unchanged: exclusion from that
   corpus's experiment set, on record, no retuning (§5.4).

### 5.3 Feature caps with actual numbers (D4)

Fit-split independent units at the floor: **n_fit = 320
trajectories** (prefix examples are not independent units and are
never counted as such). Frozen budget rule: **total feature
dimensionality D ≤ n_fit / 2 = 160**, evaluated at the floor; caps
below are maxima frozen for all corpora (a larger corpus does not
raise them — caps are not re-derived after any result).

| Block | Content | Count |
|---|---|---|
| (a) Behavioural (per prefix, PREFIX-SAFE) | is_error (current step), errors so far, error rate so far, is_retry, retries so far, loop/repeat count so far, distinct-tool count so far, recoveries so far (error followed by non-error), failure-marker hits so far, marker hits at current step | 10 |
| (b) Position / length (PREFIX-SAFE, §5.1 rule 3) | t, running token total, running mean tokens/step, running token MAD (prefix), steps since last error (capped at 32), steps since last retry (capped at 32) | 6 |
| (c) Cross-step (PREFIX-SAFE) | error-then-recover count, repeated-action max run length, tool-switch count, entropy of tool distribution so far, fraction of steps that are errors in last 5 steps, fraction in last 10 steps | 6 |
| (d) Structured subtotal | (a)+(b)+(c) | **22** |
| (e) Hashed text n-grams | word **unigrams only** (bigrams dropped — V2's {1,2} at 2^12 buckets against ~10² fit trajectories was the D4 gesture), hashed into **2^7 = 128** buckets over `text_digest` of steps ≤ t (cumulative counts, log1p-scaled) | **128** |
| **Total D** | | **150 ≤ 160 ✓** |

Head sizing against the same n: logistic regression uses blocks
(a)–(c) only (22 features against 320 trajectories; at the band's
operative failure window [0.25, 0.40] the fit split holds
80–128 failures — L2 C = 1.0 regularisation stated, and the
residual overfit risk is exactly what the disjoint gate split
exists to catch rather than hide). The GBM uses all 150 features
with min_samples_leaf = 20 (= n_fit/16 at the floor) and 100
trees (§5.1 rule 5) — a leaf cannot be supported by fewer than 20
prefix examples, and tree count is halved from V2's 200, which was
never sized against anything. If a future corpus's fit split is
smaller than 320 the corpus is below the §2 floor and ineligible;
the caps are never loosened to fit it.

### 5.4 Post-gate fixes vs tuning — an applyable test (D5)

V2 §4.2 (no adjustment after a gate AUC is seen) and V2 §7 (a fix
loop after the gate measurement) are reconciled by this test. A
post-gate change is a **correctness fix** (admissible inside the
registration) iff **all four** hold:

1. **Spec-anchored:** the change makes the code match a sentence
   of the frozen design/registration that predates the gate result
   (section and line cited in the fix log). A change with no
   pre-existing spec sentence to point at is tuning.
2. **Outcome-blind evidence:** the defect is demonstrable without
   gate / calibration / test outcomes or scores — by a unit test,
   the synthetic anchors (validate.py A+B), a crash, or a
   spec-vs-code diff. "The gate AUC was low" is not evidence of a
   defect.
3. **No free parameter moves:** the change touches no feature,
   hyperparameter, threshold, split assignment, seed, or
   selection rule.
4. **Both-ways reporting:** after the fix, the gate is re-run and
   **both** pre- and post-fix gate quantities are recorded. The
   pre-fix result remains the registered gate result — **unless**
   the pre-fix run is shown under (1)–(2) to have not implemented
   the frozen spec at all, in which case it is logged as an
   **invalid run** (not a failed gate) and the post-fix run is the
   gate of record. That distinction is decided from the spec diff,
   never from which result is better.

Pre-declared bug classes (the only classes admissible under this
test): trace-parsing errors; off-by-one in prefix truncation;
hash-seed mismatch vs the frozen seed; aggregation formula
deviating from §5.1 rule 6; split leakage in code (a trajectory
appearing in two splits). Anything failing any clause, or outside
these classes, is **tuning**: prohibited in-registration; it
routes to a new candidate under a new pre-registration, exactly
as V2 §4.2 said. Stage 7 applies this test clause by clause and
logs the application; Stage 8 audits the log.

### 5.5 Base-rate eligibility — documented facts or frozen census

The band rule is carried unchanged: confirmatory-eligible iff
base failure rate ∈ [0.10, 0.40] (with the §2 operative-window
note); (0.40, 0.50] descriptive-only; outside [0.10, 0.50]
ineligible. It is applied by exactly two routes:

- **Documented-fact route.** Where a corpus's base rate (or a
  bound on it) is a documented fact in the source's own
  publication, it is applied at design time and cited. Applied in
  §3: taubench_airline 0.84 (v1 pilot, on record — would be
  ineligible, and is excluded on the §5.6 principle anyway);
  Scale-SWE / R2E-Gym / SWE-Gym filtered sets (~0 failure by
  construction); both nebius corpora (resolved counts 838 /
  3,792 against 80,036 / 67.1k trajectories — failure foreseeably
  above the descriptive ceiling; excluded at design time so the
  registration never freezes a corpus its own card disqualifies).
- **Census route (everything else).** Where the base rate is not
  a documented fact, eligibility is decided at a **frozen
  pre-experiment census step** inside the future registration,
  executed before any signal, gate, or split-dependent work:
  (i) parse the corpus into the v1 canonical schema; (ii) record
  exactly the feasibility quantities — trajectories in file vs
  usable, usable n, base failure rate (corpus's own final
  evaluation, binarised at the benchmark's own pass condition;
  exact field named per corpus in the registration), median/mean
  n_steps, step-record coverage, and the §3.1-style integrity
  check (a trajectory counts as usable only if it carries **both**
  a step log and a final evaluation — the rule that resolves the
  swebench_verified_mini 50-vs-18 discrepancy mechanically for
  any future HAL slice); (iii) form the four splits by the frozen
  proportions/seed and record realised split sizes and class
  counts against §§2/5.2 floors; (iv) record the eligibility
  verdict per corpus from these quantities alone. Census
  quantities are recorded whether or not the corpus passes, are
  never revisited after any gate result, and computing them is a
  census act under the registration — not an experiment and not
  signal work. (No base rate was computed by this design pass
  beyond the documented facts cited in §3.)

Corpus order (carried from V2 §5.2): eligible corpora run in
ascending base-failure order, fixed by the census numbers before
any gate result exists.

### 5.6 Carried forward, verified sound by the Gate 9 tester

- **taubench_airline exclusion principle** (tester §4c: holds up):
  spent under v1 with the retired signal; a re-run with a signal
  designed after seeing its result would be test-set reuse; its
  v1 verdict stands in the area record and in any manuscript; the
  §5.5 band is denied retroactive effect on it.
- **Length-only gate mechanics** (tester §4a), with the percentile
  bootstrap now named (§5.2 rule 4).
- **Honest floor/base-rate derivations** (tester §4b) — retained,
  corrected (D6), and applied to counted corpora (D1).
- **Guarantee machinery unchanged** (V2 §6 = v1 §§2–4): T-CRC,
  union-bound arm, stratified arm, anytime-valid betting-CS
  monitor; loss, α grid, δ, anti-vacuity (risk, abstention)
  pairing. One-change-at-a-time: V3 changes signal protocol,
  split hygiene, and scoping — not machinery.
- **Area falsifier unchanged and still open** (packet §4.3:
  ≤ 40% abstention at target risk on ≥ 2 of 3 trace corpora —
  HAL family / own-lab / METR). V3, like V2, can at most falsify
  its own signal craft or authorise proposing the runs that could
  complete the area test; the H-DATA outcome of §4 decides
  neither the area falsifier nor corpus 1's v1 verdict.
- **Approach C remains the sole confirmatory signal class**
  (V2 §2 comparison and §3 choice stand; A/B/D-proxy remain
  descriptive-only, gated identically). B's omission-blindness
  does not shrink (tester §5); a fresh Gate 9 pass on V3 (§8)
  requires a named nearest learned-scorer positioning (§8).

### 5.7 Seeds and split proportions (frozen as design)

Seed **20261031** carried (V2's seed; the registration that
activates V3 will re-freeze it or supersede it on the record —
not silently). Proportions: fit 40 / gate 20 / calibration 20 /
test 20 (§5.2). Stacking folds: 5, by whole trajectory, same
seed. Bootstrap: 1,000 resamples, percentile CI, same seed.

---

## 6. Minimum measured-iteration budget (Improvement Plan P5)

Carried from V2 §7 and restated for the four-split design:
**minimum 5 measured iterations** before any test-split evaluation
may be proposed, each = one change, measured on the same anchors
(validate.py anchors A+B; gate quantities on the gate split only;
calibration quantities on the calibration split only), logged
with its numbers:

- I1 — featurisation + head v0 end-to-end on the synthetic anchor
  (prefix protocol §5.1 exercised, incl. the truncation rules).
- I2 — gate measurement of the frozen confirmatory signal on the
  first eligible corpus (gate split only; test still sealed).
- I3–I4 — fix loop for whatever I1–I2 expose, one change each,
  every change passing the §5.4 four-clause test on the record.
- I5 — full rehearsal: gate + calibration + frontier computed on
  gate/calibration splits only, test split still sealed.

Plateau rule (unchanged): three consecutive iterations improving
the gate margin ΔAUC by < 0.01 route back to Stage 5 with the
question written down — never forward to the test split on hope.
Liveness: iterations checkpoint artefacts to disk; status is
reported from artefacts only.

---

## 7. Options for Ranadhir (the H-DATA decision — his alone)

The floor was not lowered and no registration was frozen; what
follows is the honest option set, each with its price stated.
None is adopted by this document.

- **O1 — Own-lab trace generation (a different, priced study).**
  Generate ≥ 800 usable trajectories in ONE own-lab population
  (packet Corpus B): one system, one task distribution, natural
  outcomes, per-step logging by construction. Two hard sub-conditions:
  the generating system's natural base failure must land in
  [0.10, 0.40] (a system that almost always succeeds or fails is
  ineligible by the same band), and generation costs real compute /
  API spend — a compute-packet decision, $0 policy exception
  required from Ranadhir. This is also the only option that
  directly serves the area falsifier's Corpus B.
- **O2 — Cluster-aware method extension (a redesign, not a fix).**
  Pool HAL runs per family (§3.1: gaia alone offers 5,610
  trajectories over 165 tasks) and change the guarantee machinery
  to a task-group-level calibration. Price: it changes the method
  (violating V2/V3's one-change-at-a-time discipline), re-opens
  the theory-depth question the dossier priced for JMLR/TMLR, and
  changes the falsifier's effective terms — a Stage 5 redesign
  under a new recorded decision by Ranadhir, with its own Gate 9.
- **O3 — Counted re-pass on uncounted collections ($0, dated).**
  A future feasibility pass that actually counts, at metadata
  level: `nvidia/Open-SWE-Traces` per-source subsets (489k rows
  documented; a natural, unfiltered single-scaffold subset at
  ≥ 800 would activate §5 as-is), the CoderForge release (public
  artefact verification; documented failure ≈ 0.40 sits at the
  band's edge), and `SWE-bench/SWE-smith-trajectories` totals.
  Cheapest option; outcome genuinely unknown until counted —
  which is the point of counting.
- **O4 — Re-derive the floor at weaker resolution (not
  recommended; recorded so the refusal is visible).** Relaxing
  the §2 criterion to half-width ≤ 0.075 needs n_cal ≈ 75
  (exact-CP scale), i.e. ≈ 375 usable at §5.2 proportions — still
  above every verified HAL single run (max 307). Half-width
  ≤ 0.10 (n_cal ≈ 44, total ≈ 220) would admit GAIA/USACO-class
  runs at the price of a risk interval wider than the α it must
  resolve — the pilot's original disease (n = 25, half-width
  0.137) at half dose. Any such change is a criterion change only
  Ranadhir can record; this design does not make it.
- **O5 — Park the area / fold into Area 1.** The packet's
  fold-over clause (§4.3) already contemplates this area's
  negative results feeding Area 1's metrology story. The V3
  H-DATA finding — at the field's current public-data frontier,
  no natural agent population is simultaneously large enough,
  unfiltered, in-regime, and step-logged — is itself a
  metrology-relevant fact, and §3's table is its evidence.

---

## 8. Venue and the Gate 9 re-run (both pending, recorded)

- **Venue: unchanged — JMLR** (per `ORCHESTRATOR.md`). For the
  record, again, as a flagged input for Ranadhir (Gate 9 report
  §6.2, confirming the dossier): the V2 design pre-scored
  **5/12 HIGH at JMLR** and ≈ **9/12 LOW at TMLR** (S1 2 / S2 1 /
  S3 2 / S4 1 / S5 1 / S6 2). This design does not change venue
  and does not design "for TMLR"; any venue change is Ranadhir's
  and re-opens the screen (FRAMEWORK Gate 4).
- **Gate 9 must be re-run on this V3 design by a fresh tester**
  before any Stage 6 coding. Recorded in `STATE.md` as PENDING.
  The re-run's remit includes the tester's §5 novelty finding on
  V2 (Approach C positioned against a class label, K7, with no
  named nearest learned-scorer work): §5.6 carries the signal
  choice forward, but the registration that activates V3 must
  name that nearest work and state the delta, or expect the same
  debit.

---

## 9. Defect map — how each Gate 9 defect was answered

| Defect | Fix | Where |
|---|---|---|
| **D1** Floor + corpora frozen together, uncounted (fatal) | Criterion → floor → counted corpora, in that order; feasibility table built from direct/documented counts BEFORE any freeze; no corpus admitted uncounted; pooled HAL examined and rejected with arithmetic; swebench 50-vs-18 discrepancy given a mechanical resolution rule (usable = step log ∧ final evaluation) in the census spec | §§1, 3, 5.5 |
| **D2** Prefix-training protocol unspecified | Full protocol frozen: prefix examples (every t), split-before-expand, per-trajectory weight 1/T_i, final length banned from per-step features, running-statistic definitions, stacking/refit rules, scoring rule | §5.1 |
| **D3** Gate and CRC threshold share calibration split; selection-conditioning unacknowledged | Four disjoint splits (fit/gate/cal/test); gate on gate split only, λ̂ on calibration only; independence argument stated as part of the frozen design; cost counted into the 800 floor | §§2, 5.2 |
| **D4** Feature dimensionality vs fit n a gesture | Budget rule D ≤ n_fit/2 with numbers: 22 structured + 128 hashed unigram buckets = 150 ≤ 160 at n_fit = 320; bigrams dropped; logistic on 22 structured features only; GBM min_samples_leaf = 20, trees 200 → 100; caps frozen as maxima for all corpora | §5.3 |
| **D5** Post-gate fix loop vs no-adjustment rule: boundary undefined | Four-clause applyable test (spec-anchored, outcome-blind evidence, no free-parameter moves, both-ways reporting with the invalid-run distinction) + pre-declared bug-class list; anything else = tuning = new registration | §5.4 |
| **D6** Floor fails its own criterion under exact CP | One method (exact CP) used throughout; recomputed: n = 150 → 0.0513 FAIL; frozen floor n_cal, n_test ≥ **160** (CP [0.0583, 0.1573], half-width 0.0495); n = 159 recorded as the smallest integer pass and the reason 160 was chosen stated | §2 |

---

## 10. Activation conditions (what a future EXPERIMENTS_V3 freeze requires)

A V3 pre-registration (Part I mirroring V2's rigour, updated for
§5's frozen choices, with the census mechanics of §5.5 as its
first registered step) may be written and frozen **only when**:
(a) at least one corpus — target two, for the falsifier count —
has cleared §3's structural tests at the §2 floor on counted
evidence (via §7 O1 or O3, or a corpus counted in a later pass);
(b) Gate 9 has been re-run on this design and passed (§8); and
(c) the registration names the nearest learned-scorer work for
the signal positioning (§8). Until then this area's state is:
**Stage 5R2 complete, H-DATA, awaiting Ranadhir's decision among
§7's options. No coding, no experiments, no submission.**

---

*End of Stage 5R2 deliverable. V2 artefacts untouched; no V3
registration frozen (H-DATA, §4); Gate 9 re-run on V3 pending
(§8); next decision is Ranadhir's (§7).*
