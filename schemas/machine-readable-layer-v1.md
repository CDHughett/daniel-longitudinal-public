# Machine-Readable Layer Schema — v1

## Purpose

This document defines the current public schema contract for the three daily/event datasets introduced in September 2026:

- `data/daily_biomarkers_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`

The files are curated archive datasets derived primarily from private `Daniel_Dataset_v1.x` source workbooks/PDFs and governed contemporaneous records.

They are not raw provider exports.

The schema exists to make the public layer machine-readable without pretending that historical source material was more precise than it was.

---

# Common Rules

## Dates

Canonical date format:

```text
YYYY-MM-DD
```

Dates must parse as real calendar dates.

The current shared structured observation interval is:

```text
2026-02-09 through 2026-08-30
```

A future extension may advance the end date without changing this schema.

---

## Missingness

Blank means unavailable, not collected, not represented in the source, or not transferable at the required confidence.

Blank does not mean zero.

No value may be inferred from an adjacent date merely to create completeness.

---

## Controlled Vocabulary

Fields identified below as **closed vocabulary** may contain only the listed values or blank where blank is explicitly allowed.

Fields identified as **extensible vocabulary** use lower-case `snake_case` terms. Existing values remain valid, and new values may be added only when the new term has a distinct documented meaning.

Free-text fields are not controlled vocabularies.

---

## Field Evidence Classes

The schema distinguishes four evidence roles:

- **measurement / source-transcribed** — numeric or categorical value copied from a governed measurement/source field
- **subjective** — contemporaneous operator-reported state
- **contextual / classified** — archive classification or compact context label derived from preserved source context
- **provenance** — locator describing where the public row came from

A field class does not establish clinical validity.

---

# `source_ref` Contract

`source_ref` is a provenance locator, not a cryptographic checksum.

Multiple source locators are separated by a semicolon (`;`).

## Canonical Private-Source Form

New curated rows should use:

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

The sheet component may contain spaces because it preserves the private source-tab label.

## Legacy Training Aliases

`training_blocks_v1.csv` contains historical aliases created during the first backfill:

```text
wb:v<version>:TB:<YYYY-MM-DD>[:<session_label>]
pdf:v<version>:TB:<YYYY-MM-DD>[:<session_label>]
```

These aliases remain valid for existing v1 rows and are not evidence defects.

They are deprecated for new rows.

A future schema migration may normalize them if the migration is deterministic and preserves source traceability.

## File-Level Provenance

Where an immutable private source file is available for hashing, its SHA-256 is registered separately in:

`data/source_provenance/daniel_dataset_private_manifest.csv`

This separates:

```text
row locator
```

from:

```text
private file identity
```

---

# `data/daily_biomarkers_v1.csv`

## Primary Key

```text
date
```

Exactly one row is permitted per represented date.

The current dataset is continuous from `2026-02-09` through `2026-08-30`.

## Fields

| Field | Type | Evidence class | Rule |
|---|---|---|---|
| `date` | ISO date | measurement/index | unique daily key |
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
| `context_tags` | semicolon list or blank | contextual / classified | extensible `snake_case` tags |
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

Blank is permitted when the private source did not contain a transferable state.

### `stomach_state`

```text
calm
```

Blank is permitted.

### `pain_state`

```text
none
transient
```

Blank is permitted.

### `sweating_state`

```text
none
```

Blank is permitted.

## Context Tags

`context_tags` is intentionally extensible because the archive must preserve real-world context without forcing unrelated events into a small taxonomy.

Rules:

- tags use lower-case `snake_case`
- multiple tags use `;`
- a tag is descriptive, not causal
- a daily tag does not automatically create a `context_events_v1.csv` event

---

# `data/training_blocks_v1.csv`

## Primary Key

```text
session_id
```

Every session ID must be unique.

Multiple sessions may occur on the same date.

## Fields

| Field | Type | Evidence class | Rule |
|---|---|---|---|
| `session_id` | text | index | unique; date-prefixed identifier |
| `date` | ISO date | measurement/index | must fall inside represented daily observation interval |
| `block_type` | category | contextual / classified | closed vocabulary |
| `duration_min` | **duration expression** | measurement / source-transcribed | v1 compatibility field; see duration rule below |
| `intensity` | source text or blank | measurement / source-transcribed | preserves source semantics |
| `hr_range_bpm` | source text or blank | measurement / source-transcribed | may be a range/expression |
| `distance_mi` | number or blank | measurement / source-transcribed | miles |
| `load_summary` | source text or blank | measurement / source-transcribed | compact movement/load expression |
| `rpe` | number/range text or blank | subjective/source-transcribed | source-preserving |
| `fed_state` | category or blank | contextual / classified | closed vocabulary |
| `execution_state` | category or blank | subjective / classified | closed vocabulary |
| `equipment_context` | category or blank | contextual / classified | extensible `snake_case` vocabulary |
| `context_tags` | semicolon list or blank | contextual / classified | extensible `snake_case` tags |
| `protocol_status` | category | contextual / classified | extensible governed vocabulary |
| `source_ref` | text | provenance | required; canonical or accepted v1 legacy form |

## `duration_min` — v1 Compatibility Semantics

