# Measurement Sources

## Purpose

This document defines the devices, facilities, providers, software systems, source formats, and capture modes used within the Daniel Longitudinal Study.

Its purpose is to:

- preserve longitudinal comparability
- identify potential sources of systematic bias
- distinguish direct evidence from transcription and derivation
- preserve provider and device provenance
- document software and hardware uncertainty
- define public-versus-private artifact status
- prevent semantically different metrics from being substituted for one another
- support future source reconciliation and correction

This document describes measurement provenance.

It does not determine biological interpretation.

Interpretation remains governed by:

- [`ASSUMPTIONS_AND_BOUNDARIES.md`](ASSUMPTIONS_AND_BOUNDARIES.md)
- [`METHODOLOGY_AND_CONTROLS.md`](METHODOLOGY_AND_CONTROLS.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)

---

## Facility and Provider Disclosure

Where public disclosure of a facility is unnecessary or undesirable, a stable public alias may be used.

Examples:

```text
DEXA_SITE_A
BODPOD_SITE_A
LAB_SITE_A
```

The private mapping between an alias and the actual facility may be retained outside the public repository.

An alias should remain stable across time unless:

- the provider changes
- the machine changes materially
- the location changes
- the comparison relationship changes
- privacy requirements require a new designation

A public provider name may be used when it is already intentionally disclosed and useful for provenance.

---

## Measurement Governance

### Representative-State Objective

The general measurement objective is to capture a representative operating state rather than a short-term peak display.

Preferred conditions include:

- ordinary protocol execution
- no artificial dehydration
- no acute glycogen-depletion strategy
- no acute glycogen-loading strategy
- no short-term sodium manipulation
- no unusual sauna exposure immediately before testing
- no deliberate training change intended only to improve the result
- no prediction-directed intervention
- capture conditions documented when materially relevant

These are preferred comparability conditions.

They do not establish perfect control.

A measurement is not automatically invalid because an ordinary-life condition differs.

Relevant differences should instead be:

- documented
- preserved
- considered during comparison
- prevented from being silently normalized away

The actual conditions recorded for a specific artifact take precedence over the general preferred conditions described here.

---

### No Universal Capture Assumption

Not every historical measurement was collected under identical conditions.

Potential differences include:

- fasting duration
- hydration
- sodium exposure
- glycogen state
- recent training
- time of day
- GI contents
- sleep
- travel
- facility
- equipment
- software
- assay provider
- operator procedure

The repository should not retroactively represent historical measurements as perfectly standardized when they were not.

---

## Source and Capture Modes

Every measurement should be understood according to how it entered the archive.

### 1. Provider or Device Source Artifact

Examples:

- official laboratory PDF
- DEXA report
- Bod Pod report
- TruDiagnostic report
- device-generated export
- provider-generated CSV

This is generally the strongest externally generated evidence available.

A public artifact may be:

- the original provider file
- a filename-normalized but byte-identical source
- a clearly identified sanitized derivative

---

### 2. Direct Provider Export

A file generated directly by a provider or device ecosystem.

Examples:

- RingConn sleep export
- RingConn activity export
- RingConn vital-sign export
- laboratory portal CSV
- provider spreadsheet export

A direct export may reflect:

- the provider’s current database state
- later algorithmic recalculation
- current software behavior
- export-specific field definitions

A later direct export should not automatically overwrite a contemporaneous screenshot or transcription.

Both source states may remain valid records of what the provider displayed at different times.

---

### 3. Contemporaneous Screenshot

A screenshot captured near the original observation date.

Screenshots may preserve:

- app-visible values
- app-specific labels
- readiness classifications
- sleep-tab values
- contemporaneous algorithm output
- contextual UI information absent from later exports

Screenshots may also contain privacy or account information and require review before public release.

---

### 4. Manual Transcription

A value manually transferred from:

- a source report
- screenshot
- provider portal
- device display
- workbook
- contemporaneous note

Manual transcription is not equivalent to a direct export.

It may introduce:

- copied-field errors
- date errors
- unit errors
- label errors
- rounding differences

