# 2026-11-17 W45/W46 Post-Weekly-Rollover Integrated Integrity Audit

**Audit date:** 2026-11-17  
**Repository:** CDHughett/daniel-longitudinal-public  
**Working branch:** `w45-closeout-w46-rollover`  
**Production baseline (`main`):** `16582282e03f1f891285bf0f26252816c442ea16`  
**Independently audited pre-audit HEAD:** `6b0f627a027743a759d7b95cbf5893c28686af8c`  
**Successful pre-audit CI:** [Five-validator GitHub Actions run 44150834232](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/44150834232), successful on that exact pre-audit SHA.  
**Disposition:** **INTEGRITY PASS / CONDITIONAL GO** for the specified pre-audit state. This audit's own commit creates a **new HEAD**, requiring a fresh successful exact-SHA official five-validator run before PR review or merge. No production merge is authorized by this document.

---

## Scope and evidence boundary

This is an evidence-and-repository integrity review of the **internal 2026-W45 (November 9–15, 2026)** closeout and **internal 2026-W46 (November 16–22)** prospective opening. Internal reporting week labels differ from strict ISO labels; [week indexing](../../docs/WEEK_INDEXING.md) remains the controlling convention. The private **Week 40 Operator Narrative** corresponds to the internal W45 reporting window, not a public report filename.

The audit independently reopened the exact retained private workbook, recalculated core source fields, read the production and feature-branch governed CSV bytes, compared the complete Git trees and 16-file diff, checked the two report lifecycles and current public pointers, inspected protected paths, and checked the official pre-audit CI job. It does **not** externally validate device physiology, witness exercise performance, establish clinical lumbar clearance, confirm provider test completion, review unpublished November provider results, or score predictions. Private workbook bytes and the full operator narrative are **not** placed in public GitHub.

**Temporal firewall:** No November 16–17 provider-result values, new snapshot artifacts, formal Model Error scores, or Phase 2D claims are integrated here. Scheduled testing and actual verified results are different evidence states.

## 1. Exact retained source and governed v1.39 append

The retained private `Daniel_Dataset_v1.39` was independently reopened and hashed from its original bytes, rather than reconstructed from public rows:

| Property | Independently observed |
|---|---|
| Source type | Private Excel workbook |
| Retained source name | `Daniel_Dataset_v1.39` |
| Internal window | 2026-11-09 through 2026-11-15 / 2026-W45 |
| Exact size | **371,613 bytes** |
| SHA-256 | **`66272d40a250a674e3cd78bf7ee23ac40b3520ab9562fba371cf9cbd2a28622c`** |
| Public source registration | [Private source manifest](../../data/source_provenance/daniel_dataset_private_manifest.csv), `v1.39`, `hash_status=registered` |
| Public source location | Canonical `private_workbook:Daniel_Dataset_v1.39:<sheet>:<ISO date>[:<session>]` locators where applicable |
| Restricted content | Exact workbook, private full narrative, and unreviewed November medical/test documents remain outside GitHub |

Private dates include both Excel serial dates and day-of-month-only cells. Public ISO dates were normalized to the seven-day, source-supported ordered November 9–15 period. Normalization is not independent proof that every native cell was already a complete ISO date and is not permission to invent unavailable values.

The source contained **seven Daily Biomarkers rows, seven Sleep Log overnight rows, twelve completed B1/LI entries, and one distinct November 15 Rest Day note**. The rest entry has no completed duration and correctly generates no public session row. The single bounded `schedule_shift` event describes November 14's voluntarily reduced B1/LI and November 15's planned rest. Its `protocol_altering` classification is about documented exposure, **not** a provider-required taper, clinical deterioration, or demonstrated test benefit.

## 2. Historical byte-prefix integrity

An independent read-back fetched each of five governed files by immutable production and branch commit refs. In **all five**, the entire historical production file was an **exact byte prefix** of the new branch file. No earlier line, measurement, date, event, source registration or provenance reference was changed.

| Governed file | Production rows | Audited rows | New rows | Exact prior-byte prefix |
|---|---:|---:|---:|---|
| `data/daily_biomarkers_v1.csv` | 273 | **280** | +7 | PASS |
| `data/sleep_longitudinal_v1.csv` | 273 | **280** | +7 | PASS |
| `data/training_blocks_v1.csv` | 439 | **451** | +12 | PASS |
| `data/context_events_v1.csv` | 56 | **57** | +1 | PASS |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | 39 | **40** | +1 | PASS |

Daily and canonical sleep are continuous from **2026-02-09 through 2026-11-15**; the latest completed training session is **2026-11-14**, not November 15. The latest material context event ends **2026-11-15**. This endpoint asymmetry is correct: one represented rest day need not create a fabricated exercise record.

For reproducibility, production-to-audited Git blob IDs are:

- Daily: `45624987f30ebf2c0cb37f69d82c8b4db4ab9a2c` → `40af89f2f64b042ba10f98721a5992473ced4532`
- Canonical sleep: `1921b0910b4e90ba54b4fd290a4012279338d09d` → `163d2c4fdd120d8850b54c0cdd19528ae32c9a9f`
- Training: `5019936b54ca176939e4765a65bdaadc6a27c25c` → `1bbec19b546fc7656ea974035c959dc6fbe63d57`
- Context: `a874a43f5f74085e4c00b4b4afd65c294d9d0384` → `57d0e61edd0bfcf37ac53f11b210eec5ae51e0cd`
- Private manifest: `0248b6771792bfceec1cdefe45f5e236a9323967` → `e0e64bc070b48d7e875a970755c145c926c5067b`

The independent comparison additionally passed **35/35 daily numeric source-to-public pairs** (weight, HRV, RHR, daily average HR, skin temperature), **42/42 canonical sleep numeric pairs** (total, deep, light, REM, overnight HRV and sleeping HR), **14/14 daily/sleep date keys**, and **12/12 completed training structure/provenance checks**. All seven sleep-stage minute component sums matched their nightly total. Primary keys were unique in the three governed daily/sleep/training series, and no November 15 B1 or LI completion was present.

These checks are specifically scoped to the enumerated numeric/source/location fields; they do not claim external validation of physiology, source free-text accuracy, wearable stage classification, training load in pounds, or all qualitative tags.

## 3. Independently reproduced W45 structured metrics

The same twelve values were independently recalculated from private v1.39's structured fields, compared with the public appended series, and matched the closed report's exact `## Structured Weekly Metrics` table:

| Required metric | Reproduced W45 value | Governing source |
|---|---:|---|
| Morning bodyweight | **226.5 lb** | Seven structured waking values, 225.9–227.0 lb |
| Daily biomarker HRV | **69.6 ms** | Seven Daily Biomarkers fields; separate from overnight HRV |
| Resting heart rate | **47.6 bpm** | Seven Daily Biomarkers fields |
| Daily average heart rate | **59.0 bpm** | Seven Daily Biomarkers fields |
| Sleep HRV | **68.3 ms** | Seven separate Sleep Log overnight fields |
| Sleep average heart rate | **47.1 bpm** | Seven Sleep Log sleeping HR fields |
| Total sleep | **7h18m** | 3,068 total min / seven nights; half-up minute rounding |
| Deep sleep | **1h41m** | 705 total wearable-estimated minutes / seven |
| REM sleep | **44m** | 308 total wearable-estimated minutes / seven |
| B1 sessions | **6** | 330 formal minutes / 17.85 logged miles |
| Load Integration sessions | **6** | 260 formal minutes |
| Total formal training | **590 min** | 12 completed sessions, with Nov 15 formal rest excluded |

The weekly-validator-specific notes also match literal required substrings: `330 formal minutes / 17.85 miles`, `260 formal minutes`, and `12 completed sessions`. The report's additional post-B1 mass row is **NA** because acute post-exercise/pre- or post-GI readings are not comparable to the standardized morning mass series.

The source reports **five standard paired training days (November 9–13)**; **a reduced November 14 pair** (55-minute B1, 3.0 mph, 6% incline, 2.75 logged miles, plus 35-minute reduced LI); and **planned rest November 15**. Reduced duration versus W44's 700 formal minutes was intentional, not independent proof of changed capacity. HR target bands, prescribed distance and resistance structure are not all independently observed session measurements. The individual plate/bar loads and delayed lumbar responses remain incompletely verified.

## 4. Quality differences and non-causal boundaries

Structured Daily Biomarkers entries conflict with contemporaneous narrative entries in the private workbook. The discrepancies are preserved, not silently corrected:

| Date | Structured source field | Source-note counterpart |
|---|---|---|
| Nov 11 | Daily HRV **65 ms** | Daily prose **49 ms** |
| Nov 12 | Daily HRV **65 ms** | Daily prose **52 ms** |
| Nov 13 | Daily HRV **64 ms** | Training B1/LI prose **92 ms** |
| Nov 15 | Daily HRV **72 ms** | Daily prose **71 ms** |
| Nov 15 | Daily average HR **53 bpm** | Daily prose **52 bpm** |

The defined structured fields control the reproducible weekly averages. No source text or historical values were overwritten to reconcile them. The v1.39 source-manifest annotation and relevant daily context tags retain their existence. These discrepancies warrant later source arbitration if stronger native telemetry becomes available; they do not independently establish which rendering is physiologically correct.

Six of seven REM confidence labels were **Low**, one **Medium**. Estimated sleep stages, awakenings, sleep efficiency and vivid/lucid subjective dream reports are not interchangeable measurements. Source `body_temp_f` remains a legacy schema label for wearable-derived **skin** temperature, not core body temperature. A reported lack of morning lumbar symptoms and familiar subjective effort does **not** prove clinical/tissue recovery, unrestricted higher-load tolerance or favorable effects on November test results. Daily HRV and overnight HRV, as well as daily resting HR and sleeping HR, remain distinct streams.

