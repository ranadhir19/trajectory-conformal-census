# EXPERIMENTS V3 — Area 2: Trajectory-Level Conformal Risk Control
## Learned-signal programme on counted public populations (CoderForge / SWE-smith)

## PART I — PRE-REGISTRATION (FROZEN)

**Frozen at: 2026-10-31T17:22:31Z (2026-10-31 EDT)** — before any V3 census
quantity, gate result, or experiment result exists. At freeze time the
only data contact for the V3 corpora is the metadata-level counting in
`COUNTING_PASS_O3.md` (artefact-level counts, documented facts; no
outcome value of any V3 population has been computed by this programme
beyond the documented facts cited there). The design this registration
executes is `SOLUTION_DESIGN_V3.md` §5 (Stage 5R2, activation-ready
specification), whose signal architecture is `SOLUTION_DESIGN_V2.md`
§§2–4 as repaired by V3 §§2, 5.1–5.5. This file's sha256 and the
design files' sha256 values are recorded in
`PREREGISTRATION_V3.sha256`.

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
ORCHESTRATOR's JMLR screen target for V3 only). This registration
authorises NO submission: the programme's hard stop is Ranadhir's
verification of the final paper (FRAMEWORK Gate 5).

**Relation to the retired registrations (read first).** This is a NEW
pre-registration, not an amendment. `EXPERIMENTS.md` Part I (frozen
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
verbatim-applyable in its §7). A further Gate 9 scoring of THIS
registration's design (FRAMEWORK Gate 9 applied to the registration
as the Stage 5 exit artefact for the V3 programme, with the Editor
Screen pre-score at the now-decided venue TMLR) is executed after
this freeze and before any Stage 6 coding, per the programme's
mandated sequence; a route-back (< 6/10 design quality or HIGH
screen) returns the programme to design and is recorded in Part II —
the freeze itself is not edited in that event; a successor
registration would be written instead. (c) Nearest learned-scorer
work named with the delta: **YES** — §R10 of this registration.

### R1. Hypotheses

- **HV1 (primary, per eligible population).** On an eligible V3
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
  population where HV2 has passed. SQ3 is exercised only where the
  population carries a stratum field with ≥ 2 strata each holding
  ≥ 40 calibration trajectories; otherwise it is recorded as not
  exercised, with the reason.

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
      binarised at the benchmark's own pass condition. Frozen
      binarisations: SS — success iff `resolved` is true. CF —
      success iff `reward` encodes a pass under the artefact's own
      documented semantics (SWE-Critix, arXiv:2610.13356: reward is
      the trajectory's test outcome; the counting pass records the
      pooled pass count 155,144 = the `filtered_reward1` view).
      The census records the distinct values of `reward` and the
      mapping applied; if the mapping cannot be determined
      unambiguously from the artefact and its paper, the population
      is census-ineligible (H-DATA leg) with the reason recorded —
      no mapping is invented;
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
population (census quantities and, if the §R4 realisation is formed,
the gate quantity and the calibration-split frontier are reported;
no test evaluation, no falsifier count). Outside [0.10, 0.50], or
failing (a)/(c) → ineligible for any V3 claim (H-DATA leg for that
population), recorded with the binding quantity.

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
a seeded RNG stream (numpy `default_rng` with
`SeedSequence([20261031, population_index])`, population_index = the
population's position in the §R2 list, CF-1 = 1 … SS-6 = 9). Whole
groups are included in that order until the cumulative trajectory
count first reaches ≥ 4,000 (the crossing group is included whole);
if the population's usable n ≤ 4,000 the sample is the whole
population. The realised sample size is recorded. Only sampled
trajectories are stored (canonical schema, §R5); unsampled rows are
never featurised, gated, or evaluated. No second draw exists: a
sample whose §R4 split realisation fails leg (c) makes the
population ineligible (H-DATA leg), it is not re-drawn — re-drawing
until splits pass would be selection.

**Splits.** The sample is split **by task group** (all trajectories
of a task in exactly one split — v1 design §8's forbidden-splits
rule, and the counting pass's load-bearing warning), stratified by
task-group outcome composition (all-success / all-failure / mixed),
seeded RNG (seed 20261031, same per-population stream discipline as
the sample draw, drawn after it), targeting trajectory proportions
**fit 40% / gate 20% / calibration 20% / test 20%** (V3 §5.2).
Realised split sizes and per-split success/failure counts are
recorded at formation and checked against §R3 leg (c) before any
further step. Steps of a trajectory never straddle splits (a
trajectory is the smallest stored unit). The gate split is used only
for the §R6 gate; the calibration split only for CRC threshold
selection; the test split is evaluated exactly once per frozen
quantity in §R7, after the §R11 iteration budget is complete, and is
never used for fitting, gating, selection, or tuning. Split
assignments are written to disk (`results/v3/splits_<pop>.json`) at
formation and are immutable thereafter within this registration.

### R5. The frozen signal (Approach C; V3 §5.1 + §5.3 verbatim in substance)

**Canonical mapping.** Each sampled trajectory is mapped to the v1
canonical schema (design v1 §7.1) by a parser whose mapping choices
are made from schema inspection (census step (ii)) only, never from
outcomes, and are recorded in `code/BUILD_LOG_V3.md`. A **step** is
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
  - `n_tokens`: the artefact's per-step token count if present; else
    the whitespace-word count of the step's text (action +
    observation); the choice is recorded per corpus at census.
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
cross-fitting **by task group** inside the fit split (seed 20261031);
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
(1,000 trajectory-level resamples of the gate split, seed 20261031).
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

### R8. Experiment bars and kill criteria (frozen)

- **Per-population PASS:** HV2 gate passed AND test risk ≤ α AND
  test abstention ≤ 40% at α = 0.10 → the signal craft works on that
  population.
- **Per-population FAIL:** HV2 gate failed (signal excluded on
  record), OR gate passed but HV1 failed (test abstention > 40% at
  α = 0.10, or test risk > α without a guarantee alert) → the signal
  craft fails on that population.
- **Family verdict:** a family's verdict is its **primary
  population's** verdict — the first confirmatory-eligible
  population of that family in the §R3 frozen order. Later eligible
  populations of the same family are confirmatory replications:
  run under the identical protocol, reported in full, counted in
  the programme count below, but they do not change the family
  verdict. (Frozen so that a family cannot be "rescued" by running
  its populations until one passes.)
- **Programme count and verdicts:**
  - **SUPPORTED:** ≥ 2 populations PASS, spanning both families
    (i.e., at least one PASS in CF and at least one in SS) → the
    learned-signal craft restores non-vacuous trajectory-level
    control on natural recorded populations; the manuscript's
    primary claim is licensed, and separately-authorised own-lab /
    METR runs toward the area falsifier may be proposed.
  - **V3 KILL (signal craft falsified at programme level):** the
    primary population of BOTH families FAILs → STOP. Together
    with corpus 1's v1 verdict, no tested signal class (frozen
    ladder; learned head) achieves non-vacuous control anywhere it
    has been honestly tested; the area returns to Ranadhir for a
    kill / park / new-decision. No third signal bite under this
    registration.
  - **MIXED (all other configurations):** STOP and report; the
    passing populations' frontiers and the failing populations'
    regimes are the result (a regime-boundary finding, V2 §5.2).
    Any continuation needs Ranadhir's recorded decision.
  - **Single-family case:** if only one family has any eligible
    population, the programme verdicts read on that family alone
    and are recorded as single-family support/failure only;
    SUPPORTED additionally requires ≥ 2 populations PASS within
    that family (the two-population bar does not shrink).
