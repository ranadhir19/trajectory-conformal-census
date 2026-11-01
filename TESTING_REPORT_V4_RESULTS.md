# TESTING REPORT — Stage 8 Fresh Test of the V4 Execution (Results)

**Area:** 2 — Trajectory-Level Conformal Risk Control (`trajectory-conformal-risk-control`)
**Stage:** 8 of 10 (fresh tester), applied to the completed V4 execution under
`EXPERIMENTS_V4.md` (Part I frozen 2026-10-31T17:33:20Z; Part II = execution record).
**Venue scored:** **TMLR** (Ranadhir's 2026-10-31 decision, V4 §R14; zero-fee).
**Tester:** Fresh tester. I did not build the Stage 6 code, freeze the V4
registration, run the census, or author any earlier deliverable in this area.
`TESTING_REPORT_V4_DESIGN.md` (Gate 9, loop 2) was read as the record of the
freeze-time verification, not relied on as evidence for any number below.
**Method:** every binding number in §§1–2 was recomputed by me from
`results/v4/census_*.json` and `results/v4/result_*.json` on disk — not copied
from Part II, `STATE.md`, or the draft claims. Where Part II / the draft claims
and my recomputation disagree, the recomputation is stated and the disagreement
is a finding.

---

## VERDICT HEADER

- **Programme verdict chain: VERIFIED — H-DATA is the correct verdict.**
  All nine populations are ineligible on the census quantities alone; both
  families are NO-TEST; §R8 decision-table row 1 therefore yields H-DATA.
  No gate, split, calibration, or test quantity exists anywhere in the
  programme (§2). No frozen floor, band, or clause was lowered or evaded.
- **One material numeric discrepancy found:** the total trajectory count
  carried in Part II, in `STATE.md`, and in draft claim (1) — **335,135** —
  is **wrong**. The nine census files sum to **332,499** (CF 258,134 + SS
  74,365). The claimed total overstates the censused total by **2,636**
  (0.79%). This does not change any eligibility outcome or the verdict, but
  it must be corrected before any manuscript number is trusted (Fix 1).
- **Quality: 6/10** (§6.1) — below the programme's 8/10 high-distinction bar.
- **Editor Screen at TMLR: 7/12 — MEDIUM flag** (§6.2; S1 1 / S2 1 / S3 2 /
  S4 1 / S5 1 / S6 1; no zero among S1/S2/S4, so no HIGH trigger).
- **Route: PROCEED to Stages 9–10 with the mandatory fixes in §7.** No
  finding blocks writing `REPORT.md` and the manuscript on the corrected
  claims. Submission remains behind the registration's hard stop
  (Ranadhir's verification), and both a below-bar Quality score (6/10 < 8)
  and the MEDIUM screen must be presented to him as his explicit decision
  items at the Stage 10 packet — neither is silently passed.

---

## 1. Verdict-chain verification (recomputed, not trusted)

### 1.1 SS family — base failure rates recomputed from `outcome_values`

§R3(v) SS rule: success iff `resolved` is true; the observed value set is
{True, False} in all six populations, so the rule is "boolean" in every
`result_SS-*.json` — correct. Base failure = False / (True + False):

| Pop | True | False | Usable | Recomputed failure | In result file | Part II | Outcome |
|---|---|---|---|---|---|---|---|
| SS-1 | 6,906 | 10,809 | 17,715 | 10809/17715 = **0.6102** (0.61016088) | 0.61016088 ✓ | 0.6102 ✓ | > 0.50 → ineligible |
| SS-2 | 8,404 | 10,053 | 18,457 | 10053/18457 = **0.5447** (0.54467140) | 0.54467140 ✓ | 0.5447 ✓ | > 0.50 → ineligible |
| SS-3 | 8,404 | 10,053 | 18,457 | 10053/18457 = **0.5447** (0.54467140) | 0.54467140 ✓ | 0.5447 ✓ | > 0.50 → ineligible |
| SS-4 | 2,346 | 3,405 | 5,751 | 3405/5751 = **0.5921** (0.59207094) | 0.59207094 ✓ | 0.5921 ✓ | > 0.50 → ineligible |
| SS-5 | 2,925 | 4,166 | 7,091 | 4166/7091 = **0.5875** (0.58750529) | 0.58750529 ✓ | 0.5875 ✓ | > 0.50 → ineligible |
| SS-6 | 2,852 | 4,042 | 6,894 | 4042/6894 = **0.5863** (0.58630693) | 0.58630693 ✓ | 0.5863 ✓ | > 0.50 → ineligible |

Recomputed range: **0.5447–0.6102**. Draft claim (2)'s "0.545–0.610" is the
correct 3-decimal rounding of this range.

Eligibility legs (§R3), checked per population:
- **Leg (a) usable n ≥ 800: PASSES for all six** (smallest SS-4 = 5,751).
- **Leg (b) base failure ∈ [0.10, 0.40] confirmatory / (0.40, 0.50]
  descriptive: FAILS for all six** — every rate is above the 0.50 ceiling,
  so no SS population reaches even the descriptive tier.
- **Leg (c) split realisation: never reached** for any SS population, and
  correctly so — eligibility requires ALL legs, and leg (b) already fails.
  The manuscript must not imply leg (c) was tested (Fix 4).

*Record defect (minor, non-outcome):* every `result_SS-*.json` carries the
verdict string `"ineligible: census legs (a)/(b)"`. That string is the code's
combined label for the condition `n < 800 or rate outside [0.10, 0.50]`
(`run_population_v4.py`); it does not distinguish the legs. Leg (a) in fact
passed everywhere. Part II's table cites leg (b) only, which is correct; the
manuscript must do the same (Fix 2).

### 1.2 CF family — §R3(v) clause determination recomputed from `outcome_values`

Frozen §R3(v): clause 1 if every value in V coerces to exactly 0.0/1.0;
clause 2 if every value lies in [0, 1] (success iff exactly 1.0); **clause 3
(else — any value outside [0, 1], or non-numeric) → census-ineligible**.

| Pop | V (verbatim from census JSON) | −1.0 rows | −1.0 share | Clause check | Outcome |
|---|---|---|---|---|---|
| CF-1 | {0.0: 32,175; 1.0: 44,739; −1.0: 255} | 255 | 255/77,169 = **0.33%** | −1.0 ∉ [0,1] → clause 1 fails, clause 2 fails → **clause 3** | ineligible ✓ |
| CF-2 | {1.0: 89,501; 0.0: 58,133; −1.0: 367} | 367 | 367/148,001 = **0.25%** | same → **clause 3** | ineligible ✓ |
| CF-3 | {0.0: 11,782; 1.0: 20,904; −1.0: 278} | 278 | 278/32,964 = **0.84%** | same → **clause 3** | ineligible ✓ |

Each `result_CF-*.json` records `cf_reward_rule = "ineligible"` and verdict
`"census-ineligible: binarisation clause 3"` — correct in all three cases.
No base failure rate is (or may be) defined for a CF population under the
registration: clause 3 returns ineligibility, not a rate. The −1.0 share
range across the family is **0.25%–0.84%**, as draft claim (2) states.
Median/mean steps and step coverage in the census JSONs match Part II
(CF-1 59.0/62.8, cov 0.9997; CF-2 48.0/53.3, cov 1.0; CF-3 55.0/59.1, cov
0.9999 — recomputed readings agree at the recorded precision); token level
is 3 (whitespace-word counts) for all nine populations.

### 1.3 Usable counts vs `COUNTING_PASS_O3.md`; the total discrepancy

Every usable count reproduces the counting pass **exactly**:

- CF (per-source rows counted in O3 §2): CF-1 77,169 ✓; CF-2 148,001 ✓;
  CF-3 32,964 ✓. Parse failures 0; usable = in-file in all three.
- SS (per-cell trajectories counted in O3 §3): SS-1 17,715 ✓; SS-2 18,457 ✓;
  SS-3 18,457 ✓; SS-4 5,751 ✓; SS-5 7,091 ✓; SS-6 6,894 ✓. Distinct-task
  counts also reproduce O3 exactly: 9,143 / 11,824 / 11,824 / 1,965 /
  2,223 / 2,222 ✓. Parse failures 0 in all six.
- CF distinct-image counts are census quantities (O3 reserved them):
  CF-1 4,492; CF-2 444; CF-3 4,274 — these match Part II and are the
  evidence base for §3 below.

**Total: 77,169 + 148,001 + 32,964 + 17,715 + 18,457 + 18,457 + 5,751 +
7,091 + 6,894 = 332,499** (CF subtotal 258,134; SS subtotal 74,365).
Part II's eligibility section ("total trajectories censused: 335,135"),
`STATE.md`'s Stage 7 completion entry ("335,135 trajectories"), and draft
claim (1) all carry **335,135 — overstated by 2,636**. I found no population,
file, or subtotal in the census record from which 335,135 can be derived;
it is an arithmetic error in the summary text, not a counting difference
(every summand is individually correct and verified above). Two further
wording qualifications the manuscript must carry with the corrected total
(Fix 1): (i) 332,499 is a **sum over nine registered populations**, not a
count of distinct trajectories — SS-2 and SS-3 are the same trajectories in
different formats (identical outcome counts, §1.1; O3 warned of exactly
this), so the xml and ticks renderings of the claude-3-7 pool are each
counted once per population by design; (ii) CF and SS partially share the
SWE-smith task universe (§R9 item 8 cap applies to any cross-family phrasing).

### 1.4 §R8 decision-table application

- Confirmatory-eligible populations: **none**. Descriptive-tier
  populations: **none** (SS rates all > 0.50; CF populations have no
  definable rate under clause 3, hence no tier).
- Family verdicts (§R8: a family with no confirmatory-eligible population
  is NO-TEST): **CF = NO-TEST; SS = NO-TEST** ✓.
- Decision table, evaluated in order: row 1 (both families NO-TEST) is the
  first and only row that fires → **programme verdict H-DATA** ✓.
  Rows 2–3 are unreachable. No population has a PASS/FAIL/FAIL(ALERT)
  state; no guarantee alert can exist (no test split was ever evaluated).
- Population order (§R3 ascending base-failure) and descriptive processing
  order are moot: no eligible or descriptive population exists to order.
- §R8's H-DATA paragraph is satisfied verbatim: "the confirmatory programme
  does not run; the census record is the finding; STOP; floors and bands
  are not lowered post-freeze for any reason." No floor or band was lowered
  at any point in the record I inspected.

**Section 1 conclusion:** the verdict chain is correct in every leg, clause,
and table step. The only discrepancy in the entire chain is the summary
total (§1.3): **335,135 claimed vs 332,499 recomputed, Δ = +2,636**.


---

## 2. Negative-space audit and freeze integrity

### 2.1 Negative space — no gate, split, calibration, or test quantity exists

Complete inventory of `results/v4/` as found (45 JSON files + one cache dir):

- `census_<pop>.json` ×9 — the §R3 census aggregates (§1).
- `census_progress_<pop>.json` ×9 — per-file checkpointing state
  (`done_files` + the running aggregate that becomes the census file).
- `groups_<pop>.json` ×9 — per-task trajectory counts (task id → n), written
  by the census code as the §R4 sampling *input* for a later phase.
- `groupcomp_<pop>.json` ×9 — per-task [n, n_not-1.0 / n_False] pairs, the
  same census-side grouping auxiliary.
- `result_<pop>.json` ×9 — each contains only the nested census record plus
  the population's rule/verdict scalars (`cf_reward_rule` / `ss_resolved_rule`,
  `base_failure` for SS only, `verdict`). I searched all nine for the terms
  auc / lambda / gate / split / abstention / threshold: **none occurs**.
- `_cache/` — empty of retained trajectories (the census deletes each raw
  file after processing, per §R13).

**Absent, as required:** no `splits_*.json`, no `sample_*.jsonl`, no
`sampled_tasks_*.json`, no `features_*.npz` anywhere under the area's
`results/` tree (searched beyond `results/v4/` as well). This is consistent
with the code path: `run_population_v4.py:run()` returns immediately after
writing the ineligible result for CF (clause 3, before any `base_failure` is
computed) and for SS (legs (a)/(b), before `build_groups` / `phase_sample` /
`assign_splits` are reached). The gate, frontier, UB-arm, and monitor code
in that file is unreachable for every population in this programme and was
never executed on V4 data.

Two clarifications so the record is not over-read in either direction:
(i) `groups_*` / `groupcomp_*` are **not** split quantities — they contain
no split assignment, no sampled set, no proportion check, and no class-count
leg-(c) evaluation; they are per-task counts of the kind the census itself
needs for §R3(iv). (ii) `groupcomp_*`'s CF "fail" count treats reward ≠ 1.0
(hence also −1.0 rows) as not-success for grouping-arithmetic purposes. That
auxiliary never fed any eligibility decision — CF eligibility is computed
in `run_population_v4.py` solely from `outcome_values` via the frozen
`v4lib.binarise_cf_reward` function — and it fed no split, because no split
phase ran. It must nevertheless not be quoted in the manuscript as a CF
failure count (Fix 5).

**Negative space: CONFIRMED CLEAN.** There is nothing to tune and, on the
artefacts, nothing was tuned.

### 2.2 Freeze integrity — what can and cannot be verified about V4 Part I

Commands run by me in the area directory:

- `sha256sum -c PREREGISTRATION_V3.sha256` → **OK for all three files**
  (EXPERIMENTS_V3.md, SOLUTION_DESIGN_V3.md, COUNTING_PASS_O3.md), exit 0.
  The V3 chain still verifies; V3 remains byte-identical to its freeze.
- `sha256sum -c PREREGISTRATION_V2.sha256` → **OK for both files**
  (SOLUTION_DESIGN_V2.md, EXPERIMENTS_V2.md), exit 0. The V2 chain still
  verifies.
- `sha256sum -c PREREGISTRATION_V4.sha256` → **EXPERIMENTS_V4.md: FAILED;
  the other two files OK** — exactly the expected pattern, **not** evidence
  of tampering: the recorded hash `1565664b…` is the freeze-time hash of the
  Part-I-only file, and Part II appends (which §R13 and the file's own
  closing note authorise: "Part II … is appended after execution and may
  not alter Part I") necessarily change the whole-file hash. The current
  whole-file hash is `a8eb6a88…`.

**What can be verified:** (a) the V2 and V3 chains verify today; (b) the two
non-registration files in the V4 chain (SOLUTION_DESIGN_V3.md,
COUNTING_PASS_O3.md) still verify today; (c) the Gate 9 report
(`TESTING_REPORT_V4_DESIGN.md` §1) verified the V4 freeze at loop 2 — hash
`1565664b…` matched, and Part II then contained no execution content;
(d) on my read, the present file's Part I ends at its own "End of frozen
pre-registration (Part I)" marker before Part II begins, and Part I contains
no census quantity, gate result, or outcome.
**What cannot be verified:** Part I's byte-identity to its freeze cannot be
re-established cryptographically from the current file alone — no
Part-I-only hash was preserved separately from the whole-file freeze hash.
Part I integrity therefore rests on (c)+(d): the loop-2 Gate 9 verification
at freeze time plus the absence of any internal sign of post-hoc editing.
Stages 9–10 must state it in exactly those terms if the manuscript's
methods section makes a freeze-integrity claim (Fix 6) — "hash-verified"
without qualification would overstate what is checkable today.

---

## 3. Adjudication of the flagged interpretation — the §R12 question (CF task identifier)

### 3.1 The facts

- The frozen §R3 task-identifier requirement seeks, in priority order:
  `instance_id`, `issue_id`, `task_id`, then "a (repository, issue)
  composite if the artefact carries both fields"; if no task identifier
  exists, the population is census-ineligible, "recorded, never worked
  around." §R5 assigns parser mapping choices to census step (ii) schema
  inspection, "made from schema inspection (census step (ii)) only, never
  from outcomes," recorded in `code/BUILD_LOG_V4.md`.
- Stage 6's initial build-log reading sought a SWE-bench `<owner>__<repo>-
  <issue>` pattern inside `trajectory_id`, then `image`.
- During census step (ii), inspection showed CF rows carry no named id
  column; the `image` field was identified as the task-identity carrier.
  Mechanical verification recorded in the addendum: on one inspected file
  (148 rows), `trajectory_id` minus its `_runK` suffix equals the `image`
  string (with `/` and `:` mapped to `_`) on **148/148 rows, 0 mismatches**.
- The correction is timestamped **2026-10-31T19:30:43Z** in the
  `BUILD_LOG_V4.md` addendum, expressly "before any CF eligibility
  decision," and was flagged at the time for this adjudication. Partial
  CF-3 progress gathered under the old extraction was discarded and the
  CF census relaunched under the corrected parser (Part II).
- Final granularity evidence (my recomputation from the census JSONs):
  CF-1 **4,492** distinct images / 77,169 rows (≈17.2 rows per image);
  CF-2 **444** / 148,001 (≈333.3 per image); CF-3 **4,274** / 32,964
  (≈7.7 per image). Every usable row in all three populations carries an
  image (`n_with_task` = usable in each census file; rule tag
  `field:image` on all rows).

### 3.2 Ruling (a) — procedural character

**This was a conformant census-step-(ii) schema identification in its
procedural character, and it is not a §R12 event.** Grounds: (1) §R12
governs *post-gate* changes; no gate existed, or ever came to exist, in
this programme — the correction happened inside the very step (census
(ii)) whose frozen job is schema identification. (2) §R5 expressly assigns
parser mapping choices to that step, requiring only that they be made from
schema inspection, never from outcomes, and recorded in the build log —
all three conditions are met on the record (mechanical 148/148 identity
check; timestamped addendum; flagged for adjudication at the time).
(3) No frozen rule, bar, band, seed, or selection rule was changed by it,
and no eligibility quantity had been recorded for any CF population when
it was made. The four §R12 clauses are therefore not the operative test;
had they been applied by analogy, clauses (2) outcome-blind evidence and
(3) no-free-parameter-move would pass, and clause (1)'s spec anchor is
§R3(ii) + §R5's assignment of mapping choices to census inspection.

### 3.3 Ruling (a′) — substantive limit of the identification

**The identification must not be described as the discovery of a
per-instance task-identifier field, and on a strict reading of §R3's
priority-4 wording it goes beyond the frozen text.** The priority list's
fourth rung is a "(repository, issue) composite **if the artefact carries
both fields**." CoderForge carries no separate repository and issue
fields; `image` is a single field whose value is a per-repository /
per-environment image name. The final distinct counts prove the
granularity is not per-instance: for CF-2, 444 images over 148,001
trajectories cannot be instance ids for a source whose instances are
synthetic SWE-smith tasks (Part II itself records this correction);
CF-1's 4,492 (≈17 runs/image) is likewise coarser than per-instance;
only CF-3's 4,274 hash-suffixed images are near-instance-level. What the
`image` field *is*, on the evidence, is a **conservative grouping key**:
each trajectory maps to exactly one image, and the 148/148 check supports
(but, being one inspected file, does not prove for all 672 CF files) that
all runs of a task share one image — so grouping by image could never
have split one task across two splits (no leakage), but it would have
merged distinct tasks into single §R4 groups, changing the realised
group-size structure (most extremely in CF-2) and thereby the sample /
split realisation that leg (c) judges. Had any CF population been
eligible, this reading would have required Ranadhir-level scrutiny before
any split was formed on it. None was, so the question is moot for V4 —
but the manuscript may not upgrade the reading retroactively.

### 3.4 Ruling (b) — effect on outcomes: none, under either reading

Counterfactual (the initial narrow SWE-bench-pattern reading): the
pattern extraction found no task id in CF rows (Part II step-(ii) record),
so under §R3's task-identifier requirement all three CF populations would
have been **census-ineligible on the task-identity leg** (identifier
absent → task-disjoint splits cannot be enforced → ineligible, "never
worked around"). Adopted reading: all three CF populations are
**ineligible under §R3(v) clause 3** (§1.2). Either way: CF = NO-TEST.
SS is untouched by the question (its `instance_id` is a named field,
priority 1). Programme verdict under both readings: **row 1 → H-DATA,
unchanged**. The interpretation is therefore outcome-immaterial in fact,
not merely by assertion — Part II's "immaterial" claim is verified.

### 3.5 Ruling (c) — verbatim-ready text for Part II and the manuscript

The following paragraph is my ruling in a form Stages 9–10 may paste
verbatim into Part II (as the Stage 8 adjudication entry) and adapt into
the manuscript's methods/limitations:

> **Stage 8 adjudication of the CF task-identifier reading (§R12 question).**
> The correction of the CF task-identifier extraction to the `image` field
> (`code/BUILD_LOG_V4.md` addendum, 2026-10-31T19:30:43Z, recorded before
> any CF eligibility decision) is ruled a conformant census-step-(ii)
> schema identification in its procedural character: §R5 assigns parser
> mapping choices to census step (ii), the identification rested on
> outcome-blind mechanical evidence (148/148 rows: `trajectory_id` minus
> its `_runK` suffix equals the `image` string), and no frozen rule,
> parameter, or recorded quantity was changed by it; §R12, which governs
> post-gate changes, does not apply, no gate having existed. Substantively,
> however, `image` is not a per-instance task identifier and is not the
> (repository, issue) composite of §R3's priority list, which presupposes
> both fields carried separately: the final distinct counts are CF-1
> 4,492 images over 77,169 trajectories, CF-2 444 over 148,001, and CF-3
> 4,274 over 32,964 — per-repository environment images of varying
> granularity, near-instance-level only for CF-3. Grouping by `image`
> would have been task-conservative (no task could straddle splits) but
> coarser than task grouping, and no split was ever formed on it. The
> reading changes no outcome: under the counterfactual narrow
> (SWE-bench-pattern) reading the CF populations are ineligible on the
> task-identity leg; under the adopted reading they are ineligible under
> §R3(v) clause 3; the CF family is NO-TEST and the programme verdict is
> H-DATA under both.

Manuscript disclosure required (Fix 3): the initial pattern reading and
its replacement; the addendum's timestamp relative to eligibility; the
scope of the mechanical verification (one inspected file, 148 rows — not
a whole-artefact proof); the three distinct counts with the granularity
statement above; and the counterfactual outcome.


---

## 4. Execution-corrections review

Three pre-result code corrections are recorded in Part II, plus one
Stage 6 harness-expectation correction. Reviewed individually:

**(1) HF revision strings (pre-census).** The first SS launch crashed at
its first API call (`RevisionNotFoundError`): Stage 6 code had extended
the counting pass's short shas into full-length strings that were in no
source. *Record:* adequate — Part II's pre-census entry names the root
cause, the resolution route (Hub API), and the verification (prefixes
match O3; `lastModified` matches O3 exactly for both repos — CF
2026-02-26, SS 2025-07-19). I confirm the pinned full shas
(`060fca96cf723b2ebab3181e9e59fafd273df3cb` CF;
`08e109b4a59eaeebf80e4675cd125d42e7ac99a4` SS) are exactly the revision
strings recorded in all nine census JSONs. *Timing:* no data row had been
read and no census quantity existed — nothing was decided after seeing a
result this could affect. *Frozen-rule contact:* none — the correction
implements §R2's requirement (artefacts at the counted revisions); it
does not interpret or move it.

**(2) SS aggregation merge (pre-result).** The first post-fix SS pass
checkpointed usable = 0 / n_in_file = 0: the SS branch of
`run_census_v4.py` never merged the per-file aggregate (`agg_add_file`
missing). *Record:* adequate — diagnosis from the checkpoint itself, fix,
deletion of the poisoned SS-1 progress file, relaunch from scratch, all
in Part II. I confirm the current code contains the merge in both the CF
and SS paths. *Timing:* the only "result" seen was an impossible zero
(contradicted on its face by O3's counted 17,715 for the affected cell) —
a crash-equivalent diagnostic, outcome-blind in the §R12 sense; no
`census_<pop>.json` existed when it was caught, and no eligibility was
decided from it. The strongest evidence the fix is clean is §1.3: every
final SS count reproduces O3 exactly, which a contaminated merge could
not do. *Frozen-rule contact:* none — a code defect against the census's
own aggregation intent.

**(3) CF task-id extraction (census step (ii)).** Fully adjudicated in
§3. *Record:* adequate in form (timestamped build-log addendum, Part II
step-(ii) entry with counterfactual, consolidated entry, explicit flag
for Stage 8) and now closed by the §3.5 ruling. *Timing:* recorded before
any CF eligibility decision; a partial CF-3 reward observation (V already
containing −1.0 in the first files) predates it in the record, but the
correction could not affect the clause-3 determination, which depends
only on `outcome_values` — and §3.4 shows it could not affect any outcome
under either reading. *Frozen-rule contact:* **this is the only one of
the three that touches the interpretation of a frozen rule** (§R3's
priority list / §R5's mapping assignment), which is precisely why it
needed adjudication; the ruling (§3.2–3.3) sustains the procedure and
limits the substance.

**(4) Additional, Stage 6: harness test expectation (F2).** The F2
single-family check as first written expected SINGLE-FAMILY MIXED for
(primary PASS, NO-TEST family, replication PASS); frozen §R8 row 2 assigns
SINGLE-FAMILY SUPPORT to that configuration. The implementation already
followed the frozen table; the *test* was corrected to the frozen text and
the harness re-run to OVERALL PASS (48 checks, exit 0 —
`results_validate_v4_stage6.log`, which I inspected: all Stage F checks
PASS, including the 16-combination verdict-table tests in substance).
Pre-result, no frozen rule or code behaviour changed. Record adequate;
this correction is a point *in favour* of the programme's discipline —
the test was fixed to the registration, not the registration to the test.

**Iteration-log closure (§R11) — honest accounting, not a budget
violation.** §R11 requires a minimum of 5 measured iterations *before any
test-split evaluation*, with I2–I5 defined per eligible population (gate
measurement, fix loop, rehearsal — all on that population's splits). No
population was eligible, no split exists, and no test-split evaluation
occurred, so the budget's precondition never arose; §R8's H-DATA rule
("the confirmatory programme does not run … STOP") governs the stop.
I1 was completed and measured (Stage F6 synthetic prefix anchor: AUC
0.995; CRC risk 0.080 at α = 0.10 — §5, claim 4). Part II's closure entry
states I2–I5 "never existed" and expressly declines to dress the census up
as the iteration budget ("reported as what it is, not dressed as the
iteration budget"). That is the correct accounting. The plateau rule is
likewise moot (it routes on gate-margin sequences that do not exist).

---

## 5. Claims scoring

Verdicts are against the record as I recomputed it. "Supported" means the
claim as drafted is exactly what the record shows.

### Claim (1) — H-DATA over nine populations — **OVERSTATED (one number wrong; verdict itself supported)**

The verdict content is fully supported: nine counted public populations,
two families, none confirmatory-eligible under the frozen §R3 legs/clauses,
H-DATA by §R8 row 1 (§1.4). But the claim's trajectory total, **335,135, is
false**: the census files sum to **332,499** (CF 258,134 + SS 74,365),
an overstatement of 2,636 (§1.3). Corrected, and with the §1.3 wording
qualifications (sum over registered populations; SS-2/SS-3 are format
renderings of the same trajectories), the claim is supported verbatim.
As drafted it may not be used.

### Claim (2) — binding barriers are specific and data-side — **SUPPORTED**

SS: all six cells' base failure rates recomputed at 0.5447 / 0.5447 /
0.5863 / 0.5875 / 0.5921 / 0.6102 (§1.1) — the drafted "0.545–0.610" is the
correct rounding of the recomputed range 0.5447–0.6102, and leg (b) is the
binding leg for every cell (leg (a) passes everywhere). CF: V contains
−1.0 in all three sources at 255/77,169 = 0.33% (CF-1),
367/148,001 = 0.25% (CF-2), 278/32,964 = 0.84% (CF-3) — range 0.25%–0.84%
as drafted — and clause 3 is a property of the frozen function, not a
judgement call: no clause of §R3(v) assigns a meaning to a value outside
[0, 1], so no pre-registered binarisation may interpret it. One wording
guard (Fix 7): "undocumented" should be stated as the record supports it —
no definition of the −1.0 value appears in the artefact documentation or
counting record the census inspected — not as a universal claim about
every document the publisher has ever issued.

### Claim (3) — exploratory CF readings — **SUPPORTED as exploratory arithmetic, with two binding caveats**

Recomputed from the census `outcome_values`:

| Pop | Excluding −1.0: 0.0/(0.0+1.0) | Band | Counting −1.0 as failure: (0.0+−1.0)/all | Band |
|---|---|---|---|
| CF-1 | 32175/76914 = **0.4183** | descriptive (0.40, 0.50] | 32430/77169 = **0.4202** | descriptive |
| CF-2 | 58133/147634 = **0.3938** | confirmatory [0.10, 0.40] | 58500/148001 = **0.3953** | confirmatory |
| CF-3 | 11782/32686 = **0.3605** | confirmatory [0.10, 0.40] | 12060/32964 = **0.3659** | confirmatory |

These match the drafted figures (0.394 / 0.361 / 0.418 excluding; 0.395 /
0.366 / 0.420 including) at the drafted precision, and the inference drawn
— for CF the outcome encoding, not the band, is the binding barrier — is
arithmetically sound: under *both* counterfactual encodings the band
assignment of every CF population is unchanged, so the band is not what
excludes them. Caveats, both mandatory (Fix 5): (i) both readings are
**exploratory counterfactual encodings**, neither is a binarisation under
the registration — the "counting −1.0 as failure" reading is exactly as
unregistered as the exclusion reading, and the manuscript must present
the pair symmetrically, never either one as "the" CF failure rate;
(ii) CF-1 is **not** a descriptive-tier population under the registration
(descriptive tier requires a definable base rate inside (0.40, 0.50];
CF-1 has no definable rate) — "in the descriptive band" must always carry
the word "exploratory" and never be shortened to "descriptive population."
The mid-census exploratory note in `STATE.md` quoting ≈0.32 for CF-2 was a
partial-file reading and is superseded by 0.3938; it must not be quoted.

### Claim (4) — machinery is not the bottleneck — **SUPPORTED, with one mandatory qualification**

`results_validate_v4_stage6.log`: validate.py OVERALL PASS, anchors A + B
recovered (A: mean test risk 0.1000 at α = 0.10, abstention 0.753; B:
dependent-world S_haz risk 0.0154, abstention 0.454) and Stage F6 synthetic
prefix anchor: **AUC(S_haz) = 0.995; CRC test risk 0.080 at α = 0.10** on
synthetic data — the drafted numbers are exact. The v1 HAL pilot
(`results/pilot_results.json`) did run end-to-end to a falsifier-direction
verdict (n = 50; calibration AUC 0.482; λ̂ = abstain-all at all α; test
abstention 1.0 at α = 0.10). **Qualification (Fix 8):** the synthetic
anchor's abstention at α = 0.10 is **0.420 — above the 40% ceiling** — so
the anchor demonstrates risk *control* (0.080 ≤ 0.10) and signal recovery,
not an HV1-style PASS; any phrasing implying the synthetic run "passed"
the programme's own (risk, abstention) pair bar would be false. With that
stated, the claim's substance — the failure is located in the data
(§1), not in machinery that has never run — is supported. The manuscript
must also keep the pilot in its §R9 place: a v1 result on a spent corpus,
not V4 evidence.

### Claim (5) — publisher recommendations — **SUPPORTED as recommendations (normative, not findings)**

Each recommendation maps to a verified census fact: document sentinel
outcome values / encode execution failure separately (the CF −1.0 value,
§1.2 — a value plausibly encoding execution failure is exactly what
clause 3 cannot distinguish from a reward); ship a boolean pass field
(the SS `resolved` boolean is what made the SS census fully determinate,
in contrast to CF's `reward`); carry instance ids as columns (SS's
`instance_id` column vs CF's absence of any id column, §3). These are
recommendations to dataset publishers, and the manuscript must present
them as such — supported by the census as motivating evidence, not as
empirical results in their own right.

### Claim (6) — area falsifier untouched; formal kill is Ranadhir's — **SUPPORTED**

§R9 bookkeeping verified against the record: the area falsifier's corpora
are F1 (HAL) / F2 (own-lab) / F3 (METR); V4's CF/SS families are none of
them and count neither for nor against the 2-of-3 (§R9 item 3); F1 carries
v1's falsifier-direction result, F2/F3 remain untested, so the falsifier
has neither fired nor been passed; a formal area kill remains Ranadhir's
recorded decision under FRAMEWORK Gate 3. The claim as drafted states
exactly this and nothing stronger. The manuscript must not let "H-DATA"
and "kill" appear as synonyms anywhere (Fix 9).

**Claims summary:** (1) OVERSTATED as drafted (total only; corrected form
supported); (2) SUPPORTED; (3) SUPPORTED as labelled exploratory, with
caveats; (4) SUPPORTED with the abstention qualification; (5) SUPPORTED as
normative recommendations; (6) SUPPORTED. No claim is UNSUPPORTED; no
claim requires new data or new computation to cure — every defect is a
writing defect.


---

## 6. Scores

### 6.1 Quality: **6/10**

Assessed per Scoring System v2 Part A (correctness, reproducibility from
artefacts, honesty of claims, depth of demonstration), for a manuscript
built on exactly the §5 claims.

- **Correctness — strong, with one material error.** Every binding number
  in the verdict chain recomputes exactly from the deposited census files
  (§1.1–1.2): six SS rates to the last recorded digit, three CF clause
  determinations, all usable/task counts against O3. Against that, the
  programme's own summary total is arithmetically wrong by 2,636 (§1.3)
  and appears in three places (Part II, STATE, draft claim 1) — a
  headline-surface number a reviewer can falsify with a pocket calculator
  from the paper's own table. Correctable in writing; counted here
  because this score is of the claims as drafted.
- **Reproducibility — strong.** Public artefacts at pinned, verified
  revisions; census JSONs deposited per population; code path auditable
  (I traced the early-return logic that guarantees the negative space,
  §2.1); validate.py OVERALL PASS with anchors recovered. Residue: the
  programme's artefacts live in the area workspace, not yet in a public
  deposit a TMLR reader can fetch (Fix 10), and Part I freeze integrity
  is attested, not re-verifiable, in the terms of §2.2.
- **Honesty of claims — strong.** Exploratory quantities are labelled
  exploratory in Part II and were never eligibility inputs; the
  counterfactual task-id outcome is on the record; corrections were
  logged when made, including one (the F2 test expectation) where the
  programme corrected its own test to match the frozen text rather than
  the reverse; the iteration closure declines to inflate the census into
  an iteration budget (§4). The §3.3 granularity limit on the `image`
  reading is the one place the underlying record (build-log/code
  comments calling `image` a "per-task environment identifier") states
  more than the final evidence supports — cured by disclosure, §3.5.
- **Depth of demonstration — the binding limit.** The realised paper is
  an eligibility census over nine populations plus machinery evidence
  that is synthetic (anchors) or spent (v1 pilot). That is the honest
  result the frozen discipline produced, and its specificity (two named,
  quantified, data-side barriers; a falsifiable publisher-recommendation
  set) is what lifts it above a bare null. But there is no real-data
  frontier, no gate measurement, and no population on which the method
  is exercised — a depth ceiling no writing can remove, only frame.

Why not 7 (the Gate 9 design pre-score): the design score priced a
programme that could still have produced a frontier; the realised
claims carry a false headline total and a thinner empirical core. Why
not 5: the verdict chain itself is exactly right, independently
recomputed, and the negative space is clean — the execution is more
trustworthy than the summary text written over it.

**6/10 is below the 8/10 bar.** Any submission therefore requires
Ranadhir's explicit recorded below-bar decision at the Stage 10 packet,
per Scoring System v2's submission rule.

### 6.2 Editor Screen at TMLR: **7/12 — MEDIUM**

Scored per Scoring System v2 Part B, from the dossier's TMLR evidence
(§§1.1–1.2: the Action Editor's on-record acceptance of incremental
theory over CRC/LTT where correctness, positioning and evidence are
strong; TMLR's demonstrated genre of "the guarantee is limited in
exactly this way; here is what survives, with the frontier measured")
applied to the *realised* claims — not to the Gate 9 design pre-screen
(9/12 LOW), which was scored before any outcome existed and anticipated
a frontier paper among the possible results. The deltas from that
pre-screen are S1 (2→1) and S6 (2→1), both explained below; the screen
is re-scored because the manuscript's actual genre is now known.

| # | Sub-score | Value | Grounds (one line) |
|---|---|---|---|
| S1 | Venue fit vs recent contents | **1** | Within TMLR's demonstrated conformal/risk-control contents and its limits-paper genre (dossier §1.2), but the modal TMLR article demonstrates a method on real data — a census-only feasibility audit with no real-data run is unlike it, so fit must be argued, not assumed |
| S2 | Contribution legibility | **1** | The advance is statable in one sentence ("no counted public SWE-agent population is eligible for confirmatory trajectory-level CRC under pre-registered floors, for two specific data-side reasons"), but the front matter must also carry the machinery evidence, the exploratory CF readings, the recommendations, and the falsifier bookkeeping — extraction takes effort |
| S3 | Novelty positioning | **2** | Nearest learned-scorer work named with a precise, honest delta (§R10: Lightman et al. 2023; Wang et al. 2024; Xi et al. 2025, AgentPRM; SafetyDrift), and the feasibility-under-frozen-floors framing is positioned as the contribution, not overclaimed as a better scorer |
| S4 | Methods-credibility signals | **1** | Headline numbers are the author's own and I recomputed them from public artefacts at pinned revisions plus the deposited census JSONs — but there is as yet no public deposit of code + census artefacts a reader can fetch, and the drafted headline total was wrong (Fixes 1, 10 cure the second and mitigate the first) |
| S5 | Presentation polish & genre conformance | **1** | The limits/feasibility genre is TMLR-shaped (dossier §1.2), but no manuscript exists to polish-check, and the composite narrative (census + synthetic machinery + v1 pilot + recommendations) is a known presentation risk that the single-contribution front matter of Fix 11 must resolve |
| S6 | Tier calibration | **1** | TMLR remains the right tier for this work's theory depth, but the §1.2 exemplars each delivered an achievable half on real data; this paper delivers the limit without the surviving construction, so the sell at TMLR is possible but hard |
| **Total** | | **7/12** | **MEDIUM** (total 6–8; no zero among S1/S2/S4, so no HIGH trigger; total ≤ 5 is also not met) |

No HIGH flag arises, so no screen override is required. The MEDIUM flag
plus the below-bar Quality score are nevertheless Ranadhir's explicit
decision items at Stage 10 (§6.1). This screen is venue-specific to
TMLR and transfers nowhere; if Stages 9–10 change the front matter
materially (title/abstract/contribution framing), the screen should be
re-run on the actual screen surface before the packet is delivered.

---

## 7. Mandatory fixes for Stages 9–10 (numbered; all are writing/packaging fixes — none requires new data or computation)

1. **Correct the total everywhere.** Replace 335,135 with **332,499**
   (CF 258,134 + SS 74,365) in the manuscript, in `REPORT.md`, and — by
   an appended erratum entry, not a silent edit — in `EXPERIMENTS_V4.md`
   Part II and `STATE.md`. In the manuscript, phrase the total as a sum
   over nine registered populations and disclose that SS-2 and SS-3 are
   the same trajectories in different formats (identical outcome counts),
   and that CF/SS partially share the SWE-smith task universe (§R9
   item 8 cap).
2. **SS binding leg cited as leg (b) only.** Wherever SS eligibility is
   discussed, state that leg (a) passed for all six populations
   (usable n ≥ 5,751) and leg (b) alone binds; do not import the
   `result_SS-*.json` combined "legs (a)/(b)" code label into prose.
3. **Task-identifier disclosure.** Include the §3.5 adjudication
   paragraph (verbatim into Part II; adapted into the manuscript) and
   the §3.5 disclosure list: initial pattern reading, addendum timestamp
   2026-10-31T19:30:43Z (pre-eligibility), 148-row scope of the
   mechanical verification, distinct counts 4,492 / 444 / 4,274 with the
   per-repository-environment granularity statement, and the
   counterfactual (task-identity-leg ineligibility; verdict unchanged).
   Never call `image` a per-instance task id.
4. **Leg (c) honesty.** State explicitly that no population reached the
   §R4 split realisation, so leg (c), the sample draw, and the split
   formation checks were never evaluated for any population; eligibility
   failed at §R3(v) clause 3 (CF) and leg (b) (SS) before that point.
5. **Exploratory-encoding discipline.** Keep the EXPLORATORY label on
   every CF counterfactual rate (0.4183 / 0.3938 / 0.3605 excluding
   −1.0; 0.4202 / 0.3953 / 0.3659 counting −1.0 as failure) in the
   abstract, results, and tables; present both encodings symmetrically
   as unregistered counterfactuals; never call CF-1 a descriptive-tier
   population; never quote the superseded mid-census ≈0.32 CF-2 figure;
   never quote `groupcomp_*` counts as CF failure counts.
6. **Freeze-integrity wording.** Any freeze claim in the manuscript must
   use the §2.2 terms: V2/V3 chains and the V4 chain's non-registration
   files verify today; V4 Part I was hash-verified at the Gate 9 loop-2
   freeze check (`TESTING_REPORT_V4_DESIGN.md`) and Part II was appended
   under §R13 — not "the registration file hash-verifies" simpliciter.
7. **"Undocumented" scoped.** State the −1.0 finding as: no definition of
   the −1.0 reward value appears in the artefact documentation or the
   counting/census record inspected; per-population shares are 0.33%
   (CF-1), 0.25% (CF-2), 0.84% (CF-3).
8. **Synthetic-anchor qualification.** Wherever AUC 0.995 / risk 0.080 is
   reported, report the pair honestly: abstention at α = 0.10 on the
   synthetic anchor is 0.420, above the 40% ceiling — risk control is
   demonstrated, an HV1 PASS is not. Keep the v1 HAL pilot in its §R9
   place (spent corpus, v1 registration), never as V4 evidence.
9. **Falsifier bookkeeping verbatim.** Carry §R9 items 1–4 into the
   manuscript without paraphrase drift: CF/SS are not F1/F2/F3; V4
   counts neither for nor against the area falsifier; the falsifier has
   neither fired nor been passed; H-DATA is a programme verdict, not an
   area kill; the formal kill decision is Ranadhir's.
10. **Public reproducibility deposit at packaging.** Deposit the V4 code
    (`v4lib/v4parse/v4features/v4signal/run_census_v4/run_population_v4`),
    `validate.py` + its log, all `results/v4/census_*.json` and
    `result_*.json`, `EXPERIMENTS_V4.md`, and this report in a public
    repository (or TMLR supplementary material) named in the manuscript's
    availability statement — and make the statement only once the deposit
    exists. This is the cure path for S4.
11. **Single-contribution front matter.** Title and abstract lead with
    the one-sentence census advance (S2 grounds, §6.2); machinery
    evidence, recommendations, and falsifier bookkeeping appear as
    supporting sections, not as co-headline contributions; the abstract
    must not lead with the synthetic AUC.
12. **Publisher recommendations labelled as recommendations.** Present
    claim (5)'s three items under a recommendations heading, each tied
    to its census fact (CF −1.0; SS boolean `resolved`; SS `instance_id`
    column vs CF's absence of one), never as experimental findings.

---

## 8. Route verdict

**PROCEED — Stages 9 and 10 may write `REPORT.md` and the TMLR
manuscript on the §5 claims, subject to all twelve mandatory fixes in
§7.** No finding blocks that route:

- The programme verdict **H-DATA** is verified end-to-end (§1.4) and the
  negative space is clean (§2.1): there is no hidden gate, split, or test
  result that a manuscript could accidentally (or deliberately) draw on.
- The single material defect — the 335,135 total — is an arithmetic
  error in summary prose over individually correct summands; it changes
  no outcome and is cured by Fix 1.
- The one contested interpretation is adjudicated (§3), is
  outcome-immaterial under both readings, and is cured by disclosure
  (Fix 3).

**What this route does NOT authorise:** submission. The chain still ends
at the Stage 10 decision packet for Ranadhir's verification (V4 §R14 hard
stop). That packet must present, as his explicit decision items: the
below-bar Quality score (**6/10** vs the 8/10 bar), the Editor Screen
(**7/12 MEDIUM** at TMLR, with the six sub-scores), and the §3
adjudication. No part of this report is a submission decision, an
override, or a venue change.

*End of Stage 8 fresh-tester report on the V4 execution. This report
modifies no other file; its §3.5 paragraph and §7 fixes are addressed to
Stages 9–10 for application.*
