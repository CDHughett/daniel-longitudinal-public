# Dataset Overview

*Longitudinal observational archive documenting biological, behavioral, recovery, and training-system behavior under defined protocol constraints and incomplete environmental control.*

---

## Overview

The **Daniel Longitudinal Study** is a continuous single-subject observational archive documenting biological, behavioral, recovery, and training-system responses across time.

The archive operates under:

- defined protocol constraints
- repeated measurement
- structured reporting
- ordinary-life environmental variability
- incomplete experimental control
- explicit source and correction governance

The primary objective is to preserve durable evidence and enable bounded retrospective interpretation of long-term system behavior.

This is not a controlled clinical trial and does not establish population-level causality, clinical efficacy, generalized intervention guidance, or complete control of external variables.

---

## Current Public Machine-Readable Core

The September 2026 structured-data expansion created an aligned daily/session/event layer from governed source material.

| Dataset | Unit of observation | Current public coverage |
|---|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | one row per represented day | 203 continuous rows, 2026-02-09 through 2026-08-30 |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | one canonical governed wake-date row | 203 continuous rows, 2026-02-09 through 2026-08-30 |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | one row per training/session block | 325 sessions, 2026-02-09 through 2026-08-30 |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | one row per bounded contextual event | 42 events, current event coverage through 2026-08-29 |

The three newer datasets are curated public extracts derived primarily from private `Daniel_Dataset_v1.0`–`v1.28` source states and governed contemporaneous evidence.

They are not raw provider exports.

Their schema contract is:

[`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)

Private-source file identity is documented, when the exact retained file was available for hashing, in:

[`data/source_provenance/daniel_dataset_private_manifest.csv`](./data/source_provenance/daniel_dataset_private_manifest.csv)

---

## Study Scope

| Attribute | Description |
|---|---|
| Subject count | 1 |
| Observation type | Longitudinal, observational |
| Archive model | Artifact-first, version-controlled system |
| Primary domains | Training exposure, recovery signals, biological measurement, behavioral execution, contextual perturbation |
| Environmental control | Defined protocol constraints with incomplete real-world control |
| Interpretation posture | Retrospective, bounded, and subject-specific |
| Prediction layer | Explicitly registered and evaluated through the model-error system |
| AI assistance | Permitted as a maintenance/analysis aid under explicit source and governance constraints |

AI-assistance disclosure:

[`docs/AI_ASSISTANCE.md`](./docs/AI_ASSISTANCE.md)

---

## Observation Flow

```text
Protocol Inputs
      +
Training Exposure
      +
Recovery Environment
      +
Behavioral Execution
      +
Ordinary-Life Variability
      ↓
Physiological and Functional Response
      ↓
Source Evidence
      ↓
Curated Structured Data
      ↓
Retrospective Interpretation
      ↓
Prediction Evaluation
      ↓
Model Correction
```

Artifacts and contemporaneous records are preserved before final interpretation whenever practical.

Structured datasets organize the evidence; they do not outrank stronger verified source artifacts when a source-backed discrepancy is established.

---

## Evidence Layers

### Source Artifacts

Provider reports, testing outputs, direct device exports, screenshots, and other primary evidence are preserved under `/snapshots` and `/data/source_exports`.

Some source artifacts are provider-generated reports rather than raw instrument data. Source identity, date, preparation condition, and interpretation limits therefore remain important.

### Curated Structured Data

Machine-readable archive-defined datasets live under `/data`.

The current core includes:

- daily biomarkers
- sleep
- training blocks
- context events
- biomarker snapshots
- bloodwork
- epigenetic outputs
- model-error records
- calibration trackers

Curated data may include source-transcribed measurements, subjective fields, contextual classifications, correction notes, and archive-defined identifiers.

### Reports

Weekly and event-oriented reports preserve bounded retrospective interpretation after evidence accumulates.

Active reports may collect observations, but unfinished windows remain provisional.

### Model-Error Layer

`data/model_error` preserves prediction registration, later outcome evidence, error direction, status, and calibration review.

Wrong predictions remain visible.

### Governance and Audits

Governance documents define correction, prediction, phase, missingness, and interpretation boundaries. Audits review continuity and integrity without rewriting the evidence being audited.

---

## Machine-Readable Field Semantics

The newer daily/training/event datasets distinguish:

- **measurement / source-transcribed fields**
- **subjective fields**
- **contextual / classified fields**
- **provenance fields**

The distinction is defined in the schema rather than inferred by data consumers.

A notable v1 compatibility rule applies to `training_blocks_v1.csv`:

`duration_min` is a source-preserving **duration expression**, not universally numeric. Scalar values may be treated as minutes; ranges and compound historical expressions must not be coerced to a point estimate without a documented transformation.

A cleaner numeric/raw duration split is reserved for a future schema migration.

---

## Source Provenance

Public row-level provenance is retained in `source_ref`.

Current canonical private-source syntax is documented in:

[`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)

