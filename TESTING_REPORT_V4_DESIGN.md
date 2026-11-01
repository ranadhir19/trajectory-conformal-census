# TESTING REPORT — Gate 9 Design-Stage Fresh Test (V4 Pre-Registration, Loop 2)

**Area:** 2 — Trajectory-Level Conformal Risk Control (`trajectory-conformal-risk-control`)
**Gate:** FRAMEWORK Gate 9 (design-stage testing, Improvement Plan P6) — applied to
`EXPERIMENTS_V4.md` Part I (frozen 2026-10-31T17:33:20Z) as the Stage 5 exit
artefact, before any Stage 6 coding. **This is loop 2, the final loop the
programme's mandate allows** (V4's own Activation paragraph, §"Activation
conditions (c)"): a route-back here exhausts the mandate's loops, stops the
programme and is reported, with no V5 written under this mandate.
**Tester:** Fresh tester; did NOT author `EXPERIMENTS_V4.md`,
`EXPERIMENTS_V3.md`, `SOLUTION_DESIGN_V3.md`, or any earlier deliverable in
this area. `TESTING_REPORT_V3_DESIGN.md` was read as the defect specification
V4 claims to repair, not relied on as evidence.
**Date:** 2026-10-31.
**Venue scored:** **TMLR** (decided venue, V4 §R14 and Authority paragraph;
zero-fee per FRAMEWORK Gate 7 as recorded there; fee status not re-verified,
per tasking).
**What this tester did NOT do:** no coding, no experiments, no census, no gate
evaluation, no outcome computation, no data downloads. Data contact was limited
to the metadata/counts already on disk in `COUNTING_PASS_O3.md`, the frozen
artefacts, and one bibliographic sanity check on the AgentPRM citation (§4.1).

---

## VERDICT HEADER

- **Design Quality pre-score: 7/10** — at or above the Gate 9 floor of 6/10.
- **Editor Screen pre-score at TMLR: 9/12 — LOW flag** (total ≥ 9; no zero
  sub-score anywhere; none of S1/S2/S4 = 0).
- **Route: PASS (proceed to Stage 6).** Both Gate 9 conditions are met:
  Design Quality ≥ 6/10 AND the Editor Screen flag is not HIGH.

