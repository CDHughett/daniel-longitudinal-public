# Machine-Readable Layer Schema — v1

## Purpose

This document defines the public schema contract for:

- `data/daily_biomarkers_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`

These files are curated archive datasets derived primarily from private `Daniel_Dataset_v1.x` source workbooks/PDFs and governed contemporaneous records.

They are not raw provider exports.

The schema makes the public layer machine-readable without pretending historical source material was more precise than it was.

---

# Common Rules

## Dates

Canonical date format:

```text
YYYY-MM-DD
```

The represented machine-readable interval begins on `2026-02-09`. Current live row counts and endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

A later data extension may advance the end date without changing the v1 field structure.

## Missingness

Blank means unavailable, not collected, not represented in the source, or not transferable at the required confidence.

Blank does not mean zero.

Do not infer a missing value from neighboring dates merely to create completeness.

## Vocabulary Types

**Closed vocabulary** fields may contain only the values listed below or blank where blank is explicitly allowed.

**Extensible vocabulary** fields use lower-case `snake_case`. Existing values remain valid; new values require a distinct documented meaning.

## Evidence Classes

- **measurement / source-transcribed** — copied from a governed measurement/source field
- **subjective** — contemporaneous operator-reported state
- **contextual / classified** — archive classification derived from preserved context
- **provenance** — locator describing where the public row came from

A field class describes evidence role, not clinical validity.

---

# `source_ref`

`source_ref` is a row-level provenance locator, not a checksum.

Multiple source locators are separated with `;`.

## Canonical New Private-Source Form

```text
private_workbook:Daniel_Dataset_v<version>:<sheet>:<YYYY-MM-DD>[:<row_or_session_label>]
private_pdf:Daniel_Dataset_v<version>:<sheet>:<YYYY-MM-DD>[:<row_or_session_label>]
```

Examples:

```text
private_workbook:Daniel_Dataset_v1.28:Daily Biomarkers:2026-08-30
private_workbook:Daniel_Dataset_v1.28:Training Blocks:2026-08-30:LI
private_pdf:Daniel_Dataset_v1.0:Training Blocks:2026-02-09
```

## Standardized Training Provenance

All current live `training_blocks_v1.csv` rows use the canonical private-source forms above.

Historical aliases created during the initial backfill, such as:

```text
wb:v<version>:TB:<YYYY-MM-DD>[:<session_label>]
pdf:v<version>:TB:<YYYY-MM-DD>[:<session_label>]
```

remain visible in Git history only.

They are not accepted in the current live v1 dataset or by the current machine-readable validator.

The 2026-09-07 migration changed `source_ref` provenance locators only; non-`source_ref` training fields were preserved.

## File-Level Private Provenance

Where an exact retained private source file was available for hashing, file identity is registered separately in:

`data/source_provenance/daniel_dataset_private_manifest.csv`

This keeps row location distinct from private file identity.

---

# `data/daily_biomarkers_v1.csv`

## Primary Key

```text
date
```

Exactly one row per represented date.

Current row count and endpoint are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

## Fields

| Field | Type | Evidence class | Rule |
|---|---|---|---|
| `date` | ISO date | index | unique daily key |
| `morning_weight_lb` | number or blank | measurement / source-transcribed | pounds |
| `daily_hrv_ms` | number or blank | measurement / source-transcribed | milliseconds |
| `resting_hr_bpm` | number or blank | measurement / source-transcribed | bpm |
| `daily_avg_hr_bpm` | number or blank | measurement / source-transcribed | bpm |
| `body_temp_f` | number or blank | measurement / source-transcribed | °F |
| `mood_state` | category or blank | subjective | closed vocabulary |
| `energy_state` | category or blank | subjective | closed vocabulary |
| `gi_state` | category or blank | subjective | closed vocabulary |
| `stomach_state` | category or blank | subjective | closed vocabulary |
| `pain_state` | category or blank | subjective | closed vocabulary |
| `sweating_state` | category or blank | subjective | closed vocabulary |
| `context_tags` | semicolon list or blank | contextual / classified | extensible `snake_case` |
| `source_ref` | text | provenance | required; canonical private-source form |

