# Data Dictionary

This document defines measurement terms, field meanings, units, date rules, and logging conventions used in the Daniel Longitudinal Study.

Definitions prioritize:

- repeatability
- longitudinal comparability
- source traceability
- separation of source evidence from curated data
- explicit missingness
- interpretive restraint

This document does not authorize data correction, normalization, aggregation, or inference.

Dataset-specific definitions take precedence over global conventions when a conflict exists.

---

## Archive Data Layers

The archive contains several different data layers.

They must not be treated as interchangeable.

### Source Artifacts

Original measurement reports, images, PDFs, and direct provider exports.

Examples:

- DEXA reports
- Bod Pod reports
- laboratory reports
- TruDiagnostic reports
- byte-preserved RingConn CSV exports

Source artifacts preserve provider-defined output.

They are not modified to match archive schemas.

---

### Canonical Structured Datasets

Archive-defined machine-readable datasets maintained under governed schemas.

Examples:

- `data/sleep_longitudinal_v1.csv`
- `data/biomarker_snapshot.csv`
- `data/epigenetic_longitudinal.csv`
- `data/bloodwork_longitudinal.csv`
- `data/model_error/model_error_gap_v1.csv`

Canonical datasets may contain:

- source-transcribed fields
- archive-defined date assignments
- confidence annotations
- subjective context
- correction notes
- derived values created under documented rules

Canonical values must remain traceable to their source.

---

### Narrative Evidence

Contemporaneous and retrospective observations preserved in:

- weekly reports
- training notes
- snapshot context files
- audit records
- model-error closure records

Narrative evidence may preserve information that is not represented in structured data.

---

### Derived Views

Dashboards, summaries, charts, and analytical outputs generated from other archive layers.

Derived views do not create new primary evidence.

---

## Global Conventions

### Dates

Default canonical date format:

`YYYY-MM-DD`

Snapshot-month format:

`YYYY-MM`

Dataset-specific date meaning must be explicitly defined.

A date may represent:

- collection date
- result date
- wake date
- session date
- testing date
- snapshot month
- report window

The presence of a date does not establish that all measurements in the row were captured at the same time.

---

### Sleep Dates

For the curated sleep dataset, the date represents the governed morning or wake-date observation assigned to the sleep episode.

This convention must not automatically be applied to direct RingConn exports.

Direct RingConn sleep exports preserve their original:

- start timestamp
- end timestamp
- falling-asleep timestamp
- wake-up timestamp

The source export does not currently establish an authoritative timezone or archive-defined daily date.

---

### Time

Canonical time format when required:

`HH:MM`

Use 24-hour time.

The subject’s ordinary local timezone is:

`America/New_York`

This does not establish that every provider export or historical timestamp is encoded in that timezone.

When timezone provenance is unavailable:

- preserve the original timestamp
- mark timezone status as unresolved
- do not convert the value
- do not append an assumed UTC offset

---

### Timestamp Precision

Timestamp precision must not be increased through inference.

Examples:

- `2026-07-19 03:42` remains minute precision
- `2026-07-19 03:42:17` retains second precision

Do not append `:00` and then represent the value as second-level measurement unless the transformation is explicitly documented.

---

### Units

Default archive units:

| Domain | Unit |
|---|---|
| Weight | pounds (`lb`) |
| Duration | minutes (`min`) |
| Heart rate | beats per minute (`bpm`) |
| HRV | milliseconds (`ms`), when reported that way by the device |
| Speed | miles per hour (`mph`) |
| Incline | percent (`%`) |
| Temperature | Fahrenheit (`°F`) |
| Distance | miles (`mi`) unless otherwise noted |
| Energy expenditure | kilocalories (`kcal`) or kilocalories per day (`kcal/day`) |
| Biological age | years |
| Percentile score | percentile from 0–100 |
| Pace of aging | ratio |
| Oxygen saturation | percent (`%`) |

Values should remain in source units unless a documented transformation requires conversion.

Converted values must preserve:

- original value
- original unit
- conversion rule
- transformed value
- transformed unit

