# COUNTING PASS O3 — the three uncounted collections of SOLUTION_DESIGN_V3 §7

**Date:** 2026-10-31. **Authority:** Ranadhir Ghosh's directive of 2026-10-31 —
"continue with all pending tasks unless cost or compromise with quality is at
stake" — executing option **O3** of `SOLUTION_DESIGN_V3.md` §7 (counted re-pass
on the uncounted collections, $0). **Spend: $0.**

**What this document is.** A counting pass only. It applies the V3 criteria
**exactly as frozen** in `SOLUTION_DESIGN_V3.md` — no floor lowered, no
criterion relaxed, no new registration frozen, no experiment run. It produces
evidence for Ranadhir's O1/O2/O4/O5 decision. Base rates are taken by the
**documented-fact route only** (V3 §1 rule 3): a base rate is never computed
from outcome data at design stage; where no documented base rate describes the
counted artefact population, eligibility is reserved to the §5.5 census route
inside a future registration. Counts are taken **at the artefact** (HF API
`dataset_info`, per-file parquet column scans, the publisher's own distribution
file inside the dataset repo), not from landing pages — the same discipline
that produced the Gate 9 corrections C1–C6.

## The frozen criteria applied (V3, verbatim in substance)

- **Population:** one exchangeable population = one benchmark × one scaffold ×
  one model configuration, trajectories over distinct tasks.
- **Floor:** ≥ **800 usable** trajectories in that one population — four
  disjoint splits fit 40 / gate 20 / cal 20 / test 20 with exact
  Clopper–Pearson **n_cal ≥ 160 ∧ n_test ≥ 160** (n = 150 fails: half-width
  0.0513; n = 160 passes: 0.0495).
- **Eligibility band (base failure rate):** [0.10, 0.40] confirmatory;
  (0.40, 0.50] descriptive-only; outside [0.10, 0.50] ineligible. Class-count
  rule: ≥ 40 successes ∧ ≥ 40 failures in each of gate/cal/test
  (operative window [0.25, 0.40] at the floor size).
- **Usable** (V3 §5.5 integrity rule): step log **and** final evaluation
  present. Step transcripts must be transcripts, not summaries.

## Verdict summary

| Corpus | Populations counted | Floor (≥ 800 in one population) | Step transcripts | Success-filtered? | Base-rate leg | **Verdict** |
|---|---|---|---|---|---|---|
| Open-SWE-Traces (`nvidia/Open-SWE-Traces`) | 18 (5 harnesses × models × versions) | PASS everywhere (known-outcome n ≥ 15,098) | YES (`messages`) | NO | Documented: 17/18 populations > 0.50; 1 at 0.4832 | **EXCLUDED** — base rate outside the frozen envelope in every counted population |
| CoderForge-Preview (`togethercomputer/CoderForge-Preview`) | 3 (task sources; OpenHands × Qwen3-Coder-480B) | PASS per source (77,169 / 148,001 / 32,964) | YES (`messages`) | NO (source splits carry both outcomes) | Not documented per source → §5.5 census route | **SURVIVES** — per source population; base-rate eligibility reserved to census |
| SWE-smith trajectories (`SWE-bench/SWE-smith-trajectories`) | 9 (3 format splits × 3 models; SWE-agent) | PASS in the 6 Claude cells (5,751–18,457); FAIL in all 3 GPT-4o cells (475–634) | YES (`messages`) | NO (`resolved=False` rows present) | Documented rate does not describe the current artefact → §5.5 census route | **SURVIVES** — per (split × model) Claude populations; base-rate eligibility reserved to census |

---

## 1. Open-SWE-Traces — EXCLUDED (base rate binds)

**Artefact.** `nvidia/Open-SWE-Traces`, HF revision sha `4fa4c2ae`, last
modified 2026-10-28, licence CC-BY-4.0, public. Configs v1.0 / v1.1 / v1.2 /
v2.0.

**Correction to V3 §3.3.** V3 described this collection as an aggregate of
other trajectory datasets. The current artefact is not: it is **NVIDIA's own
rollouts** — five agent harnesses (Claude Code, OpenCode, OpenHands, SWE-agent,
mini-SWE-agent) × one model per release version, over issue tasks drawn from
the Scale-SWE and SWE-rebench-V2 pools. The V3 entry's "uncounted" status is
unchanged; its description is corrected here.

**Legs.** Step transcripts: YES — each row carries `messages`, the complete
conversation. Final evaluation: YES — `resolved` ∈ {1, 0, −1}; rows with
`resolved = −1` (unknown outcome) are **not usable** and are excluded from the
denominators below. Success-filtering: NO — both outcomes present in every
population.

