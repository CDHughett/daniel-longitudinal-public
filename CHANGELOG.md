# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### Added

#### August 23 catch-up audit and prediction-provenance review

- Added `docs/audits/2026-08-23-catch-up-audit.md` as a single retrospective catch-up audit covering the scheduled repository checkpoints missed on:
  - `2026-08-19`
  - `2026-08-22`

- Preserved the distinction between:
  - a scheduled audit checkpoint
  - an audit actually performed

- No backdated August 19 or August 22 audit was fabricated.

- The catch-up audit was performed on `2026-08-23` against:

  ```text
  Package:
  daniel-longitudinal-public-main (8).zip

  Size:
  40,120,282 bytes

  SHA-256:
  08828eda225717bddf2f9e5126c912d183eb935316ce7c29f2ed4c5e08dd023d
  ```

- The immediately preceding completed Saturday reference package remained:

  ```text
  Audit date:
  2026-08-15

  Size:
  35,904,925 bytes

  SHA-256:
  75ea980f1fe9b2507bf44f88a118f31af06934edca81ec24ed3e4a0ced920da1
  ```

- The catch-up audit identified the accumulated repository delta since the August 15 reference as:

  ```text
  Files added:
  8

  Files changed:
  14

  Files removed:
  0
  ```

- The change surface was consistent with the intervening August archive cycle, including:
  - W32 closeout
  - W33 initialization
  - canonical sleep extension
  - August physical-testing artifacts
  - August snapshot documentation
  - Model Error adjudications
  - Model Error 046 registration
  - UDI and calibration updates
  - validator changes
  - current-state documentation
  - archive navigation updates

- Recorded the fresh-ZIP validator result:

  ```text
  Errors:
  0

  Warnings:
  2

  Passes:
  10

  Result:
  PASS
  ```

- Recorded the extracted-directory validator result:

  ```text
  Errors:
  0

  Warnings:
  2

  Passes:
  9

  Result:
  PASS
  ```

- Recorded the current audited inventory:

  ```text
  Repository files:
  189

  Zero-byte files:
  0

  Exact duplicate hash groups:
  0

  Markdown files:
  131

  Internal Markdown references:
  813

  CSV files:
  11

  Registered checksum entries:
  33

  Canonical sleep rows:
  189

  Canonical sleep coverage:
  2026-02-09 through 2026-08-16

  Weekly reports:
  28

  Weekly range:
  2026-W06 through 2026-W33

  Active weekly report:
  2026-W33.md

  Model-error records:
  34

  Model-error range:
  013 through 046
  ```

- Confirmed current artifact readability:

  ```text
  Images:
  24 of 24 readable

  PDFs:
  7 of 7 readable

  PDF pages:
  115

  Encrypted PDFs:
  0
  ```

- Confirmed:
  - 33 of 33 registered checksums passing
  - canonical sleep continuity through `2026-08-16`
  - weekly-report continuity through active `2026-W33`
  - model-error continuity through record `046`
  - RingConn source-export preservation
  - release-metadata alignment
  - no newly introduced mechanical warning

- Preserved the existing governed sleep warnings:
  - DQ-001 awake-minute / awakening-count duplication
  - DQ-002 March 31 sleep-stage difference
  - DQ-003 April 2 sleep-stage difference

- Reviewed the August physical artifact layer and confirmed the registered artifacts remained readable and checksum-valid.

- Reconfirmed the August artifact digests:

  ```text
  Bod Pod:
  9c8e45cab3913503d89be8bf62ab489fe434382d3f633e961c070c9e22034717

  DEXA body composition:
  cabb344a66ca9044126e533241d7322c4f72d3c26a13e9fde8ebfc2330b5c3a1

  DEXA summary:
  6b624b80e60192536a965cf53914a9f648b40de13425d3b08822fc6a244311ac

  VO₂ summary:
  f6dd377ddd6537e530e86373ea096c0ea4895898e38156f32d73c985fac7bb2a
  ```

- Reconfirmed:
  - record 041 closure remained methodologically defensible
  - record 042 continued-adaptation closure remained methodologically defensible
  - record 043 correctly remained open
  - record 044 narrow governance-failure closure remained methodologically defensible
  - record 045 scoring remained supported
  - record 046 correctly remained open and unscored

- Independently rechecked the record 045 four-day means:

  ```text
  Daily biomarker HRV:
  63.5 ms

  Sleep HRV:
  71.25 ms

  Resting heart rate:
  46.5 bpm

  Sleeping heart rate:
  51.75 bpm
  ```

- Reconfirmed the record 045 threshold result:

  ```text
  4 of 4 favorable thresholds met
  ```

- Identified one narrow registration-provenance defect in record 045:
  - `calibration_state` had changed from `pre` to `post`
  - the original registered `Prediction:` narrative had been replaced by closure language rather than preserved and supplemented

- Classified the record 045 issue as:

  ```text
  governance-provenance correction
  ```

  rather than:

  ```text
  biological correction
  prediction rescoring
  ```

- Confirmed the defect did not alter:
  - record 045 prediction value
  - scoring window
  - registered thresholds
  - observed four-day means
  - supported outcome
  - error direction
  - records 041–044
  - record 046
  - canonical biological data
  - canonical sleep data
  - physical protocol
  - phase state
  - release metadata

- Identified the corresponding validator blind spot:
  - prospective `calibration_state` provenance was not protected after closure
  - preservation of the original registered prediction narrative was not mechanically enforced

- Authorized narrow validator hardening for records 041–046.

- Preserved W33 as active through the completion of `2026-08-23`.

- Preserved record 046 as open and unscored while the final day of its registered primary scoring window remained incomplete.

- Deferred the following until after complete Sunday evidence collection:

  ```text
  2026-W33 retrospective closeout

  2026-08-17 through 2026-08-23 canonical sleep append

  Model Error 046 scoring

  post-W33 LATEST advancement

  post-W33 INDEX advancement

  record 046-dependent UDI or calibration updates
  ```

- Catch-up audit disposition:

  ```text
  PASS WITH NARROW GOVERNANCE-PROVENANCE CORRECTION REQUIRED
  ```

#### August 18 Model Error 041, 042, and 044 adjudication

- Formally adjudicated Model Error records `041`, `042`, and `044` against their preserved preregistered evaluation rules in:

  `methodology/open_prediction_evaluation_plan_041_044.md`

- Closed Model Error record `041`:
  - domain `recovery_capacity`
  - registered prediction `stable`
  - prediction type `primary trajectory`
  - actual state `stable`
  - error direction `none`
  - outcome `supported`

- Record 041 closure preserves the observed July–August autonomic cost rather than treating the interval as physiologically cost-free.

- Record 041 nevertheless remained inside its registered recovery-capacity boundary because the observation interval did not produce the qualifying combination of:
  - unplanned recovery intervention
  - multi-session functional regression
  - persistent physiological suppression with the required functional or subjective deterioration

- Preserved the `2026-08-16` Load Integration omission as testing-directed rather than recovery-driven for record 041.

- The testing-directed omission therefore did not activate the record 041 recovery-intervention failure condition.

- Record 041 closure does not establish:
  - costless accumulation
  - unlimited recovery capacity
  - permanent autonomic normalization
  - absence of short-window physiological strain

