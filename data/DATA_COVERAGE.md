# Data Coverage

This document defines the scope, completeness, and limitations of datasets currently included in the archive.

It clarifies:

- what is tracked
- how each domain is represented
- what is structured versus narrative
- what is preserved as direct source evidence
- what is only measured at discrete intervals
- where known gaps or quality restrictions exist
- what has not yet been normalized into canonical datasets

This is a **coverage declaration**, not an interpretation layer.

Coverage status does not establish measurement validity, causal attribution, or biological significance.

---

## Coverage Status Definitions

| Status | Meaning |
|---|---|
| Source-preserved | Original provider or device export is retained without normalization or interpretive modification |
| Structured longitudinal | Repeated observations are available in a canonical machine-readable dataset |
| High narrative coverage | Repeated contemporaneous observations are preserved, but no complete canonical structured export exists |
| Snapshot-based | Measurements occur at discrete testing intervals rather than continuously |
| Partial | Some relevant observations exist, but collection is incomplete, irregular, or limited in scope |
| Contextual only | Information appears in reports or notes without systematic structured collection |
| Not tracked | No governed recurring collection process currently exists |
| Planned | A structured export or normalized dataset is anticipated but has not yet been implemented |

Source-preserved coverage and canonical structured coverage are separate states.

A direct vendor export may improve provenance without yet being suitable for canonical analysis.

---

## Coverage Summary

| Domain | Coverage Status | Notes |
|---|---|---|
| Training exposure | High narrative coverage | Daily execution is documented through reports and contemporaneous notes; no canonical daily training-block export yet |
| Wearable activity | Source-preserved; normalized dataset planned | Direct RingConn activity export is archived with checksums; canonical activity mapping has not yet been implemented |
| Sleep | Structured longitudinal, recent; source-preserved historical coverage | Canonical wearable-derived daily dataset begins 2026-02-09; a broader direct RingConn export is preserved separately and has not yet been normalized or reconciled |
| Recovery and vital signs | Structured, narrative, and source-preserved | HRV, resting HR, sleep HR, SpO₂, and related signals are represented through canonical records, reports, and a direct RingConn vital-signs export |
| Subjective daily biomarkers | High narrative coverage | Mental state, GI status, pain, dreams, erection quality, weight context, and related observations are recorded regularly but do not yet have a canonical public daily export |
| Body composition | Snapshot-based | DEXA, Bod Pod, scale weight, and related measurements occur at discrete intervals with differing methods |
| Blood biomarkers | Snapshot-based | Periodic laboratory panels only; not all referenced health data are publicly included |
| Epigenetic and aging measures | Structured longitudinal, snapshot-based | TruAge, Advanced TruAge, TruHealth, and associated outputs are represented across repeated testing windows |
| VO₂ and performance testing | Partial, event-based | Formal performance testing is collected at discrete events rather than continuously |
| Nutrition | Contextual only | Meal timing, fasting state, intake patterns, and selected nutrition context appear in reports; no continuous nutrition dataset exists |
| Supplementation | Contextual only | Supplement changes and continuity are documented when relevant but are not yet represented in a canonical longitudinal export |
| Environmental factors | Partial | Travel, schedule, heat, air quality, equipment access, and related conditions are documented when salient but are not comprehensively measured |
| Perturbation events | High narrative coverage; structured export planned | Travel, illness, environmental disruption, and workload events are preserved in reports but not yet consolidated into a canonical event dataset |
| Model error and prediction | Structured longitudinal | Primary forward-prediction dataset is maintained separately from historical reconstruction |
| Repository governance | High documentary coverage | Audits, changelog entries, phase criteria, methodology, and protocol-state changes are version controlled |

---

## Dataset and Source Locations

