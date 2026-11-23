# 2026-11-23 W46/W47 Post-Weekly-Rollover Integrated Integrity Audit

**Audit date:** 2026-11-23  
**Repository:** CDHughett/daniel-longitudinal-public  
**Working branch / PR:** `w46-closeout-w47-rollover` / [PR #34](https://github.com/CDHughett/daniel-longitudinal-public/pull/34)  
**Production baseline (`main`):** `cce04f350a70ef355f240a6005f130f9d3db9ff7`  
**Independently audited pre-audit HEAD:** `6b367312cee905eadd19b35b739f5c7965736795`  
**Successful pre-audit validation:** [official five-validator GitHub Actions run 45286525315](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/45286525315), green on that exact head (also [run 45286533353](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/45286533353)).  
**Disposition:** **INTEGRITY PASS / CONDITIONAL GO** for the specified pre-audit state, subject to a new official five-validator run on the audit-bearing commit, independent PR review and explicit owner merge approval. **This document does not authorize merging or mark a published release.**

---

## Scope and evidentiary limits

This audit covers the internal **2026-W46 (November 16–22, 2026)** retrospective closeout, internal **2026-W47 (November 23–29)** prospective opening, private source registration, governed public data append, and current-facing navigation. Report identifiers follow [the internal, non-ISO week convention](../../docs/WEEK_INDEXING.md). The private **November Week 41 Operator Narrative** describes internal W46; its title does not refer to public `reports/2026-W41.md`.

The original, retained private `Daniel_Dataset_v1.40` workbook was reopened and examined by sheet. Its original bytes were independently hashed. The complete **25-page** private Week 41 Operator Narrative was also inspected in the working environment, but neither private document was committed or uploaded to the public GitHub archive. The audited live production and proposed Git trees were compared by complete path and Git blob identity; the five governed CSVs were read by immutable base/head ref, and their appended records were independently compared with source workbook fields. The W46/W47 reports, public current-state documents, locked Model Error registry and official GitHub validator steps were reopened and checked.

This is an **archive/provenance/coherence audit**, not independent verification of the underlying person's physiology, eyewitness exercise evidence, provider-supplied medical measurements, running mechanical tolerance, complete content/privacy review of previously published November binary reports, or diagnosis. The November testing source-artifact intake is a separate, partial evidence layer; no numerical November provider outcomes are incorporated or scored here.

## 1. Private source identity, raw window and material exposure

| Property | Independently observed |
|---|---|
| Private source filename | `Daniel_Dataset_v1.40` |
| Source kind | Excel workbook (XLSX bytes) |
| Exact size | **367,540 bytes** |
| Original SHA-256 | **`dd10f20a62df5bf18712f880059ca1b69f75fc64a5711c3a3db26cd733169e23`** |
| Source reporting window | November 16–22, 2026 / internal W46 |
| Public provenance location | [`data/source_provenance/daniel_dataset_private_manifest.csv`](../../data/source_provenance/daniel_dataset_private_manifest.csv), `v1.40`, `hash_status=registered` |
| Daily Biomarkers source entries | 7 |
| Canonical overnight Sleep Log source entries | 7; **all seven REM confidence labels Low** |
| Training Blocks source entries | **12**, comprising **10 completed B1/LI** entries and **two assessment-day placeholders** without completed training duration |
| Weekly Summary source label | `2026-W46` |
| Private narrative | 25-page Week 41 / internal W46 narrative, reporting period November 16–22, 2026; independently inspected, not published |

The first Daily Biomarkers date and first Training Blocks date are Excel serial **46342**, equivalent to **2026-11-16** under standard Excel-date interpretation; the subsequent daily/training source cells use day numbers 17–22. Sleep Log contains serial dates 46342–46348. This mixed representation was normalized only for source-supported, consecutive ISO public keys. It is **not** a claim that each source cell already held an unambiguous ISO date.

The private narrative classifies W46 as **controlled re-entry with selective expansion**. The November 16–17 scheduled assessment interval included no completed standard training. November 18–22 contains five completed paired B1/LI days; the first supplemental running exposure was two minutes on November 18 (1 minute at 6.0 mph and 1 at 7.0 mph, both 10% grade), and the second was five minutes on November 20 (6.5 mph at 2% grade). The 55-minute familiar B1 walking anchor remains separable from the novel running component. Their different grades, speeds and durations are not a controlled single-variable progression.

## 2. Governed append and historical byte preservation

All five governed files retain their **entire exact production byte content as the beginning of the proposed file**. CSV headers and prior rows are unchanged; each new source row is appended, not interleaved or used to rewrite history.

| File | Baseline rows | Proposed rows | Append | Historical byte-prefix check |
|---|---:|---:|---:|---|
| `data/daily_biomarkers_v1.csv` | 280 | **287** | +7 | PASS |
| `data/sleep_longitudinal_v1.csv` | 280 | **287** | +7 | PASS |
| `data/training_blocks_v1.csv` | 451 | **461** | +10 | PASS |
| `data/context_events_v1.csv` | 57 | **59** | +2 | PASS |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | 40 | **41** | +1 | PASS |

For exact Git-object reproducibility, original baseline → audited proposed blobs:

- Daily biomarkers: `40af89f2f64b042ba10f98721a5992473ced4532` → `8e9dbb02642540e2128d059fa3f6f9cb5541e657`
- Canonical sleep: `163d2c4fdd120d8850b54c0cdd19528ae32c9a9f` → `8311e48cfbfb2886c94f7cd4e1fe5e6f5f843e0e`
- Training blocks: `1bbec19b546fc7656ea974035c959dc6fbe63d57` → `406986b17d308ab860a69446241fd4881c91bff1`
- Context events: `57d0e61edd0bfcf37ac53f11b210eec5ae51e0cd` → `4bc7814a4556bba673046533d33a9f5bac71b9c7`
- Private-source manifest: `e0e64bc070b48d7e875a970755c145c926c5067b` → `b5ac4939c284fb3b8934fef62fca4c11cd6429e8`

Source-to-public field comparisons passed **35/35 Daily Biomarkers numeric pairs** (weight, structured daily HRV, resting HR, daily average HR, recorded skin temperature) and **42/42 Sleep Log numeric pairs** (sleep, deep, light, REM, overnight HRV, sleeping HR) across seven dates, plus **14/14 daily/sleep date keys**. All seven canonical stage-minute component sums reconcile to total sleep. The training set has **ten unique completed session IDs** and no synthetic completed row on November 16 or 17. One assessment-related `testing` event and one supplemental-running `schedule_shift` event have bounded, source-located dates rather than one event per ordinary training day.

The latest current data endpoints are **daily and sleep November 22, training November 22, and bounded context-event end November 20**. These legitimately differ because the files have different units of observation.

## 3. Independent W46 metrics and no-running-double-count check

The following are recomputed from the exact original workbook fields and separately reconciled to the public append and the [closed W46 report](../../reports/2026-W46.md). Weekly arithmetic uses the established source-specific and half-up rounding conventions.

| Required metric | W46 independently reproduced | Source |
|---|---:|---|
| Morning bodyweight | **227.0 lb** | Seven morning measurements, range **225.9–227.8 lb** |
| Daily biomarker HRV | **64.6 ms** | Structured Daily Biomarkers series |
| Resting heart rate | **47.3 bpm** | Daily Biomarkers RHR series |
| Daily average heart rate | **60.3 bpm** | Daily Biomarkers mean-HR series |
| Sleep HRV | **64.4 ms** | Separate overnight Sleep Log series |
| Sleep average heart rate | **47.3 bpm** | Separate Sleep Log sleeping-HR series |
| Total sleep | **7h17m** | **3,058 min** / 7 nights |
| Deep sleep | **1h24m** | **591 min**, wearable stage estimate |
| REM sleep | **1h00m** | **422 min**, all seven confidence labels Low |
| B1 sessions | **5** | **282 treadmill min / 15.86 approximate source-logged miles** |
| Load Integration sessions | **5** | **225 formal min**, five 45-min blocks |
| Total formal training | **507 min** | **10 completed sessions**; Nov 16–17 assessment days excluded |

The report contains the exact **`## Structured Weekly Metrics`** heading and all twelve validator-required values. The extra Post-B1 bodyweight field is **NA** because pre-/post-GI and immediate post-exercise readings cannot be pooled with waking bodyweight. Daily HRV and overnight HRV are not interchangeable, nor are daily RHR and sleeping HR.

Critical accounting: B1 total **57 + 55 + 60 + 55 + 55 = 282 min**, consisting of **five familiar 55-min anchors = 275 min** plus **2 min on Nov 18 and 5 min on Nov 20**. LI is **5 × 45 = 225 min**. Therefore **282 + 225 = 507 min**, with the seven running minutes already included, **not** added to a separate running-session total. No independently measured segment HR/RPE or uniformly confirmed actual resistance weight was present. Source mileage is approximate or source-logged and is not independently validated distance.

Seven nightly sleep totals were 470, 402, 466, 418, 417, 440 and 445 min; **five of seven** were below the 460-min observation target. The source narrative and weekly report avoid treating dream phenomenology as independent verification of consumer REM-staging estimates.

## 4. Data-quality differences retained, not silently repaired

The original workbook and private narrative contain structured-versus-prose differences:

- November 16 structured Daily Biomarkers HRV **72 ms**, versus **45 ms** in the Training Blocks prose.
- November 18 structured Daily Biomarkers HRV **58 ms**, versus **27 ms** in the Training Blocks prose.
- November 19 structured Daily Biomarkers HRV **64 ms**, versus **48 ms** in the Training Blocks prose.
- November 16 daily steps **4,029** in Daily Biomarkers prose, versus **3,443** in Training Blocks prose.
- Time/measurement definitions for these discrepancies are not proven equivalent; the structured fields govern the specified quantitative weekly series and the conflicting notes remain source-described rather than averaged.

The public `body_temp_f` column retains the existing schema while its source is annotated as **wearable skin temperature**, not verified core-body temperature. Sleep stage minutes, awakening counts, some awake-minute derivations, source-reported treadmill distance, HR target bands and LI resistance loads have different precision and verification boundaries. The private narrative's favorable subjective morning state and easy training execution do not independently establish delayed musculoskeletal running tolerance, improved metabolic-test VO₂max, causality from changes in HRV, complete lumbar tissue clearance or unobserved clinical outcomes.

Prior DQ-011 and the two historical governed sleep warnings are preserved; no source-conflict or missing-field reconstruction was performed.

## 5. Report lifecycle, navigation and protected evidence

Compared against the original production [W46 Active report](../../reports/2026-W46.md) at the baseline SHA, the proposed W46 retains **all original prospective narrative bytes**, except the necessary top-level **Active → Closed** status. One retrospective W46 section is appended after the original opening; it does not retrospectively assign outcomes to the original Active text.

The new [W47 Active report](../../reports/2026-W47.md) covers **November 23–29**, uses the weekly posture **Post-assessment continuity / supplemental running-tolerance observation**, and deliberately contains **no retrospective W47 result** or invented session. The W47 observational question preserves the distinct running exposure, delayed mechanical/recovery monitoring, and the source/phase boundary. The [weekly-index convention](../../docs/WEEK_INDEXING.md) remains unchanged.

All nine synchronized public documents show consistent **W47 Active / W46 Closed** state and current coverage:
`README.md`, `LATEST.md`, `INDEX.md`, `docs/START_HERE.md`, `docs/CONCEPTS.md`, `docs/OBSERVER_QUICKSTART.md`, `docs/NEWCOMER_PATH.md`, `data/DATA_COVERAGE.md`, `CHANGELOG.md`. The independent documentation preflight found **343 resolved internal Markdown links** across these nine files, and the full repository validator inspected the broader Markdown graph. November epoch and checksum links introduced through previously merged PR #33 are preserved.

An exact full Git-tree comparison (262 tracked blobs on `main`, 263 on the proposed branch) showed **exactly the intended 16 changed paths**: five CSVs, W46 and new W47 reports, and nine current-facing Markdown documents. The complete PR's changed-filename list matched the independent Git-tree result. All other tracked blobs were unchanged. The privacy-sensitive private workbook and narrative filenames were absent from the proposed public Git tree.

Protected historical and scientific/release controls remained byte-identical, including:
- [November epoch](../../snapshots/2026-11/2026-11%20Epoch.md), [November checksum manifest](../../snapshots/2026-11/checksums.txt), and all four November source binaries;
- August epoch and source-state artifacts, closed W45 report, older data history;
- [primary Model Error registry](../../data/model_error/model_error_gap_v1.csv) with **041–046 closed** and **047–050 open/forecast-locked/unscored**, all four new outcome fields unpopulated;
- [locked 047–050 evaluation rules](../../methodology/open_prediction_evaluation_plan_047_050.md) and [November collection plan](../../methodology/2026-11-snapshot-collection-plan.md);
- snapshot/epigenetic structured result files and UDI tracker;
- all five validator source files and their GitHub Actions workflow;
- `CITATION.cff`, `CODEMETA.json`, `VERSIONING.md`, original `v1.1.0` tag/frozen release commit and published DOI lineage.

Phase 2 remains **Load Integration / Consolidation / lock-in observation**; formal **Phase 2D is undeclared**. W46's retrospective running exposure or “Early 2D” source phrasing does not authorize a phase transition, prospective-prediction rewrite, or new measurement score.

## 6. Official pre-audit validator result and remaining gate

The pre-audit exact-head [official GitHub Actions run 45286525315](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/45286525315) was **SUCCESS**, with all five validators explicitly successful:

1. `python tools/validate_repository.py` — PASS (0 errors; 2 inherited governed sleep warnings).
2. `python tools/validate_machine_readable.py` — PASS.
3. `python tools/validate_weekly_rollover.py` — PASS, including source manifest and closed-week metric contract.
4. `python tools/validate_august_snapshot.py` — PASS.
5. `python tools/validate_coherence.py` — PASS.

The pre-existing warnings concern historical sleep-stage discrepancies on March 31 and April 2 and DQ-001 awake/awakening duplication on 14 historical dates. They are acknowledged, not automatically rewritten. A green validator result establishes **mechanical/archive rule compliance**, not clinical validity or source truth.

**New exact-head gate:** This audit document's commit necessarily changes the branch SHA. The successful **pre-audit** run cannot be cited as a successful **audit-bearing head** run. Re-run and inspect every official validator against the new commit, verify its full diff is the same 16 reviewed paths plus **only this dated audit file**, and leave PR #34 unmerged until owner approval. If `main` changes before merge, rebase/reconcile and revalidate against the actual updated base.

**Privacy boundary:** The four already-public November physical binaries have identity-preserving registered checksums but were **not** independently inspected for PII/PHI sanitization, instrument validity or method comparability in this weekly audit. The privacy review remains a separate unresolved task and should not be misrepresented as a passing visual/content review.

---

## Audit decision

**INTEGRITY PASS / CONDITIONAL GO** for the independently audited pre-audit branch state: the source file identity, controlled data append, weekly metrics, report chronology, current navigation, protected scientific history and official CI all meet the scoped W46/W47 rollover requirements.

**No direct production merge or release action is authorized by this audit.** The audit-bearing commit requires fresh green exact-head official CI, a final change-scope review, and explicit owner authorization. The November measurement-result integration, source-content privacy review, Model Error 047–050 adjudication, future W47 closeout and formal Phase 2D declaration remain separate workflows.