---

## Missingness Conventions

Missing values must remain distinguishable from measured zero.

### Blank

Use when:

- the source contains no value
- the metric was not available
- the value was not collected
- the value cannot be transferred reliably

A blank does not mean zero.

---

### Zero

Use only when the source explicitly reports zero or the metric is structurally defined as zero.

Examples:

- `0` steps may be a device-reported value
- `0` minutes of REM may be a provider-reported value

A reported zero may still require a data-quality note when it is internally inconsistent.

---

### Not Applicable

Use only when a field does not apply to the observation.

Do not use zero as a substitute for not applicable.

---

### Unknown

Use a documented categorical value such as `unknown` only in fields designed to accept categorical missingness.

Do not place text values in numeric fields unless the schema explicitly permits them.

---

### Missing Dates

An absent date must not automatically be interpreted as:

- zero activity
- no sleep
- no device wear
- synchronization failure
- intentional non-use
- illness
- travel

Missing-date behavior must be documented separately from measured values.

---

## Correction Conventions

Canonical values may be corrected only when supported by identifiable source evidence.

A correction must document:

- dataset
- date
- field
- prior value
- corrected value
- supporting source
- reason for correction
- correction date
- associated commit or changelog entry

Do not:

- silently repair values
- derive replacements from neighboring dates
- overwrite a curated dataset from a later export without review
- treat plausibility as proof
- change unrelated fields during a targeted correction

Direct provider exports remain unchanged even when a canonical correction is made.

Known issues are recorded in:

[`data/DATA_QUALITY_NOTES.md`](data/DATA_QUALITY_NOTES.md)

---

# Source-Preserved RingConn Exports

## Directory

Current acquisition package:

[`data/source_exports/ringconn/2026-07-21/`](data/source_exports/ringconn/2026-07-21/)

## Source Status

The included CSVs are:

- direct provider exports
- preserved byte-for-byte
- checksum registered
- not normalized
- not canonical daily trackers
- not automatically merged into curated datasets

The acquisition date identifies when the package was downloaded.

It does not indicate that all represented observations occurred on that date.

---

## Source Export Naming