- Closed Model Error record `042`:
  - domain `ambient_execution`
  - registered prediction `plateau`
  - prediction type `primary trajectory`
  - actual state `continued_adaptation`
  - error direction `under`
  - outcome `not supported`

- Record 042 was closed against the model after the preregistered qualitative-transition threshold was met across:
  - at least three separately dated qualifying observations
  - more than 14 calendar days
  - multiple contexts
  - no substantive explanatory protocol progression

- Qualifying record 042 evidence included:
  - voluntary tempo modulation
  - voluntary positional control
  - conversational divided attention
  - social-context execution
  - positional optionality
  - reduced preparation
  - reduced session salience
  - automatic bar contact
  - automatic movement initiation
  - automatic positional organization
  - automatic force control
  - automatic transitions
  - preserved movement quality under accumulated workload
  - preserved execution across differing short-window autonomic states

- Record 042 therefore identifies a model-underestimation event:

  ```text
  predicted:
  plateau

  observed:
  continued_adaptation
  ```

- Record 042 closure does not independently declare Phase 2D.

- Closed Model Error record `044`:
  - domain `protocol_governance`
  - registered prediction `preserved`
  - prediction type `primary state`
  - error direction `under`
  - outcome `not supported`
  - classification `narrow snapshot-directed governance deviation`

- Record 044 retained substantial evidence of successful governance across most of its observation window, including:
  - no forced training progression
  - no direct grip program
  - no high-volume pull-up test
  - no manufactured portability test
  - no recovery-driven reaction to isolated wearable values
  - no outcome-driven prediction rewriting
  - no premature Phase 2D declaration

- A separate preregistered snapshot-governance boundary was nevertheless activated by:

  ```text
  2026-08-16
  Load Integration intentionally withheld
  to preserve recovery before VO₂ testing
  ```

- The August 16 omission was:
  - intentional
  - testing-directed
  - not provider-required
  - not recovery-driven

- Because the August collection posture was intended to preserve representative-state biology rather than deliberately improve testing freshness, the omission conflicted with the registered snapshot-manipulation boundary.

- Record 044 therefore closed as not supported.

- The record 044 result does not establish:
  - broad protocol-governance collapse
  - biological harm
  - invalidity of the August snapshot
  - failure of record 041
  - failure of record 045
  - a measured biological consequence from the governance deviation

- Preserved the distinction between:

  ```text
  governance outcome
  ≠
  biological-effect inference
  ```

- Preserved Model Error record `043` as:
  - open
  - unscored
  - dependent on the pending primary TruDiagnostic provider-result domain

- Preserved Model Error record `045` as:
  - closed
  - supported
  - unchanged by the 041/042/044 adjudication

- Preserved Model Error record `046` as:
  - open
  - unscored
  - prospectively bounded to its existing unload/reload evaluation window

- Reduced the current open model-error set to:

  ```text
  043
  046
  ```

- Established the current recent closed set as:

  ```text
  041 — supported
  042 — not supported / continued adaptation
  044 — not supported / narrow snapshot-directed governance deviation
  045 — supported
  ```

- Preserved the original `open_prediction_evaluation_plan_041_044.md` artifact unchanged rather than rewriting its preregistered language after outcome access.

- Updated `data/model_error/udi_by_type_tracker.csv` for the newly eligible closed primary predictions.

- Updated primary state calibration to:

  ```text
  eligible closed primary state predictions:
  14

  concordant:
  11

  under:
  1

  over:
  2

  primary state concordance:
  11 / 14
  0.79
  ```

- Updated primary trajectory calibration to:

  ```text
  eligible closed primary trajectory predictions:
  3

  concordant:
  2

  under:
  1

  over:
  0

  primary trajectory concordance:
  2 / 3
  0.67
  ```

- Preserved point and range magnitude UDI values unchanged because records 041, 042, and 044 are state or trajectory predictions rather than eligible point or range magnitude predictions.

- The updated concordance values are calibration summaries rather than biological-success metrics.

#### August 18 snapshot collection and artifact integration

- Completed the physical portion of the August 2026 biological and performance snapshot across `2026-08-17` and `2026-08-18`.

- Added the final August VO₂ provider artifact:

  `snapshots/2026-08/2026-08-vo2-summary.pdf`

- Finalized the current August physical source-artifact set:

  - `2026-08-dexa-body-comp.jpg`
  - `2026-08-dexa-summary.jpg`
  - `2026-08-vo2-summary.pdf`
  - `2026-08-bodpod-cosmed.jpg`

- Completed privacy review of the August physical artifacts:
  - preserved declared public identity fields where applicable
  - removed the nonessential ethnicity field from the public Bod Pod derivative
  - preserved biological and performance measurements
  - identified no public administrative identifier requiring additional VO₂ sanitization

- Replaced the August snapshot checksum placeholder with a complete SHA-256 manifest covering all four current physical artifacts.

- Verified the August VO₂ artifact SHA-256 as:

  ```text
  f6dd377ddd6537e530e86373ea096c0ea4895898e38156f32d73c985fac7bb2a
  ```

- Confirmed repository artifact-integrity validation after August physical-source ingestion:
  - zero errors
  - two governed historical sleep warnings
  - 33 registered artifact entries across 11 checksum manifests
  - all registered artifact checksums passing
  - overall validator result `PASS`

- Updated `methodology/2026-08-snapshot-collection-plan.md` with the actual collection execution record while preserving the original preregistration.

- Recorded the `2026-08-17` collection sequence:

  ```text
  05:37
  TruDiagnostic collection

  07:55
  DEXA

  approximately 08:10
  VO₂ max
  ```

- Recorded the `2026-08-17` preparation context:
  - wake time approximately `05:15`
  - morning bodyweight `235.1 lb`
  - final meal approximately `19:00` on `2026-08-16`
  - no morning caloric intake
  - no morning fluid intake
  - no coffee or caffeine
  - no supplements
  - no medications before testing
  - mental state calm and normal to the recent trend
  - GI and stomach state calm
  - no pain
  - no sweating
  - no illness or mechanical signal
  - no unusual testing event
  - DEXA completed before VO₂

- Recorded the corresponding approximate fasting durations:
  - TruDiagnostic: `10 h 37 min`
  - DEXA: `12 h 55 min`
  - VO₂: `13 h 10 min`

- Preserved the `2026-08-16` Load Integration omission as an explicit collection-condition deviation:
  - B1 was completed
  - Load Integration was intentionally withheld to preserve recovery before VO₂ testing
  - the omission was not provider-required
  - the omission reduced normal protocol exposure relative to the preregistered representative-state objective
  - the deviation was retained rather than retroactively normalized
  - the deviation remained separately relevant to Model Error records 043 and 044 during collection logging
  - no Model Error 043 or 044 outcome was assigned from the deviation during collection logging

- Record 044 was subsequently adjudicated separately under the original registered governance rules.

- The subsequent record 044 outcome does not alter the factual collection log.

- Recorded the `2026-08-18` Bod Pod collection:
  - wake time approximately `05:15`
  - final meal approximately `19:00` on `2026-08-17`
  - no morning food
  - no morning fluid
  - no supplements
  - no medications before testing
  - no exercise before testing
  - Bod Pod start time `08:26`
  - tight boxer briefs
  - hair cap
  - approximate fasting duration `13 h 26 min`
  - thoracic gas volume predicted rather than directly measured
  - direct thoracic-gas-volume mask measurement not performed
  - no unusual testing event reported

