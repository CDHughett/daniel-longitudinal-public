# Data Quality Notes

**Status:** Active  
**Created:** 2026-07-11  
**Last updated:** 2026-07-22  
**Scope:** Known data-quality questions requiring source reconciliation

---

## Purpose

This document records suspected transcription, field-mapping, completeness, provider-output, timestamp, or source-comparability issues in the structured datasets and preserved source exports.

A data-quality note does not automatically establish that a recorded value is incorrect.

Its purpose is to:

- preserve the original observation
- identify the exact field, date, or source interval under review
- prevent unsupported correction
- define the source evidence required for resolution
- preserve a traceable correction path
- distinguish structural validity from semantic validity
- distinguish source preservation from canonical integration
- separate provider anomalies from biological observations

Canonical datasets remain unchanged until source evidence, date semantics, and correction rules support a governed modification.

---

## Governing Rules

- Do not infer replacement values from neighboring dates.
- Do not calculate replacement values from percentages unless the original source explicitly supports that calculation.
- Do not silently repair suspicious values.
- Do not overwrite an unresolved value merely because another value appears more plausible.
- Do not bulk-replace curated records from a later vendor export.
- Do not assume that two records with the same calendar date are duplicates.
- Do not collapse multiple sleep episodes without a declared aggregation rule.
- Do not infer that an absent date represents zero, no sleep, no activity, or intentional non-use.
- Do not assume that vendor timestamps represent UTC or local civil time without source documentation.
- Preserve byte-registered source exports without modification.
- Preserve all corrections through Git history.
- Document the source used for every correction.
- Record unresolved missingness honestly when the original source is unavailable or insufficient.
- Keep interpretation proportional to the fields affected.
- Do not invalidate an entire row when only one field or field group is under review.

A contemporaneous primary artifact normally controls when it conflicts with a manually transcribed value.

A later direct vendor export is strong source evidence, but it is not automatically treated as superior when:

- provider algorithms may have changed
- historical records may have been reprocessed
- date assignment differs
- session aggregation differs
- the exported field is not semantically identical
- the export does not contain the corresponding field

Source precedence must therefore be evaluated field by field.

---

## Status Definitions

| Status | Meaning |
|---|---|
| Open | Source reconciliation has not been completed |
| Source located | Relevant source evidence is available but has not yet been fully reconciled |
| Source located — partial | Source evidence covers only part of the affected field group |
| Correction candidate identified | Source comparison indicates a likely correction, but implementation has not yet been authorized |
| Confirmed valid | The recorded value matches the applicable source |
| Correction required | The applicable source confirms that the structured value is incorrect and correction rules are satisfied |
| Corrected | The structured value has been updated with documented provenance |
| Unresolvable | Available evidence is insufficient to determine the correct value |

A status may be narrowed to one field while another field in the same record remains open.

---

# RingConn Direct Source Package

## Status

Source located and integrity-registered.

Canonical integration not yet authorized.

## Source Directory

