# Daniel Longitudinal Study
*A structured, real-time human system dataset*

This repository tracks how a single human system adapts over time under controlled inputs.

It contains:
- longitudinal biomarker and sleep data
- weekly system state reports
- a prediction vs. observed outcome review layer
- structured methodology, governance, and constraints

---

## What makes this different

This is not a blog, protocol, or theory thread.

Everything here is:
- measured
- logged
- versioned
- auditable

No forward claims.  
Only recorded system behavior and retrospective interpretation.

---

## Current State

→ [`LATEST.md`](./LATEST.md)

This is the fastest way to understand what the system is doing right now.

---

## Start Here

- [`LATEST.md`](./LATEST.md) — current system state  
- [`docs/START_HERE.md`](./docs/START_HERE.md) — guided repository orientation  
- [`snapshots`](./snapshots/) — primary artifacts and source evidence  
- [`reports`](./reports/) — structured retrospective interpretation  
- [`data`](./data/) — structured longitudinal datasets  

---

## System Flow

~~~text
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
Reports + Snapshots
(retrospective interpretation + source evidence)
      ↓
Model Error Layer
(predicted vs. observed outcome review)
~~~

---

## What you're looking at

A live longitudinal system:

Inputs → Biological response → Measurement → Interpretation → Iteration

---

**Archive Type:** Longitudinal dataset  
**Subject Model:** n = 1 observational system  
**Observation Mode:** Artifact-first, retrospective interpretation  
**Observation Window:** 2025–present  
**Public Archive:** Active (2026–present)