Transcribed values should remain traceable to their strongest available source.

---

### 5. Derived Value

A value calculated from preserved source fields.

Examples:

- weekly average
- bodyweight change
- stage-sum difference
- elapsed duration
- UDI value
- concordance calculation

Derived values should document:

- source fields
- formula
- units
- missingness handling
- rounding behavior

A derived value must not be represented as a direct device measurement.

---

### 6. Narrative or Subjective Observation

Examples:

- mental state
- GI state
- pain
- movement quality
- perceived effort
- readiness impression
- dream description
- operator-overhead observation

Narrative evidence may be valuable.

It is not interchangeable with device or provider measurement.

---

## Source-State Preservation

The archive may contain more than one valid value associated with the same date when those values represent different source states.

Examples include:

- contemporaneous app screenshot
- later provider export
- manually transcribed daily tracker
- retrospective structured normalization

When source states differ:

- preserve both when materially useful
- identify each source mode
- avoid silent replacement
- do not force false agreement
- document known semantic differences
- define the governing use case

### Governing-use examples

A contemporaneous weekly report should normally remain grounded in the values available during that observation window.

A later provider export may govern a separate provider-faithful longitudinal table.

A correction to an existing curated value requires:

- a semantically equivalent source field
- stronger source evidence
- documented source precedence
- traceable correction
- review of dependent summaries

---

# Wearables

## Primary Wearable

### Device

RingConn Gen 2

### Device interval

The annual exports reviewed on 2026-07-22 represent data beginning on 2025-07-21.

The repository does not currently contain enough hardware-version evidence to prove that:

- the same physical ring was used for every represented date
- firmware remained unchanged
- sensor behavior remained unchanged
- provider algorithms remained unchanged

Hardware continuity should therefore be treated as reported but not independently verified across the complete interval.

---

### Application version

Observed application version:

```text
3.15.0
```

Point-in-time observation:

```text
2026-07-22
```

This version must not be retroactively assigned to the complete 2025-07 through 2026-07 observation period.

Historical application-version intervals remain unknown unless separately documented.

---

### Firmware version

Unknown.

No complete historical firmware-version record is currently available.

Firmware uncertainty should remain visible in longitudinal comparisons.

---

### Wearable source modes used

RingConn measurements enter the archive through several distinct modes:

- contemporaneous screenshots
- manual transcription
- curated daily tracking
- weekly summary calculation
- direct annual provider exports

These modes should remain distinguishable.

---

## RingConn Metric Boundaries

### Daily average heart rate

A provider-generated whole-day average.

Recommended normalized field:

```text
daily_avg_hr_bpm
```

This is not:

- resting heart rate
- sleeping heart rate
- sleep average heart rate
- minimum heart rate

---

### Daily minimum heart rate

The minimum provider-recorded heart rate for the represented day.

Recommended normalized field:

```text
daily_min_hr_bpm
```

This must not automatically be relabeled as:

```text
resting_hr_bpm
```

The provider’s daily minimum and the archive’s resting-heart-rate field may represent different definitions.

---

### Daily maximum heart rate

Recommended normalized field:

```text
daily_max_hr_bpm
```

This is a provider-generated daily extreme.

It is not automatically equivalent to:

- exercise peak heart rate
- validated maximal heart rate
- VO₂-test peak heart rate

---

### Daily average HRV

Recommended normalized field:

```text
daily_avg_hrv_ms
```

This is a whole-day provider summary.

It is not interchangeable with:

- sleep HRV
- overnight HRV
- morning HRV
- laboratory autonomic testing
- a separately derived daily biomarker value unless definitions match

---

### Sleep HRV

A sleep-period metric captured through the RingConn sleep interface or related source.

Recommended curated field:

```text
sleep_hrv_ms
```

Sleep HRV must remain separate from daily average HRV.

---

### Resting heart rate

The archive’s resting-heart-rate value is a separately tracked metric.

Recommended curated field:

```text
resting_hr_bpm
```

It must not be reconstructed from the RingConn daily minimum unless a documented provider definition establishes equivalence.

---

### Sleep average heart rate

