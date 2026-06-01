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

- Weekly report for 2026-W21 finalized to document the completed post-travel reintegration window under stable Phase 2 Load Integration conditions.

- Weekly report for 2026-W22 initialized to maintain forward archive continuity during normal-life variability monitoring and ambient execution consolidation.

- Appended sleep dataset entries for 2026-W21 (2026-05-25 through 2026-05-31):
  - direct crossover from source dataset
  - no inferred or reconstructed values included
  - schema consistency preserved against longitudinal sleep structure
  - canonical sleep dataset extended through 2026-05-31

- Added `TELEMETRY.md` to define the relationship between the governed archive and the parallel real-time public subjective telemetry layer.

- Added `data/model_error/WHAT_THIS_LAYER_IS.md` to clarify the purpose, constraints, and calibration role of the model-error tracking layer.

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

- Added May 2026 snapshot artifacts and verification layer:
  - DEXA body composition artifact
  - DEXA summary artifact
  - BodPod / COSMED artifact
  - VO2 summary artifact
  - SHA256 checksum verification file
  - May 2026 epoch anchor
  - snapshot log integration
  - epoch index integration

- Added May 2026 prediction closures tied to observed testing outcomes:
  - closed DEXA prediction records
  - closed VO2 prediction records
  - updated latest prediction layer state for May closures
 
- Added May 2026 TruDiagnostic snapshot artifacts:
  - `2026-05-advanced-truage.pdf`
  - `2026-05-truage.pdf`
  - `2026-05-truhealth.pdf`
  - integrated into snapshot verification coverage
  - incorporated into the May 2026 epoch record

- Added May 2026 integrated biomarker fusion:
  - appended May snapshot row to `biomarker_snapshot.csv`
  - appended May epigenetic aging data to `epigenetic_longitudinal.csv`
  - appended May TruHealth marker set to `bloodwork_longitudinal.csv`

- Added May 2026 calibration event:
  - documented snapshot closure integration
  - documented expansion of post-calibration prediction inventory
  - documented continued UDI governance posture

- Added May 2026 UDI tracker update:
  - incorporated all currently closed May prediction records
  - retained governance-locked UDI status pending approved weighting methodology

- Added `docs/audits/2026-05-13-wednesday-audit.md` documenting:
  - post-snapshot repository coherence review
  - Markdown link integrity
  - checksum verification continuity
  - model-error direction normalization
  - W19 audit readiness after May artifact integration

- Added post-snapshot forward-locked model-error predictions:
  - push-up repeatability under Load Integration expansion
  - recovery stability during resumed Load Integration density
  - both marked with `calibration_state = pre`

- Closed model-error entries 037 and 038:
  - 037 push-up repeatability closed as pass
  - 038 recovery stability closed as fail due to evaluation-boundary invalidation rather than biological destabilization

- Added post-travel forward-locked model-error predictions:
  - 039 travel reintegration following travel block
  - 040 recovery-floor preservation during post-travel reintegration
  - both marked with `calibration_state = pre`
  - evaluation window begins with reintegration exposures on 2026-05-28

- Added `docs/audits/2026-05-16-saturday-audit.md` documenting:
  - post-May structural stabilization review
  - governance consistency assessment
  - observer-legibility review
  - checksum continuity verification
  - repository navigation confirmation
  - restraint and anti-overpolish posture assessment

- Added `docs/audits/2026-05-20-wednesday-audit.md` documenting:
  - mid-week repository coherence review
  - Markdown link integrity verification
  - checksum continuity verification
  - W19/W20 state alignment confirmation
  - observer-facing language refinement review
  - May biomarker integration clarification pass

- Added `docs/audits/2026-05-27-wednesday-audit.md` documenting:
  - W20/W21 continuity review
  - Markdown link integrity verification
  - dataset parse integrity confirmation
  - model-error layer consistency review
  - observer-facing wording refinement recommendations
  - continued governance posture alignment
 
- Added UDI v1.1 stratified reporting framework to formalize prediction-evaluation governance while composite UDI remains intentionally withheld.

- Added `data/model_error/udi_by_type_tracker.csv` to separate point, range, state, and trajectory prediction evaluation pathways and prevent mixed-type aggregation artifacts.

- Corrected prediction direction definitions in `methodology/prediction_evaluation.md` to align documented closure logic with repository model-error tracking conventions.

- Amended `docs/methodology/UDI_framework_v1.md` to define stratified UDI reporting, document exclusion of state and trajectory predictions from magnitude-based UDI calculations, and establish future publication criteria for composite UDI.

