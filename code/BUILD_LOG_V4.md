# BUILD LOG — V4 programme (Stage 6)

Written at Stage 6 build time, BEFORE any census quantity, gate
result, or experiment result exists (registration §R13). Contents:
environment pin; pre-result interpretation notes for the Gate 9
carry items X1–X8 (`TESTING_REPORT_V4_DESIGN.md` §5) and for parser /
feature definition points the frozen text leaves at build level.
Interpretations are readings of the frozen registration, never
amendments to it; if any reading is later shown to conflict with the
frozen text, the frozen text governs and the affected runs are
invalid under §R12.

## Environment (pinned)

- Interpreter: programme-local venv
  `~/workspace/research-orchestration/areas/trajectory-conformal-risk-control/venv/bin/python`
  (created Stage 6; $0 tooling act under §R13).
- Python 3.12.3; numpy 2.5.4; scipy 1.18.1; scikit-learn 1.9.1;
  pandas 3.1.0; pyarrow 26.0.0; huggingface_hub 2.4.0;
  matplotlib 3.11.2.
- The v1 library (`tcrc.py`, `synth.py`, `hal_parse.py`,
  `run_pilot.py`) is reused unchanged; the harness (validate.py)
  must pass under this interpreter, v1 anchors included.

## Interpretation notes (pre-result; Gate 9 X1–X8 + build-level)

- **X1 (§R8 row 2).** The §R8 decision table — specific and ordered —
  governs over the family-verdict bullet's summary sentence. Reading
  adopted: replication PASSes affect ONLY the row-2 distinction
  between SINGLE-FAMILY SUPPORT and SINGLE-FAMILY MIXED; they never
  change a family verdict, and rows 1 and 3 are replication-invariant.
  `v4lib.programme_verdict` implements the table in exactly this
  reading and is unit-tested over all 16 family-verdict combinations.
- **X2 (§R8 states).** The states partition is read on §R8's full
  text: FAIL excludes the alert case (the per-population FAIL bullet
  says "without a guarantee alert"); a population whose final run
  alerts ends FAIL(ALERT).
- **X3 (alert re-run).** "ALERT" is a provisional label and never
  enters a count; states are final states. If the single authorised
  re-execution itself alerts, the population's final state is
  FAIL(ALERT) with no second diagnosis.
- **X4 (§R3(v) CF function).** Values take the artefact's type:
  "coerces" applies within boolean/numeric types only; a string-typed
  reward column is non-numeric and falls to clause 3 (ineligible).
  V is recorded verbatim in Part II whatever it turns out to be.
- **X5 (draw primitives).** Adopted primitives: the pre-permutation
  group list is the task ids sorted ascending (string order); each
  RNG stream is one `numpy.random.default_rng(SeedSequence([20261031,
  j, k]))`; permutations are `Generator.permutation`; stream 2 is
  consumed stratum by stratum in §R4's processing order (all-failure,
  mixed, all-success); stacking folds (stream 3) assign groups
  round-robin in permutation order to folds 0–4. Realised split
  assignments are frozen to `results/v4/splits_<pop>.json`.
- **X6 (repository field; token subfields).** Repository-identifier
  candidates, in order: a field named `repo`, `repository`, or
  `repo_name` on the row. `instance_id` is a task identifier, not a
  repository field, and is not decomposed. If none exists, SQ3 is
  recorded as not exercised for that population. Token priority
  sub-order inside a `usage` container: total_tokens →
  prompt_tokens + completion_tokens → completion_tokens →
  prompt_tokens; multiple per-message counts in one step are summed
  (level 2).
- **X7 (descriptive λ̂).** §R6's gate-failure consequence ("no
  threshold is calibrated for it") applies to descriptive-tier
  populations too: a descriptive population whose gate fails reports
  gate quantities and census quantities only, with the record
  stating that no λ̂ was calibrated; a descriptive population whose
  gate passes reports the §R7 calibration-split frontier.
- **X8 (task-identifier space).** The census additionally records,
  per population, the task-identifier documentation §R9 item 8
  requires: the field/rule that supplied task ids, the number of
  distinct task ids, and the number of usable trajectories carrying
  one. Documentation only; not an eligibility leg.