Recommended curated field:

```text
sleep_avg_hr_bpm
```

This is not interchangeable with:

- daily average heart rate
- resting heart rate
- minimum heart rate

---

### Daily SpO₂ summaries

Recommended normalized fields:

```text
daily_avg_spo2_pct
daily_min_spo2_pct
daily_max_spo2_pct
```

These values are provider-generated daily summaries.

They should not be represented as:

- clinical pulse-oximetry testing
- diagnostic evidence by themselves
- laboratory-grade continuous oxygen monitoring
- interchangeable with sleep-only SpO₂ metrics

---

### Steps

Recommended normalized field:

```text
steps
```

Steps are provider-derived activity estimates.

They may be affected by:

- device wear
- activity type
- hand and arm behavior
- swimming
- incomplete daily wear
- provider algorithm changes

---

### Calories

Recommended normalized field:

```text
total_calories_kcal
```

The annual activity export labels this field as calories.

It should not be relabeled as:

```text
active_calories_kcal
```

unless RingConn documentation confirms that meaning.

---

## Annual RingConn Export Event

### Export date

2026-07-21

### Review date

2026-07-22

### Source files received

- sleep export
- activity export
- vital-sign export

The downloaded filenames contained an unnecessary personal naming string.

Public repository filenames should be normalized without changing the CSV contents.

---

### Canonical source-export location

```text
data/source_exports/ringconn/2026-07-21/
```

Recommended filenames:

```text
ringconn-sleep-export.csv
ringconn-activity-export.csv
ringconn-vital-signs-export.csv
README.md
checksums.txt
```

At the time of this documentation revision, the exports had been received and reviewed.

Repository ingestion is governed through a separate commit sequence.

---

### Sleep export coverage

- 366 episode rows
- 358 unique wake dates
- represented wake-date range: 2025-07-21 through 2026-07-21
- eight dates contain more than one sleep episode
- eight wake dates are absent
- timestamps contain no explicit UTC offset
- no provider-supplied primary-sleep or nap classification is present

The export is episode-level.

It should not be forced into a one-row-per-day structure without a registered transformation rule.

---

### Activity export coverage

- 360 daily rows
- 360 unique dates
- represented date range: 2025-07-21 through 2026-07-20
- five dates are absent from 2026-01-04 through 2026-01-08
- no row is present for 2026-07-21

Missing dates remain missing.

---

### Vital-sign export coverage

- 360 daily rows
- 360 unique dates
- represented date range: 2025-07-21 through 2026-07-20
- missing dates match the activity export
- heart-rate, SpO₂, and HRV fields contain daily minimum, average, and maximum values

The direct export should not be used to reconstruct differently defined curated fields.

---

### Timezone status

RingConn export timestamps do not contain UTC offsets.

The represented year includes travel.

Accordingly:

- timestamps should remain in exported local form
- UTC offsets should not be invented
- timezone should remain unknown or unresolved unless separately documented
- cross-timezone analysis should disclose the limitation

Recommended normalized value:

```text
timezone_status = local_offset_unknown
```

---

### Direct-export preservation rule

The source-export CSV files should remain byte-preserved.

Permitted changes before public inclusion:

- filesystem-level filename normalization
- directory placement
- checksum generation
- provenance documentation

Not permitted in the source-copy files:

- header renaming
- date conversion
- metric relabeling
- row deletion
- missing-value replacement
- timezone conversion
- nap classification
- correction of provider anomalies
- normalization for appearance

Analytical normalization belongs in separate files.

---

## RingConn Curated Data

Current curated sleep dataset:

```text
data/sleep_longitudinal_v1.csv
```

This file contains a governed one-row-per-date structure and may include:

- manually transcribed sleep values
- sleep HRV
- sleep average heart rate
- awakenings count
- subjective state
- readiness
- tags
- confidence annotations
- narrative context

It is not a raw provider export.

The direct annual sleep export should not be appended directly to this file.

---

## RingConn Normalized Data

Recommended normalized provider-faithful datasets:

