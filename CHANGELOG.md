# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### Added

#### Model Error 045 and August 12 governance

- Added Model Error record `045` to `data/model_error/model_error_gap_v1.csv`:
  - registration date `2026-08-12`
  - domain `autonomic_reconvergence`
  - model `gpt5.6-sol-subject-calibrated`
  - registered prediction `partial_reconvergence`
  - model type `subject_calibrated`
  - calibration state `pre`
  - flag `secondary`
  - prediction type `trajectory`
  - status `open`
  - preserves actual and error fields as blank before outcome evaluation

- Registered record 045 prospectively after retrospective closeout of the Week 31 autonomic-performance divergence.

- Preserved the temporal boundary between:
  - the observation that generated the prediction
  - the evidence permitted to score the prediction

- Defined the following as registration context only for record 045:

  ```text
  2026-W31
  2026-08-10
  2026-08-11
  2026-08-12
  ```

- Defined the admissible record 045 scoring window as:

  ```text
  2026-08-13 through 2026-08-16
  ```

- Explicitly excluded the following from record 045 scoring:
  - `2026-08-17` TruAge / TruHealth results
  - `2026-08-17` DEXA results
  - `2026-08-17` VO₂ max results
  - `2026-08-18` Bod Pod results
  - later August snapshot interpretation

- Added `methodology/open_prediction_evaluation_plan_045.md`:
  - preregisters the record 045 scoring rules before the admissible outcome window begins
  - defines W30 as the immediately preceding stronger autonomic reference state
  - defines W31 as the immediately preceding compressed autonomic state
  - defines partial reconvergence as recovery of at least half of the W31-to-W30 autonomic gap
  - fixes the favorable four-day mean thresholds at:
    - daily biomarker HRV `>= 59.7 ms`
    - sleep HRV `>= 65.3 ms`
    - resting heart rate `<= 49.2 bpm`
    - sleeping heart rate `<= 53.7 bpm`
  - requires at least three of four favorable autonomic threshold crossings
  - requires no multi-session functional regression
  - requires no recovery-driven protocol reduction or intervention
  - defines persistent-divergence failure
  - defines adverse functional-reconvergence failure
  - defines insufficient-evidence handling
  - defines missing-data handling
  - preserves daily biomarker HRV and sleep HRV as separate metrics
  - preserves resting heart rate and sleeping heart rate as separate metrics
  - prohibits cross-field substitution
  - preserves records 041–044 unchanged
  - excludes August 17–18 snapshot results
  - authorizes no protocol manipulation
  - authorizes no phase declaration
  - locks thresholds against outcome-driven revision

