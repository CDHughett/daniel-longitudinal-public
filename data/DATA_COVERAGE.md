# Data Coverage

This document defines the scope, completeness, and limitations of evidence currently represented in the Daniel Longitudinal Study.

It is a **coverage declaration**, not an interpretation layer.

Coverage does not establish measurement validity, causal attribution, biological significance, or clinical meaning.

---

## Coverage Status Definitions

| Status | Meaning |
|---|---|
| Source-preserved | Original provider/device file retained without analytical modification |
| Structured longitudinal | Repeated observations available in a governed machine-readable dataset |
| Structured event index | Bounded events available as machine-readable contextual records |
| High narrative coverage | Repeated observations preserved in reports/notes without complete machine-readable representation |
| Snapshot-based | Measurements occur at discrete testing intervals |
| Partial | Relevant observations exist but collection is incomplete or irregular |
| Contextual only | Information appears in reports/notes without a governed recurring dataset |
| Not tracked | No governed recurring collection process exists |
| Deferred | A possible derived layer has been considered but is not currently required |

Source-preserved coverage and canonical structured coverage are different states.

A provider export may improve provenance without becoming the canonical analytical dataset.

---

# Coverage Summary

| Domain | Current coverage | Notes |
|---|---|---|
| Daily biomarkers / subjective state | **Structured longitudinal** | `daily_biomarkers_v1.csv`; 210 continuous daily rows, 2026-02-09 through 2026-09-06 |
| Training exposure | **Structured longitudinal** | `training_blocks_v1.csv`; 339 session rows through 2026-09-06 |
| Context / perturbation events | **Structured event index** | `context_events_v1.csv`; 44 bounded events through 2026-09-03 |
| Sleep | **Structured longitudinal + source-preserved historical coverage** | Canonical curated sleep has 203 continuous daily rows through 2026-08-30; broader RingConn episode export retained separately |
| Recovery / vital signs | **Structured + narrative + source-preserved** | HRV, resting HR, daily average HR, sleep HR, SpO₂ and related signals appear across curated data, reports, screenshots and direct exports |
| Body composition | **Snapshot-based** | DEXA, Bod Pod and scale-weight measurements occur at discrete intervals using differing methods |
| Blood biomarkers | **Snapshot-based** | Periodic laboratory panels; not every private health source is public |
| Epigenetic / aging measures | **Structured longitudinal, snapshot-based** | TruAge, Advanced TruAge, TruHealth and related outputs represented across repeated testing windows |
| VO₂ / formal performance testing | **Partial, event-based** | Formal testing occurs at discrete events rather than continuously |
| Nutrition | **Contextual only** | Meal timing, fasting, intake patterns and selected dietary context appear in reports/daily tags; no continuous nutrition dataset |
| Supplementation | **Contextual only** | Material changes and continuity are documented when relevant; no canonical adherence dataset |
| Environmental factors | **Partial** | Travel, heat, air quality, equipment access, schedule and ordinary-life workload are recorded when salient, not comprehensively measured |
| Model error / prediction | **Structured longitudinal** | Primary forward prediction register, historical reconstruction, UDI/concordance trackers and registered evaluation artifacts |
| Repository governance | **High documentary coverage** | Audits, changelog, phase criteria, methodology, validation and release practices are version controlled |

---

# Current Machine-Readable Core

## Daily Biomarkers

File:

[`daily_biomarkers_v1.csv`](./daily_biomarkers_v1.csv)

Current coverage:

```text
2026-02-09 through 2026-09-06
210 continuous daily rows
```

The dataset includes source-transcribed measurements such as bodyweight and cardiovascular telemetry plus bounded subjective-state fields and compact context tags.

It is a curated public dataset derived from governed private/public source material.

It is not a raw provider export.

---

## Training Blocks

File:

[`training_blocks_v1.csv`](./training_blocks_v1.csv)

Current coverage:

```text
2026-02-09 through 2026-09-06
339 session rows
```

Multiple sessions may occur on one date.

The dataset preserves historical protocol transitions, B1, Load Integration, recovery variants and structured recreation where source-supported.

The v1 `duration_min` field is a source-preserving **duration expression**, not a guaranteed numeric column. Scalar values are numeric minutes; ranges and compound historical expressions remain nonnumeric unless a separate transformation is documented.

---