## Build-level definitions (§R5 feature list / parser)

- **CF task identifier.** The artefact carries no id column; the
  (repository, issue) composite is sought as a SWE-bench instance
  pattern (`<owner>__<repo>-<issue>`) inside `trajectory_id`, then
  `image` (v4parse.extract_task_id). Rows without an extractable
  task id cannot enter task-grouped splits: the census records
  their count separately, sampling/grouping operates on rows with
  task ids, and if trajectories-with-task-id number < 800 the
  population is recorded ineligible (task-identity leg), with the
  counts on the record.
- **Steps.** A step is one assistant message plus all following
  non-assistant messages up to the next assistant message; a final
  assistant message with no following observation is a step with an
  empty observation. System messages and the pre-first-assistant
  user message (task prompt) are not steps.
- **Marker hits (per step)** = number of distinct FAILURE_MARKERS
  strings present in the step's lowercased observation (0–8).
- **(a)8 recoveries** = adjacent error→non-error transitions inside
  the prefix. **(c)1 error-then-recover count** = error steps in the
  prefix that are followed somewhere later in the prefix by a
  non-error step (= errors so far minus the trailing error run).
  The two differ whenever an error episode has length ≥ 2.
- **Token MAD** = median absolute deviation about the median, no
  consistency scaling. **Steps since last error/retry** = t minus
  the 1-based index of the most recent such step (t if none), capped
  at 32. **Tool entropy** = natural-log entropy of the prefix tool
  distribution.
- **GBM determinism**: sklearn GradientBoostingClassifier with
  random_state = 20261031 (the frozen seed base); all other GBM
  hyperparameters exactly §R5's.
- **SQ2 comparator** (v1 design §4): the fixed-sample comparator is
  the end-of-stream Clopper–Pearson lower bound on the same loss
  sequence; "comparator violation" = that bound exceeds α while the
  time-uniform CS does not alarm, or vice versa — recorded as the
  pair (cs_alarm, fixed_sample_violation) at stream end.
- **Iterations I3/I4 (§R11).** If I1–I2 expose no defect, I3 and I4
  are consumed as measured verification iterations (descriptive-arm
  calibration on gate/cal; calibration-frontier rehearsal) and are
  logged in Part II as such, with their numbers; any defect exposed
  at any iteration inserts a §R12 fix iteration (one change) before
  I5. No test-split quantity is computed before I5 completes.

## ADDENDUM — 2026-10-31T19:30:43Z (Stage 7, census step (ii); before any CF eligibility decision)

**CF task identifier — schema identification supersedes the initial
build-log guess.** The initial note above sought the (repository,
issue) composite as a SWE-bench `__` instance pattern inside
`trajectory_id`/`image`. Census step (ii) inspection of the actual
artefact shows that guess was over-narrow: CoderForge rows carry
their task identity in the **`image` field verbatim** — the task's
per-instance environment image (e.g.
`qingyangwu/aiohttp_final:006fbe03fede4eaa1eeba7b8393cbf4d63cb44b6`),
shared by all runs of the task. Mechanical verification on an
inspected file (148 rows): 20 distinct images; `trajectory_id`
minus its `_runK` suffix equals the image string (with `/` and `:`
mapped to `_`) on 148/148 rows, 0 mismatches. The frozen
registration (§R3) requires "a task identifier per trajectory",
sought by field priority ending in a (repository, issue) composite
"if the artefact carries both fields", and §R5 assigns parser
mapping choices to census step (ii) schema inspection. The `image`
field is that composite, named as found. Adopted rule (CF only):
named id fields → `image` verbatim (rule tag `field:image`) →
`__` pattern in `trajectory_id` as fallback. This addendum is
recorded BEFORE any CF population's eligibility is decided and is
flagged for explicit adjudication by the Stage 8 fresh tester;
under §R12, if the tester judges this reading non-conformant, all
CF runs depending on it are invalid and the CF family reverts to
the narrow reading's outcome (task identity absent → ineligible),
which is also recorded in Part II as the counterfactual. CF-3's
independent reward finding (V contains −1.0 → §R3(v) clause 3) is
unaffected by this addendum either way.
