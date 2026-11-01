# EXPERIMENTS V4 — Area 2: Trajectory-Level Conformal Risk Control
## Learned-signal programme on counted public populations (CoderForge / SWE-smith)
### Successor registration to EXPERIMENTS_V3.md (Gate 9 route-back loop 1)

## PART I — PRE-REGISTRATION (FROZEN)

**Frozen at: 2026-10-31T17:33:20Z (2026-10-31 EDT)** — before any V4 census
quantity, gate result, or experiment result exists. At freeze time the
only data contact for the V4 corpora is the metadata-level counting in
`COUNTING_PASS_O3.md` (artefact-level counts, documented facts; no
outcome value of any V4 population has been computed by this programme
beyond the documented facts cited there). The design this registration
executes is `SOLUTION_DESIGN_V3.md` §5 (Stage 5R2, activation-ready
specification), whose signal architecture is `SOLUTION_DESIGN_V2.md`
§§2–4 as repaired by V3 §§2, 5.1–5.5. This file's sha256 and the
design files' sha256 values are recorded in
`PREREGISTRATION_V4.sha256`.

**Lineage (why V4 exists).** `EXPERIMENTS_V3.md` was frozen
2026-10-31T17:22:31Z (`PREREGISTRATION_V3.sha256`) and scored at
Gate 9 by a fresh tester (`TESTING_REPORT_V3_DESIGN.md`): Design
Quality pre-score **5/10** (< 6) and Editor Screen pre-score **9/12
LOW at TMLR** — ROUTE BACK to Stage 5 on the Quality rule. The frozen
V3 file is byte-identical to its freeze and is never edited; this V4
is its successor, written to the tester's defect specification. Text
carried from V3 unchanged is identical in substance; every deliberate
change is listed here and marked at its section:
  - **N1 (§R8 rewritten):** V3's SUPPORTED (a population count) and
    KILL (both family primaries FAIL) could fire simultaneously.
    V4's verdicts are an exhaustive, mutually exclusive decision
    table over family verdicts, themselves read from primary
    populations only; replication results never change any verdict
    in either direction (anti-rescue, symmetric).
  - **N2 (§R3(v)):** the CF `reward` binarisation is now frozen as a
    deterministic function of the census-observed distinct-value
    set — no census-time mapping selection remains.
  - **N3 (§R4):** RNG streams are named per use
    (SeedSequence([20261031, population_index, stream_id])); the
    split-assignment algorithm (stratified greedy deficit) and a
    ±3-percentage-point proportion tolerance are frozen.
  - **N4 (§R8):** a population under GUARANTEE ALERT carries the
    explicit state FAIL(ALERT) unless its run is shown invalid
    under §R12 and re-executed once.
  - **N5 (§R8):** the single-family case has defined verdicts
    (SINGLE-FAMILY SUPPORT / MIXED / FAILURE); none is a programme
    SUPPORTED or KILL.
  - **N6 (§§R1, R5, R7):** descriptive-tier quantities are enumerated
    exactly; the SQ3 stratum field is defined by a census-named
    repository field with a size rule; the token field follows a
    frozen three-level priority.
  - **N7 (§R9 item 8):** CF-2 and the SS family share the SWE-smith
    task universe; cross-family agreement is capped accordingly in
    every claim.
  - **Clarifications (disclosed, no bar moved):** the §2
    operative-window note is restated for realised split sizes
    (§R3); the AgentPRM citation carries its identifier (§R10);
    execution records live in this file's Part II, with
    `EXPERIMENTS_V3.md` left byte-identical to its freeze (§R13).

**Authority.** Ranadhir Ghosh's directive of 2026-10-31 — "make the
best paper out of it and submit to the journal as it fits" — taken
with his 2026-10-31 proceed-directive adopting Decision 2 = option (b)
of `~/workspace/your_files/Research_Pilots_Decision_Packet_2026-10-31.md`
(reframe around learned/verifier signal craft under a new
pre-registration). Recorded in `STATE.md`. The same directive takes
the **venue decision: TMLR** (the dossier's and V3 §8's flagged
finding — design pre-scores ≈ 9/12 LOW at TMLR vs 5/12 HIGH at JMLR —
is thereby acted on by Ranadhir; the Editor Screen target for this
programme is TMLR from this freeze onward, superseding the
ORCHESTRATOR's JMLR screen target for this programme only). This registration
authorises NO submission: the programme's hard stop is Ranadhir's
verification of the final paper (FRAMEWORK Gate 5).

**Relation to the retired registrations (read first).** This is a NEW
pre-registration, not an amendment — and it succeeds a frozen,
never-executed registration of the same programme: `EXPERIMENTS_V3.md`
(frozen 2026-10-31T17:22:31Z; Gate 9 route-back, see Lineage above).
`EXPERIMENTS.md` Part I (frozen
2026-10-31T03:21:44Z) and its pilot outcome — FALSIFIER DIRECTION on
corpus 1 of 3 (HAL taubench_airline; calibration AUC 0.482; test
abstention 100% at α ∈ {0.05, 0.10, 0.20}) — remain frozen, honoured,
and untouched. `EXPERIMENTS_V2.md` Part I (frozen
2026-10-31T15:38:14Z) and `SOLUTION_DESIGN_V2.md` remain frozen and
untouched; their hashes were re-verified OK at this freeze
(`sha256sum -c PREREGISTRATION_V2.sha256`). V2 was never executed: the
Gate 9 design-stage fresh test routed it back (Design Quality 5/10;
Editor Screen 5/12 HIGH at JMLR), and its successor design V3 found
H-DATA over V2's corpora. §R9 states exactly how the three
registrations' falsifier bookkeeping interacts. No frozen bar of v1
or V2 is moved, relaxed, or renegotiated by anything below: V3's
floors and bands are V3 design §2/§5.5's, which are *stricter* than
V2's where they differ (n_cal/n_test ≥ 160 exact-CP, not 150;
four disjoint splits, not three).

**Activation conditions (V3 design §10) — status at freeze.**
(a) Corpora cleared §3's structural tests at the §2 floor on counted
evidence: **YES** — `COUNTING_PASS_O3.md` (2026-10-31): CoderForge-
Preview survives as three source populations; SWE-smith trajectories
survive in six Claude (split × model) populations; per-population
base-rate eligibility expressly reserved to this registration's
census (§R3). (b) Gate 9 re-run on the V3 design: **COMPLETE** —
`TESTING_REPORT_V3_HDATA.md` (fresh verifier; H-DATA finding stands
with corrections C1–C6, all carried into this registration where
relevant; the §5 activation-ready specification D2/D4/D5 confirmed
verbatim-applyable in its §7). Gate 9 scoring of the predecessor
registration (`TESTING_REPORT_V3_DESIGN.md`: Design 5/10, Screen
9/12 LOW at TMLR) routed the programme back; THIS registration is
the successor written to that report's defect list (see Lineage),
and a Gate 9 re-scoring of it (fresh tester; Editor Screen at TMLR)
is executed after this freeze and before any Stage 6 coding, per
the programme's mandated sequence. That re-scoring is loop 2, the
final loop the sequence allows: a second route-back stops the
programme and is reported, with no V5 written under this mandate.
(c) Nearest learned-scorer
work named with the delta: **YES** — §R10 of this registration.

### R1. Hypotheses

- **HV1 (primary, per eligible population).** On an eligible
  population, T-CRC with the frozen Approach-C signal (§R5) and
  primary score S_haz at target risk **α = 0.10** (binary trajectory
  failure, unconditional accepted-risk) achieves held-out test
  risk ≤ α with **test abstention ≤ 40%**.
