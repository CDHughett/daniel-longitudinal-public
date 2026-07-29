# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### Added

#### Weekly reporting

- Added retrospective closeout for `reports/2026-W29.md`:
  - records seven completed B1 and seven completed Load Integration sessions
  - records 107 minutes of structured timed aquatic exposure
  - records 807 total structured logged movement minutes
  - preserves additional ring-diving and underwater-swimming activity as narrative context outside the structured duration total
  - finds no coherent delayed recovery-floor failure after the high-density W28 window
  - preserves ordinary variation between standard, subtle trait-like, and stronger trait-like session expression
  - documents preserved execution after schedule displacement, yard work, concentrated repository work, and household maintenance
  - records the spontaneous 2026-07-24 conversational pull-up demonstration with controlled holds across multiple positions
  - records preserved training during the 2026-07-26 sanding, preparation, and painting workload
  - documents the one-day repository-update delay as an intentional household-priority adjustment rather than a governance failure
  - records repeated candidate evidence relevant to Model Error records 041, 042, and 044
  - preserves records 041–044 as open and unscored
  - preserves Phase 2 status without declaring Phase 2D

- Added initialization for `reports/2026-W30.md`:
  - carries forward the standard B1 and Load Integration protocol without progression
  - records the canonical active phase as `Phase 2 — Load Integration`
  - records the operating substate as `Consolidation / lock-in observation`
  - prioritizes observation for delayed effects after two consecutive full-density weeks
  - carries forward the 2026-07-26 household-maintenance workload as an unresolved recovery observation
  - preserves distinctions between ordinary, partial trait-like, and stronger trait-like execution
  - continues passive collection of reduced-overhead, divided-attention, cognitive-load, and ordinary-life portability evidence
  - prohibits manufacturing conversational, positional-hold, aquatic, schedule-compression, or household-work tests
  - preserves ordinary training, nutrition, recovery, and collection conditions before the August biological snapshot
  - links the active prediction-evaluation and snapshot-collection plans
  - preserves records 041–044 as open and unscored
  - preserves Phase 2D as undeclared and Phase 3 as reserved and inactive

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

- Appended sleep observations for `2026-07-20` through `2026-07-26` to `data/sleep_longitudinal_v1.csv`:
  - extends canonical sleep coverage through `2026-07-26`
  - adds seven continuous daily rows without a date gap
  - preserves sleep-stage, awake-time, awakening-count, efficiency, HRV, sleeping-heart-rate, subjective-state, readiness, and sleep-tag fields
  - preserves the low-confidence REM classification for `2026-07-21`
  - retains later medium-confidence REM classifications without inferred replacement values
  - keeps daily and sleep-tab cardiovascular measurements distinct
  - adds no reconstructed or silently repaired values

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

- Added `methodology/2026-08-snapshot-collection-plan.md`:
  - preregisters the August 17–18 biological and performance collection window before outcome access
  - records the planned TruDiagnostic, DEXA, VO₂ max, and Bod Pod schedule
  - preserves TruDiagnostic as the primary Model Error 043 domain
  - preserves May 2026 as the primary comparison baseline
  - classifies DEXA, VO₂ max, Bod Pod, bodyweight, recovery, and subjective state as supplemental evidence
  - defines representative-state fasting, hydration, training, supplementation, medication, sleep, and collection documentation
  - prohibits snapshot-directed protocol, nutrition, hydration, recovery, and workload manipulation
  - defines source-artifact, privacy-review, checksum, and structured-transcription requirements
  - defines missing, delayed, invalid, incomplete, rescheduled, and discordant-result handling
  - protects outcome-access, scoring, protocol, phase, and release boundaries
  - preserves records 041–044 as open and unscored
  - introduces no prediction, protocol, phase, biological-value, or release change

- Added Event 003 to `data/model_error/calibration_events_log.md` for initialization of the July–August prediction block.

#### Repository validation tooling

- Added `tools/validate_repository.py` as a local read-only repository validator.

- The validator supports:

  - extracted repository directories
  - downloaded GitHub ZIP packages
  - human-readable output
  - machine-readable JSON output
  - nonzero exit status for mechanical errors
  - governed warnings that do not invalidate the repository

- The validator checks:

  - required repository paths
  - zero-byte files
  - ZIP CRC and path safety
  - Markdown relative links
  - Markdown internal anchors
  - fenced-code balance
  - CSV parsing
  - CSV row widths
  - duplicate CSV headers
  - checksum manifests
  - canonical sleep continuity
  - governed DQ-001 through DQ-003 warnings
  - weekly-report continuity
  - active weekly-report count
  - model-error record continuity
  - protected status of records 041–044
  - release-metadata alignment
  - RingConn byte sizes
  - RingConn SHA-256 values
  - RingConn provider headers
  - RingConn row counts
  - RingConn CRLF preservation
  - the source-export `.gitattributes` rule

