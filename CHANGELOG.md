# Changelog

All notable changes to the Daniel Longitudinal Study public archive  
are documented in this file.

This changelog reflects **recent structural and repository updates only**.

Historical entries are preserved in:  
[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

---

## Scope

This changelog records:

- repository artifacts and structural updates  
- dataset modifications  
- methodology changes  
- archive integrity adjustments  

Biological interpretation belongs in `/reports`.

---

## [Unreleased]

### Added

- Weekly report for 2026-W16 finalized to document the completed observation window under high-density execution and non-standard environmental disruption.
- Weekly report for 2026-W17 initialized to maintain forward archive continuity under the active observation window model.

- Added missing sleep dataset entry for 2026-03-22 using direct wearable-derived values.

- Updated sleep dataset to include current observation-window entries:
  - appended rows using verified sheet-based values
  - corrected prior invalid append (removed inferred data)
  - preserved schema integrity and historical continuity

- Added sleep log entries for 2026-04-13 through 2026-04-19:
  - exact crossover from source dataset
  - aligned with the canonical longitudinal sleep schema
  - no inferred or backfilled values included

- Introduced model error tracking layer for structured comparison of predictions vs observed outcomes.
  - Added `/data/model_error/` directory
  - Added primary dataset `model_error_gap_v1.csv`
  - Added rolling summary file `udi_tracker.csv`
  - Added `data/model_error/README.md` for layer orientation and handling rules
  - Added `methodology/prediction_evaluation.md` defining evaluation rules for point, range, and state predictions

- Integrated February 2026 biomarker snapshot artifacts:
  - DEXA scan  
  - BodPod composition  
  - TruAge and Advanced TruAge reports  
  - TruHealth system report  

- Introduced `biomarker_snapshot.csv` for monthly fused biomarker aggregation.

- Introduced `epigenetic_longitudinal.csv` for biological aging time-series tracking.

- Added `SHA256 checksums.txt` files across snapshot directories to establish binary artifact verification and improve auditability.

- Added `VERIFICATION.md` guide for external checksum validation of snapshot artifacts.

- Introduced `DATA_COVERAGE.md` to define dataset scope, completeness, and known limitations.

- Introduced `docs/methodology/subject_baseline_context.md` to define pre-observation context and interpretation boundaries.

- Linked subject baseline context across methodology and coverage documentation.

---

### Changed

- `LATEST.md` executive system dashboard updated to reflect:
  - W16 closed observation window
  - W17 active observation window
  - removal of multi-week historical stacking
  - observed stability under repeated exposure and environmental disruption
  - consolidation-first posture
  - alignment with strict current-state observational standard

- `DATA_DICTIONARY.md` expanded to support biomarker and epigenetic fields introduced during the February 2026 snapshot expansion.

- `sleep_longitudinal_v1.csv` refined and aligned:
  - unified prior sleep records into a single longitudinal structure
  - corrected column alignment inconsistencies
  - removed stale references to superseded sleep-file naming
  - preserved historical rows without reinterpretation
  - standardized schema for forward compatibility
  - extended observations through the current window

- `udi_tracker.csv` updated to reflect mixed post-calibration closure blocks and to withhold UDI where mixed prediction types reduce comparability.

- Model error layer documentation aligned with current methodology and open-prediction handling.

- PDFs moved out of Git LFS and re-tracked as standard Git objects to restore full artifact integrity and prevent pointer file corruption.

- Enforced strict separation between forward-logged and reconstructed prediction records:
  - moved reconstructed dataset to `data/model_error/historical/`
  - removed reconstructed records from evaluative pathways
  - clarified non-equivalence between forward and retrospective entries

- Updated prediction review pipeline to reflect correct dataset paths and enforce evaluation boundaries.

- Reclassified early UDI snapshot as historical exploratory artifact.

- Completed temporal index layer:
  - replaced `EPOCH_MAP` with `EPOCH_INDEX` across repository
  - aligned all epoch records to index structure
  - improved chronological navigation and external readability

- Corrected repository-wide path inconsistencies and reference mismatches.

---

### Changed — Structural Alignment

- `INDEX.md` updated to reflect current archive structure after document pruning.

- Repository structure simplified:
  - removed redundant conceptual layers
  - consolidated phase logic into `PHASE_MAP.md` and `STATE_TRANSITIONS.md`
  - reduced top-level document duplication to improve navigation clarity

---

### Removed

- `PHASE_INDEX.md`
- `ROADMAP.md`
- `SYSTEM_CONSTRAINTS.md`
- `EXPERIMENT_REGISTRY_PUBLIC.md`
- `PHASE_2_READINESS_CHECKLIST.md`
- `TRANSITION_MAP.md`
- `DISCLAIMER.md`

These removals reduced redundant framing and consolidated durable logic into governance, methodology, reports, and phase criteria documents.

---

### Refined

- Repository language tightened to preserve a conservative, artifact-first tone.

- Separation reinforced between:
  - snapshot artifacts  
  - reports  
  - longitudinal datasets  
  - model error layer  
  - methodology layer  

- Archive posture clarified around disturbance handling.

- `GOVERNANCE.md` updated to clarify artifact-bound interpretation constraints.

- `README.md` refined for consistency with governance and methodology layers.

---

### Notes

- Detailed marker-level TruHealth expansion remains intentionally limited at this stage.
- UDI remains selectively applied where methodological comparability is sufficient.
- Legacy trajectory prediction entries may remain open until a formal evaluation standard is defined.
- Current architecture prioritizes clarity, separation of concerns, and auditability over premature abstraction.
- Portions of repository development and commit activity were performed via a mobile-based workflow.

---

## Audit Status

- Saturday audit pass completed
- Sunday weekly closeout completed
- W16 formally closed
- W17 initialized as active observation window
- Repository considered structurally consistent for external read-through