- Added `docs/audits/2026-08-12-wednesday-audit.md`:
  - audits pre-change package `daniel-longitudinal-public-main (2).zip`
  - records pre-change ZIP size `35,877,254 bytes`
  - records pre-change ZIP SHA-256 `2b5e7fbe2477fa512dd4419b0caf70e40e2d9ee70616afe47786341ecc6897c7`
  - records zero validator errors and two governed warnings
  - records pre-change mechanical repository `PASS`
  - records 179 files
  - records 126 Markdown files
  - records 739 internal Markdown references
  - records 11 CSV files
  - records 29 of 29 checksum entries passing
  - records canonical sleep continuity through `2026-08-09`
  - records 182 continuous canonical sleep rows
  - records weekly-report continuity through active `2026-W32`
  - reconciles Week 31 training and recovery metrics
  - preserves the Week 31 autonomic-performance divergence as retrospective evidence
  - documents the prospective rationale for record 045
  - documents record 045 thresholds and failure boundaries
  - documents record 045 independence from records 041–044
  - documents validator protection expansion through record 045
  - confirms no change to the August collection plan
  - confirms no change to the original 041–044 evaluation plan
  - confirms no protocol change
  - confirms no phase transition
  - confirms no biological-data correction
  - confirms no privacy-artifact change
  - confirms no release increment
  - records completed fresh-ZIP verification of `daniel-longitudinal-public-main (3).zip`
  - records post-change ZIP size `35,902,464 bytes`
  - records post-change ZIP SHA-256 `30d5e2fa5b8694981307102750ed9c107f581048bc213c5a4a464746a8d3d20d`
  - records post-change validator result of zero errors, two governed warnings, ten passes, and overall `PASS`
  - records extracted-directory validator result of zero errors, two governed warnings, nine passes, and overall `PASS`
  - records successful Python compilation of `tools/validate_repository.py`
  - records the verified post-change inventory of 181 files, 128 Markdown files, 760 internal references, 11 CSV files, 182 canonical sleep rows, 27 weekly reports, and 33 model-error records
  - confirms records 041–045 remain open and unscored
  - confirms record 045 protected actual and error fields remain blank
  - confirms 29 of 29 registered checksums pass
  - confirms RingConn source-byte and CRLF preservation
  - confirms release metadata remains aligned
  - confirms the original 041–044 evaluation plan remained unchanged
  - confirms the August snapshot collection plan remained unchanged
  - confirms the post-change delta consisted of exactly 2 added files, 9 changed files, and 0 removed files
  - confirms no unintended material file change was identified
  - closes the required post-change verification for the substantive 11-file August 12 governance batch

#### Weekly reporting

- Added retrospective closeout for `reports/2026-W31.md`:
  - records seven completed B1 and seven completed Load Integration sessions
  - records 385 B1 minutes and 315 Load Integration minutes
  - records 700 total formal training minutes
  - records approximately 21.14 miles of B1 aerobic work
  - records morning bodyweight averaging approximately 235.1 lb
  - records daily biomarker HRV averaging approximately 57.3 ms
  - records sleep HRV averaging approximately 60.1 ms
  - records resting heart rate averaging approximately 51.4 bpm
  - records sleeping heart rate averaging approximately 56.4 bpm
  - records total sleep averaging approximately 7 hours 39 minutes
  - records a broader autonomic recovery signal than W30, with lower HRV and higher heart-rate measures across multiple related fields
  - records that the autonomic pattern did not converge with pain, GI disruption, mood instability, training-initiation failure, impaired aerobic control, technical degradation, loss of grip, or protocol interruption
  - records trait-level pull-up execution across all four sets on `2026-08-04`
  - records automatic bar organization and full positional ownership on `2026-08-05`
  - records trait-level B1 and Load Integration execution on `2026-08-06`
  - records grip improvement without specialized intervention
  - records unsolicited external recognition of grip strength during final dead hangs
  - records high, owned, ambient Load Integration execution on `2026-08-08`
  - records ambient B1 followed by substantial yard work and trait-level Load Integration on `2026-08-09`
  - records spontaneous pull-up recognition, attempted technique replication, and direct side-by-side execution on `2026-08-09`
  - preserves external recognition and social comparison as qualitative naturalistic evidence rather than formal testing
  - preserves the autonomic-performance divergence as an observational carryforward question rather than creating a retrospective prediction
  - records candidate evidence relevant to Model Error records 041, 042, and 044
  - preserves records 041–044 as open and unscored
  - preserves Phase 2 status and the `Consolidation / lock-in observation` operating substate
  - preserves Phase 2D as undeclared