```text
data/wearable_sleep_sessions_v1.csv
data/wearable_activity_daily_v1.csv
data/wearable_vitals_daily_v1.csv
```

These should remain separate because they differ in:

- row grain
- field meaning
- missingness
- timestamp structure
- source behavior

### Sleep normalized grain

One row per exported sleep episode.

### Activity normalized grain

One row per provider date.

### Vital-sign normalized grain

One row per provider date.

Normalized tables should retain:

- source export date
- source device
- source row
- timestamp status
- original missingness

---

## Curated Versus Later Export Values

Material differences were observed between:

- contemporaneous curated sleep values
- later direct RingConn export values

Potential explanations include:

- provider recalculation
- app-versus-export field differences
- software changes
- algorithm changes
- rounding
- transcription differences
- source-state differences

Neither source should silently overwrite the other.

The existing curated sleep dataset remains the source for the weekly reports already based on it unless a governed source-backed correction is later performed.

The later direct export should govern its own provider-faithful normalized tables.

---

# Body Composition

## DEXA

### Provider

DexaFit

### Public source identifier

```text
DEXA_DEXAFIT
```

### Machine model

Unknown.

The machine model should be recorded from the provider artifact or facility when available.

### Software version

Unknown.

The software version should be recorded when available.

### Source modes

- official provider PDF
- source image or screenshot when necessary
- structured transcription into snapshot or biomarker datasets
- retrospective report summary

### Capture-condition objective

Preferred conditions include:

- fasted for approximately 10 hours or more
- normal hydration
- no deliberate dehydration
- no unusual sodium manipulation
- no acute glycogen-depletion protocol
- no acute glycogen-loading protocol
- ordinary training schedule unless documented otherwise

The actual conditions for each DEXA event should be documented separately.

### Known considerations

- lean mass may vary with hydration and glycogen
- GI contents may influence total mass
- machine and software changes may affect comparability
- positioning and operator procedure may affect results
- cross-provider comparison may introduce additional uncertainty
- provider-generated regional values may not be directly interchangeable across systems

Longitudinal interpretation should prioritize:

- the same provider
- the same machine
- the same software
- comparable preparation conditions

when available.

---

## Bod Pod

### Provider

Public alias:

```text
BODPOD_SITE_A
```

Current description:

Military-base facility.

### Machine model

COSMED Bod Pod

### Software version

Unknown.

### Source modes

- official provider printout or report
- public image artifact
- structured transcription
- retrospective report summary

### Capture-condition objective

Preferred conditions include:

- fasted for approximately 10 hours or more
- minimal clothing under facility protocol
- no deliberate dehydration
- no sauna immediately before measurement
- ordinary hydration
- documented GI and recent-training context when relevant

### Known considerations

- test clothing and hair compression may affect measurement
- thoracic-gas-volume procedure or estimation may affect output
- machine calibration may vary
- hydration and GI contents may influence bodyweight context
- Bod Pod and DEXA body-fat estimates are not interchangeable

Longitudinal comparisons should prioritize the same facility and measurement procedure.

---

# Performance Testing

## VO₂ Max

### Provider

DexaFit

### Public source identifier

```text
VO2_DEXAFIT
```

### Planned capture

2026-08-17

No result is present at the time of this revision.

### Equipment

Unknown until capture.

### Software version

Unknown until capture.

### Source modes expected

- official provider report
- test-stage or summary output
- structured transcription
- snapshot interpretation

### Required capture documentation

At the time of testing, record when available:

- equipment model
- protocol type
- stage or ramp structure
- mask or gas-analysis system
- test duration
- peak heart rate
- respiratory-exchange information
- termination reason
- fasting state
- hydration
- recent training
- time of day

The planned test does not become evidence until the result and source artifact exist.

---

# Laboratory and Biological Testing

## Conventional Laboratory Testing

### Providers represented

- military laboratory services
- Department of Veterans Affairs
- Labcorp
- other provider facilities documented in individual artifacts

### Source modes

- official laboratory PDF
- portal report
- public sanitized derivative
- structured transcription
- longitudinal bloodwork dataset
- retrospective report synthesis

### Known considerations

