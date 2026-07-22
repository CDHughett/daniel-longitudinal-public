# 2026-07-22 — Wednesday Audit

## Scope

Full Wednesday repository audit performed against:

- `daniel-longitudinal-public-main (22).zip`
- RingConn sleep export covering 2025-07-21 through 2026-07-21
- RingConn activity export covering 2025-07-21 through 2026-07-21
- RingConn vital-sign export covering 2025-07-21 through 2026-07-21

The audit follows:

- completion of the 2026-07-18 Saturday audit cycle
- retrospective closeout of `2026-W28`
- initialization of `2026-W29`
- extension of the canonical sleep dataset through 2026-07-19
- sanitization of the July 2025 blood-report artifact
- update of the corresponding checksum manifest
- acquisition of approximately one year of direct RingConn CSV exports
- continued observation of Model Error records 041–044
- continued preparation for the August 2026 biological and performance snapshot

This audit evaluates:

- repository structure
- file changes since the previous verified snapshot
- Markdown-link and anchor integrity
- CSV syntax and schema integrity
- longitudinal sleep continuity
- weekly-report continuity
- W28 closeout accuracy
- W29 initialization
- snapshot and checksum integrity
- privacy-remediation state
- changelog completeness
- model-error continuity
- prediction-governance preservation
- release-metadata alignment
- direct wearable-export structure
- overlap between direct exports and existing curated datasets
- historical wearable-data architecture
- source-preservation requirements
- normalization and schema strategy
- measurement-source governance
- anonymization methodology
- data-dictionary readiness
- release and versioning readiness
- priorities for the current repository-improvement cycle

---

## Verdict

**MECHANICAL PASS — PRIVACY DISTRIBUTION REMEDIATION AND WEARABLE-INGESTION GOVERNANCE REQUIRED**

The current repository snapshot remains structurally healthy, internally navigable, and suitable for continued W29 operation.

No evidence was found of:

- broken repository structure
- missing expected repository files
- unexplained file removal
- zero-byte files
- exact duplicate files
- broken relative Markdown links
- malformed CSV datasets
- schema-breaking row-width errors
- canonical sleep-date gaps
- duplicate canonical sleep dates
- checksum mismatch
- unreadable source artifacts
- weekly report discontinuity
- model-error sequence discontinuity
- contamination of records 041–044
- premature prediction closure
- protocol escalation
- premature phase declaration
- release-metadata mismatch

Two material governance issues require attention:

1. The current July 2025 blood PDF is sanitized and checksum-valid, but the privacy correction has not yet been fully documented or verified across all distribution surfaces.

2. The newly obtained RingConn exports require a governed source-preservation and normalization architecture before they are incorporated into the public longitudinal data layer.

The appropriate posture is:

- preserve the current curated datasets
- document the blood-artifact replacement
- distinguish public sanitized derivatives from privately retained originals
- verify prior Git and archival distribution separately
- preserve the direct RingConn exports as immutable source files
- create separate normalized longitudinal tables
- avoid silently overwriting contemporaneous wearable values with later provider exports
- define metric semantics before merging or reconciliation
- expand source, anonymization, quality, and data-dictionary documentation
- preserve all existing prediction, protocol, and phase boundaries

---

## Repository Comparison

The current repository snapshot was compared with the previously verified July 18 snapshot.

### Added

- `reports/2026-W29.md`

### Changed

- `CHANGELOG.md`
- `LATEST.md`
- `data/sleep_longitudinal_v1.csv`
- `reports/2026-W28.md`
- `snapshots/2025-07/2025-07-full-blood-panel.pdf`
- `snapshots/2025-07/checksums.txt`

### Removed

- none

### Unrelated drift

- none identified

The observed changes are consistent with:

- W28 closeout
- W29 initialization
- weekly sleep-data extension
- current-state dashboard advancement
- blood-artifact sanitization
- checksum renewal

---

## Repository Structure

### Result

PASS

Current repository inventory:

- 164 files
- 117 Markdown documents
- 8 repository CSV datasets
- 21 JPEG artifacts
- 6 PDF artifacts
- 9 checksum manifests

The three newly supplied wearable exports were audited separately and were not yet part of the repository snapshot.

No zero-byte repository files were identified.

No exact duplicate repository files were identified.

No unexplained structural change was identified.

Primary archive surfaces remain present:

- `/data`
- `/data/model_error`
- `/dashboards`
- `/docs`
- `/docs/audits`
- `/docs/methodology`
- `/experiments`
- `/methodology`
- `/protocols`
- `/reports`
- `/roadmap`
- `/schemas`
- `/snapshots`

The repository remains coherent as a governed archive.

---

## Markdown Validation

### Result

PASS

Current internal Markdown validation:

- 530 relative Markdown references checked
- 0 missing relative targets
- 0 unresolved internal anchors
- 0 references escaping the repository root
- 0 unbalanced Markdown code fences

