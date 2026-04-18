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

- Weekly report for 2026-W14 finalized to document the completed observation window under continued consolidation conditions.
- Weekly report for 2026-W15 initialized to maintain forward archive continuity under the active observation window model.

- Added missing sleep dataset entry for 2026-03-22 using direct wearable-derived values.

- Updated sleep dataset to include 2026-W14 entries:
  - appended week-level rows using verified sheet-based values
  - corrected prior invalid append (removed inferred data)
  - preserved schema integrity and historical continuity

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

- Introduced DATA_COVERAGE.md:
  - defines dataset scope, completeness, and known limitations
  - establishes explicit boundary between tracked, partially tracked, and untracked domains

- Introduced subject baseline context document:
  - Added `docs/methodology/subject_baseline_context.md`
  - defines pre-observation environmental and physiological conditions
  - establishes interpretation boundaries for biomarker and epigenetic data

- Linked subject baseline context across methodology layer:
  - referenced in `ASSUMPTIONS_AND_BOUNDARIES.md`
  - referenced in `DATA_COVERAGE.md` for epigenetic and biomarker interpretation context

---

### Changed

- LATEST.md executive system dashboard updated to reflect:
  - W14 closeout status
  - W15 active observation window
  - continued stability under repeated exposure
  - consolidation-first posture with emerging passive adaptation
  - removal of narrative drift and alignment with observational standard

- DATA_DICTIONARY.md expanded to support biomarker and epigenetic fields introduced during the February 2026 snapshot expansion.

- sleep_longitudinal_v1.csv refined and aligned:
  - unified prior sleep records into a single longitudinal structure
  - corrected column alignment inconsistencies
  - removed stale references to superseded sleep-file naming
  - preserved historical rows without reinterpretation
  - standardized schema for forward compatibility
  - extended observations through the current window

- udi_tracker.csv updated to reflect mixed post-calibration closure blocks and to withhold UDI where mixed prediction types reduce comparability.

- Model error layer documentation aligned with current methodology and open-prediction handling.

- PDFs moved out of Git LFS and re-tracked as standard Git objects to restore full artifact integrity and prevent pointer file corruption.

- Enforced strict separation between forward-logged and reconstructed prediction records:
  - moved reconstructed dataset to `data/model_error/historical/`
  - removed reconstructed records from evaluative pathways
  - clarified non-equivalence between forward and retrospective entries

- Updated prediction review pipeline to reflect correct dataset paths and enforce evaluation boundaries:
  - aligned `prediction_to_outcome_pipeline.md` with current directory structure
  - restricted evaluative logic to forward-logged records only

- Reclassified early UDI snapshot as historical exploratory artifact:
  - removed from reports layer
  - relocated to historical archive
  - explicitly excluded from evaluative interpretation and UDI computation

- Completed temporal index layer:
  - replaced EPOCH_MAP with EPOCH_INDEX across repository
  - aligned all epoch records to index structure
  - improved chronological navigation and external readability

- Corrected repository-wide path inconsistencies and reference mismatches:
  - ensured internal links reflect current directory structure
  - removed stale or orphaned references

---

### Changed (Structural Alignment)

- `INDEX.md` fully updated to reflect current archive structure after document pruning:
  - removed references to deprecated phase and transition documents  
  - aligned reports description with active observation + retrospective reporting model  
  - tightened Tier 3 reference layer to include only durable, non-redundant documents  

- Repository structure simplified:
  - removed redundant conceptual layers (phase index, transition map, roadmap)
  - consolidated phase logic into `PHASE_MAP.md` and `STATE_TRANSITIONS.md`
  - reduced top-level document duplication to improve navigation clarity

---

### Removed

- `PHASE_INDEX.md` to eliminate redundant phase-layer framing after consolidation around `PHASE_MAP.md`.

- `ROADMAP.md` to remove future-facing narrative and keep archive state grounded in current artifacts and observable system behavior.

- `SYSTEM_CONSTRAINTS.md` to remove tactical, phase-local constraint framing and retain constraint visibility within `LATEST.md`, `RISK_MANAGEMENT.md`, and phase criteria.

- `EXPERIMENT_REGISTRY_PUBLIC.md` after consolidating protocol-shift visibility into reports, snapshots, and current-state documentation.

- `PHASE_2_READINESS_CHECKLIST.md` after consolidating phase gating into permanent criteria defined in `PHASE_DECLARATION_CRITERIA.md`.

- `TRANSITION_MAP.md` after consolidating transition logic into `PHASE_MAP.md` and `STATE_TRANSITIONS.md`.

- `DISCLAIMER.md` after retaining interpretation boundaries within `ASSUMPTIONS_AND_BOUNDARIES.md` and governance documents.

---

### Refined

- Repository language further tightened to preserve a conservative, artifact-first tone under increasing structural complexity.

- Separation reinforced between:
  - snapshot artifacts (immutable evidence)  
  - reports (active observation and retrospective interpretation)  
  - longitudinal datasets (time-series tracking)  
  - model error layer (prediction vs observed outcome)  
  - methodology layer (evaluation rules and closure standards)  

- Archive posture clarified around disturbance handling:
  - transient regulatory disruption is logged without overstating systemic meaning
  - continuity and recovery compatibility remain primary interpretation anchors

- GOVERNANCE.md updated to clarify interpretation constraints:
  - replaced exclusion of “narrative framing” with requirement for artifact-bound interpretation
  - aligned governance language with actual repository behavior

- README.md refined for consistency with governance and methodology layers:
  - removed residual narrative tone
  - strengthened alignment with artifact-first and retrospective interpretation model

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

## Audit Status

- Saturday audit pass completed
- Structural pruning, navigation alignment, and methodology layering validated
- Repository considered structurally consistent for external read-through

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