- Preserved unavailable `2026-08-18` morning-report and wearable fields as `unknown` rather than retrospectively reconstructing them.

- Added:

  `snapshots/2026-08/2026-08 Epoch.md`

  as the August temporal anchor record.

- The August epoch:
  - records the physical collection window as complete
  - records the TruDiagnostic collection event
  - records TruDiagnostic provider results as pending
  - enumerates the current checksum-verified physical artifacts
  - preserves the actual August 17–18 collection geometry
  - preserves the testing-directed Load Integration deviation
  - distinguishes physical collection completion from interpretive completion
  - remains explicitly non-interpretive
  - creates no phase declaration
  - creates no model-error outcome

- Extended `EPOCH_INDEX.md` through the `2026-08` epoch.

- Extended `SNAPSHOT_LOG.md` through the August 2026 Phase 2 consolidation / testing-window capture.

- Preserved the August snapshot state as:

  ```text
  physical collection:
  complete

  physical source-artifact preservation:
  complete

  TruDiagnostic sample collection:
  complete

  TruDiagnostic provider results:
  pending

  complete August biological interpretation:
  pending
  ```

- Preserved Model Error 043 as open because its preregistered primary TruDiagnostic provider-result domain remains unavailable.

- No August DEXA, VO₂, Bod Pod, bodyweight, recovery, or subjective result was substituted for the pending Model Error 043 primary endpoint.

#### Model Error 046 and August 17 governance

- Closed Model Error record `045` after completion of its prospectively fixed `2026-08-13` through `2026-08-16` scoring window:
  - preserves registration date `2026-08-12`
  - preserves domain `autonomic_reconvergence`
  - preserves registered prediction `partial_reconvergence`
  - records status `closed`
  - records outcome `supported`
  - preserves the original prediction and scoring boundary without retrospective extension

- Recorded the final record 045 four-day means:

  ```text
  Daily biomarker HRV:
  63.5 ms

  Sleep HRV:
  71.25 ms

  Resting heart rate:
  46.5 bpm

  Sleeping heart rate:
  51.75 bpm
  ```

- Recorded the final threshold result:

  ```text
  4 of 4 favorable thresholds met
  ```

- Confirmed that record 045 also satisfied its registered functional conditions:
  - no multi-session functional regression
  - no recovery-driven protocol reduction or intervention

- Preserved the `2026-08-16` Load Integration omission as:
  - testing-directed
  - scheduled before `2026-08-17` DEXA and VO₂-max testing
  - not recovery-driven for purposes of record 045 scoring
  - still separately relevant to Model Error records 043 and 044 as an actual pre-snapshot collection-condition deviation

- Preserved record 045 as a completed calibration event rather than extending it into the later testing-withdrawal period.

- Added Model Error record `046` to `data/model_error/model_error_gap_v1.csv`:
  - registration date `2026-08-17`
  - domain `autonomic_unload_reload`
  - model `gpt5.6-sol-subject-calibrated`
  - registered prediction `reconvergence_persists_after_unload_reload`
  - model type `subject_calibrated`
  - calibration state `pre`
  - flag `secondary`
  - prediction type `trajectory`
  - status `open`
  - preserves actual and error fields as blank before outcome evaluation

- Registered record 046 prospectively as a separate question from record 045.

- Defined the record 046 evidence architecture as:

  ```text
  2026-08-17:
  registration context only

  2026-08-18 through 2026-08-19:
  descriptive unload / re-entry kinetics

  2026-08-20 through 2026-08-23:
  primary scoring window
  ```

- Preserved `2026-08-17` as context only because that date had already begun before record 046 registration.

- Preserved `2026-08-18` through `2026-08-19` as descriptive rather than primary scoring evidence.

- Reused the record 045 autonomic thresholds without recalibration:

  ```text
  Daily biomarker HRV >= 59.7 ms
  Sleep HRV >= 65.3 ms
  Resting heart rate <= 49.2 bpm
  Sleeping heart rate <= 53.7 bpm
  ```

- Defined record 046 support as:

  ```text
  at least 3 of 4 favorable autonomic thresholds
  across the 2026-08-20 through 2026-08-23 means

  AND

  no multi-session functional regression after reload

  AND

  no recovery-driven protocol reduction after normal training resumes
  ```

- Defined a transient post-VO₂-max autonomic disturbance as admissible contextual evidence that cannot independently fail record 046.

- Excluded the measured outcomes of the August biological and performance snapshot from record 046 scoring, including:
  - TruAge
  - TruHealth
  - TruDiagnostic
  - DEXA
  - VO₂ max
  - Bod Pod

- Added `methodology/open_prediction_evaluation_plan_046.md`:
  - preregisters the unload/reload persistence question
  - preserves record 045 as closed
  - preserves records 041–044 unchanged at registration
  - fixes the primary scoring window before it begins
  - preserves the record 045 thresholds for direct comparability
  - defines functional-regression and recovery-driven reload-reduction failure modes
  - defines insufficient-evidence handling
  - prohibits window shifting
  - prohibits threshold recalibration
  - prohibits use of biological snapshot outcomes for scoring
  - authorizes no new training protocol
  - authorizes no phase declaration

#### Week 32 closeout and Week 33 initialization

- Replaced the active Week 32 scaffold with retrospective closeout in `reports/2026-W32.md`:
  - closes the `2026-08-10` through `2026-08-16` observation window
  - records seven completed B1 sessions
  - records six completed Load Integration sessions
  - records 385 B1 minutes
  - records 270 Load Integration minutes
  - records 655 total formal training minutes
  - records approximately 21.14 miles of B1 aerobic work
  - records morning bodyweight averaging approximately 236.3 lb
  - records daily biomarker HRV averaging approximately 60.6 ms
  - records resting heart rate averaging approximately 48.4 bpm
  - records daily average heart rate averaging approximately 64.6 bpm
  - records sleep HRV averaging approximately 66.4 ms
  - records sleeping heart rate averaging approximately 54.1 bpm
  - records total sleep averaging approximately 7 hours 41 minutes
  - records time in bed averaging approximately 8 hours 19 minutes
  - records an early-week autonomic trough followed by spontaneous rebound while formal training remained available
  - records the `2026-08-11` transient lower-back perturbation
  - records same-day resolution of the lower-back event
  - records no persistent guarding or subsequent functional restriction
  - records preserved B1 and Load Integration availability
  - records no multi-session functional regression
  - records no recovery-driven protocol reduction
  - records the `2026-08-16` Load Integration omission as testing-directed
  - scores Model Error 045 as supported
  - preserves records 041–044 as open and unscored at Week 32 closeout
  - preserves Phase 2 and the `Consolidation / lock-in observation` operating substate
  - leaves Phase 2D undeclared

