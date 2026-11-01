# REPORT — Area 2: Trajectory-Level Conformal Risk Control
## V4 programme final report (Stages 9–10 reporting agent), 2026-11-01

**Programme verdict: H-DATA** (§R8 decision table, row 1 — both
families NO-TEST). Under the frozen V4 registration, no counted
public population was eligible for confirmatory trajectory-level
conformal risk control, so the confirmatory programme did not
run. The census is the finding. This report and the accompanying
manuscript present exactly that result, with every number
traceable to `results/v4/census_*.json` and the frozen record in
`EXPERIMENTS_V4.md` (Parts I–II).

## 1. What was asked, what was frozen

The area's question (packet §4.3, Decision 2(b)): *does a learned
per-step signal restore a non-vacuous trajectory-level CRC
frontier on natural recorded populations that meet the field's
own data floors?* After the v1 pilot (falsifier-direction on HAL
taubench_airline; §6 below) and two design returns (V2 gate 5/10
route-back; V3 H-DATA at design stage), the V4 registration was
frozen 2026-10-31T17:33:20Z over the nine populations that
survived the O3 counting pass on counted evidence
(CoderForge-Preview in three source populations; SWE-smith
trajectories in six Claude format×model populations), and passed
Gate 9 on the second loop (Design Quality 7/10; Editor Screen
pre-score 9/12 LOW at TMLR; `TESTING_REPORT_V4_DESIGN.md`).

Frozen bars (never moved): ≥ 800 usable trajectories per
population; exact Clopper–Pearson split floors n_cal ≥ 160 and
n_test ≥ 160; disjoint fit/gate/cal/test splits 40/20/20/20 by
task group; base-failure band [0.10, 0.40] confirmatory,
(0.40, 0.50] descriptive-only; ≥ 40 successes and ≥ 40 failures
in each of gate/cal/test; outcome binarisation by a frozen
deterministic function of the observed value set (§R3(v));
Approach-C learned signal behind a mechanical length gate
(AUC ≥ 0.65, ΔAUC vs length ≥ +0.10, bootstrap 95% CI excluding
0); α = 0.10 primary; 40% abstention ceiling; venue TMLR.

## 2. The census (Stage 7 execution)

All nine populations were censused in full — 332,499 trajectories
in total (a sum over the nine registered populations: CoderForge
258,134; SWE-smith 74,365; SS-2 and SS-3 are the same trajectories
in two formats, and the CF and SS families partially share the
SWE-smith task universe). Zero parse failures anywhere; every
population's usable count reproduces the counting pass exactly.
Eligibility was decided from census quantities alone, before any
gate existed; in fact no population reached the §R4 split
realisation, so §R3 leg (c), the sample draw, and the split
formation checks were never evaluated for any population.

| Pop | Usable | Distinct tasks | Binding quantity | Outcome |
|---|---|---|---|---|
| CF-1 SWE_Rebench | 77,169 | 4,492 (image) | reward −1.0 on 255 rows (0.33%) | ineligible, §R3(v) clause 3 |
| CF-2 SWE_Smith | 148,001 | 444 (image) | reward −1.0 on 367 rows (0.25%) | ineligible, §R3(v) clause 3 |
| CF-3 R2E_Gym | 32,964 | 4,274 (image) | reward −1.0 on 278 rows (0.84%) | ineligible, §R3(v) clause 3 |
| SS-1 tool×3.7 | 17,715 | 9,143 | base failure 0.6102 | ineligible, leg (b) |
| SS-2 xml×3.7 | 18,457 | 11,824 | base failure 0.5447 | ineligible, leg (b) |
| SS-3 ticks×3.7 | 18,457 | 11,824 | base failure 0.5447 | ineligible, leg (b) |
| SS-4 tool×3.5 | 5,751 | 1,965 | base failure 0.5921 | ineligible, leg (b) |
| SS-5 xml×3.5 | 7,091 | 2,223 | base failure 0.5875 | ineligible, leg (b) |
| SS-6 ticks×3.5 | 6,894 | 2,222 | base failure 0.5863 | ineligible, leg (b) |

For SS, leg (a) (usable ≥ 800) passed for all six populations;
leg (b) alone binds. Median trajectory lengths: CF 48–59 steps;
SS 15–30 steps. Neither artefact carries per-step token counts;
the frozen token fallback (whitespace-word counts) applied
throughout (census token level 3).

### 2.1 The two barrier classes