The name `duration_min` predates formal schema hardening and is misleading if interpreted as a strictly numeric column.

For **v1**, its canonical meaning is now explicitly:

> a source-preserving duration expression whose unit basis is minutes when a duration is numerically represented.

Accepted forms are:

### Scalar minutes

```text
55
45
59.8
```

These may be interpreted numerically as minutes.

### Bounded source range

```text
30-45
```

This means the source supports a bounded interval.

Do not replace it with a midpoint.

### Compound historical expression

```text
52 min + circuits
30 min B1 + 35-45 strength
```

These preserve historical mixed-session architecture and are **not** a single numeric minute value.

### Blank

Blank is allowed when a source row represents an activity/session whose total duration was not resolved to a transferable value.

## Numeric Analysis Rule

Consumers must not coerce `duration_min` blindly to numeric.

Only scalar numeric values are directly suitable for arithmetic without a separately documented transformation.

Ranges and compound expressions must remain nonnumeric unless an analysis defines a reproducible treatment.

## Future v2 Duration Split

A future `training_blocks_v2.csv` should split this field into:

```text
duration_min
duration_min_low
duration_min_high
duration_raw
```

The v1 file is not silently rewritten because that would create unsupported precision for historical compound/range rows.

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

Blank is permitted when not represented.

### `execution_state`

```text
controlled
completed
ambient
trait_like
trait_level
```

Blank is permitted where the historical source did not support a classified execution state.

## Extensible Vocabularies

`equipment_context`, `context_tags`, and `protocol_status` remain extensible because historical training architecture contains legitimate state transitions and one-off conditions.

New terms must:

- use lower-case `snake_case`
- be materially distinct from an existing term
- not imply a stronger biological conclusion than the source supports

---

# `data/context_events_v1.csv`

## Purpose

This file is a **bounded event index**, not a complete diary of ordinary life.

An event row is created when preserved context is materially useful for interpreting:

- training availability
- measurement conditions
- recovery behavior
- protocol state
- portability
- model-error evaluation
- source reconciliation

Routine repetition does not require an event row.

## Primary Key

```text
event_id
```

Format:

```text
YYYY-MM-DD-##
```

The date prefix must equal `start_date`.

## Fields

| Field | Type | Evidence class | Rule |
|---|---|---|---|
| `event_id` | text | index | unique; date-prefixed |
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

Use `other` only when the event is material but no existing category is semantically appropriate.

## Impact-Level Vocabulary

### `contextual`

The event is useful for interpretation but did not materially change the recurring protocol architecture.

### `material`

The event meaningfully changed context, workload, timing, environment, or interpretation while leaving the core protocol decision boundary intact.

### `protocol_altering`

The event directly changed, paused, reduced, withheld, replaced, or transitioned a governed protocol exposure.

Impact classification describes archive relevance.

It does not imply harm.

## Outcome-State Vocabulary

### `absorbed`

The event occurred without a persistent observed loss of ordinary system function under the represented window.

### `resolved`

A transient issue or bounded condition ended or returned to the ordinary operating state.

### `transient_effect`

A temporary effect was observed but did not warrant representation as a persistent unresolved state.

These are retrospective descriptive classifications, not clinical outcomes.

## Event-Classification Rules

1. Preserve the event only when it adds interpretive value beyond a routine daily tag.
2. Prefer the most specific available `event_type`.
3. Do not infer a causal mechanism from temporal association.
4. Do not create an event solely to make a favorable portability or resilience claim.
5. Natural ordinary-life variation may be indexed when it materially changes context.
6. A protocol-altering event must state the actual protocol consequence in `protocol_impact`.
7. Model-error cross-references must point to records that exist in the archive.
8. Event dates must remain inside the represented public observation interval unless the schema is explicitly extended.

---

# Cross-File Relationships

The three datasets are related but not row-for-row equivalent.

```text
daily_biomarkers_v1.csv
one row per represented day

training_blocks_v1.csv
zero-to-many sessions per day

context_events_v1.csv
zero-to-many bounded events per day or date interval
```

Required relationships:

- every training date must exist inside the daily-biomarker represented interval
- every event interval must overlap the daily-biomarker represented interval
- every `related_model_error` ID must exist in the model-error archive
- a daily `context_tags` value does not require a matching event row
- an event row does not require a training session on every event date

---

# Validation

Machine-readable semantic checks are implemented in:

```text
tools/validate_machine_readable.py
```

The core repository validator remains:

```text
tools/validate_repository.py
```

The machine-readable validator checks:

- required headers
- unique daily dates
- unique session IDs
- unique event IDs
- ISO date parsing
- daily continuity
- numeric field syntax
- controlled vocabularies
- duration-expression syntax
- source-reference syntax
- event interval ordering
- week/reference syntax
- related model-error existence
- cross-file date relationships

Validation does not establish biological plausibility, causality, or clinical meaning.

---

# Versioning Boundary

This document formalizes the existing v1 public data layer.

It does not retroactively claim that these schema rules governed the private source workbooks before public extraction.

Breaking changes require a new dataset schema version under `VERSIONING.md`.

Historical v1 source-preserving expressions remain valid even when a cleaner future schema is planned.