- Added `reports/2026-W33.md` as the active observation report:
  - defines the observation window as `2026-08-17` through `2026-08-23`
  - documents the August biological and performance snapshot
  - documents the temporary testing-related withdrawal from B1 and Load Integration
  - documents the planned return to normal two-session training on `2026-08-19`
  - preserves `2026-08-17` as record 046 registration context only
  - preserves `2026-08-18` and `2026-08-19` as descriptive unload and re-entry kinetics
  - fixes `2026-08-20` through `2026-08-23` as the primary record 046 scoring window
  - preserves the four record 046 autonomic thresholds
  - treats maximal VO₂ testing as a possible acute autonomic perturbation
  - excludes measured August snapshot outcomes from record 046 scoring
  - initially preserved records 041–044 as open and unscored pending their separate August snapshot-cycle adjudication
  - preserves record 045 as closed and supported
  - preserves record 046 as open and unscored
  - preserves Phase 2 status
  - preserves the `Consolidation / lock-in observation` operating substate
  - leaves Phase 2D undeclared

- The active W33 report was subsequently aligned after formal closure of records 041, 042, and 044.

#### Week 32 canonical sleep extension

- Appended sleep observations for `2026-08-10` through `2026-08-16` to `data/sleep_longitudinal_v1.csv`:
  - extends canonical sleep coverage through `2026-08-16`
  - increases canonical sleep continuity to 189 daily rows beginning `2026-02-09`
  - adds seven daily rows without a date gap
  - preserves total-sleep, deep-sleep, light-sleep, REM, awakening-count, efficiency, HRV, sleeping-heart-rate, subjective-state, readiness, and sleep-tag fields
  - calculates sleep-stage percentages from recorded stage minutes divided by total sleep
  - preserves daily biomarker HRV separately from sleep HRV
  - preserves resting and daily-average heart-rate measures separately from sleeping heart rate
  - preserves medium REM-confidence context
  - preserves the early-week autonomic disturbance and subsequent multi-night recovery pattern
  - preserves subjective-objective sleep-stage disagreement where contemporaneously reported

- Recovered the `awake_min` fields for two Week 32 nights from source timing components:
  - `2026-08-11`: `0 min`
  - `2026-08-12`: `22 min`

- Preserved the reconstruction basis as timing-derived rather than silently substituting another sleep field.

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
  - preserves records 041–044 as open and unscored at Week 31 closeout
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
  - preserves records 041–044 as open and unscored at initialization
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
  - preserves records 041–044 as open and unscored at registration
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
  - protected model-error state
  - protected prospective registration provenance
  - protected registered prediction narratives
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
  - `2026-08-23`

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
  - confirms records 041–044 remain open, unscored, and unchanged at that point
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
  - confirms records 041–044 remain open, unscored, and unchanged at that point
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
  - confirms records 041–044 remain open, unscored, and unchanged at that point
  - confirms Phase 2 remains active, Phase 2D remains undeclared, and Phase 3 remains reserved
  - records direct RingConn source review of the July 31 HRV discrepancy
  - distinguishes July 31 daily-average HRV of `55 ms` from sleep HRV of `67 ms`
  - identifies the private workbook’s structured `56 ms` and narrative `68 ms` daily-HRV values as incorrect
  - authorizes correction of the W30 weekly daily-HRV average from `62.1 ms` to `62.0 ms`
  - confirms that the correction does not alter canonical sleep, weekly interpretation, prediction status, protocol state, phase status, or release metadata
  - records local validator result of zero errors, two governed warnings, and overall `PASS`

- Added `docs/audits/2026-08-23-catch-up-audit.md`:
  - records the audit as performed on August 23 rather than backdating missed August 19 and August 22 checkpoints
  - audits `daniel-longitudinal-public-main (8).zip`
  - records ZIP size `40,120,282 bytes`
  - records ZIP SHA-256 `08828eda225717bddf2f9e5126c912d183eb935316ce7c29f2ed4c5e08dd023d`
  - compares the current state with the August 15 Saturday reference package
  - confirms zero validator errors
  - confirms two governed warnings
  - confirms overall mechanical `PASS`
  - confirms 189 files
  - confirms 131 Markdown files
  - confirms 813 internal Markdown references
  - confirms 11 CSV files
  - confirms 33 of 33 registered checksums passing
  - confirms canonical sleep continuity through `2026-08-16`
  - confirms 189 continuous canonical sleep rows
  - confirms weekly-report continuity through active `2026-W33`
  - confirms model-error continuity through record `046`
  - confirms August physical-artifact readability
  - confirms RingConn byte preservation
  - confirms release metadata alignment
  - reviews records 041–046 against their preserved governance boundaries
  - confirms record 045 scoring remained supported
  - identifies record 045 registration-provenance drift
  - identifies the validator blind spot that allowed that drift to pass mechanically
  - authorizes narrow record 045 provenance correction
  - authorizes validator hardening
  - preserves record 046 as open and unscored
  - preserves W33 as active
  - defers W33 closeout and record 046 scoring until complete August 23 evidence collection
  - records overall disposition `PASS WITH NARROW GOVERNANCE-PROVENANCE CORRECTION REQUIRED`

#### Public archive and navigation

- Added Zenodo DOI and citation support across `README.md`, `LATEST.md`, and `CITATION.cff`.

- Added `docs/OBSERVER_QUICKSTART.md` as a compact external evaluation path.

- Added a minimal `.gitignore` without excluding archival content.

---

### Changed

#### August 23 registration-provenance hardening

- Updated `data/model_error/model_error_gap_v1.csv` to restore the original registration provenance of Model Error 045.

- Corrected record 045:

  ```text
  calibration_state:

  post
  →
  pre
  ```

- Restored the original prospectively registered record 045 `Prediction:` narrative at the beginning of the `notes` field.

- Preserved the later record 045 closure narrative by appending it after the restored prospective prediction rather than replacing the original registration text.

- The repair preserves:

  ```text
  registered prospective prediction
  +
  retrospective closure
  ```

  as separate inspectable historical layers.

- Record 045 remains:

  ```text
  status:
  closed

  actual_value:
  partial_reconvergence

  error_absolute:
  0

  error_direction:
  none

  error_pct:
  0%
  ```

- The repair does not alter:
  - record 045 scoring window
  - record 045 thresholds
  - record 045 four-day means
  - record 045 supported outcome
  - records 041–044
  - record 046
  - UDI values
  - canonical biological values
  - canonical sleep values
  - protocol exposure
  - phase state
  - release metadata

- Updated `tools/validate_repository.py`:
  - preserves the existing protected open-record set of `043` and `046`
  - preserves the existing protected closed-record set of `041`, `042`, `044`, and `045`
  - continues protecting selected adjudicated actual values and error directions
  - adds explicit registration-provenance protection for records `041` through `046`
  - requires all prospectively registered records in that block to retain:

    ```text
    calibration_state = pre
    ```

  - treats `calibration_state` as registration metadata rather than a lifecycle field
  - prevents a prospectively registered prediction from changing from `pre` to `post` merely because it was later scored
  - stores the original registered prediction narrative for each protected record `041` through `046`
  - requires each protected `notes` field to begin with its original registered `Prediction:` narrative
  - permits later closure language to be appended after the registered prediction
  - detects removal, replacement, substantive mutation, or reordering of the protected registered prediction narrative
  - retains explicit rather than dynamically inferred protection so corrupted row contents cannot silently become the validator's own reference state
  - continues to avoid scientific rescoring
  - continues to avoid biological-data modification

