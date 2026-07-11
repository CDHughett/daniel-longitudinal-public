# Data Coverage

This document defines the scope, completeness, and limitations of datasets currently included in the archive.

It clarifies:

- what is tracked
- how each domain is represented
- what is structured versus narrative
- what is only measured at discrete intervals
- where known gaps or quality restrictions exist

This is a **coverage declaration**, not an interpretation layer.

Coverage status does not establish measurement validity, causal attribution, or biological significance.

---

## Coverage Status Definitions

| Status | Meaning |
|---|---|
| Structured longitudinal | Repeated observations are available in a canonical machine-readable dataset |
| High narrative coverage | Repeated contemporaneous observations are preserved, but no complete canonical structured export exists |
| Snapshot-based | Measurements occur at discrete testing intervals rather than continuously |
| Partial | Some relevant observations exist, but collection is incomplete, irregular, or limited in scope |
| Contextual only | Information appears in reports or notes without systematic structured collection |
| Not tracked | No governed recurring collection process currently exists |
| Planned | A structured export is anticipated but has not yet been implemented |

---

## Coverage Summary

| Domain | Coverage Status | Notes |
|---|---|---|
| Training exposure | High narrative coverage | Daily execution is documented through reports and contemporaneous notes; no canonical daily training-block export yet |
| Sleep | Structured longitudinal, recent; partial historical | Wearable-derived daily dataset begins 2026-02-09; earlier intervals are incomplete or absent |
| Recovery signals | Structured and narrative, recent | HRV, resting HR, sleep HR, and related signals are represented through wearable data, structured sleep records, and reports during active observation windows |
| Subjective daily biomarkers | High narrative coverage | Mental state, GI status, pain, dreams, erection quality, weight context, and related observations are recorded regularly but do not yet have a canonical public daily export |
| Body composition | Snapshot-based | DEXA, BodPod, scale weight, and related measurements occur at discrete intervals with differing methods |
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

## Dataset Locations

| Dataset or Evidence Layer | Path |
|---|---|
| Sleep longitudinal | [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) |
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

- Sleep longitudinal dataset: begins `2026-02-09`
- Weekly reports: begin `2026-W06`
- Biomarker snapshot dataset: February and May 2026 comparison points currently represented
- Epigenetic dataset: repeated low-frequency snapshot outputs
- Bloodwork dataset: periodic laboratory measurements
- Primary model-error dataset: clean governed records beginning with record 013
- Historical model-error reconstruction: records 001–012, segregated from the primary dataset

Different datasets therefore cover different observation windows.

No single structured file represents the entire archive.

---

## May 2026 Structured Biomarker Integration

May 2026 represents the first archive window integrating multiple measurement domains within one coordinated snapshot cycle, including:

- DEXA
- BodPod and COSMED outputs
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

A canonical `training_blocks.csv` export is planned but not yet implemented.

Until then, training should be described as **high narrative coverage**, not complete structured coverage.

---

## Recovery Coverage

Recovery evidence includes:

- wearable-derived sleep data
- HRV
- resting heart rate
- sleep heart rate
- sleep duration and architecture
- subjective morning reports
- pain and mechanical signaling
- GI and stomach status
- edema and fluid context
- mental state
- functional compatibility with training

Coverage is strongest during recent active observation windows.

Limitations include:

- consumer-device estimation
- incomplete historical exports
- possible application or algorithm changes
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

- no canonical daily training-block export
- no canonical daily subjective-biomarker export
- no canonical perturbation-event export
- no continuous nutrition logging
- no systematic daily supplementation dataset
- no continuous VO₂ measurement
- incomplete historical wearable coverage
- incomplete environmental measurement
- irregular low-frequency biological testing
- partial reliance on manual transcription
- potential device, firmware, application, or algorithm changes
- referenced health information not always included publicly
- historical prediction reconstruction separated from the clean primary dataset
- unresolved sleep-field questions documented in `DATA_QUALITY_NOTES.md`

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

- `daily_biomarkers.csv`
- `training_blocks.csv`
- `perturbation_events.csv`

Each new dataset must define:

- primary key
- required fields
- units
- date and time rules
- source provenance
- missingness conventions
- correction procedure
- semantic validation rules

Planned status does not imply that these files currently exist.

---

## Status

Coverage is expanding incrementally.

New datasets will be introduced only when:

- repeated observations justify a stable schema
- the source and collection process are sufficiently defined
- structured representation improves continuity or analysis
- added complexity does not weaken archive governance

Future additions and material coverage changes will be documented in this file and in [`../CHANGELOG.md`](../CHANGELOG.md).
