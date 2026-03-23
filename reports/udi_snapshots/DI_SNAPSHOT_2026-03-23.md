# UDI Snapshot — 2026-03-23

Unobstructed Delta Index (UDI) snapshot based on early-stage model error tracking.

---

## Snapshot Scope

- **Window:** Initial reconstructed dataset  
- **Total prediction instances (n):** 9  
- **Completed comparisons:** 9  
- **Open predictions:** 0  

---

## Domain Coverage

| Domain        | Count |
|---------------|------|
| HRV           | 1    |
| Sleep         | 1    |
| Performance   | 4    |
| Recovery      | 3    |
| Body Comp     | 1    |

---

## Error Direction Summary

| Direction | Count | % |
|----------|------|----|
| Under    | 9    | 100% |
| Over     | 0    | 0% |
| Neutral  | 0    | 0% |

**Observation:**
Directional bias appears consistent toward underestimation.

---

## UDI (Early Approximation)

**UDI ≈ +25.5%**

Interpretation:
Observed outcomes exceeded population-model predictions across most measured domains in this early reconstructed dataset.

---

## Sample Rows (Representative)

| Domain      | Predicted | Actual | Error % | Direction |
|------------|----------|--------|--------|-----------|
| HRV        | 64       | 72     | +12.5% | Under     |
| Sleep      | 400      | 445    | +11.3% | Under     |
| Performance| 1.00     | 1.20   | +20.0% | Under     |

---

## Calibration Context

- **Calibration state:** Pre  
- **Calibration event recorded:** Not yet defined  

---

## Data Quality

| Flag Type      | Count |
|---------------|------|
| Primary        | 0    |
| Inferred       | 2    |
| Reconstructed  | 7    |

---

## Observations

- Model error appears directional rather than random  
- Direction: underestimation  
- Magnitude: moderate to high variability  

No conclusions drawn.  
Observation remains provisional.

---

## Notes

- Dataset is early-stage and reconstruction-heavy  
- Results are not generalized  
- Forward primary capture required for validation  

---

## Status

Initial UDI snapshot established.

Next step:
- begin primary prediction capture  
- increase dataset size  
- define calibration event