- Updated `VERIFICATION.md`:
  - documents registration provenance as a mechanically protected archive property
  - documents `calibration_state=pre` protection for records 041–046
  - clarifies that a prospectively registered closed prediction remains historically `pre`
  - documents original registered prediction-narrative protection
  - documents that closure language may be appended but may not replace registered prediction wording
  - documents the August 23 record 045 provenance defect and restoration
  - clarifies the distinction between:
    - prediction registration state
    - prediction lifecycle status
    - retrospective adjudication
  - preserves records 043 and 046 as open/unscored
  - preserves records 041, 042, 044, and 045 as closed/adjudicated
  - introduces no prediction scoring or biological interpretation

- The registration-provenance hardening is intended to prevent future outcome adjudication from silently changing:

  ```text
  what was registered before the outcome
  ```

  into:

  ```text
  what was concluded after the outcome
  ```

- W33 closeout and record 046 scoring remain intentionally outside this remediation batch.

#### August 18 model-error closure and documentation alignment

- Updated `data/model_error/model_error_gap_v1.csv`:
  - closes record `041` as supported
  - records `actual_value=stable`
  - records `error_direction=none`
  - closes record `042` as not supported
  - records `actual_value=continued_adaptation`
  - records `error_direction=under`
  - preserves record `043` as open and unscored
  - closes record `044` as not supported
  - records the registered governance miss
  - records `error_direction=under`
  - preserves record `045` as closed and supported
  - preserves record `046` as open and unscored
  - reduces the current open model-error set to records `043` and `046`

- Updated `data/model_error/udi_by_type_tracker.csv`:
  - incorporates record 041 as a concordant eligible primary trajectory prediction
  - incorporates record 042 as an under-direction primary trajectory miss
  - incorporates record 044 as an under-direction primary state miss
  - updates primary state concordance to `11/14 = 0.79`
  - updates primary trajectory concordance to `2/3 = 0.67`
  - leaves point UDI unchanged
  - leaves range UDI unchanged

- Updated `tools/validate_repository.py`:
  - removes records `041`, `042`, and `044` from the protected open set
  - reduces the protected open set to records `043` and `046`
  - requires records `043` and `046` to remain open and unscored
  - requires their protected actual and error fields to remain blank before authorized closure
  - protects records `041`, `042`, `044`, and `045` as closed/adjudicated history
  - protects selected committed actual values and error directions for the closed set
  - detects accidental reopening or outcome-field drift
  - does not independently recompute or adjudicate the scientific correctness of the closures
  - does not score records 043 or 046
  - preserves model-error continuity through record 046

- Updated `LATEST.md`:
  - records 041 as closed / supported
  - records 042 as closed / not supported through continued adaptation
  - records 044 as closed / not supported through a narrow snapshot-directed governance deviation
  - preserves 045 as closed / supported
  - reduces the open model-error set to 043 and 046
  - preserves 043 as dependent on pending TruDiagnostic provider results
  - preserves 046 under its prospective unload/reload boundary
  - distinguishes the record 044 governance outcome from any unmeasured biological effect
  - preserves Phase 2
  - preserves the `Consolidation / lock-in observation` operating substate
  - leaves Phase 2D undeclared

- Updated `reports/2026-W33.md`:
  - removes obsolete treatment of 041, 042, and 044 as active Week 33 scoring questions
  - preserves their outcomes as closed historical context
  - records 041 as supported
  - records 042 as not supported through continued adaptation
  - records 044 as not supported through a narrow snapshot-directed governance deviation
  - preserves 045 as closed and supported
  - narrows active Week 33 model-error work to records 043 and 046
  - prohibits later Week 33 evidence from reopening or improving records 041, 042, 044, or 045
  - preserves the August 20–23 record 046 scoring window
  - preserves W33 as active through August 23
  - leaves Phase 2D undeclared

- Updated `README.md`:
  - reduces the current open prediction set to records 043 and 046
  - records recent closures 041, 042, 044, and 045
  - identifies record 042 as a model-underestimation event rather than a system failure
  - identifies record 044 as a narrow governance miss rather than a broad biological or protocol failure
  - records the August physical collection as complete
  - preserves the pending TruDiagnostic boundary for record 043
  - exposes current primary state and trajectory concordance
  - preserves formal Phase 2D as undeclared

- Updated `INDEX.md`:
  - reduces current open model-error references to 043 and 046
  - records 041, 042, 044, and 045 as closed
  - preserves `open_prediction_evaluation_plan_041_044.md` under its original filename as the preregistered source artifact
  - records 043 as the sole remaining open record under that original 041–044 framework
  - updates model-error, prediction-review, methodology, validation, snapshot, and current-archive navigation
  - records the updated state and trajectory concordance values
  - preserves the historical August 12 and August 17 index states as point-in-time documentation
  - leaves Phase 2D undeclared

- Updated `methodology/README.md`:
  - reclassifies `open_prediction_evaluation_plan_041_044.md` as a preserved preregistered multi-record artifact with one remaining open governed record
  - records 041 as closed and supported
  - records 042 as closed and not supported through continued adaptation
  - records 043 as open pending TruDiagnostic provider results
  - records 044 as closed and not supported through a narrow snapshot-directed governance deviation
  - preserves 045 as closed and supported
  - preserves 046 as active and prospective
  - distinguishes active, completed, and partially resolved preregistration states
  - records the August physical collection plan as collection-complete but still relevant to pending record 043 interpretation
  - updates validator-governance documentation
  - leaves the original preregistration files unchanged

- Updated `VERIFICATION.md`:
  - reduces the explicit protected open set to records 043 and 046
  - documents records 041, 042, 044, and 045 as protected closed/adjudicated history
  - documents selected protected actual values and error directions for those closed records
  - clarifies that validation protects committed governance state rather than independently scoring predictions
  - records the August physical artifact-verification state
  - preserves the pending record 043 primary-domain boundary
  - preserves the prospective record 046 boundary
  - retains the existing governed sleep warnings

- The current documentation hierarchy remains:

  ```text
  weekly reports:
  record what changed

  methodology:
  preserves standing and preregistered rules

  model-error layer:
  preserves prediction and scoring state

  LATEST:
  preserves broad executive synthesis

  README and INDEX:
  preserve observer-facing orientation and navigation

  VERIFICATION:
  protects mechanical and governance state
  ```

- No closed record was retroactively rewritten to make its prediction appear more accurate.

- No Phase 2D declaration was introduced by the 042 continued-adaptation finding.

- No biological consequence was inferred from the 044 governance miss.

#### August 18 current-state and physical-snapshot alignment

- Updated current documentation through completion of the August 17–18 physical collection window:
  - records DEXA, VO₂, and Bod Pod physical collection as complete
  - records the physical source artifacts as privacy-reviewed and checksum-verified
  - records the TruDiagnostic sample as collected on `2026-08-17` at `05:37`
  - preserves TruDiagnostic provider results as pending
  - exposes the August temporal epoch
  - records actual collection timing and preparation conditions
  - preserves the August 16 Load Integration omission as a testing-directed collection-condition deviation
  - preserves the planned `2026-08-19` return to standard B1 + Load Integration
  - distinguishes physical collection completion from complete August interpretation
  - preserves Model Error 043 as open pending its primary molecular domain
  - preserves Model Error 046 as open and prospective
  - preserves Phase 2 and the `Consolidation / lock-in observation` operating substate
  - leaves Phase 2D undeclared