**Documented base rates.** The publisher's own `data_distribution.md` (a file
inside the dataset repository) documents Resolved / Unresolved / Unknown
trajectory counts per (version × scaffold × model). Failure rate below =
Unresolved / (Resolved + Unresolved), computed from those documented counts —
the same documented-fact route and the same arithmetic discipline as the
Gate 9 rebench correction (0.5205).

| Version | Scaffold | Model | Resolved | Unresolved | Unknown | Known-outcome n | Failure rate | Band |
|---|---|---|---:|---:|---:|---:|---:|---|
| v1.0 | OpenHands | Minimax-M2.5 | 14,363 | 19,510 | 9,730 | 33,873 | 0.5760 | ineligible |
| v1.0 | OpenHands | Qwen3.5-122B | 9,833 | 21,124 | 9,506 | 30,957 | 0.6824 | ineligible |
| v1.0 | SWE-agent | Minimax-M2.5 | 16,749 | 19,206 | 10,864 | 35,955 | 0.5342 | ineligible |
| v1.0 | SWE-agent | Qwen3.5-122B | 7,348 | 7,750 | 5,236 | 15,098 | 0.5133 | ineligible |
| v1.1 | OpenHands | DeepSeek-V4-Flash-0731 | 23,110 | 27,185 | 0 | 50,295 | 0.5405 | ineligible |
| v1.1 | OpenHands | Qwen3.6-27B | 16,782 | 23,597 | 0 | 40,379 | 0.5844 | ineligible |
| v1.1 | SWE-agent | Qwen3.6-27B | 32,151 | 37,735 | 7,375 | 69,886 | 0.5400 | ineligible |
| v1.1 | mini-SWE-agent | Qwen3.6-27B | 32,231 | 53,622 | 9,438 | 85,853 | 0.6246 | ineligible |
| v1.2 | Claude Code | Qwen3.8-27B | 15,876 | 18,137 | 0 | 34,013 | 0.5332 | ineligible |
| v1.2 | OpenCode | Qwen3.8-27B | 16,377 | 18,927 | 0 | 35,304 | 0.5361 | ineligible |
| v1.2 | OpenHands | Qwen3.8-27B | 11,933 | 13,666 | 0 | 25,599 | 0.5338 | ineligible |
| v1.2 | SWE-agent | Qwen3.8-27B | 15,640 | 17,573 | 0 | 33,213 | 0.5291 | ineligible |
| v1.2 | mini-SWE-agent | Qwen3.8-27B | 49,925 | 46,670 | 10,672 | 96,595 | **0.4832** | descriptive-only |
| v2.0 | Claude Code | Qwen3.8-Flash-Next | 17,145 | 17,789 | 0 | 34,934 | 0.5092 | ineligible |
| v2.0 | OpenCode | Qwen3.8-Flash-Next | 17,155 | 19,443 | 0 | 36,598 | 0.5313 | ineligible |
| v2.0 | OpenHands | Qwen3.8-Flash-Next | 12,810 | 13,217 | 0 | 26,027 | 0.5078 | ineligible |
| v2.0 | SWE-agent | Qwen3.8-Flash-Next | 17,075 | 17,613 | 0 | 34,688 | 0.5078 | ineligible |
| v2.0 | mini-SWE-agent | Qwen3.8-Flash-Next | 17,807 | 18,770 | 0 | 36,577 | 0.5132 | ineligible |

**Artefact reconciliation.** For v1.2 the documented distribution totals
235,396 trajectories against the artefact's 235,391 rows (datasets-server
`/size`; per-split agreement within 3) — the documented distribution describes
the v1.2 artefact. For v2.0 the documented distribution totals 168,824
trajectories while the v2.0 artefact holds 489,109 rows: the distribution file
covers only the **xhigh-effort** sub-population; the medium/low-effort
sub-populations present in the artefact have **no documented base rates** and
are therefore **not counted** in this pass (V3 §1 rule 3).

**Verdict: EXCLUDED.** Binding reason: the documented base failure rate lies
outside the frozen [0.10, 0.50] eligibility envelope for **every** counted
single population — 17 of 18 are above 0.50 (ineligible outright) and the
remaining one (v1.2 × mini-SWE-agent × Qwen3.8-27B, 0.4832) reaches only the
descriptive-only band. The size and transcript legs pass everywhere
(known-outcome n ≥ 15,098 per population); the base-rate leg binds. No pooling
across versions, scaffolds, or models was used to manufacture a rate — pooling
was rejected in V3 and stays rejected.

---

## 2. CoderForge (= CoderForge-Preview) — SURVIVES as three source populations

**Artefact.** `togethercomputer/CoderForge-Preview`, HF revision sha
`060fca96`, last modified 2026-02-26, public. (The "CoderForge" of V3 §7 is
this artefact; no other CoderForge dataset exists on the Hub.)

