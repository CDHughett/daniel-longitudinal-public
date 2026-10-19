# 2026-10-19 W41/W42 Post-Weekly-Rollover Integrated Integrity Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Baseline `main`:** `76ac71123035c42cdf7fc85d13912954a9590444`  
**Working branch:** `w41-closeout-w42-rollover`  
**Batch 1 data/provenance commit:** `fa86a25eec20735b7d09b57beb8bc04230d9a5ee`  
**Batch 2 report lifecycle commit:** `5ad678ea0858e6ff1cd8e1c34ad7a9b1681c2aa5`  
**Pre-audit Batch 3 head:** `dc8a6727a51159763b62694fa5ebe4eeffe54376`  
**Audit date:** 2026-10-19  
**Audit status at preparation:** **PASS on source/provenance, append-only integrity, metric reproduction, lifecycle, current-state coherence, privacy-boundary and protected-governance checks. The final audit-commit GitHub Actions run is an independent required gate; do not treat the pre-audit green result as a final-head run.**

---

## Scope and audit authority

This audit is a **selective credibility-relevant integrity checkpoint**, warranted under `docs/audits/README.md` because the repository's public longitudinal core, source provenance, completed report lifecycle and current-state documents were advanced together. It is not a routine biological progress report.

Scope includes: exact retained private-source identity; curated appended records; historical-prefix preservation; source-to-report arithmetic; sleep/date/exposure semantics; W41 closeout versus original opening intent; W42 active opening; context-event indexing; privacy/publication boundaries; Phase 2 / Model Error / DQ governance; frozen release identity; and five existing validators.

This audit establishes archive-level traceability and mechanical consistency. It does **not** independently verify exercise repetitions, prove biological causation or clinical safety, establish full musculoskeletal recovery, measure nutritional adequacy, certify sleep-stage accuracy, or declare a new phase.

---

## 1. Exact controlling private source

The retained uploaded workbook was inspected and hashed directly:

```text
Source filename:    Daniel_Dataset_v1.35
Coverage:           2026-10-12 through 2026-10-18
Bytes:              373,951
SHA-256:            65dcaa2a2f2e6fb6acfc116dd9290a3d5834de27c26071807e6d05fab6dd61a1
Manifest version:   v1.35
Manifest status:    registered
```

This same identity is present in `data/source_provenance/daniel_dataset_private_manifest.csv`. Row source references use `private_workbook:Daniel_Dataset_v1.35:...` locators. The private workbook contains seven Daily Biomarkers entries, seven Sleep Log entries and 14 Training Blocks entries: 13 completed sessions and **one scheduled LI rest entry without completed LI**.

Private source dates mix Excel serial and day-of-month representations. The governed public layer uses ISO-indexed October 12–18 dates; date normalization did not authorize alteration of the associated metric values.

The private operator narrative, titled *2026-10 — Week 36 / 2026-W41 Operator Narrative (Private)*, supplies interpretation but is not treated as an independent measurement source or committed. The workbook and narrative remain private; the public archive retains only governed extracts, bounded observations and source identity.

---

## 2. Exact append-only preservation

GitHub `fetch_file` comparisons against baseline `main` verified that the entire earlier contents of all five governed files are **exact byte-for-byte prefixes** of their W41 branch versions:

| Governed path | Baseline rows | Appended | W41 branch rows | Historical-prefix result |
|---|---:|---:|---:|---|
| `data/daily_biomarkers_v1.csv` | 245 | 7 | 252 | Identical |
| `data/sleep_longitudinal_v1.csv` | 245 | 7 | 252 | Identical |
| `data/training_blocks_v1.csv` | 396 | 13 | 409 | Identical |
| `data/context_events_v1.csv` | 52 | 1 | 53 | Identical |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | 35 | 1 | 36 | Identical |

No historical structured row was deleted, reordered, rewritten or corrected in place. The five deltas total **29 appended records**, not 29 training sessions.

Current endpoints:

- Daily Biomarkers: 252 daily records, `2026-02-09` through `2026-10-18`.
- Curated canonical sleep: 252 wake-date records through `2026-10-18`.
- Completed training: 409 session rows through `2026-10-18`.
- Bounded context events: 53 rows, most recent event ending `2026-10-14`.

The event-index end date is intentionally different from the daily-data endpoint. The index is not a complete diary, and no fabricated October 18 resistance-training row was created for the planned rest day.

---

## 3. Independent source-to-report arithmetic

The actual retained private workbook was independently imported and examined apart from the public rollup text. Its seven daily and seven sleep observations, plus completed-session counts, reproduce the closed W41 Structured Weekly Metrics table.

| W41 measure | Reproduced value |
|---|---:|
| Morning bodyweight | **226.4 lb** |
| Daily Biomarkers HRV | **70.6 ms** |
| Daily resting heart rate | **44.6 bpm** |
| Daily average heart rate | **61.4 bpm** |
| Sleep Log HRV | **75.7 ms** |
| Sleep average heart rate | **51.6 bpm** |
| Overnight sleep | **7h17m** |
| Deep sleep, wearable estimate | **1h18m** |
| REM, wearable estimate | **49m** |
| Completed B1 sessions | **7** |
| Completed LI sessions | **6** |
| Formal session minutes | **670 min** |