The July 18 index and observer-navigation expansion introduced no link regression.

No navigation repair is required.

---

## Repository CSV Validation

### Result

PASS

All 8 repository CSV datasets parsed successfully:

- `data/biomarker_snapshot.csv`
- `data/bloodwork_longitudinal.csv`
- `data/epigenetic_longitudinal.csv`
- `data/sleep_longitudinal_v1.csv`
- `data/model_error/model_error_gap_v1.csv`
- `data/model_error/udi_by_type_tracker.csv`
- `data/model_error/historical/model_error_gap_reconstructed.csv`
- `snapshots/sleep_signal_core_v1.csv`

No malformed row widths were identified.

No structural correction is required.

---

## Canonical Sleep Dataset

### Result

PASS WITH EXISTING GOVERNED QUALITY ITEMS

Current canonical sleep dataset:

- path: `data/sleep_longitudinal_v1.csv`
- rows: 161
- date range: 2026-02-09 through 2026-07-19
- duplicate dates: 0
- missing dates inside the represented interval: 0
- columns: 18
- malformed rows: 0

The dataset now covers the complete W28 closeout interval.

No continuity correction is required.

### Existing quality items

The following previously documented issues remain:

#### DQ-001

From 2026-05-18 through 2026-05-31:

- `awake_min` equals `awakenings_count`
- the repeated equality remains suspicious
- the existing values remain unresolved
- no inferred correction is authorized

#### DQ-002

For 2026-03-31:

- sleep-stage total is 16 minutes below recorded total sleep

#### DQ-003

For 2026-04-02:

- sleep-stage total is 14 minutes below recorded total sleep

The newly obtained RingConn export contains potentially relevant source evidence for these dates.

That evidence should enter through a documented reconciliation process rather than immediate silent replacement.

---

## W28 Closeout Verification

### Result

PASS

The sleep-derived values reported for 2026-07-13 through 2026-07-19 reconcile with the canonical sleep dataset.

Verified averages:

| Metric | W28 average |
|---|---:|
| Total sleep | 480.6 minutes |
| Approximate total sleep | 8h01m |
| Deep sleep | 94.7 minutes |
| Approximate deep sleep | 1h35m |
| REM sleep | 61.0 minutes |
| Approximate REM sleep | 1h01m |
| Sleep HRV | 75.4 ms |
| Sleep average heart rate | 51.4 bpm |

The report correctly distinguishes these sleep values from:

- daily biomarker HRV: 68.1 ms
- resting heart rate: 45.1 bpm

No metric-substitution issue was identified.

The closeout also preserves:

- no protocol escalation
- no compensatory workload
- no forced recurrence of successful movement variations
- no premature scoring of records 041–044
- no Phase 2D declaration
- no claim that the dense weekly workload necessarily lacked delayed cost

No W28 correction is required.

---

## W29 Initialization

### Result

PASS

`reports/2026-W29.md` is present and active.

The report correctly uses the newer delta-focused weekly structure.

It carries forward:

- stable B1 execution
- stable Load Integration
- normal recovery monitoring
- August preparation
- open records 041–044
- restraint against proof-seeking progression
- distinction between available capacity and required workload
- retrospective weekly interpretation

The closeout remains incomplete as expected.

No W29 interpretation should be added before the observation window closes.

---

## Snapshot and Checksum Integrity

### Result

PASS

Current snapshot verification:

- 9 checksum manifests
- 26 checksum-listed artifacts
- 0 missing checksum-listed artifacts
- 0 SHA-256 mismatches

All repository JPEG and PDF artifacts were readable.

The updated July 2025 blood PDF matches the updated checksum in:

`snapshots/2025-07/checksums.txt`

No checksum repair is required.

Checksum validity confirms file identity.

It does not independently establish privacy completeness, clinical validity, or historical-distribution removal.

---

## July 2025 Blood Artifact

### Current-file result

PASS — CURRENT PUBLIC FILE SANITIZED

The current repository version of:

`snapshots/2025-07/2025-07-full-blood-panel.pdf`

retains the laboratory-result content while removing non-public administrative information.

The reviewed current file no longer exposes:

- full date of birth
- patient identifier
- specimen identifier
- address
- contact information
- ordering-physician identity

The following remain intentionally public:

- subject name
- chronological age
- biological measurement values

The current file contains a minor clipped footer fragment on page five.

This does not affect:

- measurement values
- interpretation
- subject privacy
- checksum integrity

It does not justify another artifact rebuild.

---

## Missing Blood-Artifact Changelog Entry

### Result

CORRECTION REQUIRED

The blood-report replacement and checksum update are not adequately documented in `CHANGELOG.md`.

The changelog should record that:

