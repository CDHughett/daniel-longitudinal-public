# Data Quality Notes

**Status:** Active  
**Created:** 2026-07-11  
**Last updated:** 2026-09-06  
**Scope:** Known data-quality questions requiring source reconciliation or analytical restriction

---

## Purpose

This document records suspected transcription, field-mapping, completeness, provider-output, timestamp, or source-comparability issues in structured datasets and preserved source exports.

A data-quality note does not automatically establish that a recorded value is incorrect.

Its purpose is to:

- preserve the original observation
- identify the exact field, date, source row, or interval under review
- prevent unsupported correction
- define the evidence required for resolution
- preserve a traceable correction path
- distinguish structural validity from semantic validity
- distinguish source preservation from curated integration
- separate provider anomalies from biological observations
- define when a limitation affects only a narrow analysis rather than the entire archive

Curated datasets remain unchanged until source evidence, field equivalence, date semantics, and correction rules support a governed modification.

---

## Governing Rules

- Do not infer replacement values from neighboring dates.
- Do not calculate replacement values from percentages unless the source explicitly supports that calculation.
- Do not silently repair suspicious values.
- Do not overwrite an unresolved value merely because another value appears more plausible.
- Do not bulk-replace curated records from a later provider export.
- Do not assume that two records sharing a calendar date are duplicates.
- Do not collapse multiple sleep episodes without a declared analytical rule.
- Do not infer that an absent source date represents zero, no sleep, no activity, or intentional non-use.
- Do not assume provider timestamps represent UTC or a known local timezone without source documentation.
- Preserve registered source exports without modification.
- Preserve corrections through Git history.
- Document the supporting source for every correction.
- Record unresolved missingness honestly when the source is unavailable or insufficient.
- Keep interpretation proportional to the affected fields.
- Do not invalidate an entire row when only one field or field group is under review.
- Do not create a permanent transformed dataset solely to resolve a narrow transcription question.
- Use the smallest correction or analytical procedure sufficient for the defined need.

A contemporaneous primary artifact normally controls when it conflicts with a manual transcription of the same metric.

A later direct provider export is strong source evidence, but it is not automatically superior when:

- provider algorithms may have changed
- historical records may have been reprocessed
- date assignment differs
- session aggregation differs
- the exported field is not semantically identical
- the export omits the corresponding field
- the application and export represent different provider states

Source precedence must therefore be evaluated field by field.

---

## Status Definitions

| Status | Meaning |
|---|---|
| Open | Reconciliation has not been completed |
| Source located | Relevant source evidence is available but has not been fully reconciled |
| Source located — partial | Source evidence covers only part of the affected field group |
| Correction candidate identified | Source comparison indicates a likely narrow correction, but implementation has not yet been authorized |
| Confirmed valid | The recorded value matches the applicable source |
| Correction required | Applicable source evidence confirms that the curated value is incorrect and correction conditions are satisfied |
| Corrected | The curated value has been updated with documented provenance |
| Analytical restriction | The source value remains preserved, but a defined use or interpretation is restricted |
| Unresolvable | Available evidence is insufficient to determine the correct value |

A status may be narrowed to one field while another field in the same record remains open.

---

# RingConn Direct Source Package

## Status

**Source located, integrity registered, and externally verified.**

No broad canonical integration is currently required or scheduled.

The package is available for:

- targeted reconciliation
- source verification
- defined historical analysis
- future reproducible transformation if a concrete need arises

---

## Source Directory