- **HV2 (signal gate, gate split only).** The frozen signal passes
  the length-only baseline gate (V3 §5.2 rule 4) on that population:
  AUC ≥ 0.65, AUC − AUC(S_len) ≥ +0.10, percentile-bootstrap 95% CI
  for the difference excludes 0 — all computed on the **gate split
  only** (the D3 repair: gate and CRC threshold never share data;
  V2's calibration-split gate is superseded by V3 §5.2).
- **HV3 (SQ1, descriptive).** At α = 0.10, the union-bound arm's test
  abstention exceeds T-CRC's on the same split. The UB arm is carried
  from v1 **unchanged** (per-step behavioural-composite score, native
  error bit as step label; §R6) — it does not use the learned signal.
- Secondary questions SQ2 (anytime-valid betting-CS monitor vs
  fixed-sample repeated-look comparator, v1 design §4), SQ3
  (stratified arm under mixture shift, v1 design §3) and SQ4
  (loss-functionals beyond binary failure, v1 design §1) are carried
  over unchanged, descriptive only, and are exercised only on a
  population where HV2 has passed. SQ3's stratum field is defined
  as follows (defect N6 repair): if census step (ii) finds a
  repository-identifier field on the population's rows, strata are
  that field's values; otherwise the population has no strata and
  SQ3 is not exercised on it. SQ3 is exercised only where ≥ 2
  strata each hold ≥ 40 calibration trajectories after the §R4
  realisation; otherwise it is recorded as not exercised, with the
  reason.

### R2. Corpora and populations (frozen)

Population = one benchmark × one scaffold × one model configuration,
trajectories over distinct tasks (V3 §3 counting discipline). The
candidate populations are exactly the survivors of
`COUNTING_PASS_O3.md` — no other population may enter this
registration:

**Corpus family CF — CoderForge-Preview**
(`togethercomputer/CoderForge-Preview`, HF revision sha `060fca96`,
public; OpenHands scaffold × Qwen3-Coder-480B-A35B-Instruct; outcome
field `reward`; step records in `messages`):
  - CF-1: task source SWE_Rebench — 77,169 trajectories (counted).
  - CF-2: task source SWE_Smith — 148,001 trajectories (counted).
  - CF-3: task source R2E_Gym — 32,964 trajectories (counted).
The `filtered_reward1` split (155,144 rows) is the success-filtered
view documented in the counting pass; it is **not** a population and
is never touched by this registration. The pooled mixture of the
three sources is not a population and is never pooled.

**Corpus family SS — SWE-smith trajectories**
(`SWE-bench/SWE-smith-trajectories`, HF revision sha `08e109b4`,
licence MIT, public; SWE-agent scaffold; outcome field `resolved`;
step records in `messages`). Populations are (format split × model)
cells, Claude cells only (the three GPT-4o cells fail the floor at
counting — 634 / 528 / 475 trajectories — and are excluded):
  - SS-1: tool × claude-3-7-sonnet-20250219 — 17,715 traj / 9,143 tasks.
  - SS-2: xml × claude-3-7-sonnet-20250219 — 18,457 traj / 11,824 tasks.
  - SS-3: ticks × claude-3-7-sonnet-20250219 — 18,457 traj / 11,824 tasks.
  - SS-4: tool × claude-3-5-sonnet-20241022 — 5,751 traj / 1,965 tasks.
  - SS-5: xml × claude-3-5-sonnet-20241022 — 7,091 traj / 2,223 tasks.
  - SS-6: ticks × claude-3-5-sonnet-20241022 — 6,894 traj / 2,222 tasks.
Recorded structural facts the protocol must respect (counting pass):
the format splits share one task pool (xml × claude-3-7 and
ticks × claude-3-7 hold the *identical* 11,824-task set; tool's 9,143
are a subset) — the splits are format variants over common tasks,
never independent corpora; multiple attempts per task exist in every
population (1.56–3.19 trajectories/task), so task-grouped splitting
(§R4) is load-bearing. Cross-population claims never treat SS-1/2/3
(or SS-4/5/6) as independent replications over distinct tasks.

`taubench_airline` and the other HAL slices remain excluded (V3
§5.6: spent under v1; re-running a spent corpus with a redesigned
signal would be test-set reuse). Open-SWE-Traces remains excluded
(counting pass: documented base rates outside the eligibility
envelope in all 18 counted populations). The nebius corpora remain
excluded on corrected documented facts (Gate 9 report C1/C2:
documented failure 0.8327 and 0.5205 respectively — both > 0.50).

### R3. Census — the frozen first step (V3 §5.5 census route)

Before any signal, gate, split-dependent, or confirmatory work, each
candidate population passes through the census, in this order, and
the census quantities are recorded in Part II whether or not the
population passes. Computing census quantities is a census act under
this registration — not an experiment and not signal work.

Per population, the census records exactly:
  (i) artefact identification: dataset id, HF revision sha as
      downloaded, file list with sizes;
  (ii) schema identification (metadata-level, from the artefact):
      the outcome field, the step-record field, the task-identifier
      field, any native per-step error/status field, any per-step
      token-count field — each named exactly as found;
  (iii) trajectories in file vs **usable** (V3 §5.5 integrity rule:
      a trajectory is usable iff it carries BOTH a step log — a
      non-empty step-record list — AND a final evaluation — a
      non-null outcome value); usable n;
  (iv) distinct task count over usable trajectories (by the
      task-identifier field of (ii));
  (v) **base failure rate**: the population's own final evaluation,
      binarised at the benchmark's own pass condition, by these
      frozen rules — no mapping is selected at census time; the
      census only *observes* the distinct-value set and applies the
      rule whose clause matches it (defect N2 repair):
      SS — success iff `resolved` is true (the field is boolean;
      any non-boolean, non-null value set makes the population
      census-ineligible, H-DATA leg).
      CF — let V be the set of distinct non-null values of `reward`
      observed over the population's rows at census, recorded
      verbatim in Part II. The binarisation is the following
      deterministic function of V, fixed here sight-unseen:
        · if every value in V coerces to exactly 0.0 or 1.0
          (booleans coercing as False→0, True→1): success iff the
          value is 1;
        · else if every value in V lies in [0, 1]: success iff the
          value is exactly 1.0 (a fractional reward is a partial
          test pass; the benchmark's own pass condition — the
          SWE-Critix construction, in which the pooled pass count
          155,144 equals the `filtered_reward1` view — is a full
          pass);
        · else (any value outside [0, 1], or non-numeric values):
          the population is census-ineligible (H-DATA leg: the
          benchmark's pass condition cannot be determined from the
          frozen rule), with V recorded as the reason.
      No other clause exists; no clause is chosen by a human after
      seeing V; if the observed V matches no clause the population
      is ineligible, never reinterpreted;
  (vi) median / mean n_steps over usable trajectories; step-record
      coverage (fraction of usable trajectories with ≥ 3 steps);
  (vii) the token-field decision of §R5 (which token quantity the
      corpus carries), from (ii) alone.

**Task-identifier requirement (frozen).** Task-grouped splitting
(§R4) requires a task identifier per trajectory. Census step (ii)
seeks it in this priority order: `instance_id`, `issue_id`,
`task_id`, then a (repository, issue) composite if the artefact
carries both fields. If no task identifier exists for a population,
that population is census-ineligible (H-DATA leg: task-disjoint
splits cannot be enforced, and the hashed-text features of §R5 make
task-identity leakage a concrete failure mode, V3 §3.1) — recorded,
never worked around.

**Eligibility (frozen; V3 §5.5 band + §2 floors).** A population is
confirmatory-eligible iff ALL hold, decided from census quantities
and the §R4 split realisation alone, recorded before any gate
result exists, and never revisited after any gate result:
  (a) usable n ≥ 800;
  (b) base failure rate ∈ [0.10, 0.40];
  (c) the §R4 sample/split realisation yields n_cal ≥ 160 and
      n_test ≥ 160, and each of gate / calibration / test contains
      ≥ 40 successes and ≥ 40 failures.
Base failure rate ∈ (0.40, 0.50] → **descriptive-only tier** for that
population (its reported quantities are enumerated exactly in §R7;
no test evaluation, no falsifier count). Outside [0.10, 0.50], or
failing (a)/(c) → ineligible for any claim under this registration (H-DATA leg for that
population), recorded with the binding quantity.

**Operative-window clarification (disclosed; no bar moved).** V3
design §2's operative confirmatory window [0.25, 0.40] was derived
at the floor split size (n = 160 per split ⇒ ≥ 40 failures needs a
realised failure fraction ≥ 0.25). Leg (c) above is checked on
*realised* counts exactly as frozen; at larger realised splits the
class-count rule binds less (at n_split = 800, ≥ 40 failures needs
only a 0.05 fraction), so a population whose base rate lies in
[0.10, 0.25) can pass leg (c) at the §R4 sample size. The eligibility
band itself — [0.10, 0.40] — is unchanged; what changes with size is
only how much of it the class-count rule can reach, and that is
arithmetic, not a relaxation.

**Population order (frozen).** Eligible populations run in ascending
census base-failure order across BOTH families (the V2 §5.2 ordering
rule, carried); ties break by population id (CF-1 < CF-2 < CF-3 <
SS-1 < … < SS-6). The order is fixed by the census record before any
gate result exists and is never re-ordered afterwards.
Descriptive-tier populations are processed after all confirmatory
populations, in the same ascending order.

### R4. Sampling and split discipline (frozen)

**Study sample.** For each population that passes census legs
(a)/(b) (usable n and base-rate band, confirmatory or descriptive
tier), a study sample is drawn ONCE, as follows. Task groups = all
usable trajectories sharing a task identifier. Groups are ordered by
the population's **sample stream** (defect N3 repair — all RNG
streams in this registration are named, never a bare seed: for
population index j, stream k is numpy `default_rng` with
`SeedSequence([20261031, j, k])`, j = the population's position in
the §R2 list, CF-1 = 1 … SS-6 = 9; stream ids: 1 = sample draw,
2 = split assignment, 3 = stacking folds, 4 = gate bootstrap,
5 = monitor/descriptive resampling if any). Whole
groups are included in sample-stream order until the cumulative trajectory
count first reaches ≥ 4,000 (the crossing group is included whole);
if the population's usable n ≤ 4,000 the sample is the whole
population. The realised sample size is recorded. Only sampled
trajectories are stored (canonical schema, §R5); unsampled rows are
never featurised, gated, or evaluated. No second draw exists: a
sample whose split realisation fails §R3 leg (c) makes the
population ineligible (H-DATA leg), it is not re-drawn — re-drawing
until splits pass would be selection.