- Added initialization for `reports/2026-W32.md`:
  - defines the observation window as `2026-08-10` through `2026-08-16`
  - carries forward the standard B1 and Load Integration protocol unchanged
  - defines W32 as the final full ordinary observation week before the August 17–18 snapshot
  - prioritizes observation of whether the W31 multi-marker autonomic pattern rebounds, stabilizes, continues, or converges with functional change
  - preserves daily HRV, sleep HRV, resting heart rate, and sleeping heart rate as distinct evidence streams
  - continues observation of sleep continuity, subjective restoration, training initiation, aerobic control, perceived exertion, grip, positional control, pain, mood, GI state, and ordinary-life availability
  - preserves the W31 autonomic-performance divergence as an observational carryforward question
  - prohibits retrospective creation of a prediction from the W31 evidence window
  - retains grip as an observed local variable rather than a new training objective
  - prohibits specialized grip work, additional dead hangs, farmer’s carries, rice-bucket work, crushing-grip work, grip testing, and high-volume pull-up sessions
  - prohibits deliberate reproduction of the `2026-08-09` yard-work-plus-training or firefighter-comparison contexts
  - preserves distinctions among standard, ambient, background, partial trait-like, pseudo–trait-level, and fully trait-like execution
  - defines W32 as neither a taper, peak week, deliberate overload week, nor recovery experiment
  - prohibits snapshot-directed workload, bodyweight, hydration, HRV, or resting-heart-rate optimization
  - preserves ordinary training, nutrition, hydration, supplementation, sleep opportunity, recovery, and recreational conditions before the August snapshot
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

- Appended sleep observations for `2026-08-03` through `2026-08-09` to `data/sleep_longitudinal_v1.csv`:
  - extends canonical sleep coverage through `2026-08-09`
  - increases the canonical dataset to 182 continuous daily rows beginning `2026-02-09`
  - adds seven daily rows without a date gap
  - preserves total-sleep, deep-sleep, light-sleep, REM, awake-time, awakening-count, efficiency, HRV, sleeping-heart-rate, subjective-state, readiness, and sleep-tag fields
  - calculates sleep-stage percentages directly from recorded stage minutes divided by total sleep minutes
  - preserves the structured awakening counts from the contemporaneous sleep log
  - preserves awake-after-sleep-onset values from the nightly records without reconstructing unobserved values
  - preserves medium-confidence REM classifications across the W31 nights according to contemporaneous wearable and subjective evidence
  - preserves unusually low device-estimated REM where recorded without inferred replacement values
  - keeps daily biomarker HRV separate from sleep HRV
  - keeps daily heart-rate measurements separate from sleeping-heart-rate measurements
  - adds no interpolated, reconstructed, or silently repaired values
  - leaves the existing governed DQ-001 through DQ-003 findings unchanged

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
  - protected status of records 041–045
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
  - `2026-08-05`
  - `2026-08-12`

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

- Added `docs/audits/2026-08-05-wednesday-audit.md`:
  - audits `daniel-longitudinal-public-main (35).zip`
  - records ZIP SHA-256 `083a2014d86dab927222113fbffa8b39823f2097a3a2bf315780f6c90afabfb9`
  - confirms safe ZIP paths, coherent repository structure, and no zero-byte or exact duplicate files
  - confirms 124 Markdown files and 737 valid internal references
  - confirms all 11 CSV files parse with consistent row widths
  - confirms canonical sleep continuity through `2026-08-02`
  - reconciles W30 sleep metrics against the canonical sleep dataset
  - reconciles seven B1 sessions, seven Load Integration sessions, and 700 formal training minutes
  - confirms W30 closure and W31 initialization
  - confirms 29 of 29 registered checksums
  - confirms RingConn source-byte and CRLF preservation
  - confirms current privacy and release-metadata integrity
  - confirms records 041–044 remain open, unscored, and unchanged
  - confirms Phase 2 remains active, Phase 2D remains undeclared, and Phase 3 remains reserved
  - records direct RingConn source review of the July 31 HRV discrepancy
  - distinguishes July 31 daily-average HRV of `55 ms` from sleep HRV of `67 ms`
  - identifies the private workbook’s structured `56 ms` and narrative `68 ms` daily-HRV values as incorrect
  - authorizes correction of the W30 weekly daily-HRV average from `62.1 ms` to `62.0 ms`
  - confirms that the correction does not alter canonical sleep, weekly interpretation, prediction status, protocol state, phase status, or release metadata
  - records local validator result of zero errors, two governed warnings, and overall `PASS`