Supporting training arithmetic:

- B1: seven 55-minute sessions = **385 minutes** and **21.14 recorded miles**.
- LI: October 12–17 durations 45, 50, 55, 45, 35, 55 minutes = **285 minutes**.
- Total formal training: **13 sessions** and **670 minutes**.
- October 18: B1 completed; LI rest **not** counted as a completed LI session.

The private sleep source's seven total-sleep values agree with the sum of REM, deep and light minutes on each date. All seven REM confidence labels are **Low**. No stage estimate is presented as polysomnographic truth, and subjective vivid dreams do not validate or negate a specific calculated REM duration.

The two HRV sources remain distinct, as do daily resting HR and sleeping HR. The archive does not pool the different values into a single purported measurement.

---

## 4. Weight, date, sleep and missingness boundaries

- Morning scale values are the comparable weekly series, averaging 226.4 lb versus W40's 227.0 lb.
- Acute post-B1 weights represent different exercise, fluid and gastrointestinal conditions. October 15's documented **pre-GI** post-B1 value is not silently pooled with post-GI values.
- A lower weekly scale average is an observation, not independent evidence of lost fat tissue or sufficient energy/protein intake.
- Consumer wearable sleep stage values retain their limitations. October 14 and October 18 overnight sleep durations were below seven hours; longer sleep on other nights did not make recovery biomarkers uniformly favorable.
- Sleeping HR was notably elevated on October 16 (62 bpm) and October 18 (56 bpm) relative to several surrounding nights; this is retained alongside reported preserved daytime function without assigning a training, respiratory, clinical or device-specific cause.
- The public schema uses one canonical sleep row per wake date, zero-to-many completed training rows per day, and sparse material context events.

These conventions preserve interpretable missingness and prevent artificial completeness.

---

## 5. W41 progression: prospective boundary versus actual dose

The original W41 **Active** report asked whether the W40 first-exposure increases could be repeated while remaining mechanically controlled, low-overhead and recovery-compatible. It did **not** prospectively prescribe a new independent load increase.

The closed W41 report preserves that original question and describes actual training as it developed:

| Date | Exposure | What the evidence supports |
|---|---|---|
| 2026-10-12 | Standard LI | Familiar baseline repeated, reported easy |
| 2026-10-13 | Control/accessory | Deliberately reduced prescription preserved |
| 2026-10-14 | Pull/press overload plus yardwork | Pull-up prescription **5×5**, compared with W40's **5×4**; brief added attention noted |
| 2026-10-15 | Standard LI after overload | Favorable next-session functional availability by operator report |
| 2026-10-16 | Technique/reduced load | Lighter day preserved despite overnight HR variation |
| 2026-10-17 | Higher-priority hinge/grip | Repeat prescription of trap bar **4×5** and hangs **3×45s**, reported manageable |
| 2026-10-18 | Scheduled LI rest | No formal LI training; B1 and home mobility remained |

October 14 is **not** claimed as an exact-dose replication: 5×5 prescribes 25 pull-up repetitions compared with 20 at W40's 5×4 and 16 at the prior standard 4×4. The increase was documented within the observation window and published retrospectively, **not backdated as prospective public preregistration**.

The source contains operator-reported execution but not independent movement video, independently verified completed repetition counts or numeric trap-bar working mass sufficient for an external load replication. W41's retrospective descriptor *conditional repeatability* is therefore appropriate at the reported execution/functional level while sustained cumulative recovery cost remains unresolved.

---

## 6. Context-event indexing

One bounded event, `2026-10-14-01`, documents the protocol-relevant increase in the pull/press prescription alongside the same-day ordinary physical work. Its retrospective nature is explicit.

Ordinary yardwork, a scheduled LI rest, individual sleep measurements and standard sessions are retained in training/daily/report context rather than multiplied into artificial event-index rows. The event-index role and the source reference remain schema-governed.

---

## 7. Report lifecycle and current-state coherence

- `reports/2026-W41.md`: **Closed**, 2026-10-12 through 2026-10-18; descriptor **conditional repeatability**.
- `reports/2026-W42.md`: **Active**, 2026-10-19 through 2026-10-25; no assigned outcome.
- Observation windows are contiguous without a gap or overlap.
- The active W42 posture is **Continued LI progression / recovery-cost and dose-repeatability observation**.
- The declared phase remains **Phase 2 — Load Integration**, with broader substate **Consolidation / lock-in observation**.

Nine current-facing documentation/changelog files were synchronized: `README.md`, `LATEST.md`, `INDEX.md`, `docs/START_HERE.md`, `docs/CONCEPTS.md`, `docs/OBSERVER_QUICKSTART.md`, `docs/NEWCOMER_PATH.md`, `data/DATA_COVERAGE.md`, and `CHANGELOG.md`.