- Refactored `reports/2026-W33.md` into a shorter evidence-centered active report before the later 041/042/044 closure alignment:
  - removes repeated methodology and prediction-history material already maintained in governed source files
  - retains the Week 32 handoff only where necessary for Week 33 interpretation
  - records the actual August 17–18 snapshot execution
  - records physical artifact status and pending TruDiagnostic status
  - preserves the August 16 testing-directed Load Integration omission
  - preserves the unload / reload observation geometry
  - retains record 046 thresholds and scoring-window boundaries
  - keeps the report active through `2026-08-23`
  - introduces no phase declaration

- The later August 18 model-error alignment subsequently replaced obsolete open-status language for records 041, 042, and 044.

#### August 17 current-state and governance alignment

- Updated `data/model_error/model_error_gap_v1.csv`:
  - closes record 045 as supported
  - populates the record 045 outcome
  - preserves record 045 historical scoring context
  - adds open record 046
  - extends model-error continuity through record 046
  - preserves records 041–044 unchanged at that point

- Updated `tools/validate_repository.py`:
  - protects records `041`, `042`, `043`, `044`, and `046` as open and unscored at that point
  - separately requires record `045` to remain closed
  - requires record 045 to retain a populated prediction
  - requires record 045 to retain a populated actual outcome
  - requires protected open records to retain blank outcome and error fields
  - extends model-error sequence continuity through record 046
  - updates validator pass messaging to distinguish the closed 045 record from the then-open prediction set
  - does not independently recompute or adjudicate the record 045 score
  - does not score record 046

- Updated `VERIFICATION.md`:
  - records Model Error 045 as closed/scored
  - preserves the record 045 prediction and recorded outcome as validator-protected history
  - clarifies that validation protects state but does not independently rescore record 045
  - protects records 041–044 and 046 as open and unscored at that point
  - requires blank outcome and error fields for active protected predictions
  - extends model-error continuity documentation through record 046
  - documents record 046 as a separate prospective unload/reload trajectory question

- Updated `methodology/README.md`:
  - records record 045 as a completed preregistered evaluation
  - preserves `open_prediction_evaluation_plan_045.md` as historical preregistration provenance
  - records record 045 as closed and supported
  - exposes `open_prediction_evaluation_plan_046.md`
  - records the record 046 registration date
  - records the descriptive and primary scoring windows
  - preserves the record 045 thresholds for record 046 comparability
  - excludes August snapshot outcomes from record 046 scoring
  - updates the then-active prediction set to records 041–044 and 046
  - preserves records 041–044 unchanged at that point
  - preserves Phase 2 and the `Consolidation / lock-in observation` operating substate

- Updated `LATEST.md`:
  - marks `2026-W32` closed
  - marks `2026-W33` active
  - advances canonical sleep coverage through `2026-08-16`
  - records Week 32 spontaneous autonomic reconvergence with preserved function
  - records Model Error 045 consistently as closed and supported
  - removes record 045 from the open prediction set
  - sets the then-open model-error set to records 041–044 and 046
  - exposes Model Error 046 as the active prospective unload/reload trajectory probe
  - records the August 17–18 testing-related formal training withdrawal
  - records the planned August 19 return to normal B1 + Load Integration
  - preserves the August 16 Load Integration omission as an explicit collection-condition deviation
  - preserves the original representative-state language rather than retroactively rewriting it
  - preserves records 043 and 044 as unresolved at that point
  - preserves Phase 2 and leaves Phase 2D undeclared

- Updated `INDEX.md`:
  - advances the active weekly report from W32 to W33
  - identifies W32 as the most recent closed weekly report
  - advances canonical sleep coverage through `2026-08-16`
  - removes record 045 from every current open-prediction reference
  - records record 045 as closed and supported
  - exposes the completed record 045 preregistration plan for provenance
  - exposes the active record 046 evaluation plan
  - sets the then-current open prediction set to records 041–044 and 046
  - documents the record 046 evidence boundaries
  - updates prediction-review, snapshot-review, methodology, and validation navigation
  - preserves the August testing-related exposure deviation
  - preserves Phase 2 and the `Consolidation / lock-in observation` substate

- Updated `README.md`:
  - records the active weekly window as `2026-W33`
  - records the then-current open model-error set as records 041–044 and 046
  - records record 045 as closed and supported
  - preserves the completed 045 evaluation plan for provenance
  - exposes the active 046 evaluation plan
  - documents the 046 evidence boundary
  - documents the temporary August testing-related withdrawal from formal training
  - preserves the August biological snapshot as separately governed from record 046
  - preserves Phase 2
  - preserves the `Consolidation / lock-in observation` operating substate
  - leaves Phase 2D undeclared

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
  - advances the then-current active methodology state to records 041–045 open and unscored
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
  - preserves records 041–044 as the then-current open prediction set
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
  - preserves records 041–044 as open and unscored at that time
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
  - preserves records 041–044 as open and unscored at that time
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
  - indexes the preregistered evaluation plan for records 041–044
  - indexes the August snapshot collection plan
  - distinguishes standing methodology, preregistered evaluation plans, preregistered collection plans, retrospective notes, and historical or superseded methodology
  - defines active-status labels and file-header expectations
  - defines relationships among methodology, governance, protocols, reports, data, artifacts, schemas, audits, and validation
  - distinguishes `/methodology` from `/docs/methodology`
  - defines source, correction, preregistration, and interpretation boundaries
  - adds methodology file-naming, placement, linking, and maintenance guidance
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

- Updated `methodology/open_prediction_evaluation_plan_041_044.md` before its outcome windows closed:
  - discloses observations already known at registration
  - confirms final trajectories and August outcomes remained unknown
  - distinguishes the primary TruDiagnostic endpoint from supplemental DEXA, VO₂ max, Bod Pod, bodyweight, and recovery evidence
  - defines the planned August 17–18 measurement window
  - preserves original thresholds and record status at that time

- After outcome access and formal adjudication, the preregistration artifact itself remains preserved unchanged.

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
  - exposes the August collection plan
  - exposes the preregistered evaluation plan for records 041–044
  - exposes `methodology/README.md` as the methodology-directory guide
  - exposes `tools/validate_repository.py` as the local read-only validator
  - distinguishes structured data from byte-preserved source exports
  - distinguishes collection plans from outcome evidence
  - adds dedicated August snapshot and repository-verification reading flows
  - expands the archive-structure table to include source exports and tools
  - improves navigation and representation without altering evidence or interpretation

---

### Fixed

#### Model Error 045 registration provenance

- Corrected a narrow registration-provenance defect identified during the `2026-08-23` catch-up audit.

- Record 045 had been prospectively registered on `2026-08-12` with:

  ```text
  calibration_state:
  pre
  ```

- During later closure, the row had incorrectly changed to:

  ```text
  calibration_state:
  post
  ```

- Restored the correct field state:

  ```text
  post
  →
  pre
  ```

- `calibration_state` is treated as registration metadata.

- It records whether a prediction was registered prospectively or retrospectively.

