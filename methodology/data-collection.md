# Data Collection

## Status

Active methodology document.

This document defines how observations, measurements, source artifacts, and manually transcribed values enter the governed archive.

It applies prospectively to new collection and retrospectively when resolving documented data-quality questions.

---

## Purpose

The data-collection layer exists to preserve a traceable relationship between:

1. the observed event or measurement
2. the original source
3. the structured archive entry
4. later interpretation
5. any subsequent correction

The objective is not to eliminate all uncertainty.

The objective is to make uncertainty, missingness, transcription, and correction visible enough that another observer can understand how a value entered the archive and how much confidence it deserves.

---

## Core Principles

- Source artifacts take precedence over summaries.
- Collection should occur before final interpretation whenever practical.
- Directly exported values are preferred over manually transcribed values.
- Manually transcribed values must remain traceable to their source.
- Missing values remain missing rather than being estimated for completeness.
- Suspicious values are flagged before they are corrected.
- Corrections require source evidence.
- Inferred values must not be presented as directly observed values.
- Later interpretation must not rewrite the original observation.
- Collection procedures should remain proportionate to the value of the data.

---

## Collection Layers

The archive distinguishes several collection layers.

### 1. Primary Source Artifacts

Primary source artifacts are the closest available representation of the original measurement or event.

Examples include:

- provider-generated laboratory reports
- DEXA or BodPod reports
- epigenetic testing reports
- device-generated exports
- wearable screenshots
- testing-system outputs
- contemporaneous photographs
- dated source documents

Primary artifacts are stored in:

[`../snapshots`](../snapshots/)

A provider-generated report may be primary evidence for the archive even when it is not raw instrument data.

Its limitations should remain visible.

---

### 2. Direct Structured Exports

Direct structured exports are machine-readable files produced by a device, application, provider, or testing system.

Examples include:

- CSV exports
- JSON exports
- spreadsheet downloads
- structured laboratory-result files

Direct exports are preferred when they:

- preserve original units
- preserve dates and timestamps
- expose stable field definitions
- reduce manual transcription
- can be archived without altering the source values

A direct export should not be silently reformatted in a way that obscures the original schema.

When normalization is required, the original export should be preserved separately when practical.

---

### 3. Manual Structured Transcription

Manual transcription is permitted when a direct export is unavailable or incomplete.

Examples include:

- entering wearable values from screenshots
- entering laboratory values from reports
- entering body-composition values from provider artifacts
- converting dated observations into a structured CSV

Manual transcription must preserve:

- source date
- original unit
- field meaning
- missingness
- source location or artifact reference
- any uncertainty relevant to interpretation

Transcription should reproduce the source value rather than improve, normalize, or reinterpret it during entry.

---

### 4. Contemporaneous Collection Notes

Contemporaneous collection notes capture observations not represented adequately by a device or formal report.

Examples include:

- training-session execution
- pain or mechanical signaling
- GI state
- edema or fluid context
- dream characteristics
- mental state
- environmental disruption
- travel constraints
- divided-attention execution
- unusual recovery demands

These notes may enter:

- daily biomarker records
- training logs
- weekly reports
- perturbation records
- model-error evidence notes

Contemporaneous notes should distinguish direct observation from interpretation.

Example:

> Pull-up execution remained controlled while verbal instruction continued.

is a direct observation.

> Nervous-system adaptation has permanently advanced.

is an interpretation requiring broader evidence.

---

### 5. Retrospective Interpretation

Retrospective interpretation occurs after evidence has accumulated.

Examples include:

- weekly closeouts
- phase summaries
- snapshot interpretations
- model-error closures
- longitudinal synthesis

Retrospective documents may:

- organize evidence
- compare intervals
- identify repeated patterns
- state uncertainty
- evaluate predictions

They may not create a measurement or event that was not otherwise recorded.

---

## Source Hierarchy

When two records conflict, use the following hierarchy unless a documented reason supports another order:

1. verified primary source artifact
2. direct device or provider export
3. contemporaneous structured transcription
4. contemporaneous collection note
5. weekly retrospective report
6. later synthesis grounded in preserved evidence
7. unsupported memory

Unsupported memory is not sufficient to overwrite a governed value.

A later report may identify a likely error, but the structured source should remain unchanged until the original evidence is reviewed.

---

## Date and Time Handling

Every structured observation should include the most precise reliable temporal reference available.

Preferred order:

1. exact timestamp with timezone
2. exact local date and approximate time
3. exact date
4. bounded date range
5. explicitly unknown date

Dates should use ISO 8601 format where practical:

`YYYY-MM-DD`

