# Calibration Events Log

This file records dated changes in prediction framing, model calibration state, or model-version shifts relevant to the Model Error Layer.

---

## Event 001 — Provisional Subject Calibration Boundary

**Date:** 2026-03-21  
**Type:** Provisional transition from population-calibrated interpretation toward subject-specific interpretation  
**Domains affected:** HRV, sleep, performance, recovery  
**Model state:** pre → post  

**Description:**  
By this point, forward-looking model interpretations had begun shifting away from general population caution assumptions and toward subject-specific pattern recognition based on repeated observed performance, recovery behavior, and stabilization signals.

**Notes:**  
This boundary is currently treated as the primary working anchor for post-calibration interpretation and may be refined later if an earlier or more precise boundary becomes defensible from dated primary records.

---

## Event 002 — May 2026 Snapshot Closure Integration

**Date:** 2026-06-01  
**Type:** Post-calibration closure update following May 2026 artifact completion  
**Domains affected:** epigenetic aging, body composition, VO2 max, recovery, performance, UDI governance  
**Model state:** post  

**Description:**  
The May 2026 snapshot artifact set was completed with DEXA, BodPod/COSMED, VO2 summary, TruAge, Advanced TruAge, and TruHealth reports. Model error records 032 through 038 were closed or incorporated into the active closure inventory, including epigenetic aging, DEXA body composition, VO2 max, push-up repeatability, and recovery-stability predictions.

**Notes:**  
At the time of this calibration event, the May closure block materially expanded the post-calibration prediction ledger. UDI remained intentionally withheld because the closure inventory contained mixed prediction classes, including point, range, trajectory, and binary-state outcomes, without an approved stratified reporting methodology.

Subsequent UDI v1.1 governance updates introduced stratified reporting, published eligible point and range UDI metrics, and retained composite UDI withholding under documented release criteria.

Directional counts are retained in `udi_by_type_tracker.csv` for transparency.

---

## Event 003 — July–August Forward Prediction Block Initialization

**Date:** 2026-06-27  
**Type:** Post-DOI forward-prediction block initialization  
**Domains affected:** recovery capacity, ambient execution, biological snapshot translation, protocol governance  
**Model state:** post  

**Description:**  
Following DOI issuance, `v1.0.0` archival publication, post-DOI observer-pathway cleanup, and closure of the May 2026 / W24 prediction block, model error records 041 through 044 were opened as an active forward-prediction block for the July–August / August 2026 observation window.

This block extends the post-calibration prediction ledger beyond artifact closure and into prospective observation of recovery capacity, ambient execution plateau behavior, August biological snapshot translation, and protocol-governance preservation through the next full snapshot cycle.

**Notes:**  
Records 041 through 044 were forward-logged for their defined observation windows.

This event does not represent a structural change to prediction methodology. It records a calibration-context transition from post-DOI archive stabilization into the next active prospective observation block.

UDI handling remains governed by UDI v1.1. Closed eligible records may be incorporated into stratified UDI reporting only after closure criteria are met. Composite UDI remains intentionally withheld under documented release criteria.

---

## Event 004 — August 2026 Biological Translation Adjudication

**Date:** 2026-09-10  
**Type:** Post-outcome adjudication of a prospectively registered primary trajectory prediction  
**Domains affected:** biological translation, trajectory concordance, source reconciliation  
**Registration provenance:** record 043 remains `calibration_state=pre`

**Description:**  
After the August TruDiagnostic source reports were archived and their structured values were integrated, record 043 was evaluated against the criteria frozen in `methodology/open_prediction_evaluation_plan_041_044.md`.

The preregistered overall-improvement rule was not met. DunedinPACE improved from 0.79 to 0.77, OMICm age delta moved slightly more favorable from -3.7 to -3.9 years but remained inside the registered stable band, and SymphonyAge increased from 37.8 to 46.1 years. The required two-of-three core-anchor improvement threshold was therefore not met. All 11 directly comparable system/organ ages were materially adverse under the registered threshold, and only 11 of 30 combined supporting metrics were stable or improved, below the required 60%.

Record 043 closed as `overall_improvement_not_met` with error direction `over`, meaning the model overestimated the breadth of August biological improvement under the locked evaluation rule.

**Notes:**  
The record remains prospectively registered in provenance; closure does not change `calibration_state=pre` to `post`.

Primary trajectory concordance updates from:

```text
2/3 = 0.67
```

to:

```text
2/4 = 0.50
```

Point and range UDI remain unchanged. State concordance remains unchanged. Secondary trajectory records remain excluded from the primary trajectory-concordance denominator.

The August provider-header metadata difference is governed separately by `data/source_provenance/2026-08-trudiagnostic-reconciliation.md` and does not alter the biological values used for record 043.

This event records calibration outcome only. It does not establish a causal explanation for the August provider-output changes, modify the physical protocol, or declare a phase transition.