#### Public archive and navigation

- Added Zenodo DOI and citation support across `README.md`, `LATEST.md`, and `CITATION.cff`.

- Added `docs/OBSERVER_QUICKSTART.md` as a compact external evaluation path.

- Added a minimal `.gitignore` without excluding archival content.

---

### Changed

#### August 12 current-state and governance alignment

- Updated `reports/2026-W32.md`:
  - advances the open model-error set from records 041–044 to records 041–045
  - documents record 045 registration on `2026-08-12`
  - preserves Week 31 and August 10–12 as record 045 registration context only
  - defines August 13–16 as the sole record 045 scoring window
  - exposes the four fixed record 045 autonomic thresholds
  - documents functional-regression and recovery-intervention failure boundaries
  - excludes August 17–18 snapshot results from record 045 scoring
  - adds a dedicated record 045 model-error boundary
  - preserves records 041–044 independently
  - preserves ordinary representative-state execution
  - prohibits behavior manipulation intended to satisfy record 045
  - preserves Phase 2 and leaves Phase 2D undeclared

- Updated `LATEST.md`:
  - advances the current open model-error set to records 041–045
  - exposes record 045 as a secondary prospective autonomic-reconvergence trajectory probe
  - records the `2026-08-13` through `2026-08-16` scoring window
  - preserves Week 31 as the retrospective observation that generated the question
  - preserves August 10–12 as known registration context
  - exposes the separate record 045 evaluation plan
  - records the registered thresholds and support criteria
  - documents record 045 independence from records 041–044
  - preserves the August snapshot collection plan separately
  - preserves ordinary protocol behavior
  - preserves Phase 2D as undeclared

- Updated `INDEX.md`:
  - exposes `methodology/open_prediction_evaluation_plan_045.md`
  - advances the current open prediction set to records 041–045
  - preserves `methodology/open_prediction_evaluation_plan_041_044.md` as the original preregistered evaluation block
  - records the separate record 045 timing and evidence boundary
  - adds record 045 to the prediction-review flow
  - adds separate pre-snapshot record 045 evaluation flow
  - documents validator protection through record 045
  - preserves August 17–18 snapshot outcomes as inadmissible for record 045 scoring
  - preserves Phase 2, protocol, collection, privacy, and release boundaries

- Updated `methodology/README.md`:
  - indexes `open_prediction_evaluation_plan_045.md`
  - distinguishes the record 045 plan from the existing records 041–044 plan
  - records the record 045 registration date
  - records the August 13–16 admissible scoring window
  - records the fixed autonomic thresholds
  - records Week 31 and August 10–12 as registration context only
  - excludes August 17–18 snapshot results from record 045 scoring
  - documents the relationship between record 045 and records 041–044
  - documents validator protection through record 045
  - advances the current active methodology state to records 041–045 open and unscored
  - preserves the August collection plan as a separate governance artifact
  - preserves the physical protocol and phase state

- Updated `README.md`:
  - exposes both active prediction-evaluation plans
  - advances the current open model-error set to records 041–045
  - records record 045 as separately governed
  - records the August 13–16 scoring window
  - preserves Week 31 and August 10–12 as context only
  - excludes August 17–18 snapshot results from record 045 scoring
  - preserves the original 041–044 plan
  - preserves the August collection plan separately
  - adds the record 045 plan to navigation and governance links

- Updated `VERIFICATION.md`:
  - advances protected model-error documentation from records 041–044 to records 041–045
  - documents explicit rather than dynamically inferred open-record protection
  - documents that record 045 must remain open before its scoring window closes
  - documents preservation of the record 045 prediction
  - documents blank protected actual and error fields before scoring
  - links `methodology/open_prediction_evaluation_plan_045.md`
  - clarifies that the validator protects record state but does not score record 045