- Updated UDI governance records to reflect v1.1 approval status and continued withholding of composite UDI pending compound-record resolution and further methodological development.

- Updated UDI framework definition language to align the core UDI definition with v1.1 stratified reporting methodology and continued composite withholding.

- Clarified that UDI applies only to eligible magnitude-based prediction classes, while state and trajectory predictions are tracked separately through concordance measures.

---

### Changed

- `README.md` updated to include:
  - `TELEMETRY.md` navigation
  - model-error layer context
  - subjective telemetry context
  - clearer distinction between governed records and informal subjective telemetry

- `WHY_PUBLIC.md` clarified to define the public archive as the governed observation layer rather than the full lived experience.

- `DATA_DICTIONARY.md` updated to clarify that some subjective or qualitative context may intentionally remain outside structured dataset fields and may be externally represented through the public telemetry layer.

- `data/model_error/WHAT_THIS_LAYER_IS.md` link paths corrected to align with existing methodology file names and locations.

- `LATEST.md` executive system dashboard updated to reflect:
  - W21 closed observation window
  - W22 active observation window
  - W21 sleep observations appended
  - normal-life variability monitoring posture
  - ambient execution consolidation posture
  - continued no-forward-claims posture while TruDiagnostic results remain pending

- `reports/2026-W19.md` refined to remove repository/public-activity language and preserve weekly report scope around training, recovery, testing-window conditions, and documentation continuity.

- `reports/2026-W21.md` finalized to reflect:
  - completed post-travel recovery normalization
  - preserved B1 aerobic anchor continuity
  - resumed Load Integration compatibility
  - pull-up sequencing refinement
  - push-up integration stability
  - stable sleep and autonomic behavior
  - continued archive stewardship without recovery collapse or behavioral destabilization

- `reports/2026-W22.md` initialized to reflect:
  - active W22 observation window
  - normal-life variability monitoring
  - ambient execution consolidation
  - continued Load Integration without escalation assumptions

- `reports/2026-W16.md` refined to replace stronger validation language with retrospective stability evaluation language.

- `DATA_COVERAGE.md` updated:
  - clarified May 2026 structured biomarker integration status
  - explicitly constrained interpretation of pending TruDiagnostic-linked testing artifacts
  - reinforced distinction between archived source artifacts and completed structured biomarker fusion

- `data/sleep_longitudinal_v1.csv` extended through 2026-05-31 to preserve weekly continuity across the W21 observation window.

- `data/model_error/model_error_gap_v1.csv` updated:
  - closed 035 as FAIL using first out-of-range violation
  - closed 036 as PASS across all prescribed sessions without structural breakdown
  - closed May 2026 DEXA and VO2 prediction records
  - closed 037 as PASS after push-up integration completed without structural regression or recovery destabilization
  - closed 038 as FAIL due to evaluation-boundary invalidation from controlled travel-associated recovery / reduced structured exposure
  - added open prediction 039 for post-travel B1 and Load Integration reintegration
  - added open prediction 040 for recovery-floor preservation during post-travel reintegration
  - preserved distinction between failed prediction criteria and biological destabilization
  - preserved forward-locked evaluation structure before reintegration exposure begins

- `data/model_error/model_error_gap_v1.csv` normalized historical `error_direction` labels for closed model-error records to align with the active prediction-versus-actual convention. No prediction values, actual values, error magnitudes, statuses, or notes were changed.

- `methodology/prediction_evaluation.md` updated:
  - aligned point and range prediction `error_direction` with dataset convention
  - clarified state prediction handling where `under` indicates the predicted condition did not materialize
  - no changes to schema or existing records

- `CHANGELOG.md` restructured:
  - converted to active rolling window model
  - moved historical entries to `docs/archive/CHANGELOG_ARCHIVE.md`

- `INDEX.md` updated:
  - added navigation reference to week indexing convention
  - aligned snapshot navigation with May 2026 epoch integration

- `DATA_DICTIONARY.md` expanded to support biomarker and epigenetic fields introduced during the February 2026 snapshot expansion.

- `sleep_longitudinal_v1.csv` refined and aligned:
  - unified prior sleep records into a single longitudinal structure
  - corrected column alignment inconsistencies
  - removed stale references to superseded sleep-file naming
  - preserved historical rows without reinterpretation
  - standardized schema for forward compatibility
  - extended observations through 2026-W20

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