| Dataset or Evidence Layer | Path |
|---|---|
| Sleep longitudinal | [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) |
| RingConn direct source export | [`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/) |
| RingConn export provenance | [`source_exports/ringconn/2026-07-21/README.md`](./source_exports/ringconn/2026-07-21/README.md) |
| RingConn export checksums | [`source_exports/ringconn/2026-07-21/checksums.txt`](./source_exports/ringconn/2026-07-21/checksums.txt) |
| Biomarker snapshot | [`biomarker_snapshot.csv`](./biomarker_snapshot.csv) |
| Epigenetic longitudinal | [`epigenetic_longitudinal.csv`](./epigenetic_longitudinal.csv) |
| Bloodwork longitudinal | [`bloodwork_longitudinal.csv`](./bloodwork_longitudinal.csv) |
| Model error — primary | [`model_error/model_error_gap_v1.csv`](./model_error/model_error_gap_v1.csv) |
| UDI by-type tracker | [`model_error/udi_by_type_tracker.csv`](./model_error/udi_by_type_tracker.csv) |
| Model error — historical reconstruction | [`model_error/historical/`](./model_error/historical/) |
| Data-quality notes | [`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md) |
| Weekly reports | [`../reports/`](../reports/) |
| Primary artifacts | [`../snapshots/`](../snapshots/) |

---

## Baseline Context Reference

Interpretation of biomarker, epigenetic, recovery, and performance data should consider documented pre-observation conditions:

[`../docs/methodology/subject_baseline_context.md`](../docs/methodology/subject_baseline_context.md)

This document records known starting context but does not assign causal interpretation to later changes.

---

## Temporal Coverage

The archive operates through continuous observation with progressively expanding structured public representation.

### Observation Continuity

The governed observation period begins in 2026-W01 and continues through the present archive state.

This reflects ongoing observation of:

- training exposure
- recovery conditions
- behavioral execution
- biological measurements
- protocol state
- environmental and life-context perturbations

Not every observation is represented in a machine-readable public dataset.

Continuous observation should therefore not be interpreted as continuous structured measurement of every domain.

---

### Structured Reporting Coverage

The consistent weekly reporting layer begins at:

- `2026-W06`

From that point forward, weekly reports provide a recurring documentary layer for:

- protocol exposure
- recovery state
- notable deviations
- contextual events
- retrospective weekly interpretation

Weekly reports are evidence-rich but are not substitutes for canonical structured daily exports.

---

### Dataset-Specific Coverage

Datasets begin when stable collection and schema conditions were available.

Current examples:

- Canonical sleep longitudinal dataset: begins `2026-02-09`
- Direct RingConn source-export package: acquired `2026-07-21`
- Weekly reports: begin `2026-W06`
- Biomarker snapshot dataset: February and May 2026 comparison points currently represented
- Epigenetic dataset: repeated low-frequency snapshot outputs
- Bloodwork dataset: periodic laboratory measurements
- Primary model-error dataset: clean governed records beginning with record 013
- Historical model-error reconstruction: records 001–012, segregated from the primary dataset

Different datasets therefore cover different observation windows.

No single structured file represents the entire archive.

---

## Direct RingConn Source-Export Coverage

A direct RingConn export package was acquired on `2026-07-21` and preserved in:

[`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/)

The package contains:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- `README.md`
- `checksums.txt`

The three CSVs are preserved byte-for-byte as downloaded.

Pre-publication screening found:

- no obvious administrative-identifier fields in the exported headers
- no email-like values
- expected wearable-domain fields only

This screening reduces obvious privacy risk but does not convert the export into a canonical dataset.

### Export Structure

The archived source package contains:

- 367 lines in the sleep export, including its header
- 361 lines in the activity export, including its header
- 361 lines in the vital-signs export, including its header

These line counts must not automatically be interpreted as equal numbers of covered calendar days.

The sleep export may contain:

- multiple sleep episodes associated with one date
- different date-assignment behavior from the canonical sleep tracker
- missing dates
- provider-defined session records rather than one normalized daily record

The activity and vital-signs exports may also differ in date coverage or missingness.

Actual temporal coverage must be determined from file contents and documented mapping rules rather than inferred from the label “annual export.”

---

## Source-Export Integration Boundary

The RingConn exports are source artifacts.

They do not automatically replace, correct, or extend:

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

The direct export and the curated canonical dataset serve different roles.

### Direct Export

The direct export preserves:

- vendor-defined field names
- vendor-defined units
- vendor-defined date assignment
- vendor-defined aggregation
- original missingness
- original row ordering
- original byte representation

### Canonical Dataset

The canonical sleep dataset may preserve:

- archive-defined field names
- manually transcribed values
- subjective morning observations
- confidence labels
- correction notes
- governed date decisions
- fields not supplied by the vendor export

Neither layer should silently overwrite the other.

---

## Required Mapping Before Historical Integration

Historical RingConn data should enter normalized or canonical trackers only after a documented source-to-canonical mapping is approved.

The mapping must define:

1. source filename and acquisition event
2. source field name
3. source unit
4. intended normalized field
5. date and timestamp interpretation
6. timezone assumptions or unresolved timezone status
7. treatment of multiple sleep episodes
8. duplicate-row handling
9. missing-date handling
10. blank-value handling
11. unit conversion, if any
12. derived-field rules
13. source-versus-curated discrepancy handling
14. correction provenance
15. reproducible transformation procedure

No historical backfill should be performed through manual copy-and-paste without this mapping.

---

## Timestamp and Timezone Limitation

The RingConn exports do not currently establish a fully governed timezone interpretation.

Vendor timestamps must not automatically be assumed to represent:

- UTC
- local civil time
- the date sleep began
- the date sleep ended
- the date shown in the RingConn application
- device synchronization time
- server processing time

This is especially important for:

- sessions crossing midnight
- travel across time zones
- daylight-saving transitions
- multiple sleep episodes
- date-level comparison with manually curated morning records

Timezone and date-assignment behavior must be resolved or explicitly retained as uncertain before timestamped source data are normalized.

---

## Multiple Sleep Episodes

The direct sleep export may contain more than one sleep episode associated with a calendar date.

A normalized daily sleep dataset must not silently:

- discard secondary episodes
- sum all episodes without a declared rule
- select the longest episode without documentation
- assign episodes to a date solely from row order
- force one-row-per-date structure before session semantics are understood

Possible future treatment may include:

- preserving a session-level normalized dataset
- identifying a primary sleep episode
- retaining secondary sleep episodes separately
- deriving a daily aggregate under explicit rules

The source export must remain unchanged regardless of the eventual normalization method.

---

## Missing-Date Behavior

Missing source rows must remain missing at the source layer.

The archive must not infer that an absent date means:

- zero activity
- no sleep
- no device wear
- no measurement
- synchronization failure
- intentional non-use

Missing dates may reflect:

- absent wear
- export limitations
- synchronization gaps
- provider processing behavior
- unavailable measurements
- multiple episodes assigned to adjacent dates
- undocumented vendor logic

Missing-date classification belongs in the normalized-data methodology.

---

## November 17 Provider Anomaly

The direct export includes a provider-side anomaly associated with November 17.

This anomaly should be treated as a source-quality issue rather than silently repaired.

Before normalization, the archive should determine:

- which export file or fields are affected
- whether the anomaly is limited to one row or multiple domains
- whether the same behavior appears in the application view
- whether adjacent dates are affected
- whether the issue reflects date assignment, missingness, duplication, or provider aggregation
- whether a source-backed correction is possible

Until reviewed, the source row remains preserved as exported.

Any normalized treatment must be explicitly documented in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

---

## Curated Versus Direct-Export Differences

The canonical sleep dataset and direct RingConn export were produced through different collection pathways.

Differences may arise from:

- manual transcription
- application-screen presentation
- later direct export
- changing vendor algorithms
- date assignment
- session aggregation
- multiple sleep episodes
- rounding
- missing fields
- corrected manual dates
- confidence annotations unavailable in the source export

A difference does not automatically establish that either record is wrong.

Each discrepancy should be classified as one of the following:

- exact match
- rounding-only difference
- unit or formatting difference
- date-assignment difference
- session-aggregation difference
- source-export omission
- curated-record omission
- manual transcription error
- provider anomaly
- unresolved discrepancy

No large-scale overwrite of the curated dataset is authorized.

---

## Relationship to Existing Data-Quality Findings

The new RingConn export may provide candidate source evidence relevant to existing data-quality records, including:

- unresolved awake-field duplication
- sleep-stage total discrepancies
- historical source-verification questions

These findings are currently documented in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

The existence of a direct export does not automatically resolve those findings.

Before correction, the archive must confirm:

- that the export covers the relevant dates
- that the exported field represents the same metric
- that the units and date semantics are comparable
- that the provider did not retrospectively alter the value
- that the proposed replacement is source-supported
- that the correction trail can be preserved

The RingConn export therefore represents candidate reconciliation evidence for DQ-001 through DQ-003, not automatic authorization for correction.

---

## May 2026 Structured Biomarker Integration

May 2026 represents the first archive window integrating multiple measurement domains within one coordinated snapshot cycle, including:

- DEXA
- Bod Pod and COSMED outputs
- VO₂ testing
- TruAge
- Advanced TruAge
- TruHealth

Structured values from that window were incorporated into:

- [`biomarker_snapshot.csv`](./biomarker_snapshot.csv)
- [`epigenetic_longitudinal.csv`](./epigenetic_longitudinal.csv)
- [`bloodwork_longitudinal.csv`](./bloodwork_longitudinal.csv)

Associated model-error outcomes supported by the May artifact set were incorporated into the primary model-error layer after evaluation.

The presence of multiple measurements within the same general snapshot window does not establish that all tests were collected under identical conditions or that their changes share one cause.

---

## Training Coverage

Training exposure is documented with high narrative continuity through:

- weekly reports
- contemporaneous B1 notes
- Load Integration notes
- travel and constraint records
- performance-testing artifacts
- occasional detailed movement observations

Current coverage is sufficient to establish broad exposure continuity and identify many deviations.

It is not yet sufficient for fully automated analysis of:

- exact daily exercise selection
- set and repetition counts
- external load
- rest intervals
- session duration
- training density
- progression history
- movement-specific volume

The RingConn activity export adds direct wearable activity evidence but does not replace a structured training log.

Steps and estimated calories cannot establish:

- exercise selection
- resistance-training volume
- pull-up or push-up exposure
- trap-bar load
- session intent
- movement quality
- formal versus recreational activity

A canonical `training_blocks.csv` export is planned but not yet implemented.

Until then, training should be described as **high narrative coverage**, not complete structured coverage.

---

## Recovery Coverage

Recovery evidence includes:

- wearable-derived sleep data
- HRV
- resting heart rate
- sleep heart rate
- SpO₂
- sleep duration and architecture
- subjective morning reports
- pain and mechanical signaling
- GI and stomach status
- edema and fluid context
- mental state
- functional compatibility with training

Coverage is strongest during recent active observation windows.

The direct RingConn sleep and vital-signs exports extend the available source layer but have not yet been normalized into governed daily trackers.

Limitations include:

- consumer-device estimation
- incomplete or irregular historical coverage
- possible application or algorithm changes
- unresolved timestamp and timezone behavior
- multiple sleep episodes
- provider-defined aggregation
- unresolved field-level quality questions
- absence of a canonical structured daily subjective-biomarker export

Known data-quality restrictions are recorded in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

---

## Nutrition and Supplementation Coverage

The archive contains meaningful context regarding:

- meal timing
- fasting status
- anchor foods and shakes
- hydration
- electrolyte use
- selected macronutrient strategies
- supplementation additions, removals, and dose changes

However, there is no continuous structured record of:

- total calories
- complete macronutrient intake
- micronutrient intake
- food-level intake
- exact daily supplement adherence

Nutrition and supplementation should therefore be treated as contextual explanatory variables rather than complete quantified datasets.

---

## Environmental and Perturbation Coverage

Environmental and ordinary-life factors are documented when they are salient to interpretation.

Examples include:

- travel
- schedule disruption
- altered sleep environment
- equipment or scale access
- household labor
- social and administrative workload
- heat or air-quality exposure
- illness or irritation
- sodium and hydration variation
- family events

These records are useful for perturbation analysis but are not comprehensive environmental monitoring.

The absence of a recorded factor does not establish that all other conditions were controlled.

A structured perturbation-event export is planned.

---

## Model-Error Coverage

The active model-error layer contains prospectively registered predictions and later observed outcomes.

Primary dataset:

[`model_error/model_error_gap_v1.csv`](./model_error/model_error_gap_v1.csv)

Historical reconstructed records remain segregated in:

[`model_error/historical/`](./model_error/historical/)

Current coverage includes:

- state predictions
- trajectory predictions
- prediction dates
- outcome fields
- error direction and magnitude where applicable
- closure status
- calibration context

Open records remain unscored until their defined windows end and sufficient evidence is available.

Evaluation rules for the current open block are documented in:

[`../methodology/open_prediction_evaluation_plan_041_044.md`](../methodology/open_prediction_evaluation_plan_041_044.md)

Composite UDI remains governed by documented eligibility criteria.

---

## Known Gaps

Current gaps include:

- no normalized RingConn sleep dataset
- no normalized RingConn activity dataset
- no normalized RingConn vital-signs dataset
- unresolved direct-export timezone behavior
- unresolved multiple-sleep-episode handling
- unresolved November 17 provider anomaly
- no canonical daily training-block export
- no canonical daily subjective-biomarker export
- no canonical perturbation-event export
- no continuous nutrition logging
- no systematic daily supplementation dataset
- no continuous VO₂ measurement
- incomplete environmental measurement
- irregular low-frequency biological testing
- partial reliance on manual transcription
- potential device, firmware, application, or algorithm changes
- referenced health information not always included publicly
- historical prediction reconstruction separated from the clean primary dataset
- unresolved sleep-field questions documented in `DATA_QUALITY_NOTES.md`

The direct export reduces uncertainty about source availability.

It does not eliminate uncertainty about field meaning, date semantics, measurement validity, or canonical integration.

---

## Data-Quality Boundary

A dataset may be structurally complete for a date range while containing field-specific quality restrictions.

Coverage and confidence must therefore be evaluated separately.

For example:

- a row may preserve date continuity
- most fields may remain usable
- one field may require source reconciliation
- the entire dataset need not be discarded

Canonical values are not corrected through inference.

Direct vendor-export values are not silently substituted for curated values.

Source-backed corrections follow the procedure defined in:

[`../methodology/data-collection.md`](../methodology/data-collection.md)

---

## Interpretation Boundary

Coverage limitations must be considered when evaluating:

- performance trends
- training tolerance
- recovery dynamics
- perturbation response
- model calibration
- body-composition change
- biomarker trajectories
- biological-aging outputs
- protocol effects

The archive cannot isolate every concurrent variable.

No conclusion should exceed the coverage, comparability, and source quality of the evidence supporting it.

---

## Planned Structured Expansion

Future structured datasets may include:

- `data/wearable_sleep_daily_v1.csv`
- `data/wearable_activity_daily_v1.csv`
- `data/wearable_vitals_daily_v1.csv`
- `data/daily_biomarkers.csv`
- `data/training_blocks.csv`
- `data/perturbation_events.csv`

The wearable filenames remain proposed until source-to-canonical schemas are approved.

Each new dataset must define:

- primary key
- required fields
- units
- date and time rules
- timezone treatment
- multiple-session handling
- source provenance
- missingness conventions
- correction procedure
- semantic validation rules
- transformation reproducibility
- relationship to existing curated datasets

Planned status does not imply that these files currently exist.

---

## Proposed Wearable Architecture

The intended architecture is:

```text
Byte-Preserved RingConn Source Exports
                ↓
Documented Source-to-Canonical Mapping
                ↓
Normalized Wearable Datasets
                ↓
Curated and Governed Analytical Datasets
                ↓
Retrospective Reports and Model Evaluation
```

The source exports remain preserved even after normalized trackers are created.

Normalized datasets must be reproducible from the archived source package.

Curated datasets may retain subjective, confidence, and contextual fields not present in the vendor export.

---

## Status

Coverage is expanding incrementally.

The `2026-07-21` RingConn source-export package adds a materially stronger historical wearable evidence layer.

It does not yet change the canonical status of:

- sleep
- activity
- vital signs
- daily subjective biomarkers
- training exposure

New normalized datasets will be introduced only when:

- repeated observations justify a stable schema
- source-field meanings are sufficiently defined
- timestamp and date behavior are addressed
- source-to-canonical mapping is documented
- discrepancies with curated records are preserved
- structured representation improves continuity or analysis
- added complexity does not weaken archive governance

Future additions and material coverage changes will be documented in this file and in:

[`../CHANGELOG.md`](../CHANGELOG.md)
