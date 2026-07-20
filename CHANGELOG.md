# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records repository, dataset, methodology, governance, and archive-integrity changes.

---

## [Unreleased]

### Added

#### Weekly reporting

- Added retrospective closeout for `reports/2026-W28.md`:
  - records seven completed B1 and seven completed Load Integration sessions
  - records 169 minutes of optional aquatic activity and 869 total logged movement minutes
  - summarizes verified bodyweight, recovery, and sleep metrics
  - documents naturally occurring schedule, fatigue, equipment, recreational, and social-context variation
  - records repeated candidate evidence relevant to Model Error records 041, 042, and 044
  - preserves records 041–044 as open and unscored
  - preserves Phase 2 status without declaring Phase 2D

- Added initialization for `reports/2026-W29.md`:
  - carries forward the standard protocol without progression
  - prioritizes observation for delayed effects after the higher-density W28 window
  - continues passive collection of reduced-overhead, adaptable-execution, and portability evidence
  - prohibits converting successful W28 variations into required tests
  - uses a shorter delta-focused structure to reduce weekly-report overhead

#### Datasets and data quality

- Appended sleep observations for `2026-07-13` through `2026-07-19` to `data/sleep_longitudinal_v1.csv`:
  - extends canonical sleep coverage through `2026-07-19`
  - preserves daily sleep-stage, HRV, sleeping-heart-rate, readiness, and subjective-state fields
  - retains low-confidence REM classification for `2026-07-17` and `2026-07-19`
  - preserves reported awake time without reconstructing values from other fields
  - uses `2026-07-13` as the corrected chronological date
  - adds no inferred replacement values

- Added `data/DATA_QUALITY_NOTES.md`:
  - documents unresolved awake-field duplication from `2026-05-18` through `2026-05-31`
  - documents sleep-stage total discrepancies for `2026-03-31` and `2026-04-02`
  - requires source reconciliation before modification
  - prohibits silent or inferred repair

#### Prediction and methodology governance

- Added Model Error records 041–044 covering:
  - July–August recovery capacity
  - ambient-execution plateau behavior
  - August biological-snapshot translation
  - protocol-governance preservation

- Added `methodology/open_prediction_evaluation_plan_041_044.md`:
  - registers scoring rules and admissible evidence before outcome review
  - defines repeated-evidence requirements for record 042
  - separates the primary epigenetic endpoint from supplemental August measurements
  - protects prediction language from outcome-driven revision

- Added Event 003 to `data/model_error/calibration_events_log.md` for initialization of the July–August prediction block.

#### Audits and archive integrity

- Added repository audits dated:
  - `2026-06-24`
  - `2026-06-27`
  - `2026-07-02`
  - `2026-07-08`
  - `2026-07-11`
  - `2026-07-15`
  - `2026-07-18`

- The July audits collectively:
  - verified repository structure, links, Markdown integrity, CSV parsing, checksums, report continuity, prediction continuity, and release metadata
  - identified targeted sleep-data, protocol-status, experiment-wording, and governance-language issues
  - confirmed remediation where source evidence was sufficient
  - preserved unresolved source-reconciliation items without inferred correction
  - recognized administrative overhead as a repository-design concern
  - recommended shorter, delta-focused weekly reports and audits

#### Public archive and navigation

- Added Zenodo DOI and citation support across `README.md`, `LATEST.md`, and `CITATION.cff`.

- Added `docs/OBSERVER_QUICKSTART.md` as a compact external evaluation path.

- Added a minimal `.gitignore` without excluding archival content.

---

### Changed

#### Current-state alignment

- Updated `LATEST.md`:
  - marks `2026-W28` closed and `2026-W29` active
  - advances canonical sleep coverage through `2026-07-19`
  - summarizes W28 training density, preserved recovery, and cross-context execution
  - distinguishes daily biomarker HRV from sleep HRV
  - carries Model Error records 041–044 forward unchanged
  - identifies delayed-load observation as the primary W29 question
  - retains the August 2026 snapshot as the next major objective checkpoint
  - reduces repeated protocol and weekly-report language to preserve dashboard scope

#### Weekly report governance

- Updated `reports/2026-W27.md`:
  - closes the post-travel reintegration window
  - distinguishes daily biomarker HRV from sleep HRV
  - records divided-attention pull-up control and voluntary tempo modulation as candidate record 042 evidence
  - preserves Phase 2D as a retrospective classification

- Replaced the active W28 planning scaffold with a retrospective closeout:
  - emphasizes material change rather than repeating standing protocol details
  - separates verified metrics from interpretation
  - distinguishes internal fatigue from functional degradation
  - records source-confidence limitations and unresolved correction notes
  - carries only consequential observations into W29