- the public July 2025 blood-report artifact was replaced with a sanitized derivative
- non-public administrative identifiers and contact information were removed
- the measured laboratory values were preserved
- subject name and chronological age remain intentionally public
- the associated checksum was regenerated
- the change was a privacy and archive-maintenance correction
- the replacement does not constitute new biological evidence

This is the clearest confirmed omission in the current repository state.

---

## Privacy Distribution Boundary

### Result

EXTERNAL VERIFICATION REQUIRED

A sanitized file in the current working tree does not by itself establish removal of prior file versions from:

- Git history
- forks
- clones
- caches
- previously downloaded archives
- DOI-bearing archival deposits

The ZIP snapshot contains no `.git` directory and therefore cannot verify whether an earlier sensitive binary remains retrievable through repository history.

The existing Zenodo `v1.0.0` deposit also predates the July 2025 blood-artifact replacement and requires direct inspection.

Required treatment:

- verify whether the earlier artifact exists in Git history
- verify whether the earlier artifact exists in the current Zenodo deposit
- preserve evidence of the verification
- perform distribution-level remediation when required
- avoid representing the privacy issue as fully resolved until those surfaces have been checked

This work is separate from ordinary repository documentation commits.

---

## Anonymization Methodology

### Result

EXPANSION REQUIRED

`methodology/anonymization.md` remains too minimal for the archive’s current maturity.

The repository has now performed a material public-artifact sanitization.

The methodology should define:

- private original
- public original
- public sanitized derivative
- redacted derivative
- permitted public identifiers
- prohibited public identifiers
- data-minimization principles
- visual redaction versus actual removal
- hidden text and metadata inspection
- image-layer and annotation inspection
- checksum renewal
- changelog requirements
- source-value preservation
- Git-history verification
- archival-release verification
- correction and disclosure procedure

The methodology should explicitly allow:

> A verified original may remain privately retained while the public archive contains a clearly identified sanitized derivative when privacy requires it.

The public derivative should remain:

- traceable
- source-preserving
- clearly labeled
- checksummed
- documented

---

## Snapshot-Epoch Documentation

### Result

ALIGNMENT REQUIRED

`snapshots/2025-07/2025-07 Epoch.md` should identify the public blood PDF as a sanitized derivative.

The epoch file should clarify that:

- the public PDF preserves the laboratory measurements
- administrative identifiers were removed
- the original source was verified before public replacement
- the public derivative is the current canonical public artifact
- sanitization did not alter the biological values

This prevents future observers from assuming that the public PDF is the untouched provider original.

---

# Direct RingConn Export Audit

## Source Files Reviewed

Three direct provider exports were reviewed:

- sleep export
- activity export
- vital-sign export

The files cover approximately one year beginning 2025-07-21.

The filenames contain a personal naming string.

The CSV contents themselves do not expose:

- date of birth
- email address
- street address
- patient identifier
- account identifier
- specimen identifier

Public repository copies should use stable provider-oriented filenames rather than the current downloaded names.

---

## Sleep Export

### Structural result

PASS WITH EPISODE-LEVEL AND TIMEZONE LIMITATIONS

The sleep export contains:

- 366 rows
- 358 unique wake dates
- coverage from 2025-07-21 through 2026-07-21

The file is episode-level rather than strictly daily.

Eight dates contain two sleep episodes:

- 2025-10-09
- 2025-11-02
- 2025-11-09
- 2025-11-17
- 2025-12-25
- 2026-05-31
- 2026-07-03
- 2026-07-04

These appear consistent with:

- an overnight sleep episode
- a secondary sleep or nap episode

The export contains no explicit provider field designating:

- primary sleep
- nap
- secondary sleep

No derived nap classification should be inserted without a registered transformation rule.

### Missing wake dates

The export contains no wake-date row for:

- 2025-08-10
- 2025-10-23
- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08
- 2026-01-09

These dates should remain missing.

No interpolation is authorized.

### Stage consistency

For 365 of 366 episodes:

- REM
- light
- deep

sum exactly to exported time asleep.

One secondary episode on 2025-11-17 reports:

- 98 minutes asleep
- 0 minutes REM
- 0 minutes light
- 0 minutes deep

This should be preserved as a provider-source anomaly.

It should not be repaired by inference.

### Sleep-ratio semantics

The exported sleep ratio appears to correspond closely to:

```text
time asleep ÷ elapsed time from Start Time to End Time
```

It should not be assumed to use only:

- Falling Asleep Time
- Wake-up Time

The provider field definition should remain documented as export-derived unless RingConn documentation confirms a different formula.

### Timestamp boundary

The timestamps contain no UTC offset.

The observation year includes travel and altered locations.

Therefore:

- timestamps should be preserved as local device or application time
- UTC conversion should not be attempted
- timezone should remain unknown or unresolved unless separately documented
- chronological ordering should preserve the exported timestamp text

---

## Activity Export

### Structural result

PASS

