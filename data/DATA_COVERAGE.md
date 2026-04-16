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

## Temporal Coverage

- Continuous observation: 2026-W01 → present  
- Partial historical backfill: 2025 selected epochs  
- Snapshot-based anchor points define longitudinal structure  

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
