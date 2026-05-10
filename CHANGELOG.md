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

- Weekly report for 2026-W18 finalized to document the completed observation window under stable Phase 2C consolidation and testing-window preservation.

- Weekly report for 2026-W19 initialized to maintain forward archive continuity during the May testing-window observation period.

- Appended sleep dataset entries for 2026-W18 (2026-05-04 through 2026-05-10):
  - direct crossover from source dataset
  - no inferred or reconstructed values included
  - schema consistency preserved against longitudinal sleep structure

- Introduced model error tracking layer for structured comparison of predictions vs observed outcomes.
  - Added `/data/model_error/` directory
  - Added primary dataset `model_error_gap_v1.csv`
  - Added rolling summary file `udi_tracker.csv`
  - Added `data/model_error/README.md` for layer orientation and handling rules
  - Added `methodology/prediction_evaluation.md` defining evaluation rules for point, range, and state predictions

- Introduced first forward-locked, pre-registered predictions in model error layer:
  - bodyweight stability prediction
  - pull-up repeatability prediction
  - marked with `calibration_state = pre`
  - no post-hoc adjustment or exemption permitted

- Integrated February 2026 biomarker snapshot artifacts:
  - DEXA scan
  - BodPod composition
  - TruAge and Advanced TruAge reports
  - TruHealth system report

- Introduced `biomarker_snapshot.csv` for monthly fused biomarker aggregation.

- Introduced `epigenetic_longitudinal.csv` for biological aging time-series tracking.

- Added `checksums.txt` files across snapshot directories to establish SHA256 binary artifact verification and improve auditability.

- Added `VERIFICATION.md` guide for external checksum validation of snapshot artifacts.

- Introduced `DATA_COVERAGE.md` to define dataset scope, completeness, and known limitations.

- Introduced `docs/methodology/subject_baseline_context.md` to define pre-observation context and interpretation boundaries.

- Linked subject baseline context across methodology and coverage documentation.

- Introduced internal week indexing convention:
  - added `docs/WEEK_INDEXING.md`
  - clarified reporting week offset relative to calendar weeks
  - linked indexing convention from `LATEST.md` and `INDEX.md`

- Added `docs/audits/2026-05-06-wednesday-audit.md` documenting:
  - repository coherence review
  - dataset maintenance targets
  - verification continuity
  - model-error layer assessment
  - structural stability observations during active operation

- Added supplementary public movement artifact documenting controlled-tempo pull-up execution under unchanged loading conditions.

- Added `docs/audits/2026-05-09-saturday-audit.md` documenting:
  - post-Wednesday structural review
  - dataset hygiene confirmation
  - checksum verification
  - model-error separation
  - weekly continuity
  - pre-snapshot archive stabilization

---

### Changed

- `LATEST.md` executive system dashboard updated to reflect:
  - W18 closed observation window
  - W19 active observation window
  - transition from active load confirmation into testing-window preservation
  - late-W18 autonomic strengthening under reduced Load Integration density
  - continued no-forward-claims posture ahead of May artifact ingestion

- `reports/2026-W19.md` refined to remove repository/public-activity language and preserve weekly report scope around training, recovery, testing-window conditions, and documentation continuity.

- `data/sleep_longitudinal_v1.csv` extended through 2026-05-10 to preserve weekly continuity across the W18 observation window.

- `data/model_error/model_error_gap_v1.csv` updated:
  - closed 035 as FAIL using first out-of-range violation
  - closed 036 as PASS across all prescribed sessions without structural breakdown
  - no schema changes; evaluation structure preserved

- `methodology/prediction_evaluation.md` updated:
  - aligned point and range prediction `error_direction` with dataset convention
  - clarified state prediction handling where `under` indicates the predicted condition did not materialize
  - no changes to schema or existing records

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
  - extended observations through 2026-W18

- `udi_tracker.csv` updated to reflect mixed post-calibration closure blocks and to withhold UDI where mixed prediction types reduce comparability.

- Model error layer documentation aligned with current methodology and open-prediction handling.

- `data/model_error/README.md` updated to clarify `calibration_state` semantics:
  - explicitly distinguishes `pre` from `post`
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

- Trimmed trailing blank rows from:
  - `sleep_longitudinal_v1.csv`
  - `model_error_gap_v1.csv`
  - `bloodwork_longitudinal.csv`
  - `epigenetic_longitudinal.csv`

- Clarified `/docs/audits/README.md` to support selective audit records by type rather than Saturday-only audit inclusion.

- Updated `PHASE_MAP.md` to describe Phase 3 as a reserved future structural category rather than a projected outcome, preserving retrospective phase-governance language.

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
- May testing artifacts are not yet integrated in this changelog window.

---

## Audit Status

- Wednesday audit pass completed
- Saturday audit pass completed
- Sunday weekly closeout completed
- W18 formally closed
- W19 initialized as active observation window
- Repository considered structurally consistent for external read-through
- May 9 Saturday audit recorded as pre-snapshot stabilization checkpoint