The activity export contains:

- 360 rows
- 360 unique dates
- coverage from 2025-07-21 through 2026-07-20

Missing dates:

- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08

The filename extends through 2026-07-21, but the final represented date is 2026-07-20.

This likely reflects export timing or an incomplete final day.

No July 21 activity row should be invented.

Observed value ranges:

- steps: 598 through 20,544
- calories: 2,233 through 5,087 kcal

The calories field should be preserved as:

```text
total_calories_kcal
```

unless provider documentation establishes a more specific meaning.

It should not be relabeled as active calories.

---

## Vital-Sign Export

### Structural result

PASS WITH METRIC-SEMANTIC RESTRICTIONS

The vital-sign export contains:

- 360 rows
- 360 unique dates
- coverage from 2025-07-21 through 2026-07-20

Its missing dates match the activity export:

- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08

All rows satisfy:

```text
minimum ≤ average ≤ maximum
```

for:

- heart rate
- SpO₂
- HRV

Observed ranges include:

- average heart rate: 51–77 bpm
- minimum heart rate: 34–51 bpm
- maximum heart rate: 81–179 bpm
- average HRV: 39–87 ms
- minimum SpO₂: 87–97%

### Required semantic boundaries

The exported metrics must not be substituted for differently defined tracked metrics.

Specifically:

- minimum heart rate is not automatically resting heart rate
- daily average heart rate is not sleep average heart rate
- daily average HRV is not sleep HRV
- daily minimum SpO₂ is not a clinical pulse-oximetry diagnosis
- daily provider summaries are not direct raw-sensor streams

Normalized field names should preserve the `daily_` scope.

---

# Existing Curated Sleep Data Versus Direct Export

## Result

MATERIAL SOURCE-STATE DIFFERENCES PRESENT

The current canonical sleep CSV and the direct RingConn sleep export overlap across 161 dates.

Across those overlapping dates:

- total sleep matches exactly on 110 dates
- deep sleep matches exactly on 115 dates
- REM matches exactly on 84 of 113 dates where both contain values
- efficiency matches on 48 of 99 comparable dates
- only 32 dates match across every comparable field

Some differences appear compatible with:

- rounding
- field-definition differences
- later provider processing
- historical algorithm recalculation
- contemporaneous screenshot versus later export state

Other differences are large enough to affect weekly summaries.

Example:

| Field | Curated value | Later direct export |
|---|---:|---:|
| Date | 2026-07-15 | 2026-07-15 |
| Total sleep | 453 min | 454 min |
| REM | 82 min | 92 min |
| Light | 236 min | 232 min |
| Deep | 135 min | 130 min |
| Efficiency | 90% | 87% |

Using the later export instead of the contemporaneous curated values would alter some W28 summary metrics.

That does not establish that the existing weekly report is wrong.

It establishes that the two source states should not be silently merged.

---

## Source-State Interpretation

The archive may now contain evidence of two legitimate measurement states:

### Contemporaneous state

Values observed and recorded near the original date through:

- screenshots
- manual transcription
- daily reports
- weekly closeout

### Later provider-export state

Values downloaded in July 2026 through:

- current RingConn export logic
- current provider database state
- possible provider recalculation
- possible software or algorithm changes

Both may be preserved.

Neither should silently overwrite the other.

---

## Existing W28 Metrics

The later export should not be used to rewrite W28.

For example:

- W28 curated sleep REM average: 61.0 minutes
- later export-derived REM average: approximately 62.4 minutes

Related daily metrics also remain semantically distinct:

- W28 daily biomarker HRV: 68.1 ms
- export daily average HRV over the same dates: approximately 66.6 ms
- W28 resting heart rate: 45.1 bpm
- export daily minimum heart rate over the same dates: approximately 39.9 bpm

These are related signals.

They are not interchangeable fields.

---

# Wearable Ingestion Recommendation

## Decision

**DO NOT APPEND THE ANNUAL EXPORT DIRECTLY INTO `data/sleep_longitudinal_v1.csv`.**

The current canonical sleep file is a curated, operator-enriched dataset.

It includes fields and context not present in the export, including:

- subjective morning state
- operator notes
- mental state
- sleep tags
- confidence annotations
- sleep average heart rate
- sleep HRV
- awakenings count
- one governed row per date

The RingConn sleep export is an episode-level provider source with:

- multiple rows on some dates
- no operator context
- no sleeping-heart-rate field
- no sleep-HRV field
- no awakenings-count field
- later provider-state values
- unresolved timezone context

The two files should remain distinct.

---

## Recommended Data Architecture

### Layer 1 — Immutable source exports

Create:

```text
data/source_exports/ringconn/2026-07-21/
```

Recommended files:

```text
ringconn-sleep-export.csv
ringconn-activity-export.csv
ringconn-vital-signs-export.csv
README.md
checksums.txt
```

