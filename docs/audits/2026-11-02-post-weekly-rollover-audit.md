# 2026-11-02 W43/W44 Post-Weekly-Rollover Integrated Integrity Audit

**Repository:** \`CDHughett/daniel-longitudinal-public\`  
**Baseline production \`main\`:** \`b6a708de46b04d6af350cc8a3ff9522ff22ee960\`  
**Working branch:** \`w43-closeout-w44-rollover\`  
**Batch 1 governed data/provenance commit:** \`39f51a883bc73ccfe70e39a851f4e64653712639\`  
**Batch 2 report-lifecycle commit:** \`ef9545b1b0c237185fdb22adbd278db93d86f7f9\`  
**Batch 3 / Batch 4 independently validated head:** \`b81c449e64dcd42a311711e9f161ff5d921df03f\`  
**Pre-audit GitHub Actions run:** [41485871108](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/41485871108)  
**Audit date:** 2026-11-02  
**Pre-audit determination:** **INTEGRITY PASS / CONDITIONAL GO** for the exact Batch 3 head. Five unchanged official validators completed successfully with zero errors; two inherited historical warnings remain. **This new audit commit requires a separate exact-head CI success before PR review or merge.**

---

## Scope and audit authority

This is a **selective, credibility-relevant integrity checkpoint**, not a daily training narrative. A seven-day private workbook was converted into multiple governed public datasets; a weekly report was retrospectively closed, a subsequent weekly report prospectively opened, and nine current-facing navigation/coverage documents changed. The simultaneous updates across source, metrics, interpretive status, and current-state surfaces satisfy [audit inclusion criteria](README.md).

Audit scope:

- exact identification and privacy status of the retained private \`Daniel_Dataset_v1.37\` source;
- append-only checks against the pre-rollover production \`main\`;
- Batch 4's independently recorded **90/90** source-value comparison checks and separate data-shape/chronology tests;
- reproducibility of 12 structured W43 metrics and the intentional separation of daily and overnight HRV;
- real completed-session records, intentionally missing days, and November 1 trap-bar **loading-level** interpretation;
- correctly bounded mechanical context event and date/source uncertainty;
- W43 **Closed — conditional restoration** / W44 **Active — prospective observation**;
- exact synchronization of nine current-facing files;
- original five-validator GitHub Actions job evidence, the two inherited warnings, and unchanged validator/workflow blobs;
- protection of phase, prospective forecasts, historical outcomes, quality warnings, snapshot sources and frozen release;
- changed-file inventory, scope, non-public private artifacts and final audit-commit CI gate.

**An integrity PASS supports transcription, chronology, provenance and internal consistency. It does not independently verify wearable physiology, witness completed repetitions, diagnose lumbar pathology, establish causation or constitute clinical clearance for training.**

---

## 1. Exact controlling private source and source boundary

The source was supplied as the retained private workbook and registered in \`data/source_provenance/daniel_dataset_private_manifest.csv\`:

\`\`\`text
Source version:         v1.37
Private source name:    Daniel_Dataset_v1.37
Source type:            private_workbook
Covered dates:          2026-10-26 through 2026-11-01
Exact retained bytes:   378166
SHA-256:                b6a989538909086d267c2dc99fa2488fe6dbf9576066ae5672f7fa9297510620
Manifest status:        registered
Manifest count:         37 -> 38 entries
\`\`\`

The filename, byte count and hash refer to the **actual retained source**, not a recreated spreadsheet or a hash inferred from an old GitHub entry. The public manifest records its identity while the workbook and full private operator narrative remain outside the repository.

Mixed date representation in the source (including Excel serials/day-of-month entries) was normalized to ISO dates in curated rows. This was a date-index conversion, not permission to supply missing measurements. One waking-weight value on October 26 remains blank because a scale was unavailable. No November 2 data were added. Source locators identify the retained workbook's relevant daily, sleep and training sections; they do not make the raw source public.

The internal archive identifier \`2026-W43\` refers to **October 26–November 1**, equivalent to **ISO 2026-W44**. The established internal convention is retained, and \`2026-W44\` opens on November 2. Automated external week joins must not silently equate the internal and ISO labels.

---

## 2. Historical preservation and exact governed append

The audit compared the five governed CSV/manifest files on the verified pre-rollover \`main\` with the Batch 3 head. **Each complete historical file was an unchanged, byte-for-byte prefix of its new version**, including CSV headers and all pre-existing rows. Only the intended new records were appended.

| Governed file | Historical rows | Appended | Verified total | Current represented endpoint |
|---|---:|---:|---:|---|
| \`data/daily_biomarkers_v1.csv\` | 259 | 7 | **266** | 2026-11-01 |
| \`data/sleep_longitudinal_v1.csv\` | 259 | 7 | **266** | 2026-11-01 |
| \`data/training_blocks_v1.csv\` | 419 | 6 | **425** | 2026-11-01 |
| \`data/context_events_v1.csv\` | 55 | 1 | **56** | Context interval ends 2026-11-01 |
| \`data/source_provenance/daniel_dataset_private_manifest.csv\` | 37 | 1 | **38** | v1.37 |

**22 new governed records; zero historical deletions or historical row revisions.** All seven daily and seven canonical sleep dates are present in order (2026-10-26 through 2026-11-01). All 425 training session identifiers remain unique and the 56 context-event identifiers remain unique. The independent machine-readable validator additionally preserved the separately protected historical 325-session training prefix through August 30.

The three B1 and three LI session records are genuine reported completions on **October 27, October 31 and November 1**. October 26's travel interruption and October 28–30's deliberate lumbar remediation did not create synthetic completed-session entries. The bounded context record \`2026-10-26-01\` describes the material mechanical interruption and graded return; it is **not** a seven-day symptom diary.

---

## 3. Independent source-to-public values: 90/90

Batch 4 independently compared the newly appended public values with the supplied source-grounded expectations; this audit preserves the exact check scope rather than implying a comprehensive re-measurement of all private workbook cells.

| Comparison group | Checked | Matched | Scope |
|---|---:|---:|---|
| Daily markers | **41** | **41** | Seven date keys; six nonmissing waking weights; seven each daily HRV, resting HR, daily average HR, body temperature |
| Canonical sleep | **49** | **49** | Seven nights × date, total sleep, deep, light, REM, overnight HRV and average sleeping HR |
| **Total** | **90** | **90** | Exact source-to-curated comparisons in the two enumerated groups |

The six completed training blocks were **separately enumerated** and checked for dates, block type, minutes, recorded B1 mileage, unique IDs and the operator-clarified trap-bar plate description; those training checks are **not** falsely included in the 90 numeric/key comparisons.

Seven sleep-stage minute sums reproduce total sleep exactly. Stage percentages reflect fractions of **total sleep** (not time in bed); October 26 and 28 each sum to 99.9% due to independent one-decimal rounding, an allowed rounding difference rather than a missing stage. Overnight sleep is separate from the reported additional 47-minute October 26 nap. REM was device-estimated with Low confidence across seven nights; these records are not polysomnography.

Source-level discrepancies and explicit operator clarifications are preserved as interpretation/provenance notes rather than silently mutating the retained private source.

---

## 4. W43 metrics independently reproduced from the committed data

The unmodified latest-weekly-rollover validator recalculated the W43 structured metric table on the exact pre-audit head. Batch 4 arithmetic independently produced the same values:

| Metric | Verified W43 result | Measurement boundary |
|---|---:|---|
| Morning bodyweight | **225.8 lb** | Six observations; October 26 missing |
| Daily Biomarkers HRV | **68.6 ms** | Seven daily observations |
| Resting heart rate | **44.6 bpm** | Daily Biomarkers seven-day mean |
| Daily average heart rate | **55.9 bpm** | Distinct from sleep HR |
| Sleep HRV | **69.9 ms** | Seven overnight observations; not interchangeable with daily HRV |
| Sleep average heart rate | **45.4 bpm** | Seven overnight observations |
| Total overnight sleep | **7h32m** | 452-minute mean; 47-minute Oct 26 nap excluded |
| Deep sleep | **1h35m** | Wearable-estimated sleep stage |
| REM sleep | **1h07m** | Wearable-estimated; Low confidence |
| B1 sessions | **3** | 165 minutes; 8.89 recorded miles |
| Load Integration sessions | **3** | 140 minutes |
| Total formal training | **305 min** | Six completed sessions |

W42 recorded 510 formal minutes; W43 recorded **205 fewer** (approximately 40.2%). The weeks differed in available training and lumbar movement tolerance. This arithmetic does **not** establish lost conditioning or a uniform change in physiological training dose.

W43 overnight mean was 7h32m, median 7h08m; the seven nights varied from 6h14m to 9h17m. Six waking weights ranged 224.0–227.0 lb. These descriptive measurements do not independently establish a change in fat or lean tissue, nutritional sufficiency, recovery mechanism, or clinical state.

---

## 5. Mechanical loading semantics and evidence limits

The established three-set trap-bar loading convention uses **plate configurations per side**:

- normal first set: 45 lb;
- normal second set: 45 + 25 lb;
- normal third/heaviest set: 45 + 45 + 5 lb.

The actual two-day graded return was **not a set-by-set progression within November 1**:

- **October 31:** 3×5 at the **normal first-set plate level (45 lb per side)** for **all three sets**;
- **November 1:** 3×5 at the **normal second-set plate level (45+25 lb per side)** for **all three sets**;
- the established heaviest third-set loading level was deliberately **withheld on both days**.

This interpretation reflects the operator's explicit November 2 clarification. Original private workbook shorthand was **not rewritten**. Actual trap-bar mass is unspecified, so a verified total external/system load must not be invented.

On October 27 the initial post-travel B1/LI return was completed despite restricted lumbar positioning and unusually costly hinging; pulling and grip remained comparatively strong. Both structured components were withheld October 28–30, with symptom-directed mobility and comfortable movement. Modified B1/LI were immediately tolerated on October 31 and normal-reported B1 plus the second plate-level LI prescription were immediately tolerated November 1.

**Conditional restoration** is a defensible bounded retrospective description. Successful immediate completion does **not** establish full recovery, normal lumbar extension in all contexts, full normal third-set tolerance, a diagnosis, or sustained symptom-free repeatability. The November 1 session ends the closed observation window; later outcomes are unavailable in W43.

The causal roles of travel, unfamiliar sleep arrangements, road sitting, training load and any specific anatomical structure are **not confirmed**. The VA blood-draw date remains contradictory across provided references and was not asserted as resolved in the public event chronology.

---

## 6. Report lifecycle and nine-current-surface alignment

The closed report is [\`reports/2026-W43.md\`](../../reports/2026-W43.md):

\`\`\`text
Status:             Closed
Descriptor:         conditional restoration
Observation window: 2026-10-26 through 2026-11-01
\`\`\`

The report retains its **original October 28 opening question**, which was authored *after* October 26–27 were already reported; those initial facts are correctly identified as historical starting context, **not prospectively preregistered outcomes**. Subsequent W43 observations and outcome interpretation occur in a separate retrospective closeout section.

The next report is [\`reports/2026-W44.md\`](../../reports/2026-W44.md):

\`\`\`text
Status:             Active
Posture:            Lumbar tolerance consolidation / repeatable normal-execution observation
Observation window: 2026-11-02 through 2026-11-08
Assigned outcome:   none
\`\`\`

W44 is an **observation question**, not an automatic exercise progression order or a registered forecast predicting functional recovery.

Nine current-facing files were synchronized:

1. \`README.md\`
2. \`LATEST.md\`
3. \`INDEX.md\`
4. \`docs/START_HERE.md\`
5. \`docs/CONCEPTS.md\`
6. \`docs/OBSERVER_QUICKSTART.md\`
7. \`docs/NEWCOMER_PATH.md\`
8. \`data/DATA_COVERAGE.md\`
9. \`CHANGELOG.md\`

The current-state surfaces show **W44 Active / W43 Closed**, the identical W44 posture, the Phase 2 consolidation state and covered record counts (**266 daily / 266 sleep / 425 training / 56 context**). Observer and newcomer entry points route to W43 as the most recent closed report rather than the old W42 closeout; W42 remains available as historical evidence. The glossary and start page distinguish immediate weekly posture from the broader Phase 2 substate.

---

## 7. Exact pre-audit CI: five official validators, unchanged

**Verified GitHub Actions run:** [41485871108](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/41485871108)  
**Head SHA:** \`b81c449e64dcd42a311711e9f161ff5d921df03f\`  
**Job ID:** \`125415939997\`  
**Job:** \`validate\`; **status \`completed\` / conclusion \`success\`**  
**Run date:** 2026-11-02; Python 3.11.17

| Unmodified command from \`.github/workflows/validate.yml\` | Observed step result |
|---|---|
| \`python tools/validate_repository.py\` | **PASS** — 10 passes, 0 errors, 2 inherited warnings |
| \`python tools/validate_machine_readable.py\` | **PASS** — 0 errors, 0 warnings |
| \`python tools/validate_weekly_rollover.py\` | **PASS** — 12 W43 structured markers reproduced |
| \`python tools/validate_august_snapshot.py\` | **PASS** — protected snapshot/adjudication alignment |
| \`python tools/validate_coherence.py\` | **PASS** — W44 Active/W43 Closed, data endpoints, posture and published release aligned |

GitHub Actions logs for the exact job confirm all five named steps succeeded. The core repository validator additionally reported:

- 282 files and no zero-byte files **at the pre-audit head**;
- 176 Markdown files, 951 checked internal references and valid target/anchor/fence checks **before this new document**;
- 15 CSVs with consistent widths;
- 36 checksum artifact entries across 11 manifests;
- 266 continuous canonical sleep rows, February 9–November 1;
- 39 contiguous standardized reports W06–W44, with W44 Active;
- 38 model-error records 013–050; 041–046 closed/scored and 047–050 open/forecast-locked;
- canonical v1.1.0 release DOI accepted;
- preserved registered RingConn source-export identities.

The exact validator and workflow **blob SHAs on the audit's pre-audit head equal those on baseline \`main\`**. No test, warning threshold or enforcement rule was weakened to pass. Earlier Batch 1 and 2 intermediate CI runs had failed while the weekly lifecycle and current navigation were incomplete; the completed Batch 3 head successfully passed.

**This audit document is a new Markdown file. Therefore the pre-audit counts of 282 files, 176 Markdown files and 951 references must not be treated as post-audit counts. The new head requires its own exact-SHA run.**

---

## 8. Inherited warnings, unresolved quality items and limitations

Two **pre-existing core-validator warnings**, reproduced in the pre-rollover \`main\` CI run and in run 41485871108, remain intentionally visible:

1. **Canonical sleep-stage reconciliation:** 2026-03-31 **+16 minutes** and 2026-04-02 **+14 minutes** are historical governed differences. No W43 source row caused or resolved these observations.
2. **DQ-001:** historical awake/awakening duplication remains on **14 dates**. This issue predates the W43 append and should not be suppressed or presented as a new W43 failure.

Other recorded limitations:

- **DQ-011** remains open for the September 8 resting-heart-rate source verification; no retroactive change is authorized here.
- The exact **VA blood collection date** is inconsistent among available records; no public date is manufactured.
- The October 26 waking weight is genuinely missing; some activity measurements on October 28 and 30 are **partial-day snapshots** and not final comparable daily totals.
- **Daily HRV and overnight HRV** are different acquisition windows, as are daily resting HR and average sleeping HR.
- The consumer REM stage estimates are Low confidence; vivid dreams cannot validate device staging.
- The **trap-bar's own mass**, witnessed movement fidelity, symptomatic delayed response and full heaviest-level repeatability remain unverified.
- Travel and sleep changes do not establish the anatomical cause of lumbar restriction, and favorable wearable metrics are not clinical clearance.
- Calories, protein adequacy, energy availability and body-composition changes were not independently measured for the week.
- The archive's internal week index is not equivalent to the ISO calendar label without documented mapping.

These issues are **tracked evidence boundaries**, not grounds to silently rewrite the source. No claim that technical PASS extinguishes them is made.

---

## 9. Protected scientific and governance state

The baseline-to-pre-audit compare contains **16 expected changed paths**: five governed append-only data/provenance paths, two weekly reports and nine current-facing surfaces. It contains **no modified validator, GitHub Actions workflow, snapshot/source-export, model-error, methodology, phase-map, prediction or release-governance file**.

The original five Python validator blob identities and \`.github/workflows/validate.yml\` are identical on baseline \`main\` and the verified pre-audit head.

Protected states:

- **Phase:** Phase 2 — Load Integration; broader substate **Consolidation / lock-in observation**; **Phase 2D undeclared**.
- **Predictions:** historical 041–046 closed/scored; prospective November Model Errors **047–050 open, forecast-locked and unscored**. The 2026-10-19 scoring registration remains unchanged.
- **August:** protected molecular outputs, source documents, body-composition measurements and closed Model Error 043 (\`overall_improvement_not_met\` / \`over\`) passed the cross-layer validator.
- **Release:** frozen published **v1.1.0** tag remains at \`92126e1cc882c3822d9e03b30b11cfc1d30b4fbb\`; version DOI **10.5281/zenodo.22759132**, all-versions DOI **10.5281/zenodo.20815611**. No new release or DOI is authorized.
- **Private boundary:** the retained v1.37 workbook and long-form operator narrative are not public artifacts; public records contain scoped curated evidence and source identity rather than full private content.

Prior completed reports, source corrections, prediction hypotheses and admissibility rules are not retrospectively redefined by this rollover.

---

## 10. Publication decision and required exact-final-head gate

**Batch 4 determination:** **INTEGRITY PASS**, with two inherited official warnings and explicit scientific/source limitations.

**Batch 5 audit artifact:** This file is to be committed **alone** to \`docs/audits/2026-11-02-post-weekly-rollover-audit.md\`; it does **not** revise \`CHANGELOG.md\` or any earlier file. GitHub \`main\` remains at the unchanged baseline until an independently reviewed PR is merged.

**Publication decision:** **CONDITIONAL GO to exact-audit-head CI and subsequent PR review, but no permission to merge from the pre-audit CI result alone.**

Required sequence after this document is committed:

1. Read the **new audit commit SHA** and confirm this audit is its **sole changed file** versus \`b81c449e64dcd42a311711e9f161ff5d921df03f\`.
2. Obtain and inspect the GitHub Actions run for **that exact new SHA**, not a prior branch run. Confirm the same **five unchanged official validators** completed successfully. Record any warnings and new Markdown/reference counts accurately.
3. Compare the final branch against baseline production \`main\`: the previously approved **16 rollover paths plus this one audit file**, no unexpected changes or protected artifact modifications.
4. Verify W43 Closed / W44 Active, the row endpoints, locked Model Errors 047–050, undeclared Phase 2D, source provenance, DQ status and frozen v1.1.0 identity.
5. Permit Batch 6 PR review/merge only **after** exact-head CI and all integrity/provenance gates are verified. Following merge, independently verify production \`main\` and its separate post-merge CI.
6. Do **not** create a new version tag/Zenodo DOI, rescore forecasts, infer future W44 observations or declare full lumbar recovery.

At authoring time, **run 41485871108 validates the pre-audit head only**. A successful new audit-commit CI result must be observed independently; it is not pre-claimed by this document.
