# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented in this file.

This changelog records recent repository, dataset, methodology, governance, and archive-integrity changes.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`.

---

## [Unreleased]

### Added

#### Weekly reporting

- Added closeout for `reports/2026-W27.md`:
  - records successful return to standard B1 and Load Integration on all five available home-training days
  - documents post-travel reintegration without graded re-entry, compensatory workload, or protocol repair
  - records divided-attention pull-up control and voluntary tempo modulation as candidate evidence relevant to Model Error 042
  - distinguishes daily biomarker HRV from sleep HRV
  - preserves records 041–044 as open and unscored
  - retains Phase 2D as a retrospective classification rather than a current declaration

- Added initialization for `reports/2026-W28.md`:
  - carries forward standard B1 and Load Integration without escalation
  - prioritizes recovery monitoring after the higher W27 multimodal workload
  - continues passive observation of reduced-overhead execution, divided attention, and force modulation
  - preserves August snapshot and model-error governance boundaries

#### Datasets and data quality

- Appended W27 sleep observations for `2026-07-06` through `2026-07-12` to `data/sleep_longitudinal_v1.csv`:
  - values were transferred from the current source dataset
  - no inferred or reconstructed values were added
  - canonical sleep coverage now extends through `2026-07-12`

- Added `data/DATA_QUALITY_NOTES.md`:
  - documents unresolved sleep-field duplication for `2026-05-18` through `2026-05-31`
  - documents sleep-stage total discrepancies for `2026-03-31` and `2026-04-02`
  - requires source reconciliation before correction
  - prohibits inferred modification of unresolved values
  - defines a traceable correction process

#### Prediction and methodology governance

- Added Model Error records 041–044:
  - recovery capacity during the July–August observation block
  - ambient-execution plateau behavior through the August snapshot window
  - August 2026 biological snapshot translation
  - protocol-governance preservation through the next snapshot cycle

- Added `methodology/open_prediction_evaluation_plan_041_044.md`:
  - defines prospective scoring rules and evidence boundaries for records 041–044
  - establishes repeated-evidence requirements for record 042
  - defines biological-anchor and magnitude rules for record 043
  - protects all records from outcome-driven reinterpretation
  - preserves the original prediction fields and open status of records 041–044

- Added Event 003 to `data/model_error/calibration_events_log.md`:
  - records initialization of the July–August prospective prediction block
  - preserves existing prediction methodology and UDI governance

#### Audits and archive integrity

- Added repository audits for:
  - `2026-06-24`
  - `2026-06-27`
  - `2026-07-02`
  - `2026-07-08`
  - `2026-07-11`
  - `2026-07-15`

- The `2026-07-11` Saturday audit:
  - reviews repository structure, links, CSV parsing, checksums, report continuity, prediction continuity, protocol state, methodology, metadata, and release readiness
  - identifies targeted sleep-data, protocol-status, and experiment-wording issues
  - records completion of the approved remediation sequence
  - confirms final passing checks while preserving unresolved source-reconciliation items

- Added `docs/audits/2026-07-15-wednesday-audit.md`:
  - verifies repository continuity after W27 closeout and W28 initialization
  - confirms all CSV datasets remain parseable and structurally consistent
  - confirms canonical sleep continuity through `2026-07-12`
  - verifies checksum, metadata, weekly-report, and model-error continuity
  - identifies the need to distinguish daily biomarker HRV from sleep HRV
  - documents the difference between the July 10 instructional pull-up event and its July 11 repository review
  - identifies remaining governance-language inconsistencies across legacy documentation
  - confirms records 041–044 remain open, unscored, and unchanged
  - records a final passing audit disposition with targeted documentation alignment due

#### Public archive and navigation

- Added Zenodo DOI metadata and citation support:
  - DOI badge and citation section in `README.md`
  - DOI reference in `LATEST.md`
  - DOI metadata in `CITATION.cff`

- Added `docs/OBSERVER_QUICKSTART.md` as a compact external evaluation path.

- Added a minimal `.gitignore` covering operating-system files, editor settings, caches, virtual environments, checkpoints, and logs without excluding archive content.

---

### Changed

#### Current-state alignment

- Updated `LATEST.md`:
  - advances the archive from W27 active to W28 active
  - records W27 as closed
  - advances canonical sleep coverage through `2026-07-12`
  - summarizes successful post-travel reintegration
  - distinguishes daily biomarker HRV from sleep HRV
  - surfaces candidate reduced-overhead and divided-attention evidence without declaring Phase 2D
  - preserves Model Error records 041–044 as open
  - records that prospective scoring rules for records 041–044 have been registered
  - distinguishes retrospective interpretation from the governed prospective prediction layer
  - adds navigation to data-quality, data-collection, and open-prediction methodology
  - identifies the August 2026 artifact cycle as the next major objective checkpoint
  - reduces repeated weekly-report interpretation and restores an executive-dashboard scope

#### Weekly report governance

- Updated `reports/2026-W27.md` during and after the observation window:
  - confines forward prediction to the registered model-error layer
  - adds the instructional pull-up observation as candidate evidence for record 042
  - documents divided attention, verbal instruction, positional pauses, and preserved control
  - explicitly preserves record 042 unchanged and open
  - distinguishes daily biomarker HRV of approximately 61 ms from sleep HRV of approximately 59.4 ms
  - applies the distinction in the current-state, recovery, and closeout sections

- Expanded `reports/README.md`:
  - defines active observation reports and retrospective reports as separate operating modes
  - establishes the weekly report lifecycle from initialization through retrospective closeout
  - permits clearly labeled contemporaneous observations and candidate model-error evidence
  - prohibits unregistered forward predictions, premature closure, and prediction rewriting
  - defines relationships among source artifacts, structured datasets, collection notes, reports, dashboards, and model-error records
  - adds correction rules for dates, labels, references, and source attribution
  - aligns report language with incomplete environmental control and source-backed correction governance

#### Prediction-plan registration context

- Updated `methodology/open_prediction_evaluation_plan_041_044.md`:
  - discloses that the Washington perturbation and July 10 instructional pull-up were already known when the plan was registered
  - clarifies that final trajectories and all August outcomes remained unknown
  - confirms that the known pull-up event remained one candidate observation rather than a completed record 042 transition
  - distinguishes the August TruDiagnostic sample as the primary biological endpoint
  - defines `2026-08-17` through `2026-08-18` as the planned supplemental measurement window
  - distinguishes primary epigenetic scoring from supplemental DEXA, VO₂, BodPod, bodyweight, and recovery evidence
  - defines snapshot-cycle completion and delayed-test handling
  - preserves all original scoring thresholds, prediction fields, and record statuses

#### Governance alignment

- Expanded `GOVERNANCE.md`:
  - replaces claims of complete environmental control with defined protocol constraints under incomplete real-world control
  - prohibits silent, unsupported, and outcome-driven rewriting
  - permits narrow, traceable, source-backed correction
  - establishes source and evidence hierarchy
  - defines prediction governance and candidate-evidence boundaries
  - defines protocol-change and phase-declaration requirements
  - adds missingness, public-archive, checksum, and enforcement standards
  - distinguishes archive maintenance from new biological observation
  - preserves records, outcomes, protocol exposures, and phase status

- Expanded `METHODOLOGY_AND_CONTROLS.md`:
  - replaces controlled-lifestyle framing with stabilized inputs under incomplete environmental control
  - defines biological, body-composition, performance, recovery, and behavioral outcome domains
  - distinguishes structured datasets from narrative evidence
  - defines source hierarchy, missingness, source-backed correction, measurement comparability, and derived-value procedures
  - distinguishes daily biomarker HRV from sleep HRV
  - adds registered prediction and model-error methodology
  - defines perturbation handling, phase interpretation, audit scope, and methodological limitations
  - preserves the single-subject, non-causal, non-prescriptive boundary

- Expanded `SYSTEM_OVERVIEW.md`:
  - updates the archive from a simple observation pipeline to a longitudinal observation and calibration system
  - adds source-artifact, structured-data, contemporaneous-note, model-error, and governance layers
  - replaces the absolute prohibition on forward claims with governed prediction language
  - defines incomplete environmental control and ordinary-life contextual variability
  - establishes source-backed correction logic
  - adds protocol, experiment, data-quality, and prediction-evaluation paths to the artifact map
  - defines model correction as an explicit system output
  - preserves retrospective phase and interpretation boundaries

#### Coverage and collection methodology

- Updated `data/DATA_COVERAGE.md`:
  - replaces broad completeness claims with defined coverage categories
  - distinguishes structured, narrative, snapshot, contextual, partial, planned, and untracked coverage
  - documents the absence of canonical daily training, subjective-biomarker, and perturbation-event exports
  - distinguishes continuity from field-level confidence
  - adds navigation to collection methodology, quality notes, reports, snapshots, and prediction evaluation

- Expanded `methodology/data-collection.md`:
  - defines source hierarchy, transcription, missingness, units, temporal handling, derivation, inference, and correction rules
  - separates collection from interpretation
  - defines provenance requirements for screenshots, device exports, operator notes, and future structured datasets
  - establishes how candidate model-error evidence enters through ordinary collection

#### Protocol and experiment status

- Updated `protocols/hybrid-expansion-phase-v2.md`:
  - marks the document historical, superseded, and inactive
  - preserves its original design for provenance
  - separates historical prescriptions from current Load Integration governance

- Updated `experiments/EXP-001-autophagy-endurance.md`:
  - corrects the active observation window to January 2026 through April 16, 2026
  - identifies the experiment as paused
  - removes it as an active explanatory variable
  - defines requirements for any future reactivation

#### Repository orientation

- Updated `README.md`:
  - clarifies that biological interpretation is retrospective while registered predictions remain prospective and governed
  - adds direct navigation to prediction-evaluation and data-quality documentation
  - improves observer entry and archive-structure descriptions
  - aligns scope, limitations, and environmental-control language with actual repository practice

- Updated `DATASET_OVERVIEW.md`:
  - replaces claims of tightly controlled conditions with defined protocol constraints under incomplete real-world control
  - distinguishes source artifacts, structured datasets, reports, predictions, and milestone context
  - adds evidence hierarchy, limitations, environmental context, and correction-aware integrity language

- Updated observer-facing navigation:
  - rewrote `docs/START_HERE.md` as a compact first-contact guide
  - clarified `docs/NEWCOMER_PATH.md` as the longer reading route
  - linked `docs/OBSERVER_QUICKSTART.md` from primary orientation documents
  - updated `docs/FOR_OBSERVERS.md` and `INDEX.md` to distinguish quickstart, evaluation, newcomer, and complete-index pathways

#### Audit closeout

- Updated `docs/audits/2026-07-11-saturday-audit.md`:
  - preserves original pre-remediation findings
  - appends post-cleanup verification
  - confirms repository inventory, Markdown-link integrity, CSV parsing, artifact checksums, report continuity, prediction continuity, protocol status, and release metadata
  - records a final `PASS`
  - preserves sleep-source reconciliation, blood-report replacement, and later structured-export work as governed open items

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
