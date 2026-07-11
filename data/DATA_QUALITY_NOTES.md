# Data Quality Notes

**Status:** Active  
**Created:** 2026-07-11  
**Scope:** Known data-quality questions requiring source reconciliation

---

## Purpose

This document records suspected transcription, field-mapping, completeness, or source-comparability issues in the structured datasets.

A data-quality note does not establish that a recorded value is incorrect.

Its purpose is to:

- preserve the original observation
- identify the exact field and date range under review
- prevent unsupported correction
- define the source evidence required for resolution
- preserve a traceable correction path
- distinguish structural validity from semantic validity

The canonical datasets remain unchanged until source evidence supports a correction.

---

## Governing Rules

- Do not infer replacement values from neighboring dates.
- Do not calculate replacement values from percentages unless the original source explicitly supports that calculation.
- Do not silently repair suspicious values.
- Do not overwrite an unresolved value merely because another value appears more plausible.
- Preserve all corrections through Git history.
- Document the source used for every correction.
- Record unresolved missingness honestly when the original source is unavailable.
- Keep interpretation proportional to the fields affected.
- Do not invalidate an entire row when only one field or field group is under review.

The source artifact controls when it conflicts with a manually transcribed value.

---

## Status Definitions

| Status | Meaning |
|---|---|
| Open | Source reconciliation has not been completed |
| Source located | Original evidence is available but has not yet been fully compared |
| Confirmed valid | The recorded value matches the original source |
| Correction required | The original source confirms that the structured value is incorrect |
| Corrected | The structured value has been updated with documented provenance |
| Unresolvable | The original source is unavailable or insufficient to determine the correct value |

---

# DQ-001 — Possible Sleep-Field Duplication

## Status

Open

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

## Affected Dates

2026-05-18 through 2026-05-31

## Affected Fields

- `awake_min`
- `awakenings_count`

## Observation

Across 14 consecutive rows, the value recorded in `awake_min` exactly matches the value recorded in `awakenings_count`.

Observed paired values range from 3 to 5.

The pattern:

- begins abruptly on 2026-05-18
- persists through 2026-05-31
- ends before 2026-06-01
- appears alongside sleep-efficiency values ranging from 86% to 96%

Because awake duration and awakening count represent different concepts, exact duplication across a continuous 14-day block is suspicious and may indicate:

- copied-field transcription
- field-mapping confusion
- source-interface misreading
- an export-labeling issue
- valid source behavior not yet understood

The current evidence does not establish which field, if either, is incorrect.

## Evaluation Restriction

Until reconciliation is complete:

- do not use `awake_min` from the affected dates for quantitative awake-duration analysis
- do not treat agreement between `awake_min` and `awakenings_count` as biological evidence
- do not derive replacement awake minutes from sleep efficiency
- do not alter sleep-efficiency values through inference
- retain the affected rows for date continuity and unaffected-field analysis

Other fields in the affected rows remain usable according to their normal limitations unless separate evidence identifies another issue.

## Required Source Evidence

For each affected date, compare the structured row against the original RingConn screenshot or direct source export for:

- total sleep duration
- deep sleep duration
- light sleep duration
- REM sleep duration
- awake duration
- awakening count
- sleep efficiency

## Resolution Rule

If the source confirms the current values:

- mark this note `Confirmed valid`
- document the source format and comparison date

If the source confirms a transcription error:

- correct only the source-supported fields
- preserve all unaffected fields
- document the correction date
- identify the supporting source artifact
- record the correction in `CHANGELOG.md`
- retain the prior values through Git history

If the source cannot be recovered:

- retain the current values
- mark the affected fields as unresolved
- avoid using them in analyses requiring verified awake duration or awakening count

---

# DQ-002 — Sleep-Stage Total Reconciliation

## Status

Open

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

## Affected Date

2026-03-31

## Recorded Values

| Field | Value |
|---|---:|
| `total_sleep_min` | 298 |
| `deep_sleep_min` | 55 |
| `light_sleep_min` | 207 |
| `rem_sleep_min` | 20 |
| Sum of recorded sleep stages | 282 |
| Difference from total sleep | 16 |

The recorded stage percentages total 94.7%.

## Observation