The three exported CSV files should be preserved byte-for-byte.

Filename normalization is permitted.

File-content alteration is not.

The directory README should document:

- provider: RingConn
- export date: 2026-07-21
- requested export window
- actual coverage of each file
- device model
- known application version
- known firmware version
- direct-export status
- timestamp timezone limitation
- missing-date behavior
- multiple sleep episodes
- source-file checksum procedure
- public-filename normalization
- absence of inferred values

---

### Layer 2 — Normalized wearable datasets

Create three separate longitudinal datasets:

```text
data/wearable_sleep_sessions_v1.csv
data/wearable_activity_daily_v1.csv
data/wearable_vitals_daily_v1.csv
```

Do not combine them into one wide daily table.

Their row structures and metric semantics differ.

---

## Proposed Sleep-Session Schema

The normalized sleep table should remain one row per exported episode.

Recommended fields:

```text
session_id
sleep_date
start_local
end_local
fall_asleep_local
wake_local
sleep_ratio_pct
time_asleep_min
awake_stage_min
rem_min
light_min
deep_min
source_export_date
source_device
timezone_status
source_row
```

### Sleep normalization rules

- `sleep_date` means exported wake date.
- Each source row remains one normalized row.
- Duplicate wake dates remain separate sessions.
- Sessions are not labeled as naps without a registered rule.
- Original local timestamps remain unchanged.
- UTC offsets are not invented.
- Missing dates remain missing.
- The 2025-11-17 stage anomaly remains unchanged.
- `source_row` permits direct traceability.
- `session_id` should be deterministic and stable.
- No primary-sleep aggregation should occur in version 1.

A future derived daily table may be created only after rules are defined for:

- primary sleep
- nap classification
- cross-midnight episodes
- multiple sessions
- travel and timezone handling
- stage aggregation
- provider anomalies

---

## Proposed Activity Schema

Recommended fields:

```text
date
steps
total_calories_kcal
source_export_date
source_device
source_row
```

Rules:

- preserve one row per provider date
- preserve missing dates
- do not infer July 21
- do not relabel calories as active calories
- retain the direct source row

---

## Proposed Vital-Sign Schema

Recommended fields:

```text
date
daily_avg_hr_bpm
daily_min_hr_bpm
daily_max_hr_bpm
daily_avg_spo2_pct
daily_min_spo2_pct
daily_max_spo2_pct
daily_avg_hrv_ms
daily_min_hrv_ms
daily_max_hrv_ms
source_export_date
source_device
source_row
```

Rules:

- retain the `daily_` prefix
- do not map `daily_min_hr_bpm` to resting heart rate
- do not map `daily_avg_hr_bpm` to sleep average heart rate
- do not map `daily_avg_hrv_ms` to sleep HRV
- do not interpret SpO₂ fields clinically
- preserve missing dates
- retain direct row provenance

---

## Layer 3 — Curated and Interpreted Data

Preserve:

`data/sleep_longitudinal_v1.csv`

as the contemporaneous curated sleep layer.

Do not overwrite it with the later provider export.

A separate future reconciliation surface may compare:

- curated contemporaneous value
- later direct-export value
- field-definition compatibility
- magnitude of difference
- source date
- suspected provider reprocessing
- governing use case
- correction eligibility

Potential future file:

```text
data/reconciliation/ringconn_sleep_curated_vs_export_2026-07-21.csv
```

This should not be created until its rules are documented.

---

# Potential Resolution of Existing Sleep Quality Items

## March 31 and April 2

The direct export provides stage values that reconcile exactly with total sleep on both dates.

The observed differences correspond to:

- 2026-03-31: exported light sleep is 16 minutes higher
- 2026-04-02: exported light sleep is 14 minutes higher

This is strong candidate evidence that the current stage-sum deficits may reflect light-sleep transcription differences.

However, correction should wait until:

- source precedence is defined
- the direct export is preserved in the repository
- the measurement-source document identifies it
- the correction method is documented
- dependent summaries are reviewed

---

## May 18 Through May 31

The direct export contains plausible awake-stage values that do not duplicate awakenings count.

However, the existing field `awake_min` may not be semantically identical to RingConn’s exported:

`Sleep Stages - Awake(min)`

Potential differences may include:

- time awake across the full sleep interval
- stage-classified awake time
- time after sleep onset
- app-view field behavior
- export-field behavior

No correction should occur until the field semantics are established.

The current DQ-001 entry should remain open.

---

# Measurement-Source Governance

## Result

MATERIAL REVISION REQUIRED

`MEASUREMENT_SOURCES.md` does not yet adequately represent:

- direct provider exports
- screenshot-derived values
- manual transcription
- current versus historical provider state
- dated software-version intervals
- sanitized public derivatives
- private original retention
- measurement-field differences
- July 2026 RingConn exports

The next revision should define, for each source:

