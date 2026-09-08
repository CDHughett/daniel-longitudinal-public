# Daniel Longitudinal Study

**A governed N-of-1 longitudinal research archive for studying how training, recovery, physiology, behavior, and context interact over time.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20815612.svg)](https://zenodo.org/doi/10.5281/zenodo.20815612)
[![Repository validation](https://github.com/CDHughett/daniel-longitudinal-public/actions/workflows/validate.yml/badge.svg)](https://github.com/CDHughett/daniel-longitudinal-public/actions/workflows/validate.yml)

**Archived release:** [Zenodo v1.0.0 — DOI 10.5281/zenodo.20815612](https://zenodo.org/doi/10.5281/zenodo.20815612)

The Daniel Longitudinal Study follows one human system through repeated measurement, machine-readable data, contemporaneous observation, source-preserved testing, registered predictions, retrospective interpretation, correction history, and explicit archive governance.

The central aim is not to prove a universal intervention. It is to build a durable record in which **what was measured, what was predicted, what happened, what changed, and what was corrected remain inspectable over time**.

> **Scope:** single-subject, longitudinal, observational. This is not a clinical trial, coaching product, or generalized intervention protocol.

---

## At a Glance

Current public structured coverage through **2026-09-06**:

| Layer | Current public state |
|---|---:|
| Daily biomarkers | **210 continuous daily rows** |
| Canonical sleep | **210 continuous daily rows** |
| Training exposure | **339 session/block rows** |
| Context events | **44 bounded events** |
| Weekly reporting | Continuous from **2026-W06** |
| August physical snapshot | **DEXA + VO₂ + Bod Pod archived** |
| Open recent prediction | **043 — provider evidence pending** |

Authoritative live counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md).

### What makes this archive different

- **Evidence is preserved beneath interpretation.** Higher-level narratives do not replace source artifacts or structured rows.
- **Wrong predictions stay visible.** Fixed scoring windows remain fixed, and later favorable evidence does not retrospectively rescue a miss.
- **Corrections are traceable.** Source-backed discrepancies are corrected narrowly without silently rewriting unrelated historical evidence.
- **Measured, subjective, contextual, and provenance fields are separated.** Machine readability does not erase evidence class.
- **Private-source provenance is represented without publishing private workbooks.** Exact retained files are hashed when available; unavailable hashes remain explicitly missing.
- **The repository validates itself mechanically.** Read-only validators run locally and in GitHub Actions.

---

## Choose Your Entry Point

| If you want to... | Start here |
|---|---|
| Understand the project in a few minutes | [`docs/START_HERE.md`](./docs/START_HERE.md) |
| See the current live state | [`LATEST.md`](./LATEST.md) |
| Inspect the structured datasets | [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md) |
| Understand the dataset as a research object | [`DATASET_OVERVIEW.md`](./DATASET_OVERVIEW.md) |
| Audit the archive skeptically | [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) |
| Inspect prediction accountability | [`data/model_error/`](./data/model_error/) |
| Inspect source provenance | [`data/source_provenance/`](./data/source_provenance/) |
| Inspect testing artifacts | [`snapshots/`](./snapshots/) |
| Reproduce mechanical checks | [`VERIFICATION.md`](./VERIFICATION.md) |
| Navigate everything | [`INDEX.md`](./INDEX.md) |

For recurring terminology, see [`docs/CONCEPTS.md`](./docs/CONCEPTS.md).

---

# Current Archive State

| Domain | Current state |
|---|---|
| Phase | **Phase 2 — Load Integration** |
| Operating substate | **Consolidation / lock-in observation** |
| Active weekly window | **2026-W36** |
| Most recent closed window | **2026-W35** |
| Installed training architecture | **B1 + Load Integration** |
| Open model-error record | **043 — biological translation** |
| August TruDiagnostic result | **provider result pending** |
| Formal Phase 2D declaration | **none** |

Current-state anchors retained for repository validation:

```text
Active weekly window:
2026-W36

Most recent closed window:
2026-W35
```

The recent operating posture is intentionally conservative: ordinary B1 + Load Integration continues while recovery variability, lower bodyweight/intake context, behavioral economy, and natural portability are observed without forcing progression or manufacturing perturbations.

Current details: [`LATEST.md`](./LATEST.md)

---

# Machine-Readable Core

The public archive now supports aligned daily, sleep, training, and event analysis.

| Dataset | Unit of observation | Current coverage |
|---|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | one row per represented day | 210 rows through 2026-09-06 |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | one canonical governed wake-date row | 210 rows through 2026-09-06 |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | one row per training/session block | 339 rows through 2026-09-06 |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | one row per bounded contextual event | 44 events through 2026-09-03 |

The daily/training/event datasets are curated public extracts derived primarily from governed private `Daniel_Dataset_v1.x` source states. They are **not raw provider exports**.

Schema contract: [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)  
Data dictionary: [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)  
Private-source provenance: [`data/source_provenance/`](./data/source_provenance/)

## Evidence classes

The machine-readable layer explicitly distinguishes:

- **measurement / source-transcribed** fields
- **subjective** fields
- **contextual / classified** fields
- **provenance** fields

Structured subjective data remain subjective. Context classification does not establish causality.

### Historical duration compatibility

`training_blocks_v1.csv` preserves historical training architecture rather than inventing false precision. Its v1 `duration_min` field may contain:

- scalar minutes
- bounded ranges
- compound historical duration expressions

Only scalar values are directly numeric without a separately documented transformation. See [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md).

---

# Evidence Architecture

The repository deliberately separates layers that are often collapsed together:

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

The archive is designed to preserve disagreement as well as agreement. Examples include:

- strong function alongside less-favorable recovery telemetry
- favorable observations alongside failed predictions
- broad governance discipline alongside a narrow governance failure
- later recovery that does not retrospectively alter a failed fixed scoring window
- increasing behavioral automaticity without premature phase declaration

---

# Data, Source Preservation, and Provenance

Primary structured/public layers include:

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

Coverage, field semantics, and limitations:

- [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)
- [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
- [`MEASUREMENT_SOURCES.md`](./MEASUREMENT_SOURCES.md)

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

This distinction is important: **a correction is allowed to repair the archive; it is not allowed to repair the story.**

---

# Prediction Accountability

The model-error layer exists to evaluate prediction/model calibration rather than demonstrate foresight.

Recent prospective block:

| Record | Domain | Status | Outcome |
|---|---|---|---|
| 041 | recovery_capacity | Closed | supported |
| 042 | ambient_execution | Closed | not supported — continued adaptation |
| 043 | biological_translation | **Open** | TruDiagnostic provider result pending |
| 044 | protocol_governance | Closed | not supported — narrow snapshot-directed deviation |
| 045 | autonomic_reconvergence | Closed | supported |
| 046 | autonomic_unload_reload | Closed | failed_autonomic_recompression |

Wrong predictions remain visible. Fixed evidence windows remain fixed. Original registered prediction narratives remain distinguishable from later closure language.

Model-error layer: [`data/model_error/`](./data/model_error/)  
Prediction criteria: [`docs/methodology/valid_prediction_criteria.md`](./docs/methodology/valid_prediction_criteria.md)

## UDI

UDI canonically means **Unobstructed Delta Index**.

The current framework separates eligible magnitude error from state/trajectory concordance:

```text
UDI_point
UDI_range
State_concordance
Trajectory_concordance
```

Composite UDI remains withheld under predefined sample-size criteria. UDI is a model-error framework, **not a biological score**.

Methodology: [`docs/methodology/UDI_framework_v1.md`](./docs/methodology/UDI_framework_v1.md)

## Future model-error schema

The historical v1 field `calibration_state` carries legacy semantic debt because prospective registration and subject-specific model calibration are separate concepts.

Protected recent records 041–046 retain `calibration_state=pre` as historical registration provenance. Future design separates:

```text
registration_status
model_calibration_scope
```

without rewriting current v1 records.

See [`docs/methodology/model_error_schema_v2.md`](./docs/methodology/model_error_schema_v2.md).

---

# August 2026 Snapshot

Physical collection was completed across 2026-08-17 and 2026-08-18:

```text
2026-08-17
TruDiagnostic → DEXA → VO₂ max

2026-08-18
Bod Pod
```

Preserved DEXA, VO₂, and Bod Pod artifacts are available under [`snapshots/2026-08/`](./snapshots/2026-08/).

The TruDiagnostic sample was collected, but the provider-result evidence required for Model Error 043 remains pending. The archive therefore keeps 043 open/unscored rather than substituting physical or behavioral evidence for its registered primary domain.

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

Formal Phase 2D declaration:

```text
none
```

Current evidence includes repeated load compatibility, increasingly low-salience execution, automatic grip/movement organization, natural portability, preserved function across autonomic variability, and reduced operator-management cost.

Those observations can accumulate as transition evidence without independently declaring a phase transition.

See:

- [`PHASE_MAP.md`](./PHASE_MAP.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

---

# Verification and Reproducibility

Two read-only validators are maintained:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
```

The core validator checks repository structure, Markdown integrity, CSV structure, checksums, canonical sleep continuity, weekly-report continuity, protected model-error state, release metadata, and source-export preservation.

The machine-readable validator checks the daily/training/event schema contract, including identifiers, dates, vocabularies, source references, duration semantics, event intervals, and cross-file relationships.

GitHub Actions runs both validators on:

```text
push to main
pull request
```

Workflow: [`.github/workflows/validate.yml`](./.github/workflows/validate.yml)  
Verification guide: [`VERIFICATION.md`](./VERIFICATION.md)  
Validation tools: [`tools/README.md`](./tools/README.md)

A validation PASS confirms the implemented mechanical/governance checks. It does not establish biological causality, clinical validity, device accuracy, or correct scientific interpretation.

---

# AI Assistance

AI/LLM systems may assist with source-backed structuring, drafting, calculation, analysis, audit review, validator code, and formally governed prediction generation.

AI is **not** a source-evidence class.

It may not invent missing observations, fabricate provenance, override stronger source evidence, rewrite registered predictions after outcome access, or strengthen claims beyond the evidence.

Disclosure: [`docs/AI_ASSISTANCE.md`](./docs/AI_ASSISTANCE.md)

---

# Scope and Limitations

This repository documents one subject under defined protocol constraints and incomplete environmental control.

It does **not** establish:

- population-level causality
- clinical efficacy
- generalized intervention guidance
- protocol safety for other people
- universal device/assay accuracy
- certainty from prediction accuracy

Additional limitations include provider-specific algorithms, consumer wearable measurement limits, manually transcribed fields, incomplete environmental control, concurrent inputs, and private source material that cannot always be independently inspected publicly.

Repeated measurement, source preservation, explicit correction, validation, and governance improve interpretability. They do not remove the limitations of an observational N-of-1 system.

---

# Release, Citation, and License

The Zenodo DOI currently points to the archived **v1.0.0** release.

**Zenodo archive:** [DOI 10.5281/zenodo.20815612](https://zenodo.org/doi/10.5281/zenodo.20815612)

The live `main` branch contains later unreleased documentation, data, methodology, prediction, report, validation, and snapshot updates.

**Citation**

Hughett, C. D. (2026). *Daniel Longitudinal Study (v1.0.0)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20815612

See:

- [`VERSIONING.md`](./VERSIONING.md)
- [`CITATION.cff`](./CITATION.cff)
- [`LICENSE.md`](./LICENSE.md)

---

# Repository Map

- Current state → [`LATEST.md`](./LATEST.md)
- First-contact guide → [`docs/START_HERE.md`](./docs/START_HERE.md)
- Technical observer route → [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md)
- Dataset overview → [`DATASET_OVERVIEW.md`](./DATASET_OVERVIEW.md)
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