- **GUARANTEE ALERT:** a test risk whose two-sided 95% binomial
  (Clopper–Pearson) CI lies entirely above α → implementation /
  method problem suspected; route back to Stage 6 for diagnosis
  under the §R12 test. No tuning on test data under any outcome.
- **H-DATA (programme level):** no population is confirmatory-
  eligible under §R3 → the confirmatory programme does not run;
  the census record is the finding; STOP; floors and bands are not
  lowered post-freeze for any reason. (Descriptive-tier populations,
  if any, are still processed as §R3 specifies and reported.)

### R9. Falsifier bookkeeping — explicit, across v1 + V2 + V3 (frozen)

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
3. **What V3's families are — and are not.** V3's families
   (CF = CoderForge-Preview, SS = SWE-smith trajectories) are
   **not** F1, F2, or F3: they are public SWE-agent trajectory
   collections, a source class the packet did not name. V3
   population results therefore count **neither for nor against**
   the area falsifier's 2-of-3. Any document that maps a V3 PASS
   onto F2/F3, or a V3 FAIL onto the area count, misstates this
   registration.
4. **What V3 does decide** is the signal-craft question that v1's
   decomposition (dossier §3.3) isolated and Decision 2(b) posed:
   *does a learned per-step signal restore a non-vacuous
   trajectory-level CRC frontier on natural recorded populations
   that meet the field's own data floors?* Its count is §R8's
   programme count over V3's two families (family verdict = primary
   population; SUPPORTED needs PASS in both families). A V3 KILL,
   combined with F1's recorded v1 result, is reported as programme-
   level evidence that no tested signal class achieves non-vacuous
   control — and the formal area kill remains Ranadhir's recorded
   decision (FRAMEWORK Gate 3: a fired falsifier kills or reframes
   only by his decision; here the falsifier itself has not fired).
5. **If V3 is SUPPORTED**, completing the area falsifier still
   requires separately pre-registered runs on F2 (own-lab) and F3
   (METR) — where the 2-of-3 verdict would then also have to reckon
   with F1's recorded v1 failure under the area rule as originally
   frozen. Nothing in V3 pre-decides that reckoning.
6. **Corpus 1's verdict stands** in every case (V2 §V8.2 carried
   verbatim in substance): it is neither erased nor softened by
   anything in V3, including by the observation that its 0.84 base
   rate would be ineligible under the V3 band — that band post-dates
   its run and has no retroactive effect.
7. No frozen bar moves: α = 0.10 primary; 40% ceiling; gate bars in
   §R6; floors and band in §R3 — any change to any of them is a new
   pre-registration under a new recorded decision by Ranadhir.

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
- **Agent process reward models (e.g., AgentPRM, 2025)** — PRMs
  lifted to multi-step agent trajectories, scoring steps to guide
  search / test-time selection in agent benchmarks. The nearest
  learned step-scorer *on agent traces specifically*.
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
  version-pinned in `code/BUILD_LOG_V3.md` at build time from the
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
  `results/v3/` incrementally, so any host restart resumes from
  artefacts, never from memory.

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