**Splits.** The sample is split **by task group** (all trajectories
of a task in exactly one split — v1 design §8's forbidden-splits
rule, and the counting pass's load-bearing warning) by this frozen
algorithm (no step of it is discretionary):
  1. Classify each sampled task group by outcome composition:
     all-success / all-failure / mixed.
  2. Within each composition stratum, order the groups by a
     permutation drawn from the population's split stream
     (stream 2).
  3. Process strata in the order all-failure, mixed, all-success;
     within a stratum, process groups in the stream-2 order; assign
     each group whole to the split with the largest remaining
     trajectory deficit, deficit(split) = target(split) −
     assigned(split), where target = proportion × sample n with
     proportions **fit 0.40 / gate 0.20 / calibration 0.20 /
     test 0.20** (V3 §5.2); ties break in the fixed order fit,
     gate, calibration, test.
  4. Formation checks (recorded, deterministic): every realised
     split's trajectory share is within **±3 percentage points** of
     its target proportion, and §R3 leg (c) holds. If either check
     fails — possible only with pathological group-size structure —
     the population is recorded as a split-realisation failure
     (H-DATA leg). The algorithm is a deterministic function of the
     frozen streams, so there is nothing to re-draw.
Realised split sizes and per-split success/failure counts are
recorded at formation and checked against §R3 leg (c) before any
further step. Steps of a trajectory never straddle splits (a
trajectory is the smallest stored unit). The gate split is used only
for the §R6 gate; the calibration split only for CRC threshold
selection; the test split is evaluated exactly once per frozen
quantity in §R7, after the §R11 iteration budget is complete, and is
never used for fitting, gating, selection, or tuning. Split
assignments are written to disk (`results/v4/splits_<pop>.json`) at
formation and are immutable thereafter within this registration.

### R5. The frozen signal (Approach C; V3 §5.1 + §5.3 verbatim in substance)

**Canonical mapping.** Each sampled trajectory is mapped to the v1
canonical schema (design v1 §7.1) by a parser whose mapping choices
are made from schema inspection (census step (ii)) only, never from
outcomes, and are recorded in `code/BUILD_LOG_V4.md`. A **step** is
one assistant action turn together with the environment observation
that follows it (the granularity both artefacts' `messages` support).
Frozen field rules:
  - `is_error` (native rung): 1 iff the artefact marks the step
    erroneous via a status/error field (as identified at census), OR
    the step's observation text, lowercased, contains any marker of
    the v1 frozen list `tcrc.FAILURE_MARKERS` ("error", "failed",
    "exception", "traceback", "timeout", "invalid", "not found",
    "cannot").
  - `is_retry`: the step's action text is identical to the previous
    step's action text (v1 rule).
  - `tool`: the artefact's tool/function name for the step if
    present; else the first whitespace-delimited token of the action
    text (the "tool key" for the distinct-tool / tool-switch
    features); the choice is recorded per corpus at census.
  - `n_tokens`: by this frozen priority (defect N6 repair): (1) the
    artefact's per-step token-count field, if census step (ii)
    finds one (candidate names, in order: a per-step usage /
    token_count / n_tokens field on the step or its messages);
    (2) else, the sum of per-message token counts over the step's
    messages, if the artefact carries those; (3) else, the
    whitespace-word count of the step's text (action + observation).
    The level used is recorded per corpus at census; no other
    quantity may be substituted after census.
  - `text_digest`: action text + "\n" + observation text, truncated
    to 1,000 characters. All text-derived features (failure-marker
    hits, hashed n-grams, loop detection) are computed on
    `text_digest` and on fields above only — never on the outcome or
    any post-outcome record (v1 leakage guard, carried and
    strengthened by V3 §5.1 rule 3: the final trajectory length T_i
    is banned from per-step features).

**Prefix protocol (V3 §5.1, frozen).** Splits are formed first
(§R4); only then are fit-split trajectories expanded into prefix
examples — one per prefix length t = 1 … T_i, features computed only
from steps 1 … t, label = the trajectory's binary outcome, weight
1/T_i per trajectory. Features (§R5 list below) mark each PREFIX-SAFE
or TRAJECTORY-ONLY; TRAJECTORY-ONLY features never enter the head.
The trajectory-level baseline S_len uses final length legitimately
(it is evaluated after completion, at gate time).

**Heads and stacking (V3 §5.1 rule 5, frozen).** Two base heads on
the identical prefix example set: (i) L2 logistic regression,
C = 1.0, on the 22 structured features only, features standardised by
fit-split prefix-example weighted mean/SD; (ii) gradient-boosted
trees on all 150 features, max_depth = 3, n_estimators = 100,
learning_rate = 0.05, min_samples_leaf = 20. Stacking: 5-fold
cross-fitting **by task group** inside the fit split (population split-stream discipline: stacking folds drawn from stream 3, §R4);
out-of-fold prefix scores from both heads train a logistic
meta-learner (L2, C = 1.0, intercept included, weights 1/T_i). Base
heads are then refit on the full fit split; the meta-learner is NOT
refit. Scoring: s(i, t) = meta-learner output on prefix-(i, t)
features for every t. Aggregation: primary **S_haz** = 1 − Π_t
(1 − s(i, t)); descriptive S_max, S_mean. Confirmatory hypotheses
use S_haz only.

**Feature list (V3 §5.3, frozen; D ≤ n_fit/2 = 160 at the floor;
caps are maxima for all populations and are never re-derived).**
  (a) Behavioural (PREFIX-SAFE), 10: is_error (current step); errors
      so far; error rate so far; is_retry; retries so far;
      loop/repeat count so far (steps whose action text equals any
      earlier step's action text); distinct-tool count so far;
      recoveries so far (an error step followed by a non-error
      step); failure-marker hits so far; marker hits at current step.
  (b) Position/length (PREFIX-SAFE), 6: t; running token total;
      running mean tokens/step; running token MAD (over steps ≤ t);
      steps since last error (capped at 32); steps since last retry
      (capped at 32).
  (c) Cross-step (PREFIX-SAFE), 6: error-then-recover count;
      repeated-action max run length so far; tool-switch count;
      entropy of the tool distribution so far; fraction of steps
      that are errors in the last 5 steps; fraction in the last 10.
  (d) Structured subtotal: 22.
  (e) Hashed text (PREFIX-SAFE): word **unigrams only**, hashed into
      2^7 = 128 buckets over the cumulative `text_digest` of
      steps ≤ t (cumulative counts, log1p-scaled). Hash: a fixed
      seeded hash (Python `hashlib` blake2b of the token, digest
      size 8, reduced mod 128 — deterministic across runs and
      platforms; `PYTHONHASHSEED`-dependent hashing is prohibited).
  Total D = 150 ≤ 160 ✓.
TRAJECTORY-ONLY (never in the head): final length T_i, total tokens
over the full trajectory, full-trajectory token-outlier statistics —
used only by S_len and descriptive reporting.

### R6. Gate, machinery, and arms (frozen)

**Length-only gate (V3 §5.2 rule 4, on the GATE split only).**
Baseline S_len(i) = n_steps(i). AUC estimator: rank (Mann–Whitney)
AUC with average ranks for ties (the v1 pilot's estimator). Per
population, on the gate split: compute AUC(S_haz), AUC(S_len), their
difference, and the difference's **percentile** bootstrap 95% CI
(1,000 trajectory-level resamples of the gate split, population stream 4, §R4).
Per-stratum AUCs are reported alongside where strata exist. **Pass =
all three: AUC(S_haz) ≥ 0.65 AND AUC(S_haz) − AUC(S_len) ≥ +0.10 AND
the CI excludes 0.** Failure consequence (V3 §5.2 rule 4, V2 §4.4):
the signal is excluded from that population's experiment set — no
threshold is calibrated for it, its test split is never evaluated,
and the failure (AUCs, difference, CI) is recorded. No retuning:
any change after a gate quantity is seen is judged by the §R12 test.

**Guarantee machinery — unchanged from v1** (design v1 §§2–4;
V3 §5.6): T-CRC (the `tcrc.crc_threshold` rule: λ̂ = max{λ over
unique calibration scores : (Σ L(i,λ) + 1)/(n+1) ≤ α}, ties exact,
λ̂ = −∞ = abstain-all if no candidate qualifies); the UB arm
(per-step CRC at level α/T̄, T̄ = calibration mean trajectory
length; step score = behavioural composite `step_signal(...,
include_error=False)`, step label = `is_error`; a trajectory is
accepted iff all its steps pass); the stratified arm (per-stratum
T-CRC with Bonferroni correction across strata, descriptive); the
anytime-valid betting-CS monitor (fixed-λ mixture CS as in
`tcrc.betting_cs_bounds`, δ = 0.05; alarm when the CS lower bound
for the accepted-stream loss mean exceeds α; descriptive, with the
fixed-sample repeated-look comparator of v1 design §4 reported
beside it). Loss: L(i, λ) = 1{failed} · 1{S(i) ≤ λ}; controlled
quantity = unconditional accepted-risk. α primary **0.10**; frontier
grid α ∈ {0.05, 0.10, 0.20} (same calibration, three thresholds;
test evaluated once per α). Anti-vacuity guard: risk and abstention
are reported only as a pair.

**Guarantee statement for the gated pipeline (V3 §5.2 rule 2,
frozen as part of the design).** The gate event is measurable
w.r.t. fit + gate splits, which are disjoint from — hence
independent of — the calibration and test splits; conditioning on
it does not alter the calibration sample's distribution, so the CRC
statement for the gated pipeline is the unconditional one. Any
future change letting gate information touch calibration re-opens
the conditioning and must re-state the guarantee as conditional, on
the record, in a new registration.

### R7. Quantities reported (confirmatory list — frozen)

Per population: census quantities (§R3, all legs, pass or fail);
sample/split realisations (sizes, per-split success/failure counts);
gate quantities (AUC(S_haz), AUC(S_len), difference, bootstrap CI,
per-stratum AUCs where strata exist) for the frozen signal; per α in
the grid (for gate-passing confirmatory populations): λ̂, test risk,
test abstention, risk among accepted, n per split; HV3's abstention
pair at α = 0.10; SQ2's monitor outcome (alarm or not, CS bounds at
stream end, comparator violation or not) where exercised; base
failure rate per split; median/mean n_steps per split. Plus the
programme-level verdicts of §R8/§R9 and the §R11 iteration log with
its numbers. Anything beyond this list is labelled EXPLORATORY in
Part II. Risk and abstention are reported only as a pair.
**Descriptive-tier populations report exactly** (defect N6 repair):
the §R3 census quantities; the §R4 sample/split realisations (if
formed); the §R6 gate quantities on the gate split; and per α in
the grid, λ̂ from the calibration split with the **calibration-split**
(risk, abstention) pair, labelled CALIBRATION-SPLIT in every record
and in the manuscript — never a test number, never a verdict, never
part of any count. Populations failing §R3 legs (a)/(b) outside the
descriptive band, or failing leg (c), report the census quantities
and the binding leg only.

### R8. Experiment bars and kill criteria (frozen)

- **Per-population PASS:** HV2 gate passed AND test risk ≤ α AND
  test abstention ≤ 40% at α = 0.10 → the signal craft works on that
  population.
- **Per-population FAIL:** HV2 gate failed (signal excluded on
  record), OR gate passed but HV1 failed (test abstention > 40% at
  α = 0.10, or test risk > α without a guarantee alert) → the signal
  craft fails on that population.
- **Population states (exhaustive).** Every confirmatory-eligible
  population ends in exactly one state: **PASS** (HV2 gate passed
  AND test risk ≤ α AND test abstention ≤ 40% at α = 0.10);
  **FAIL** (gate failed, or gate passed but HV1 failed); or
  **FAIL(ALERT)** (§R8 guarantee-alert rule below). Descriptive-tier
  and ineligible populations have no state and enter no count.
- **Family verdict:** a family's verdict is its **primary
  population's** state — the primary population being the first
  confirmatory-eligible population of that family in the §R3
  frozen order. A family with no confirmatory-eligible population
  has verdict **NO-TEST**. Later eligible populations of the same
  family are confirmatory replications: run under the identical
  protocol and reported in full — and they **never change the
  family verdict or the programme verdict, in either direction**
  (anti-rescue, symmetric: a replication can neither rescue a
  failed primary nor overturn a passed one; defect N1 repair —
  under V3's text, SUPPORTED's population count and KILL's
  primary rule could fire at once; under this table they cannot).
- **Programme verdicts (decision table — exhaustive and mutually
  exclusive; evaluate in this order):**
  1. Both families NO-TEST → **H-DATA** (rule below).
  2. Exactly one family NO-TEST → **single-family reading** on the
     tested family: primary PASS **and** ≥ 1 replication PASS →
     **SINGLE-FAMILY SUPPORT**; primary PASS with no replication
     PASS (or none run) → **SINGLE-FAMILY MIXED**; primary FAIL or
     FAIL(ALERT) → **SINGLE-FAMILY FAILURE**. None of these is a
     programme SUPPORTED or KILL, and none completes any
     two-family count (defect N5 repair).
  3. Both families tested: both primaries PASS → **SUPPORTED**
     (the learned-signal craft restores non-vacuous trajectory-
     level control on natural recorded populations in both
     families; the manuscript's primary claim is licensed, subject
     to the §R9 item-8 claim cap; separately-authorised own-lab /
     METR runs toward the area falsifier may be proposed).
     Both primaries FAIL or FAIL(ALERT) → **V4 KILL** (signal
     craft falsified at programme level) → STOP. Together with
     corpus 1's v1 verdict, no tested signal class (frozen ladder;
     learned head) achieves non-vacuous control anywhere it has
     been honestly tested; the area returns to Ranadhir for a
     kill / park / new-decision. No third signal bite under this
     registration. Exactly one primary PASS → **MIXED** → STOP and
     report; the passing population's frontier and the failing
     population's regime are the result (a regime-boundary
     finding, V2 §5.2); any continuation needs Ranadhir's recorded
     decision.
  No configuration of results maps to two verdicts, and every
  configuration maps to one: the table is a function of the two
  family verdicts (each PASS / FAIL / FAIL(ALERT) / NO-TEST) and,
  only in row 2, of replication PASSes in the tested family.
- **GUARANTEE ALERT (defect N4 repair):** a test risk whose
  two-sided 95% binomial (Clopper–Pearson) CI lies entirely above
  α puts the population in state **ALERT** on occurrence.
  Diagnosis routes back to Stage 6 under the §R12 test: if the
  affected run is shown — by spec-vs-code evidence, without using
  test outcomes beyond the alert itself — to have not implemented
  the frozen spec, the run is logged **invalid**, re-executed
  once, and the population's state is read from the re-run. In
  every other case (defect found and fixed without invalidating
  the run's spec-conformance, no defect found, or diagnosis not
  completable) the population's final state is **FAIL(ALERT)**:
  it counts as FAIL in the table above, and the alert itself is a
  headline result reported wherever the population is reported.
  No tuning on test data under any outcome.
- **H-DATA (programme level):** no population is confirmatory-
  eligible under §R3 → the confirmatory programme does not run;
  the census record is the finding; STOP; floors and bands are not
  lowered post-freeze for any reason. (Descriptive-tier populations,
  if any, are still processed as §R3 specifies and reported.)

### R9. Falsifier bookkeeping — explicit, across v1 + V2 + V3 + V4 (frozen)

1. **The area falsifier (packet §4.3, verbatim from v1 §P2):**
   "Pre-registered abstention ceiling: trajectory-level coverage at
   the target risk must be achievable with <=40% abstention on at
   least 2 of 3 trace corpora. If honest calibration only meets its
   risk budget by abstaining on most trajectories everywhere, the
   guarantee is vacuous - kill, and the negative result folds into
   Area 1's metrology story instead." Its three corpora are fixed
   by the packet's operationalisation: **(F1) HAL task family,
   (F2) own-lab traces, (F3) METR runs.**
2. **Where the count stands after v1:** F1 has a recorded
   **falsifier-direction** result on one HAL task family
   (taubench_airline, retired signal, abstention 100% at α = 0.10).
   F2 and F3 are untested. The area falsifier has therefore NOT
   fired (it needs the condition on ≥ 2 of 3) and has NOT been
   passed; it is open, with one of three families carrying
   negative evidence.
3. **What this registration's families are — and are not.** Its
   families (CF = CoderForge-Preview, SS = SWE-smith trajectories;
   carried unchanged from V3) are **not** F1, F2, or F3: they are
   public SWE-agent trajectory collections, a source class the
   packet did not name. Population results under this registration
   therefore count **neither for nor against** the area falsifier's
   2-of-3. Any document that maps a PASS here onto F2/F3, or a FAIL
   onto the area count, misstates this registration.
4. **What this registration decides** is the signal-craft question
   that v1's decomposition (dossier §3.3) isolated and Decision 2(b)
   posed: *does a learned per-step signal restore a non-vacuous
   trajectory-level CRC frontier on natural recorded populations
   that meet the field's own data floors?* Its count is §R8's
   verdict table over the two families (family verdict = primary
   population; SUPPORTED needs both primaries PASS). A V4 KILL,
   combined with F1's recorded v1 result, is reported as programme-
   level evidence that no tested signal class achieves non-vacuous
   control — and the formal area kill remains Ranadhir's recorded
   decision (FRAMEWORK Gate 3: a fired falsifier kills or reframes
   only by his decision; here the falsifier itself has not fired).
5. **If this programme is SUPPORTED**, completing the area
   falsifier still requires separately pre-registered runs on F2
   (own-lab) and F3 (METR) — where the 2-of-3 verdict would then
   also have to reckon with F1's recorded v1 failure under the area
   rule as originally frozen. Nothing here pre-decides that
   reckoning.
6. **Corpus 1's verdict stands** in every case (V2 §V8.2 carried
   verbatim in substance): it is neither erased nor softened by
   anything here, including by the observation that its 0.84 base
   rate would be ineligible under the §R3 band — that band
   post-dates its run and has no retroactive effect.
