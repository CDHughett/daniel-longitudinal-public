# Data Dictionary

This document defines measurement terms, field meanings, units, date rules, and logging conventions used in the Daniel Longitudinal Study.

Definitions prioritize repeatability, longitudinal comparability, source traceability, explicit missingness, and interpretive restraint.

Dataset-specific schema definitions take precedence over global conventions when a conflict exists.

For the current daily/training/event schema, see:

[`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)

---

# Archive Data Layers

## Source Artifacts

Original provider reports, images, PDFs, screenshots, and direct provider/device exports.

Source artifacts preserve the closest available source state and are not modified merely to match archive schemas.

## Curated Structured Datasets

Archive-defined machine-readable datasets maintained under governed schemas.

Current examples include:

- `data/daily_biomarkers_v1.csv`
- `data/sleep_longitudinal_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`
- `data/biomarker_snapshot.csv`
- `data/epigenetic_longitudinal.csv`
- `data/bloodwork_longitudinal.csv`
- `data/model_error/model_error_gap_v1.csv`

Curated datasets may contain source-transcribed values, archive-defined identifiers, subjective context, classification fields, correction notes, and documented derived values.

A curated value does not supersede stronger verified source evidence when a source-backed discrepancy is established.

## Narrative Evidence

Contemporaneous and retrospective observations preserved in weekly reports, snapshot notes, audit records, and model-error closure text.

## Derived Views

Dashboards, summaries, figures, and analysis outputs generated from other archive layers.

Derived views do not create new primary evidence.

---

# Global Conventions

## Dates

Default format:

```text
YYYY-MM-DD
```

Snapshot-month format:

```text
YYYY-MM
```

A date may represent collection date, wake date, session date, testing date, snapshot month, or report window. Dataset-specific date meaning must remain explicit.

## Time

Canonical time format when needed:

```text
HH:MM
```

Ordinary local timezone:

```text
America/New_York
```

This does not establish that every provider export or historical timestamp uses that timezone.

When timezone provenance is unresolved, preserve the source timestamp and do not invent an offset.

## Units

| Domain | Default unit |
|---|---|
| Weight | pounds (`lb`) |
| Duration | minutes (`min`) |
| Heart rate | beats per minute (`bpm`) |
| HRV | milliseconds (`ms`) when provider reports it that way |
| Speed | miles per hour (`mph`) |
| Incline | percent (`%`) |
| Temperature | Fahrenheit (`°F`) |
| Distance | miles (`mi`) unless otherwise noted |
| Energy expenditure | `kcal` or `kcal/day` |
| Biological age | years |
| Pace of aging | ratio |
| Oxygen saturation | percent (`%`) |

Values remain in source units unless a documented transformation explicitly converts them.

---

# Missingness

## Blank

Blank means the source contains no transferable value, the metric was not available/collected, or the value cannot be transferred reliably.

Blank does not mean zero.

## Zero

Use only when the source explicitly reports zero or the metric is structurally defined as zero.

## Unknown

Use categorical `unknown` only in fields designed to accept it.

Do not place text missingness in numeric fields unless the dataset schema explicitly permits it.

## Missing Dates

An absent date does not automatically mean no sleep, zero activity, no device wear, illness, or synchronization failure.

---

# Machine-Readable Core

The aligned public structured layer currently includes:

```text
daily biomarkers
+
canonical sleep
+
training sessions
+
context events
+
model-error outcomes
```

Current public coverage:

| Dataset | Unit | Current coverage |
|---|---|---|
| `daily_biomarkers_v1.csv` | daily | 203 continuous rows, 2026-02-09 through 2026-08-30 |
| `sleep_longitudinal_v1.csv` | governed wake date | 203 continuous rows, 2026-02-09 through 2026-08-30 |
| `training_blocks_v1.csv` | session/block | 325 rows, 2026-02-09 through 2026-08-30 |
| `context_events_v1.csv` | bounded event | 42 rows, current event coverage through 2026-08-29 |

These files have different units of observation and are not row-for-row equivalent.

---

# Field Evidence Classes

The current machine-readable schema distinguishes:

## Measurement / Source-Transcribed

A numeric or categorical value copied from a governed source field.

Examples include bodyweight, HRV, heart rate, temperature, duration, distance, and source-listed training load.

## Subjective

Contemporaneous operator-reported state.

Examples include mood, energy, GI state, pain, and execution-state descriptions.

Structured subjective data remain subjective.

## Contextual / Classified

Archive-defined labels used to organize preserved context.

Examples include context tags, equipment context, protocol status, event type, impact level, and outcome state.

Classification does not establish causal mechanism.

## Provenance

Fields describing where a row came from, primarily `source_ref`.

---

# `daily_biomarkers_v1.csv`

Primary key:

```text
date
```

Exactly one row per represented date.

Fields:

| Field | Meaning |
|---|---|
| `date` | governed observation date |
| `morning_weight_lb` | morning bodyweight in pounds |
| `daily_hrv_ms` | daily HRV metric in milliseconds |
| `resting_hr_bpm` | resting heart rate |
| `daily_avg_hr_bpm` | daily average heart rate |
| `body_temp_f` | body temperature in °F |
| `mood_state` | structured subjective mood state |
| `energy_state` | structured subjective energy state |
| `gi_state` | structured GI state |
| `stomach_state` | structured stomach state |
| `pain_state` | structured pain state |
| `sweating_state` | structured sweating state |
| `context_tags` | semicolon-separated descriptive context tags |
| `source_ref` | row-level provenance locator |

The controlled vocabularies are defined in the machine-readable schema.

---

# `training_blocks_v1.csv`

Primary key:

```text
session_id
```

Multiple sessions may occur on one date.

Fields include:

- date
- block type
- source-preserving duration expression
- intensity
- heart-rate range
- distance
- compact load summary
- RPE
- fed/fasted state
- execution state
- equipment context
- context tags
- protocol status
- source reference

## `duration_min` Compatibility Rule

Despite its historical column name, `duration_min` is **not uniformly numeric in v1**.

Accepted source-preserving forms include:

```text
55
30-45
52 min + circuits
30 min B1 + 35-45 strength
```

Scalar numbers may be interpreted as minutes.

Ranges must remain ranges unless an analysis defines a reproducible rule.

Compound historical expressions must remain nonnumeric unless a future governed transformation explicitly decomposes them.

Do not silently replace a range with a midpoint or invent a total for compound historical sessions.

A future v2 schema is expected to separate scalar/range/raw duration representations.

## Load Integration

Load Integration is the current structured resistance/movement layer paired with B1.

The public `training_blocks_v1.csv` now provides machine-readable session-level coverage of Load Integration and historical training architecture.

This is a curated session dataset, not a raw provider training export.

---

# `context_events_v1.csv`

Primary key:

```text
event_id
```

Format:

```text
YYYY-MM-DD-##
```

The file is a bounded event index, not a complete diary.

Fields include:

- start/end dates
- event type/subtype
- impact level
- bounded factual description
- protocol impact
- retrospective descriptive outcome state
- related week
- related model-error record
- source reference

Current event types include testing, mechanical, ordinary-life load, travel, environmental, social, schedule shift, equipment change, and other.

Event inclusion requires interpretive value beyond a routine daily tag.

---

# `source_ref`

`source_ref` is a provenance locator, not a checksum.

Canonical new private-source forms:

```text
private_workbook:Daniel_Dataset_v<version>:<sheet>:<YYYY-MM-DD>[:label]
private_pdf:Daniel_Dataset_v<version>:<sheet>:<YYYY-MM-DD>[:label]
```

All current live training rows use the canonical private-source forms above.

Legacy `wb:v...` and `pdf:v...` aliases remain visible in Git history as provenance of the initial backfill, but they are no longer valid in the live v1 dataset.

File-level private-source SHA-256 values, where exact retained files were available, are recorded in:

[`data/source_provenance/daniel_dataset_private_manifest.csv`](./data/source_provenance/daniel_dataset_private_manifest.csv)

---

# Canonical Sleep

File:

`data/sleep_longitudinal_v1.csv`

The canonical date represents the governed morning/wake-date observation assigned to the sleep episode.

This convention must not be automatically imposed on direct RingConn source exports.

Important distinctions:

- total sleep versus time in bed
- awake duration versus awakening count
- sleep HRV versus daily average HRV
- sleeping average HR versus resting HR versus daily average HR
- canonical daily row versus provider sleep episode

Known quality restrictions are documented in `data/DATA_QUALITY_NOTES.md`.

---

# RingConn Source-Preserved Exports

Current acquisition:

[`data/source_exports/ringconn/2026-07-21/`](./data/source_exports/ringconn/2026-07-21/)

The preserved CSVs are direct provider exports, byte-preserved, checksum-registered, and not automatically normalized into canonical daily trackers.

## Sleep Export

Session/episode-level provider source.

Important source fields include start/end timestamps, falling-asleep/wake-up times, provider sleep ratio, time asleep, awake minutes, REM, light sleep, and deep sleep.

Timezone is not authoritatively established from the export.

Multiple episodes may occur for one preliminary wake date and must not be silently deduplicated or summed.

## Activity Export

Provider daily source containing fields such as date, steps, and RingConn-reported calories.

RingConn calories should not be assumed equivalent to measured total daily energy expenditure or active calories without provider-semantic evidence.

## Vital-Signs Export

Provider daily source containing minimum/average/maximum heart rate, SpO₂, and HRV.

Provider daily minimum heart rate is not automatically resting heart rate; daily average HRV is not automatically sleep HRV.

---

# Wearable Metric Definitions

## Daily Average Heart Rate

Provider average heart rate across its defined daily window.

Distinct from resting and sleeping heart rate.

## Resting Heart Rate

Provider-derived or separately recorded resting-heart-rate metric.

Unit: bpm.

## Average Sleeping Heart Rate

Average heart rate during the provider-defined sleep interval.

Unit: bpm.

## Daily Average HRV

Provider-reported daily HRV average.

Unit: ms when reported that way by the device.

## Sleep HRV

HRV associated with the provider-defined sleep interval/summary.

Distinct from daily average HRV.

## Awakening Count

Number of discrete awakening events.

Distinct from awake duration.

## Awake Duration

Minutes awake within or around a sleep interval.

Must not be populated using awakening count.

## Sleep Efficiency

Percentage of an applicable sleep opportunity/session spent asleep.

Provider-reported sleep ratio, provider sleep efficiency, and archive-derived sleep efficiency must not be assumed identical without documented formula semantics.

---

# Snapshot and Biological Data

## `biomarker_snapshot.csv`

Integrated low-frequency snapshot table containing fields from DEXA, Bod Pod/COSMED, TruDiagnostic/TruHealth, and related measurement artifacts.

Different source methods remain distinct.

Examples:

- DEXA lean mass is not Bod Pod fat-free mass
- a provider biological-age output is not a direct measure of lifespan
- provider TruHealth percentiles are provider-derived scores, not automatically laboratory concentrations

## `epigenetic_longitudinal.csv`

Longitudinal provider-specific epigenetic/aging outputs.

Common fields:

- `date`
- `domain`
- `biomarker`
- `value`
- `unit`
- `status`
- `source`
- `notes`

Relevant outputs may include OMICm age, DunedinPACE, Symphony organ/system ages, and TruHealth domains.

Comparisons require attention to provider, assay family, algorithm version, source date, units, and preparation conditions.

## Body Composition Terms

### DEXA Lean Mass

Lean soft tissue reported by DEXA. It excludes fat mass and is distinct from Bod Pod fat-free mass.

### DEXA Fat Mass / Body Fat Percentage

DEXA provider-reported fat mass and percent body fat.

### DEXA Visceral Fat

Provider-defined visceral-fat output. Preserve the source unit/form rather than converting among mass, area, volume, or proprietary score without a governed rule.

### Bod Pod Fat-Free Mass

All non-fat mass estimated through air-displacement plethysmography, including muscle, bone, water, organs, and other non-fat tissue.

Hydration-sensitive and not equivalent to DEXA lean soft tissue.

### Resting/Total Energy Estimates

Bod Pod/COSMED-associated energy estimates should not be described as dedicated directly measured metabolic tests unless the source artifact confirms the method.

---

# Training Terms

## B1

Recurring aerobic anchor, typically incline treadmill under the active Phase 2 architecture.

Historical B1 details vary across the archive; compare sessions using the logged source fields rather than assuming one fixed configuration across all dates.

## B3 / B4

Historical locomotion/structural circuit terminology retained for provenance.

Presence in historical data does not establish current protocol exposure.

## Circuit

One complete pass through a defined movement sequence.

Circuit counts are comparable only when the underlying sequence is known.

## Execution State

Structured descriptive labels such as controlled, completed, ambient, trait-like, trait-level, or recreational.

These labels describe observed execution and do not independently declare a phase.

---

# Capture States

## Fasted

Default archive definition where explicitly used:

- no caloric intake for at least 10 hours before capture
- water permitted
- non-caloric electrolytes permitted only when part of normal routine
- caffeine/stimulants logged when used
- no deliberate extension solely to manipulate the measurement

Specific test-provider instructions may supersede this general archive definition for an individual capture and should be documented.

## Normal Operating Conditions

No artificial dehydration, cosmetic sodium manipulation, acute glycogen-depletion strategy, short-term loading intended to alter the capture, or protocol change introduced solely to produce a favorable measurement.

Normal operating conditions do not mean complete environmental control.

---

# Correction Conventions

Canonical values may be corrected only when identifiable source evidence supports the correction.

A correction should record:

- dataset/date/field
- prior and corrected representation
- supporting source
- reason
- correction date
- affected downstream summaries

Do not infer replacements from neighboring dates, silently overwrite a curated value from a later export, or treat plausibility as proof.

---

# Validation

The current machine-readable layer is validated by:

```text
tools/validate_machine_readable.py
```

The broader repository is validated by:

```text
tools/validate_repository.py
```

Validation checks implemented structure and semantics. It does not establish clinical validity or biological causality.

---

# Change Control

When an existing definition materially changes:

1. update the applicable dictionary/schema
2. identify affected datasets/reports
3. record material changes in `CHANGELOG.md`
4. preserve prior meaning through Git history
5. assess whether a schema migration is required
6. apply release changes only under `VERSIONING.md`

A new schema rule must not be represented as though it governed historical source workbooks before the rule existed.