The recorded deep, light, and REM durations sum to 282 minutes, while total sleep is recorded as 298 minutes.

The 16-minute difference may represent:

- an omitted or unclassified stage interval
- source-device rounding or categorization behavior
- incomplete transcription
- a source-interface value not represented by the current schema
- an incorrect total or stage value

The available structured row does not determine which explanation is correct.

## Evaluation Restriction

Until source reconciliation:

- do not force the stage values to equal total sleep
- do not distribute the missing 16 minutes across stages
- do not infer an unrecorded stage
- preserve the recorded total and individual stage values
- disclose the discrepancy when using this date in stage-composition analysis

## Required Source Evidence

Compare the row against the original RingConn screenshot or direct export for:

- total sleep
- deep sleep
- light sleep
- REM sleep
- awake time
- any unclassified or uncategorized duration
- displayed stage percentages

---

# DQ-003 — Sleep-Stage Total Reconciliation

## Status

Open

## Dataset

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

## Affected Date

2026-04-02

## Recorded Values

| Field | Value |
|---|---:|
| `total_sleep_min` | 336 |
| `deep_sleep_min` | 60 |
| `light_sleep_min` | 217 |
| `rem_sleep_min` | 45 |
| Sum of recorded sleep stages | 322 |
| Difference from total sleep | 14 |

The recorded stage percentages total 95.9%.

## Observation

The recorded deep, light, and REM durations sum to 322 minutes, while total sleep is recorded as 336 minutes.

The 14-minute difference may represent:

- an omitted or unclassified stage interval
- source-device rounding or categorization behavior
- incomplete transcription
- a source-interface value not represented by the current schema
- an incorrect total or stage value

The available structured row does not determine which explanation is correct.

## Evaluation Restriction

Until source reconciliation:

- do not force the stage values to equal total sleep
- do not distribute the missing 14 minutes across stages
- do not infer an unrecorded stage
- preserve the recorded total and individual stage values
- disclose the discrepancy when using this date in stage-composition analysis

## Required Source Evidence

Compare the row against the original RingConn screenshot or direct export for:

- total sleep
- deep sleep
- light sleep
- REM sleep
- awake time
- any unclassified or uncategorized duration
- displayed stage percentages

---

## Current Dataset Disposition

No change to [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) is authorized by this document.

The identified rows remain:

- syntactically valid
- date-continuous
- parseable
- preserved in their original structured form
- subject to the field-specific restrictions documented above

These findings do not invalidate:

- the overall sleep date sequence
- unaffected sleep fields
- checksum integrity
- weekly report continuity
- the broader recovery record

They narrow the confidence assigned to the specific fields under review.

---

## Source-Reconciliation Procedure

When source evidence becomes available:

1. verify the date shown in the source
2. compare each relevant source field with the structured row
3. determine whether the issue is transcription, schema, source behavior, or no error
4. avoid modifying unrelated fields
5. save or reference the supporting source artifact
6. update the applicable data-quality note status
7. correct the CSV only when supported
8. record the correction in `CHANGELOG.md`
9. rerun CSV parsing and semantic validation
10. verify that reports or derived analyses do not require a corresponding correction note

A source-backed correction should be treated as archive maintenance, not as a new biological observation.

---

## Future Validation Requirements

Future automated sleep-data validation should test for:

- duplicate dates
- missing dates
- malformed row widths
- missing required fields
- exact duplication across conceptually distinct columns
- sleep-stage sums that differ from total sleep
- stage percentages that materially differ from recorded durations
- impossible percentages
- negative durations
- implausible field ranges
- abrupt field-behavior changes
- source-label or unit changes

Automated flags should initiate review.

They should not automatically rewrite source data.

---

## Related Documents

- [`../docs/audits/2026-07-11-saturday-audit.md`](../docs/audits/2026-07-11-saturday-audit.md)
- [`../methodology/data-collection.md`](../methodology/data-collection.md)
- [`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)
- [`DATA_COVERAGE.md`](./DATA_COVERAGE.md)

---

## Version Note

This document was created on 2026-07-11 after semantic review identified questions that were not detectable through CSV parsing and date-continuity checks alone.

No source value was changed as part of this commit.