[`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/)

---

## Acquisition Event

- Provider: RingConn
- Wearable: RingConn Gen 2
- Acquisition date: 2026-07-21
- Review and ingestion date: 2026-07-22
- Acquisition method: direct user-account export
- Preservation state: byte-preserved
- Integrity state: SHA-256 manifest registered and verified
- External distribution state: verified from a fresh GitHub ZIP
- Curated transformation state: not performed
- Routine normalization state: deferred

---

## Included Files

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- `README.md`
- `checksums.txt`

---

## Structural Inventory

| File | Data rows | Fields | Verified bytes |
|---|---:|---:|---:|
| `ringconn-sleep-export.csv` | 366 | 10 | 38,703 |
| `ringconn-activity-export.csv` | 360 | 3 | 8,171 |
| `ringconn-vital-signs-export.csv` | 360 | 10 | 16,059 |

The data-row counts exclude the header row.

---

## Byte-Preservation Verification

The source-export CSVs are protected by the repository rule:

```gitattributes
data/source_exports/**/*.csv -text
```

Verification confirmed:

- the repository files match the original downloaded files byte-for-byte
- original CRLF line endings are retained
- the existing checksum manifest remained unchanged
- all three source-export SHA-256 values pass
- a fresh GitHub ZIP preserves the same bytes
- all registered archive checksum targets pass

The package is therefore considered mechanically preserved.

Mechanical integrity does not establish semantic validity for every provider field or row.

---

## Preliminary Privacy Review

The pre-publication scan identified:

- no obvious administrative-identifier fields in the exported headers
- no email-like values
- expected wearable-domain fields only

This screening reduces obvious public-distribution risk.

It does not establish:

- complete anonymity under every possible inference
- clinical validity
- field-level semantic equivalence
- suitability for automatic integration into curated datasets

---

## Source Role

The package preserves provider-exported observations.

It does not automatically:

- replace curated datasets
- resolve existing quality notes
- establish a daily primary key
- establish timezone semantics
- identify a primary sleep episode
- authorize bulk historical backfill
- prove that provider-export values are unchanged from the original observation date
- require creation of normalized wearable trackers

The source package remains unchanged.

Any correction or analytical transformation must occur separately.

---

# DQ-001 — Possible Sleep-Field Duplication

## Status

**Source located — partial**

A correction candidate has been identified for `awake_min`.

`awakenings_count` remains unresolved because the direct export does not contain an awakening-count field.

---

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

---

## Affected Dates

2026-05-18 through 2026-05-31

---

## Affected Fields

- `awake_min`
- `awakenings_count`

---

## Original Observation

Across 14 consecutive curated rows, the value recorded in `awake_min` exactly matches the value recorded in `awakenings_count`.

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

---

## Direct-Export Comparison

The direct RingConn sleep export includes:

```text
Sleep Stages - Awake(min)
```

It does not include an awakening-count field.

Using provisional wake-date assignment, the comparison is:

| Date | Curated `awake_min` | Curated `awakenings_count` | Direct-export awake minutes |
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

The direct export does not support the current curated `awake_min` values.

The pattern provides strong candidate evidence that awakening-count values were copied into the awake-minute field.

The export cannot validate the curated awakening counts because no equivalent awakening-count field is present.

---

## Preliminary Disposition

### `awake_min`

Status:

**Correction candidate identified**

The exported values provide a candidate replacement series, subject to:

- confirmation of wake-date assignment
- confirmation that the selected source episode corresponds to the intended curated date
- confirmation that the export field is semantically equivalent to curated `awake_min`
- review of whether provider reprocessing materially affects correction authority
- a dedicated correction commit
- changelog registration

### `awakenings_count`

Status:

**Open**

The direct export cannot confirm or replace these values.

Original RingConn application screenshots or another contemporaneous source remain necessary.

---

## Evaluation Restriction

Until reconciliation is completed:

- do not use curated `awake_min` from the affected dates for quantitative awake-duration analysis
- do not treat agreement between `awake_min` and `awakenings_count` as biological evidence
- do not derive replacement awake minutes from sleep efficiency
- do not alter `awakenings_count` using the direct export
- do not overwrite unrelated fields
- retain the affected rows for date continuity and unaffected-field analysis

Other fields remain usable under their normal limitations unless separately flagged.

---

## Resolution Rule

For `awake_min`:

1. verify the applicable source session for each date
2. confirm wake-date assignment
3. confirm field equivalence
4. assess whether provider reprocessing prevents a definitive correction
5. correct only `awake_min` if the evidence is sufficient
6. preserve the prior values through Git history
7. update this note
8. record the correction in `CHANGELOG.md`

For `awakenings_count`:

- compare against contemporaneous RingConn screenshots or equivalent evidence
- retain the current values as unresolved if no applicable source can be recovered

A complete normalized wearable dataset is not required to perform this narrow reconciliation.

---

# DQ-002 — Sleep-Stage Total Reconciliation

## Status

**Source located — correction candidate identified**

---

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

---

## Affected Date

2026-03-31

---

## Curated Recorded Values

| Field | Value |
|---|---:|
| `total_sleep_min` | 298 |
| `deep_sleep_min` | 55 |
| `light_sleep_min` | 207 |
| `rem_sleep_min` | 20 |
| Sum of recorded sleep stages | 282 |
| Difference from total sleep | 16 |

The recorded curated stage percentages total 94.7%.

---

## Direct-Export Record

The direct export contains the following sleep episode:

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

---

## Comparison

The direct export matches the curated values for:

- total sleep
- REM sleep
- deep sleep

It differs only in light sleep:

| Field | Curated | Direct export | Difference |
|---|---:|---:|---:|
| Light sleep | 207 | 223 | 16 |

The 16-minute difference exactly accounts for the stage-total discrepancy.

---

## Preliminary Disposition

The direct export indicates that:

```text
light_sleep_min = 223
```

is the likely source-supported value.

This remains a correction candidate until:

- the source episode is confirmed as the applicable overnight session
- wake-date assignment is confirmed
- field equivalence is documented
- provider-history limitations are considered
- the correction is implemented through a dedicated commit

---

## Evaluation Restriction

Until correction is authorized:

- do not force the curated stage values to equal total sleep
- do not distribute the missing 16 minutes across stages
- do not infer an unrecorded stage
- preserve the existing curated row
- disclose the discrepancy in stage-composition analysis

---

## Resolution Rule

If the narrow source review confirms equivalence:

- replace only `light_sleep_min`
- recalculate only schema-defined dependent percentages, if applicable
- preserve unrelated fields
- update this note
- identify the direct RingConn export as the supporting source
- record the correction in `CHANGELOG.md`

A broader source-to-canonical mapping document is not required unless the correction cannot be explained and reproduced within the issue-specific record.

---

# DQ-003 — Sleep-Stage Total Reconciliation

## Status

**Source located — correction candidate identified**

---

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

---

## Affected Date

2026-04-02

---

## Curated Recorded Values

| Field | Value |
|---|---:|
| `total_sleep_min` | 336 |
| `deep_sleep_min` | 60 |
| `light_sleep_min` | 217 |
| `rem_sleep_min` | 45 |
| Sum of recorded sleep stages | 322 |
| Difference from total sleep | 14 |

The recorded curated stage percentages total 95.9%.

---

## Direct-Export Record

The direct export contains the following sleep episode:

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

---

## Comparison

The direct export matches the curated values for:

- total sleep
- REM sleep
- deep sleep

It differs only in light sleep:

| Field | Curated | Direct export | Difference |
|---|---:|---:|---:|
| Light sleep | 217 | 231 | 14 |

The 14-minute difference exactly accounts for the stage-total discrepancy.

---

## Preliminary Disposition

The direct export indicates that:

```text
light_sleep_min = 231
```

is the likely source-supported value.

This remains a correction candidate until:

- the source episode is confirmed as the applicable overnight session
- wake-date assignment is confirmed
- field equivalence is documented
- provider-history limitations are considered
- the correction is implemented through a dedicated commit

---

## Evaluation Restriction

Until correction is authorized:

- do not force the curated stage values to equal total sleep
- do not distribute the missing 14 minutes across stages
- do not infer an unrecorded stage
- preserve the existing curated row
- disclose the discrepancy in stage-composition analysis

---

## Resolution Rule

If the narrow source review confirms equivalence:

- replace only `light_sleep_min`
- recalculate only schema-defined dependent percentages, if applicable
- preserve unrelated fields
- update this note
- identify the direct RingConn export as the supporting source
- record the correction in `CHANGELOG.md`

A broader normalized wearable layer is not required for this correction.

---

# DQ-004 — Sleep Date Assignment, Timezone, and Timestamp Precision

## Status

**Open — analytical restriction**

---

## Source

[`source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

---

## Affected Fields

- `Start Time`
- `End Time`
- `Falling Asleep Time`
- `Wake-up time`

---

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

---

## Preliminary Date-Mapping Evidence

Preliminary comparison with the curated sleep dataset favors assigning a primary overnight record to its wake date.

The DQ-002 and DQ-003 records align with curated dates under wake-date assignment.

This supports issue-specific reconciliation.

It does not establish a universal timezone or date-assignment rule for every source row.

---

## Mixed Timestamp Precision

Most exported timestamps include seconds.

Six source rows use minute-only timestamps across all four timestamp fields.

Affected session start dates:

- 2026-06-20
- 2026-06-28
- 2026-07-03
- 2026-07-17
- 2026-07-18
- 2026-07-19

A strict parser requiring seconds may fail or convert these timestamps incorrectly.

---

## Evaluation Restriction

Without a defined analytical rule:

- do not create a universal daily date solely from start time
- do not assume UTC
- do not apply timezone conversion
- do not invent missing seconds
- do not treat minute-only timestamps as second-precision measurements
- do not use a strict single-format parser
- do not make cross-timezone or circadian-timing claims from the export alone

---

## Issue-Specific Use

A narrow correction may use wake-date assignment when:

- the session clearly crosses into the curated date
- only one plausible overnight session exists
- total sleep and multiple stage values independently match
- the rule is documented in the correction record

A complete global timestamp model is not required for every narrow transcription correction.

---

## Future Analytical Rule

Any future multi-row or historical timestamp analysis should define:

1. date assignment
2. overnight-session handling
3. same-day secondary-session handling
4. travel handling
5. daylight-saving treatment
6. parsing with and without seconds
7. preservation of original strings
8. unresolved timezone representation

This rule is optional until such analysis is undertaken.

---

# DQ-005 — Multiple Sleep Episodes and Daily Cardinality

## Status

**Open — analytical restriction**

---

## Source

[`source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

---

## Observation

The sleep export contains 366 source rows and is not a strict one-row-per-date dataset.

Under provisional wake-date grouping, eight dates contain two episodes:

- 2025-10-09
- 2025-11-02
- 2025-11-09
- 2025-11-17
- 2025-12-25
- 2026-05-31
- 2026-07-03
- 2026-07-04

The paired records generally appear consistent with:

- one overnight episode
- one daytime or secondary episode

They are not presumed duplicate rows.

They may represent:

- naps
- split sleep
- recovery sleep
- secondary provider-detected sessions
- another provider-defined classification

---

## Analytical Risk

A one-row-per-day transformation could lose information if it:

- discards the shorter session
- keeps only the first row
- keeps only the last row
- sums sessions without a declared rule
- treats a secondary episode as a duplicate
- overwrites the overnight episode
- assigns sessions solely by row order

---

## Evaluation Restriction

Unless a specific analysis defines otherwise:

- preserve every source row
- do not deduplicate by date
- do not sum multiple sessions
- do not discard secondary episodes
- do not merge awake or stage durations
- do not force secondary episodes into the curated sleep dataset

---

## Future Transformation Boundary

A session-level transformation may be created if a defined analysis requires it.

A daily aggregate may be derived only after defining:

- primary-session selection
- secondary-session treatment
- nap handling
- daily aggregation
- date assignment
- source-row traceability

No routine normalized sleep tracker is currently required.

---

# DQ-006 — Cross-Domain Missing Dates

## Status

**Open — source missingness**

---

## Sources

- [`ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)
- [`ringconn-activity-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-activity-export.csv)
- [`ringconn-vital-signs-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-vital-signs-export.csv)

---

## Activity and Vital-Sign Coverage

The activity and vital-sign exports each contain:

- 360 data rows
- one row per represented date
- no duplicate represented dates

Both span:

- first represented date: 2025-07-21
- last represented date: 2026-07-20

Both omit:

- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08

The shared absence may reflect:

- no device wear
- synchronization interruption
- provider export omission
- account or application interruption
- hardware unavailability
- another common capture disruption

The source files do not identify the cause.

---

## Sleep Coverage

Under provisional wake-date grouping, no sleep session is represented for:

- 2025-08-10
- 2025-10-23
- 2026-01-04
- 2026-01-05
- 2026-01-06
- 2026-01-07
- 2026-01-08
- 2026-01-09

This list remains provisional because a universal sleep date-assignment rule has not been registered.

---

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

---

## Evaluation Restriction

- Do not insert zero-filled rows.
- Do not forward-fill values.
- Do not interpolate values.
- Do not infer device non-wear without supporting evidence.
- Do not classify the gap as illness, travel, or behavioral disruption without contemporaneous evidence.
- Preserve source missingness in any derived analysis.

---

## Resolution

Contemporaneous context may be reviewed when an analysis depends on the missing interval.

Potential sources include:

- application screenshots
- weekly reports
- travel records
- device-use notes
- hardware or synchronization records

When no cause can be established, classify the interval as:

```text
source missingness — cause unknown
```

No immediate repository action is required.

---

# DQ-007 — November 17 Unclassified Sleep-Stage Session

## Status

**Open — analytical restriction**

---

## Source

[`source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

---

## Affected Session

- Start: `2025-11-17 15:15:29`
- End: `2025-11-17 17:40:29`
- Falling asleep: `2025-11-17 15:40:29`
- Wake-up: `2025-11-17 17:17:59`

---

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

---

## Observation

This is the only source row in which:

- `Time Asleep(min)` is greater than zero
- all sleep-stage fields are zero

Possible explanations include:

- a provider-recognized nap without stage classification
- incomplete stage processing
- an export defect
- an application-versus-export difference
- a session below a stage-classification threshold
- another undocumented provider rule

The record must not be interpreted as biologically stage-free sleep.

---

## Evaluation Restriction

- Retain the source row unchanged.
- Do not distribute the 98 minutes across stages.
- Do not treat zero stage values as measured absence of REM, light, or deep sleep.
- Do not silently discard the session.
- Exclude the row from stage-proportion analysis.
- Do not merge it into another session without a documented rule.
- Treat total sleep as provider-reported and stage classification as unavailable.

---

## Possible Resolution Categories

The row may eventually be classified as:

- valid unclassified session
- provider export omission
- provider processing anomaly
- source-backed correction required
- unresolvable

No resolution is required unless an analysis depends on this session.

---

# DQ-008 — Curated Versus Direct-Export Differences

## Status

**Open — diagnostic comparison**

---

## Datasets

- Curated dataset: [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)
- Direct source export: [`ringconn-sleep-export.csv`](./source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv)

---

## Preliminary Comparison Method

A preliminary non-canonical comparison used:

- curated dates represented in both layers
- provisional wake-date assignment
- the longest source episode when multiple source rows occurred on a date
- direct field comparison without automatic correction

The overlap contained 161 curated dates.

This method was diagnostic only.

It is not an approved recurring transformation or aggregation procedure.

---

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

---

## Possible Explanations

Differences may reflect:

- manual transcription errors
- application-screen rounding
- export precision
- date assignment
- primary-versus-secondary session selection
- provider algorithm changes
- retrospective provider reprocessing
- corrected dates in the curated archive
- non-equivalent source fields
- spreadsheet transfer errors
- application-versus-export presentation differences

A difference does not establish that either source is automatically correct.

---

## Difference Categories

When a discrepancy requires review, it may be classified as:

- exact match
- rounding-only difference
- formatting difference
- date-assignment difference
- session-selection difference
- unit difference
- confirmed manual transcription error
- export omission
- curated omission
- provider revision
- provider anomaly
- unresolved source-state difference

---

## Evaluation Restriction

- Do not bulk-overwrite the curated dataset.
- Do not prefer the export solely because it is machine-generated.
- Do not preserve the curated value solely because it was entered first.
- Review fields independently.
- Preserve confidence labels and subjective context in the curated layer.
- Do not treat the export as containing fields it does not supply.
- Do not treat the longest-session rule as a permanent aggregation rule.
- Do not build an ongoing reconciliation workload without a defined analytical need.

---

## Relationship to DQ-001 Through DQ-003

The export provides strong candidate evidence for:

- DQ-001 `awake_min`
- DQ-002 `light_sleep_min`
- DQ-003 `light_sleep_min`

It does not independently resolve:

- DQ-001 `awakenings_count`
- historical provider-state stability
- timezone interpretation
- a universal multiple-session policy
- all other curated-versus-export differences

The preliminary difference table does not authorize broad historical correction.

---

# DQ-009 — August 17 Snapshot Morning-Weight Transcription Reconciliation

## Status

**Corrected**

The discrepancy is resolved.

---

## Affected Date

2026-08-17

---

## Affected Metric

Morning bodyweight

---

## Conflicting Records

The August snapshot collection-plan execution log recorded:

```text
235.1 lb
```

The canonical Daily Biomarkers dataset for 2026-08-17 records:

```text
234.1 lb
```

The Week 33 report already used the following daily sequence:

```text
234.1, 235.7, 235.8, 236.5, 235.5, 235.5, 234.4
```

which yields a mean of approximately:

```text
235.36 lb
```

and is reported as:

```text
235.4 lb
```

---

## Source Reconciliation

The canonical Daily Biomarkers entry is the contemporaneous structured source for the 2026-08-17 morning weight and therefore controls over the later manual transcription in the collection-plan execution log.

The existing Week 33 daily-weight sequence independently corroborates that `234.1 lb` was already the value used in the weekly calculation.

No correction to the canonical Daily Biomarkers dataset is required.

The conflict is therefore classified as a downstream transcription error rather than a source-data error.

---

## Correction

On 2026-09-06:

- `methodology/2026-08-snapshot-collection-plan.md` was corrected from `235.1 lb` to `234.1 lb`
- a source-reconciliation note was added to the execution log
- the canonical Daily Biomarkers value remained unchanged
- the Week 33 daily sequence remained unchanged
- the Week 33 reported mean remained `235.4 lb`

The correction does not alter any biological observation, trend estimate, model-error score, phase state, or snapshot interpretation.

---

## Downstream Cleanup Boundary

Files that still describe the `234.1 lb` versus `235.1 lb` discrepancy as unresolved or the Week 33 `235.4 lb` mean as provisional should be updated separately to reflect this resolution.

Those narrative cleanups do not authorize changing the underlying Week 33 daily values or weekly mean.

---

## Final Disposition

```text
Canonical 2026-08-17 morning weight: 234.1 lb
Incorrect downstream transcription: 235.1 lb
Canonical dataset modification required: no
Collection-plan correction required: completed
W33 daily sequence modification required: no
W33 weekly mean modification required: no
Status: corrected / resolved
```

---

# Current Dataset Disposition

No change to [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) is authorized by this documentation commit.

Current disposition:

- DQ-001 `awake_min` — correction candidate identified
- DQ-001 `awakenings_count` — unresolved
- DQ-002 `light_sleep_min` — correction candidate identified
- DQ-003 `light_sleep_min` — correction candidate identified
- DQ-004 date and timestamp semantics — restricted for broad timestamp analysis
- DQ-005 multiple-session handling — restricted for daily aggregation
- DQ-006 missing dates — preserved as unexplained source missingness
- DQ-007 November 17 stage classification — restricted from stage analysis
- DQ-008 broader curated-versus-export comparison — diagnostic only
- DQ-009 August 17 morning weight — corrected; `234.1 lb` controls and the W33 `235.4 lb` mean is unchanged

The curated rows remain:

- syntactically valid
- date-continuous within their represented interval
- parseable
- preserved in their current structured form
- subject to the field-specific restrictions documented above

The RingConn source exports remain:

- byte-preserved
- checksum registered
- externally verified
- separate from curated data
- available for targeted reconciliation

These findings do not invalidate:

- the overall curated sleep date sequence
- unaffected fields
- source-export integrity
- weekly report continuity
- checksum integrity
- the broader recovery record

They narrow confidence only where documented.

---

# Source-Reconciliation Procedure

When a specific correction is considered:

1. verify the source-export checksum
2. preserve the original source bytes
3. identify the source acquisition date
4. identify the applicable source row or session
5. establish the issue-specific date-assignment rule
6. determine whether multiple sessions exist
7. select the applicable source session under a documented rule
8. compare only the affected fields
9. confirm field semantics and units
10. distinguish application display from later direct export
11. consider possible provider reprocessing
12. classify the discrepancy
13. avoid modifying unrelated fields
14. save or reference the supporting evidence
15. update the applicable data-quality status
16. correct the curated CSV only when supported
17. record the correction in `CHANGELOG.md`
18. rerun parsing and relevant semantic checks
19. verify dependent percentages or derived fields
20. assess whether a report or analysis requires a correction note

A source-backed correction is archive maintenance.

It is not a new biological observation.

---

# Correction Commit Boundary

When correction is authorized, use narrow commits where practical.

Recommended sequence:

1. correct DQ-002 and DQ-003 light-sleep values after issue-specific verification
2. correct DQ-001 awake-minute values after session and date verification
3. retain or separately resolve uncertainty in awakening counts
4. update this document
5. update `CHANGELOG.md`
6. run focused parsing, checksum, and semantic verification

Do not combine:

- narrow DQ-001 through DQ-003 corrections
- broad historical wearable transformation
- unrelated reporting changes

A full normalized wearable architecture is not a prerequisite for these corrections.

---

# Future Validation Requirements

Future sleep and wearable validation may test for:

- duplicate curated dates
- multiple source sessions per date
- missing dates
- cross-domain missing-date alignment
- malformed row widths
- missing required fields
- mixed timestamp precision
- invalid timestamp parsing
- unresolved timezone status
- exact duplication across conceptually distinct fields
- sleep-stage sums differing from total sleep
- positive total sleep with zero classified stages
- percentages materially inconsistent with durations
- impossible percentages
- negative durations
- implausible field ranges
- abrupt field-behavior changes
- source-label changes
- unit changes
- provider-schema changes
- source-export versus curated discrepancies
- possible retrospective provider revisions

Automated flags should initiate review.

They must not automatically rewrite source or curated data.

---

# Optional Future Mapping Artifact

No comprehensive RingConn source-to-canonical mapping document is currently required.

An analytical mapping artifact may be created when:

- repeated historical comparison is undertaken
- multiple acquisition packages must be merged
- a publication requires stable archive-defined fields
- provider schemas change
- a model-error question requires broader wearable history
- repeated manual reconciliation becomes burdensome

Such an artifact should define, as applicable:

- source acquisition
- source fields
- target fields
- units
- date assignment
- timezone handling
- timestamp precision
- primary and secondary session rules
- missingness
- duplicate handling
- provider anomalies
- transformation procedure
- reproducibility
- source-row traceability

Previously proposed normalized datasets remain deferred:

```text
data/wearable_sleep_sessions_v1.csv
data/wearable_activity_daily_v1.csv
data/wearable_vitals_daily_v1.csv
```

Their absence is not a current data-quality or coverage failure.

---

# Related Documents

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

It was expanded on 2026-07-22 after preservation and preliminary review of the direct RingConn export package.

The 2026-07-22 revision:

- registers the externally verified source package
- documents byte-preservation and checksum status
- identifies narrow correction candidates for DQ-001 through DQ-003
- records mixed timestamp precision
- records multiple sleep episodes
- records cross-domain missing dates
- documents the November 17 unclassified-stage session
- establishes curated-versus-export comparison boundaries
- converts unresolved provider-export questions into issue-specific analytical restrictions
- defers normalized wearable trackers until a concrete analytical requirement exists
- confirms that no broad historical correction or canonical integration is authorized

The 2026-09-06 revision:

- adds DQ-009 for the 2026-08-17 morning-weight discrepancy
- records `234.1 lb` as the controlling canonical Daily Biomarkers value
- classifies `235.1 lb` in the August snapshot collection plan as a downstream transcription error
- records that the collection-plan correction has been completed
- confirms that the Week 33 daily sequence and `235.4 lb` weekly mean already used `234.1 lb` and therefore remain unchanged
- identifies remaining downstream provisional-discrepancy language as narrative cleanup rather than a data correction

No curated value was changed as part of this documentation commit.