7. No frozen bar moves: α = 0.10 primary; 40% ceiling; gate bars in
   §R6; floors and band in §R3 — any change to any of them is a new
   pre-registration under a new recorded decision by Ranadhir.
8. **Shared task universe between CF-2 and the SS family (defect
   N7 repair; claim cap).** CF-2's trajectories were generated on
   SWE-smith tasks, and the SS family's tasks are SWE-smith
   instances: the two families partially share an underlying task
   universe (different scaffold and model, overlapping tasks).
   Cross-family agreement is therefore agreement across scaffold
   and model on a partially shared task universe — **no claim in
   any product of this programme may describe CF and SS as
   independent task replications**, and the SUPPORTED wording in
   §R8 is read subject to this cap. The census records, per
   population, the task-identifier space (so the overlap is
   documented, not estimated).

### R10. Nearest learned-scorer work — named, with the delta (V3 §10(c))

The Gate 9 V2 report's novelty debit was that Approach C was
positioned against a class label (dossier K7) with no named nearest
work. This registration names them:

- **Lightman et al. (2023), "Let's Verify Step by Step"** — process
  reward models (PRMs) trained on human step-level labels, used to
  *select among sampled solutions* at test time. The nearest
  canonical learned step-scorer.
- **Wang et al. (2024), "Math-Shepherd"** — a PRM trained from
  automatic process supervision (no human step labels), used for
  step-weighted verification and reinforcement. The nearest
  *automatically-trained* step-scorer — the closest relative of
  Approach C's fit-split training.
