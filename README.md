# Daniel Longitudinal Study

*A governed longitudinal observational archive*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20815612.svg)](https://doi.org/10.5281/zenodo.20815612)

This archive began as a personal health project, evolved into a longitudinal observational archive, and now documents an ongoing effort to learn from reality through repeated measurement, prediction auditing, and error correction.

This repository documents the behavior of a single human system across time under defined constraints.

It contains:

- longitudinal biomarker and sleep data
- weekly system-state reports
- a prediction-versus-observed-outcome review layer
- structured methodology, governance, and constraints
- a defined relationship between governed archive records and real-time subjective telemetry

---

## DOI and Versioning Note

The Zenodo DOI points to the archived `v1.0.0` release snapshot.

The `main` branch may include post-publication documentation updates, including DOI badges, citation text, metadata cleanup, methodology refinement, navigation improvements, new prospective prediction records, retrospective closeouts, and later snapshot artifacts.

For citation, use the Zenodo DOI-linked release record:

Hughett, C. D. (2026). *Daniel Longitudinal Study (v1.0.0)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20815612

---

## First 5 Minutes

If this is your first visit, read in this order:

1. [`docs/START_HERE.md`](./docs/START_HERE.md) — 5-minute orientation
2. [`LATEST.md`](./LATEST.md) — current system state
3. [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
4. [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md) — broader observer evaluation path
5. [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md) — what data is and is not included
6. [`docs/CONCEPTS.md`](./docs/CONCEPTS.md) — recurring terms

This path is enough to understand what the archive is, what it claims, what it does not claim, and where the evidence lives.

Use these based on depth:

- [`docs/START_HERE.md`](./docs/START_HERE.md) — first 5 minutes
- [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
- [`docs/NEWCOMER_PATH.md`](./docs/NEWCOMER_PATH.md) — first full reading pass
- [`INDEX.md`](./INDEX.md) — complete repository map

---

## What Makes This Different

This is not a blog, protocol, intervention program, or theory thread.

Everything preserved here is intended to be:

- measured or contemporaneously observed
- logged
- versioned
- auditable

Biological interpretation remains retrospective and artifact-bound.

Forward predictions are permitted only when they are:

- explicitly registered in the model-error layer
- stated before the relevant outcome is known
- time-bounded
- preserved without hindsight revision
- evaluated against observed outcomes after their windows close

Predictions are calibration instruments, not claims of certainty.

A completed prediction remains preserved after scoring.

A later related question should receive a new prospective record rather than silently extending or reopening the earlier one.

---

## Current State

→ [`LATEST.md`](./LATEST.md)

This is the fastest way to understand the system's current observed state.

Current archive posture includes:

```text
Phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Active weekly window:
2026-W33

Recently closed model-error records:
041 — supported
042 — not supported / continued adaptation
044 — not supported / narrow governance deviation
045 — supported

Current open model-error records:
043
046

August physical snapshot collection:
complete

August TruDiagnostic provider results:
pending

Formal Phase 2D declaration:
None
```

Record 041 closed with the registered recovery-capacity prediction supported.

Record 042 closed against the model: continued adaptation exceeded the predicted ambient-execution plateau.

Record 044 closed against the model after a testing-directed pre-snapshot Load Integration omission violated the separately registered snapshot-governance boundary.

Record 045 remains closed and supported.

Record 043 remains open pending the primary TruDiagnostic provider-result domain.

Record 046 remains prospectively open through its fixed unload/reload scoring window.

---

## How to Evaluate This Archive

Use `/snapshots` for primary evidence.  
Use `/reports` for retrospective interpretation.  
Use `/data` for structured longitudinal datasets.  
Use `/data/model_error` for prediction-versus-observed-outcome review.  
Use `/methodology` and `/docs/methodology` for evaluation and governance rules.

For a compact inspection route, see [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md).

For the broader skeptical or technical review path, see [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md).

For the preregistered evaluation rules governing records 041–044, see:

[`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

Records 041, 042, and 044 have now been adjudicated.

Record 043 remains open under that preregistered framework pending its required primary biological evidence.

For the completed preregistered evaluation rules that governed record 045, see:

[`methodology/open_prediction_evaluation_plan_045.md`](./methodology/open_prediction_evaluation_plan_045.md)

For the separately registered prospective evaluation rules governing record 046, see:

[`methodology/open_prediction_evaluation_plan_046.md`](./methodology/open_prediction_evaluation_plan_046.md)

These records remain separate because their registration dates, evidence windows, and scoring questions differ.

Record 046 does not reopen or extend record 045.

Later unload/reload evidence does not reopen records 041, 042, or 044.

---

## Start Here

- [`docs/START_HERE.md`](./docs/START_HERE.md) — first-contact orientation
- [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
- [`docs/NEWCOMER_PATH.md`](./docs/NEWCOMER_PATH.md) — extended reading path for first-time visitors
- [`docs/CONCEPTS.md`](./docs/CONCEPTS.md) — glossary of recurring archive concepts
- [`LATEST.md`](./LATEST.md) — current system state
- [`snapshots`](./snapshots/) — primary artifacts and source evidence
- [`reports`](./reports/) — structured retrospective interpretation
- [`data`](./data/) — structured longitudinal datasets
- [`TELEMETRY.md`](./TELEMETRY.md) — relationship between the governed archive and real-time public subjective telemetry

---

## System Flow

```text
Protocol Inputs
      ↓
Biological System
      ↓
Measurement Layer
(sleep, HRV, body composition, biomarkers)
      ↓
Dataset Layer
(versioned tracking)
      ↓
Snapshots
(primary artifacts)
      ↓
Reports
(retrospective interpretation)
      ↓
Model-Error Layer
(registered prediction vs. observed outcome)
      ↓
Model Correction
```

---

## Dataset Orientation

This repository documents a longitudinal observation of a human performance system operating under defined constraints.

The archive preserves continuity across:

- body-composition measurements
- training-architecture evolution
- phase-based system progression
- governance and constraint frameworks
- biomarker and system-health snapshots where publicly included
- prediction-versus-observed-outcome tracking as an auxiliary calibration layer
- separation between governed records and informal subjective telemetry

**Data scope and limitations:**  
→ [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)

**Known structured-data quality questions:**  
→ [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

**Model-error layer context:**  
→ [`data/model_error/WHAT_THIS_LAYER_IS.md`](./data/model_error/WHAT_THIS_LAYER_IS.md)

**Subjective telemetry context:**  
→ [`TELEMETRY.md`](./TELEMETRY.md)

**Note:** Some biomarker data may be referenced in reports but not included in the public archive.

SHA-256 verification is provided for binary snapshot artifacts where applicable.

---

## External Observers

If you are evaluating the system structure directly:

→ [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md)

For the broader observer review path:

→ [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md)

---

## Archive Posture

This repository is maintained as a longitudinal observational archive.

Interpretation remains intentionally constrained:

- artifacts take precedence over language
- observations remain provisional
- conclusions require repeated evidence across time
- biological interpretation remains retrospective
- registered predictions remain isolated in the model-error layer
- prediction wording is preserved until the applicable observation window closes
- completed predictions retain their original evidence and scoring boundaries
- later related observations require a separate prospective record when they represent a new question
- observations that generate predictions remain distinct from future evidence permitted to score them
- subjective context is separated from governed archive records unless formally incorporated
- documented protocol or collection deviations remain visible rather than being retrospectively normalized
- prediction misses remain visible rather than being softened after outcome access
- protocol documents describe this subject’s archive and are not generalized prescriptions

This archive documents one subject under defined protocol constraints and incomplete environmental control.

No claim extends beyond the recorded system without separate evidence.

---

## Current Phase Context

**Phase 2 — Load Integration**

**Operating substate:** Consolidation / lock-in observation

→ [`PHASE_MAP.md`](./PHASE_MAP.md)

Phase language is retrospective and evidence-earned.

Record 042 now establishes that the registered ambient-execution plateau prediction underestimated continued adaptation under the existing architecture.

That is meaningful evidence of continued consolidation.

It does not independently declare Phase 2D.

Record 041 support likewise does not establish unlimited recovery capacity.

Record 044 failure does not independently terminate the current phase or invalidate the underlying training architecture.

Record 045 remains closed and supported.

A supported or failed record 046 result likewise cannot independently declare or terminate a phase.

Formal Phase 2D remains undeclared.

---

## Temporal Navigation

- [`EPOCH_INDEX.md`](./EPOCH_INDEX.md) — temporal index of snapshot epochs
- [`SNAPSHOT_LOG.md`](./SNAPSHOT_LOG.md) — chronological artifact record
- [`snapshots`](./snapshots/) — primary artifact windows

Recommended flow:

`LATEST.md`  
→ `EPOCH_INDEX.md`  
→ `SNAPSHOT_LOG.md`  
→ `/snapshots/YYYY-MM/`

---

## Repository Structure

```text
Root
│
├── snapshots/
├── reports/
├── dashboards/
│
├── data/
│   └── model_error/
│
├── protocols/
├── experiments/
├── schemas/
├── methodology/
├── docs/
│   ├── audits/
│   └── methodology/
│
├── roadmap/
│
├── README.md
├── INDEX.md
├── LATEST.md
├── TELEMETRY.md
├── CHANGELOG.md
```

Historical or superseded protocol material may remain in the repository for provenance when its inactive status is clearly identified.

Completed or partially completed preregistration artifacts may likewise remain under their original filenames when preserving the original committed artifact is preferable to renaming it after outcome access.

---

## Prediction Governance

The prediction layer exists to test model calibration rather than demonstrate foresight.

Registered predictions must be:

- specific enough to evaluate
- preserved without outcome-driven rewriting
- linked to an observation window
- closed only after sufficient evidence exists
- scored independently where multiple domains are involved
- retained when evidence is insufficient rather than forced into a pass or failure
- retained after closure so the original prediction and outcome remain inspectable

Current open model-error records:

```text
043
046
```

Recently closed records:

```text
041 — supported
042 — not supported / continued adaptation
044 — not supported / narrow snapshot-directed governance deviation
045 — supported
```

Records 041–044 were registered under:

→ [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

Records 041, 042, and 044 are now closed.

Record 043 remains open under the same preregistered evaluation framework because its primary TruDiagnostic evidence is still pending.

Record 045 was separately governed by:

→ [`methodology/open_prediction_evaluation_plan_045.md`](./methodology/open_prediction_evaluation_plan_045.md)

Record 046 is separately governed by:

→ [`methodology/open_prediction_evaluation_plan_046.md`](./methodology/open_prediction_evaluation_plan_046.md)

---

### Record 041 — Closed Recovery-Capacity Prediction

Record 041 predicted:

```text
stable
```

It closed as:

```text
actual:
stable

outcome:
supported
```

Accumulated July–August exposure produced measurable autonomic compression.

The registered recovery-capacity failure boundary nevertheless was not crossed.

No qualifying combination of:

- recovery-driven intervention
- multi-session training regression
- persistent physiological suppression with corresponding functional or subjective deterioration

was observed.

The later autonomic rebound does not imply the accumulation block was costless.

Record 041 establishes only that the observed cost remained inside its preregistered recovery-capacity boundary.

---

### Record 042 — Closed Ambient-Execution Plateau Prediction

Record 042 predicted:

```text
plateau
```

It closed as:

```text
actual:
continued_adaptation

error direction:
under

outcome:
not supported
```

The registered counter-evidence threshold was met across repeated dates, more than 14 calendar days, multiple contexts, and without substantive explanatory protocol progression.

Evidence included increasing:

- positional optionality
- voluntary tempo control
- divided-attention execution
- automatic movement organization
- reduced cognitive overhead
- low-salience execution
- preservation across accumulated workload and differing autonomic states

The external protocol remained broadly stable while the relationship to the work continued changing.

Record 042 therefore represents a model underestimation rather than a failure of the observed system.

It does not independently declare Phase 2D.

---

### Record 044 — Closed Protocol-Governance Prediction

Record 044 predicted:

```text
preserved
```

Most of the observation window showed strong governance restraint.

However:

```text
2026-08-16:
Load Integration intentionally withheld
to preserve recovery before VO₂ testing
```

The omission was:

- testing-directed
- intentional
- not provider-required
- not recovery-driven

The August collection plan had established a representative-state posture rather than deliberate short-term testing optimization.

Record 044 contained a separately registered snapshot-manipulation boundary.

The pre-test Load Integration omission conflicted with that boundary.

Record 044 therefore closed as:

```text
outcome:
not supported

classification:
narrow snapshot-directed governance deviation
```

This does not establish:

- broad protocol-governance collapse
- biological harm
- invalidity of the August snapshot
- failure of record 041
- failure of record 045

The archive preserves the governance miss without inferring an unmeasured biological effect.

---

### Record 045 — Completed Autonomic Reconvergence Probe

Record 045 was registered prospectively on:

```text
2026-08-12
```

Its admissible scoring window was:

```text
2026-08-13 through 2026-08-16
```

For record 045:

```text
Registration context only:
2026-W31
2026-08-10
2026-08-11
2026-08-12

Admissible scoring evidence:
2026-08-13
2026-08-14
2026-08-15
2026-08-16

Excluded:
2026-08-17 through 2026-08-18 snapshot outcomes
later unload/reload evidence
```

The four preregistered favorable thresholds were:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

Observed four-day means were:

```text
Daily HRV:
63.5 ms

Sleep HRV:
71.25 ms

Resting HR:
46.5 bpm

Sleeping HR:
51.75 bpm
```

Result:

```text
4 of 4 favorable thresholds
```

No multi-session functional regression occurred.

No recovery-driven protocol reduction or intervention occurred.

Record 045 was therefore scored:

```text
supported
```

The 2026-08-16 Load Integration omission was testing-directed rather than recovery-driven for purposes of the record 045 failure rule.

The same event was separately relevant to record 044 because record 044 governed snapshot preparation rather than recovery-driven intervention.

Record 045 is closed.

It must not be reopened using later unload/reload evidence.

---

### Record 043 — Active August Biological Translation Prediction

Record 043 remains open.

Its primary comparison remains:

```text
May 2026
→
August 2026
```

The August physical collection is complete.

Current preserved physical domains include:

- DEXA
- VO₂ max
- Bod Pod

The TruDiagnostic sample was collected on:

```text
2026-08-17
```

The primary TruDiagnostic provider-result domain remains pending.

No supplemental physical result may substitute for that primary evidence.

The record 044 governance determination does not establish whether the August 16 training deviation materially altered any biological result.

That materiality remains unknown unless supported by separate evidence.

Record 043 must remain open until its required primary source evidence is available.

---

### Record 046 — Active Autonomic Unload/Reload Probe

Record 046 was registered separately on:

```text
2026-08-17
```

Its prediction is:

```text
reconvergence_persists_after_unload_reload
```

Its evidence structure is fixed as:

```text
2026-08-17:
registration context only

2026-08-18 through 2026-08-19:
descriptive unload / re-entry kinetics

2026-08-20 through 2026-08-23:
primary scoring window
```

Record 046 reuses the record 045 autonomic thresholds without recalibration:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

Support requires:

```text
at least 3 of 4 favorable autonomic thresholds

AND

no multi-session functional regression after reload

AND

no recovery-driven protocol reduction after normal training resumes
```

The August biological and performance outcomes are excluded from record 046 scoring.

This includes:

- TruAge
- TruHealth
- TruDiagnostic
- DEXA
- VO₂ max
- Bod Pod

A transient autonomic disturbance after maximal VO₂ testing may be documented but does not independently fail record 046.

Record 046 does not:

- reopen record 041
- reopen record 042
- repair record 044
- reopen record 045
- determine the August biological snapshot outcome
- declare Phase 2D

---

## August Snapshot Governance

The August biological and performance collection remains governed by:

→ [`methodology/2026-08-snapshot-collection-plan.md`](./methodology/2026-08-snapshot-collection-plan.md)

and, for the original records 041–044 framework:

→ [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

The primary physical collection window was completed across:

```text
2026-08-17
TruDiagnostic sample collection
DEXA
VO₂ max

2026-08-18
Bod Pod
```

Current August state:

```text
physical collection:
complete

physical source-artifact preservation:
complete

TruDiagnostic sample collection:
complete

TruDiagnostic provider results:
pending

complete biological interpretation:
pending
```

The underlying physical architecture remains:

```text
B1
+
Load Integration
```

The actual testing transition was:

```text
2026-08-16:
B1 completed
Load Integration intentionally withheld before testing

2026-08-17:
No B1
No Load Integration
TruDiagnostic
DEXA
VO₂ max

2026-08-18:
No B1
No Load Integration
Bod Pod

2026-08-19:
Planned return to normal B1 + Load Integration
```

The 2026-08-16 Load Integration omission and the August 17–18 training withdrawal remain visible as actual collection-condition facts.

They are not retrospectively rewritten into the original representative-state collection posture.

The governance significance of the August 16 omission has been adjudicated under record 044.

The record closed as not supported because the testing-directed omission conflicted with the registered snapshot-manipulation boundary.

That governance result does not establish that the deviation materially altered any August biological measurement.

Record 043 therefore remains open pending its primary TruDiagnostic evidence.

The biological snapshot and Model Error 046 remain analytically separate.

---

## Current Prediction Calibration State

The August 18 closure batch changed the primary state and trajectory concordance layers.

Current tracked primary-prediction concordance includes:

```text
State:
11 concordant of 14 eligible closed primary state predictions
0.79

Trajectory:
2 concordant of 3 eligible closed primary trajectory predictions
0.67
```

Point and range magnitude UDI values remain unchanged by this closure batch.

These values are calibration summaries.

They are not measures of biological success.

A prediction miss may reflect:

- model underestimation
- model overestimation
- governance failure
- boundary-condition discovery
- insufficient evidence

The underlying record determines interpretation.

---

## Governance

- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)
- [`RISK_MANAGEMENT.md`](./RISK_MANAGEMENT.md)
- [`TELEMETRY.md`](./TELEMETRY.md)
- [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)
- [`methodology/open_prediction_evaluation_plan_045.md`](./methodology/open_prediction_evaluation_plan_045.md)
- [`methodology/open_prediction_evaluation_plan_046.md`](./methodology/open_prediction_evaluation_plan_046.md)
- [`methodology/2026-08-snapshot-collection-plan.md`](./methodology/2026-08-snapshot-collection-plan.md)

---

## Scope

Single-subject longitudinal observational archive.

This repository does not establish:

- population-level causality
- clinical efficacy
- generalized intervention guidance
- a protocol suitable for direct replication without independent review
- certainty from prediction accuracy

Claims remain bounded to the recorded subject, artifacts, methods, and observation windows.

---

## License

CC BY-NC-ND 4.0

---

## Citation

If you use or reference this archive, please cite:

Hughett, C. D. (2026). *Daniel Longitudinal Study (v1.0.0)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20815612

---

## Navigation

- First 5 minutes → [`docs/START_HERE.md`](./docs/START_HERE.md)
- Current state → [`LATEST.md`](./LATEST.md)
- Observer quickstart → [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md)
- Observer evaluation → [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md)
- Data coverage → [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- Data-quality notes → [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)
- Recurring terms → [`docs/CONCEPTS.md`](./docs/CONCEPTS.md)
- Guided orientation → [`docs/NEWCOMER_PATH.md`](./docs/NEWCOMER_PATH.md)
- Index → [`INDEX.md`](./INDEX.md)
- Epoch tracking → [`EPOCH_INDEX.md`](./EPOCH_INDEX.md)
- Snapshot log → [`SNAPSHOT_LOG.md`](./SNAPSHOT_LOG.md)
- Artifact history → [`snapshots`](./snapshots/)
- Weekly reports → [`reports`](./reports/)
- Model-error layer → [`data/model_error/WHAT_THIS_LAYER_IS.md`](./data/model_error/WHAT_THIS_LAYER_IS.md)
- Preregistered prediction plan 041–044 → [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)
- Completed prediction plan 045 → [`methodology/open_prediction_evaluation_plan_045.md`](./methodology/open_prediction_evaluation_plan_045.md)
- Open-prediction plan 046 → [`methodology/open_prediction_evaluation_plan_046.md`](./methodology/open_prediction_evaluation_plan_046.md)
- August collection plan → [`methodology/2026-08-snapshot-collection-plan.md`](./methodology/2026-08-snapshot-collection-plan.md)
- Telemetry layer → [`TELEMETRY.md`](./TELEMETRY.md)
- Versioning → [`VERSIONING.md`](./VERSIONING.md)

---

_Public longitudinal archive initiated 2026._