Current filenames:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`

These filenames are archive-assigned names for the preserved acquisition files.

They do not change the internal provider field names.

---

## RingConn Sleep Export Fields

Source file:

`data/source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`

The source file is session-based rather than guaranteed to be one row per calendar date.

### Start Time

Provider-reported beginning of the detected sleep session.

Format varies between:

- `YYYY-MM-DD HH:MM:SS`
- `YYYY-MM-DD HH:MM`

Timezone is not established by the export.

---

### End Time

Provider-reported end of the detected sleep-session interval.

Timezone is not established by the export.

This field is not automatically equivalent to the governed canonical sleep date.

---

### Falling Asleep Time

Provider-reported estimated time at which sleep began.

This field may differ from `Start Time`.

It remains a device estimate.

---

### Wake-up time

Provider-reported estimated time at which sleep ended.

This field may differ from `End Time`.

Preliminary comparison suggests that wake date may align with the curated sleep date for primary overnight sessions, but that mapping is not yet a universal source rule.

---

### Sleep Time Ratio(%)

Provider-reported percentage representing time asleep relative to the applicable session interval.

Unit:

`%`

This field should not automatically be treated as identical to every archive use of the term sleep efficiency.

Provider calculation behavior may differ from manually recorded or application-displayed values.

---

### Time Asleep(min)

Provider-reported total minutes asleep during the exported session.

Unit:

`min`

This is session-level duration.

It is not automatically a daily total when multiple sessions exist.

---

### Sleep Stages - Awake(min)

Provider-reported awake duration associated with the sleep session.

Unit:

`min`

This is not equivalent to awakening count.

---

### Sleep Stages - REM(min)

Provider-reported REM sleep duration for the session.

Unit:

`min`

A value of zero may mean:

- provider-reported zero
- unavailable stage classification
- provider anomaly

Context must be checked before interpretation.

---

### Sleep Stages - Light Sleep(min)

Provider-reported light-sleep duration for the session.

Unit:

`min`

---

### Sleep Stages - Deep Sleep(min)

Provider-reported deep-sleep duration for the session.

Unit:

`min`

---

## RingConn Sleep Session Boundary

Multiple exported sleep rows may correspond to the same preliminary wake date.

Possible examples include:

- overnight sleep plus a nap
- split sleep
- two provider-detected sessions
- a recovery sleep episode
- a session requiring separate classification

Do not:

- deduplicate by date
- discard the shorter session
- automatically sum all sessions
- automatically select the longest session
- overwrite the canonical daily sleep row

The direct source export remains session-based.

A daily aggregation rule has not been adopted.

---

## RingConn Activity Export Fields

Source file:

`data/source_exports/ringconn/2026-07-21/ringconn-activity-export.csv`

### Date

Provider-assigned calendar date.

Format:

`YYYY-MM-DD`

Timezone behavior is not explicitly documented by the source export.

---

### Steps

Provider-reported daily step count.

Unit:

`count`

This metric does not establish:

- exercise type
- formal training exposure
- resistance-training volume
- swimming activity
- session intensity
- movement quality

---

### Calories(kcal)

Provider-estimated daily energy expenditure represented by the export field.

Unit:

`kcal`

The exact provider definition should not be assumed to mean:

- active calories only
- total daily energy expenditure
- measured caloric expenditure
- resting metabolic expenditure

Until provider semantics are confirmed, retain the original field name and describe the value as:

**RingConn-reported calories**

Do not merge it with Bod Pod or COSMED energy-expenditure estimates.

---

## RingConn Vital-Signs Export Fields

Source file:

`data/source_exports/ringconn/2026-07-21/ringconn-vital-signs-export.csv`

### Date

Provider-assigned calendar date.

Format:

`YYYY-MM-DD`

---

### Avg. Heart Rate(bpm)

Provider-reported daily average heart rate.

Unit:

`bpm`

This is distinct from:

- resting heart rate
- sleeping average heart rate
- minimum heart rate
- workout heart rate
- morning spot measurement

---

### Min. Heart Rate(bpm)

Provider-reported minimum heart rate for the applicable daily window.

Unit:

`bpm`

This is not automatically equivalent to resting heart rate.

---

### Max. Heart Rate(bpm)

Provider-reported maximum heart rate for the applicable daily window.

Unit:

`bpm`

This is not automatically equivalent to exercise-session peak heart rate.

---

### Avg. SpO2(%)

Provider-reported daily average blood-oxygen saturation estimate.

Unit:

`%`

Consumer wearable estimate.

---

### Min. SpO2(%)

Provider-reported minimum blood-oxygen saturation estimate.

Unit:

`%`

A minimum value may reflect:

- true physiological variation
- transient measurement artifact
- poor ring contact
- motion
- device estimation behavior

It should not be interpreted independently of surrounding evidence.

---

### Max. SpO2(%)

Provider-reported maximum blood-oxygen saturation estimate.

Unit:

`%`

---

### Avg. HRV(ms)

Provider-reported daily average heart-rate variability.

Unit:

`ms`

This is distinct from:

- sleep HRV
- overnight HRV
- morning HRV
- spot-measurement HRV
- HRV from another device ecosystem

---

### Min. HRV(ms)

Provider-reported minimum HRV within the applicable daily window.

Unit:

`ms`

Provider aggregation and sampling behavior remain device-defined.

---

### Max. HRV(ms)

Provider-reported maximum HRV within the applicable daily window.

Unit:

`ms`

---

## Wearable Metric Distinctions

### Daily Average Heart Rate

Average heart rate across the provider-defined daily observation window.

Do not label this as:

- resting heart rate
- sleeping heart rate
- average sleep heart rate

---

### Resting Heart Rate

Provider-derived or separately recorded resting-heart-rate metric.

Unit:

`bpm`

The exact device definition should be documented when available.

---

### Average Sleeping Heart Rate

Average heart rate during the provider-defined sleep interval.

Unit:

`bpm`

This is distinct from daily average heart rate.

---

### Sleep HRV

HRV associated with the provider-defined sleep interval or sleep summary.

Unit:

`ms`

This is distinct from daily average HRV.

---

### Daily Average HRV

Provider-reported HRV average across the defined daily observation window.

Unit:

`ms`

Daily average HRV and sleep HRV must be labeled separately in reports and datasets.

---

### Awakening Count

Number of discrete awakening events reported by the application or manually transcribed source.

Unit:

`count`

This is distinct from awake duration.

The direct RingConn sleep export currently preserved in the archive does not include an awakening-count field.

---

### Awake Duration

Provider-reported minutes awake within or around a sleep session.

Unit:

`min`

Awake duration must not be populated using awakening count.

---

### Sleep Efficiency

Percentage of the applicable sleep opportunity or session interval spent asleep.

Unit:

`%`

The exact denominator may vary by provider or archive calculation.

Whenever possible, distinguish:

- provider-reported sleep ratio
- provider-reported sleep efficiency
- archive-derived sleep efficiency

Do not assume they are interchangeable.

---

## Periodic Wearable Export Policy

Periodic direct exports may be preserved without creating normalized wearable datasets.

Each acquisition should use a separate directory:

`data/source_exports/ringconn/YYYY-MM-DD/`

Each acquisition package should contain:

- original sleep export
- original activity export
- original vital-signs export
- acquisition README
- checksum manifest

Overlapping coverage between exports is permitted.

A newer acquisition does not overwrite an older acquisition.

The acquisition directories preserve:

- what the provider supplied
- when it was downloaded
- how the files were verified
- whether provider output changed across export events

Normalized wearable datasets remain optional and deferred until a defined analytical, publication, or automation requirement exists.

---

## Source Export Versus Canonical Sleep Data

The direct RingConn sleep export and:

[`data/sleep_longitudinal_v1.csv`](data/sleep_longitudinal_v1.csv)

serve different roles.

### Direct RingConn Export

Preserves:

- provider field names
- provider timestamps
- session-level rows
- provider missingness
- provider stage values
- original file bytes

### Curated Sleep Dataset

May preserve:

- governed observation date
- manually transcribed sleep values
- confidence annotations
- morning subjective observations
- dreams
- mental state
- GI state
- pain state
- contextual notes
- source-backed correction history

Neither layer silently replaces the other.

---

# biomarker_snapshot.csv Fields

## date

Snapshot month.

Format:

`YYYY-MM`

Example:

`2026-02`

---

## source

Indicates that the row is an integrated snapshot compiled from multiple artifacts.

Expected value:

`integrated`

---

## dexa_date

Date of the DEXA artifact used for the snapshot.

Format:

`YYYY-MM-DD`

---

## bodpod_date

Date of the Bod Pod artifact used for the snapshot.

Format:

`YYYY-MM-DD`

---

## chronological_age

Calendar age at time of testing.

Unit:

`years`

---

## omicm_age

TruAge OMICm biological-age output.

Unit:

`years`

---

## omicm_age_delta_years

Difference between `omicm_age` and `chronological_age`.

Unit:

`years`

Negative values indicate OMICm age below chronological age.

---

## dunedin_pace

DunedinPACE rate-of-aging output.

Unit:

`ratio`

Interpretive anchor:

- `1.0` represents one biological year per chronological year
- values below `1.0` represent a slower measured pace
- values above `1.0` represent a faster measured pace

The value remains an assay output rather than a direct measurement of future lifespan.

---

## symphony_age

Composite SYMPHONY organ-system age output.

Unit:

`years`

---

## blood_age

SYMPHONY blood-system age.

Unit:

`years`

---

## brain_age

SYMPHONY brain-system age.

Unit:

`years`

---

## inflammation_age

SYMPHONY inflammation-system age.

Unit:

`years`

---

## heart_age

SYMPHONY heart-system age.

Unit:

`years`

---

## hormone_age

SYMPHONY hormone-system age.

Unit:

`years`

---

## immune_age

SYMPHONY immune-system age.

Unit:

`years`

---

## kidney_age

SYMPHONY kidney-system age.

Unit:

`years`

---

## liver_age

SYMPHONY liver-system age.

Unit:

`years`

---

## metabolic_age

SYMPHONY metabolic-system age.

Unit:

`years`

---

## lung_age

SYMPHONY lung-system age.

Unit:

`years`

---

## musculoskeletal_age

SYMPHONY musculoskeletal-system age.

Unit:

`years`

---

## body_score

DEXA summary body-score grade.

Unit:

categorical

Example:

`A`

---

## total_mass_lbs

Total body mass reported by DEXA.

Unit:

`lb`

---

## body_fat_pct_dexa

Body-fat percentage reported by DEXA.

Unit:

`%`

---

## fat_mass_lbs_dexa

Fat mass reported by DEXA.

Unit:

`lb`

---

## lean_mass_lbs_dexa

Lean soft-tissue mass reported by DEXA.

Unit:

`lb`

This is not equivalent to Bod Pod fat-free mass.

---

## visceral_fat_lbs

Visceral-fat estimate reported by the DEXA provider.

Unit:

`lb`

Provider-specific units should be confirmed against the artifact.

---

## t_score

Bone-density T-score reported by DEXA.

Unit:

score

---

## bodpod_body_fat_pct

Body-fat percentage estimated through air-displacement plethysmography.

Unit:

`%`

---

## bodpod_fat_mass_lbs

Fat mass estimated by Bod Pod.

Unit:

`lb`

---

## bodpod_ffm_lbs

Fat-free mass estimated by Bod Pod.

Unit:

`lb`

This is not equivalent to DEXA lean soft-tissue mass.

---

## bodpod_body_mass_lbs

Body mass recorded during the Bod Pod measurement.

Unit:

`lb`

---

## bodpod_ree_kcal_day

Resting energy-expenditure estimate reported with the Bod Pod or associated COSMED output.

Unit:

`kcal/day`

This field should not be described as a dedicated measured resting-metabolic-rate result unless the underlying artifact confirms indirect calorimetry.

---

## bodpod_tee_kcal_day

Total energy-expenditure estimate reported with the Bod Pod or associated COSMED output.

Unit:

`kcal/day`

This may be calculated from assumptions rather than directly measured.

---

## TruHealth Score Fields

The following fields represent provider-reported TruHealth percentile outputs:

- `truhealth_vitamins_score`
- `truhealth_amino_acids_score`
- `truhealth_antioxidants_score`
- `truhealth_fats_membranes_score`
- `truhealth_lipid_peroxidation_score`
- `truhealth_serum_lipids_score`
- `truhealth_blood_pressure_score`
- `truhealth_metabolic_score`
- `truhealth_immune_score`
- `truhealth_neurocognitive_score`
- `truhealth_inflammation_score`
- `truhealth_stress_score`
- `truhealth_toxins_score`
- `truhealth_uric_acid_pathway_score`
- `truhealth_mitochondrial_function_score`
- `truhealth_oxidative_defense_score`
- `truhealth_nad_metabolism_score`
- `truhealth_ketones_score`
- `truhealth_supplements_score`

Unit:

`percentile from 0–100`

These are provider-derived outputs.

They are not direct concentration measurements unless the corresponding artifact explicitly reports a laboratory concentration.

---

## notes

Free-text snapshot context.

May include:

- source scope
- collection caveats
- comparability notes
- integration notes
- known missing domains

---

# epigenetic_longitudinal.csv Fields

## date

Capture date of the epigenetic test result.

Format:

`YYYY-MM-DD`

---

## domain

Broad grouping of the result.

Examples:

- `aging`
- `organ_age`
- `truhealth_domain`
- `truhealth_marker`

---

## biomarker

Machine-readable biomarker or output name.

Examples:

- `omicm_age`
- `dunedin_pace`
- `blood_age`
- `ldl_c`
- `pfos`

---

## value

Numeric result as reported or derived under documented rules.

Unit depends on field context.

---

## unit

Measurement unit.

Examples:

- `years`
- `ratio`
- `percentile`
- provider-reported concentration unit

---

## status

Provider or archive interpretation category associated with the value.

Examples:

- `normal`
- `suboptimal`
- `high`
- `high_warning`
- `low`
- `reference`

Status labels must not be treated as equivalent across providers unless comparability is documented.

---

## source

Report source used for the row.

Expected examples:

- `TruAge`
- `Advanced_TruAge`
- `TruHealth`

---

## notes

Free-text context, caveats, source details, or interpretation limits.

---

# Subjective State Context

Some subjective or qualitative context may be intentionally absent from structured dataset fields.

The repository prioritizes governed, retrospective, artifact-first documentation.

Real-time subjective observations, informal state notes, and public-facing commentary are not always backfilled into structured tables.

When relevant, the accompanying X account may serve as an external subjective-telemetry reference:

[@CDHughett](https://x.com/CDHughett)

This account is not a replacement for:

- structured data
- formal reports
- source artifacts
- governed archive entries

It is a complementary real-time layer that may provide context around:

- subjective state
- training texture
- recovery observations
- public execution cadence

Empty or sparsely populated subjective fields should not automatically be interpreted as collection failure.

In some cases, they reflect intentional separation between the governed archive and informal human telemetry.

See:

- [`TELEMETRY.md`](TELEMETRY.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)

---

# Capture States

## Fasted

Defined as:

- no caloric intake for at least 10 hours before capture
- water permitted
- non-caloric electrolytes permitted only when part of normal routine
- caffeine or stimulants logged when used
- no deliberate extension solely to manipulate the measurement

---

## Normal Operating Conditions

Defined as:

- no artificial dehydration protocol
- no sodium manipulation for cosmetic effect
- no acute glycogen-depletion strategy
- no short-term loading strategy intended to influence the result
- no protocol change made solely to produce a favorable capture

Normal operating conditions do not mean complete environmental control.

Material deviations should be documented in the associated report or snapshot context.

---

# Body Composition Terms

## DEXA Total Mass

Total body mass measured during DEXA.

Unit:

`lb`

---

## DEXA Lean Mass

Lean soft-tissue mass reported by DEXA.

Unit:

`lb`

DEXA lean mass:

- excludes fat mass
- is distinct from bone mineral
- is sensitive to glycogen and hydration
- is not equivalent to Bod Pod fat-free mass

---

## DEXA Fat Mass

Total fat mass reported by DEXA.

Unit:

`lb`

---

## DEXA Body Fat Percentage

Body-fat percentage reported by DEXA.

Unit:

`%`

---

## DEXA Bone Mineral Content

Bone mineral content reported by DEXA.

Unit:

record exactly as reported, commonly `g` or `lb`

---

## DEXA Bone Mineral Density

Bone mineral density reported by DEXA.

Unit:

commonly `g/cm²`

Record exactly as reported.

---

## DEXA Visceral Fat

Visceral-fat metric reported by the DEXA provider.

Unit:

provider-defined

Possible forms include:

- mass
- area
- volume
- proprietary score

Do not convert between forms without a documented rule.

---

## Bod Pod Body Fat Percentage

Body-fat percentage estimated through air-displacement plethysmography.

Unit:

`%`

---

## Bod Pod Fat Mass

Fat mass estimated by Bod Pod.

Unit:

`lb`

---

## Bod Pod Fat-Free Mass

All non-fat mass estimated by Bod Pod.

Unit:

`lb`

Includes:

- water
- bone
- organs
- muscle
- other non-fat tissue

It is hydration-sensitive and is not equivalent to DEXA lean soft-tissue mass.

---

# Training Terms

## B-Blocks

Internal naming convention for governed training modules.

Training blocks are logged as executed.

---

## B1 — Incline Treadmill

Incline treadmill session.

Typical logged fields:

- duration
- incline
- speed
- breathing constraint
- completion context
- relevant deviations

Example:

`B1: 52 min | 10% | 3.3 mph`

---

## B3 / B4 — Locomotion or Structural Circuits

Historical or context-dependent movement circuits emphasizing locomotion and structural integrity.

Possible logged fields:

- circuit count
- movement
- repetitions
- distance
- duration
- execution notes

Historical naming does not establish current protocol status.

---

## Load Integration

Current structured resistance and movement-integration layer.

May include:

- trap-bar movement
- pull-ups
- push-ups
- dead hangs
- mobility
- other explicitly governed components

Narrative evidence may document:

- execution quality
- grip behavior
- divided attention
- force modulation
- discomfort
- context variation

A complete canonical daily Load Integration export does not yet exist.

---

## Circuit

One complete pass through a defined movement sequence.

Unit:

`count`

The sequence must be known before circuit counts are compared across sessions.

---

# Recovery and Physiology Terms

## Heart Rate

Heart rate reported by a wearable or measurement device.

Unit:

`bpm`

Whenever possible, specify:

- daily average
- resting
- sleeping average
- minimum
- maximum
- exercise average
- exercise peak
- spot measurement

---

## Heart-Rate Variability

Heart-rate variability reported by a wearable or measurement device.

Unit:

typically `ms`

Always distinguish:

- daily average HRV
- sleep HRV
- overnight HRV
- morning spot HRV
- provider-specific HRV

HRV comparisons should remain within the same device and metric definition whenever possible.

---

## Steps

Provider-reported daily step count.

Unit:

`count`

Steps are an activity proxy.

They are not a complete training-exposure metric.

---

## Wearable Calories

Provider-estimated energy expenditure.

Unit:

`kcal`

Device estimates may vary by:

- algorithm
- body profile
- wear time
- heart-rate availability
- firmware
- application version

Use primarily for within-device trend comparison.

---

## SpO₂

Wearable-estimated peripheral oxygen saturation.

Unit:

`%`

Consumer wearable SpO₂ is an observational estimate rather than a clinical arterial measurement.

---

# Files and Naming

## Snapshots

Location:

`/snapshots/`

Snapshot structure may contain:

- source artifacts
- epoch context files
- checksum manifests
- event-specific subdirectories

Preferred naming:

`YYYY-MM-DD_<capture>_<source>.<ext>`

Historical formats remain preserved rather than being retroactively renamed without need.

---

## Source Exports

Location:

`/data/source_exports/`

Preferred structure:

`provider/acquisition-date/`

Example:

`data/source_exports/ringconn/2026-07-21/`

Each acquisition package should include:

- original export files
- `README.md`
- `checksums.txt`

Source exports are organized by acquisition event rather than measurement date.

---

## Reports

### Weekly Reports

Location:

`/reports/`

Naming:

`YYYY-W##.md`

