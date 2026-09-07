# Daniel Longitudinal Study

*A governed, machine-readable, single-subject longitudinal observational archive*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20815612.svg)](https://doi.org/10.5281/zenodo.20815612)

The Daniel Longitudinal Study documents one human system across time through repeated measurement, structured data, contemporaneous observation, retrospective interpretation, registered prediction evaluation, source-backed correction, and explicit archive governance.

This is not a clinical trial, coaching product, or generalized intervention protocol.

---

## First 5 Minutes

1. [`docs/START_HERE.md`](./docs/START_HERE.md) — first-contact orientation
2. [`LATEST.md`](./LATEST.md) — current executive system state
3. [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md) — what is and is not publicly structured
4. [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
5. [`docs/CONCEPTS.md`](./docs/CONCEPTS.md) — recurring terminology

Deeper review:

- [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md)
- [`docs/NEWCOMER_PATH.md`](./docs/NEWCOMER_PATH.md)
- [`INDEX.md`](./INDEX.md)

---

# Current Archive State

Current declared state:

```text
Phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Active weekly window:
2026-W36

Most recent closed window:
2026-W35

Open model-error record:
043

Recently closed:
041 — supported
042 — not supported / continued_adaptation
044 — not supported / narrow governance deviation
045 — supported
046 — not supported / failed_autonomic_recompression

August physical snapshot:
complete

August TruDiagnostic provider results:
pending

Formal Phase 2D declaration:
none
```

The installed physical architecture remains:

```text
B1
+
Load Integration
```

For current biological, training, recovery, and report details, use [`LATEST.md`](./LATEST.md).

---

# Machine-Readable Core

The public archive contains an aligned daily/session/event layer:

| Dataset | Unit |
|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | one row per represented day |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | one canonical governed wake-date row |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | one row per training/session block |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | one row per bounded contextual event |

**Live row counts and coverage endpoints are maintained in one place:** [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md).

The daily/training/event datasets are curated public extracts derived primarily from governed private `Daniel_Dataset_v1.x` source states. They are not raw provider exports.

Schema: [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)
Private-source provenance: [`data/source_provenance/`](./data/source_provenance/)

---

# Evidence Architecture

The repository intentionally separates layers that are often collapsed together:

```text
Source Artifacts
      ↓
Curated Structured Data
      ↓
Contemporaneous Context
      ↓
Retrospective Reports
      ↓
Phase / State Interpretation
      ↓
Registered Prediction Evaluation
      ↓
Model Correction
```

A higher-level interpretation does not overwrite the evidence beneath it.

The archive is designed to preserve disagreement as well as agreement.

Examples include:

- strong function alongside less-favorable recovery telemetry
- favorable biological observations alongside prediction misses
- broad governance discipline alongside a narrow governance failure
- later recovery that does not retrospectively rescue a failed fixed scoring window
- increasing behavioral automaticity without premature phase declaration

---

# Data and Provenance

Primary structured/public layers:

- [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv)
- [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv)
- [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv)
- [`data/context_events_v1.csv`](./data/context_events_v1.csv)
- [`data/biomarker_snapshot.csv`](./data/biomarker_snapshot.csv)
- [`data/bloodwork_longitudinal.csv`](./data/bloodwork_longitudinal.csv)
- [`data/epigenetic_longitudinal.csv`](./data/epigenetic_longitudinal.csv)
- [`data/model_error/model_error_gap_v1.csv`](./data/model_error/model_error_gap_v1.csv)

Direct provider/device source preservation:

- [`data/source_exports/`](./data/source_exports/)

Private-source provenance without publishing private workbooks:

- [`data/source_provenance/`](./data/source_provenance/)

Coverage and limitations:

- [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)
- [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
- [`MEASUREMENT_SOURCES.md`](./MEASUREMENT_SOURCES.md)

---

# Current Machine-Readable Schema Boundary

The daily/training/event schema explicitly distinguishes:

- measurement / source-transcribed fields
- subjective fields
- contextual / classified fields
- provenance fields

The current `training_blocks_v1.csv` field `duration_min` is a v1 compatibility field and is **not universally numeric**.

Scalar values are minutes. Historical ranges and compound expressions remain source-preserving expressions and must not be converted to a point estimate without a documented transformation.

A future schema may split raw/range/numeric duration fields rather than silently rewriting historical rows.

---

# Source Hierarchy and Correction

When records conflict, interpretation generally prioritizes:

1. verified primary source artifact
2. direct provider/device export
3. contemporaneous structured transcription
4. contemporaneous collection note
5. closed retrospective report
6. later evidence-grounded synthesis
7. unsupported memory

The repository prohibits silent alteration, outcome-driven rewriting, deletion of unfavorable valid evidence, unsupported reconstruction, and retrospective prediction revision.

Source-backed corrections must remain narrow, traceable, documented, and reviewed for downstream effects.

---

# Prediction Accountability

The model-error layer exists to evaluate model calibration rather than demonstrate foresight.

Current recent state:

| Record | Domain | Status | Outcome |
|---|---|---|---|
| 041 | recovery_capacity | Closed | supported |
| 042 | ambient_execution | Closed | not supported — continued adaptation |
| 043 | biological_translation | Open | TruDiagnostic provider results pending |
| 044 | protocol_governance | Closed | not supported — narrow snapshot-directed deviation |
| 045 | autonomic_reconvergence | Closed | supported |
| 046 | autonomic_unload_reload | Closed | failed_autonomic_recompression |

Wrong predictions remain visible.

Fixed scoring windows remain fixed.

The original registered prediction text for protected records remains distinguishable from later closure language.

---

## UDI

UDI canonically means **Unobstructed Delta Index**.

The current framework reports prediction calibration by type:

```text
UDI_point
UDI_range
State_concordance
Trajectory_concordance
```

State and trajectory predictions are not forced into magnitude UDI.

Composite UDI remains withheld under its predefined sample-size criteria.

UDI is not a biological score.

Methodology:

[`docs/methodology/UDI_framework_v1.md`](./docs/methodology/UDI_framework_v1.md)

---

## Model-Error Schema Semantics

The historical v1 field `calibration_state` carries legacy semantic debt because prospective registration and subject-specific model calibration are separate concepts.

For protected recent records 041–046, `calibration_state=pre` records prospective registration provenance and remains unchanged after closure.

Future design separates:

```text
registration_status
```

from:

```text
model_calibration_scope
```

without rewriting current v1 records.

See [`docs/methodology/model_error_schema_v2.md`](./docs/methodology/model_error_schema_v2.md).

---

# August 2026 Snapshot

Physical collection was completed across 2026-08-17 and 2026-08-18:

```text
2026-08-17:
TruDiagnostic
→ DEXA
→ VO₂ max

2026-08-18:
Bod Pod
```

Preserved physical artifacts include the August DEXA, VO₂, and Bod Pod files under [`snapshots/2026-08/`](./snapshots/2026-08/).

Physical source preservation is complete.

The TruDiagnostic sample was collected on 2026-08-17, but provider-result evidence remains pending. Therefore Model Error 043 remains open/unscored.

Physical or behavioral evidence does not substitute for the registered primary TruDiagnostic domain.

---

# Phase Governance

Current phase:

```text
Phase 2 — Load Integration
```

Current operating substate:

```text
Consolidation / lock-in observation
```

Phase 2D:

```text
undeclared
```

Current evidence includes repeated load compatibility, ambient/trait-like execution, automatic grip/movement organization, natural portability, preserved function across autonomic variability, and reduced operator-management cost.

These observations can accumulate as transition evidence without independently declaring Phase 2D.

See:

- [`PHASE_MAP.md`](./PHASE_MAP.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

---

# Verification and CI

The repository contains two read-only validators:

```text
tools/validate_repository.py
tools/validate_machine_readable.py
```

The machine-readable validator checks:

- required headers
- unique dates/session/event IDs
- daily continuity
- numeric syntax
- controlled vocabularies
- source-reference grammar
- historical duration-expression grammar
- event interval validity
- related model-error references
- cross-file date relationships

GitHub Actions runs both validators on:

```text
push to main
pull request
```

Workflow:

`.github/workflows/validate.yml`

Guide:

[`tools/README.md`](./tools/README.md)

A validator pass confirms implemented checks, not biological causality or clinical validity.

---

# AI Assistance

AI/LLM systems may assist with source-backed structuring, drafting, calculation, analysis, audit review, validator code, and formally governed prediction generation.

AI is **not** a source-evidence class.

It may not invent missing values, fabricate provenance, override stronger source evidence, rewrite registered predictions after outcome access, or strengthen claims beyond the evidence.

Disclosure:

[`docs/AI_ASSISTANCE.md`](./docs/AI_ASSISTANCE.md)

---

# Release and DOI

The Zenodo DOI currently points to the archived:

```text
v1.0.0
```

release.

The live `main` branch contains later unreleased documentation, data, methodology, prediction, report, validation, and snapshot updates.

Citation:

Hughett, C. D. (2026). *Daniel Longitudinal Study (v1.0.0)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20815612

See:

- [`VERSIONING.md`](./VERSIONING.md)
- [`CITATION.cff`](./CITATION.cff)

---

# Scope

This repository documents one subject under defined protocol constraints and incomplete environmental control.

It does not establish:

- population-level causality
- clinical efficacy
- generalized intervention guidance
- protocol safety for other people
- universal device/assay accuracy
- certainty from prediction accuracy

Repeated measurement, source preservation, explicit correction, validation, and governance improve interpretability.

They do not remove the limitations of an observational N-of-1 system.

---

# Repository Map

- Current state → [`LATEST.md`](./LATEST.md)
- Full index → [`INDEX.md`](./INDEX.md)
- Data coverage → [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- Data dictionary → [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
- Machine-readable schema → [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)
- Private-source provenance → [`data/source_provenance/`](./data/source_provenance/)
- Source exports → [`data/source_exports/`](./data/source_exports/)
- Weekly reports → [`reports/`](./reports/)
- Snapshots → [`snapshots/`](./snapshots/)
- Model error → [`data/model_error/`](./data/model_error/)
- Governance → [`GOVERNANCE.md`](./GOVERNANCE.md)
- Methodology → [`METHODOLOGY_AND_CONTROLS.md`](./METHODOLOGY_AND_CONTROLS.md)
- Verification → [`VERIFICATION.md`](./VERIFICATION.md)
- Validation tools → [`tools/README.md`](./tools/README.md)
- AI disclosure → [`docs/AI_ASSISTANCE.md`](./docs/AI_ASSISTANCE.md)
- Audits → [`docs/audits/`](./docs/audits/)
- Changelog → [`CHANGELOG.md`](./CHANGELOG.md)

---

_Public longitudinal archive initiated 2026._
