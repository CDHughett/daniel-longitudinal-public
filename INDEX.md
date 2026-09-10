# Daniel Longitudinal Study — Index

This is the complete navigation map for the governed public longitudinal archive.

The repository separates evidence, structured data, interpretation, prediction, governance, and validation so those layers remain inspectable independently.

---

# Tier 1 — First Contact

- [`README.md`](./README.md) — archive scope, current state, and machine-readable orientation
- [`docs/START_HERE.md`](./docs/START_HERE.md) — first five minutes
- [`LATEST.md`](./LATEST.md) — current executive system state
- [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
- [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md) — public evidence coverage
- [`docs/CONCEPTS.md`](./docs/CONCEPTS.md) — terminology

Broader observer guidance:

- [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md)
- [`docs/NEWCOMER_PATH.md`](./docs/NEWCOMER_PATH.md)

---

# Current State

```text
Active phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Active weekly window:
2026-W36

Most recent closed window:
2026-W35

Open model-error records:
none in protected block 041–046

Recently closed:
041, 042, 043, 044, 045, 046

Record 043:
closed / not supported — overall_improvement_not_met / over

Formal Phase 2D:
undeclared

August physical snapshot:
complete

August TruDiagnostic provider-result artifacts:
complete and checksum-registered

August structured molecular integration:
complete for currently represented fields
```

Current state source: [`LATEST.md`](./LATEST.md)

---

# Machine-Readable Core

The structured public layer is:

| Dataset | Role |
|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | daily physiology + bounded subjective state |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | canonical sleep |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | session-level training exposure |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | bounded contextual/perturbation events |
| [`data/model_error/model_error_gap_v1.csv`](./data/model_error/model_error_gap_v1.csv) | prediction → outcome → error |

Live row counts/endpoints: [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
Schema: [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)
Definitions: [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
Quality notes: [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

---

# Provenance

## Public Source Artifacts and Exports

- [`snapshots/`](./snapshots/)
- [`data/source_exports/`](./data/source_exports/)
- [`data/source_exports/ringconn/2026-07-21/`](./data/source_exports/ringconn/2026-07-21/)
- [`MEASUREMENT_SOURCES.md`](./MEASUREMENT_SOURCES.md)

## Private Daniel Dataset Provenance

- [`data/source_provenance/README.md`](./data/source_provenance/README.md)
- [`data/source_provenance/daniel_dataset_private_manifest.csv`](./data/source_provenance/daniel_dataset_private_manifest.csv)

The manifest records exact-file SHA-256 only when the retained private source was actually available for hashing.

## August TruDiagnostic Source Reconciliation

- [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](./data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

This record preserves the distinction between provider-displayed administrative metadata and the contemporaneous repository collection record that controls the actual 2026-08-17 sample event and preparation conditions.

---

# Data and Biological Snapshot Layer

- [`data/biomarker_snapshot.csv`](./data/biomarker_snapshot.csv)
- [`data/epigenetic_longitudinal.csv`](./data/epigenetic_longitudinal.csv)
- [`data/bloodwork_longitudinal.csv`](./data/bloodwork_longitudinal.csv)
- [`SNAPSHOT_LOG.md`](./SNAPSHOT_LOG.md)
- [`EPOCH_INDEX.md`](./EPOCH_INDEX.md)
- [`snapshots/2026-08/2026-08 Epoch.md`](./snapshots/2026-08/2026-08%20Epoch.md)
- [`methodology/2026-08-snapshot-collection-plan.md`](./methodology/2026-08-snapshot-collection-plan.md)
- [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](./data/source_provenance/2026-08-trudiagnostic-reconciliation.md)
- [`data/model_error/record_043_closure.md`](./data/model_error/record_043_closure.md)

Current August physical and molecular source artifacts are preserved under [`snapshots/2026-08/`](./snapshots/2026-08/), with SHA-256 registration in the folder manifest.

---

# Reports

- [`reports/README.md`](./reports/README.md) — report lifecycle
- [`reports/2026-W36.md`](./reports/2026-W36.md) — current active report
- [`reports/2026-W35.md`](./reports/2026-W35.md) — most recent closed report
- [`reports/2026-W34.md`](./reports/2026-W34.md) — prior ordinary continuity window
- [`reports/2026-W33.md`](./reports/2026-W33.md) — August testing/reload window
- [`reports/`](./reports/) — full weekly report series

Reports interpret recorded evidence. They do not replace source artifacts or canonical datasets.

---

# Prediction and Model-Error Layer

Primary files:

- [`data/model_error/WHAT_THIS_LAYER_IS.md`](./data/model_error/WHAT_THIS_LAYER_IS.md)
- [`data/model_error/README.md`](./data/model_error/README.md)
- [`data/model_error/model_error_gap_v1.csv`](./data/model_error/model_error_gap_v1.csv)
- [`data/model_error/record_043_closure.md`](./data/model_error/record_043_closure.md)
- [`data/model_error/udi_by_type_tracker.csv`](./data/model_error/udi_by_type_tracker.csv)
- [`data/model_error/calibration_events_log.md`](./data/model_error/calibration_events_log.md)
- [`data/model_error/historical/`](./data/model_error/historical/)

Evaluation methodology:

- [`methodology/prediction_evaluation.md`](./methodology/prediction_evaluation.md)
- [`docs/methodology/valid_prediction_criteria.md`](./docs/methodology/valid_prediction_criteria.md)
- [`docs/methodology/prediction_to_outcome_pipeline.md`](./docs/methodology/prediction_to_outcome_pipeline.md)

Registered plans:

- [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)
- [`methodology/open_prediction_evaluation_plan_045.md`](./methodology/open_prediction_evaluation_plan_045.md)
- [`methodology/open_prediction_evaluation_plan_046.md`](./methodology/open_prediction_evaluation_plan_046.md)

The protected 041–046 block is fully closed. Original prospective registration provenance and prediction narratives remain preserved.

---

## UDI

UDI canonically means **Unobstructed Delta Index**.

Framework:

[`docs/methodology/UDI_framework_v1.md`](./docs/methodology/UDI_framework_v1.md)

Current reporting remains stratified across point/range UDI and state/trajectory concordance.

UDI is a prediction-calibration construct, not a biological score.

---

## Future Model-Error Schema

Design-only future semantic split:

[`docs/methodology/model_error_schema_v2.md`](./docs/methodology/model_error_schema_v2.md)

The future design separates:

```text
registration_status
```

from:

```text
model_calibration_scope
```

without rewriting the protected v1 record history.

---

# Governance and Methodology

Core governing documents:

- [`SYSTEM_OVERVIEW.md`](./SYSTEM_OVERVIEW.md)
- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`METHODOLOGY_AND_CONTROLS.md`](./METHODOLOGY_AND_CONTROLS.md)
- [`ASSUMPTIONS_AND_BOUNDARIES.md`](./ASSUMPTIONS_AND_BOUNDARIES.md)
- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)
- [`PHASE_MAP.md`](./PHASE_MAP.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)
- [`STATE_TRANSITIONS.md`](./STATE_TRANSITIONS.md)
- [`RISK_MANAGEMENT.md`](./RISK_MANAGEMENT.md)
- [`VERSIONING.md`](./VERSIONING.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- [`methodology/anonymization.md`](./methodology/anonymization.md)

---

# AI-Assistance Transparency

Disclosure:

[`docs/AI_ASSISTANCE.md`](./docs/AI_ASSISTANCE.md)

AI may assist with source-backed structuring, drafting, analysis, validation code, audits, and formally governed prediction generation.

AI is not a source-evidence class and cannot override the archive's source hierarchy.

---

# Validation and CI

Validation guide:

[`tools/README.md`](./tools/README.md)

Core validator:

[`tools/validate_repository.py`](./tools/validate_repository.py)

Machine-readable validator:

[`tools/validate_machine_readable.py`](./tools/validate_machine_readable.py)

GitHub Actions workflow:

[`.github/workflows/validate.yml`](./.github/workflows/validate.yml)

Both validators run on pushes to `main` and on pull requests.

Broader verification documentation:

[`VERIFICATION.md`](./VERIFICATION.md)

Formal audits:

[`docs/audits/`](./docs/audits/)

---

# Schema Layer

- [`schemas/README.md`](./schemas/README.md)
- [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)
- [`schemas/weekly-report-template.md`](./schemas/weekly-report-template.md)
- [`schemas/experiment-template.md`](./schemas/experiment-template.md)
- [`schemas/metrics-dictionary.md`](./schemas/metrics-dictionary.md)

---

# Protocol and Experiment History

- [`protocols/`](./protocols/)
- [`experiments/`](./experiments/)

Presence in the repository does not imply current exposure. Active/historical status must be established from current state and the applicable document.

---

# Dashboards and Derived Views

- [`dashboards/`](./dashboards/)
- [`LATEST.md`](./LATEST.md)

Derived views compress lower-level evidence and cannot strengthen claims beyond their sources.

---

# Release and Archive Metadata

- [`CITATION.cff`](./CITATION.cff)
- [`CODEMETA.json`](./CODEMETA.json)
- [`VERSIONING.md`](./VERSIONING.md)
- [`CHANGELOG.md`](./CHANGELOG.md)
- [`docs/archive/CHANGELOG_ARCHIVE.md`](./docs/archive/CHANGELOG_ARCHIVE.md)
- [`LICENSE.md`](./LICENSE.md)

Current DOI-bearing release:

```text
v1.0.0
```

Live `main` contains later unreleased work.

---

# Recommended Reading Flows

## First Contact

```text
README
→ START_HERE
→ LATEST
→ DATA_COVERAGE
→ OBSERVER_QUICKSTART
```

## Data Inspection

```text
DATA_COVERAGE
→ machine-readable schema
→ core CSVs
→ source provenance / source exports
→ DATA_QUALITY_NOTES
→ relevant report
```

## Prediction Review

```text
model_error_gap_v1.csv
→ applicable registered evaluation plan
→ source evidence
→ closure record
→ UDI / concordance layer
```

## Verification

```text
validate_repository.py
+
validate_machine_readable.py
→ governed warnings / errors
→ human semantic review
→ formal audit when required
```

---

# Correction Path

```text
Preserve current state
→ locate strongest source
→ classify discrepancy
→ document finding
→ make only source-supported correction
→ preserve Git history
→ rerun validation
→ review dependent summaries
```

Relevant files:

- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)
- [`CHANGELOG.md`](./CHANGELOG.md)

---

# Archive Standard

The repository aims to preserve:

- continuity
- source traceability
- machine readability
- explicit uncertainty
- source-backed correction
- prediction accountability
- fixed outcome boundaries
- reproducible mechanical validation
- retrospective phase governance
- separation of source, data, interpretation, and model layers

No claim extends beyond the recorded single-subject archive without separate evidence.