Example:

`2026-W29.md`

---

### Capture Reports

Location:

`/reports/`

Naming:

`YYYY-MM_<capture>-report.md`

Capture reports are used selectively for discrete measurement events.

Weekly reports remain the primary recurring interpretation layer.

---

## Current State

File:

`LATEST.md`

Updated:

- during weekly closeout
- when a material archive-state change occurs
- when the active observation window changes
- when a major measurement cycle is completed

`LATEST.md` is a current-state orientation document.

It is not a primary evidence source.

---

# Change Control

When an existing definition materially changes:

1. update this document
2. identify affected datasets or reports
3. record the change in `CHANGELOG.md`
4. preserve prior values and meanings through Git history
5. assess whether a schema migration is required
6. apply release-version changes only when required by `VERSIONING.md`

Adding documentation for a newly preserved source does not automatically require:

- renaming historical fields
- restructuring existing datasets
- creating normalized trackers
- issuing a new archival release

---

## Current Wearable Disposition

As of the 2026-07-21 RingConn acquisition:

- direct sleep, activity, and vital-sign exports are preserved
- checksums are registered
- source-field semantics are documented
- canonical sleep data remain unchanged
- normalization remains deferred
- periodic provider exports are the current maintenance model
- targeted source reconciliation may proceed independently

No normalized wearable dataset is declared active by this document.
