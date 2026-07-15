# System Overview

Daniel Longitudinal Study  
Single-Subject Structured Adaptation System

---

## Purpose

This repository documents a governed longitudinal observation of one human system across:

- training
- recovery
- sleep
- nutrition
- behavior
- environmental variation
- biological measurement
- functional performance

The system operates under defined protocol constraints and incomplete real-world environmental control.

Its primary objective is the preservation of durable, interpretable signal across time rather than short-term performance optimization, staged presentation, or rapid intervention turnover.

The archive prioritizes:

- longitudinal consistency
- source-artifact preservation
- structured data continuity
- interpretive discipline
- explicit uncertainty
- prediction accountability
- model correction

Biological interpretation follows evidence collection and artifact verification.

Formally registered predictions may precede outcomes, but they remain isolated within the governed model-error layer and cannot substitute for later observation.

---

## System Model

The repository can be described as a constrained longitudinal observation and calibration pipeline.

```text
Protocol Inputs
│
├─ Training Structure
├─ Recovery Conditions
├─ Nutrition and Supplementation
├─ Sleep Opportunity
├─ Behavioral Execution
└─ Ordinary-Life Context
      ↓
Physiological and Functional Response
      ↓
Source Evidence
│
├─ Provider Reports
├─ Device Exports
├─ Testing Artifacts
├─ Screenshots
└─ Contemporaneous Observations
      ↓
Structured Data
      ↓
Retrospective Reports
      ↓
Phase and State Interpretation
      ↓
Registered Prediction Evaluation
      ↓
Model Correction
```

The system does not assume that every outcome can be attributed to a single input.

Observed changes may reflect interacting effects from:

- accumulated training exposure
- recovery conditions
- nutrition
- sleep
- travel
- schedule variability
- household or recreational activity
- measurement timing
- environmental context
- device or assay behavior
- unmeasured factors

Causal claims therefore remain limited.

---

## Observation Principles

The system operates under the following rules:

- biological interpretation remains retrospective and artifact-bound
- forward predictions are permitted only within the formally governed model-error layer
- predictions must be registered before the relevant outcome is known
- original prediction fields remain preserved
- phase declarations occur retrospectively
- source artifacts take priority over later summaries
- structured values remain subordinate to verified source evidence
- favorable and unfavorable outcomes remain visible
- missingness and uncertainty are not concealed
- source-backed corrections are permitted when traceable
- silent or outcome-driven rewriting is prohibited
- structural consistency is prioritized over novelty
- measurements should reflect normal operating conditions whenever practical
- protocol progression requires repeated evidence and governance support
- no intervention should be introduced merely to force a prediction, phase, or snapshot result

These principles are intended to preserve signal integrity across long observation horizons.

---

## Environmental-Control Boundary

The repository does not claim laboratory-grade environmental control.

Selected protocol inputs are stabilized where practical, including:

- B1 structure
- Load Integration structure
- recurring meal and supplementation patterns
- hydration
- sleep opportunity
- measurement methods
- reporting cadence
- data-entry procedures

Observation still occurs within ordinary life.

Relevant variability may include:

- travel
- schedule displacement
- family and social demands
- household workload
- recreational activity
- equipment access
- altered sleep environment
- hydration and sodium variation
- meal and GI timing
- illness or environmental exposure
- device or provider changes

The correct system description is:

> defined protocol constraints under incomplete environmental control

Known deviations are documented when they materially affect interpretation.

The absence of a recorded deviation does not establish that every external variable was controlled.

---

## Evidence Layers

The repository is organized into distinct but connected evidence layers.

### 1. Source Artifacts

Primary evidence may include:

- laboratory reports
- DEXA reports
- BodPod reports
- VO₂ testing outputs
- wearable exports
- screenshots
- provider-generated PDFs
- measurement images
- checksum-verified binary files

Source artifacts preserve the closest available representation of the original measurement.

---

### 2. Structured Datasets

Machine-readable datasets support:

- continuity checks
- longitudinal comparison
- derived metrics
- automated validation
- prediction evaluation
- reproducible analysis

Structured data may be created through:

- direct export
- source-backed transcription
- governed derivation