- It is not a lifecycle field and therefore does not change merely because a prediction has subsequently been scored or closed.

- Restored the original record 045 prospective `Prediction:` narrative from preserved preregistration evidence.

- Preserved the existing retrospective closure narrative by appending it after the restored registered prediction rather than replacing the registration text.

- The repaired row therefore preserves both:

  ```text
  what was predicted prospectively
  ```

  and:

  ```text
  what was concluded retrospectively
  ```

- Record 045 remains closed and supported.

- The correction did not change:

  - `prediction_value=partial_reconvergence`
  - `actual_value=partial_reconvergence`
  - `error_absolute=0`
  - `error_direction=none`
  - `error_pct=0%`
  - August 13–16 scoring window
  - registered autonomic thresholds
  - four-day scoring means
  - functional-regression assessment
  - recovery-driven-intervention assessment
  - records 041–044
  - record 046
  - UDI or concordance values
  - biological data
  - canonical sleep data
  - physical protocol
  - phase state
  - release metadata

- Classified the repair as:
  - source-backed
  - narrow
  - traceable
  - governance-provenance preserving
  - non-biological
  - non-scoring
  - non-interpretive

- The corresponding validator protection was expanded so the same class of drift cannot pass silently for the current preregistered block.

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

- Current weekly-report state:

  ```text
  2026-W32:
  closed

  2026-W33:
  active
  ```

- W33 remains active until the complete `2026-08-23` evidence set is available for retrospective closeout.

- Current canonical sleep state:

  ```text
  Continuous through 2026-08-16
  189 daily rows
  ```

- Current open prediction state:

  ```text
  Model Error 043:
  open / unscored

  Model Error 046:
  open / unscored
  ```

- Current recent closed prediction state:

  ```text
  Model Error 041:
  closed / supported

  Model Error 042:
  closed / not supported
  actual = continued_adaptation
  error direction = under

  Model Error 044:
  closed / not supported
  narrow snapshot-directed governance deviation
  error direction = under

  Model Error 045:
  closed / supported
  ```

- Current prediction-governance state:

  ```text
  Records 041–044 preregistration artifact:
  preserved unchanged

  Record 041:
  closed / supported

  Record 042:
  closed / not supported — continued adaptation

  Record 043:
  open / pending primary TruDiagnostic provider results

  Record 044:
  closed / not supported — narrow snapshot-directed governance deviation

  Record 045:
  registered 2026-08-12
  calibration_state = pre
  original prospective Prediction narrative preserved
  scoring window 2026-08-13 through 2026-08-16
  closed / supported
  original preregistered plan retained for provenance

  Record 046:
  registered 2026-08-17
  calibration_state = pre
  registration context 2026-08-17
  descriptive unload / re-entry 2026-08-18 through 2026-08-19
  primary scoring window 2026-08-20 through 2026-08-23
  open / unscored
  ```

- Current prediction-registration provenance state:

  ```text
  Protected prospective registration block:
  041–046

  Required calibration_state:
  pre

  Original registered Prediction narrative:
  protected

  Closure text:
  may be appended
  may not replace registered prediction text
  ```

- Current prediction-calibration state:

  ```text
  Primary state concordance:
  11 / 14
  0.79

  Primary trajectory concordance:
  2 / 3
  0.67

  Point UDI:
  unchanged

  Range UDI:
  unchanged
  ```

- Current August collection-governance state:

  ```text
  Records 041–044 evaluation plan:
  original preregistration preserved

  Records 041, 042, and 044:
  formally adjudicated

  Record 043:
  remains governed by the original plan
  pending primary TruDiagnostic evidence

  August collection plan:
  committed before outcome access
  execution conditions recorded after collection

  Record 045:
  completed under its independent preregistered boundary
  registration provenance restored and protected

  Record 046:
  separately preregistered before its primary scoring window
  remains open until complete scoring-window evidence is available

  2026-08-16:
  B1 completed
  Load Integration withheld before testing

  2026-08-17:
  no B1 / no Load Integration
  TruDiagnostic collected 05:37
  DEXA 07:55
  VO₂ approximately 08:10

  2026-08-18:
  no exercise before Bod Pod
  Bod Pod 08:26
  physical collection window complete

  2026-08-19:
  planned return to normal B1 + Load Integration

  Physical source artifacts:
  archived
  privacy-reviewed
  checksum-verified

  TruDiagnostic provider results:
  pending

  August interpretation:
  incomplete

  Underlying physical architecture:
  unchanged
  ```

- Current August physical artifact-layer validation state:

  ```text
  Errors:
  0

  Governed warnings:
  2

  Registered artifact entries:
  33 across 11 checksum manifests

  Registered artifact checksums:
  PASS

  Result:
  PASS
  ```

- Current validator governance model:

  ```text
  Local read-only validation

  Protected open / unscored:
  043
  046

  Protected closed / adjudicated:
  041
  042
  044
  045

  Protected registration provenance:
  041–046

  Required protected calibration state:
  pre

  Registered Prediction narratives:
  protected

  Human semantic review:
  required

  GitHub Actions:
  deferred
  ```

- The validator protects selected closed-record outcome state from accidental drift.

- The validator now also protects prospective registration provenance from accidental drift.

- It does not independently adjudicate whether the registered prediction outcomes were scientifically correct.

- The `2026-08-23` catch-up audit identified the record 045 provenance defect despite the pre-repair repository mechanically passing.

- This reinforces the repository distinction:

  ```text
  mechanical validation
  +
  human semantic audit
  ```

- The narrow record 045 remediation has been incorporated into the current change set.

- Final fresh-ZIP verification of the complete August 23 remediation batch remains pending until the changelog commit is complete.

- W33 closeout and Model Error 046 scoring remain deferred until the complete August 23 evidence set is collected.

- Completed final fresh-package verification for the August 17 repository update:

  ```text
  Package:
  daniel-longitudinal-public-main (2).zip

  Package size:
  35,936,521 bytes

  SHA-256:
  9d3318e6c7150b0392faa8963252288ad44d75e4c6309beb6ef30cf3712b4792
  ```

- Fresh-ZIP validator result:

  ```text
  Errors:
  0

  Governed warnings:
  2

  Passes:
  10

  Result:
  PASS
  ```

- Fresh-ZIP validation confirms the historical August 17 state:

  ```text
  ZIP safety:
  PASS

  Repository files:
  183

  Zero-byte files:
  0

  Markdown files:
  130

  Internal Markdown references:
  773

  CSV files:
  11

  Registered checksum entries:
  29 of 29 PASS

  Canonical sleep:
  189 continuous rows
  2026-02-09 through 2026-08-16

  Weekly reports:
  28 continuous reports
  W06 through W33

  Active report:
  2026-W33.md

  Model-error records:
  34 continuous records
  013 through 046

  Record 045:
  closed / scored

  Records 041–044 and 046:
  open / unscored at the August 17 verification point

  Release metadata:
  aligned

  RingConn source-export preservation:
  PASS
  ```

- The preceding fresh-package verification is retained as a point-in-time record of the August 17 repository state.

- Its `29 of 29` checksum count and records 041–044 open state are historical and are not rewritten after the August 18 artifact and prediction-closure changes.

