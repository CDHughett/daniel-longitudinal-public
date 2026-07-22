# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records repository, dataset, methodology, governance, privacy, and archive-integrity changes.

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

#### RingConn source exports

- Added a direct RingConn source-export acquisition package under:

  `data/source_exports/ringconn/2026-07-21/`

- Added:

  - `ringconn-sleep-export.csv`
  - `ringconn-activity-export.csv`
  - `ringconn-vital-signs-export.csv`
  - `README.md`
  - `checksums.txt`

- Registered the package as:

  - a direct user-account export
  - provider-source evidence
  - separate from curated longitudinal datasets
  - byte-preserved
  - checksum registered
  - privacy screened
  - available for targeted reconciliation or future analysis

- Documented source coverage:

  - 366 sleep-episode rows
  - 360 activity-date rows
  - 360 vital-sign-date rows
  - sleep coverage beginning 2025-07-21
  - activity and vital-sign coverage through 2026-07-20
  - missing source dates
  - multiple sleep episodes
  - unresolved timezone behavior
  - mixed timestamp precision
  - provider-defined field semantics

- Added root `.gitattributes` control:

  ```gitattributes
  data/source_exports/**/*.csv -text
  ```

- The Git attribute prevents line-ending conversion for provider-source CSV files stored beneath `data/source_exports/`.

- Verified that the committed RingConn files:

  - match the original downloaded exports byte-for-byte
  - preserve original CRLF line endings
  - retain their original file sizes
  - match the registered SHA-256 manifest
  - remain byte-identical after download through a fresh GitHub repository ZIP

- Verified all registered archive checksums after the byte-preservation repair:

  - 10 checksum manifests
  - 29 registered artifacts
  - 29 of 29 passed

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

- Expanded the data-quality register through DQ-008:
  - identifies direct-export correction candidates for DQ-001 through DQ-003
  - preserves `awakenings_count` as unresolved
  - documents sleep date-assignment and timezone uncertainty
  - documents mixed timestamp precision
  - documents multiple sleep episodes
  - documents cross-domain missing dates
  - documents the November 17 unclassified-stage provider session
  - documents broader curated-versus-export differences
  - converts unresolved source questions into field-specific analytical restrictions
  - authorizes no bulk historical overwrite

- Confirmed that RingConn ingestion did not modify:

  - `data/sleep_longitudinal_v1.csv`
  - existing weekly reports
  - Model Error records
  - protocol exposure
  - phase status

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
  - `2026-07-22`

- The July audits collectively:
  - verified repository structure, links, Markdown integrity, CSV parsing, checksums, report continuity, prediction continuity, and release metadata
  - identified targeted sleep-data, protocol-status, experiment-wording, governance-language, privacy, and source-provenance issues
  - confirmed remediation where source evidence was sufficient
  - preserved unresolved source-reconciliation items without inferred correction
  - recognized administrative overhead as a repository-design concern
  - recommended shorter, delta-focused weekly reports and audits

- Added `docs/audits/2026-07-22-wednesday-audit.md`:
  - confirms mechanical repository integrity after W28 closeout and W29 initialization
  - verifies canonical sleep continuity through `2026-07-19`
  - verifies the current sanitized July 2025 blood artifact and updated checksum
  - distinguishes current-tree sanitization from historical and archival distribution
  - audits annual RingConn sleep, activity, and vital-sign exports
  - identifies multiple sleep episodes, missing dates, timezone limitations, and provider anomalies
  - documents material differences between contemporaneous curated sleep values and later provider-export values
  - prohibits direct append of the annual sleep export into `data/sleep_longitudinal_v1.csv`
  - preserves records 041–044, release metadata, protocol state, and phase status unchanged

- Appended a post-audit disposition to the July 22 audit:
  - preserves the original audit as a point-in-time record
  - records completion of controlled privacy remediation
  - records completion of RingConn source ingestion and byte verification
  - supersedes the immediate normalized-tracker recommendation
  - establishes periodic immutable provider exports as the current wearable-preservation model
  - retains GitHub provider-side cleanup as pending
  - confirms that no canonical biological value was changed

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

#### Wearable evidence architecture

