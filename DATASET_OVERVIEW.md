# Dataset Overview

*Longitudinal observational archive documenting biological, behavioral, recovery, and training-system behavior under defined protocol constraints and incomplete environmental control.*

---

## Overview

The **Daniel Longitudinal Study** is a continuous single-subject observational archive documenting biological, behavioral, recovery, and training-system responses across time.

The archive follows one subject through extended observation windows under:

- defined protocol constraints
- repeated measurement
- structured reporting
- ordinary-life environmental variability
- incomplete experimental control

The primary objective is to preserve artifact continuity and enable bounded retrospective interpretation of long-term system behavior.

This is not a controlled clinical trial.

Travel, schedule variation, household demands, environmental exposure, social context, equipment access, intake variation, and other real-world conditions may affect individual observation windows. These factors are documented when known but are not comprehensively controlled or measured.

---

## Dataset Scope

| Attribute | Description |
|---|---|
| Subject count | 1 |
| Observation type | Longitudinal, observational |
| Archive model | Artifact-first, version-controlled system |
| Primary domains | Training exposure, recovery signals, biological measurement, behavioral execution |
| Environmental control | Defined protocol constraints with incomplete real-world control |
| Interpretation posture | Retrospective, bounded, and subject-specific |
| Prediction layer | Explicitly registered and evaluated through the model-error system |

The archive preserves chronological continuity so system behavior can be examined across repeated measurement windows, protocol states, perturbations, and recovery periods.

The dataset does not establish:

- population-level causality
- clinical efficacy
- generalized intervention guidance
- complete control of external variables
- attribution of an outcome to a single input without supporting evidence

---

## Observation Flow

The archive follows a governed observational pipeline:

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
Artifact and Data Capture
      ↓
Structured Dataset Integration
      ↓
Retrospective Interpretation
      ↓
Prediction Evaluation and Model Correction
```

Artifacts and contemporaneous records are preserved before final interpretation whenever practical.

Interpretive documents may organize and contextualize evidence, but they do not replace the underlying source material.

---

## Dataset Structure

The archive is organized into several complementary evidence layers.

### Snapshots

Time-bounded source and measurement artifacts.

Examples include:

- DEXA reports
- BodPod outputs
- epigenetic reports
- biomarker panels
- bloodwork
- physiological testing outputs
- supporting images and verification files

Location:

[`/snapshots`](./snapshots/)

Snapshots represent primary archived evidence for specific measurement windows.

Some snapshot artifacts are provider-generated reports rather than unprocessed raw instrument data. Their source, date, and interpretation limits should therefore remain visible.

---

### Structured Data

Machine-readable longitudinal datasets derived from source artifacts, wearable records, and governed transcription.

Examples include:

- longitudinal sleep data
- biomarker snapshots
- bloodwork data
- epigenetic outputs
- model-error records
- calibration trackers

Location:

[`/data`](./data/)

Structured data improves continuity, comparison, and analysis but remains subordinate to verified source artifacts when a conflict is identified.

Known data-quality questions are documented in:

[`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

Coverage and missingness are documented in:

[`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)

---

### Reports

Structured interpretive summaries produced after evidence accumulates.

Reports may include:

- weekly observation summaries
- phase closeouts
- snapshot interpretations
- perturbation and recovery synthesis
- unresolved questions
- evidence relevant to open predictions

Location:

[`/reports`](./reports/)

Reports interpret preserved evidence but do not replace it.

Weekly reports may also contain contemporaneous collection notes. Final weekly interpretation remains retrospective and is completed at closeout.

---

### Model-Error Layer

A governed prediction-versus-observed-outcome review system.

Location:

[`/data/model_error`](./data/model_error/)

This layer preserves:

- predictions registered before outcomes are known
- applicable observation windows
- observed outcomes
- direction and magnitude of error
- closure status
- model-correction evidence

Forward predictions are permitted only when explicitly registered, time-bounded, preserved without hindsight revision, and evaluated after the relevant window closes.

The model-error layer is a calibration instrument rather than evidence of certainty.

---

### Milestone Artifacts

Contextual or symbolic artifacts associated with notable events in the archive timeline.

Examples include:

- challenge coins
- recognition tokens
- contextual markers tied to external observation

Location:

[`/snapshots/milestones`](./snapshots/milestones/)

Milestone artifacts provide historical context.

They are not treated as biological evidence unless a separate record establishes a direct evidentiary role.

---

## Evidence Hierarchy

When sources disagree, interpretation should generally prioritize:

1. verified primary artifacts
2. direct device exports
3. contemporaneous structured records
4. contemporaneous collection notes
5. weekly retrospective reports
6. later synthesis grounded in preserved evidence

A later narrative should not create an observation that was not otherwise recorded.

Structured values should not be corrected through inference when the original source remains unresolved.

---

## Observation Philosophy

The archive follows a conservative observational posture:

- artifacts precede interpretation
- biological interpretation remains retrospective
- observations remain provisional
- conclusions require repeated evidence across time
- uncertainty and missingness remain visible
- real-world constraints are distinguished from behavioral failure
- protocol changes require explicit governance
- predictions remain separate from retrospective interpretation
- failed predictions are preserved as model-correction evidence

Because the dataset represents one subject under incomplete environmental control, findings should not be generalized without independent evidence.

---

## Environmental Context

The archive operates under real-world rather than laboratory conditions.

Known contextual variables may include:

- travel
- schedule disruption
- household workload
- social and administrative demands
- equipment availability
- altered sleep environment
- hydration and sodium variation
- meal timing
- GI timing
- transient illness or exposure
- environmental temperature and air quality
- incomplete scale or measurement access

These factors are documented when they are known and relevant.

Their absence from a report does not establish that all external variables were controlled.

---

## Phase Model

The longitudinal system is organized into operational phases.

Phase definitions are documented in:

[`PHASE_MAP.md`](./PHASE_MAP.md)

Phases describe retrospectively identified system states and protocol conditions.

They are not declared solely from:

- a single favorable measurement
- one strong training session
- prediction accuracy
- subjective confidence
- elapsed time

Phase transitions require the evidence and governance standards defined in:

[`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

---

## Data Integrity

Artifact and dataset continuity are supported through:

- chronological storage
- version-controlled history
- explicit governance constraints
- source-linked structured data
- documented correction procedures
- checksum verification for applicable binary artifacts
- audit records
- visible data-quality notes

Dataset and structural changes are documented in:

[`CHANGELOG.md`](./CHANGELOG.md)

Audit records are preserved in:

[`docs/audits`](./docs/audits/)

---

## Limitations

Important limitations include:

- single-subject design
- incomplete environmental control
- partial reliance on consumer wearable estimates
- evolving measurement availability
- manually transcribed fields in some datasets
- irregular low-frequency biological testing
- incomplete structured training exports
- potential changes in device software or algorithms
- inability to isolate many concurrent variables
- incomplete public inclusion of some referenced health data

These limitations narrow interpretation but do not eliminate the value of repeated, traceable longitudinal observation.

---

## Intended Use

This repository is published to:

- document long-term system behavior
- preserve primary artifacts and structured data
- support retrospective longitudinal analysis
- audit predictions against observed outcomes
- expose uncertainty and model error
- maintain an inspectable record of protocol evolution
- provide a reference architecture for governed single-subject observation

The archive may inform future longitudinal research design, but it should not be treated as a validated intervention program or direct clinical guide.

---

## Archive Principle

**Artifacts first.  
Structured evidence second.  
Interpretation third.  
Narrative last.**