## Context Events

File:

[`context_events_v1.csv`](./context_events_v1.csv)

Current coverage:

```text
44 bounded event rows
represented interval begins 2026-02-09
latest current event ends 2026-09-03
```

This is an event index, not a complete diary.

It captures context that materially improves interpretation of training availability, measurement conditions, recovery, protocol state, portability, model-error evaluation or source reconciliation.

Routine ordinary days do not require an event row.

---

## Machine-Readable Schema

The three files above are governed by:

[`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)

That schema defines:

- field evidence classes
- controlled vocabularies
- v1 duration semantics
- `source_ref` grammar
- event classification
- cross-file relationships
- missingness rules

Machine-readable validation is implemented in:

[`../tools/validate_machine_readable.py`](../tools/validate_machine_readable.py)

---

# Dataset and Source Locations

| Dataset or evidence layer | Path |
|---|---|
| Daily biomarkers | [`daily_biomarkers_v1.csv`](./daily_biomarkers_v1.csv) |
| Training blocks | [`training_blocks_v1.csv`](./training_blocks_v1.csv) |
| Context events | [`context_events_v1.csv`](./context_events_v1.csv) |
| Curated sleep longitudinal | [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) |
| RingConn direct source-export package | [`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/) |
| Private Daniel Dataset provenance | [`source_provenance/`](./source_provenance/) |
| Biomarker snapshot | [`biomarker_snapshot.csv`](./biomarker_snapshot.csv) |
| Epigenetic longitudinal | [`epigenetic_longitudinal.csv`](./epigenetic_longitudinal.csv) |
| Bloodwork longitudinal | [`bloodwork_longitudinal.csv`](./bloodwork_longitudinal.csv) |
| Model error — primary | [`model_error/model_error_gap_v1.csv`](./model_error/model_error_gap_v1.csv) |
| UDI / concordance tracker | [`model_error/udi_by_type_tracker.csv`](./model_error/udi_by_type_tracker.csv) |
| Historical model-error reconstruction | [`model_error/historical/`](./model_error/historical/) |
| Data-quality notes | [`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md) |
| Weekly reports | [`../reports/`](../reports/) |
| Primary snapshot artifacts | [`../snapshots/`](../snapshots/) |

---

# Temporal Coverage

## Governed Observation

The governed observation period begins in 2026-W01 and continues through the active archive state.

Not every domain has machine-readable coverage from the first observation day.

Continuous observation must not be interpreted as continuous structured measurement of every variable.

## Weekly Reports

Consistent weekly reporting begins at:

```text
2026-W06
```

Reports preserve recurring interpretation and context but do not replace the structured datasets.

## Current Daily Structured Interval

The aligned daily machine-readable interval currently begins at:

```text
2026-02-09
```

The current public daily/training/sleep structured layer is populated through:

```text
2026-09-06
```

Different datasets may have different row counts because their unit of observation differs.

```text
daily biomarkers: one row per date
sleep: one canonical row per governed wake date
training: zero-to-many session rows per date
context events: zero-to-many bounded event rows per date/interval
```

---

# Private Daniel Dataset Provenance

The current daily/training/event layer was retrospectively backfilled from completed private `Daniel_Dataset_v1.0` through `v1.29` source states and then preserved publicly as curated CSVs.

Row-level provenance is retained through `source_ref`.

File-level private-source identity is registered when the exact historical workbook was available for hashing:

[`source_provenance/daniel_dataset_private_manifest.csv`](./source_provenance/daniel_dataset_private_manifest.csv)

The manifest currently includes several registered private-workbook SHA-256 values and explicitly marks versions for which the exact immutable historical file was unavailable during the provenance pass.

A missing private-source hash is not replaced with a reconstructed checksum.

Public provenance does not require publishing the private workbook itself.

---

# Direct RingConn Source-Export Coverage

A direct RingConn export package was acquired on `2026-07-21` and preserved under:

[`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/)

The package contains:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- acquisition `README.md`
- checksum manifest

The provider CSVs are preserved byte-for-byte.

Git text conversion is disabled for source-export CSVs through `.gitattributes`.

Previous external verification established the registered files matched their original downloads byte-for-byte and their SHA-256 values passed.

Mechanical preservation does not establish semantic validity for every provider field.

## Sleep export

The preserved source sleep export contains:

- 366 sleep-episode rows
- 358 unique wake dates
- represented wake-date range 2025-07-21 through 2026-07-21
- eight dates containing more than one sleep episode
- eight absent wake dates
- timestamps without explicit UTC offsets
- no provider-supplied primary-sleep/nap classification

The source is episode-level and is not forced into the canonical one-row-per-date sleep structure.

## Activity export

The preserved source activity export contains:

- 360 daily rows
- represented date range 2025-07-21 through 2026-07-20
- missing source dates that remain missing

An absent row does not establish zero activity.

## Vital-sign export

The preserved source vital-sign export contains:

- 360 daily rows
- represented date range 2025-07-21 through 2026-07-20
- provider-defined daily minimum/average/maximum heart rate, SpO₂ and HRV fields

Provider-defined daily values must not be silently substituted for differently defined curated metrics such as resting HR or sleep HRV.

---

# Source Export Versus Curated Data

Direct provider exports and curated archive datasets serve different roles.

A direct export preserves:

- provider field names
- provider date/timestamp behavior
- provider aggregation
- original missingness
- original row ordering
- original byte representation

A curated dataset may preserve:

- archive-defined field names
- governed date assignment
- contemporaneous structured transcription
- subjective state
- context tags
- correction history
- values not present in the provider export

Neither layer silently overwrites the other.

A difference between a direct export and a curated value requires semantic review before correction.

---

# Sleep Coverage and Known Restrictions

Canonical sleep:

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

Current public interval:

```text
2026-02-09 through 2026-08-30
203 continuous daily records
```

Known field-level quality restrictions remain documented in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

These include governed sleep discrepancies and provider/source-state questions that are intentionally not repaired by automatic overwrite.

A structurally continuous sleep dataset may still contain field-level uncertainty.

---

# Snapshot-Based Coverage

Low-frequency biological and performance domains include:

- DEXA
- Bod Pod
- formal VO₂ testing
- bloodwork
- TruDiagnostic / epigenetic outputs
- other provider-generated biological reports

These measurements are discrete observations rather than daily time series.

Different methods must not be treated as interchangeable merely because they describe a similar construct.

---

# Context That Remains Incompletely Structured

The machine-readable expansion materially improves public coverage, but it does not make the archive exhaustive.

The following remain partially structured or contextual:

- continuous nutrition intake
- supplement adherence
- hydration and sodium exposure
- complete environmental measurements
- all social/psychological context
- every incidental physical activity
- every subjective narrative detail
- every private medical/source artifact

The archive intentionally does not manufacture completeness.

---

# Event Coverage Boundary

`context_events_v1.csv` does not contain every context tag or every ordinary-life occurrence.

An event row is justified when the context materially improves interpretation.

Daily context may therefore exist only as:

- a daily biomarker `context_tags` value
- a training `context_tags` value
- a weekly report observation
- a snapshot note

without a duplicate event row.

See the event-classification rules in:

[`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)

---

# Deferred Derived Layers

The archive does not currently require normalized RingConn datasets such as:

```text
data/wearable_sleep_sessions_v1.csv
data/wearable_activity_daily_v1.csv
data/wearable_vitals_daily_v1.csv
```

They remain deferred until a specific analysis, publication or automation requirement justifies transformation rules for:

- timezone handling
- sleep-session aggregation
- duplicate/secondary sessions
- provider metric definitions
- missing source dates
- source-row traceability

The absence of these derived files is not a current coverage failure.

---

# Validation Boundary

The repository contains two complementary read-only validators:

```text
tools/validate_repository.py
tools/validate_machine_readable.py
```

The machine-readable validator checks the three new public datasets for syntax, identifiers, vocabularies, date relationships, source references and event/model-error relationships.

Validation does not establish:

- clinical correctness
- causal interpretation
- provider accuracy
- biological plausibility
- completeness of private evidence

---

# Current Coverage Assessment

The public archive now contains a materially stronger structured core than earlier repository states.

The key current machine-readable relationship is:

```text
daily physiological / subjective state
+
sleep
+
training exposure
+
context events
+
model-error outcomes
```

This improves reproducible longitudinal analysis while preserving the distinction between structured data, source artifacts, narrative evidence and interpretation.

Coverage should continue to expand only when the added structure improves traceability or analysis more than it increases administrative complexity.