- **Xi et al. (2025), "AgentPRM: Process Reward Models for LLM
  Agents via Step-Wise Promise and Progress" (arXiv:2511.08325)** —
  PRMs lifted to multi-step agent trajectories, scoring steps to
  guide search / test-time selection in agent benchmarks. The
  nearest learned step-scorer *on agent traces specifically*.
  (Citation completed at V4 — Gate 9's V3 report found the V3 text's
  bare "AgentPRM, 2025" too thin to audit.)
- **SafetyDrift (2026)** (dossier K8) — a Markov/absorbing-chain
  risk model over agent traces with monitor alarms; the un-guaranteed
  pole of trace-risk prediction.

**The delta (what none of these does, and this programme does):**
none of them places a distribution-free, finite-sample risk
guarantee over the learned score; none prices abstention against a
pre-registered ceiling as the quantity of interest; none separates
gate / calibration / test so that the guarantee for the *gated*
pipeline is the unconditional statement (§R6); and none is evaluated
as a feasibility question — with pre-registered data floors, a frozen
census, and eligibility decided before any signal exists — over
natural recorded populations. The claimed contribution is the
guarantee + abstention pricing + feasibility discipline over a
learned signal, **not** a better step-scorer; if the scorer itself
were the claim, Math-Shepherd and AgentPRM would be the bar and this
design would not clear it. The manuscript must carry this paragraph's
positioning, not a stronger one.

### R11. Minimum measured-iteration budget (Improvement Plan P5; V3 §6)

Minimum **5 measured iterations** before any test-split evaluation,
each = one change, measured on the same anchors (validate.py
anchors A + B + the V3 synthetic prefix anchor of Stage 6; gate
quantities on the gate split only; calibration quantities on the
calibration split only), logged in Part II with its numbers:
  - I1 — featurisation + head v0 end-to-end on the synthetic anchor
    (the §R5 prefix protocol exercised, incl. truncation rules and
    task-grouped stacking).
  - I2 — gate measurement of the frozen confirmatory signal on the
    first eligible population (gate split only; test still sealed).
  - I3–I4 — fix loop for whatever I1–I2 expose, one change each,
    every change passing the §R12 four-clause test on the record.
  - I5 — full rehearsal: gate + calibration + frontier computed on
    gate/calibration splits only, test split still sealed.