Retained, historical warnings were independently confirmed in the official CI logs:

- Canonical sleep-stage differences on **March 31 (+16 min)** and **April 2 (+14 min), 2026**.
- **DQ-001** awake/awakening duplication on fourteen historical dates.

The governed [data-quality notes](../../data/DATA_QUALITY_NOTES.md) also retain **DQ-011** (September 8 resting-HR source verification, open; existing 64 bpm value preserved). These are known historical limitations, not new W45 errors or resolved issues.

## 5. Report lifecycle and public navigation

The prior W45 Active report was compared byte-for-byte with the W45 Closed version after reversing **only the top status change**; its entire **11,214-character prospective opening** is retained. The appended retrospective separately classifies W45 as **controlled restraint** and states its observation limits. W46 was newly opened with **Active** status, posture **November measurement intake / recovery and mechanical continuity**, and the contiguous **November 16–22** seven-day window. It contains no retrospective metrics or integrated November testing outcomes.

README, LATEST, INDEX, START_HERE, CONCEPTS, observer quickstart, newcomer path, DATA_COVERAGE and CHANGELOG now reflect **W46 Active / W45 Closed**. The core pointer and coverage statements were checked against the branch: **280 daily, 280 sleep, 451 training, 57 context**, using appropriate differing endpoints. Earlier W43/W44 historical reports remain intact. The broader Phase 2 substate **Consolidation / lock-in observation** is not replaced by the temporary weekly posture.

## 6. Full diff, protected history and privacy

A complete nontruncated Git-tree comparison between production baseline and audited pre-audit HEAD agreed with GitHub's diff: **exactly 16 changed blob files, no removals**.

- **5 data/source-provenance files:** `data/daily_biomarkers_v1.csv`, `data/sleep_longitudinal_v1.csv`, `data/training_blocks_v1.csv`, `data/context_events_v1.csv`, `data/source_provenance/daniel_dataset_private_manifest.csv`.
- **2 report files:** `reports/2026-W45.md` (prospective-preserving closeout), `reports/2026-W46.md` (outcome-free Active opening).
- **9 current-facing files:** `README.md`, `LATEST.md`, `INDEX.md`, `docs/START_HERE.md`, `docs/CONCEPTS.md`, `docs/OBSERVER_QUICKSTART.md`, `docs/NEWCOMER_PATH.md`, `data/DATA_COVERAGE.md`, `CHANGELOG.md`.

An explicit Git blob comparison found **89 protected files unchanged**, including August and other snapshot artifacts/checksums, primary and historical Model Error records, 047–050 locked November evaluation methodology, phase declaration/mapping documents, data-quality history, release/version/DOI metadata, and all five validator scripts plus CI workflow. Model Errors **041–046 remain closed** (043 remains `overall_improvement_not_met` / over); **047–050 remain registered, open, forecast-locked and unscored**. No Phase 2D declaration or tagged release was added. The published **v1.1.0** freeze, version DOI **10.5281/zenodo.22759132** and all-versions DOI **10.5281/zenodo.20815611** remain untouched.

A review of **264 added diff lines** did not find email-address or telephone-number patterns or a claim that November testing results had been measured/verified; the Git tree added no new medical PDF, raw private workbook, private narrative, snapshot output or test binary. This is a bounded change-scope/privacy screen, **not** a claim that all health-related information is inherently non-sensitive or that every historical artifact was freshly sanitized. Future November provider documents require a separate privacy and source review.

## 7. Five-validator pre-audit CI and final gate

The exact audited pre-audit HEAD `6b0f627a027743a759d7b95cbf5893c28686af8c` passed **all five existing official GitHub Actions checks** in [run 44150834232](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/44150834232):

1. `python tools/validate_repository.py` — **PASS** (0 errors, 2 retained historical sleep warnings).
2. `python tools/validate_machine_readable.py` — **PASS** (0 errors, 0 warnings).
3. `python tools/validate_weekly_rollover.py` — **PASS** (W45 Closed, W46 Active; exact metrics/source window).
4. `python tools/validate_august_snapshot.py` — **PASS** (August protected cross-layer state).
5. `python tools/validate_coherence.py` — **PASS** (current public pointers/posture/coverage/release state).

**Decision:** Integrity checks support **CONDITIONAL GO to the final exact-HEAD gate**, not an immediate production merge. The audit-bearing commit is necessarily a new Git SHA: obtain successful official five-validator CI on that SHA, inspect unchanged source/history and audit-only added-path scope, then submit a reviewable PR against production. Production merge and post-merge validation require a separate explicit approval step. Any change after a successful run invalidates that SHA's CI gate and requires another exact-head run.

**November results remain strictly deferred:** no `snapshots/2026-11/` entry, provider-source intake, TruAge/DEXA/VO₂/Tanita public outcome, Model Error 047–050 scoring, new UDI interpretation, phase advancement, release/tag or Zenodo action belongs to this closeout.