The three defects that blocked V3 (N1 verdict overlap, N2 unfrozen CF primary
outcome, N3 unspecified split/RNG procedure) are repaired in their blocking
substance (§2). Two repairs are partial at the level of wording or of
descriptive-tier detail (N1's blanket anti-rescue sentence, refuted in the
single-family row's scope by V4's own table; N6's SQ3/token residues). Every
residual found in this pass — including all new defects in §5 — is classified
**non-blocking**, with reasons stated per item: none of them leaves a
confirmatory verdict, a primary outcome, an eligibility leg, or any frozen bar
to post-freeze choice. No frozen bar of V3 was moved or relaxed (§3). Because
the route is PASS, the loop-2 exhaustion note above does not trigger; it is
recorded here because the mandate requires the tester to state it.

---

## 1. Freeze integrity — VERIFIED (all three chains)

Run in the area directory by this tester:

- `sha256sum -c PREREGISTRATION_V4.sha256` — **OK for all three files**:
  `EXPERIMENTS_V4.md`
  (`1565664b8c7dec724b306254807cdbd4a827b2c0e2dd95e045e23730d935dbdd`),
  `SOLUTION_DESIGN_V3.md`, `COUNTING_PASS_O3.md`. Exit status 0.
- `sha256sum -c PREREGISTRATION_V3.sha256` — **OK for all three files**:
  `EXPERIMENTS_V3.md`
  (`9e68440316730c7924c5bd6864e9b7c3b7b1f7b4a0cd44b18dfe669822f80d02` — the
  hash in its own chain, so **EXPERIMENTS_V3.md is unchanged / byte-identical
  to its freeze, as V4's Lineage and §R13 claim**), `SOLUTION_DESIGN_V3.md`,
  `COUNTING_PASS_O3.md`. Exit status 0.
- `sha256sum -c PREREGISTRATION_V2.sha256` — **OK for both files**:
  `SOLUTION_DESIGN_V2.md`, `EXPERIMENTS_V2.md`. Exit status 0. V4's claim
  that the V2 hashes were re-verified at its freeze is consistent with the
  artefacts as they stand now.

Timing/content consistency: the V4 freeze (2026-10-31T17:33:20Z) post-dates
the V3 freeze it succeeds (17:22:31Z) and the Gate 9 V3 design report it
answers; the file ends with Part I's closing note and **Part II contains no
execution content** — no V4 census quantity, gate result, or experiment
artefact exists in the registration, as it must be pre-execution. A
frozen-after-results registration would have been an automatic FAIL; that is
not what happened here.

**Freeze: VERIFIED.**

## 2. Defect-repair audit — N1–N7 against TESTING_REPORT_V3_DESIGN.md §5

Judgement scale: REPAIRED / PARTIALLY REPAIRED / NOT REPAIRED, each with its
blocking status stated separately, so that "partial" is never allowed to blur
into "blocking" or vice versa.

### N1 — PARTIALLY REPAIRED (blocking part fully repaired; one non-blocking overstatement remains)

*V3 defect:* §R8's SUPPORTED (a population count, ≥ 2 PASS spanning both
families) and KILL (both family primaries FAIL) could co-fire, and SUPPORTED
was reachable by the replication rescue §R8 claimed to forbid.

*V4 text claimed as repair (§R8):* family verdict = "its **primary
population's** state"; programme verdicts are a "decision table — exhaustive
and mutually exclusive; evaluate in this order" over the two family verdicts;
SUPPORTED (row 3) is now "both primaries PASS"; "Both primaries FAIL or
FAIL(ALERT) → **V4 KILL**".

*Enumeration (this tester, all 16 combinations).* Family verdicts are read as
PASS / FAIL / FAIL(ALERT) / NO-TEST, with FAIL(ALERT) counting as FAIL wherever
the table says FAIL (§R8 alert paragraph: "it counts as FAIL in the table
above" — the distributive reading of row 3's "Both primaries FAIL or
FAIL(ALERT)", i.e. each primary ∈ {FAIL, FAIL(ALERT)}):

| CF \ SS | PASS | FAIL | FAIL(ALERT) | NO-TEST |
|---|---|---|---|---|
| **PASS** | SUPPORTED | MIXED | MIXED | SINGLE-FAMILY MIXED / SUPPORT † |
| **FAIL** | MIXED | V4 KILL | V4 KILL | SINGLE-FAMILY FAILURE |
| **FAIL(ALERT)** | MIXED | V4 KILL | V4 KILL | SINGLE-FAMILY FAILURE |
| **NO-TEST** | SINGLE-FAMILY MIXED / SUPPORT † | SINGLE-FAMILY FAILURE | SINGLE-FAMILY FAILURE | H-DATA |

† Row 2 only: primary PASS **and** ≥ 1 replication PASS in the tested family →
SINGLE-FAMILY SUPPORT; primary PASS with no replication PASS (or none run) →
SINGLE-FAMILY MIXED (§R8 row 2).

Count check: row 1 = 1 combination (H-DATA); row 2 = 6 combinations (3 tested
states × 2 orientations), with the PASS cells split by the binary replication
bit into exactly one verdict each; row 3 = 9 combinations (1 SUPPORTED,
4 KILL, 4 MIXED). **Every one of the 16 combinations maps to exactly one
programme verdict; no combination maps to two.** 

*Counterexample attempts:*
1. **The V3 killer configuration is dead.** CF primary FAIL, SS primary FAIL,
   one later CF population PASS and one later SS population PASS: under V3
   this satisfied KILL and SUPPORTED simultaneously. Under V4, SUPPORTED
   requires both *primaries* PASS, so this configuration is **V4 KILL only**.
   No rescue.
2. **Replication-invariance in rows 1 and 3 — proved.** Both primaries PASS
   with *all* replications FAIL is still SUPPORTED; both primaries FAIL with
   replications PASS is still KILL (attempt 1). In the both-tested rows a
   replication result changes nothing, in either direction — anti-rescue,
   symmetric, as claimed.
3. **The blanket claim is nevertheless REFUTED in row 2's scope.** §R8's
   family-verdict bullet states replications "**never change the family
   verdict or the programme verdict, in either direction**", and the Lineage
   repeats "replication results never change any verdict in either direction".
   Counterexample configuration: CF primary PASS, SS NO-TEST, no CF
   replication PASS → **SINGLE-FAMILY MIXED**; add one CF replication PASS,
   all else identical → **SINGLE-FAMILY SUPPORT**. The replication changed
   the programme verdict. (The family verdict — PASS — did not change.) V4's
   own table paragraph concedes the exception ("the table is a function of
   the two family verdicts … and, **only in row 2**, of replication PASSes in
   the tested family"), so the registration contradicts its own summary
   sentence but not its operative table. The row-2 dependence is itself
   inherited, deliberate design — it is V3's single-family two-PASS bar,
   renamed — and it cannot rescue a *failed* primary (row 2: primary FAIL or
   FAIL(ALERT) → SINGLE-FAMILY FAILURE regardless of replications).

*Judgement:* the blocking defect — co-firing verdicts and a post-results
choice of headline verdict — is **fully repaired**: the table plus its
concluding sentence determine a unique verdict for every configuration, and
an executor never has to choose between the bullet and the table because the
table is the section's operative, ordered rule. What remains is an
overbroad summary sentence, carried as non-blocking new defect X1 (§5).
Hence PARTIALLY REPAIRED at the level of the registration's text, REPAIRED at
the level of the defect that routed V3 back.

### N2 — REPAIRED (blocking)

*V3 defect:* the CF `reward` binarisation was a census-time selection
procedure ("the mapping applied" recorded at census), not a frozen function.

*V4 text (§R3(v)):* "let V be the set of distinct non-null values of `reward`
observed over the population's rows at census… · if every value in V coerces
to exactly 0.0 or 1.0 (booleans coercing as False→0, True→1): success iff the
value is 1; · else if every value in V lies in [0, 1]: success iff the value
is exactly 1.0… · else (any value outside [0, 1], or non-numeric values): the
population is census-ineligible". Plus: "No other clause exists; no clause is
chosen by a human after seeing V".

*Totality probe (this tester), case by case:*

| V | Clause reached | Defined outcome |
|---|---|---|
| {0.0, 0.5, 1.0} | Clause 1 fails (0.5); clause 2 holds (all ∈ [0, 1]) | Success iff value = 1.0 exactly; 0.5 is a partial pass = failure. **Defined.** |
| {True, False} | Clause 1, by the stated boolean coercion False→0, True→1 | Success iff True. **Defined.** |
| {0, 2} | Clause 1 fails (2); clause 2 fails (2 ∉ [0, 1]); clause 3 (else) | Census-ineligible, H-DATA leg, V recorded. **Defined.** |
| Nulls only (every row's `reward` null) | V = ∅ as a set of *non-null* values | No usable trajectories exist (§R3(iii): usable requires a non-null outcome), so usable n = 0 fails eligibility leg (a) (n ≥ 800): population ineligible, H-DATA leg. **Defined at registration level** — no base rate is ever computed over an empty usable set. (See X4 on the vacuous-truth wording of clause 1 over ∅.) |
| String values, e.g. {"pass", "fail"} | Clauses 1–2 fail (non-numeric); clause 3 names "non-numeric values" | Census-ineligible. **Defined.** (See X4 on numeric-looking strings.) |
| Mixed, e.g. {0.0, 1.0, "x"}; NaN; +∞ | Clause 3 is a structural *else*, not conditioned on its parenthetical examples | Census-ineligible. **Defined.** |

No non-empty numeric/boolean value set falls through: clauses 1–2 are
predicates and clause 3 is an else, so the function is total on its intended
domain, and it was written sight-unseen (the census "only *observes* the
distinct-value set and applies the rule whose clause matches it"). The SS
leg is likewise hardened: "any non-boolean, non-null value set makes the
population census-ineligible". The clause-2 rationale is anchored, not
invented: success = full pass is tied to the SWE-Critix construction in which
the pooled pass count 155,144 equals the `filtered_reward1` view (counting
pass §2 verifies that identity at the artefact). **N2: REPAIRED.** Two
wording edges (empty V; what "coerces" means for string-typed values) are
carried as non-blocking X4 — neither can arise on a population that survives
the usable-trajectory leg with a numeric/boolean `reward` column, which is
the only domain the census will meet if the artefact matches its documented
schema (§R3(ii) records the field as found).

### N3 — REPAIRED (blocking)

*V3 defect:* split-assignment algorithm unspecified; RNG-stream identity
ambiguous ("seed 20261031" bare in §§R5/R6); no proportion tolerance.

*V4 text (§R4):* "all RNG streams in this registration are named, never a
bare seed: for population index j, stream k is numpy `default_rng` with
`SeedSequence([20261031, j, k])`, j = the population's position in the §R2
list, CF-1 = 1 … SS-6 = 9; stream ids: 1 = sample draw, 2 = split assignment,
3 = stacking folds, 4 = gate bootstrap, 5 = monitor/descriptive resampling
if any".

*Grep audit (this tester, every seed/RNG mention in EXPERIMENTS_V4.md):*

| Use | Section | Stream | Status |
|---|---|---|---|
| Sample draw | §R4 | Stream 1 (`SeedSequence([20261031, j, 1])`) | Named ✓ |
| Split assignment permutation | §R4 steps 2–3 | Stream 2 | Named ✓ |
| Stacking 5-fold cross-fitting by task group | §R5 | "stacking folds drawn from stream 3, §R4" | Named ✓ |
| Gate bootstrap (1,000 resamples, percentile CI) | §R6 | "population stream 4, §R4" | Named ✓ |
| Monitor / descriptive resampling | §R4 stream list | Stream 5, "if any" | Reserved; no operative section in V4 specifies an unstreamed resampling — §R6's betting-CS monitor and repeated-look comparator are deterministic given the stream, so no use is left bare ✓ |
| Hashed text features | §R5(e) | Not RNG: `hashlib` blake2b, digest 8, mod 128; "`PYTHONHASHSEED`-dependent hashing is prohibited" | Deterministic ✓ |

The only remaining "seed" mentions are non-uses: §R12 clause (3) (a change may
move no "seed") and the §R12 bug class "hash-seed mismatch vs the frozen
seed". **No operative RNG use in the registration is left on a bare seed.**

*Assignment algorithm determinism.* §R4 steps 1–4 freeze: stratum
classification (all-success / all-failure / mixed); within-stratum order by
the stream-2 permutation; stratum processing order **all-failure, mixed,
all-success**; assignment of each group, whole, "to the split with the
largest remaining trajectory deficit, deficit(split) = target(split) −
assigned(split)", target = proportion × sample n, proportions **fit 0.40 /
gate 0.20 / calibration 0.20 / test 0.20**; **ties break in the fixed order
fit, gate, calibration, test**. Given the stream-2 ordering, every step is a
function: deficit is defined, tie-breaks are total (the fixed split order
breaks every deficit tie; the permutation totally orders groups within a
stratum), and whole-group overshoot is absorbed by the deficit rule itself
(an overshot split's deficit falls and stops attracting groups). This is the
pseudocode precision the V3 report demanded.

*Tolerance coherence.* Step 4's formation checks — "every realised split's
trajectory share is within **±3 percentage points** of its target proportion,
and §R3 leg (c) holds. If either check fails… the population is recorded as a
split-realisation failure (H-DATA leg)" — are **checks on the frozen
algorithm's output, not a re-draw licence**, and §R4's sample paragraph is
explicit: a sample whose realisation fails leg (c) "makes the population
ineligible (H-DATA leg), it is not re-drawn — re-drawing until splits pass
would be selection", and step 4 closes "there is nothing to re-draw". The
tolerance and the no-re-draw rule are coherent: the tolerance decides
eligibility, never a second attempt. (Residual: the permutation *primitive*
and the consumption order of stream 2 across the three strata are not named
beyond "a permutation drawn from the population's split stream", and the
stacking-fold assignment rule is named only by its stream — the same level of
abstraction the V3 tester accepted as precise for the sample draw, with split
files frozen to disk at formation under §R4. Carried as non-blocking X5.)
**N3: REPAIRED.**

### N4 — REPAIRED (non-blocking in V3; now closed)

*V3 defect:* a population with an alert (test-risk CP CI entirely above α)
was neither PASS nor FAIL as defined; §R8's count was not always computable.

*V4 text (§R8):* population states are "exhaustive" — PASS / FAIL /
**FAIL(ALERT)**; the alert paragraph assigns the final disposition: if the run
"is shown — by spec-vs-code evidence, without using test outcomes beyond the
alert itself — to have not implemented the frozen spec, the run is logged
**invalid**, re-executed once, and the population's state is read from the
re-run. In every other case… the population's final state is **FAIL(ALERT)**:
it counts as FAIL in the table above, and the alert itself is a headline
result reported wherever the population is reported."

*Consistency check (every verdict-counting site):* the per-population FAIL
bullet expressly excludes the alert case ("test risk > α **without a
guarantee alert**"), so PASS / FAIL / FAIL(ALERT) partition the HV1-failure
space; §R8 row 2 counts "primary FAIL or FAIL(ALERT) → SINGLE-FAMILY FAILURE";
row 3 counts both-primaries FAIL-or-FAIL(ALERT) → KILL and
exactly-one-PASS → MIXED (which therefore covers PASS × FAIL(ALERT));
§R7's descriptive paragraph states descriptive populations carry "never a
verdict, never part of any count", so no alert can leak in from that tier.
The §R9 item-3 use of "a FAIL" is about the *area* falsifier count, where
FAIL(ALERT) populations count neither for nor against — consistently.
Terminology residues (the states bullet's summary "HV1 failed" and the alert
paragraph's provisional label "state **ALERT** on occurrence") are carried as
non-blocking X2/X3; the specific clauses partition the space and the final
state is always assigned, so §R8's count is now always computable after the
diagnosis disposition. **N4: REPAIRED.**

### N5 — REPAIRED (non-blocking in V3; now closed)

*V3 defect:* the single-family case had no defined KILL/failure verdict and
reused programme verdict names.

*V4 text (§R8 row 2):* exactly one family NO-TEST → primary PASS + ≥ 1
replication PASS = **SINGLE-FAMILY SUPPORT**; primary PASS with no replication
PASS (or none run) = **SINGLE-FAMILY MIXED**; primary FAIL or FAIL(ALERT) =
**SINGLE-FAMILY FAILURE**; and the row closes the naming loophole: "None of
these is a programme SUPPORTED or KILL, and none completes any two-family
count (defect N5 repair)." The rows are complete over the tested family's
states: PASS is split by the replication bit (PASS-with / PASS-without,
including "none run"), and FAIL and FAIL(ALERT) are both named, with
replication PASSes unable to rescue either (see N1, attempt 3). Both-NO-TEST
is row 1 (H-DATA), consistent with the §R8 H-DATA bullet ("no population is
confirmatory-eligible under §R3"). The second half of V3's N5 — descriptive
execution order — is answered in combination: §R3 orders descriptive-tier
populations "after all confirmatory populations, in the same ascending
order", and §R11 states iterations I2–I5 "run per population"; the two are
not cross-referenced in one sentence (non-blocking X7). **N5: REPAIRED.**

### N6 — PARTIALLY REPAIRED (non-blocking in V3; all remaining residues non-blocking and descriptive/minor in scope)

(a) **Descriptive-tier quantities — REPAIRED.** §R7 now enumerates them
"exactly": "the §R3 census quantities; the §R4 sample/split realisations (if
formed); the §R6 gate quantities on the gate split; and per α in the grid,
λ̂ from the calibration split with the **calibration-split** (risk,
abstention) pair, labelled CALIBRATION-SPLIT in every record and in the
manuscript — never a test number, never a verdict, never part of any count".
The α grid is §R6's frozen {0.05, 0.10, 0.20}, incorporated by "per α in the
grid". This is the definition V3's N6(a) found missing.
(b) **SQ3 stratum field — PARTIALLY REPAIRED.** §R1 now defines the field by
kind and gives the size rule: "if census step (ii) finds a
repository-identifier field on the population's rows, strata are that field's
values; otherwise the population has no strata and SQ3 is not exercised on
it. SQ3 is exercised only where ≥ 2 strata each hold ≥ 40 calibration
trajectories after the §R4 realisation". Residue: §R3(ii)'s enumerated census
schema list still does **not** include a repository-identifier field among
the fields it records (outcome, step-record, task-identifier, native
error/status, token-count), and no candidate-name priority is given if more
than one repository-like field exists — so *which* field the census "finds"
still involves a schema-identification judgement (see X6). SQ3 is
descriptive-only and exercised only on HV2-passing populations, so the
residue touches no confirmatory quantity.
(c) **AgentPRM citation — REPAIRED.** See §4.1: full authors-lead, title and
arXiv identifier now in §R10, and verified correct.
(d) **Token field — PARTIALLY REPAIRED.** §R5 `n_tokens` is now a frozen
three-level priority: "(1) the artefact's per-step token-count field, if
census step (ii) finds one (candidate names, in order: a per-step usage /
token_count / n_tokens field…); (2) else, the sum of per-message token counts
over the step's messages…; (3) else, the whitespace-word count of the step's
text", with "no other quantity may be substituted after census". The
cross-level discretion V3 flagged is closed. Residue: *within* level (1), a
`usage` container's subfields (prompt / completion / total) are not
prioritised, and level (2) does not order multiple per-message count fields
(see X6). `n_tokens` feeds three of the 22 structured features (position/
length block §R5(b)); it is not an outcome, gate, or eligibility quantity.
**N6 overall: PARTIALLY REPAIRED** — every element is materially better
specified than V3 and none of the residues reaches a load-bearing decision.

### N7 — REPAIRED (non-blocking in V3; claim cap now stated where claims are licensed)

*V3 defect (b):* §R2 barred treating SS splits as independent replications
but was silent on cross-family overlap (CF-2's source is SWE_Smith; SS's
tasks are SWE-smith instances), so "spanning both families" could be upgraded
by implication into task independence.

*V4 text:* new §R9 item 8 — "the two families partially share an underlying
task universe (different scaffold and model, overlapping tasks). Cross-family
agreement is therefore agreement across scaffold and model on a partially
shared task universe — **no claim in any product of this programme may
describe CF and SS as independent task replications**" — **and the cap is
carried into the licensing sentence itself**, as the tasking required §R8 to
show: SUPPORTED licenses the primary claim "**subject to the §R9 item-8 claim
cap**". §R9 item 4's restatement of what SUPPORTED needs ("both primaries
PASS") does not repeat the cap, but §R9 item 8's prohibition is
product-wide ("in any product of this programme"), so no claim surface is
left uncapped. Residues: §R9 item 8's "the census records, per population,
the task-identifier space" is not an enumerated §R3 census quantity ((ii)
records the field name, (iv) the distinct count — not the identifier set or
an overlap size), and the W2 half of V3's N7 (a realised *gate-size*
eligibility leg) was not added — §R7 does report split sizes, and at the
§R4 sample size (gate target ≈ 800, §3 below) the analogy floor is not
load-bearing, exactly as the V3 tester held in its §3.5. Both are carried as
non-blocking X8. **N7: REPAIRED.**

## 3. Regression check — V4 vs V3 in substance: NO FROZEN BAR MOVED OR RELAXED

Full-text diff of `EXPERIMENTS_V4.md` against `EXPERIMENTS_V3.md` was run by
this tester. Outside the header/Lineage, the N1–N7 repair sites (§§R1, R3,
R4, R5, R7, R8, R9, R10), and bookkeeping renames (`results/v3/` →
`results/v4/`, `BUILD_LOG_V3.md` → `BUILD_LOG_V4.md`, "V3 KILL" → "V4 KILL",
"V3 only" → "this programme only"), the frozen text is identical in substance.
Bar-by-bar:

| Frozen bar | V3 | V4 | Status |
|---|---|---|---|
| Floors, exact-CP | §R3(c): n_cal ≥ 160 ∧ n_test ≥ 160 | §R3(c): identical text | **UNCHANGED** |
| Class counts | ≥ 40 successes ∧ ≥ 40 failures in each of gate/cal/test (§R3(c)) | Identical | **UNCHANGED** |
| Eligibility band | [0.10, 0.40] confirmatory; (0.40, 0.50] descriptive; outside [0.10, 0.50] ineligible | Identical (§R3) | **UNCHANGED** |
| Splits | fit 40% / gate 20% / cal 20% / test 20% | §R4 step 3: fit 0.40 / gate 0.20 / cal 0.20 / test 0.20 | **UNCHANGED** |
| Gate bars | AUC ≥ 0.65 ∧ Δ ≥ +0.10 ∧ percentile-bootstrap 95% CI (1,000 resamples) excludes 0 | §R6: identical; only the bootstrap's seed is now named as stream 4 (N3) | **UNCHANGED** |
| α / δ / ceiling | α = 0.10 primary; grid {0.05, 0.10, 0.20}; δ = 0.05; abstention ≤ 40% | §§R1, R6, R8, R9.7: identical | **UNCHANGED** |
| Feature budget | D ≤ n_fit/2 = 160; 22 structured + 128 hashed = 150; heads and hyper-parameters as in §R5 | §R5: identical numbers; only the stacking seed is now named as stream 3 (N3) | **UNCHANGED** |
| Seed base | 20261031 | 20261031 — now as `SeedSequence([20261031, j, k])` (N3 stream refinement; V3 was never executed, so no V3 draw, split, or result exists whose stream this could betray; §R12's no-seed-move clause governs changes *inside* a registration, not a successor's disclosed construction) | **UNCHANGED (base)** |
| Iteration budget | Minimum 5 measured iterations (I1–I5), plateau rule | §R11: identical | **UNCHANGED** |
| Fix-vs-tuning | §R12 four clauses + closed bug-class list | §R12: carried verbatim in substance (diff shows no change) | **UNCHANGED** |

*The two disclosed clarifications — judged:*

1. **Operative-window restatement (§R3) — CLARIFICATION, not a disguised
   relaxation.** The restated paragraph changes no leg: (a), (b) and (c) are
   textually identical to V3, the band [0.10, 0.40] is identical, and leg (c)
   was *already* a realised-count check in V3 ("the §R4 sample/split
   realisation yields… each of gate / calibration / test contains ≥ 40…").
   The paragraph only does the arithmetic the V3 tester (its §2, elaboration
   1) said the registration should have stated: SOLUTION_DESIGN_V3 §2's
   operative window [0.25, 0.40] was derived at the floor split size
   (n = 160 ⇒ ≥ 40 failures needs a realised fraction ≥ 0.25); at the §R4
   realised split size (n_split = 800) the same frozen ≥ 40 rule needs only a
   0.05 realised fraction (40/800 = 0.05 — recomputed by this tester). A
   population in [0.10, 0.25) passing leg (c) at the sampled size was already
   possible under V3's frozen text; V4 says so. Nothing that was ineligible
   under V3's legs becomes eligible under V4's.
2. **The 4,000-sample (§R4) — NOT NEW IN V4, and not a relaxation.** The
   whole-group draw "until the cumulative trajectory count first reaches
   ≥ 4,000 (the crossing group is included whole); if the population's usable
   n ≤ 4,000 the sample is the whole population" is **identical in V3's §R4**
   (diff-verified; the only §R4 sample-paragraph change is the stream
   construction, N3). It raises realised split sizes far above the floors; it
   lowers nothing. Its interaction with the operative window is item 1.

**No silent deviation that relaxes any bar was found.**

## 4. Supporting verifications

### 4.1 §R10 AgentPRM citation — READS CORRECTLY (verified)

V4 §R10: **Xi et al. (2025), "AgentPRM: Process Reward Models for LLM Agents
via Step-Wise Promise and Progress" (arXiv:2511.08325)**. Sanity check run by
this tester: arXiv:2511.08325 is that exact title, first author Zhiheng Xi
(with 14 co-authors), submitted 11 Nov 2025 — so "Xi et al. (2025)", the
title, and the identifier all read correctly, and the full title + identifier
disambiguate it from a distinct, similarly-named AgentPRM framework paper by
a different author. The characterisation in §R10 (PRMs for multi-step agent
trajectories, scoring steps to guide search / test-time selection) matches
the paper's stated contribution (step scores from promise + progress, TD/GAE
training). The V3 thinness ("AgentPRM, 2025", no authors/venue/identifier) is
cured. The rest of §R10 is unchanged from V3, whose four-work positioning and
honest delta the V3 tester verified (§4.1 of that report); the delta
paragraph still disclaims the stronger claim in terms ("**not** a better
step-scorer; if the scorer itself were the claim, Math-Shepherd and AgentPRM
would be the bar and this design would not clear it").

### 4.2 Feasibility on the counted evidence — SS-4 arithmetic recomputed

Smallest surviving population, SS-4 (tool × claude-3-5-sonnet-20241022;
5,751 trajectories / 1,965 distinct tasks = 2.93 trajectories/task, counting
pass §3): the §R4 draw takes whole task groups in stream-1 order until the
cumulative count first reaches ≥ 4,000 (≈ 1,367 groups at the population
mean; realised sample ∈ [4,000, 4,000 + largest group − 1]; satisfiable,
since 5,751 ≥ 4,000). Split targets at a 4,000 sample: fit 1,600 / gate 800 /
calibration 800 / test 800; the new ±3pp check bounds realised gate/cal/test
to [680, 920], so §R3(c)'s n_cal, n_test ≥ 160 floors are met with a > 4×
margin even at the tolerance edge. Class counts at any confirmatory base
rate in [0.10, 0.40]: an 800-trajectory split holds in expectation 80–320
failures and 480–720 successes — both ≥ 40 with margin; the stratum-ordered
greedy assignment (§R4) is what protects this under task-clustering. CF
populations (smallest CF-3: 32,964 trajectories) satisfy the same arithmetic
a fortiori. The V3 tester's caveat stands and is not hidden by V4: these
margins are conditional on *usable* retention under §R3(iii), which only the
census will measure; if retention shrank a sample, leg (c) is checked on
realised counts and the failure mode is honest ineligibility, never a silent
pass. Per-population base rates remain census-reserved by design
(`COUNTING_PASS_O3.md` reserved exactly that leg) — feasibility here is
structural, as it was when the V3 tester credited it. **No named population
was found where the frozen rules are jointly unsatisfiable.**

### 4.3 Falsifier bookkeeping (§R9) — STILL EXACT

§R9 items 1–7 are unchanged in substance from V3 (diff-verified), whose
bookkeeping the V3 tester checked word-for-word against `EXPERIMENTS.md` §P2
(area falsifier quoted verbatim; corpora F1 HAL / F2 own-lab / F3 METR) and
`EXPERIMENTS_V2.md` §V8 (corpus 1's verdict stands, §V8.2; the 2-of-3 reckoning
deferred to separately registered F2/F3 runs, §V8.3): F1 carries one
falsifier-direction result (taubench_airline, AUC 0.482, abstention 100% at
α = 0.10), F2/F3 untested, the area falsifier neither fired nor passed, and
V4's CF/SS results count neither for nor against it (§R9 item 3). V4's edits
to §R9 are exactly two: renames (V3 → "this registration" / V4 KILL), and the
new item 8 (N7, §2 above). Item 4 now states the count correctly under the
repaired table: "SUPPORTED needs both primaries PASS". **No bookkeeping
error was found.**

## 5. New-defect hunt — NO NEW BLOCKING DEFECT FOUND

Read fresh, with attention to text adjacent to the V4 edits (§§R3–R9, R13).
All findings are **non-blocking**; each is stated with the reason it cannot
change a confirmatory verdict, outcome, eligibility leg, or bar. They are
carry-notes for Stage 6/7 (to be logged as pre-result interpretation notes in
`code/BUILD_LOG_V4.md` where an interpretation is needed — never as amendments
to the frozen registration):

- **X1 (§R8, family-verdict bullet + Lineage vs §R8 row 2) — wording
  inconsistency.** The blanket "replications never change any verdict" is
  refuted in row 2's scope (full analysis at N1, attempt 3). Non-blocking:
  the operative decision table and its concluding sentence determine a
  unique verdict for every configuration; the specific, ordered table
  governs over the summary bullet, and no configuration is left ambiguous.
- **X2 (§R8, population-states bullet) — summary overlap.** The states bullet
  summarises FAIL as "gate passed but HV1 failed", which read alone would
  include the alert case (risk > α with CI entirely above α) and overlap
  FAIL(ALERT). Non-blocking: the per-population FAIL bullet immediately
  above it excludes the alert case expressly, and the alert paragraph
  assigns the final state; the partition holds on the section's full text.
- **X3 (§R8, alert paragraph) — provisional label; second-alert silence.**
  The paragraph first puts the population "in state **ALERT** on occurrence",
  a label the exhaustive states list does not contain; the final state is
  FAIL(ALERT) (or a state read from the single authorised re-run). It also
  does not say in words what happens if the *re-run itself* alerts.
  Non-blocking: "re-executed **once**" caps the loop, and reading the re-run
  under the same state rules yields FAIL(ALERT) with no second diagnosis
  authorised; the provisional label never enters a count, because states are
  final states ("**ends in** exactly one state").
- **X4 (§R3(v)) — two wording edges in the CF function.** (i) Over V = ∅
  (nulls only), clause 1 is vacuously true; the registration-level outcome is
  nevertheless ineligibility via usable n = 0 / leg (a) (see N2 table).
  (ii) "Coerces" is not typed: for a *string-typed* column, a numeric-looking
  string ("1") could in principle be read as float-parseable (clause 1) or as
  a non-numeric value (clause 3). Non-blocking: the second reading is the one
  §R3(ii)'s schema identification supports (values take the artefact's type;
  clause 3 expressly names non-numeric values), `reward` is documented as a
  numeric test outcome (SWE-Critix construction, counting pass §2), and
  Part II must record V verbatim, so any such case would be visible on the
  record, not silently chosen.
- **X5 (§§R4–R5) — draw-primitive residues.** The stream-2 permutation
  primitive (e.g. `Generator.permutation`), its consumption order across the
  three strata, the pre-permutation group list order, and the stacking-fold
  assignment rule (beyond stream 3) are not named; §R5 also mislabels stream
  3's context once ("population split-stream discipline: stacking folds drawn
  from stream 3" — the stream *id* is unambiguous, the label is a copy
  residue). Non-blocking: this is the abstraction level the programme has
  twice accepted for seeded draws, no eligibility or verdict rule depends on
  which conforming primitive the Stage 6 code uses, and §R4 freezes the
  realised split assignments to disk at formation (`results/v4/splits_<pop>.json`),
  immutable thereafter.
- **X6 (§R1 + §R3(ii); §R5 `n_tokens`) — the N6 residues.** The repository
  field for SQ3 is not added to §R3(ii)'s recorded schema list and has no
  candidate priority (see N6(b)); token subfields within §R5 level (1) (a
  `usage` container's prompt/completion/total) and multiple per-message
  counts at level (2) are not ordered (see N6(d)). Non-blocking: SQ3 is
  descriptive-only on HV2-passing populations; `n_tokens` is one feature
  input among 22 structured features; neither touches an outcome, a gate, a
  threshold, or a verdict.
- **X7 (§§R3/R7 vs §R6) — descriptive λ̂ gate-condition not restated.** §R7's
  descriptive list reports "per α in the grid, λ̂ from the calibration split"
  without restating §R6's gate-failure consequence ("no threshold is
  calibrated for it"), and §R11 does not cross-reference the descriptive
  iteration order (see N5). Non-blocking: §R6's consequence is stated
  population-generally, descriptive results are labelled CALIBRATION-SPLIT
  and are "never a verdict, never part of any count", so a conforming
  execution calibrates no λ̂ for a gate-failed descriptive population; the
  gap is one of cross-referencing, not of permission.
- **X8 (§R9 item 8 vs §R3; V3 N7(a) residue) — documentation legs not
  enumerated.** Item 8's "the census records, per population, the
  task-identifier space" is not an enumerated §R3(i)–(vii) census quantity,
  and no realised-gate-size eligibility leg was added (see N7). Non-blocking:
  the item-8 *claim cap* — the operative content — is unconditional and
  product-wide, and realised split sizes are reported under §R7 in any case.

No internal inconsistency, undefined term, or ambiguity beyond X1–X8 was
found in §§R3–R9 or R13, and nothing in X1–X8 re-opens any question the
V3 route-back made blocking.

## 6. Scores

### 6.1 Design Quality PRE-SCORE: 7/10

*Pre-score of the registration as frozen — not a Stage 8 score.*

Sub-grounds:

- **Novelty / positioning (§R10): sound, honestly capped.** Four named
  nearest learned scorers (Lightman et al. 2023; Wang et al. 2024;
  Xi et al. 2025, AgentPRM — citation now complete and verified, §4.1;
  SafetyDrift 2026), with a delta that is true of each as characterised: none
  places a distribution-free finite-sample guarantee over the learned score,
  prices abstention against a pre-registered ceiling, separates
  gate/calibration/test so the gated pipeline's guarantee is the
  unconditional statement (§R6), or is evaluated as a feasibility question
  under pre-registered floors over natural recorded populations. The
  positioning still concedes what caps it: Approach C is a classical head
  over behavioural features plus hashed unigrams, trained on trajectory
  labels only — the guarantee + pricing + feasibility discipline is the
  contribution, not the scorer.
- **Falsifier sharpness (§§R8–R9): now sharp.** §R9's cross-registration
  bookkeeping was exact in V3 and remains exact (§4.3); the defect was in
  §R8's own verdicts, and the repaired §R8 is an exhaustive, mutually
  exclusive decision table (16/16 configurations mapped exactly once, §2/N1)
  whose SUPPORTED can no longer be reached by replication rescue and whose
  KILL can no longer co-fire with it. The single-family verdicts are defined
  and fenced off from the programme verdicts (N5), and the alert state is
  always assigned a count (N4). The X1 overstatement is a wording flaw in a
  summary sentence, not a hole in the table.
- **Feasibility on the counted evidence: structural, arithmetic verified.**
  Corpora enter §R2 only as counted survivors; the census/eligibility/split
  machinery is jointly satisfiable for every named population including the
  smallest (SS-4, §4.2), with margins carried by the unchanged 4,000-sample
  rule and honest ineligibility — never a silent pass — as the failure mode
  if census quantities (usable retention, per-population base rate) fall
  short. Feasibility of *outcome* (whether any population's base rate lands
  in [0.10, 0.40], whether the signal clears the gate) is by design a census/
  experiment question, not a design-stage fact, and is not scored as one.
- **Definitional completeness: the blocking gaps are closed.** The CF primary
  outcome is a total frozen function (N2); the eligibility-deciding split
  realisation is produced by a frozen algorithm on named RNG streams under a
  frozen tolerance (N3); descriptive-tier reporting is enumerated (N6(a)).
  The §R12 fix-vs-tuning test, §R11 iteration budget, and the §R6
  guarantee-conditioning argument are carried intact, and no bar moved (§3).

Why not higher: the signal remains the modest end of its technique class
(dossier K7), no headline number exists at design stage, feasibility remains
conditional on census quantities the design cannot supply, and the X1–X8
residues — all non-blocking — keep the text short of the standard a frozen
registration should ideally meet in one pass. Why above the floor: every
defect that made V3's registration unable to decide its own verdict or define
its own primary outcome has been repaired in substance, and what remains is
enumerated, bounded, and incapable of moving a confirmatory result. **7/10.**

### 6.2 Editor Screen PRE-SCORE at TMLR: 9/12 — LOW

*Pre-score of the design as specified, from the dossier's TMLR evidence
(§§1.1–1.2: the Action Editor's on-record acceptance of incremental theory
over CRC/LTT where correctness, positioning and evidence are strong; TMLR's
demonstrated genre appetite for "the guarantee is limited in exactly this
way; here is the construction that survives, with the frontier measured").
No manuscript exists; S2/S5 are scored on the registration's stated
contribution and genre plan. Sub-scores are 0–2 each under Scoring System v2.*

| # | Sub-score | Value | Grounds (one line) |
|---|---|---|---|
| S1 | Venue fit vs recent contents | **2** | TMLR has published exactly this family on record (risk-controlling model selection, dossier §1.1; conformal-under-dependence, §1.2) — trajectory-level CRC with a measured frontier is inside its demonstrated contents |
| S2 | Contribution legibility | **1** | A one-paragraph delta exists (§R10), but the front matter must still carry three contributions (trajectory unit + signal craft + feasibility census) plus the negative-pilot reframe; the advance is extractable, not immediate — the verdict repairs do not change the front-matter burden |
| S3 | Novelty positioning | **2** | Unit claim positioned vs the packet's named works and signal claim vs four named learned scorers with an explicit, honest delta; the completed AgentPRM citation (§4.1) removes the one bibliographic thinness the V3 screen's grounds noted |
| S4 | Methods-credibility signals | **1** | Public counted corpora, frozen census, seeded task-grouped splits, CPU-reproducible $0 pipeline — strong signals, but at design stage no headline number exists and per-population eligibility is still census-reserved, so the evidence element is promised, not demonstrated |
| S5 | Presentation polish & genre conformance | **1** | The planned genre (guarantee + priced frontier, failures included) is the §1.2 TMLR genre; polish itself is unscorable pre-manuscript and the composite narrative remains a known presentation risk |
| S6 | Tier calibration | **2** | TMLR is the dossier-evidenced fit for this theory depth (§1.1 AE precedent accepts exactly this increment-over-CRC shape); the venue decision corrects the JMLR miscalibration that produced V2's HIGH flag |
| **Total** | | **9/12** | **LOW flag** (total ≥ 9 and no zero sub-score; a fortiori total > 5 and none of S1/S2/S4 = 0) |

This agrees independently with the V3 design-stage screen at the same venue
(9/12 LOW, same sub-score pattern), as it should: V4 changes the
registration's verdict/outcome layer, not the work's venue fit, genre, or
evidence state. Per FRAMEWORK Gate 4, this screen is venue-specific to TMLR
and transfers nowhere.

## 7. Route verdict

**PASS (proceed to Stage 6).**

Triggering rule (FRAMEWORK Gate 9, as tasked): PASS iff Design Quality
≥ 6/10 AND the Editor Screen flag is not HIGH. Both hold — Design Quality
pre-score **7/10**, Editor Screen pre-score at TMLR **9/12, LOW** — so Stage 6
coding may start on `EXPERIMENTS_V4.md` as frozen.

Recorded for exactness, per the mandate: this was loop 2, the final loop the
programme's sequence allows (V4, Activation conditions). **Had this report
routed back, the mandate's loops would have been exhausted: the programme
would have stopped and been reported, with no V5 written under this
mandate.** That condition does not trigger.

Carry-notes for Stage 6 (interpretation discipline, not conditions on the
PASS, and not amendments to the frozen registration): the X1–X8 readings
adopted in §5 — operative table over summary sentence (§R8), §R6's
gate-failure consequence governing descriptive λ̂ (§R7), the type-based
reading of §R3(v) clause 3, and the single re-execution cap in the alert
rule — should be logged in `code/BUILD_LOG_V4.md` at build time, **before**
any census or gate quantity exists, so that no interpretation is ever chosen
after seeing a result it could affect. The frozen `EXPERIMENTS_V4.md` is not
to be edited to embody them.

Nothing in this report questions the venue decision (TMLR stands as
Ranadhir's), authorises any submission (V4 §R14's hard stop — Ranadhir's
verification of the final paper — is untouched), or scores anything beyond
the design of the frozen registration.

*End of Gate 9 design-stage fresh-tester report on the V4 pre-registration,
loop 2. This report scores the registration; it does not amend it or any
frozen artefact, and it authorises nothing beyond the Gate 9 route stated
above.*