**Documented facts.** The SWE-Critix paper (arXiv:2610.13356, §II-A) documents
the collection: **258K trajectories (155K pass / 103K fail) over 51K issues in
1,655 repositories**, generated with **OpenHands × Qwen3-Coder-480B**, from
three task sources (SWE-Rebench, SWE-Smith, R2E-Gym).

**Artefact reconciliation (HF API `dataset_info`, config `trajectories`).**

| Split (task source) | Rows |
|---|---:|
| SWE_Rebench | 77,169 |
| SWE_Smith | 148,001 |
| R2E_Gym | 32,964 |
| **Total** | **258,134** ✓ matches the documented 258K |

The fourth split, `filtered_reward1` (155,144 rows), numerically matches the
documented 155K pass count: it is the **success-filtered view**, not a corpus —
recorded here so it is never mistaken for one.

**Legs.** Step transcripts: YES — `messages` carries the full conversation;
`reward` carries the final evaluation. Success-filtering: NO for the three
source splits (both outcomes present; the >64K-token / no-patch pruning
described elsewhere was SWE-Critix's own training subset, not the released
corpus).

**Population discipline.** The pooled mixture is **not** one population under
the frozen definition — the three sources are three different benchmarks. The
pass therefore counts **per source**: each source population (one benchmark ×
OpenHands × Qwen3-Coder-480B) individually clears the floor by two orders of
magnitude (77,169 / 148,001 / 32,964 ≥ 800). Trajectories per issue average
≈ 5.06 pooled (258,134 / 51K documented issues); per-source distinct-issue
counts are a census quantity, and the floor clears under task-unit accounting
for any per-source allocation consistent with the documented totals (smallest
source 32,964 trajectories ⇒ ≥ ~6,500 distinct issues even at the pooled
attempts-per-issue rate).

**Base-rate leg — reserved.** The pooled documented failure rate is
≈ 103K/258K = 0.399 (precisely (258,134 − 155,144)/258,134 = 0.3990 from the
artefact counts), at the confirmatory band's edge — but it is pooled over
three benchmarks and **may not be carried onto any single population**. No
per-source base rate is documented; per-source eligibility is therefore
reserved to the **§5.5 census route** inside a future registration.

**Verdict: SURVIVES** — as three per-source populations, each structurally
complete (floor, transcripts, both outcomes). What a future registration would
still have to establish, in order: (i) per-source base-rate eligibility via
the §5.5 census; (ii) per-source distinct-issue counts; (iii) a note on
licence — the dataset card states no dataset-level licence (a per-row
`license` field is present). None of these is a counting-pass verdict leg.

---

## 3. SWE-smith trajectories — SURVIVES in the six Claude (split × model) populations

**Artefact.** `SWE-bench/SWE-smith-trajectories`, HF revision sha `08e109b4`,
last modified 2025-07-19, licence MIT, public. Configured splits (HF API
`dataset_info`): **tool 24,100 / xml 26,076 / ticks 25,826 = 76,002 rows**.

**Correction to a documented number.** The dataset card's prose — "contains
the 5017 trajectories we fine-tuned Qwen 2.5 Coder Instruct on" — describes
the authors' SFT subset, **not** the artefact, whose own split counts total
76,002 rows. All counts below are the artefact's.

**Legs.** Step transcripts: YES — `messages` is the full conversation JSON.
Final evaluation: YES — `resolved` (bool), with `resolved = False` rows
present in sampled artefact rows ⇒ **not success-filtered**. Scaffold:
SWE-agent throughout (card and SWE-smith paper, arXiv:2504.21798).

**The splits are not populations — the model column decides.** The three
splits are output-format collection variants (tool / xml / ticks), and each
mixes three model configurations. The population unit under the frozen
definition is (split × model). Exact counts from a full artefact column scan
of the `model` field over all 24 configured parquet files (checkpointed
per-file; totals reconcile exactly with `dataset_info`):

| Split | claude-3-7-sonnet-20250219 | claude-3-5-sonnet-20241022 | gpt-4o-2024-08-06 | Split total |
|---|---:|---:|---:|---:|
| tool | **17,715** | **5,751** | 634 | 24,100 |
| xml | **18,457** | **7,091** | 528 | 26,076 |
| ticks | **18,457** | **6,894** | 475 | 25,826 |

Floor test per population: the six Claude cells pass (5,751–18,457 ≥ 800);
**all three GPT-4o cells fail the floor** (634 / 528 / 475 < 800) and are
excluded on size alone. File-level note: rows are block-grouped by model
within shards, and the repository also holds an unreferenced duplicate of the
xml split under `train-*` filenames — not part of any dataset config and
excluded from every count (counting it would double-count xml).

**Distinct tasks (exact).** A second full column scan (`instance_id`, all 24
configured files, per-file checkpointed) gives exact distinct-task counts per
population, and the overlap structure across splits:

| Split | Model | Trajectories | Distinct tasks | Traj / task |
|---|---|---:|---:|---:|
| tool | claude-3-7-sonnet-20250219 | 17,715 | 9,143 | 1.94 |
| xml | claude-3-7-sonnet-20250219 | 18,457 | 11,824 | 1.56 |
| ticks | claude-3-7-sonnet-20250219 | 18,457 | 11,824 | 1.56 |
| tool | claude-3-5-sonnet-20241022 | 5,751 | 1,965 | 2.93 |
| xml | claude-3-5-sonnet-20241022 | 7,091 | 2,223 | 3.19 |
| ticks | claude-3-5-sonnet-20241022 | 6,894 | 2,222 | 3.10 |
| tool | gpt-4o-2024-08-06 | 634 | 211 | 3.00 |
| xml | gpt-4o-2024-08-06 | 528 | 211 | 2.50 |
| ticks | gpt-4o-2024-08-06 | 475 | 211 | 2.25 |

Every Claude population clears the floor on **both** readings — trajectories
(≥ 5,751) and distinct tasks (≥ 1,965) — and the GPT-4o cells fail on both
(≤ 634 trajectories, 211 tasks). Two structural facts the census must respect:
(i) multiple attempts per task exist in every population (1.56–3.19
traj/task), so the frozen design's task-disjoint split construction is
load-bearing, not decorative; (ii) the splits share one task pool — the
xml × claude-3-7 and ticks × claude-3-7 instance sets are **identical**
(11,824 tasks), tool's 9,143 are a subset of them, and the GPT-4o cells cover
the same 211 tasks in all three splits — so the three splits are format
variants over common tasks and must never be treated as independent corpora.

**Base-rate leg — reserved, with a documented-fact warning.** The nebius
comparison table documents SWE-smith at 49,897 total / 21,513 successful
(failure 0.5688) — but that total does **not** describe the current artefact
(76,002 rows), so the documented rate may not be carried onto the counted
population (the rebench-correction discipline, applied in reverse: a rate is
only as good as the population it was counted on). Per-population base-rate
eligibility is reserved to the **§5.5 census route**.

**Verdict: SURVIVES structurally** — in the six Claude (split × model)
populations. A future registration would name **one** such population as its
corpus; the GPT-4o cells are excluded on the floor.

---

## What this pass changes, and what it does not

- **H-DATA is no longer the whole state of the evidence.** Two of the three
  uncounted collections contain structurally complete populations that clear
  every frozen structural leg (CoderForge per source; SWE-smith per
  split × model). For both, exactly one leg remains open — per-population
  base-rate eligibility — and the frozen design already contains the
  instrument that decides it: the §5.5 census inside a future registration.
- **Open-SWE-Traces is closed** on documented facts: no counted population is
  inside the eligibility envelope, and the only descriptive-band population
  (0.4832) cannot carry a confirmatory design.
- **Nothing here authorises anything.** No registration is frozen by this
  pass; no floor was lowered; the v1 pilot verdict (FALSIFIER DIRECTION,
  corpus 1 of 3) and the V2 freeze are untouched; the area falsifier
  (≥ 2 of 3 corpora) remains open. Activation conditions in V3 §10 apply
  unchanged to any future registration (Gate 9 re-run on V3 — complete;
  the registration must name the nearest learned-scorer work).
- **The decision returns to Ranadhir** among V3 §7's remaining options:
  O1 (own-lab generation), O2 (cluster-aware redesign), O4 (criterion
  relaxation — not recommended in V3), O5 (park / fold into Area 1) — now
  with O3's evidence in hand: a V3-style registration over a CoderForge
  source population or a SWE-smith Claude population is the path O3 leaves
  open, subject to its §5.5 census deciding base-rate eligibility.

## Methods note (verification discipline)

Counts were taken at the artefact: HF API `dataset_info` (split sizes,
features, revision shas), the datasets-server `/size` and `/rows` endpoints,
full parquet column scans of SWE-smith's `model` and `instance_id` fields
(24 configured files each; per-file checkpointed counts; column totals
reconcile exactly with `dataset_info`), and the publisher's
`data_distribution.md` inside the Open-SWE-Traces repository (all 18 failure
rates recomputed from its documented Resolved/Unresolved counts). The
datasets-server `/filter` endpoint proved unreliable during the pass (auth
timeouts, index-loading errors) and was not relied on. A first three-column
scan of SWE-smith died on a network error at file 26 of 32 after 34 minutes;
the `model` and `instance_id` columns were then re-scanned separately with
per-file checkpointing and both completed exactly. CoderForge per-source
distinct-issue counts were not exactly countable at $0 within this pass's
routes and are recorded as a census quantity, not estimated.