- Updated `tools/validate_repository.py`:
  - changes explicit protected model-error range from:

    ```python
    range(41, 45)
    ```

    to:

    ```python
    range(41, 46)
    ```

  - advances the validator pass-state message from:

    ```text
    041-044 remain open and unscored
    ```

    to:

    ```text
    041-045 remain open and unscored
    ```

  - retains explicit protected-record enumeration so an accidental premature status change cannot evade validation
  - introduces no dynamic scoring behavior
  - does not score predictions
  - does not modify source or biological data

#### Current-state alignment

- Updated `LATEST.md`:
  - marks `2026-W31` closed and `2026-W32` active
  - advances canonical sleep coverage through `2026-08-09`
  - records canonical sleep continuity at 182 daily rows
  - records the canonical operating substate as `Consolidation / lock-in observation`
  - records seven completed B1 and seven completed Load Integration sessions during W31
  - records 385 B1 minutes, 315 Load Integration minutes, and 700 total formal training minutes
  - records approximately 21.14 miles of B1 aerobic work
  - records W31 morning bodyweight averaging approximately 235.1 lb
  - records daily biomarker HRV averaging approximately 57.3 ms
  - records sleep HRV averaging approximately 60.1 ms
  - records resting heart rate averaging approximately 51.4 bpm
  - records sleeping heart rate averaging approximately 56.4 bpm
  - records total sleep averaging approximately 7 hours 39 minutes
  - advances the recovery posture from the isolated late-W30 HRV observation to a broader W31 multi-marker autonomic recovery pattern
  - records that the less favorable autonomic profile did not converge with demonstrated functional failure
  - records stronger candidate evidence for reduced operator overhead, positional ownership, grip consolidation, social-salience tolerance, and ordinary-life portability
  - preserves the W31 autonomic-performance divergence as an observational carryforward question rather than a retrospectively registered prediction
  - defines W32 as the final ordinary full observation week before the August snapshot
  - preserves representative-state behavior and prohibits tapering, peaking, or snapshot-directed optimization
  - carries Model Error records 041–044 forward unchanged
  - preserves Phase 2 status without declaring Phase 2D

- Updated `INDEX.md`:
  - advances the active weekly-report link from W31 to W32
  - identifies W31 as the most recent closed weekly report
  - advances canonical sleep coverage through `2026-08-09`
  - advances the index alignment date to `2026-08-10`
  - preserves records 041–044 as the current open prediction set
  - preserves the W31 autonomic-performance divergence as observational rather than retrospectively registered
  - aligns the temporal, reports, and structured-data sections with the current repository state
  - preserves central access to the August collection and prediction-evaluation plans
  - changes navigation and current-state representation only

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

- Updated `reports/2026-W31.md`:
  - replaces the active planning scaffold with a retrospective closeout
  - records seven completed B1 and seven completed Load Integration sessions
  - records 385 B1 minutes, 315 Load Integration minutes, and 700 total formal training minutes
  - records the W31 multi-marker autonomic recovery pattern
  - distinguishes autonomic recovery compression from demonstrated functional failure
  - records repeated ambient and trait-level execution
  - records stronger pull-up positional ownership and automatic bar organization
  - records grip improvement without targeted intervention
  - records naturalistic external-recognition and social-comparison evidence
  - records preserved execution after substantial same-day yard work
  - preserves external recognition as qualitative rather than physiological evidence
  - preserves the W31 autonomic-performance divergence as an observational carryforward question
  - creates no retrospective Model Error record
  - preserves the existing protocol without progression or preemptive reduction
  - preserves records 041–044 as open and unscored
  - preserves Phase 2 and the `Consolidation / lock-in observation` operating substate
  - declares no Phase 2D transition