Plateau rule: three consecutive iterations improving the gate margin
ΔAUC by < 0.01 route back to Stage 5 with the question written
down — never forward to the test split on hope. Iterations run per
population for I2–I5 (each population's gate/calibration work is its
own measured sequence on its own splits); I1 is programme-level.
Liveness: iterations checkpoint artefacts to disk; status is
reported from artefacts only.

### R12. Post-gate fixes vs tuning — the four-clause test (V3 §5.4, frozen)

A post-gate change is a **correctness fix** (admissible inside this
registration) iff ALL four hold: (1) **spec-anchored** — it makes
the code match a sentence of the frozen design/registration that
predates the gate result (section cited in the fix log); (2)
**outcome-blind evidence** — the defect is demonstrable without
gate/calibration/test outcomes or scores (unit test, synthetic
anchors, crash, spec-vs-code diff); (3) **no free parameter moves**
— no feature, hyperparameter, threshold, split assignment, seed, or
selection rule changes; (4) **both-ways reporting** — the gate is
re-run after the fix and BOTH pre- and post-fix gate quantities are
recorded; the pre-fix result remains the gate of record unless the
pre-fix run is shown under (1)–(2) to have not implemented the
frozen spec at all, in which case it is logged as an **invalid run**
and the post-fix run is the gate of record. Pre-declared admissible
bug classes (the only ones): trace-parsing errors; off-by-one in
prefix truncation; hash-seed mismatch vs the frozen seed;
aggregation formula deviating from §R5; split leakage in code (a
task group or trajectory appearing in two splits). Anything failing
any clause, or outside these classes, is **tuning**: prohibited
in-registration; it routes to a new candidate under a new
pre-registration. Stage 7 applies this test clause by clause and
logs the application; Stage 8 audits the log.

### R13. Compute, environment, data handling (frozen)

- **CPU-first, $0 spend.** No API calls, no GPU jobs, no paid
  compute. Execution politeness on this shared host: ≤ 2 worker
  processes, `nice -n 10`; other programmes' live jobs are not
  starved.
- **Environment (recorded tooling note, v1 precedent).** System
  python3 on this host carries numpy only — it has neither scipy
  nor scikit-learn — so Stage 6/7 code runs under an existing
  programme venv interpreter that carries the full stack
  (scikit-learn / scipy / numpy / pandas / pyarrow), identified and
  version-pinned in `code/BUILD_LOG_V4.md` at build time from the
  interpreter actually used. All library versions are pinned in
  the build log; the harness must pass under that interpreter.
  Installing public packages into a programme-local venv, if
  needed, is a $0 tooling act recorded in the build log; it changes
  no method quantity.
- **Data handling.** Artefacts are pulled from Hugging Face at the
  revision shas frozen in §R2. Downloads stream per population;
  only census aggregates and the §R4 sampled trajectories (canonical
  schema) are retained; raw download caches are deleted as each
  population is processed. Checkpointing: census, sampling, splits,
  features, and every iteration write artefacts under
  `results/v4/` incrementally, so any host restart resumes from
  artefacts, never from memory.
- **Execution records.** Part II of THIS file is the programme's
  execution log (census first). `EXPERIMENTS_V3.md` is left
  byte-identical to its freeze — its Part II is never written;
  the V3 programme's only execution-adjacent records are the
  Gate 9 report and this file's lineage.

### R14. Venue and the hard stop (frozen)

Target venue: **TMLR** (Ranadhir's 2026-10-31 directive; zero-fee —
TMLR is in the programme's verified zero-fee set, FRAMEWORK Gate 7;
no APC at any route). This registration's chain ends at the Stage 10
decision packet: manuscript + tester verdicts + the exact TMLR
submission checklist, delivered for **Ranadhir's verification**.
No submission, no OpenReview account creation or registration, and
no contact with the journal is authorised by this registration or
by the directive it cites — submission is a separate act on his
explicit direction after he verifies the final paper.

*End of frozen pre-registration (Part I). Part II (Gate 9 record,
census record, iteration log, results, deviations) is appended after
execution and may not alter Part I.*

## PART II — EXECUTION RECORD (appended after the freeze; may not alter Part I)

### Gate 9 records

- **Predecessor (V3):** `EXPERIMENTS_V3.md` frozen
  2026-10-31T17:22:31Z; Gate 9 fresh tester
  (`TESTING_REPORT_V3_DESIGN.md`): Design Quality 5/10, Editor
  Screen 9/12 LOW at TMLR → ROUTE BACK (blocking N1–N3,
  non-blocking N4–N7). V3 was never executed; its file is
  byte-identical to its freeze (§R13 of this registration).
- **This registration (V4):** frozen 2026-10-31T17:33:20Z; Gate 9
  re-scoring, loop 2 (final allowed), fresh tester
  (`TESTING_REPORT_V4_DESIGN.md`): **Design Quality 7/10; Editor
  Screen 9/12 LOW at TMLR → PASS, proceed to Stage 6.** N1's
  blocking part fully repaired (16-combination enumeration);
  N2/N3/N4/N5/N7 repaired; N6 partially repaired (residues
  non-blocking); eight non-blocking items X1–X8 carried as
  pre-result interpretation notes in `code/BUILD_LOG_V4.md`.

### Stage 6 record (build)

- Code: `code/v4lib.py` (frozen-rule machinery), `code/v4parse.py`
  (canonical parser), `code/v4features.py` (frozen §R5 features),
  `code/v4signal.py` (Approach-C stacking, gate, frontier,
  descriptive arms), `code/run_census_v4.py`, `code/run_population_v4.py`;
  v1 library (`tcrc.py`, `synth.py`, `hal_parse.py`, `run_pilot.py`)
  reused unchanged. Environment pinned in `code/BUILD_LOG_V4.md`
  (programme venv; Python 3.12.3; scikit-learn 1.9.1; scipy 1.18.1;
  numpy 2.5.4; pyarrow 26.0.0; matplotlib 3.11.2).
- **Harness: validate.py OVERALL PASS — 48 checks, exit 0**
  (`results_validate_v4_stage6.log`), including v1 anchors A + B
  recovered and Stage F (V4 machinery + synthetic prefix anchor).
- One harness TEST expectation was corrected during the build, on
  the record: the F2 single-family check as first written expected
  SINGLE-FAMILY MIXED for (primary PASS, NO-TEST family,
  replication PASS); §R8 row 2 as frozen assigns SINGLE-FAMILY
  SUPPORT to that configuration. The implementation already
  followed the frozen table; the test was corrected to the frozen
  text and the harness re-run to OVERALL PASS. No frozen rule,
  threshold, or code behaviour changed.
- **Iteration I1 (§R11) — measured:** the synthetic prefix anchor
  (validate.py Stage F6): planted per-step error signal recovered
  by the full §R5 pipeline — gate-split AUC(S_haz) = 0.995;
  CRC frontier at α = 0.10 on synthetic cal/test: test risk 0.080,
  abstention 0.420 (non-vacuous, controls). I1 complete; no defect
  exposed.

### Census record (§R3) — in progress

(Entries appended per population as the census completes; eligibility
is decided from census + split realisation alone and recorded here
before any gate result exists.)

### Pre-census code correction (recorded before any census quantity)

The first SS census launch (2026-10-31) crashed at its first API
call: `run_census_v4.py` carried full-length revision strings that
did not match the Hub (`RevisionNotFoundError` for the SS repo).
Root cause: the Stage 6 code extended the counting pass's recorded
short shas (`060fca96`, `08e109b4`) into full-length strings that
were never in any source. Correction: the full shas were resolved
from the Hub API and verified against the counting pass — prefixes
match and `lastModified` matches the counting pass exactly for both
repos (CF 2026-02-26; SS 2025-07-19), so the artefacts are the ones
counted. Pinned constants now: CF
`060fca96cf723b2ebab3181e9e59fafd273df3cb`; SS
`08e109b4a59eaeebf80e4675cd125d42e7ac99a4`. No data row had been
read and no census quantity existed when this was caught; the
frozen §R2 requirement (artefacts at the counted revisions) is
satisfied by the verified resolution.

### Pre-result census code correction (SS aggregation)