**Barrier 1 — base rates (SS family).** All six Claude cells of
SWE-smith trajectories fail at 0.545–0.610. A population whose
base failure rate exceeds 0.50 cannot support a confirmatory
claim at α = 0.10 with a 40% abstention ceiling under the frozen
floors — the band's ceiling is a property of the method's
operating point, not a preference, and it was not relaxed.

**Barrier 2 — outcome encoding (CF family).** CoderForge's
`reward` (float64) takes three values: 1.0 (pass), 0.0 (fail),
and **−1.0**, for which no definition appears in the artefact
documentation or in the counting/census record inspected. The
registration's binarisation was frozen — deliberately, after a
Gate 9 defect — as a deterministic function of the observed
value set with no clause covering values outside [0, 1]: any
such set is census-ineligible, because assigning −1.0 to failure
or to missingness would be a post-hoc mapping invented after
seeing the data. All three CF sources contain −1.0 rows
(0.25–0.84%), so all three are ineligible under clause 3.

**Exploratory counterfactuals (EXPLORATORY — unregistered
readings, reported for interpretation only; neither encoding is
the registered one and neither fed any decision).** Excluding
the −1.0 rows, the CF failure shares are CF-1 0.4183
(descriptive band), CF-2 0.3938, CF-3 0.3605 (confirmatory band).
Counting −1.0 as failure instead gives CF-1 0.4202, CF-2 0.3953,
CF-3 0.3659 — the same band assignment in every case. For CF-2
and CF-3 the binding barrier is therefore the outcome encoding,
not the band; for CF-1 the band would have bound anyway
(descriptive tier — CF-1 is not, and is never called, a
descriptive-tier population, since the tier is a registered
status it did not attain).

### 2.2 Task identity

SS populations carry `instance_id` as a column. CF carries no
task-id column; at census step (ii) the `image` field was
identified as the artefact's per-task environment identifier
(mechanical verification on one inspected file: 148/148 rows,
`trajectory_id` minus its `_runK` suffix equals the image
string; addendum timestamped 2026-10-31T19:30:43Z, before any CF
eligibility decision). The Stage 8 adjudication (Part II, pasted
verbatim from `TESTING_REPORT_V4_RESULTS.md` §3.5) rules the
reading procedurally conformant but substantively limited:
`image` values are per-repository environment images (distinct
counts CF-1 4,492, CF-2 444, CF-3 4,274), not per-instance task
ids; grouping by them would have been task-conservative but
coarser. The reading is outcome-immaterial: under the
counterfactual narrow reading the CF populations are ineligible
on the task-identity leg instead of clause 3, and the verdict
is H-DATA under both.

## 3. Machinery evidence (supporting, not the headline)

The guarantee machinery is not the bottleneck this programme
hit. The harness (validate.py, OVERALL PASS, 48 checks) carries:
the v1 anchors (single-turn CRC: mean test risk 0.1000 at
α = 0.10; planted-dependence synthetic: S_haz mean risk 0.0154);
and the V4 synthetic prefix anchor (§R11 iteration I1), where a
planted per-step error signal was recovered by the full §R5
pipeline (gate AUC 0.995) and CRC controlled risk at α = 0.10
(test risk 0.080) — reported with its pair: synthetic abstention
was 0.420, above the 40% ceiling, so the anchor demonstrates
risk control, not an HV1 pass. Iterations I2–I5 were defined per
eligible population; none existed, and none is claimed.

## 4. Scores

- Gate 9 on the frozen V4 registration: Design Quality **7/10**;
  Editor Screen pre-score **9/12 LOW** at TMLR.
- Stage 8 fresh tester on the realised results and claims
  (`TESTING_REPORT_V4_RESULTS.md`): verdict chain VERIFIED;
  negative space clean; **Quality 6/10**; **Editor Screen 7/12
  MEDIUM** at TMLR (S1 1, S2 1, S3 2, S4 1, S5 1, S6 1). Route:
  PROCEED to Stages 9–10 with twelve mandatory fixes, all
  applied in this report and the manuscript (Fix 10's public
  deposit is a pre-submission packaging step — see §7).
- The 6/10 is below the programme's 8/10 high-distinction bar
  and the screen is MEDIUM: both are Ranadhir's explicit
  decision items at the submission gate (§7), presented, not
  smoothed over.

## 5. Falsifier bookkeeping (frozen §R9, carried without drift)