## Closed Vocabularies

### `mood_state`

```text
stable
sympathetic_leaning
sympathetic
labile_but_regulated
calm
reflective
```

### `energy_state`

```text
stable
depleted_but_executed
low_but_executed
low_downregulated
low_recovery_limited
moderate
low_moderate
moderate_high
high
```

### `gi_state`

```text
calm
```

Blank permitted.

### `stomach_state`

```text
calm
```

Blank permitted.

### `pain_state`

```text
none
transient
```

Blank permitted.

### `sweating_state`

```text
none
```

Blank permitted.

## Context Tags

Rules:

- lower-case `snake_case`
- multiple tags separated with `;`
- descriptive rather than causal
- a daily tag does not automatically require a context-event row

---

# `data/training_blocks_v1.csv`

## Primary Key

```text
session_id
```

Every session ID must be unique. Multiple sessions may occur on one date.

Current row count and endpoint are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md). The historical prefix through `2026-08-30` is protected at 325 sessions; later governed rows append without changing that prefix.

## Fields

| Field | Type | Evidence class | Rule |
|---|---|---|---|
| `session_id` | text | index | unique, date-prefixed |
| `date` | ISO date | index | within represented daily interval |
| `block_type` | category | contextual / classified | closed vocabulary |
| `duration_min` | duration expression | measurement / source-transcribed | v1 compatibility rule below |
| `intensity` | source text or blank | measurement / source-transcribed | source-preserving |
| `hr_range_bpm` | source text or blank | measurement / source-transcribed | may be range/expression |
| `distance_mi` | number or blank | measurement / source-transcribed | miles |
| `load_summary` | source text or blank | measurement / source-transcribed | compact movement/load expression |
| `rpe` | scalar/range text or blank | subjective/source-transcribed | source-preserving |
| `fed_state` | category or blank | contextual / classified | closed vocabulary |
| `execution_state` | category or blank | subjective / classified | closed vocabulary |
| `equipment_context` | category or blank | contextual / classified | extensible `snake_case` |
| `context_tags` | semicolon list or blank | contextual / classified | extensible `snake_case` |
| `protocol_status` | category | contextual / classified | extensible governed vocabulary |
| `source_ref` | text | provenance | required; canonical private-source form |

## `duration_min` — v1 Compatibility Semantics

The historical column name is misleading if treated as strictly numeric.

For v1, canonical meaning is:

> a source-preserving duration expression whose unit basis is minutes when a duration is represented numerically.

Accepted forms include:

### Scalar minutes

```text
55
45
59.8
```

Suitable for direct numeric minute analysis.

### Bounded range

```text
30-45
```

Preserve as a range. Do not replace with a midpoint.

### Compound historical expressions

```text
52 min + circuits
30 min B1 + 35-45 strength
```

These are not a single numeric minute value.

### Blank

Permitted when no reliable total duration is transferable.

## Numeric Analysis Rule

Consumers must not coerce `duration_min` blindly to numeric.

Only scalar numeric values are directly suitable for arithmetic without a separately documented transformation.

## Future Duration Split

A future `training_blocks_v2.csv` may separate:

```text
duration_min
duration_min_low
duration_min_high
duration_raw
```

The v1 file is not silently rewritten because doing so could invent unsupported precision.

## Closed Vocabularies

### `block_type`

```text
legacy_firmware_block
b1_load_integration
b1
load_integration
b1_ground_integration
active_recovery
structured_recreation
```

### `fed_state`

```text
fasted
fed
```

Blank permitted.

### `execution_state`

```text
controlled
completed
ambient
trait_like
trait_level
recreational
```

Blank permitted when no classified state was transferable.

## Extensible Training Vocabularies

`equipment_context`, `context_tags`, and `protocol_status` remain extensible.

New terms must:

- use lower-case `snake_case`
- be materially distinct from existing terms
- not imply a stronger biological conclusion than the source supports