Times should preserve the relevant local timezone when timing affects interpretation.

The following should not be assumed silently:

- that upload date equals collection date
- that report date equals sample date
- that device synchronization date equals observation date
- that UTC date equals the subject’s local date

When several dates exist, preserve their distinct meanings where relevant:

- collection date
- sample date
- result date
- report date
- upload date
- archive date

---

## Units and Field Definitions

Values should be recorded using the unit shown in the source unless a governed schema requires normalization.

When normalization occurs:

- preserve the original source value when practical
- document the conversion rule
- use consistent units within the structured dataset
- do not mix units within a field
- do not infer a unit from neighboring rows when the source is ambiguous

Field names should reflect the measured concept rather than the display label alone.

For example:

- duration and event count must remain separate concepts
- percentage and absolute duration must remain separate fields
- biological age and age acceleration must not be treated as interchangeable
- sample date and report date must remain distinct when both matter

Definitions belong in:

[`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)

---

## Missingness

Missing values must remain visibly missing.

Acceptable missingness representations should be defined per dataset and used consistently.

Examples may include:

- empty field
- `NA`
- `not collected`
- `not available`
- `not applicable`
- `source unavailable`

A zero must not be used to represent missingness unless zero is the verified observed value.

Missing values must not be filled through:

- averaging neighboring dates
- linear interpolation
- assumed routine behavior
- retrospective memory
- percentage-derived reconstruction
- copying a nearby value

Derived or imputed values may be created only in a separate analysis layer and must be labeled explicitly as derived or imputed.

They must not replace the canonical observation.

---

## Manual Entry Procedure

When entering a value manually:

1. confirm the observation or collection date
2. identify the original source
3. confirm the field meaning
4. confirm the displayed unit
5. enter the value without interpretive adjustment
6. preserve missing fields as missing
7. compare the completed row against the source
8. review conceptually similar fields for accidental duplication
9. verify that date and row alignment are correct
10. commit the structured change with a descriptive message

For high-density source artifacts, a second comparison pass should occur after the full entry is complete.

When practical, structured entries should be reviewed independently from the original entry sequence to reduce copy-forward errors.

---

## Screenshots

Screenshots are acceptable source artifacts when direct exports are unavailable.

A screenshot used as source evidence should, where practical, show:

- measurement date
- relevant field labels
- full values
- units
- enough application or device context to identify the source

Screenshots should not be treated as complete exports when they omit relevant fields or truncate values.

A screenshot may support a structured entry without requiring every screenshot to remain in the public archive, provided the archive’s provenance and verification standard remains clear.

Values visible only in a screenshot must not be reconstructed from chart geometry when the exact number is unavailable.

---

## Device and Application Changes

Consumer devices and applications may change:

- field labels
- algorithms
- firmware
- application versions
- score definitions
- export schemas
- displayed precision

Known changes should be documented in:

[`../MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)

A value should not be assumed comparable across versions merely because the field name remains the same.

When a change may affect longitudinal interpretation:

- identify the affected date boundary
- preserve the new source version
- document the comparability limitation
- avoid merging incompatible values without explanation

---

## Derived Values

Derived values are calculated from one or more recorded observations.

Examples include:

- weekly averages
- percentage change
- trend slopes
- recovery duration
- prediction error
- stage percentages calculated from durations

Derived values must:

- identify the source fields
- define the formula
- preserve the underlying observations
- remain reproducible
- be labeled as derived rather than directly measured

A derived value must not be used to silently repair a missing source value.

---

## Inferred Values

An inferred value is an estimate not directly supported by the original source.

Examples include:

- calculating awake minutes from sleep efficiency without knowing the device denominator
- estimating missing sleep stages from total sleep
- inferring body composition from scale weight
- assigning an exact training load from memory
- converting a narrative description into an unsupported numerical score

Inferred values are prohibited from the canonical dataset unless:

- the dataset explicitly includes an inference field
- the inference method is documented
- the value is labeled as inferred
- the direct observation remains preserved separately

Inferred values must never be presented as source-confirmed measurements.

---

## Data-Quality Review

Data-quality review includes more than checking whether a file parses.

Review should consider:

- malformed rows
- duplicate dates
- missing dates
- unit inconsistency
- impossible ranges
- duplicated conceptual fields
- unexplained abrupt field changes
- stage or component totals that do not reconcile
- source and structured-value disagreement
- unexpected schema changes
- missing provenance
- ambiguous collection dates

Potential issues should be documented in:

[`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)

A data-quality flag narrows confidence in the affected field or interval.

It does not automatically invalidate the entire dataset.

---

## Correction Procedure

A canonical value may be corrected when source evidence confirms that the archived value is inaccurate.

The correction procedure is:

1. locate the original source
2. verify the affected date and field
3. determine whether the issue is transcription, schema mapping, source behavior, or unit handling
4. correct only the affected value or field
5. preserve unrelated values
6. update the applicable data-quality note
7. record the correction in [`../CHANGELOG.md`](../CHANGELOG.md)
8. rerun structural and semantic validation
9. review derived outputs that may depend on the corrected value
10. preserve the prior value through Git history

Corrections should not be described as new biological observations.

They are archive-maintenance events.

---

## Unresolvable Values

When the source is unavailable or insufficient:

- do not invent a correction
- retain the original value when deletion would obscure the record
- mark the field or interval as unresolved
- restrict analyses that depend on the affected value
- preserve the reason the issue cannot be resolved

An unresolved value may remain in the canonical dataset when its uncertainty is clearly documented.

---

## Provenance Requirements

A structured dataset should provide enough context to determine, directly or through accompanying documentation:

- what was measured
- when it was measured
- where the value came from
- whether it was exported or transcribed
- what unit was used
- whether the value was corrected
- whether any quality restriction applies

Not every row must contain a full artifact path when the dataset has a stable documented source and collection method.

Low-frequency or high-importance measurements should maintain stronger artifact-level linkage than routine high-frequency telemetry.

---

## Collection Versus Interpretation

The archive separates collection from interpretation.

### Collection statements

Examples:

- HRV was recorded as 62 ms.
- Post-B1 weight was 229.3 lb.
- Pull-up execution remained controlled while speaking.
- Formal training did not occur during travel.

### Interpretive statements

Examples:

- recovery remained compatible
- the system demonstrated portability
- operator overhead appeared reduced
- the perturbation did not produce regression

Interpretation should be placed in reports, evaluation documents, or model-error records.

Structured collection files should remain as close as practical to the observed measurement or event.

---

## Weekly Reports

Weekly reports serve two functions:

1. contemporaneous collection of notable events
2. retrospective interpretation at weekly closeout

Before closeout:

- candidate evidence may be recorded
- unresolved observations may be preserved
- open predictions must not be rewritten

At closeout:

- interpretation should remain bounded to evidence accumulated during the week
- stable protocol details should not be restated unnecessarily
- deviations, new evidence, perturbations, predictions, and unresolved questions should receive priority

---

## Model-Error Evidence

Evidence relevant to an open prediction should first enter a normal collection layer.

Examples include:

- weekly report note
- training observation
- biomarker entry
- source artifact
- perturbation record

A prediction record should not be modified merely because candidate evidence appears.

The original prediction remains preserved until the evaluation window closes.

Current evaluation rules for records 041–044 are documented in:

[`open_prediction_evaluation_plan_041_044.md`](./open_prediction_evaluation_plan_041_044.md)

---

## Publication Boundary

Not every privately collected source must be published.

The public archive may include:

- redacted source artifacts
- structured values derived from private source material
- summary evidence with documented provenance
- public derivatives of privately retained originals

Public omission does not remove the requirement for internal source verification.

Publication decisions should preserve:

- evidentiary usefulness
- source traceability
- data minimization
- repository integrity

Detailed anonymization and public-artifact rules belong in:

[`anonymization.md`](./anonymization.md)

---

## Scope Boundary

This methodology does not claim:

- laboratory-grade environmental control
- perfect device validity
- complete measurement of all relevant variables
- causal isolation of concurrent interventions
- absence of transcription risk
- clinical significance from consumer-device signals
- generalizability beyond the recorded subject

Its role is to make the collection process inspectable and correction-capable.

---

## Future Structured Exports

Planned structured exports may include:

- daily biomarkers
- training blocks
- perturbation events

Each future export should define:

- primary key
- required fields
- date and time rules
- units
- source field
- missingness convention
- correction provenance
- applicable quality checks

A new export should not be added merely because it is possible.

It should be added when repeated observations justify a stable schema and the structured form improves analysis or continuity.

---

## Related Documents

- [`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)
- [`../DATASET_OVERVIEW.md`](../DATASET_OVERVIEW.md)
- [`../MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)
- [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)
- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../STRUCTURAL_PRINCIPLES.md`](../STRUCTURAL_PRINCIPLES.md)
- [`../CHANGELOG.md`](../CHANGELOG.md)

---

## Version Note

This methodology was expanded on 2026-07-11 after semantic review demonstrated that syntactically valid structured data may still require source-level verification.

The expansion defines current collection and correction practice without altering any existing source value.
