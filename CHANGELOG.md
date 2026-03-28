# Changelog

All notable changes to the Daniel Longitudinal Study public archive
are documented in this file.

The format follows a simplified Keep-a-Changelog structure adapted
for a longitudinal dataset archive.

This changelog records **repository artifacts and structural updates**.  
Biological interpretation belongs in `/reports`.

---

## [Unreleased]

### Added

- Weekly report for **2026-W11** documenting continued consolidation under repeated exposure conditions.
- Initialized **2026-W12** report to maintain forward archive continuity.

- Introduced **model error tracking layer** for structured comparison of AI predictions vs observed outcomes.
  - Added `/data/model_error/` directory with primary schema `model_error_gap_v1.csv`
  - Added `/docs/methodology/UDI_framework_v1.md` defining Unobstructed Delta Index (UDI)
  - Added `/docs/methodology/annotation_protocol.md` for prediction capture and data integrity rules
  - Added calibration event logging structure for tracking model interpretation shifts

- Added supporting README documentation for new measurement layer:
  - `data/model_error/README.md`
  - `docs/methodology/README.md`

- Established forward capture protocol for logging model predictions at time of generation

- Closed early THC transition predictions in UDI dataset (018, 020, 023) based on observed alignment with predicted nervous system and cognitive responses
- Added GI instability event (025) with attribution to pre-training fueling timing mismatch rather than systemic failure
- Added performance resilience signal (026) capturing maintained execution capacity under sympathetic activation and GI disturbance

---

### Added (Biomarker Expansion — Feb 2026)

- Integrated **February 2026 biomarker snapshot artifacts**:
  - DEXA scan  
  - BodPod composition  
  - TruAge and Advanced TruAge reports  
  - TruHealth system report  

- Introduced `biomarker_snapshot.csv`
  - Monthly fused biomarker layer combining body composition, epigenetic age, and system health domains  

- Introduced `epigenetic_longitudinal.csv`
  - Time-series tracking of biological aging metrics (OMICm age, DunedinPACE, SYMPHONY age)  

- Expanded `DATA_DICTIONARY.md`
  - Added definitions for all new biomarker and epigenetic variables  

---

### Updated

- **LATEST.md** executive system dashboard updated to reflect:
  - active THC removal window
  - observed sympathetic activation and increased behavioral awareness
  - transient GI instability with corrected attribution (timing mismatch)
  - confirmed performance stability under regulatory disturbance

- Bodyweight observation band updated to reflect current range (~221–233 lb)

- Snapshot layer expanded from single-domain (body composition) to **multi-domain biological state representation**

---

### Refined

- README.md updated to reduce onboarding friction and improve initial repository orientation:
  - Added “What This Is / Why It Exists / What Makes It Different” entry block
  - Introduced guided “Start Here” navigation
  - Added “Why This Matters” context layer
  - Clarified practical interpretation of Phase 2 (Load Integration)
  - Improved readability for first-time external readers

- Reinforced separation between:
  - snapshot layer (derived, fused state)  
  - longitudinal datasets (granular, time-series tracking)  

---

### Observations

- Training architecture remains stable under Phase 2 load integration monitoring
- Recovery signals remain compatible with repeated exposure structure
- System demonstrates performance stability under transient regulatory disturbance
- GI instability event classified as input-timing mismatch, not systemic degradation
- Archive continuity maintained through ongoing weekly report initialization

---

### Notes

- Detailed TruHealth marker-level data intentionally not expanded into longitudinal dataset at this stage  
- Current architecture prioritizes clarity, separation of concerns, and auditability  

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
- Archive established as a **continuous longitudinal observation system**
- Interpretation constrained to artifact-confirmed observations

---

## Versioning Notes

This repository does not follow a traditional software release cycle.

Version tags represent **structural milestones in the archive**, not performance outcomes.

Most changes remain in the **Unreleased** section until a major structural transition occurs.
