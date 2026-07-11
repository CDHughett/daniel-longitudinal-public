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

The `main` branch may include post-publication documentation updates, including DOI badges, citation text, metadata cleanup, methodology refinement, and navigation improvements.

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

---

## Current State

→ [`LATEST.md`](./LATEST.md)

This is the fastest way to understand the system's current observed state.

---

## How to Evaluate This Archive

Use `/snapshots` for primary evidence.  
Use `/reports` for retrospective interpretation.  
Use `/data` for structured longitudinal datasets.  
Use `/data/model_error` for prediction-versus-observed-outcome review.  
Use `/methodology` and `/docs/methodology` for evaluation and governance rules.

For a compact inspection route, see [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md).

For the broader skeptical or technical review path, see [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md).

For the prospective evaluation rules governing the current prediction block, see [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md).

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
- subjective context is separated from governed archive records unless formally incorporated
- protocol documents describe this subject’s archive and are not generalized prescriptions

This archive documents one subject under defined protocol constraints and incomplete environmental control.

No claim extends beyond the recorded system without separate evidence.

---

## Current Phase Context

**Phase 2 — Load Integration**

→ [`PHASE_MAP.md`](./PHASE_MAP.md)

Phase language is retrospective and evidence-earned.

Open prediction outcomes may contribute to a later phase evaluation but do not independently declare a phase transition.

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

Current open-record evaluation rules:

→ [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

Model-error layer:

→ [`data/model_error/WHAT_THIS_LAYER_IS.md`](./data/model_error/WHAT_THIS_LAYER_IS.md)

---

## Governance

- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)
- [`RISK_MANAGEMENT.md`](./RISK_MANAGEMENT.md)
- [`TELEMETRY.md`](./TELEMETRY.md)
- [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

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
- Open-prediction evaluation plan → [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)
- Telemetry layer → [`TELEMETRY.md`](./TELEMETRY.md)
- Versioning → [`VERSIONING.md`](./VERSIONING.md)

---

_Public longitudinal archive initiated 2026._