The first SS census pass (after the revision fix) checkpointed two
files with usable = 0 and n_in_file = 0. Diagnosis from the
checkpoint itself: model values in the artefact are
`claude-3-7-sonnet-20250219` / `claude-3-5-sonnet-20241022` (they do
contain the frozen "3-7"/"3-5" class substrings) — the defect was in
`run_census_v4.py`: the SS branch never merged the per-file
aggregate into the population aggregate (`agg_add_file` missing), so
every file's counts were discarded while the file was marked done.
Fix applied (merge + a zero-row warning), the poisoned SS-1
progress file deleted, and the SS census relaunched from scratch.
No census quantity had been recorded anywhere when this was caught
(no `census_<pop>.json` existed); the frozen rules are untouched —
this is a Stage 6 code defect caught by Stage 7 checkpointing,
recorded here per the programme's honesty discipline.

**SS-1 (tool × claude-3-7) — census complete.** Artefact
`SWE-bench/SWE-smith-trajectories` @
`08e109b4a59eaeebf80e4675cd125d42e7ac99a4`, 8 files. In file
17,715; usable 17,715 (parse failures 0); task id =
`field:instance_id` on all rows; distinct tasks 9,143 — both counts
reproduce COUNTING_PASS_O3 exactly. Outcome values: resolved True
6,906 / False 10,809 → **base failure rate 0.6102 — outside
[0.10, 0.50] → INELIGIBLE (leg b)**, recorded before any gate
result. Median n_steps 30, mean 35.0; step coverage (≥ 3 steps)
1.0; token level 3 (whitespace-word counts; the artefact carries
no token fields). Model values: {claude-3-7-sonnet-20250219}.

**SS-2 (xml × claude-3-7) — census complete.** Usable 18,457;
distinct tasks 11,824 (both reproduce COUNTING_PASS_O3 exactly);
parse failures 0; task id on all rows. Outcome: True 8,404 /
False 10,053 → **base failure rate 0.5447 — outside [0.10, 0.50] →
INELIGIBLE (leg b)**. Median n_steps 29, mean 33.5; token level 3.

**SS-3 (ticks × claude-3-7) — census complete.** Usable 18,457;
distinct tasks 11,824; outcomes True 8,404 / False 10,053 →
**base failure rate 0.5447 — INELIGIBLE (leg b)**. Its aggregates
are identical to SS-2's, as the counting pass warned: the xml and
ticks splits are the same trajectories in different formats over
one shared task pool (never independent corpora). Median n_steps
29, mean 33.5; token level 3.

**SS-4 (tool × claude-3-5) — census complete.** Usable 5,751;
distinct tasks 1,965 (both reproduce COUNTING_PASS_O3); outcomes
True 2,346 / False 3,405 → **base failure rate 0.5921 —
INELIGIBLE (leg b)**. Median n_steps 15, mean 21.2; token level 3.
Model values: {claude-3-5-sonnet-20241022}.

**SS-5 (xml × claude-3-5) — census complete.** Usable 7,091;
distinct tasks 2,223 (both reproduce COUNTING_PASS_O3); outcomes
True 2,925 / False 4,166 → **base failure rate 0.5875 —
INELIGIBLE (leg b)**. Median n_steps 15, mean 21.5; token level 3.

**SS-6 (ticks × claude-3-5) — census complete.** Usable 6,894;
distinct tasks 2,222 (both reproduce COUNTING_PASS_O3); outcomes
True 2,852 / False 4,042 → **base failure rate 0.5863 —
INELIGIBLE (leg b)**. (Unlike the 3-7 pair, SS-6's outcomes are
not identical to SS-5's.)

**SS family census summary.** All six populations are ineligible
on leg (b) — base failure rates 0.5447 (SS-2, SS-3), 0.5875
(SS-5), 0.5863 (SS-6), 0.5921 (SS-4), 0.6102 (SS-1), every one
above the 0.50 eligibility ceiling, so no SS population reaches
even the descriptive tier. Under §R8 the SS family verdict is
therefore **NO-TEST** regardless of what follows; the programme
verdict will be read from §R8 rows 1–2 (H-DATA if CF is also
NO-TEST; a single-family reading on CF otherwise). Every SS
usable/task count reproduced COUNTING_PASS_O3 exactly.

### Census step (ii) findings on CoderForge (recorded mid-census, before any CF eligibility decision)

Two findings from the first CF-3 files (10 files, 1,480 rows at
first inspection):

1. **Reward value set contains −1.0.** Observed V so far:
   {−1.0 (4 rows), 0.0 (447), 1.0 (1,029)}. Under the frozen
   §R3(v) function, any set containing a value outside [0, 1]
   falls to **clause 3 — census-ineligible** (the benchmark's pass
   condition cannot be determined from the frozen rule; treating
   −1.0 as failure or as missing would be an invented mapping,
   which the frozen text prohibits). This is recorded as soon as
   observed; the CF-3 census still runs to completion so V and the
   counts are recorded verbatim in full, and CF-1/CF-2 get their
   own V readings.
2. **Task identity is carried in the `image` field.** The Stage 6
   extraction (SWE-bench `__` pattern) found no task id in CF-3
   rows; schema inspection shows the artefact's per-task
   environment image is the task identifier (mechanical
   verification: 148/148 rows, `trajectory_id` minus `_runK` =
   image string). The parser was corrected to the §R3 priority-4
   reading (`field:image`), documented in the BUILD_LOG_V4
   addendum (2026-10-31T19:30:43Z, before any CF eligibility
   decision) and flagged for Stage 8 adjudication under §R12.
   Counterfactual on record: under the initial narrow pattern the
   CF family would have read as task-identity-absent (ineligible);
   CF-3's clause-3 reward outcome is independent of this question.
   The partial CF-3 progress gathered under the old extraction was
   discarded and the CF census relaunched with the corrected
   parser.

**CF-3 (R2E_Gym) — census complete.** Artefact
`togethercomputer/CoderForge-Preview` @
`060fca96cf723b2ebab3181e9e59fafd273df3cb`, 224 files. In file
32,964; usable 32,964 (parse failures 0 — reproduces the counted
population size); task id `field:image` on all rows; distinct
tasks 4,274. **Reward V = {−1.0: 278, 0.0: 11,782, 1.0: 20,904}
(recorded verbatim) → §R3(v) clause 3: INELIGIBLE** — the set
contains a value outside [0, 1], so the frozen function returns
ineligible; no mapping was invented for −1.0. Median n_steps 55,
mean 59.1; step coverage (≥ 3) 0.9999; token level 3.
Exploratory only (never an eligibility input): among the
{0.0, 1.0} rows the failure share is 11,782 / 32,686 = 0.3605 —
inside the confirmatory band; the binding barrier for CF-3 is the
undocumented third reward value (278 rows, 0.84%), not the band.

**CF-1 (SWE_Rebench) — early reading.** After 5 files (1,725
rows) V already contains −1.0 (5 rows), so CF-1's clause is also
determined (clause 3) once its census completes; the census runs
on for the verbatim full record.

**CF-2 (SWE_Smith) — census complete.** 224 files. In file
148,001; usable 148,001 (parse failures 0 — reproduces the
counted population size). **Reward V = {−1.0: 367, 0.0: 58,133,
1.0: 89,501} (verbatim) → §R3(v) clause 3: INELIGIBLE.** Median
n_steps 48, mean 53.3; step coverage (≥ 3) 1.0; token level 3.
Task-identity documentation (correcting the granularity picture
in the step-(ii) note): the `image` field takes only **444
distinct values** over CF-2's 148,001 trajectories — for the
SWE_Smith source it is a per-repository environment image shared
by many distinct synthetic instances, NOT a per-instance id
(CF-3's R2E_Gym images, hash-suffixed, are near-instance-level at
4,274 distinct; CF-1's reading is pending). Grouping by image
would still be task-conservative (each instance maps to exactly
one image), so no split could have leaked; but the granularity
difference is on the record here and in the manuscript, and the
Stage 8 tester is asked to adjudicate the reading with this
per-population evidence. Immaterial to CF-2's eligibility, which
clause 3 settles independently. Exploratory only: among
{0.0, 1.0} rows the failure share is 0.3938 — inside the
confirmatory band, near its top; the −1.0 share is 0.25%.

**CF-1 (SWE_Rebench) — census complete.** 224 files. In file
77,169; usable 77,169 (parse failures 0 — reproduces the counted
population size); task id `field:image` on all rows; distinct
images 4,492 (per-repository/version environments, ~17 runs per
image — same granularity family as CF-3, not per-instance).
**Reward V = {−1.0: 255, 0.0: 32,175, 1.0: 44,739} (verbatim) →
§R3(v) clause 3: INELIGIBLE.** Median n_steps 59, mean 62.8; step
coverage (≥ 3) 0.9997; token level 3. Exploratory only: among
{0.0, 1.0} rows the failure share is 0.4183 — the descriptive
band; counting −1.0 rows as failures instead would give 0.4203,
also descriptive-band. CF-1 would not have been confirmatory
under either exploratory reading.

### Eligibility table and programme verdict (frozen §R3/§R8 reading)

| Pop | Usable | Tasks (id space) | Binding quantity | Outcome |
|---|---|---|---|---|
| CF-1 | 77,169 | 4,492 (image) | V ∋ −1.0 (255 rows) | ineligible — §R3(v) clause 3 |
| CF-2 | 148,001 | 444 (image) | V ∋ −1.0 (367 rows) | ineligible — §R3(v) clause 3 |
| CF-3 | 32,964 | 4,274 (image) | V ∋ −1.0 (278 rows) | ineligible — §R3(v) clause 3 |
| SS-1 | 17,715 | 9,143 (instance_id) | base failure 0.6102 | ineligible — leg (b) |
| SS-2 | 18,457 | 11,824 (instance_id) | base failure 0.5447 | ineligible — leg (b) |
| SS-3 | 18,457 | 11,824 (instance_id) | base failure 0.5447 | ineligible — leg (b) |
| SS-4 | 5,751 | 1,965 (instance_id) | base failure 0.5921 | ineligible — leg (b) |
| SS-5 | 7,091 | 2,223 (instance_id) | base failure 0.5875 | ineligible — leg (b) |
| SS-6 | 6,894 | 2,222 (instance_id) | base failure 0.5863 | ineligible — leg (b) |

Every usable count reproduces COUNTING_PASS_O3 exactly; total
trajectories censused: 335,135; parse failures: 0 across all nine
populations. No population reached the split realisation, so no
gate was ever computed and no test split exists anywhere in this
programme — there is nothing to tune and nothing was tuned.

**Family verdicts:** CF = NO-TEST (no confirmatory-eligible
population); SS = NO-TEST (same). **Programme verdict (§R8
decision table, row 1): H-DATA.** The confirmatory programme does
not run; the census record is the finding; STOP, per the frozen
registration and the mandate. Floors and bands were not lowered,
no binarisation was invented, and no criterion was relaxed at any
point. Formal per-population records: `results/v4/result_<pop>.json`
(all nine).

**Falsifier bookkeeping (final, per §R9).** The area falsifier's
count is unchanged by this programme: F1 (HAL) carries v1's
falsifier-direction result; F2/F3 remain untested; CF/SS results
count neither for nor against the 2-of-3. The V4 programme
decided its own question — the signal-craft question — only in
the negative-feasibility sense: the question could not be put to
any eligible population, because no counted public population
survives the field's own data floors under pre-registered rules.
The formal area kill remains Ranadhir's decision (FRAMEWORK
Gate 3); this record recommends the H-DATA outcome be reported to
him as the programme's result, with the manuscript below.

**Iteration log closure (§R11).** I1 completed (synthetic prefix
anchor, Stage 6 record). I2–I5 were defined per eligible
population (gate measurement, fix loop, rehearsal); no population
was eligible, so no I2–I5 iteration exists and none is claimed.
The execution's measured work after I1 is the census itself
(nine populations, per-file checkpointed, two pre-result code
corrections and one parser schema correction recorded above) —
reported as what it is, not dressed as the iteration budget.

### Execution corrections — consolidated

Three code defects were caught and corrected during execution,
each before the quantities it could have touched were recorded
as results, each recorded at the time (entries above): (1) the
census script's full-length HF revision strings (resolved and
verified against the counting pass); (2) the SS aggregation merge
(checkpoint showed usable = 0; poisoned progress discarded,
census relaunched); (3) the CF task-identifier extraction
(initial SWE-bench-pattern reading superseded by the census's
schema identification of the `image` field; flagged for Stage 8
adjudication; immaterial to every eligibility outcome, since
clause 3 and leg (b) settle all nine populations independently).
No frozen rule, bar, band, floor, or clause was changed by any
correction.