- reference intervals may change
- assays may change
- laboratory provider may change
- unit conventions may change
- fasting state may differ
- collection time may differ
- specimen handling may differ
- provider comments may not be directly comparable
- identical analyte names do not guarantee identical methodology

Cross-laboratory comparisons should remain cautious and explicitly contextualized.

---

## July 2025 Blood Panel

### Public artifact

```text
snapshots/2025-07/2025-07-full-blood-panel.pdf
```

### Public status

Sanitized derivative.

The public artifact preserves:

- laboratory values
- units
- reference intervals
- flags
- test dates
- interpretation-relevant report structure

The public derivative removes:

- full date of birth
- patient identifier
- specimen identifier
- address
- contact information
- ordering-physician identity

The subject’s public name and chronological age remain intentionally visible.

### Private source status

The verified provider source is retained privately for source verification.

### Checksum status

The current public derivative is represented by the current checksum in:

```text
snapshots/2025-07/checksums.txt
```

The public checksum identifies the sanitized derivative.

It does not assert byte identity with the private original.

### Distribution status

Current-tree sanitization is complete.

Historical Git and prior archival-distribution verification remain separate tasks until directly completed.

---

## TruDiagnostic

### Provider

TruDiagnostic

### Measurement domains

May include:

- TruAge
- TruHealth
- OMICm age
- DunedinPACE
- SymphonyAge
- organ or system-age outputs
- provider-generated supporting biological-age metrics

### Source modes

- provider report
- portal output
- screenshot
- source artifact
- structured transcription
- longitudinal epigenetic dataset
- retrospective snapshot interpretation

### Known considerations

- provider algorithms may change
- report structures may change
- model versions may change
- one biological-age metric should not be substituted for another
- composite and organ-specific metrics may move differently
- collection and processing dates should remain distinct
- result-release date is not the same as sample-collection date

The archive should preserve the specific metric name and provider version when available.

---

# Public and Private Artifact Status

Measurement evidence may exist in one of the following states:

- public original
- public filename-normalized source
- public sanitized derivative
- private source only
- structured transcription from a verified private source
- derived summary
- narrative interpretation

The status should be documented when it affects external verifiability.

A public sanitized derivative must not be described as an untouched provider original.

An unpublished private source should not be represented as publicly inspectable.

Detailed sanitization rules are defined in:

[`methodology/anonymization.md`](methodology/anonymization.md)

---

# Source Precedence

Source precedence is context-dependent.

The default hierarchy is:

1. verified provider or device source artifact
2. direct provider export
3. contemporaneous screenshot
4. contemporaneous structured transcription
5. contemporaneous operator note
6. retrospective synthesis
7. unsupported memory

This hierarchy does not authorize automatic overwriting.

A later direct export may differ from an earlier screenshot because it reflects a different provider state.

Source precedence for correction requires both:

- stronger evidence
- semantic equivalence

When semantic equivalence is uncertain, preserve both and document the conflict.

---

# Correction and Reconciliation

A measurement should be corrected only when:

- the affected field is identified
- the stronger source is available
- the source field has the same meaning
- units are compatible
- dates are aligned
- transformation rules are explicit
- the correction is narrow
- downstream effects are reviewed
- the correction remains traceable through Git history
- the changelog is updated when material

The archive prohibits:

- correction from memory alone
- silent replacement
- field substitution
- use of neighboring values
- interpolation presented as observation
- rewriting a weekly report merely to match a later provider export
- forcing two source states to agree

Known unresolved issues remain documented in:

[`data/DATA_QUALITY_NOTES.md`](data/DATA_QUALITY_NOTES.md)

---

# Longitudinal Comparability

When any of the following change materially:

- measurement facility
- provider
- hardware platform
- physical device
- software version
- firmware
- assay method
- report algorithm
- capture mode
- public artifact status
- preparation conditions
- field definition
- normalization method

the repository should:

1. update this document
2. record the change in `CHANGELOG.md` when material
3. note comparability limitations in the relevant report or snapshot
4. preserve the prior source state
5. avoid silent crosswalks
6. update the data dictionary when field definitions change
7. update validation rules when needed