The area falsifier requires ≤ 40% abstention at target risk on
at least 2 of 3 trace corpora — (F1) HAL task family, (F2)
own-lab traces, (F3) METR runs. After v1, F1 carries a recorded
falsifier-direction result (taubench_airline, abstention 100% at
α = 0.10); F2 and F3 are untested; the falsifier has neither
fired nor been passed. V4's families (CF, SS) are not F1, F2, or
F3: V4's results count neither for nor against the area
falsifier. H-DATA is a programme verdict, not an area kill; the
formal area kill decision remains Ranadhir's.

## 6. The v1 pilot, in its place

Under the v1 registration (frozen 2026-10-31T03:21:44Z, separate
from V4), the HAL taubench_airline corpus was run end-to-end
with the frozen signal ladder: base failure 0.84, calibration
AUC 0.482, λ̂ = abstain-all at every α ∈ {0.05, 0.10, 0.20},
abstention 100% at α = 0.10 — the falsifier-direction result on
F1 recorded above. It is v1 evidence under a v1 registration,
cited here for the area's history; it is not V4 evidence, and
V4's verdict does not rest on it.

## 7. Decision packet (for Ranadhir)

Delivered: this report; the manuscript (PDF + LaTeX source,
`paper/`); the TMLR submission checklist
(`SUBMISSION_CHECKLIST_TMLR.md`). **Hard stop (§R14): nothing
has been submitted; no OpenReview account has been created; the
journal has not been contacted.** His decision items:

1. **Verify the manuscript** (standing rule: he verifies the
   final paper before any submission).
2. **Below-bar scores, explicit:** Quality 6/10 (bar 8/10);
   Editor Screen 7/12 MEDIUM at TMLR. Submission on these scores
   is his recorded-override decision under Scoring System v2, or
   the paper is revised/held.
3. **Fix 10 packaging step:** the public reproducibility deposit
   (code, registrations, census/result JSONs, tester reports) in
   a public repository — with the standing FIS scan + harness
   gates — must exist before the manuscript's availability
   statement is activated; the manuscript as delivered makes no
   public-availability claim.
4. **Area decision:** H-DATA is the V4 programme verdict. The
   formal area-level decision (kill / park / reframe Area 2, or
   commission F2/F3 work toward the area falsifier) is his.

## 8. Recommendations (labelled as recommendations; each tied to its census fact)

For publishers of agent-trajectory corpora:

1. **Document sentinel outcome values, or encode execution
   failure separately from task failure.** (Census fact: an
   undefined −1.0 reward value, 0.25–0.84% of rows, in all three
   CoderForge sources, is the sole reason three otherwise
   countable populations could not be binarised under any
   pre-registered rule.)
2. **Ship the benchmark's pass/fail as a boolean field.** (SS's
   `resolved` boolean was the one outcome encoding in this
   census that needed no interpretation at all.)
3. **Carry instance/task identifiers as a column.** (SS's
   `instance_id` column made task identity unambiguous; CF has
   no task-id column, and its environment-image field is a
   per-repository identifier of varying granularity.)

For this research programme: the frozen protocol (floors, band,
gate, binarisation discipline) is reusable unchanged; a future
registration on a corpus that documents its outcome encoding
and sits in the band would run end-to-end on the machinery as
built and anchored.

## 9. Knowledge write-back (Stage 9)

Lessons deposited for the Learning Context Graph via this
report (graph ingestion from programme records):

- **L-A2-1 (sentinel outcomes).** A public corpus's outcome
  field can carry an undocumented sentinel value (−1.0 in
  CoderForge `reward`, 0.25–0.84% of rows) that no
  pre-registered binarisation may interpret; eligibility can
  turn entirely on outcome-encoding documentation, not on
  sample size or base rate. Check the distinct-value set of the
  outcome field before designing around a corpus.
- **L-A2-2 (base-rate concentration).** Current public
  SWE-agent corpora concentrate above the 0.50 failure ceiling
  (six of six SWE-smith Claude cells at 0.545–0.610); a
  confirmatory band must be validated against counted base
  rates before a registration is written, not assumed.
- **L-A2-3 (identifier location).** Task identity may live in
  environment metadata (docker image names) rather than schema
  columns, at granularities that vary by source (444 to 4,492
  distinct values over 33K–148K trajectories); census step (ii)
  must identify and document it per population, and a coarser
  grouping is conservative but changes split arithmetic.
- **L-A2-4 (summary arithmetic).** A programme total was
  overstated by 2,636 through summary-prose arithmetic over
  correct summands, and was caught only by a fresh tester's
  recomputation: totals in prose must be recomputed from the
  artefacts, never summed mentally.

## 10. Artefact index

