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

- Weekly report for 2026-W17 finalized to document the completed observation window under restored baseline conditions and stabilized load integration.

- Weekly report for 2026-W18 initialized to maintain forward archive continuity under the active observation window model.

- Appended sleep dataset entries for 2026-W17 (2026-04-27 through 2026-05-03):
  - direct crossover from source dataset  
  - no inferred or reconstructed values included  
  - schema consistency verified against longitudinal structure  

- Introduced model error tracking layer for structured comparison of predictions vs observed outcomes.
  - Added `/data/model_error/` directory
  - Added primary dataset `model_error_gap_v1.csv`
  - Added rolling summary file `udi_tracker.csv`
  - Added `data/model_error/README.md` for layer orientation and handling rules
  - Added `methodology/prediction_evaluation.md` defining evaluation rules for point, range, and state predictions

- Introduced first forward-locked, pre-registered predictions in model error layer:
  - bodyweight stability prediction (5-day binary window)
  - pull-up repeatability prediction (5-session binary window)
  - marked with `calibration_state = pre`
  - no post-hoc adjustment or exemption permitted

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

- Introduced internal week indexing convention:
  - added `docs/WEEK_INDEXING.md`
  - clarified reporting week offset relative to calendar weeks
  - linked indexing convention from `LATEST.md` and `INDEX.md`

---

### Changed

- `LATEST.md` executive system dashboard updated to reflect:
  - W17 closed observation window
  - W18 active observation window
  - transition from disruption-resilience → repeatability under control
  - alignment with current consolidation-phase signal
  - explicit week indexing clarification retained

- `CHANGELOG.md` restructured:
  - converted to active rolling window model
  - moved historical entries to `docs/archive/CHANGELOG_ARCHIVE.md`

- `INDEX.md` updated:
  - added navigation reference to week indexing convention

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

- `data/model_error/README.md` updated to clarify `calibration_state` semantics:
  - explicitly distinguishes `pre` (forward-locked) vs `post` (subject-calibrated)
  - resolves ambiguity between post-calibration and post-outcome interpretation
  - improves external legibility of evaluation layer

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
- W17 formally closed
- W18 initialized as active observation window
- Repository considered structurally consistent for external read-through