A change does not necessarily invalidate the new measurement.

It may limit direct comparison.

---

# Missing Version Information

Unknown machine, software, firmware, or assay information should remain explicitly unknown.

The repository should not infer version history from:

- current application version
- current device appearance
- later provider reports
- memory without supporting evidence

Future capture should become more version-aware.

Historical uncertainty should remain visible.

---

# Capture-Condition Documentation

Each major snapshot cycle should record, when relevant:

- date
- local time
- fasting duration
- hydration state
- recent food intake
- recent training
- recent sauna or heat exposure
- recent travel
- sleep context
- medication or supplement deviations
- provider
- facility
- machine
- software
- source-artifact type

General preferred conditions in this file do not substitute for event-specific documentation.

The August 2026 snapshot should use a separate preregistered collection-condition plan before outcome review.

---

# Data Handling Policy

Measurement artifacts follow these rules:

- verified source artifacts are preserved privately or publicly as appropriate
- public artifacts may be sanitized when privacy requires it
- sanitized derivatives must be identified
- direct exports should be preserved separately from normalized tables
- numerical values may be transcribed for structured use
- transcribed values must remain source-traceable
- derived values must be labeled
- missing values remain missing
- corrections require source support
- prior repository states remain preserved through Git history unless privacy remediation requires deliberate history rewriting
- historical biological evidence should not be overwritten for narrative consistency

The principle is:

> Preserve the strongest available evidence, disclose the source state, and avoid false equivalence.

---

# Repository Locations

Current and planned measurement-source locations include:

```text
/snapshots
/data
/data/source_exports
/data/model_error
/reports
/methodology
```

### `/snapshots`

Primary milestone artifacts and public source representations.

### `/data/source_exports`

Byte-preserved provider or device exports with provenance and checksums.

### `/data`

Normalized and curated longitudinal tables.

### `/reports`

Active collection and closed retrospective interpretation.

### `/methodology`

Rules governing collection, normalization, correction, sanitization, and evaluation.

---

# Interpretation Boundary

Measurement artifacts represent observation points.

They do not independently establish:

- causality
- protocol efficacy
- phase transition
- generalizability
- clinical diagnosis
- prediction success
- absence of measurement error
- cross-provider equivalence

Interpretation must remain proportional to:

- source quality
- source timing
- metric definition
- capture conditions
- comparability
- missingness
- provider behavior
- preserved uncertainty

---

# Related Documents

- [`ASSUMPTIONS_AND_BOUNDARIES.md`](ASSUMPTIONS_AND_BOUNDARIES.md)
- [`METHODOLOGY_AND_CONTROLS.md`](METHODOLOGY_AND_CONTROLS.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`DATASET_OVERVIEW.md`](DATASET_OVERVIEW.md)
- [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md)
- [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)
- [`data/DATA_QUALITY_NOTES.md`](data/DATA_QUALITY_NOTES.md)
- [`methodology/data-collection.md`](methodology/data-collection.md)
- [`methodology/anonymization.md`](methodology/anonymization.md)
- [`VERSIONING.md`](VERSIONING.md)
- [`CHANGELOG.md`](CHANGELOG.md)

---

## Version Note

This document was expanded on 2026-07-22 to align measurement-source governance with the archive’s current evidence structure.

The revision:

- replaces timeless source descriptions with date-aware provenance
- distinguishes direct exports, screenshots, transcription, derivation, and narrative observation
- registers the 2026-07-21 RingConn export event
- distinguishes daily, resting, and sleep cardiovascular metrics
- documents timezone and provider-reprocessing limitations
- separates immutable source exports from normalized and curated datasets
- permits clearly identified public sanitized derivatives
- documents the July 2025 blood panel’s public artifact status
- preserves unknown hardware, software, firmware, and assay information as unknown
- defines source-state and correction boundaries
- replaces universal capture assumptions with event-specific comparability requirements

The revision does not alter:

- any source measurement
- any curated longitudinal value
- any prediction record
- any closed outcome
- any protocol exposure
- any phase status