- Registrations/designs: `EXPERIMENTS.md` (v1), `EXPERIMENTS_V2.md`,
  `SOLUTION_DESIGN_V3.md`, `EXPERIMENTS_V3.md`, `EXPERIMENTS_V4.md`
  (+ hash chains `PREREGISTRATION_V2/V3/V4.sha256`; freeze wording:
  the V2 and V3 chains and the V4 chain's non-registration files
  verify today; V4 Part I was hash-verified at the Gate 9 loop-2
  freeze check, and Part II was appended under the registration's
  own §R13 rule).
- Counting: `COUNTING_PASS_O3.md`.
- Tester reports: `TESTING_REPORT_V3_DESIGN.md`,
  `TESTING_REPORT_V4_DESIGN.md`, `TESTING_REPORT_V4_RESULTS.md`.
- Code: `code/` (`v4lib.py`, `v4parse.py`, `v4features.py`,
  `v4signal.py`, `run_census_v4.py`, `run_population_v4.py`,
  `BUILD_LOG_V4.md`, v1 library, `validate.py` +
  `results_validate_v4_stage6.log`).
- Results: `results/v4/census_*.json`, `results/v4/result_*.json`.
- Manuscript: `paper/manuscript.tex`, `paper/manuscript.pdf`.
- Checklist: `SUBMISSION_CHECKLIST_TMLR.md`.

## 11. Submission decision (2026-11-01)

**Ranadhir Ghosh verified the final manuscript and recorded his
below-bar override on 2026-11-01 (00:11 ET):** "Verify it —
override the bar, deposit the repo, and submit to TMLR." The
verification covers `paper/manuscript.pdf` / `paper/manuscript.tex`
as delivered with this report (8 pages, all Stage 8 fixes
applied). The override is explicit, and it is on the scores
exactly as reported in §4: **Quality 6/10** against the
programme's 8/10 high-distinction bar, and **Editor Screen 7/12
MEDIUM** at TMLR. Under Scoring System v2 this recorded override
is the authorisation to submit on those scores; no score has
been revised, re-run, or smoothed in consequence.

Executed under this decision (2026-11-01, submission
preparation):

1. **Fix 10 deposit built** at
   `~/workspace/trajectory-conformal-deposit/` (to be published
   as `ranadhir19/trajectory-conformal-census`): the V4
   programme code plus the unchanged v1 library it builds on,
   the frozen V3/V4 registrations with their hash records, the
   18 census/result JSONs, both V4 tester reports, this report,
   the programme harness log, and the manuscript source. The
   deposit's own `validate.py` runs **OVERALL PASS** (83 checks:
   compile/import of the deposited code, registration hash
   chains, and recomputation of every headline census number
   from the deposited JSONs through the deposited frozen-rule
   functions — the 332,499 total, the −1.0 counts 255/367/278,
   the SS base failures, and the §R8 row-1 H-DATA probe all
   reproduce). The FIS scan of the exact deposit content was
   run and every candidate hit judged in context: all are
   benign — the author's published affiliation ("FIS Global":
   the manuscript byline and the README's author line) and this
   report's own references, in §7 and in this section, to the
   standing FIS-scan gate. No internal FIS reference (no
   internal domain, codename, path, or repository) is present;
   nothing blocks.
2. **Manuscript finalised — two changes only.** (i) The
   SWE-Critix bibliography entry was completed from the arXiv
   record: Hu, J. & Chong, C. Y. (2026), *SWE-Critix:
   Post-training generalist verifiers for assessing
   coding-agent trajectories*, arXiv:2610.13356 (the entry
   previously carried no author list and a descriptive title).
   (ii) The reproducibility paragraph was activated to name the
   deposit — https://github.com/ranadhir19/trajectory-conformal-census
   — replacing the future-tense wording. The PDF was rebuilt
   (tectonic) and content-verified by text extraction: 8 pages,
   zero unresolved references, the availability statement
   present with the URL, and all headline numbers unchanged
   (332,499 total; per-population usable counts; −1.0 counts
   255/367/278; SS base failures 0.5447–0.6102; verdict H-DATA).

**Not executed here:** GitHub repository creation/push and the
OpenReview submission itself. The deposit URL activates at the
push, which precedes the submission; the TMLR submission is the
author's act on OpenReview (`SUBMISSION_CHECKLIST_TMLR.md` items
7–10; the programme has no knowledge of his OpenReview account
state, and no account has been created by the agent). The
formal Area 2 decision (decision packet item 4 in §7 — kill /
park / reframe, or commission F2/F3 work toward the area
falsifier) is **not** part of this record and remains open.