Current pointers show W42 Active / W41 Closed, the current posture matches the active report, and the public numerical coverage claims match the structured files. The historical W40 report remains intact as an independent first-exposure reference. The archive's established **internal week-number convention**, rather than inferred ISO week numbering, controls its report labeling.

---

## 8. Five-validator execution before this audit

The last completed **pre-audit** workflow on the synchronized branch head was:

- **Commit:** `dc8a6727a51159763b62694fa5ebe4eeffe54376`
- **Run:** [39340015019](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/39340015019)
- **Status:** Completed / Success.
- **Checks:** Core repository **PASS**, machine-readable semantic **PASS**, latest weekly rollover **PASS**, August snapshot cross-layer **PASS**, post-release coherence **PASS**.

All five original validator commands ran successfully. No check was disabled, no rule was relaxed and no historical data were modified in response to a desired conclusion.

This run occurred **before** the present audit record was committed. A green run from this earlier commit **cannot** satisfy the final audited-head gate. The existing rollover-branch push trigger must run the same five checks after the audit/changelog commit; the result is to be verified by exact commit SHA before Batch 5.

---

## 9. Protected-governance and frozen-publication invariants

Comparison of repository Git trees against the baseline `main` confirmed **identical blob identities** for:

- `PHASE_MAP.md`
- `GOVERNANCE.md`
- `PHASE_DECLARATION_CRITERIA.md`
- `VERSIONING.md`
- `VERIFICATION.md`
- `CITATION.cff`
- `CODEMETA.json`
- `reports/2026-W40.md` and `reports/2026-W39.md`
- `data/model_error/record_043_closure.md`
- `data/DATA_QUALITY_NOTES.md`
- `protocols/load-integration-progression-exposures-2026-W40.md`
- `.github/workflows/validate.yml`

Protected Model Error records **041–046 remain closed** with their adjudications unchanged; Record 043 remains not supported / `overall_improvement_not_met` / `over`. **DQ-011 remains open.** No historical data correction, prospective prediction registration, Phase 2D declaration, new training mandate or causal nutritional intervention was introduced by this rollover.

Frozen publication identity remains:

```text
Published version:    v1.1.0
Frozen commit:        92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
Version DOI:          10.5281/zenodo.22759132
All-versions DOI:     10.5281/zenodo.20815611
```

No release tag, source-export package, DOI record or immutable release artifact was modified.

---

## 10. Privacy and changed-file scope

The 16 **pre-audit** changed paths consist exactly of five append-only CSV/source-manifest files, W41 closeout and W42 active reports, and nine current-facing documentation/changelog files. No protected file is in this diff. This audit adds one new markdown path and a changelog annotation only.

The retained private workbook and private narrative are **not** in the public changed-file set. Source-provenance filenames, SHA-256 and row locators are disclosed under existing rules without posting original private bytes. Automated screening of the newly published weekly-report text found no email addresses, phone numbers, US Social Security number patterns, absolute private filesystem paths or embedded source binary material. The public text uses bounded operator terminology rather than additional directly identifying personal contact details.

The screening is a limited disclosure check, not a universal guarantee of anonymity for a public N-of-1 archive. The intended scientific/measurement disclosures are already part of the project; this rollover adds no private raw-provider or household-document artifact.

---

## 11. Findings and limits

**Positive integrity findings:** Exact private-source file identity; all five historical CSV prefixes unchanged; seven dates represented in each aligned daily/sleep series; 13 genuine training sessions rather than 14; reproduced W41 arithmetic; a source-grounded material event; retained opening-versus-execution distinction; synchronized W42/W41 current state; identical protected-governance blobs; pre-audit five-validator success.

**Remaining research questions, not validated defects:** Verified numeric mechanical loading and repetition fidelity; cumulative recovery after repeated higher-dose sessions; significance and cause of episodic overnight HR elevations; wearable sleep-stage confidence; composition of lower observed scale weight; actual measured energy/protein availability. No correction is invented for these uncertainties.

No new source-backed numerical discrepancy or private-data exposure requiring alteration of protected data was identified in the reviewed W41 closeout. Audit validation is necessary but does not turn an observational archive into proof of therapeutic efficacy.

---

## 12. Publication decision and final-head gate

**Provisional integrity verdict: PASS. Publication decision: CONDITIONAL GO for Batch 5 preparation only after exact final audit-commit SHA passes all five GitHub Actions validator steps.**

The post-audit branch must remain separate from `main` until:

1. Audit and changelog changes have been committed.
2. GitHub Actions has completed against the **same new commit SHA**.
3. All five validators show **success** in that run.
4. The final changed-file inventory contains only the approved weekly rollover and audit paths.

At the time this audit is written, the pre-audit branch-head check is green; the additional required final-head result must be independently confirmed after publication of this document to the rollover branch. **This audit is not permission to merge, open a release, edit a DOI, or declare Phase 2D.**