- Added `reports/2026-W32.md` as the active observation report:
  - defines the observation window as `2026-08-10` through `2026-08-16`
  - carries forward standard B1 and Load Integration unchanged
  - prioritizes observation of the W31 autonomic-performance divergence
  - requires multi-domain convergence before recovery intervention
  - preserves grip as an observed variable without specialized training
  - prohibits deliberate reproduction of spontaneous portability or social-comparison events
  - prohibits tapering, peaking, deliberate overload, and snapshot-directed manipulation
  - preserves representative-state behavior through the final pre-snapshot week
  - links the committed prediction-evaluation and August collection plans
  - preserves records 041–044 as open and unscored
  - preserves Phase 2D as undeclared and Phase 3 as reserved and inactive

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

#### W30 July 31 daily-HRV transcription

- Corrected the July 31 daily-average HRV used by `reports/2026-W30.md`:

  ```text
  Private workbook structured value:
  56 ms

  Private workbook narrative value:
  68 ms

  Direct RingConn Vital Signs value:
  55 ms
  ```

- Direct RingConn source review separately confirmed:

  ```text
  July 31 sleep HRV:
  67 ms
  ```

- Preserved daily-average HRV and sleep HRV as distinct measurement fields.

- Corrected the W30 daily-biomarker HRV sequence to:

  ```text
  72, 72, 64, 57, 55, 57, 57
  ```

- Corrected the W30 weekly daily-biomarker HRV average:

  ```text
  62.1 ms
  →
  62.0 ms
  ```

- Classified the correction as:

  - source-backed
  - field-specific
  - semantically confirmed
  - narrow
  - traceable
  - non-interpretive
  - unrelated to the August outcome
  - not a canonical sleep correction
  - not a prediction revision
  - not a protocol or phase event

- The correction did not change:

  - July 31 sleep HRV
  - W30 sleep-HRV average
  - canonical sleep data
  - W30 training totals
  - W30 recovery interpretation
  - Model Error status
  - protocol exposure
  - phase status
  - release metadata

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
  Model Error records 041–045 open and unscored
  ```

- Current prediction-governance state:

  ```text
  Records 041–044:
  original preregistered evaluation plan remains binding

  Record 045:
  separately preregistered on 2026-08-12
  scoring window 2026-08-13 through 2026-08-16
  secondary trajectory prediction
  ```

- Current August collection-governance state:

  ```text
  Records 041–044 evaluation plan committed and binding
  Record 045 evaluation plan committed before its scoring window
  August collection plan committed and binding before outcome access
  Physical protocol unchanged
  ```

- Current validator model:

  ```text
  Local read-only validation
  Explicit protection of records 041–045
  Human semantic review
  GitHub Actions deferred
  ```

- Post-change verification state:

  ```text
  Core 2026-08-12 governance batch:
  verified from fresh GitHub ZIP

  Package:
  daniel-longitudinal-public-main (3).zip

  SHA-256:
  30d5e2fa5b8694981307102750ed9c107f581048bc213c5a4a464746a8d3d20d

  Validator:
  0 errors
  2 governed warnings
  PASS

  Intended delta:
  2 files added
  9 files changed
  0 files removed

  Unintended material changes:
  none identified
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
  - W31 retrospective closeout
  - W32 observation-window initialization
  - W31 canonical sleep append through `2026-08-09`
  - `LATEST.md` advancement from W31 to W32
  - `INDEX.md` advancement through W32 and sleep coverage through `2026-08-09`
  - preservation of the W31 autonomic-performance divergence as an observational question without retrospective prediction registration
  - prospective Model Error 045 registration
  - record 045 evaluation-plan preregistration
  - validator protection expansion through record 045
  - August 12 Wednesday audit
  - August 12 current-state and navigation alignment
  - August 12 post-change verification closure

- Current release metadata remains:
  - version: `1.0.0`
  - release date: `2026-06-23`
  - DOI: `10.5281/zenodo.20815612`

- Records 041–044 remain:
  - open
  - unscored
  - unchanged in prediction wording
  - governed by their original evaluation plan

- Record 045 remains:
  - open
  - unscored
  - secondary
  - prospectively bounded to `2026-08-13` through `2026-08-16`

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