### Erratum (appended 2026-11-01, per Stage 8 Fix 1 — not a silent edit)

The eligibility section above states "total trajectories censused:
335,135". That total is an arithmetic error in summary prose,
identified by the Stage 8 fresh tester
(`TESTING_REPORT_V4_RESULTS.md` §1) by recomputation from the
census files. The correct total is **332,499** (CF subtotal
258,134 = 77,169 + 148,001 + 32,964; SS subtotal 74,365 =
17,715 + 18,457 + 18,457 + 5,751 + 7,091 + 6,894 — a sum over the
nine registered populations; SS-2 and SS-3 are the same
trajectories in two formats). Every summand and every per-population
quantity in this record was individually correct; only the summary
total was wrong (overstated by 2,636). No outcome, eligibility
decision, or verdict is affected. All downstream documents
(REPORT.md, the manuscript, STATE.md) use 332,499.

### Stage 8 adjudication of the CF task-identifier reading (§R12 question)

The correction of the CF task-identifier extraction to the `image` field
(`code/BUILD_LOG_V4.md` addendum, 2026-10-31T19:30:43Z, recorded before
any CF eligibility decision) is ruled a conformant census-step-(ii)
schema identification in its procedural character: §R5 assigns parser
mapping choices to census step (ii), the identification rested on
outcome-blind mechanical evidence (148/148 rows: `trajectory_id` minus
its `_runK` suffix equals the `image` string), and no frozen rule,
parameter, or recorded quantity was changed by it; §R12, which governs
post-gate changes, does not apply, no gate having existed. Substantively,
however, `image` is not a per-instance task identifier and is not the
(repository, issue) composite of §R3's priority list, which presupposes
both fields carried separately: the final distinct counts are CF-1
4,492 images over 77,169 trajectories, CF-2 444 over 148,001, and CF-3
4,274 over 32,964 — per-repository environment images of varying
granularity, near-instance-level only for CF-3. Grouping by `image`
would have been task-conservative (no task could straddle splits) but
coarser than task grouping, and no split was ever formed on it. The
reading changes no outcome: under the counterfactual narrow
(SWE-bench-pattern) reading the CF populations are ineligible on the
task-identity leg; under the adopted reading they are ineligible under
§R3(v) clause 3; the CF family is NO-TEST and the programme verdict is
H-DATA under both.

*(Paragraph pasted verbatim from `TESTING_REPORT_V4_RESULTS.md`
§3.5, as that report directed.)*

### Stage 8 record (fresh tester on the results)

`TESTING_REPORT_V4_RESULTS.md` (2026-11-01): verdict chain
VERIFIED (all base rates and clause determinations recomputed
from the census files; §R8 row 1 → H-DATA correct); negative
space clean (no gate/split/test artefact exists anywhere);
execution corrections all judged adequately recorded and
pre-result; §R11 closure judged honest accounting. **Quality
6/10** (below the programme's 8/10 high-distinction bar);
**Editor Screen 7/12 MEDIUM at TMLR** (S1 1 / S2 1 / S3 2 /
S4 1 / S5 1 / S6 1; no HIGH trigger). Route verdict: PROCEED to
Stages 9–10 subject to twelve mandatory writing/packaging fixes
(all applied in REPORT.md and the manuscript; Fix 10's public
deposit is carried as a pre-submission packaging step in the
TMLR checklist, and the manuscript makes no public-availability
claim). Submission remains behind Ranadhir's verification
(§R14 hard stop), with the 6/10 score, the 7/12 MEDIUM screen,
and this adjudication as his explicit decision items.