![Dataset Status](https://img.shields.io/badge/status-active_observation-blue)
![Observation Type](https://img.shields.io/badge/model-longitudinal_archive-purple)
![Subjects](https://img.shields.io/badge/subjects-n%3D1-lightgrey)
![Artifact Model](https://img.shields.io/badge/data-artifact_first-green)
![Archive Version](https://img.shields.io/badge/archive-v0.1-black)
[![Release](https://img.shields.io/badge/release-v0.1-111111)](https://github.com/CDHughett/daniel-longitudinal-public/releases/tag/v0.1)

---

## External Observers

If you're evaluating the system structure directly:

→ [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md)

---

## Dataset Orientation

This repository documents a longitudinal observation of a human performance system operating under defined constraints.

The archive preserves continuity across:

- body composition measurements  
- training architecture evolution  
- phase-based system progression  
- governance and constraint frameworks  
- biomarker and system health snapshots (where publicly included)  
- prediction vs. observed outcome tracking (auxiliary review layer)  

**Note:** Some biomarker data (e.g., detailed bloodwork) may be referenced in reports but not included in the public archive.

This is not a motivational archive.  
It is a structured longitudinal dataset.

This archive includes SHA256 verification for binary artifacts within snapshot directories, supporting public auditability of recorded states.

---

## Why This Matters

Most human performance data is fragmented, short-term, or anecdotal.

This archive documents a continuous system under consistent conditions, enabling:

- observation of long-term adaptation patterns  
- evaluation of stability vs. intensity strategies  
- traceable relationships between inputs and biological response  

---

## Archive Posture

This repository is maintained as a longitudinal observational archive.

Interpretation remains intentionally conservative:

- artifacts take precedence over narrative  
- observations remain provisional  
- conclusions require repeated evidence across time  

This archive documents one subject under constrained conditions.  
No claims extend beyond the recorded system.

---

## Current Phase Context

**Phase 2 — Load Integration**

Current focus:

- maintaining aerobic base capacity  
- reintroducing strength under recovery constraints  
- monitoring stability under repeated exposure  

Key tracking areas:

- strength exposure within recovery limits  
- neuromuscular density development  
- preservation of aerobic capacity  
- biomarker stability  

Phase transitions are declared retrospectively following sustained system stability.

→ [`PHASE_MAP.md`](./PHASE_MAP.md)

---

## Phase Architecture

~~~text
Phase 0 | ██████████ | Completed
Phase 1 | ██████████ | Completed
Phase 2 | ████░░░░░░ | Load Integration (Active)
Phase 3 | ░░░░░░░░░░ | Locked
~~~

System progression is artifact-verified and versioned.

---

## Repository Structure

~~~text
Root
│
├── snapshots/                        # Primary measurement artifacts (source of truth)
├── reports/                          # Structured retrospective interpretation
├── dashboards/                       # Derived visualization surfaces
│
├── data/                             # Structured datasets (longitudinal + model error)
│   └── model_error/                  # Prediction vs outcome review layer
│
├── experiments/                      # Intervention summaries
├── schemas/                          # Naming conventions and definitions
├── methodology/                      # Core methodological rules and constraints
├── docs/                             # Guided orientation and extended methodology
│
├── README.md
├── INDEX.md
├── LATEST.md
├── CHANGELOG.md
│
├── GOVERNANCE.md
├── STRUCTURAL_PRINCIPLES.md
├── PHASE_DECLARATION_CRITERIA.md
├── RISK_MANAGEMENT.md
├── RECOVERY_MONITORING_FRAMEWORK.md
│
├── DATA_DICTIONARY.md
├── MEASUREMENT_SOURCES.md
├── METHODOLOGY_AND_CONTROLS.md
└── ASSUMPTIONS_AND_BOUNDARIES.md
~~~

---

## Architectural Layers

~~~text
Raw Logs
→ Snapshots (immutable evidence)
→ Reports (retrospective interpretation)
→ Datasets (structured tracking layers)
→ Governance (constraints and boundaries)
~~~

Each layer increases abstraction while remaining artifact-bound.

---

## Methodology

See:

[`METHODOLOGY_AND_CONTROLS.md`](./METHODOLOGY_AND_CONTROLS.md)  
[`methodology/prediction_evaluation.md`](./methodology/prediction_evaluation.md)  
[`docs/START_HERE.md`](./docs/START_HERE.md)

These documents define:

- measurement rules  
- stabilization criteria  
- interpretation constraints  
- system boundaries  
- prediction evaluation rules (post-outcome only)  

---

## Model Error Layer

This repository includes a structured review layer for tracking the difference between predicted and observed outcomes.

This layer operates alongside the primary dataset and does not replace artifact-first observation.

### Purpose

- preserve prediction records in structured form  
- compare predicted vs. observed outcomes after closure  
- quantify directional and magnitude error  
- review error patterns across eligible closed records  

### Context

Most performance models rely on population-based assumptions.

This layer preserves a narrow record of how those assumptions compare with observed outcomes in a single-subject archive under controlled conditions.

### Status

Active auxiliary review layer.  
Evaluation methodology is defined; interpretation remains retrospective and conservative.

### Reference

- [`data/model_error/model_error_gap_v1.csv`](./data/model_error/model_error_gap_v1.csv)  
- [`data/model_error/README.md`](./data/model_error/README.md)  
- [`methodology/prediction_evaluation.md`](./methodology/prediction_evaluation.md)  

---

## Governance

All structural interpretation follows defined criteria:

- phase declarations are retrospective  
- load increases are recovery-gated  
- claims require artifact confirmation  
- system constraints govern progression  

Reference:

- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)  
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)  
- [`RISK_MANAGEMENT.md`](./RISK_MANAGEMENT.md)  
- [`RECOVERY_MONITORING_FRAMEWORK.md`](./RECOVERY_MONITORING_FRAMEWORK.md)  

---

## Scope

This repository documents a single-subject observational system.

It does not constitute medical, training, or performance advice.  
All observations remain context-bound.

---

## Citation

~~~text
Hughett, C. D. (2026).
Daniel Longitudinal Study — Structured Human Performance Dataset.
GitHub Repository.
https://github.com/CDHughett/daniel-longitudinal-public
~~~

Machine-readable metadata:

`CITATION.cff`

---

## License

This repository and all included materials are licensed under:

**Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**

Full license text available in `LICENSE.md`.

---

## Intent

This dataset exists to demonstrate:

- structured adaptation  
- conservative escalation  
- artifact-verified governance  
- durability across time  

All conclusions remain bound to recorded evidence.

---

## Navigation

- Current state → [`LATEST.md`](./LATEST.md)  
- Guided orientation → [`docs/START_HERE.md`](./docs/START_HERE.md)  
- Weekly reports → [`reports`](./reports/)  
- Artifact history → [`snapshots`](./snapshots/)  
- Epoch tracking → [`EPOCH_MAP.md`](./EPOCH_MAP.md)  
- Snapshot log → [`SNAPSHOT_LOG.md`](./SNAPSHOT_LOG.md)  
- Versioning → [`VERSIONING.md`](./VERSIONING.md)  

---

_Public longitudinal archive initiated 2026._