All 325 current training rows now use the canonical `private_workbook:` / `private_pdf:` source-reference grammar. Earlier `wb:v...` / `pdf:v...` aliases remain visible in Git history only.

File-level private-source SHA-256 values are registered only when the exact private file was available. Missing hashes are left missing rather than reconstructed.

---

## Direct Provider Exports

The RingConn acquisition package under:

[`data/source_exports/ringconn/2026-07-21/`](./data/source_exports/ringconn/2026-07-21/)

remains a separate source-preservation layer.

Direct exports preserve provider-defined bytes, fields, timestamps, aggregation, and missingness. They do not silently overwrite curated public datasets.

---

## Data Quality and Correction

Known data-quality questions are documented in:

[`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

Coverage boundaries are documented in:

[`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)

A source-backed correction must remain narrow, traceable, and review downstream derived values without rewriting unrelated historical evidence.

---

## Validation

Two read-only validators are maintained:

```text
tools/validate_repository.py
tools/validate_machine_readable.py
```

The machine-readable validator checks the new daily/training/event layer for:

- headers
- unique identifiers
- date continuity and bounds
- numeric syntax
- controlled vocabularies
- duration-expression semantics
- source-reference syntax
- event interval validity
- model-error cross-references
- cross-file date relationships

GitHub Actions runs both validators on pushes to `main` and on pull requests.

Validation confirms implemented structural/semantic checks; it does not establish biological causality or clinical validity.

---

## Interpretation and Environmental Boundary

Observation occurs under ordinary life rather than laboratory isolation.

Potential influences include travel, schedule displacement, household workload, social context, equipment availability, intake variation, hydration, sleep environment, environmental exposure, device/provider behavior, and unmeasured factors.

The archive therefore prioritizes:

- repeated evidence over isolated results
- visible uncertainty
- explicit missingness
- source traceability
- natural rather than manufactured perturbations
- retrospective interpretation
- prediction accountability
- correction over narrative defense

---

## Current Limitations

Important limitations include:

- single-subject design
- absence of randomized controls
- incomplete environmental control
- concurrent exposures and interventions
- consumer wearable limitations
- low-frequency biological testing
- partial manual/source-backed transcription
- incomplete public availability of some private source material
- provider and algorithm variability
- no continuous structured nutrition or supplement-adherence dataset
- incomplete environmental measurement
- v1 historical training-duration expressions that are not uniformly numeric
- potential operator and observer bias

The newer machine-readable layer improves analyzability but does not remove these limitations.

---

## Intended Use

The repository is published to:

- document long-term system behavior
- preserve primary artifacts and source provenance
- support reproducible longitudinal analysis
- audit predictions against observed outcomes
- expose uncertainty and model error
- preserve protocol/governance evolution
- provide a reference architecture for governed single-subject observation

The appropriate framing is a governed longitudinal case archive and methodological research object, not a universal intervention program.

---

## Archive Principle

**Artifacts first.  
Structured evidence second.  
Interpretation third.  
Narrative last.**