- Normalized May 2026 snapshot checksum formatting for consistency with repository-wide verification conventions.

- `snapshots/2026-05/2026-05 Epoch.md` updated:
  - removed pending TruDiagnostic language
  - added TruAge references
  - added Advanced TruAge references
  - added TruHealth references
  - updated snapshot completeness status

- `SNAPSHOT_LOG.md` updated:
  - May 2026 snapshot revised from partial testing window to completed integrated testing window
  - added TruDiagnostic artifact references

- `EPOCH_INDEX.md` updated:
  - aligned May 2026 entry with completed integrated snapshot state

- `LATEST.md` updated:
  - May 2026 integrated snapshot marked complete
  - TruDiagnostic results no longer pending
  - model-error record 032 closed
  - prediction-layer status updated
  - archive state aligned with completed May integration cycle

- `DATA_COVERAGE.md` updated:
  - May 2026 structured biomarker fusion marked complete
  - added bloodwork longitudinal dataset reference
  - added UDI tracker dataset reference
  - removed pending TruDiagnostic dependency language

- `data/model_error/model_error_gap_v1.csv` updated:
  - closed 032 against observed May TruDiagnostic outcomes
  - recorded DunedinPACE and SymphonyAge comparison results
  - preserved artifact-bound closure methodology

- `data/model_error/udi_tracker.csv` updated:
  - added May 2026 closure inventory summary
  - retained governance-locked UDI status

- `data/model_error/calibration_events_log.md` updated:
  - added May 2026 snapshot closure integration event

- `biomarker_snapshot.csv` expanded to include:
  - integrated May 2026 DEXA
  - BodPod / COSMED
  - TruAge
  - Advanced TruAge
  - TruHealth data

- `epigenetic_longitudinal.csv` expanded with:
  - May 2026 OMICm age
  - May 2026 DunedinPACE
  - May 2026 SymphonyAge
  - May 2026 organ-system age domains

- `bloodwork_longitudinal.csv` expanded with:
  - May 2026 TruHealth marker set
  - vascular markers
  - inflammation markers
  - immune markers
  - neurocognitive markers
  - toxin exposure markers
  - mitochondrial markers
  - NAD metabolism markers
 
- `methodology/prediction_evaluation.md` updated to correct point and range prediction direction logic and align closure rules with repository-wide UDI v1.1 directional definitions.

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
  - telemetry layer

- Archive posture clarified around disturbance handling.

- `GOVERNANCE.md` updated to clarify artifact-bound interpretation constraints.

- `README.md` refined for consistency with governance and methodology layers.

---

### Notes

- Detailed marker-level TruHealth expansion remains intentionally limited at this stage.
- UDI remains selectively applied where methodological comparability is sufficient.
- Legacy trajectory prediction entries may remain open until a formal evaluation standard is defined.
- Current architecture prioritizes clarity, separation of concerns, and auditability over premature abstraction.
- May 2026 TruDiagnostic results have been integrated into the snapshot, dataset, and model-error layers. Interpretation remains governed by artifact-first methodology and retrospective reporting boundaries.

---

## Audit Status

- Wednesday audit pass completed
- Saturday audit pass completed
- Sunday weekly closeout completed
- Model-error entries 037 and 038 closed
- Model-error entries 039 and 040 opened for post-travel reintegration monitoring
- Repository considered structurally consistent for external read-through
- May 9 Saturday audit recorded as pre-snapshot stabilization checkpoint
- May 2026 snapshot artifact integration completed
- May 2026 checksum verification layer normalized
- May 2026 prediction closure pass completed
- May 13 Wednesday audit completed after post-snapshot model-error direction normalization
- May 16 Saturday audit completed after post-snapshot stabilization and observer-legibility review
- May 20 Wednesday audit completed after mid-week coherence, verification, and observer-facing refinement review
- May 27 Wednesday audit completed after W20/W21 continuity review and observer-facing wording refinement
- W21 formally closed
- W22 initialized as active observation window
- W21 sleep dataset entries appended
- `LATEST.md` updated for W22 active state
- May 2026 TruDiagnostic reports integrated
- May 2026 structured biomarker fusion completed
- May 2026 epigenetic longitudinal dataset updated
- May 2026 bloodwork longitudinal dataset updated
- Model-error record 032 closed against observed TruDiagnostic outcomes
- UDI tracker updated through May 2026 closure inventory
- Calibration events log updated for May 2026 snapshot completion
- Data coverage layer updated to reflect completed May integration