- Independent extracted-directory validation also completed for the August 17 repository update:

  ```text
  Errors:
  0

  Governed warnings:
  2

  Passes:
  9

  Result:
  PASS
  ```

- The extracted-directory result independently confirmed the historical August 17 state:
  - required repository structure was present
  - 183 files were present
  - no zero-byte files were present
  - all 130 Markdown files passed target, anchor, and fence checks
  - all 11 CSV files parsed with consistent row widths
  - all 29 then-registered artifact checksums passed
  - canonical sleep was continuous through `2026-08-16`
  - weekly-report continuity extended through active `2026-W33`
  - model-error continuity extended through record 046
  - record 045 remained closed/scored
  - records 041–044 and 046 remained open/unscored at that point
  - release metadata remained aligned
  - RingConn source bytes, CRLF line endings, provider headers, and row counts remained preserved

- Final file-level comparison against the repository state that preceded the August 17 update confirmed:

  ```text
  Baseline files:
  181

  Updated files:
  183

  Added:
  2

  Changed:
  10

  Removed:
  0
  ```

- Added files:

  ```text
  methodology/open_prediction_evaluation_plan_046.md
  reports/2026-W33.md
  ```

- Changed files:

  ```text
  CHANGELOG.md
  INDEX.md
  LATEST.md
  README.md
  VERIFICATION.md
  data/model_error/model_error_gap_v1.csv
  data/sleep_longitudinal_v1.csv
  methodology/README.md
  reports/2026-W32.md
  tools/validate_repository.py
  ```

- No unintended file additions, removals, or material changes were identified in the August 17 verification package.

- Current governed validator warnings remain limited to:
  - canonical sleep-stage differences on `2026-03-31` and `2026-04-02`
  - DQ-001 awake-minute / awakening-count duplication on 14 historical dates

- These warnings:
  - were present before the August 17 update
  - remained present after August physical-artifact integration
  - do not authorize automatic correction
  - do not make the repository mechanically invalid
  - remain subject to their existing source-reconciliation rules

- The August 17 substantive repository update remains mechanically closed as:

  ```text
  PASS
  ```

- The August 18 physical-artifact layer separately passed local repository validation.

- The August 18 model-error closure and documentation batch has been incorporated into the current repository state.

- The August 23 catch-up audit and provenance-remediation batch now supersedes the prior pending verification posture for the next integrity checkpoint.

- Final fresh-package verification for the complete August 23 provenance-remediation batch remains pending after the current changelog commit.

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
  - W32 retrospective closeout
  - W33 observation-window initialization
  - W32 canonical sleep append through `2026-08-16`
  - Model Error 045 scoring and closure
  - Model Error 046 prospective registration
  - record 046 evaluation-plan preregistration
  - validator governance update for 045 and 046
  - verification-guide alignment for 045 and 046
  - methodology-directory alignment for 045 and 046
  - `LATEST.md` advancement from W32 to W33
  - `INDEX.md` advancement through W33
  - `README.md` current-state alignment
  - August 17 governance and navigation alignment
  - August 17 final fresh-package verification closure
  - August 18 VO₂ source-artifact ingestion
  - August 18 Bod Pod public-artifact privacy finalization
  - August physical checksum-manifest completion
  - August physical artifact-layer validation
  - August collection-plan execution logging
  - August temporal epoch creation
  - `EPOCH_INDEX.md` advancement through August 2026
  - `SNAPSHOT_LOG.md` advancement through August 2026
  - `LATEST.md` advancement through physical snapshot completion
  - W33 evidence-centered report compression
  - August 18 snapshot collection and documentation alignment
  - Model Error 041 formal adjudication and closure
  - Model Error 042 formal adjudication and closure
  - Model Error 044 formal adjudication and closure
  - primary state and trajectory concordance updates
  - validator protection transition from open 041–044 to closed 041/042/044
  - `LATEST.md` alignment with the 041/042/044 closure set
  - `reports/2026-W33.md` alignment with the 041/042/044 closure set
  - `README.md` alignment with the August model-error closure state
  - `INDEX.md` alignment with the August model-error closure state
  - `methodology/README.md` alignment with partially resolved 041–044 preregistration state
  - `VERIFICATION.md` alignment with the updated open and closed validator-protection sets
  - current `CHANGELOG.md` closure-state reconciliation
  - August 23 catch-up audit
  - Model Error 045 registration-provenance restoration
  - restoration of the original record 045 registered prediction narrative
  - validator protection of `calibration_state=pre` for records 041–046
  - validator protection of original registered prediction narratives for records 041–046
  - verification-guide prediction-provenance alignment
  - August 23 changelog provenance-remediation alignment

- Current release metadata remains:
  - version: `1.0.0`
  - release date: `2026-06-23`
  - DOI: `10.5281/zenodo.20815612`

- Record 041 is:
  - closed
  - supported
  - prospectively registered with `calibration_state=pre`
  - preserved under its original prediction wording
  - not interpreted as evidence of costless or unlimited recovery capacity

- Record 042 is:
  - closed
  - not supported
  - prospectively registered with `calibration_state=pre`
  - observed as `continued_adaptation`
  - classified as an under-direction model miss
  - not independently sufficient for a Phase 2D declaration

- Record 043 remains:
  - open
  - unscored
  - prospectively registered with `calibration_state=pre`
  - dependent on the pending TruDiagnostic provider-result domain
  - protected from substitution by supplemental August physical measurements

- Record 044 is:
  - closed
  - not supported
  - prospectively registered with `calibration_state=pre`
  - classified as a narrow snapshot-directed governance deviation
  - not interpreted as proof of biological harm or broad protocol failure

- Record 045 is:
  - closed
  - supported
  - prospectively registered with `calibration_state=pre`
  - preserved under its original prospective scoring boundary
  - original registered prediction narrative restored and protected
  - closure narrative retained after the registered prediction
  - excluded from later unload/reload evidence

- Record 046 remains:
  - open
  - unscored
  - secondary
  - prospectively registered with `calibration_state=pre`
  - prospectively bounded to its registered unload/reload evidence windows
  - not eligible for scoring until the complete August 23 scoring-window evidence is available

- Current open model-error set:

  ```text
  043
  046
  ```

- Current recent closed model-error set:

  ```text
  041
  042
  044
  045
  ```

- The underlying protocol architecture remains:

  ```text
  B1
  +
  Load Integration
  ```

- The August 16–18 reduction in formal training exposure is preserved as a temporary testing-related interruption rather than a newly declared recurring protocol.

- Current August snapshot status remains:

  ```text
  Physical collection:
  complete

  Physical artifacts:
  archived and checksum-verified

  TruDiagnostic sample:
  collected

  TruDiagnostic provider results:
  pending

  Complete snapshot interpretation:
  pending
  ```

- Current weekly archive state remains:

  ```text
  2026-W33:
  active through completion of 2026-08-23 evidence collection

  W33 retrospective closeout:
  pending

  August 17–23 canonical sleep append:
  pending

  Model Error 046 adjudication:
  pending
  ```

- Current phase remains:

  ```text
  Phase 2 — Load Integration
  ```

- Current operating substate remains:

  ```text
  Consolidation / lock-in observation
  ```

- Formal Phase 2D remains undeclared.

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