- Updated `MEASUREMENT_SOURCES.md`:
  - distinguishes provider artifacts, direct exports, screenshots, transcription, derivation, and narrative evidence
  - records RingConn Gen 2 provenance and known software-version limitations
  - defines daily, resting, and sleep heart-rate and HRV boundaries
  - registers completion of the 2026-07-21 RingConn export ingestion
  - documents source-export coverage and byte-preservation controls
  - distinguishes RingConn-reported calories from active or total calorie assumptions
  - preserves timezone and provider-reprocessing uncertainty
  - establishes periodic immutable exports as the current wearable-maintenance model
  - defers normalized wearable trackers until a defined analytical or publication need exists

- Updated `DATA_DICTIONARY.md`:
  - defines provider-source, curated, derived, and narrative data layers
  - registers direct RingConn export fields using provider labels
  - defines missingness and source-state boundaries
  - separates daily HRV from sleep HRV
  - separates daily minimum HR from resting HR
  - separates daily average HR from sleep average HR
  - records that no normalized RingConn tracker is currently active

- Updated `data/DATA_COVERAGE.md`:
  - distinguishes source-preserved wearable coverage from canonical structured coverage
  - registers the RingConn acquisition package
  - documents byte-preservation and fresh-ZIP verification
  - records actual sleep, activity, and vital-sign coverage
  - documents missing dates, multiple sessions, timestamp uncertainty, and provider anomalies
  - establishes periodic provider exports as the current operating model
  - classifies normalized wearable trackers as deferred rather than planned
  - confirms that the absence of normalized trackers is not a current coverage failure

- Updated `data/DATA_QUALITY_NOTES.md`:
  - registers the externally verified RingConn package
  - records exact row counts and file sizes
  - preserves correction candidates for DQ-001 through DQ-003
  - retains broader RingConn differences as diagnostic evidence
  - limits timestamp, multiple-session, missing-date, and anomaly issues to their applicable analyses
  - removes a full normalized wearable architecture as a prerequisite for narrow correction
  - defers comprehensive mapping until a concrete analytical need exists

- Updated `data/source_exports/ringconn/2026-07-21/README.md`:
  - records public filename normalization
  - records exact row counts and byte sizes
  - documents the `.gitattributes` protection
  - records checksum and fresh-GitHub-ZIP verification
  - documents privacy-screening results
  - defines source-versus-curated boundaries
  - establishes separate acquisition-date directories for later exports
  - defers normalized wearable datasets

- Replaced the previously proposed immediate wearable architecture:

  ```text
  Source exports
  → normalized wearable trackers
  → curated datasets
  ```

  with:

  ```text
  Periodic byte-preserved RingConn exports
  → acquisition README and checksums
  → targeted reconciliation or analysis when needed
  → optional reproducible derived layer when justified
  ```

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

- Expanded `methodology/data-collection.md`:
  - defines source hierarchy, transcription, provenance, units, timing, derivation, inference, missingness, and correction rules
  - separates collection from interpretation

- Expanded `methodology/anonymization.md`:
  - defines private originals, public originals, filename-normalized sources, and sanitized derivatives
  - distinguishes true removal from visual covering
  - requires hidden-text, metadata, annotation, and embedded-object review when applicable
  - defines checksum and changelog requirements
  - distinguishes current-tree, active-ref, historical-object, provider-side, and uncontrolled-copy remediation states
  - documents the completed July 2025 blood-panel privacy sequence
  - documents Git-history rewriting and fresh-clone requirements
  - documents correction of the Zenodo v1.0.0 package
  - documents RingConn privacy screening and filename normalization
  - retains GitHub provider-side cleanup as pending
  - prohibits claims of universal erasure

- Updated `snapshots/2025-07/2025-07 Epoch.md`:
  - identifies the blood PDF as a sanitized public derivative
  - documents the public/private source boundary
  - records the verified current checksum
  - records active Git branch and tag remediation
  - records current GitHub ZIP verification
  - records Zenodo v1.0.0 package remediation
  - discloses GitHub Support and uncontrolled-copy limitations
  - confirms that biological values and interpretation were unchanged

- Updated `VERSIONING.md`:
  - aligns versioning rules with actual repository practice
  - distinguishes ordinary commits from formal releases
  - defines patch, minor, and major release triggers
  - clarifies release-candidate use
  - documents privacy and integrity repair behavior
  - clarifies Zenodo archival cadence
  - confirms that routine weekly, audit, and source-export work does not automatically require a version increment

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

#### Public blood-artifact sanitization

