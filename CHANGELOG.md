# Changelog

All notable changes to the Daniel Longitudinal Study public archive
are documented in this file.

The format follows a simplified Keep-a-Changelog structure adapted
for a longitudinal dataset archive.

This changelog records **repository artifacts and structural updates**.  
Biological interpretation belongs in /reports.

---

## [Unreleased]

### Added

- Weekly report for 2026-W13 finalized to document the completed observation window under continued Phase 2 load integration conditions.
- Weekly report for 2026-W14 initialized to maintain forward archive continuity under the active observation window model.

- Introduced model error tracking layer for structured comparison of predictions vs observed outcomes.
  - Added /data/model_error/ directory
  - Added primary dataset model_error_gap_v1.csv
  - Added rolling summary file udi_tracker.csv
  - Added data/model_error/README.md for layer orientation and handling rules
  - Added methodology/prediction_evaluation.md defining evaluation rules for point, range, and state predictions

- Expanded prediction logging and closure coverage within the model error layer:
  - closed early THC transition predictions where sufficient evidence existed
  - added GI instability event with explicit attribution context
  - added performance-resilience closures under transient sympathetic / GI disturbance
  - preserved open predictions where observation windows remain active or methodologically incomplete

- Integrated February 2026 biomarker snapshot artifacts:
  - DEXA scan  
  - BodPod composition  
  - TruAge and Advanced TruAge reports  
  - TruHealth system report  

- Introduced biomarker_snapshot.csv
  - monthly fused biomarker layer combining body composition, epigenetic age, and system health domains  

- Introduced epigenetic_longitudinal.csv
  - time-series tracking of biological aging metrics (OMICm age, DunedinPACE, SYMPHONY age)  

- Added SHA256 checksums.txt files across snapshot directories to establish binary artifact verification and improve auditability.

- Added VERIFICATION.md guide for external checksum validation of snapshot artifacts.

---

### Changed

- LATEST.md executive system dashboard updated to reflect:
  - W13 closeout status
  - W14 active observation window
  - recent transient regulatory disturbance without structural drift
  - active model error and prediction-evaluation layers
  - current archive posture as consolidation-first rather than escalation-oriented

- DATA_DICTIONARY.md expanded to support biomarker and epigenetic fields introduced during the February 2026 snapshot expansion.

- sleep_signal_core_v1.csv refined:
  - removed static subjective field that was not changing
  - preserved only changing sleep / HRV signal columns
  - extended observations through the current window

- sleep_longitudinal_v1.csv introduced and aligned:
  - unified prior sleep records into a single longitudinal structure
  - corrected column alignment inconsistencies
  - preserved historical rows without reinterpretation
  - standardized schema for forward compatibility

- udi_tracker.csv updated to reflect mixed post-calibration closure blocks and to withhold UDI where mixed prediction types reduce comparability.

- Model error layer documentation aligned with current methodology and open-prediction handling.

- PDFs moved out of Git LFS and re-tracked as standard Git objects to restore full artifact integrity and prevent pointer file corruption.

---

### Refined

- Repository language further tightened to preserve a conservative, artifact-first tone under increasing structural complexity.

- Separation reinforced between:
  - snapshot artifacts (immutable evidence)  
  - reports (retrospective interpretation)  
  - longitudinal datasets (time-series tracking)  
  - model error layer (prediction vs observed outcome)  
  - methodology layer (evaluation rules and closure standards)  

- Archive posture clarified around disturbance handling:
  - transient regulatory disruption is logged without overstating systemic meaning
  - continuity and recovery compatibility remain primary interpretation anchors

---

### Notes

- Detailed marker-level TruHealth expansion remains intentionally limited at this stage.
- UDI remains selectively applied; mixed prediction-type blocks may be logged without a populated UDI value when methodological comparability is not yet sufficient.
- Legacy trajectory prediction entries may remain open in the model error dataset until a formal evaluation standard is defined for that prediction type.
- Current architecture prioritizes clarity, separation of concerns, and auditability over premature abstraction.
- Portions of repository development and commit activity were performed via a mobile-based workflow.
- As a result, some commits may appear more granular or repetitive than a typical desktop-based development pattern.
- Changes are grouped conceptually within this changelog to preserve clarity of intent.

---

## [0.1] – Initial Public Archive Release

### Added
- Initial public repository structure
- Core governance documentation
- System overview and archive orientation
- Initial reports and snapshot artifacts
- Measurement source documentation
- Data dictionary

---

### Governance
- Archive established as a continuous longitudinal observation system
- Interpretation constrained to artifact-confirmed observations

---

## Versioning Notes

This repository does not follow a traditional software release cycle.

Version tags represent structural milestones in the archive, not performance outcomes.

Most changes remain in the Unreleased section until a major structural transition occurs.