- The validator:

  - uses only the Python standard library
  - does not edit repository files
  - does not infer corrections
  - does not score predictions
  - does not normalize provider exports
  - does not replace human semantic review

- GitHub Actions validation remains deferred until the local validator demonstrates stability across repeated audit cycles.

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
  - `2026-07-25`
  - `2026-07-29`

- The July audits collectively:
  - verified repository structure, links, Markdown integrity, CSV parsing, checksums, report continuity, prediction continuity, and release metadata
  - identified targeted sleep-data, protocol-status, experiment-wording, governance-language, privacy, source-provenance, terminology, and validation-tooling issues
  - confirmed remediation where source evidence was sufficient
  - preserved unresolved source-reconciliation items without inferred correction
  - recognized administrative overhead as a repository-design concern
  - recommended shorter, delta-focused weekly reports and audits
  - identified repeatable mechanical checks suitable for local automation

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

- Added `docs/audits/2026-07-25-saturday-audit.md`:
  - confirms that the reviewed Saturday package was unchanged from the preceding verified closeout package
  - reconfirms ZIP safety and repository structure
  - reconfirms Markdown, CSV, checksum, artifact, privacy, report, prediction, and release integrity
  - reconfirms RingConn source-byte and CRLF preservation
  - confirms W29 remains active through its full observation window
  - confirms records 041–044 remain open, unscored, and unchanged
  - identifies phase-language hierarchy as the principal remaining documentation debt
  - identifies repeated mechanical audit work as suitable for a local validator
  - preserves the August collection plan as due before outcome access
  - recommends no canonical-data, privacy-artifact, source-export, protocol, prediction, or phase modification

- Added `docs/audits/2026-07-29-wednesday-audit.md`:
  - audits `daniel-longitudinal-public-main (30).zip`
  - records ZIP SHA-256 `a3a417035f2b580574b1adae3cffe24b89769a721a6039abc77679de91194453`
  - confirms safe ZIP paths, coherent repository structure, and no zero-byte or exact duplicate files
  - confirms 122 Markdown files and 670 valid internal references
  - confirms all 11 CSV files parse with consistent row widths
  - confirms canonical sleep continuity through `2026-07-26`
  - reconciles the W29 sleep-derived metrics against the canonical sleep dataset
  - confirms the 107-minute and 807-minute structured movement calculations
  - identifies the need to distinguish timed aquatic exposure from additional narrative aquatic activity
  - confirms 29 of 29 registered checksums
  - confirms RingConn source-byte and CRLF preservation
  - confirms current privacy and release metadata integrity
  - confirms records 041–044 remain open, unscored, and unchanged
  - confirms Phase 2 remains active, Phase 2D remains undeclared, and Phase 3 remains reserved
  - confirms the August collection plan is methodologically aligned and preregistered before outcome access
  - identifies the missing August collection-plan changelog entry
  - identifies collection-plan and validator discoverability improvements
  - recommends expansion of `methodology/README.md`
  - records local validator result of zero errors, two governed warnings, and overall `PASS`
  - recommends no canonical-data, source-export, privacy-artifact, prediction, protocol, phase, or release modification

#### Public archive and navigation

- Added Zenodo DOI and citation support across `README.md`, `LATEST.md`, and `CITATION.cff`.

- Added `docs/OBSERVER_QUICKSTART.md` as a compact external evaluation path.

- Added a minimal `.gitignore` without excluding archival content.

---

### Changed

#### Current-state alignment

- Updated `LATEST.md`:
  - marks `2026-W29` closed and `2026-W30` active
  - advances canonical sleep coverage through `2026-07-26`
  - records the canonical operating substate as `Consolidation / lock-in observation`
  - summarizes W29 training density, recovery posture, and cross-context execution
  - records that numerically softer recovery values did not form a coherent functional decline
  - preserves ordinary and below-peak session expression as a boundary against narrative inflation
  - records the 2026-07-24 conversational positional-control event as candidate evidence rather than a formal test
  - clarifies that the 107-minute aquatic figure represents structured timed exposure
  - preserves additional ring-diving and underwater-swimming activity as narrative context outside the structured total
  - records compatibility between formal training and the 2026-07-26 household-maintenance workload
  - identifies delayed effects after two consecutive dense weeks and the household-work day as the primary W30 observation question
  - documents that the normal Sunday repository update was intentionally delayed one day for household maintenance and resumed without loss of continuity
  - links the active evaluation plan and August collection plan
  - records that both plans were committed before outcome access and remain binding
  - removes wording implying that August collection-condition documentation remains due
  - carries Model Error records 041–044 forward unchanged
  - retains the August 2026 snapshot as the next major objective checkpoint
  - preserves Phase 2 status without declaring Phase 2D

