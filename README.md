# Daniel Longitudinal Study

**A governed N-of-1 longitudinal research archive for studying how training, recovery, physiology, behavior, and context interact over time.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20815611.svg)](https://doi.org/10.5281/zenodo.20815611)
[![Repository validation](https://github.com/CDHughett/daniel-longitudinal-public/actions/workflows/validate.yml/badge.svg)](https://github.com/CDHughett/daniel-longitudinal-public/actions/workflows/validate.yml)

**Current published release:** `v1.1.0` — 2026-09-14  
**Version DOI:** `10.5281/zenodo.22759132`  
**All-versions DOI:** `10.5281/zenodo.20815611`  
**Frozen release commit:** `92126e1cc882c3822d9e03b30b11cfc1d30b4fbb`

The Daniel Longitudinal Study follows one human system through repeated measurement, machine-readable data, contemporaneous observation, source-preserved testing, registered predictions, retrospective interpretation, correction history, and explicit archive governance.

The aim is not to prove a universal intervention. It is to preserve an inspectable record of **what was measured, what was predicted, what happened, what changed, and what was corrected**.

> **Scope:** single-subject, longitudinal, observational. This is not a clinical trial, coaching product, or generalized intervention protocol.

---

## Start here

| Goal | Entry point |
|---|---|
| Understand the project quickly | [`docs/START_HERE.md`](./docs/START_HERE.md) |
| See the current live state | [`LATEST.md`](./LATEST.md) |
| Inspect structured coverage | [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md) |
| Understand the dataset as a research object | [`DATASET_OVERVIEW.md`](./DATASET_OVERVIEW.md) |
| Audit the archive skeptically | [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md) |
| Inspect prediction accountability | [`data/model_error/`](./data/model_error/) |
| Inspect source provenance | [`data/source_provenance/`](./data/source_provenance/) |
| Inspect testing artifacts | [`snapshots/`](./snapshots/) |
| Reproduce mechanical checks | [`VERIFICATION.md`](./VERIFICATION.md) |
| Read v1.1.0 release notes | [`docs/releases/v1.1.0.md`](./docs/releases/v1.1.0.md) |
| Read publication reconciliation | [`docs/audits/2026-09-14-v1.1.0-publication-reconciliation.md`](./docs/audits/2026-09-14-v1.1.0-publication-reconciliation.md) |
| Navigate the repository | [`INDEX.md`](./INDEX.md) |

---

# Current archive state

| Domain | Current state |
|---|---|
| Phase | **Phase 2 — Load Integration** |
| Operating substate | **Consolidation / reserve-replication observation** |
| Active weekly window | **2026-W38** |
| Most recent closed window | **2026-W37** |
| Installed training architecture | **B1 + Load Integration** |
| Open model-error records | **none in protected block 041–046** |
| Record 043 | **closed / not supported — `overall_improvement_not_met` / over** |
| August snapshot | **source artifacts archived, reconciled, structured, checksum-protected** |
| Formal Phase 2D declaration | **none** |

Current-state anchors retained for repository validation:

```text
Active weekly window:
2026-W38

Most recent closed window:
2026-W37
```

Week 38 preserves the unchanged B1 + Load Integration architecture while observing whether the preliminary reserve exposed at W37 closeout is reproducible. One favorable capacity probe is not treated as a progression authorization, short-window wearable variability remains distinct from demonstrated function, and Phase 2D remains undeclared.

Authoritative current detail: [`LATEST.md`](./LATEST.md)

---

# Machine-readable core

Current public structured coverage through 2026-09-20:

| Dataset | Unit | Coverage |
|---|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | one row per represented day | 224 continuous rows through 2026-09-20 |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | one governed wake-date row | 224 continuous rows through 2026-09-20 |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | one row per completed session/block | 362 rows through 2026-09-20 |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | one bounded context event | 49 rows through 2026-09-20 |

Training is session-indexed: a represented day with zero completed training sessions does not require a synthetic training row.

The daily/training/event layers are curated public extracts derived primarily from governed private `Daniel_Dataset_v1.x` source states. They are **not raw provider exports**.

Schema and provenance:

- [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)
- [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
- [`data/source_provenance/`](./data/source_provenance/)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

---

# Evidence architecture

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

The repository is designed to preserve disagreement as well as agreement: favorable observations can coexist with failed predictions; recovery telemetry can diverge from demonstrated function; corrections can repair source transcription without repairing the narrative.

---

# Source hierarchy and correction

When records conflict, interpretation generally prioritizes:

1. verified primary source artifact
2. direct provider/device export
3. contemporaneous structured transcription
4. contemporaneous collection note
5. closed retrospective report
6. later evidence-grounded synthesis
7. unsupported memory

Silent alteration, outcome-driven rewriting, unsupported reconstruction, and retrospective prediction revision are prohibited.

Source-backed corrections must remain narrow, traceable, and reviewed for downstream effects.

---

# August 2026 coordinated snapshot

Collection occurred across 2026-08-17 and 2026-08-18:

```text
2026-08-17
TruDiagnostic → DEXA → VO₂ max

2026-08-18
Bod Pod
```

Preserved public artifacts under [`snapshots/2026-08/`](./snapshots/2026-08/) include DEXA, VO₂, Bod Pod/COSMED, TruAge, Advanced TruAge, and TruHealth outputs. Seven protected August artifacts are registered in the folder SHA-256 manifest.

The contemporaneous repository record controls the canonical TruDiagnostic sample event: **2026-08-17 at 05:37 local**. Provider-displayed administrative metadata remain preserved but do not overwrite that collection record. See [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](./data/source_provenance/2026-08-trudiagnostic-reconciliation.md).

Integrated snapshot values are represented in:

- [`data/biomarker_snapshot.csv`](./data/biomarker_snapshot.csv)
- [`data/epigenetic_longitudinal.csv`](./data/epigenetic_longitudinal.csv)

---

# Prediction accountability

Recent protected records:

| Record | Domain | Outcome |
|---|---|---|
| 041 | recovery_capacity | supported |
| 042 | ambient_execution | not supported — continued adaptation |
| 043 | biological_translation | **not supported — `overall_improvement_not_met` / over** |
| 044 | protocol_governance | not supported — narrow snapshot-directed deviation |
| 045 | autonomic_reconvergence | supported |
| 046 | autonomic_unload_reload | failed_autonomic_recompression |

Record 043 remains fixed under its preregistered biological scoring boundary. Later favorable training or behavioral evidence does not reopen or rescue the outcome.

Full adjudication: [`data/model_error/record_043_closure.md`](./data/model_error/record_043_closure.md)

UDI is an error/calibration framework, not a biological score. See [`docs/methodology/UDI_framework_v1.md`](./docs/methodology/UDI_framework_v1.md).

---

# Known limitations

This archive does not establish population-level causality, clinical efficacy, generalized intervention guidance, protocol safety for other people, or universal device/assay accuracy.

Known bounded data-quality restrictions remain visible rather than silently repaired. Examples include historical sleep-field reconciliation notes and DQ-011 for the recorded 2026-09-08 resting-heart-rate value pending source verification.

Some historical private source states also lack exact retained immutable files for SHA-256 registration. Those hashes remain explicitly unavailable rather than reconstructed.

See [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md) and [`methodology/anonymization.md`](./methodology/anonymization.md).

---

# Verification

Read-only validators:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
python tools/validate_august_snapshot.py
python tools/validate_coherence.py
```

GitHub Actions runs repository validation on pushes to `main` and pull requests.

A validation PASS confirms implemented mechanical/governance checks. It does not establish biological causality, clinical validity, device accuracy, or correct scientific interpretation.

See [`VERIFICATION.md`](./VERIFICATION.md).

---

# AI assistance

AI/LLM systems may assist with source-backed structuring, drafting, calculation, analysis, audit review, validator code, and formally governed prediction generation.

AI is **not** a source-evidence class and may not invent observations, fabricate provenance, override stronger source evidence, or rewrite registered predictions after outcome access.

Disclosure: [`docs/AI_ASSISTANCE.md`](./docs/AI_ASSISTANCE.md)

---

# v1.1.0 publication identity

The externally published v1.1.0 release is fixed to:

```text
GitHub tag:              v1.1.0
Frozen release commit:  92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
Release archive:         daniel-longitudinal-study-v1.1.0-92126e1cc882.zip
Release archive SHA-256: f7bad6d466c28d85fc263128083fe37d9039cb116cff67fb1c8a35482d5ce0a9
Zenodo version DOI:      10.5281/zenodo.22759132
Zenodo all-versions DOI: 10.5281/zenodo.20815611
```

The GitHub `v1.1.0` tag remains fixed to the Batch 5A frozen commit. Post-publication DOI reconciliation occurs only on later `main`; it does not move the tag or mutate the published release archive.

The Zenodo lineage contains an earlier immutable record labeled `v1.1.0` with DOI `10.5281/zenodo.22759127`. The finalized version-specific DOI for the frozen Batch 5A package is `10.5281/zenodo.22759132`. The all-versions DOI `10.5281/zenodo.20815611` remains the stable cross-version entry point.

Release notes: [`docs/releases/v1.1.0.md`](./docs/releases/v1.1.0.md)  
Publication reconciliation: [`docs/audits/2026-09-14-v1.1.0-publication-reconciliation.md`](./docs/audits/2026-09-14-v1.1.0-publication-reconciliation.md)  
Versioning rules: [`VERSIONING.md`](./VERSIONING.md)  
Citation metadata: [`CITATION.cff`](./CITATION.cff)  
License: [`LICENSE.md`](./LICENSE.md)

---

# Repository map

- Current state → [`LATEST.md`](./LATEST.md)
- Start guide → [`docs/START_HERE.md`](./docs/START_HERE.md)
- Observer route → [`docs/OBSERVER_QUICKSTART.md`](./docs/OBSERVER_QUICKSTART.md)
- Dataset overview → [`DATASET_OVERVIEW.md`](./DATASET_OVERVIEW.md)
- Full index → [`INDEX.md`](./INDEX.md)
- Data coverage → [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- Data dictionary → [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
- Private-source provenance → [`data/source_provenance/`](./data/source_provenance/)
- Source exports → [`data/source_exports/`](./data/source_exports/)
- Weekly reports → [`reports/`](./reports/)
- Snapshots → [`snapshots/`](./snapshots/)
- Model error → [`data/model_error/`](./data/model_error/)
- Governance → [`GOVERNANCE.md`](./GOVERNANCE.md)
- Methodology → [`METHODOLOGY_AND_CONTROLS.md`](./METHODOLOGY_AND_CONTROLS.md)
- Verification → [`VERIFICATION.md`](./VERIFICATION.md)
- Audits → [`docs/audits/`](./docs/audits/)
- Changelog → [`CHANGELOG.md`](./CHANGELOG.md)

---

The pre-v1.1.0 long-form README is preserved byte-for-byte at [`docs/archive/README_PRE_V1.1.0.txt`](./docs/archive/README_PRE_V1.1.0.txt).

_Public longitudinal archive initiated 2026._