- source identifier
- provider
- device
- application version
- firmware version
- active date interval
- capture mode
- export date
- direct versus transcribed status
- public versus private artifact status
- known algorithm changes
- known comparability limitations
- source-precedence rules
- metric-specific interpretation boundaries

The file should no longer imply that all public artifacts are untouched originals.

It should permit clearly identified sanitized derivatives.

---

# Data Dictionary

## Result

EXPANSION REQUIRED AFTER SCHEMA APPROVAL

`DATA_DICTIONARY.md` currently provides incomplete coverage of the repository’s canonical fields.

Remaining work includes:

- most fields in `data/sleep_longitudinal_v1.csv`
- model-error register fields
- UDI tracker fields
- normalized sleep-session fields
- normalized activity fields
- normalized vital-sign fields
- source classification
- direct versus transcribed status
- missingness conventions
- units
- timezone status
- source-row provenance
- derived-field restrictions

The data dictionary should be expanded after the wearable schemas are approved.

This avoids defining fields that may immediately change.

---

# Versioning Policy

## Result

ALIGNMENT STILL DUE

`VERSIONING.md` does not match current repository practice.

The current language implies formal releases for ordinary weekly reports and major-version changes for routine governance or schema work.

The archive’s actual operating pattern is closer to:

- ordinary commits for continuous data and documentation work
- weekly closeouts without formal release tags
- patch releases for material corrections to an existing published artifact cycle
- minor releases for new integrated biological or performance snapshot cycles
- major releases for incompatible architecture or schema changes
- Zenodo deposits for intentional archival versions

This should be aligned before the August release is selected.

No release increment is required merely because the policy is being corrected.

---

# Model-Error Layer

## Result

PASS

Primary records remain continuous from:

- record 013

through:

- record 044

Historical reconstructed records 001–012 remain separate.

Records 041–044 remain:

- open
- unscored
- unchanged in prediction wording
- blank in actual-value fields
- blank in error fields
- protected by the registered evaluation plan

No new wearable-derived prediction should be added merely because more historical data are now available.

No UDI update is warranted.

---

## Record 041

Recovery-capacity observation remains active.

The added historical wearable exports may later support baseline and context analysis.

They do not close the current July–August window.

---

## Record 042

Candidate evidence remains open.

The exports do not independently establish:

- reduced operator overhead
- divided-attention movement control
- portability
- trait-level execution

Record 042 remains dependent on contemporaneous performance observations and its registered repetition threshold.

---

## Record 043

The August biological-snapshot record remains unchanged.

The new wearable exports may provide broader supporting context.

They do not alter:

- primary TruDiagnostic endpoint
- May comparison baseline
- magnitude rules
- primary-versus-supplemental domain hierarchy
- collection-condition requirements

---

## Record 044

Repository expansion does not constitute protocol progression.

Governance remains preserved if:

- data import does not change physical behavior
- the archive does not chase more favorable August outcomes
- no new intervention is introduced
- predictions remain unchanged
- historical values are not rewritten for coherence

---

# Findings

## Finding 1 — Repository Mechanics Remain Strong

The archive passed:

- structure review
- link validation
- Markdown-fence validation
- CSV parsing
- canonical sleep continuity
- checksum verification
- artifact readability
- weekly report continuity
- model-error continuity
- release-metadata review

No mechanical repository repair is required.

---

## Finding 2 — The Blood Artifact Is Correct in the Current Tree

The current public PDF is materially sanitized and checksum-valid.

The remaining work concerns:

- documentation
- distribution history
- archive-release verification
- anonymization methodology

It is no longer primarily a file-editing problem.

---

## Finding 3 — The Blood Replacement Is Missing From the Changelog

The replacement and checksum renewal should be documented before the privacy-remediation sequence is considered internally complete.

---

## Finding 4 — Privacy Correction Must Be Evaluated Across Distribution Surfaces

Current-tree replacement does not prove removal from historical repository or archival-release surfaces.

Those surfaces require separate verification.

---

## Finding 5 — The RingConn Exports Are Valuable Primary Evidence

The exports provide:

- broad historical coverage
- direct provider-origin data
- activity and vital-sign domains not currently represented as canonical longitudinal tables
- candidate evidence for existing sleep-quality questions
- a stronger basis for future automated analysis

They should be preserved.

---

## Finding 6 — The Exports Are Not Compatible With Direct Append Into the Curated Sleep Table

The direct sleep export and existing sleep CSV differ in:

- row grain
- metric availability
- source state
- timestamps
- duplicate dates
- operator context
- sleep HRV
- sleep heart rate
- awakenings
- subjective fields
- historical recalculation behavior

Direct append would blur source and interpretation layers.

---

## Finding 7 — The Correct Architecture Is Source, Normalized, and Curated

The repository should distinguish:

1. immutable direct exports
2. normalized provider-faithful datasets
3. curated contemporaneous interpretation datasets

This creates a stronger long-term data architecture than forcing all values into one table.

---

## Finding 8 — Later Provider Exports May Differ From Contemporaneous App Values

The differences are important evidence.

They may indicate:

- algorithm change
- retrospective recalculation
- export-specific transformation
- app-field variation
- rounding behavior

They should be preserved and studied rather than erased through reconciliation.

---

## Finding 9 — Existing Sleep Quality Items May Become Source-Resolvable

The March and April discrepancies now have strong candidate source evidence.

The May awake-field issue remains semantically ambiguous.

Corrections should be performed only after methodology and source precedence are defined.

---

## Finding 10 — Source and Field Semantics Must Precede Analysis

Daily, resting, sleep, average, minimum, and stage-derived metrics must remain distinct.

The archive should never equate:

- minimum HR with resting HR
- daily average HR with sleep average HR
- daily average HRV with sleep HRV
- daily minimum SpO₂ with a clinical measure
- later export values with contemporaneous app values without disclosure

---

## Finding 11 — Measurement and Anonymization Documentation Are Now Operationally Necessary

These are no longer optional placeholders.

The archive now contains:

- public sanitized derivatives
- privately retained originals
- direct provider exports
- manual transcription
- multiple source states
- field-level comparability questions

The documentation must catch up with actual practice.

---

# Recommended Commit Sequence

Proceed one file and one commit at a time.

## 1. Add This Wednesday Audit

File:

`docs/audits/2026-07-22-wednesday-audit.md`

Purpose:

- preserve the current verified repository baseline
- document the blood-artifact privacy state
- document the changelog omission
- preserve the wearable-export audit
- define the ingestion architecture
- distinguish immediate work from later normalization and correction

Suggested commit:

```text
docs(audit): add 2026-07-22 Wednesday audit
```

---

## 2. Add the Missing Blood-Artifact Changelog Entry

File:

`CHANGELOG.md`

Record:

- sanitized public blood-report replacement
- removal of non-public identifiers
- preservation of laboratory values
- intentional retention of name and age
- checksum regeneration
- privacy-maintenance classification

Suggested commit:

```text
docs(changelog): record blood artifact sanitization
```

---

## 3. Expand Anonymization Methodology

File:

`methodology/anonymization.md`

Purpose:

- define public sanitized derivatives
- define private-original retention
- establish redaction and verification procedure
- require metadata and hidden-text inspection
- define checksum and changelog requirements
- address Git-history and archival-release verification

Suggested commit:

```text
methodology: define public artifact sanitization rules
```

---

## 4. Align the July 2025 Epoch Record

File:

`snapshots/2025-07/2025-07 Epoch.md`

Purpose:

- identify the blood PDF as a public sanitized derivative
- preserve source-value integrity
- state that administrative identifiers were removed
- distinguish the public file from the privately retained original

Suggested commit:

```text
docs(snapshot): identify sanitized blood panel derivative
```

---

## 5. Align Measurement Sources

File:

`MEASUREMENT_SOURCES.md`

Purpose:

- register direct export, screenshot, and transcription modes
- permit sanitized public derivatives
- add date-aware source intervals
- add RingConn export provenance
- distinguish daily and sleep metrics
- document version and comparability uncertainty

Suggested commit:

```text
methodology: align measurement source provenance
```

---

## 6. Verify External Privacy Distribution

This is not an ordinary repository documentation commit.

Verify:

- prior Git objects
- GitHub history exposure
- current Zenodo `v1.0.0` contents
- other intentional public mirrors

Document the result separately.

Do not declare full distribution remediation complete until verification is finished.

---

## 7. Add the RingConn Source-Export Directory

Directory:

```text
data/source_exports/ringconn/2026-07-21/
```

Initial file:

`README.md`

Purpose:

- register the direct export event
- document actual coverage
- define file naming
- identify timestamp and timezone limitations
- define byte-preservation rules
- record missing-date behavior

Suggested commit:

```text
data(ringconn): add 2026-07-21 export provenance
```

---

## 8. Add the Three Source Exports