#### Weekly report governance

- Updated `reports/2026-W27.md`:
  - closes the post-travel reintegration window
  - distinguishes daily biomarker HRV from sleep HRV
  - records divided-attention pull-up control and voluntary tempo modulation as candidate record 042 evidence
  - preserves Phase 2D as a possible retrospective classification rather than a current declaration

- Replaced the active W28 planning scaffold with a retrospective closeout:
  - emphasizes material change rather than repeating standing protocol details
  - separates verified metrics from interpretation
  - distinguishes internal fatigue from functional degradation
  - records source-confidence limitations and unresolved correction notes
  - carries only consequential observations into W29

- Updated `reports/2026-W29.md`:
  - clarifies that 107 minutes represents structured timed aquatic exposure
  - identifies the contributing 30-minute and 77-minute water-treading sessions
  - preserves approximately 30 minutes of ring diving and underwater swimming as contemporaneous narrative context
  - excludes the additional aquatic activity from the 107-minute structured aquatic total
  - excludes the additional aquatic activity from the 807-minute structured logged movement total
  - preserves all original weekly calculations, recovery interpretation, model-error evidence, and phase status

- Updated `reports/2026-W30.md`:
  - replaces parallel phase language with the canonical `Phase 2 — Load Integration` label
  - records `Consolidation / lock-in observation` as the operating substate
  - links the active prediction-evaluation and August collection plans
  - records both plans as committed and binding before outcome access
  - clarifies the W29 aquatic accounting carried into the starting state
  - adds an explicit phase boundary
  - preserves Phase 2D-type observations as candidate evidence only
  - preserves Phase 2D as undeclared and Phase 3 as reserved and inactive
  - introduces no midweek interpretation, prediction scoring, or protocol change

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

#### Phase and state governance

- Updated `PHASE_MAP.md`:
  - establishes canonical phase names
  - defines the active state as `Phase 2 — Load Integration`
  - defines consolidation and lock-in observation as operating substates within Phase 2
  - distinguishes phase, operating substate, candidate characteristic, transition evidence, and retrospective declaration
  - maps historical aliases without rewriting historical reports
  - treats Phase 2C as historical consolidation or lock-in shorthand rather than a separate canonical phase
  - reserves Phase 2D as a possible retrospectively declared Phase 2 substate
  - classifies Phase 2D-type observations as candidate evidence only
  - confirms that no Phase 2D or Phase 3 declaration has occurred
  - prohibits phase language from creating progression pressure

- Updated `STATE_TRANSITIONS.md`:
  - converts the file from a parallel phase-description document into a governed transition record
  - records Phase 0 baseline establishment
  - records the completed Phase 0-to-Phase 1 transition
  - records the completed Phase 1-to-Phase 2 transition
  - classifies Phase 2 consolidation and lock-in as an operating-substate change
  - records the possible Phase 2D boundary as open and undeclared
  - retains Phase 3 as reserved and inactive
  - avoids inventing unsupported exact transition dates
  - preserves historical terminology through aliases
  - defines required fields for future transition entries

- Expanded `docs/CONCEPTS.md`:
  - defines observation, telemetry, artifact, collection, archive, and interpretation layers
  - defines source state, provider source artifact, direct export, byte preservation, curated data, canonical data, and derived data
  - defines normalization, source precedence, source-backed correction, reconciliation, missingness, and analytical restrictions
  - defines prediction, model error, prediction auditing, closure, admissible evidence, concordance, UDI, calibration, and model correction
  - defines phase, operating substate, candidate characteristic, transition evidence, retrospective declaration, and historical alias
  - defines Phase 2C, Phase 2D-type characteristics, Phase 2D, and reserved phases
  - defines ambient execution, trait-like execution, operator overhead, movement optionality, portability, reintegration, recovery floor, and spare capacity
  - defines perturbation, naturalistic perturbation, representative state, sanitized derivatives, and controlled distribution remediation
  - aligns public-facing terminology with the current governance architecture

- Historical reports were not rewritten solely to enforce the newer canonical vocabulary.

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

#### Verification governance

- Expanded `VERIFICATION.md`:
  - distinguishes artifact verification from whole-repository validation
  - documents local-directory and ZIP validation
  - provides Windows, macOS, and Linux commands
  - documents machine-readable JSON output
  - defines exit-code behavior
  - separates `PASS`, `WARN`, and `ERROR`
  - documents expected governed warnings for DQ-001 through DQ-003
  - describes each validator check
  - retains manual SHA-256 verification instructions
  - documents temporal-anchor relationships
  - defines privacy-verification limitations
  - establishes a routine local verification workflow
  - identifies semantic questions that still require human review
  - keeps GitHub Actions deferred

