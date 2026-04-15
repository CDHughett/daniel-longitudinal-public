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

**Note:** Some biomarker data may be referenced in reports but not included in the public archive.

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

→ [`PHASE_MAP.md`](./PHASE_MAP.md)

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

~~~text
Root
│
├── snapshots/
├── reports/
├── dashboards/
│
├── data/
│   └── model_error/
│
├── experiments/
├── schemas/
├── methodology/
├── docs/
│
├── README.md
├── INDEX.md
├── LATEST.md
├── CHANGELOG.md
~~~

---

## Governance

- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)  
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)  
- [`RISK_MANAGEMENT.md`](./RISK_MANAGEMENT.md)  

---

## Scope

Single-subject observational system.  
No external claims.

---

## License

CC BY-NC-ND 4.0

---

## Navigation

- Current state → [`LATEST.md`](./LATEST.md)  
- Guided orientation → [`docs/START_HERE.md`](./docs/START_HERE.md)  
- Index → [`INDEX.md`](./INDEX.md)  
- Epoch tracking → [`EPOCH_INDEX.md`](./EPOCH_INDEX.md)  
- Snapshot log → [`SNAPSHOT_LOG.md`](./SNAPSHOT_LOG.md)  
- Artifact history → [`snapshots`](./snapshots/)  
- Weekly reports → [`reports`](./reports/)  
- Versioning → [`VERSIONING.md`](./VERSIONING.md)  

---

_Public longitudinal archive initiated 2026._
