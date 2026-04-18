# DATA COVERAGE

This document defines the scope, completeness, and limitations of datasets currently included in the archive.

It exists to clarify:
- what is tracked
- what is partially tracked
- what is not tracked
- where gaps may exist

This is a **coverage declaration**, not an interpretation layer.

---

## Coverage Summary

| Domain | Coverage Status | Notes |
|---|---|---|
| Training Exposure | Complete (current phase) | Daily structure captured via reports |
| Sleep | High (recent), Partial (historical) | Wearable-derived; earlier gaps present |
| Recovery Signals (HRV, RHR) | High | Continuous tracking during active observation windows |
| Body Composition | Snapshot-based | DEXA, BodPod at discrete intervals |
| Biomarkers (blood panels) | Snapshot-based | Periodic lab captures only |
| Epigenetic / Aging | Emerging | TruAge / TruHealth integrated; longitudinal build in progress |
| VO₂ / Performance Testing | Partial | Event-based, not continuous |
| Nutrition | Not explicitly tracked | Only indirect via outcome signals |
| Supplementation | Not systematically tracked | Referenced contextually in reports |
| Environmental Factors | Partial | Not fully controlled or logged |
| Model Error / Prediction | Active (forward) | Clean dataset maintained; historical reconstruction separated |

---

## Dataset Locations

| Dataset | Path |
|---|---|
| Sleep longitudinal | `data/sleep_longitudinal_v1.csv` |
| Biomarker snapshot | `data/biomarker_snapshot.csv` |
| Epigenetic longitudinal | `data/epigenetic_longitudinal.csv` |
| Model error (primary) | `data/model_error/model_error_gap_v1.csv` |
| Model error (historical) | `data/model_error/historical/` |

---

## Baseline Context Reference

Interpretation of biomarker and epigenetic data should consider documented pre-observation conditions:

`docs/methodology/subject_baseline_context.md`

This file defines known starting conditions but does not assign causal interpretation to observed values.

---

## Temporal Coverage

The dataset operates under a continuous observational model, with staged public data exposure.

### Observation Continuity

- Continuous observation: 2026-W01 → present  

This reflects the start of stable training exposure, recovery control, and behavioral execution.

Not all early observations are represented as structured public artifacts.

---

### Structured Archive Coverage

- Structured reporting layer: 2026-W06 → present  

From this point forward, reports, snapshots, and supporting datasets are consistently represented in the archive.

---

### Dataset-Specific Coverage

Individual datasets begin when stable measurement conditions were achieved.

Examples:

- Sleep longitudinal dataset: begins 2026-02-09  
- Weekly reports: begin 2026-W06  
- Snapshot artifacts: increase in frequency over time  

Datasets are introduced only when signal stability is sufficient for reliable inclusion.

---

### Notes

- Absence of early structured data does not indicate absence of observation  
- Data layers are added progressively as stability improves  
- The archive prioritizes **data integrity over backfilled completeness**

---

## Known Gaps

- No continuous nutrition logging  
- No continuous VO₂ tracking  
- No full environmental standardization  
- Early prediction dataset contains reconstructed entries (segregated)  

---

## Interpretation Boundary

Coverage limitations must be considered when evaluating:

- performance trends  
- recovery dynamics  
- model calibration quality  

No conclusions should be drawn outside the bounds of available data.

---

## Status

Coverage is expanding over time.

Future additions will be documented here as new datasets are introduced.