- The verification model now distinguishes:

  ```text
  Artifact identity
  → repository mechanics
  → human semantic review
  → interpretation
  ```

- Local validation does not replace formal audits when a scheduled audit or material event requires one.

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

- Expanded `methodology/README.md`:
  - converts the file from a minimal placeholder into a methodology-directory guide
  - indexes active standing methodology
  - indexes the active evaluation plan for records 041–044
  - indexes the August snapshot collection plan
  - distinguishes standing methodology, preregistered evaluation plans, preregistered collection plans, retrospective notes, and historical or superseded methodology
  - defines active-status labels and file-header expectations
  - defines relationships among methodology, governance, protocols, reports, data, artifacts, schemas, audits, and validation
  - distinguishes `/methodology` from `/docs/methodology`
  - defines source, correction, preregistration, and interpretation boundaries
  - adds methodology file-naming, placement, linking, and maintenance guidance
  - records the active Phase 2, open prediction, and August collection-governance state
  - introduces no source, dataset, prediction, protocol, phase, or release change

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
  - confirms that routine weekly, audit, source-export, governance, and local-tooling work does not automatically require a version increment

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

- Updated `README.md`, `DATASET_OVERVIEW.md`, `docs/START_HERE.md`, and `docs/NEWCOMER_PATH.md` to:
  - clarify archive scope and environmental limitations
  - distinguish source artifacts, structured data, reports, snapshots, and predictions
  - expose data-quality, collection, protocol, experiment, audit, and prediction-evaluation paths
  - improve external navigation without duplicating methodology

- Updated `INDEX.md`:
  - exposes the active August collection plan
  - exposes the active evaluation plan for records 041–044
  - exposes `methodology/README.md` as the methodology-directory guide
  - exposes `tools/validate_repository.py` as the local read-only validator
  - distinguishes structured data from byte-preserved source exports
  - distinguishes collection plans from outcome evidence
  - adds dedicated August snapshot and repository-verification reading flows
  - expands the archive-structure table to include source exports and tools
  - records the current W30 active report and current Phase 2 governance posture
  - improves navigation and representation without altering evidence or interpretation

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

#### Phase-terminology ambiguity

- Removed the parallel interpretation of `Phase 2 — Lock-In Confirmation` as though it were a second canonical Phase 2.

- Clarified that:

  - `Phase 2 — Load Integration` remains the active canonical phase
  - consolidation and lock-in observation are operating substates
  - Phase 2C is historical shorthand
  - Phase 2D-type characteristics are candidate evidence
  - no formal Phase 2D declaration has occurred
  - Phase 3 remains reserved and inactive

- Preserved historical wording without rewriting prior weekly reports.

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

### Current governance and validation status

- Current canonical phase:

  ```text
  Phase 2 — Load Integration
  ```

- Current operating substate:

  ```text
  Consolidation / lock-in observation
  ```

- Current transition state:

  ```text
  Phase 2D undeclared
  Phase 3 reserved and inactive
  ```

- Current open prediction state:

  ```text
  Model Error records 041–044 open and unscored
  ```

- Current August collection-governance state:

  ```text
  Evaluation plan committed and binding
  Collection plan committed and binding before outcome access
  Physical protocol unchanged
  ```

- Current validator model:

  ```text
  Local read-only validation
  Human semantic review
  GitHub Actions deferred
  ```

- Current expected governed validator warnings concern:

  - DQ-001 awake-minute and awakening-count duplication
  - DQ-002 March 31 sleep-stage difference
  - DQ-003 April 2 sleep-stage difference

- These warnings do not authorize automatic correction and do not make the repository mechanically invalid.

---

### Release status

- No release-version increment was made for:
  - privacy remediation
  - source-export preservation
  - documentation alignment
  - audit disposition
  - phase-hierarchy alignment
  - terminology expansion
  - local validator addition
  - verification-guide expansion
  - versioning-policy clarification
  - August collection-plan preregistration
  - July 29 Wednesday audit
  - W29 aquatic-accounting clarification
  - W30 governance alignment
  - methodology-directory guide expansion
  - navigation and discoverability improvements

- Current release metadata remains:
  - version: `1.0.0`
  - release date: `2026-06-23`
  - DOI: `10.5281/zenodo.20815612`

- Records 041–044 remain:
  - open
  - unscored
  - unchanged in prediction wording

- Current protocol exposure remains unchanged.

- Current phase remains:

  ```text
  Phase 2 — Load Integration
  ```

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