---

# `data/context_events_v1.csv`

## Purpose

A bounded contextual event index, not a complete diary.

An event row is created when preserved context materially improves interpretation of training availability, measurement conditions, recovery, protocol state, portability, model-error evaluation, or source reconciliation.

Routine repetition does not require an event row.

## Primary Key

```text
event_id
```

Format:

```text
YYYY-MM-DD-##
```

Date prefix must equal `start_date`.

Current event count and endpoint are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

## Fields

| Field | Type | Evidence class | Rule |
|---|---|---|---|
| `event_id` | text | index | unique, date-prefixed |
| `start_date` | ISO date | contextual/index | required |
| `end_date` | ISO date | contextual/index | required; `end_date >= start_date` |
| `event_type` | category | contextual / classified | closed vocabulary |
| `event_subtype` | category | contextual / classified | extensible `snake_case` |
| `impact_level` | category | contextual / classified | closed vocabulary |
| `description` | text | contextual narrative | bounded factual summary |
| `protocol_impact` | category | contextual / classified | extensible `snake_case` |
| `outcome_state` | category | retrospective classification | closed vocabulary |
| `related_week` | week ID list or blank | cross-reference | `YYYY-W##`, `;` separated |
| `related_model_error` | record ID list or blank | cross-reference | 3-digit IDs, `;` separated |
| `source_ref` | text | provenance | one or more source locators |

## Event-Type Vocabulary

```text
testing
mechanical
ordinary_life_load
travel
environmental
social
schedule_shift
equipment_change
other
```

## Impact-Level Vocabulary

### `contextual`
Useful for interpretation but did not materially alter recurring protocol architecture.

### `material`
Meaningfully changed context, workload, timing, environment, or interpretation while leaving the core protocol decision boundary intact.

### `protocol_altering`
Directly changed, paused, reduced, withheld, replaced, or transitioned a governed protocol exposure.

Impact describes archive relevance, not harm.

## Outcome-State Vocabulary

### `absorbed`
Event occurred without a persistent observed loss of ordinary function within the represented window.

### `resolved`
Transient issue or bounded condition ended/returned to ordinary operating state.

### `transient_effect`
Temporary effect observed without representation as a persistent unresolved state.

These are retrospective descriptive classifications, not clinical outcomes.

## Event Classification Rules

1. Include an event only when it adds value beyond a routine tag.
2. Prefer the most specific event type.
3. Do not infer causal mechanism from temporal association.
4. Do not create an event solely to manufacture a favorable resilience/portability claim.
5. Natural ordinary-life variation may be indexed when materially relevant.
6. A protocol-altering event must state its actual consequence in `protocol_impact`.
7. Model-error cross-references must identify records that exist in the archive.
8. Event dates must remain inside the represented public interval unless the schema is explicitly extended.

---

# Cross-File Relationships

```text
daily_biomarkers_v1.csv
one row per represented day

training_blocks_v1.csv
zero-to-many sessions per day

context_events_v1.csv
zero-to-many bounded events per day/interval
```

Required relationships:

- training dates must fall within the daily-biomarker represented interval
- event intervals must fall within the represented public interval
- `related_model_error` IDs must exist in the model-error archive
- daily/training tags do not require a matching event row
- event rows do not require a training session on every event date

---

# Validation

Machine-readable validation:

```text
tools/validate_machine_readable.py
```

Core repository validation:

```text
tools/validate_repository.py
```

The machine-readable validator checks headers, identifiers, dates, continuity, numeric syntax, controlled vocabularies, duration expressions, source-reference syntax, event intervals, model-error references, and cross-file relationships.

Validation does not establish biological plausibility, causality, measurement validity, or clinical meaning.

---

# Versioning Boundary

This document formalizes the current public v1 layer.

It does not claim these schema rules governed private source workbooks before public extraction.

Breaking field/semantic changes require a future dataset schema version under `VERSIONING.md`.

Historical source-preserving v1 expressions remain valid even when a cleaner future schema is planned.