Files:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`

The contents should remain byte-preserved.

Suggested commits:

```text
data(ringconn): add annual sleep source export
```

```text
data(ringconn): add annual activity source export
```

```text
data(ringconn): add annual vital signs source export
```

---

## 9. Add Source-Export Checksums

File:

`data/source_exports/ringconn/2026-07-21/checksums.txt`

Suggested commit:

```text
data(ringconn): add source export checksums
```

---

## 10. Update Coverage and Quality Documentation

Files:

- `data/DATA_COVERAGE.md`
- `data/DATA_QUALITY_NOTES.md`

Record:

- direct annual wearable coverage
- missing dates
- multiple sleep episodes
- timezone limitation
- November 17 provider anomaly
- curated-versus-export differences
- candidate relevance to DQ-001 through DQ-003
- prohibition on immediate silent correction

Suggested commits:

```text
docs(data): register annual wearable coverage
```

```text
docs(data): document RingConn export quality findings
```

---

## 11. Create Normalized Wearable Trackers

Only after schemas are approved.

Files:

- `data/wearable_sleep_sessions_v1.csv`
- `data/wearable_activity_daily_v1.csv`
- `data/wearable_vitals_daily_v1.csv`

Suggested commits:

```text
data: add normalized wearable sleep sessions
```

```text
data: add normalized wearable activity history
```

```text
data: add normalized wearable vital signs history
```

---

## 12. Expand the Data Dictionary

File:

`DATA_DICTIONARY.md`

Add:

- wearable sleep-session fields
- wearable activity fields
- wearable vital-sign fields
- source and provenance fields
- timezone status
- source-row traceability
- metric distinctions
- missingness rules

Suggested commit:

```text
docs(data): define normalized wearable fields
```

---

## 13. Align Versioning

File:

`VERSIONING.md`

Purpose:

- align release policy with actual archive practice
- distinguish ordinary commits from archival releases
- define patch, minor, and major release triggers
- align Zenodo deposit cadence

Suggested commit:

```text
governance: align repository versioning policy
```

---

## 14. Update the Changelog

After the wearable source and normalized layers are complete, record the full ingestion sequence.

Suggested commit:

```text
docs(changelog): record annual wearable ingestion
```

---

## 15. Run Final Verification

Verify:

- links
- CSV parsing
- source-export checksums
- normalized row counts
- source-to-normalized traceability
- no duplicate normalized activity or vital dates
- preserved duplicate sleep sessions
- records 041–044 unchanged
- W29 active status
- release metadata unchanged
- changelog accuracy

---

# Work Not Recommended Today

Do not:

- append the annual sleep export directly to `sleep_longitudinal_v1.csv`
- overwrite curated historical sleep values
- collapse multiple sleep episodes without a transformation rule
- classify naps by assumption
- invent timezone offsets
- infer missing activity or vital-sign dates
- relabel minimum HR as resting HR
- relabel daily HRV as sleep HRV
- relabel total calories as active calories
- silently correct DQ-001 through DQ-003
- rewrite W28 from the later export
- merge all wearable domains into one giant CSV
- create a new model-error record merely because more historical data exist
- alter the physical protocol to exploit the expanded data
- declare the privacy issue distribution-complete without external verification
- increment the release version for routine documentation work

---

# Deferred Work

The following remain valuable but subordinate to the immediate privacy and source-ingestion sequence:

- curated-versus-export reconciliation table
- daily primary-sleep derivation
- formal nap classification
- timezone reconstruction
- automated wearable validators
- automated source-to-normalized transformation
- recovery-trajectory analysis
- activity-response analysis
- SpO₂ trend analysis
- perturbation-event structured export
- daily training structured export
- GitHub Actions deployment
- phase-vocabulary alignment
- August collection-plan finalization
- August release and Zenodo update

---

# Protected Boundaries

Do not modify during this audit cycle without separate evidence and governance:

- records 041–044
- original prediction wording
- registered evaluation thresholds
- closed prediction outcomes
- historical weekly interpretations
- existing curated sleep values
- unresolved sleep fields
- phase status
- active physical protocol
- August comparison baseline
- `CITATION.cff`
- `CODEMETA.json`
- Zenodo release metadata
- privately retained source artifacts

---

## Audit Summary

**Result: MECHANICAL PASS — PRIVACY DISTRIBUTION REMEDIATION AND WEARABLE-INGESTION GOVERNANCE REQUIRED**

Repository structure: pass  
Markdown links and anchors: pass  
Markdown fences: pass  
Repository CSV parsing: pass  
Canonical sleep continuity: pass  
Snapshot checksums: pass  
Artifact readability: pass  
Weekly report continuity: pass  
W28 closeout: pass  
W29 initialization: pass  
Model-error continuity: pass  
Open-record governance: pass  
Release metadata: pass  
Current blood-artifact sanitization: pass  
Blood-artifact changelog coverage: correction required  
Historical privacy distribution: verification required  
RingConn source-export integrity: pass with documented limitations  
Direct append into curated sleep CSV: not recommended  
Separate normalized longitudinal trackers: recommended  
Measurement-source documentation: revision required  
Anonymization methodology: expansion required  
Data dictionary: expansion required after schema approval  
Versioning policy: alignment due  

The repository remains suitable for:

- continued W29 operation
- continued Phase 2 Load Integration
- continued observation of records 041–044
- governed preservation of the annual wearable exports
- preparation for the August biological and performance snapshot

The next action should be the missing blood-artifact changelog entry, followed by anonymization and measurement-source governance before the wearable source files are incorporated.