- Expanded `reports/README.md`:
  - distinguishes active observation reports from retrospective closeouts
  - defines the weekly report lifecycle
  - permits labeled contemporaneous observations and candidate model-error evidence
  - prohibits unregistered prediction, prediction rewriting, and premature closure

- Expanded `schemas/weekly-report-template.md`:
  - establishes a compact governed structure
  - emphasizes deviations, new evidence, unresolved questions, and decisions
  - separates B1, Load Integration, optional activity, recovery, structured metrics, perturbations, model-error relevance, and governance
  - prohibits inferred missing values
  - does not require historical reports to be reformatted

#### Governance and methodology

- Expanded `GOVERNANCE.md`, `METHODOLOGY_AND_CONTROLS.md`, `SYSTEM_OVERVIEW.md`, and `ASSUMPTIONS_AND_BOUNDARIES.md` to:
  - replace complete-control claims with stabilized inputs under incomplete real-world control
  - distinguish retrospective interpretation from registered prospective prediction
  - define evidence hierarchy, missingness, derivation, source-backed correction, and measurement comparability
  - establish candidate-evidence and phase-declaration boundaries
  - prohibit silent, unsupported, or outcome-driven rewriting
  - define model correction as an explicit archive output

- Expanded `docs/FOR_OBSERVERS.md`:
  - distinguishes active reports, closed reports, datasets, snapshots, and predictions
  - explains candidate evidence and source-backed correction
  - adds concise evaluation and warning-sign guidance

- Updated `data/DATA_COVERAGE.md`:
  - replaces broad completeness claims with explicit structured, narrative, contextual, partial, planned, and untracked categories
  - documents the absence of canonical daily training, subjective-biomarker, and perturbation-event exports

- Expanded `methodology/data-collection.md`:
  - defines source hierarchy, transcription, provenance, units, timing, derivation, inference, missingness, and correction rules
  - separates collection from interpretation

#### Prediction-plan registration context

- Updated `methodology/open_prediction_evaluation_plan_041_044.md`:
  - discloses observations already known at registration
  - confirms final trajectories and August outcomes remained unknown
  - distinguishes the primary TruDiagnostic endpoint from supplemental DEXA, VO₂ max, Bod Pod, bodyweight, and recovery evidence
  - defines the planned August 17–18 measurement window
  - preserves original thresholds and record status

#### Protocol and experiment status

- Updated `protocols/hybrid-expansion-phase-v2.md`:
  - marks the document historical, superseded, and inactive
  - preserves it for provenance

- Updated `experiments/EXP-001-autophagy-endurance.md`:
  - corrects the active observation window
  - marks the experiment paused
  - removes it as an active explanatory variable
  - defines requirements for reactivation

#### Repository orientation

- Updated `README.md`, `DATASET_OVERVIEW.md`, `INDEX.md`, `docs/START_HERE.md`, and `docs/NEWCOMER_PATH.md` to:
  - clarify archive scope and environmental limitations
  - distinguish source artifacts, structured data, reports, snapshots, and predictions
  - expose data-quality, collection, protocol, experiment, audit, and prediction-evaluation paths
  - improve external navigation without duplicating methodology

---

### Fixed

- Corrected the instructional pull-up observation date to `2026-07-10` while preserving `2026-07-11` as the audit and repository-incorporation date.

- Corrected the active EXP-001 duration wording and deprecated the stale hybrid protocol without rewriting historical exposure.

- Preserved `2026-07-13` as the intended W28 date in the canonical sleep append after identifying an incorrect source-workbook date encoding.

- Documented the correct separation of the `2026-07-13` cardiovascular values:
  - daily HRV: `77 ms`
  - resting heart rate: `44 bpm`
  - daily average heart rate: `61 bpm`
  - sleep HRV: `88 ms`
  - average sleeping heart rate: `46 bpm`

The source-workbook narrative discrepancy remains documented rather than silently overwritten.

---

## [1.0.0] - 2026-06-23

### Added

- Published the first DOI-bearing archival release.
- Minted Zenodo DOI `10.5281/zenodo.20815612`.
- Archived and preserved version `v1.0.0` through Zenodo.
- Transitioned the repository to a citable public research archive.

### Changed

- Updated `CODEMETA.json`:
  - version set to `1.0.0`
  - `dateModified` set to `2026-06-23`

- Updated `CITATION.cff`:
  - version set to `1.0.0`
  - release date set to `2026-06-23`

- Normalized historical audit filenames.

- Restructured `CHANGELOG.md`:
  - moved older history to `docs/archive/CHANGELOG_ARCHIVE.md`
  - limited the active changelog to recent structural changes

- Updated `LATEST.md` to distinguish recent activity from archived repository history.
