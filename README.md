# Daniel Longitudinal Study
*A structured, real-time human system dataset*

This repository documents how a single human system adapts over time under controlled and repeatable conditions.

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

This is the fastest way to understand the system’s current observed state.

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
Snapshots (artifacts)
      ↓
Reports (retrospective interpretation)
      ↓
Model Error Layer
(predicted vs. observed outcome review)
~~~

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

**Data scope and limitations:**
→ [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)

**Note:** Some biomarker data may be referenced in reports but not included in the public archive.

SHA256 verification is provided for binary snapshot artifacts where applicable.

---

## External Observers

If you are evaluating the system structure directly:

→ [`docs/FOR_OBSERVERS.md`](./docs/FOR_OBSERVERS.md)

---

## Archive Posture

This repository is maintained as a longitudinal observational archive.

Interpretation remains intentionally constrained:

- artifacts take precedence over language  
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

- [`GOVERNANCE.md`](./GOVERNANCE.md)  
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