A structured value does not supersede a verified source artifact when a discrepancy is identified.

---

### 3. Contemporaneous Collection Notes

Collection notes preserve observations that may not be represented adequately by formal measurements.

Examples include:

- movement quality
- pain or mechanical signaling
- subjective morning state
- GI status
- travel or environmental context
- training-session characteristics
- perturbations
- divided-attention execution
- reasons for protocol decisions

These notes may later support retrospective interpretation or prediction evaluation.

---

### 4. Weekly Reports

Weekly reports provide bounded retrospective synthesis of the closed observation window.

They may summarize:

- training execution
- recovery behavior
- sleep
- bodyweight and fluid context
- constraints
- perturbations
- candidate evidence
- model-error relevance

Candidate evidence may be documented while a record remains open.

A weekly report may not:

- rewrite a prediction
- force an outcome
- create evidence that was not preserved
- declare a phase transition from one favorable event

---

### 5. Phase and State Interpretation

Phase documents describe retrospectively identified operating states.

Phase language summarizes patterns such as:

- repeatability
- recovery compatibility
- portability
- reduced operator overhead
- structural stability
- adaptive capacity

A phase transition requires repeated evidence and the criteria defined in:

[`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

---

### 6. Model-Error Layer

The model-error layer contains formally registered forward predictions and later outcome evaluations.

Its purpose is to test the quality of the operating model rather than defend prior expectations.

The layer preserves:

- prediction date
- prediction domain
- expected outcome
- observation window
- prediction type
- actual outcome
- direction and magnitude of error
- calibration consequences

Incorrect predictions remain part of the archive.

Open records must remain open when evidence is insufficient.

Current evaluation rules for records 041–044 are documented in:

[`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

---

### 7. Governance Layer

Governance defines:

- correction boundaries
- prediction rules
- protocol-change requirements
- phase-declaration standards
- missingness handling
- archival integrity
- release discipline
- scope limitations

Governance exists to constrain interpretation and intervention, not to rationalize a preferred outcome.

---

## Data Abstraction Flow

The repository’s abstraction flow is:

```text
Source Artifacts
      ↓
Structured Data
      ↓
Contemporaneous Context
      ↓
Weekly Retrospective Reports
      ↓
Phase and State Interpretation
      ↓
Prediction Evaluation
      ↓
Model Correction
      ↓
Future Governance
```

Each layer should remain traceable to the evidence beneath it.

Higher-level interpretation must not overwrite lower-level observations.

---

## Source and Correction Logic

When conflicting records exist, the preferred hierarchy is:

1. verified primary source artifact
2. direct provider or device export
3. contemporaneous structured transcription
4. contemporaneous collection note
5. weekly report
6. later evidence-grounded synthesis
7. unsupported memory

The archive prohibits:

- silent data alteration
- unsupported reconstruction
- outcome-driven correction
- deletion of unfavorable valid measurements
- prediction rewriting after the outcome is known

The archive permits source-backed correction when:

- the original source is available
- the affected field is identifiable
- the correction is narrow
- the prior repository state remains preserved through Git history
- the correction is documented
- applicable validation is rerun

Detailed correction rules are defined in:

- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

---

## Repository Artifact Map

### Current State and Navigation

**`LATEST.md`**  
Executive summary of the current system state.

**`INDEX.md`**  
Complete repository navigation map.

**`EPOCH_INDEX.md`**  
Temporal index across major observation periods.

**`SNAPSHOT_LOG.md`**  
Chronological index of major measurement artifacts.

---

### Governance and Methodology

**`GOVERNANCE.md`**  
Correction, prediction, protocol, phase, and archive-integrity rules.

**`METHODOLOGY_AND_CONTROLS.md`**  
Study design, stabilized inputs, limitations, evidence handling, and interpretation framework.

**`ASSUMPTIONS_AND_BOUNDARIES.md`**  
Declared scope limits and interpretive constraints.

**`STRUCTURAL_PRINCIPLES.md`**  
Repository organization and evidence-preservation principles.

**`PHASE_DECLARATION_CRITERIA.md`**  
Requirements for retrospective phase transitions.

**`VERSIONING.md`**  
Repository release and versioning rules.

---

### Data and Quality

**`DATASET_OVERVIEW.md`**  
Overview of evidence classes and structured datasets.

**`DATA_DICTIONARY.md`**  
Definitions for dataset fields and terminology.

**`MEASUREMENT_SOURCES.md`**  
Devices, providers, capture modes, and measurement context.

**`data/DATA_COVERAGE.md`**  
Coverage boundaries across structured, narrative, snapshot, and contextual evidence.

**`data/DATA_QUALITY_NOTES.md`**  
Known unresolved quality findings and correction status.

**`methodology/data-collection.md`**  
Collection, transcription, missingness, correction, and provenance procedures.

---

### Reports and Snapshots

**`/reports`**  
Weekly retrospective reports and reporting guidance.

**`/snapshots`**  
Primary biological, body-composition, performance, and source-artifact collections.

**`/data`**  
Canonical structured longitudinal datasets.

---

### Prediction and Calibration

**`data/model_error/model_error_gap_v1.csv`**  
Primary governed model-error register.

**`data/model_error/udi_by_type_tracker.csv`**  
Prediction-calibration summary by eligible record type.

**`methodology/prediction_evaluation.md`**  
General prediction-evaluation methodology.

**`methodology/open_prediction_evaluation_plan_041_044.md`**  
Prospective evaluation rules for the active July–August prediction block.

---

### Protocol and Experiment History

**`/protocols`**  
Active, historical, and superseded protocol documents.

**`/experiments`**  
Defined experiments, including active, completed, or paused states.

Presence in the repository does not by itself establish current exposure.

Each protocol or experiment should state its current status.

---

## System Boundaries

This repository documents a single-subject observational system.

It does not claim:

- population-level generalizability
- clinical efficacy
- complete causal identification
- laboratory-grade control
- universal intervention value
- medical guidance
- guaranteed outcomes
- that consumer-device measurements are definitive clinical measures
- that prediction accuracy establishes authority

Findings should be interpreted as evidence from one governed longitudinal case.

Causal inference remains limited by:

- single-subject design
- concurrent inputs
- environmental variability
- incomplete measurement
- device and assay limitations
- partial historical structure
- low-frequency biological snapshots
- operator and observer bias

Repeated measurement and transparent governance improve interpretability.

They do not remove these limitations.

---

## Operational Constraint

The system operates continuously.

The recurring operational sequence is:

```text
Execute
→ Observe
→ Preserve
→ Verify
→ Structure
→ Interpret
→ Evaluate
→ Correct the Model
```

Behavioral execution precedes retrospective interpretation.

Registered predictions may exist before outcomes, but their evaluation remains deferred until:

- the observation window closes
- evidence is sufficient
- source artifacts are verified
- comparability is reviewed

Normal repository operation should not be altered merely to produce a cleaner narrative or preferred prediction result.

---

## System Success Criteria

The system is not judged only by improvement.

A successful archive should demonstrate:

- continuity
- traceability
- visible uncertainty
- source preservation
- accurate correction
- durable execution
- governed protocol decisions
- preserved unfavorable outcomes
- prediction accountability
- calibrated interpretation
- readable long-term structure

A prediction failure may improve the system when it produces a better model.

An unfavorable measurement may strengthen the archive when it is preserved and interpreted honestly.

---

## Document Scope

This document describes the architecture and information flow of the system.

Operational details are governed by:

- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`METHODOLOGY_AND_CONTROLS.md`](./METHODOLOGY_AND_CONTROLS.md)
- [`ASSUMPTIONS_AND_BOUNDARIES.md`](./ASSUMPTIONS_AND_BOUNDARIES.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- [`methodology/prediction_evaluation.md`](./methodology/prediction_evaluation.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

---

## Version Note

This document was aligned on 2026-07-15 with the repository’s current:

- incomplete environmental-control boundary
- structured-data layer
- contemporaneous observation layer
- retrospective reporting model
- registered prediction layer
- model-correction process
- source-backed correction rules
- protocol and phase governance

The revision does not alter any source measurement, prediction record, protocol exposure, closed outcome, or phase status.