- Replaced `snapshots/2025-07/2025-07-full-blood-panel.pdf` with a sanitized public derivative:
  - removes the full date of birth
  - removes patient and specimen identifiers
  - removes address and contact information
  - removes ordering-physician identity
  - preserves measured laboratory values
  - preserves units, reference intervals, flags, dates, and report structure
  - intentionally retains the subject’s public name and chronological age
  - preserves the artifact’s evidentiary role while reducing non-public administrative exposure

- Regenerated and verified the corresponding SHA-256 entry in:

  `snapshots/2025-07/checksums.txt`

- Verified public artifact SHA-256:

  `e3fe18d94b003217f2d9024ee1952117305f1b48dc72bebf183269ec60a375cb`

- Classified the replacement as:
  - privacy remediation
  - archive maintenance
  - source-preserving public sanitization
  - checksum-changing artifact replacement
  - not new biological evidence
  - not a protocol or phase event

#### Git-history and active-ref remediation

- Rewrote repository history to remove the prior blood-artifact path from historical commits.

- Restored the sanitized derivative and corresponding checksum to:
  - `main`
  - `v0.9.0`
  - `v1.0.0`
  - `v1.0.0-rc1`
  - `v1.0.0-rc2`

- Confirmed that:
  - the previously affected commits are not reachable from active rewritten refs
  - remote branches and tags match the rewritten local refs
  - current maintained refs contain the sanitized derivative
  - subsequent work is being performed from a fresh clone

- Historical commit hashes changed as a consequence of the privacy rewrite.

- Old clones containing pre-rewrite ancestry must not be merged or pushed back into the repository.

- Submitted a GitHub Support request concerning residual Git LFS or other provider-controlled objects.

- GitHub provider-side cleanup remains pending and must not be described as completed until direct confirmation is received.

#### Zenodo v1.0.0 remediation

- Rebuilt the DOI-bearing Zenodo v1.0.0 archive so that:
  - the sanitized blood-panel derivative replaces the prior artifact
  - the corrected snapshot checksum is included
  - the intended release inventory is preserved
  - unrelated release content remains unchanged

- Corrected package:

  `daniel-longitudinal-public-v1.0.0.zip`

- Verified corrected archive digests:

  - MD5: `4dd3838c5c1f90003e1c98d72fec812e`
  - SHA-256: `0c00fc1c7ea7a708d6fe6224c88fc33b6a4b853e6fbc127c88a0432b5bc8d330`

- Independently downloaded and verified the corrected Zenodo archive for:
  - expected archive structure
  - expected file inventory
  - presence of the sanitized derivative
  - internal checksum agreement
  - absence of unrelated archive differences

- Preserved:
  - DOI
  - release version
  - biological interpretation
  - protocol state
  - phase status

#### RingConn source-export byte preservation

- Identified that initial Git ingestion converted RingConn CSV line endings from CRLF to LF.

- Added `.gitattributes` protection for provider-source CSV files.

- Replaced the converted repository copies with the original downloaded bytes.

- Retained the original checksum manifest rather than regenerating hashes around transformed files.

- Verified original source sizes:

  - sleep export: 38,703 bytes
  - activity export: 8,171 bytes
  - vital-sign export: 16,059 bytes

- Verified the source files:
  - in the working tree
  - in the Git index
  - after commit
  - after push
  - through a fresh GitHub ZIP

- Closed the RingConn source-export byte-preservation blocker.

#### Other corrections

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

### Security and privacy status

- Controlled distribution remediation is complete for:
  - active GitHub `main`
  - applicable maintained Git tags
  - current GitHub repository ZIP
  - Zenodo v1.0.0 package

- Remaining limitation:
  - GitHub provider-side cleanup of residual or orphaned Git or Git LFS objects is pending support confirmation

- The project does not claim removal from:
  - prior uncontrolled clones
  - prior personal downloads
  - third-party mirrors
  - browser caches
  - search-engine caches
  - redistributed archives
  - other copies created before remediation

- Current classification:

  > Controlled distribution remediation completed, with GitHub provider-side cleanup pending and uncontrolled-copy limitations disclosed.

---

### Release status

- No release-version increment was made for:
  - privacy remediation
  - source-export preservation
  - documentation alignment
  - audit disposition
  - versioning-policy clarification

- Current release metadata remains:
  - version: `1.0.0`
  - release date: `2026-06-23`
  - DOI: `10.5281/zenodo.20815612`

- Records 041–044 remain:
  - open
  - unscored
  - unchanged in prediction wording

- Current protocol exposure and phase status remain unchanged.

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