[`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/)

## Acquisition Event

- Provider: RingConn
- Wearable: RingConn Gen 2
- Acquisition date: 2026-07-21
- Acquisition method: direct user-account export
- Preservation state: byte-preserved
- Integrity state: SHA-256 manifest registered and verified
- Canonical transformation state: not yet performed

## Included Files

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- `README.md`
- `checksums.txt`

## Structural Inventory

| File | Data rows | Fields |
|---|---:|---:|
| `ringconn-sleep-export.csv` | 366 | 10 |
| `ringconn-activity-export.csv` | 360 | 3 |
| `ringconn-vital-signs-export.csv` | 360 | 10 |

The data-row counts exclude the header row.

## Preliminary Privacy Review

The pre-publication scan identified:

- no obvious administrative-identifier terms in the headers
- no email-like values
- expected wearable-domain fields only

This screening reduces obvious public-distribution risk.

It does not establish that the data are anonymous or that every possible identifier pattern has been excluded.

## Source Role

The package preserves vendor-exported observations.

It does not automatically:

- replace canonical datasets
- resolve existing quality notes
- establish a daily primary key
- establish timezone semantics
- identify the primary sleep episode
- authorize historical backfill
- establish that provider-export values are unchanged from the original observation date

The source package must remain unchanged while mapping and reconciliation occur separately.

---

# DQ-001 — Possible Sleep-Field Duplication

## Status

**Source located — partial**

A correction candidate has been identified for `awake_min`.

`awakenings_count` remains unresolved because the direct export does not contain an awakening-count field.

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

## Affected Dates

2026-05-18 through 2026-05-31

## Affected Fields

- `awake_min`
- `awakenings_count`

## Original Observation

Across 14 consecutive canonical rows, the value recorded in `awake_min` exactly matches the value recorded in `awakenings_count`.

Observed paired values range from 3 to 5.

The pattern:

- begins abruptly on 2026-05-18
- persists through 2026-05-31
- ends before 2026-06-01
- appears alongside sleep-efficiency values ranging from 86% to 96%

Because awake duration and awakening count represent different concepts, exact duplication across a continuous 14-day block was considered suspicious.

Potential explanations included:

- copied-field transcription
- field-mapping confusion
- source-interface misreading
- provider-labeling behavior
- valid source behavior not yet understood

## Direct-Export Comparison

The direct RingConn sleep export includes:

- `Sleep Stages - Awake(min)`

It does not include:

- awakening count

Using the preliminary wake-date mapping, the comparison is:

| Date | Canonical `awake_min` | Canonical `awakenings_count` | Direct-export awake minutes |
|---|---:|---:|---:|
| 2026-05-18 | 4 | 4 | 22 |
| 2026-05-19 | 5 | 5 | 38 |
| 2026-05-20 | 5 | 5 | 28 |
| 2026-05-21 | 5 | 5 | 10 |
| 2026-05-22 | 4 | 4 | 22 |
| 2026-05-23 | 4 | 4 | 17 |
| 2026-05-24 | 5 | 5 | 17 |
| 2026-05-25 | 4 | 4 | 13 |
| 2026-05-26 | 4 | 4 | 13 |
| 2026-05-27 | 4 | 4 | 13 |
| 2026-05-28 | 4 | 4 | 17 |
| 2026-05-29 | 4 | 4 | 21 |
| 2026-05-30 | 4 | 4 | 15 |
| 2026-05-31 | 3 | 3 | 8 |

The direct export does not support the current canonical `awake_min` values.

The pattern strongly supports the original suspicion that awakening-count values were copied into the awake-minute field.

However, the export cannot validate the canonical awakening counts because no equivalent awakening-count field is included.

## Preliminary Disposition

### `awake_min`

Status:

**Correction candidate identified**

The source values provide a direct candidate replacement series, subject to:

- confirmation of wake-date assignment
- confirmation that the export field is equivalent to canonical `awake_min`
- confirmation that the relevant rows represent the intended primary sleep episodes
- documentation of the correction commit
- changelog registration

### `awakenings_count`

Status:

**Open**

The current values cannot be confirmed from the direct export.

Original RingConn application screenshots or another contemporaneous source remain necessary.

## Evaluation Restriction

Until reconciliation is completed:

- do not use canonical `awake_min` from the affected dates for quantitative awake-duration analysis
- do not treat agreement between `awake_min` and `awakenings_count` as biological evidence
- do not derive replacement awake minutes from sleep efficiency
- do not alter `awakenings_count` from the direct export
- do not automatically overwrite other fields in the affected rows
- retain the rows for date continuity and unaffected-field analysis

Other fields remain usable according to their normal limitations unless separate comparison identifies another issue.

## Resolution Rule

For `awake_min`:

1. approve the source-to-canonical date mapping
2. verify the primary source session for each affected date
3. confirm field equivalence
4. correct only `awake_min`
5. preserve the old values through Git history
6. update this note to `Corrected`
7. document the correction in `CHANGELOG.md`

For `awakenings_count`:

- compare against original RingConn screenshots or equivalent contemporaneous evidence
- retain the current values as unresolved if that source cannot be recovered

---

# DQ-002 — Sleep-Stage Total Reconciliation

## Status

**Source located — correction candidate identified**

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

## Affected Date

2026-03-31

## Canonical Recorded Values

| Field | Value |
|---|---:|
| `total_sleep_min` | 298 |
| `deep_sleep_min` | 55 |
| `light_sleep_min` | 207 |
| `rem_sleep_min` | 20 |
| Sum of recorded sleep stages | 282 |
| Difference from total sleep | 16 |

The recorded canonical stage percentages total 94.7%.

## Direct-Export Record

The direct export contains a sleep episode:

- Start: `2026-03-30 21:21:18`
- End: `2026-03-31 03:01:43`
- Falling asleep: `2026-03-30 21:33:48`
- Wake-up: `2026-03-31 02:54:13`

| Source field | Exported value |
|---|---:|
| Sleep time ratio | 87% |
| Time asleep | 298 min |
| Awake | 23 min |
| REM | 20 min |
| Light sleep | 223 min |
| Deep sleep | 55 min |
| Sum of exported sleep stages | 298 min |

## Comparison

The direct export matches the canonical values for:

- total sleep
- REM sleep
- deep sleep

The direct export differs only in light sleep:

| Field | Canonical | Direct export | Difference |
|---|---:|---:|---:|
| Light sleep | 207 | 223 | 16 |

The 16-minute source difference exactly accounts for the canonical stage-total discrepancy.

## Preliminary Disposition

The direct export indicates that:

- `light_sleep_min = 223`

is the likely source-supported value.

This remains a correction candidate rather than an implemented correction until:

- wake-date mapping is formally approved
- source-field equivalence is documented
- provider-history limitations are considered
- the correction is made through a dedicated traceable commit

## Evaluation Restriction

Until correction is authorized:

- do not force the canonical stage values to equal total sleep
- do not distribute the missing 16 minutes across stages
- do not infer an unrecorded stage
- preserve the existing canonical row
- disclose the discrepancy in stage-composition analysis

## Resolution Rule

If the mapping review confirms equivalence:

- replace only `light_sleep_min`
- recalculate only directly dependent percentage fields when governed by the canonical schema
- preserve unrelated fields
- update this note to `Corrected`
- identify the direct RingConn export as the supporting source
- record the correction in `CHANGELOG.md`

---

# DQ-003 — Sleep-Stage Total Reconciliation

## Status

**Source located — correction candidate identified**

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

## Affected Date

2026-04-02

## Canonical Recorded Values

| Field | Value |
|---|---:|
| `total_sleep_min` | 336 |
| `deep_sleep_min` | 60 |
| `light_sleep_min` | 217 |
| `rem_sleep_min` | 45 |
| Sum of recorded sleep stages | 322 |
| Difference from total sleep | 14 |

The recorded canonical stage percentages total 95.9%.

## Direct-Export Record

The direct export contains a sleep episode:

- Start: `2026-04-01 20:43:13`
- End: `2026-04-02 03:02:08`
- Falling asleep: `2026-04-01 20:53:13`
- Wake-up: `2026-04-02 02:49:38`

| Source field | Exported value |
|---|---:|
| Sleep time ratio | 89% |
| Time asleep | 336 min |
| Awake | 21 min |
| REM | 45 min |
| Light sleep | 231 min |
| Deep sleep | 60 min |
| Sum of exported sleep stages | 336 min |

## Comparison

The direct export matches the canonical values for:

- total sleep
- REM sleep
- deep sleep

The direct export differs only in light sleep:

| Field | Canonical | Direct export | Difference |
|---|---:|---:|---:|
| Light sleep | 217 | 231 | 14 |

The 14-minute source difference exactly accounts for the canonical stage-total discrepancy.

## Preliminary Disposition

The direct export indicates that:

- `light_sleep_min = 231`

is the likely source-supported value.

This remains a correction candidate rather than an implemented correction until:

- wake-date mapping is formally approved
- source-field equivalence is documented
- provider-history limitations are considered
- the correction is made through a dedicated traceable commit

## Evaluation Restriction

Until correction is authorized:

- do not force the canonical stage values to equal total sleep
- do not distribute the missing 14 minutes across stages
- do not infer an unrecorded stage
- preserve the existing canonical row
- disclose the discrepancy in stage-composition analysis

## Resolution Rule

If the mapping review confirms equivalence:

- replace only `light_sleep_min`
- recalculate only directly dependent percentage fields when governed by the canonical schema
- preserve unrelated fields
- update this note to `Corrected`
- identify the direct RingConn export as the supporting source
- record the correction in `CHANGELOG.md`

---

# DQ-004 — Sleep Date Assignment, Timezone, and Timestamp Precision

## Status

Open

## Source

[`source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

## Affected Fields

- `Start Time`
- `End Time`
- `Falling Asleep Time`
- `Wake-up time`

## Observation

The sleep export does not contain a separate daily `Date` field.

Each row contains timestamps for:

- session start
- session end
- estimated falling-asleep time
- wake-up time

The export does not state:

- timezone
- UTC offset
- daylight-saving status
- whether the application assigns the record to start date or wake date
- how travel across time zones is represented
- whether timestamps were normalized at export time

## Preliminary Date-Mapping Evidence

Preliminary comparison with the canonical sleep dataset strongly favors assigning the primary overnight record to the wake date rather than the start date.

The DQ-002 and DQ-003 source rows align with the canonical dates when assigned by wake date.

This is evidence for the likely convention.

It is not yet a formally approved mapping rule.

## Mixed Timestamp Precision

Most exported sleep timestamps include seconds.

Six source rows use minute-only timestamps across all four timestamp fields.

The affected session start dates are:

- 2026-06-20
- 2026-06-28
- 2026-07-03
- 2026-07-17
- 2026-07-18
- 2026-07-19

A strict parser that assumes one timestamp format may therefore fail or silently convert these rows to missing timestamps.

## Evaluation Restriction

Until a mapping rule is registered:

- do not create canonical dates solely from start time
- do not create canonical dates solely from wake time without documenting the rule
- do not assume UTC
- do not apply timezone conversion
- do not infer missing seconds
- do not treat minute-only precision as measurement to the second
- do not use strict single-format parsing

## Required Resolution

The source-to-canonical mapping should define:

1. the daily date-assignment rule
2. treatment of overnight sessions
3. treatment of same-day naps
4. treatment of sessions crossing time zones
5. treatment of daylight-saving transitions
6. parsing of timestamps with and without seconds
7. preservation of original timestamp strings
8. representation of unresolved timezone status

---

# DQ-005 — Multiple Sleep Episodes and Daily Cardinality

## Status

Open

## Source

[`source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

## Observation

The sleep export contains 366 source rows but does not represent a strict one-row-per-date daily dataset.

Under preliminary wake-date grouping, eight dates contain two sleep episodes:

- 2025-10-09
- 2025-11-02
- 2025-11-09
- 2025-11-17
- 2025-12-25
- 2026-05-31
- 2026-07-03
- 2026-07-04

The paired records generally consist of:

- one primary overnight sleep episode
- one daytime or secondary sleep episode

These are not presumed duplicate rows.

They may represent:

- naps
- split sleep
- recovery sleep
- provider-detected secondary sessions
- sessions requiring separate classification

## Canonical Risk

A one-row-per-day normalization could silently lose information if it:

- discards the shorter session
- keeps only the first row
- keeps only the final row
- sums sessions without a declared rule
- assigns both sessions to separate dates
- treats the secondary episode as a duplicate
- overwrites the primary overnight record

## Evaluation Restriction

Until session rules are approved:

- preserve every source row
- do not deduplicate by calendar date
- do not sum multiple sessions
- do not discard naps
- do not merge awake and stage durations
- do not force secondary episodes into the existing canonical sleep dataset

## Required Resolution

A normalized sleep architecture should consider preserving two layers:

### Session-Level Dataset

One row per exported sleep episode.

Potential primary key:

- source acquisition event
- original start timestamp
- original end timestamp

### Daily Dataset

One row per governed day, derived under explicit rules.

The mapping must define:

- primary sleep episode
- secondary sleep episode
- nap handling
- daily totals
- date assignment
- whether daily aggregation is permitted
- how the derivation remains reversible to source rows

---

# DQ-006 — Cross-Domain Missing Dates

## Status

Open

## Sources

- [`ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)
- [`ringconn-activity-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-activity-export.csv)
- [`ringconn-vital-signs-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-vital-signs-export.csv)

## Activity and Vital-Signs Coverage

The activity and vital-signs exports each contain:

- 360 data rows
- one row per represented date
- no duplicate represented dates

Both span:

- first represented date: 2025-07-21
- last represented date: 2026-07-20

Both omit the same five dates:

- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08

The matching absence across both files may indicate:

- no device wear
- synchronization interruption
- provider export omission
- account or application interruption
- device unavailability
- another common capture disruption

The source files do not identify the cause.

## Sleep Coverage

Under provisional wake-date grouping, the sleep export contains no represented sleep session for:

- 2025-08-10
- 2025-10-23
- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08
- 2026-01-09

This list remains provisional because sleep date assignment has not yet been formally approved.

## Interpretation Boundary

An absent source row does not establish:

- zero activity
- zero heart rate
- zero HRV
- zero SpO₂
- no sleep
- no recovery
- deliberate device removal
- a biological event

## Evaluation Restriction

- Do not insert zero-filled rows.
- Do not forward-fill measurements.
- Do not interpolate missing values.
- Do not infer device non-wear without supporting evidence.
- Do not classify the gap as illness, travel, or behavioral disruption without contemporaneous context.
- Preserve the missing interval explicitly in normalized datasets.

## Required Resolution

Review available contemporaneous evidence for the affected dates, including:

- application screenshots
- weekly reports
- travel records
- device-use notes
- account export history
- any known synchronization or hardware events

If no evidence explains the gap, classify it as:

- source missingness — cause unknown

---

# DQ-007 — November 17 Unclassified Sleep-Stage Session

## Status

Open

## Source

[`source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

## Affected Session

- Start: `2025-11-17 15:15:29`
- End: `2025-11-17 17:40:29`
- Falling asleep: `2025-11-17 15:40:29`
- Wake-up: `2025-11-17 17:17:59`

## Exported Values

| Field | Value |
|---|---:|
| Sleep time ratio | 68% |
| Time asleep | 98 min |
| Awake | 0 min |
| REM | 0 min |
| Light sleep | 0 min |
| Deep sleep | 0 min |
| Sum of classified sleep stages | 0 min |
| Difference from time asleep | 98 min |

## Observation

This is the only source row in which:

- `Time Asleep(min)` is greater than zero
- every sleep-stage field is zero

All other sleep-export rows have classified sleep-stage minutes summing to total time asleep.

The session may represent:

- a provider-recognized nap without stage classification
- incomplete stage processing
- a provider export defect
- an application-versus-export discrepancy
- a session below a stage-classification threshold
- another undocumented provider rule

The record must not be interpreted as 98 minutes of biologically stage-free sleep.

## Evaluation Restriction

Until source clarification:

- retain the source row unchanged
- do not distribute 98 minutes across stages
- do not treat zero stages as measured absence of REM, light, and deep sleep
- do not silently discard the session
- do not include the row in stage-proportion analysis
- do not merge it into an overnight record without a declared rule
- treat total sleep duration as provider-reported but stage classification as unavailable

## Required Source Evidence

Review:

- the RingConn application display for the session
- any contemporaneous screenshot
- provider documentation regarding nap-stage classification
- adjacent synchronization history
- whether re-export reproduces the same row

## Resolution Categories

The row may eventually be classified as:

- valid unclassified session
- provider export omission
- provider processing anomaly
- source-backed correction required
- unresolvable

---

# DQ-008 — Curated Versus Direct-Export Differences

## Status

Open

## Datasets

- Curated canonical dataset: [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)
- Direct source export: [`ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

## Preliminary Comparison Method

A preliminary, non-canonical comparison was performed using:

- canonical dates represented in both layers
- provisional wake-date assignment
- the longest source sleep episode when more than one source row occurred on a date
- direct field comparison without automatic correction

The overlap contained 161 canonical dates.

This comparison is diagnostic only.

It is not an approved transformation procedure.

## Preliminary Difference Counts

| Field | Comparable dates | Exact matches | Differences |
|---|---:|---:|---:|
| Total sleep | 161 | 110 | 51 |
| Deep sleep | 161 | 115 | 46 |
| Light sleep | 113 | 72 | 41 |
| REM sleep | 113 | 84 | 29 |
| Awake minutes | 113 | 18 | 95 |
| Sleep efficiency | 99 | 48 | 51 |

The largest systematic difference occurs in awake minutes, including the DQ-001 interval.

## Possible Explanations

Differences may reflect:

- manual transcription errors
- application-screen rounding
- export precision
- date assignment
- primary-versus-secondary session selection
- provider algorithm changes
- retrospective provider reprocessing
- corrected dates in the canonical archive
- source fields not equivalent to canonical fields
- spreadsheet or workbook transfer errors
- application-versus-export presentation differences

A difference does not automatically establish that the direct export is correct or that the curated value is wrong.

## Required Difference Classification

Each compared field should eventually be classified as:

- exact match
- rounding-only difference
- formatting difference
- date-assignment difference
- session-selection difference
- unit difference
- manual transcription error
- export omission
- curated omission
- provider revision
- provider anomaly
- unresolved discrepancy

## Evaluation Restriction

- Do not bulk-overwrite the canonical sleep dataset.
- Do not prefer the export solely because it is machine-generated.
- Do not preserve the curated value solely because it was entered first.
- Do not combine comparison results across fields without field-level review.
- Do not remove confidence labels or subjective context from the canonical layer.
- Do not treat the direct export as containing fields it does not actually provide.
- Do not use the preliminary longest-session rule as a final aggregation rule.

## Relationship to DQ-001 Through DQ-003

The direct export provides strong candidate reconciliation evidence for:

- DQ-001 `awake_min`
- DQ-002 `light_sleep_min`
- DQ-003 `light_sleep_min`

It does not independently resolve:

- DQ-001 `awakenings_count`
- provider-history stability
- timezone interpretation
- multiple-session policy
- all other curated-versus-export differences

---

## Current Dataset Disposition

No immediate change to [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) is authorized by this document.

Current disposition:

- DQ-001 `awake_min` — correction candidate identified
- DQ-001 `awakenings_count` — unresolved
- DQ-002 `light_sleep_min` — correction candidate identified
- DQ-003 `light_sleep_min` — correction candidate identified
- DQ-004 date and timestamp mapping — open
- DQ-005 multiple-session handling — open
- DQ-006 missing-date classification — open
- DQ-007 November 17 stage classification — open
- DQ-008 broader curated-versus-export reconciliation — open

The canonical rows remain:

- syntactically valid
- date-continuous within their represented interval
- parseable
- preserved in their current structured form
- subject to the field-specific restrictions documented above

The RingConn source exports remain:

- byte-preserved
- checksum-registered
- separate from canonical data
- available for governed reconciliation

These findings do not invalidate:

- the overall sleep date sequence
- unaffected fields
- source-export integrity
- weekly report continuity
- checksum integrity
- the broader recovery record

They narrow confidence and define the required correction path.

---

## Source-Reconciliation Procedure

When source evidence becomes available or is integrated:

1. verify the source-export checksum
2. preserve the original source bytes
3. identify the source acquisition date
4. verify the source row or session
5. establish the date-assignment rule
6. identify whether multiple sessions exist
7. select the applicable source session under a documented rule
8. compare each relevant field
9. confirm field semantics and units
10. distinguish application display from direct export
11. classify each discrepancy
12. consider possible provider reprocessing
13. avoid modifying unrelated fields
14. save or reference supporting evidence
15. update the applicable data-quality status
16. correct the canonical CSV only when supported
17. record the correction in `CHANGELOG.md`
18. rerun CSV parsing and semantic validation
19. verify dependent percentages or derived fields
20. assess whether reports or analyses require a correction note

A source-backed correction is archive maintenance.

It is not a new biological observation.

---

## Correction Commit Boundary

When corrections are authorized, they should be separated by issue when practical.

Recommended sequence:

1. approve and document the RingConn source-to-canonical mapping
2. correct DQ-002 and DQ-003 light-sleep values
3. correct DQ-001 awake-minute values
4. resolve or retain uncertainty for awakening counts
5. update this document
6. update `CHANGELOG.md`
7. run a focused continuity and semantic audit

Do not combine broad historical normalization with narrow DQ-001 through DQ-003 corrections unless the transformation has been separately reviewed and reproduced.

---

## Future Validation Requirements

Future automated sleep and wearable validation should test for:

- duplicate canonical dates
- multiple source sessions per date
- missing dates
- cross-domain missing-date alignment
- malformed row widths
- missing required fields
- mixed timestamp precision
- invalid timestamp parsing
- unresolved timezone status
- exact duplication across conceptually distinct fields
- sleep-stage sums that differ from total sleep
- positive total sleep with zero classified stages
- stage percentages that materially differ from recorded durations
- impossible percentages
- negative durations
- implausible field ranges
- abrupt field-behavior changes
- source-label changes
- unit changes
- provider-schema changes
- source-export versus curated discrepancies
- direct-export values that may have been retrospectively revised

Automated flags should initiate review.

They should not automatically rewrite source or canonical data.

---

## Planned Mapping Artifact

Before normalized wearable trackers are created, add a source-to-canonical mapping document defining:

- source files
- source fields
- target fields
- units
- date assignment
- timezone handling
- timestamp precision
- primary and secondary sleep-session rules
- missingness
- duplicate handling
- provider anomalies
- transformation procedure
- reproducibility requirements
- correction provenance

Potential normalized datasets remain planned rather than active:

- `wearable_sleep_daily_v1.csv`
- `wearable_activity_daily_v1.csv`
- `wearable_vitals_daily_v1.csv`

A session-level sleep dataset may also be required before a daily sleep dataset can be derived safely.

---

## Related Documents

- [`../docs/audits/2026-07-11-saturday-audit.md`](../docs/audits/2026-07-11-saturday-audit.md)
- [`../docs/audits/2026-07-22-wednesday-audit.md`](../docs/audits/2026-07-22-wednesday-audit.md)
- [`../methodology/data-collection.md`](../methodology/data-collection.md)
- [`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)
- [`DATA_COVERAGE.md`](./DATA_COVERAGE.md)
- [`source_exports/ringconn/2026-07-21/README.md`](./source_exports/ringconn/2026-07-21/README.md)
- [`source_exports/ringconn/2026-07-21/checksums.txt`](./source_exports/ringconn/2026-07-21/checksums.txt)

---

## Version Note

This document was created on 2026-07-11 after semantic review identified questions that were not detectable through CSV parsing and date-continuity checks alone.

It was expanded on 2026-07-22 after preservation and preliminary review of the direct RingConn annual export package.

The 2026-07-22 update:

- registers the direct source package
- identifies correction candidates for DQ-001 through DQ-003
- records mixed timestamp precision
- records multiple sleep episodes
- records cross-domain missing dates
- documents the November 17 unclassified-stage session
- establishes curated-versus-export reconciliation boundaries
- prohibits immediate bulk correction

No canonical source value was changed as part of this documentation commit.
