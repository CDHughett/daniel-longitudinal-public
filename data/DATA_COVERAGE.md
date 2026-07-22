# Data Coverage

This document defines the scope, completeness, and limitations of evidence currently included in the archive.

It clarifies:

- what is tracked
- how each domain is represented
- what is structured versus narrative
- what is preserved as direct source evidence
- what is measured only at discrete intervals
- where known gaps or quality restrictions exist
- which possible derived layers are intentionally deferred

This is a **coverage declaration**, not an interpretation layer.

Coverage status does not establish:

- measurement validity
- causal attribution
- biological significance
- clinical meaning
- cross-source equivalence

---

## Coverage Status Definitions

| Status | Meaning |
|---|---|
| Source-preserved | Original provider or device export is retained without analytical or interpretive modification |
| Structured longitudinal | Repeated observations are available in a canonical machine-readable dataset |
| High narrative coverage | Repeated contemporaneous observations are preserved, but no complete canonical structured dataset exists |
| Snapshot-based | Measurements occur at discrete testing intervals rather than continuously |
| Partial | Some relevant observations exist, but collection is incomplete, irregular, or limited in scope |
| Contextual only | Information appears in reports or notes without systematic structured collection |
| Not tracked | No governed recurring collection process currently exists |
| Planned | A governed structured dataset is expected but has not yet been implemented |
| Deferred | A possible derived layer has been considered but is not currently required or scheduled |

Source-preserved coverage and canonical structured coverage are separate states.

A provider export may materially improve provenance without becoming a canonical analytical dataset.

---

## Coverage Summary

| Domain | Coverage Status | Notes |
|---|---|---|
| Training exposure | High narrative coverage | Daily execution is documented through reports and contemporaneous notes; no canonical daily training-block dataset yet |
| Wearable activity | Source-preserved | Periodic RingConn activity exports are retained as acquisition packages; no archive-defined normalized activity tracker is currently required |
| Sleep | Structured longitudinal, recent; source-preserved historical coverage | Canonical curated daily sleep coverage begins 2026-02-09; a broader episode-level RingConn export is preserved separately |
| Recovery and vital signs | Structured, narrative, and source-preserved | HRV, resting HR, sleep HR, SpO₂, and related signals appear across curated records, reports, screenshots, and the direct RingConn export |
| Subjective daily biomarkers | High narrative coverage | Mental state, GI status, pain, dreams, erection quality, bodyweight context, and related observations are recorded regularly but do not yet have a canonical public daily dataset |
| Body composition | Snapshot-based | DEXA, Bod Pod, scale weight, and related measurements occur at discrete intervals using differing methods |
| Blood biomarkers | Snapshot-based | Periodic laboratory panels only; not all referenced health information is publicly included |
| Epigenetic and aging measures | Structured longitudinal, snapshot-based | TruAge, Advanced TruAge, TruHealth, and related outputs are represented across repeated testing windows |
| VO₂ and performance testing | Partial, event-based | Formal testing is collected at discrete events rather than continuously |
| Nutrition | Contextual only | Meal timing, fasting state, intake patterns, and selected nutrition context appear in reports; no continuous nutrition dataset exists |
| Supplementation | Contextual only | Material supplement changes and continuity are documented when relevant; no canonical adherence dataset exists |
| Environmental factors | Partial | Travel, schedule, heat, air quality, equipment access, and related conditions are documented when salient but are not comprehensively measured |
| Perturbation events | High narrative coverage; structured dataset planned | Travel, illness, environmental disruption, and workload events are preserved in reports but not yet consolidated into a canonical event dataset |
| Model error and prediction | Structured longitudinal | Primary prospective prediction records are maintained separately from historical reconstruction |
| Repository governance | High documentary coverage | Audits, changelog entries, phase criteria, methodology, protocol state, and release practices are version controlled |

---

## Dataset and Source Locations

| Dataset or Evidence Layer | Path |
|---|---|
| Curated sleep longitudinal | [`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv) |
| RingConn direct source-export package | [`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/) |
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

# Temporal Coverage

The archive operates through continuous observation with progressively expanding public representation.

## Observation Continuity

The governed observation period begins in 2026-W01 and continues through the present archive state.

This includes observation of:

- training exposure
- recovery conditions
- behavioral execution
- biological measurements
- protocol state
- environmental and life-context perturbations

Not every observation is represented in a public machine-readable dataset.

Continuous observation should not be interpreted as continuous structured measurement of every domain.

---

## Structured Reporting Coverage

The consistent weekly reporting layer begins at:

```text
2026-W06
```

Weekly reports provide a recurring documentary layer for:

- protocol exposure
- recovery state
- notable deviations
- contextual events
- retrospective weekly interpretation

Weekly reports are evidence-rich but are not substitutes for canonical daily datasets.

---

## Dataset-Specific Coverage

Current structured and source-preserved layers begin at different times.

Examples:

- curated sleep longitudinal dataset: begins `2026-02-09`
- direct RingConn source-export coverage: begins `2025-07-21`
- RingConn export acquisition: `2026-07-21`
- weekly reports: begin `2026-W06`
- biomarker snapshot dataset: February and May 2026 comparison points currently represented
- epigenetic dataset: repeated low-frequency snapshot outputs
- bloodwork dataset: periodic laboratory measurements
- primary model-error dataset: governed records beginning with record 013
- historical model-error reconstruction: records 001–012, segregated from the primary dataset

Different files therefore cover different periods and evidence types.

No single structured file represents the complete archive.

---

# Direct RingConn Source-Export Coverage

A direct RingConn export package was acquired on `2026-07-21` and preserved in:

[`source_exports/ringconn/2026-07-21/`](./source_exports/ringconn/2026-07-21/)

The package contains:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- `README.md`
- `checksums.txt`

The three CSVs are preserved byte-for-byte as downloaded.

Filename normalization occurred at the filesystem level without changing file contents.

---

## Byte-Preservation Verification

Git text conversion is disabled for direct source-export CSVs through:

```gitattributes
data/source_exports/**/*.csv -text
```

Post-commit external verification confirmed:

- all three repository files match the original RingConn downloads byte-for-byte
- original CRLF line endings remain intact
- the existing checksum manifest remained unchanged
- all three source-export SHA-256 values pass
- a fresh GitHub ZIP preserves the original bytes
- all registered archive checksums pass

Verified file sizes:

| File | Bytes |
|---|---:|
| `ringconn-sleep-export.csv` | 38,703 |
| `ringconn-activity-export.csv` | 8,171 |
| `ringconn-vital-signs-export.csv` | 16,059 |

The source-export package is therefore considered mechanically preserved.

Mechanical integrity does not establish semantic validity for every provider field or row.

---

## Pre-Publication Screening

Read-only screening identified:

- no obvious administrative-identifier fields in the exported headers
- no email-like values
- expected wearable-domain fields only

This reduces obvious public-distribution risk.

It does not:

- establish clinical validity
- establish complete anonymization under every possible inference
- convert the files into canonical analytical datasets
- resolve provider-specific field semantics

---

## Sleep Export Coverage

The direct sleep export contains:

- 366 sleep-episode rows
- 358 unique wake dates
- represented wake-date range from `2025-07-21` through `2026-07-21`
- eight dates containing more than one sleep episode
- eight absent wake dates
- timestamps without explicit UTC offsets
- no provider-supplied primary-sleep or nap classification

The export is episode-level.

Its row count is not equivalent to covered calendar days.

The file should not be forced into a one-row-per-date structure without an explicit analytical requirement and documented transformation rules.

---

## Activity Export Coverage

The direct activity export contains:

- 360 daily rows
- 360 unique dates
- represented date range from `2025-07-21` through `2026-07-20`
- absent rows from `2026-01-04` through `2026-01-08`
- no row for `2026-07-21`

Missing source dates remain missing.

The absence of a row does not establish zero activity.

---

## Vital-Sign Export Coverage

The direct vital-sign export contains:

- 360 daily rows
- 360 unique dates
- represented date range from `2025-07-21` through `2026-07-20`
- missing dates corresponding to the activity export
- daily minimum, average, and maximum heart-rate values
- daily minimum, average, and maximum SpO₂ values
- daily minimum, average, and maximum HRV values

Provider-defined daily metrics must not be substituted for differently defined curated metrics.

Examples include:

- daily minimum heart rate versus resting heart rate
- daily average HRV versus sleep HRV
- whole-day SpO₂ versus sleep-period SpO₂

---

# Source-Export Role

The RingConn exports are source artifacts.

They do not automatically replace, correct, or extend:

[`sleep_longitudinal_v1.csv`](./sleep_longitudinal_v1.csv)

The source export and curated dataset serve different roles.

## Direct Export

The direct export preserves:

- provider-defined field names
- provider-defined units
- provider-defined date assignment
- provider-defined aggregation
- original missingness
- original row ordering
- original byte representation
- the provider’s database state at export time

## Curated Dataset

The curated sleep dataset may preserve:

- archive-defined field names
- manually transcribed contemporaneous values
- subjective morning observations
- confidence labels
- correction notes
- governed date decisions
- fields unavailable in the provider export
- values visible in the application during the original observation window

Neither layer should silently overwrite the other.

---

# Periodic RingConn Export Policy

Periodic direct exports are the current wearable-preservation model.

Recommended directory structure:

```text
data/source_exports/ringconn/YYYY-MM-DD/
```

Each acquisition package should contain:

- original provider-export files
- an acquisition `README.md`
- a checksum manifest

A later export:

- does not overwrite an earlier acquisition
- may overlap the same historical dates
- remains a separate provider-source event
- may reflect provider recalculation or later software behavior
- does not silently replace curated records
- does not require a normalized longitudinal tracker

Export frequency may align with:

- major biological snapshot cycles
- annual archive review
- a defined reconciliation need
- a material device or provider change
- an external publication requirement

No mandatory export cadence is currently imposed.

---

# Timestamp and Timezone Limitation

RingConn export timestamps do not contain explicit UTC offsets.

The represented interval includes travel.

The repository therefore does not assume that every timestamp represents:

- UTC
- America/New_York
- the date sleep began
- the date sleep ended
- the date displayed in the RingConn application
- device synchronization time
- provider processing time

This limitation matters for:

- sessions crossing midnight
- travel across time zones
- daylight-saving transitions
- multiple sleep episodes
- comparison with curated morning records

The source timestamp remains preserved exactly as exported.

UTC offsets are not invented.

---

# Multiple Sleep Episodes

The sleep export contains more than one episode for some wake dates.

The archive currently preserves those episodes without attempting to:

- discard secondary episodes
- classify naps
- select a primary episode
- sum all sessions into one day
- assign a session based only on row order
- reconcile episodes with the curated daily row

A transformation may be created later only when a specific analysis requires it.

Such a transformation would need to define:

- session date
- primary-sleep selection
- secondary-session treatment
- midnight behavior
- travel and timezone handling
- missingness
- source-row traceability

The original source export would remain unchanged.

---

# Missing-Date Behavior

Missing source rows remain missing.

The archive does not infer that an absent date means:

- zero activity
- zero sleep
- no device wear
- no measurement
- synchronization failure
- intentional non-use
- provider deletion

Missing dates may reflect:

- absent wear
- synchronization gaps
- export limitations
- unavailable measurements
- provider processing behavior
- date-assignment rules
- undocumented vendor logic

Classification should occur only when sufficient evidence exists.

---

# Provider Anomalies

The source package includes at least one provider-side anomaly associated with November 17.

The affected source state remains preserved as exported.

The anomaly should be examined only when:

- analysis depends on the affected date
- it bears directly on source reconciliation
- correction of a curated value is being considered
- repeated export behavior suggests a broader provider issue

The source artifact itself must not be edited to remove or repair the anomaly.

Any analytical treatment should be recorded in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

---

# Curated Versus Direct-Export Differences

The curated sleep dataset and direct RingConn export were created through different pathways.

Differences may result from:

- manual transcription
- application-screen presentation
- later provider export
- provider recalculation
- changing algorithms
- date assignment
- sleep-session aggregation
- multiple sleep episodes
- rounding
- missing source fields
- confidence annotations unavailable in the provider export
- correction of an earlier manually entered date
- source-state differences

A difference does not automatically establish that either record is wrong.

Discrepancies may be classified as:

- exact match
- rounding-only difference
- unit or formatting difference
- date-assignment difference
- session-aggregation difference
- provider-export omission
- curated-record omission
- confirmed transcription error
- provider anomaly
- unresolved source-state difference

No large-scale overwrite of the curated dataset is authorized.

---

# Relationship to Data-Quality Findings

The direct RingConn export may provide candidate source evidence for existing data-quality questions.

These findings are documented in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

The existence of the export does not automatically resolve a finding.

Before using it to correct a curated field, the archive must establish:

- that the export covers the relevant date
- that the source field represents the same metric
- that units are compatible
- that date semantics are compatible
- that session aggregation is understood
- whether the provider may have recalculated the value
- that the correction can be documented and traced
- that dependent reports or summaries have been reviewed

The export is therefore candidate reconciliation evidence rather than automatic correction authority.

---

# Optional Future Wearable Transformation

No normalized RingConn dataset is currently active, required, or scheduled.

Previously proposed files such as:

```text
data/wearable_sleep_sessions_v1.csv
data/wearable_activity_daily_v1.csv
data/wearable_vitals_daily_v1.csv
```

are deferred.

The absence of those files is not currently considered a coverage failure.

A transformed wearable layer may become useful when:

- repeated historical analysis requires merged export packages
- provider schemas change across acquisitions
- automated comparison becomes operationally necessary
- publication requires stable archive-defined fields
- a specific model-error question requires broader historical analysis
- manual reconciliation becomes burdensome

Any future transformation must be:

- separate from the source exports
- reproducible
- versioned
- documented
- source-row traceable
- explicit about date and timezone rules
- explicit about multiple-session behavior
- explicit about missingness
- non-destructive to the original acquisition packages

The source exports remain the preserved evidence layer regardless of whether a transformed layer is later created.

---

# Current Wearable Architecture

The current architecture is:

```text
Periodic Byte-Preserved RingConn Exports
                  ↓
Acquisition README and SHA-256 Checksums
                  ↓
Targeted Reconciliation or Analysis When Needed
                  ↓
Optional Reproducible Derived Layer, If Justified
                  ↓
Retrospective Reporting or Model Evaluation
```

This structure avoids creating a permanent normalization workload before a concrete analytical need exists.

---

# May 2026 Structured Biomarker Integration

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

The presence of multiple measurements within the same general snapshot window does not establish that:

- all tests were collected under identical conditions
- all measurement changes share one cause
- provider methods are interchangeable

---

# Training Coverage

Training exposure is documented with high narrative continuity through:

- weekly reports
- contemporaneous B1 notes
- Load Integration notes
- travel and constraint records
- performance-testing artifacts
- detailed movement observations when relevant

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

The RingConn activity export adds direct wearable activity evidence.

It does not replace a structured training record.

Steps and RingConn-reported calories cannot establish:

- resistance-training volume
- movement selection
- pull-up or push-up exposure
- trap-bar load
- session intent
- movement quality
- formal versus recreational activity

A canonical `training_blocks.csv` dataset remains planned but has not yet been implemented.

Until then, training should be described as **high narrative coverage**, not complete structured coverage.

---

# Recovery Coverage

Recovery evidence includes:

- wearable-derived sleep values
- sleep HRV
- daily HRV
- resting heart rate
- sleep average heart rate
- daily heart-rate summaries
- SpO₂
- sleep duration and architecture
- subjective morning reports
- pain and mechanical signaling
- GI and stomach status
- edema and fluid context
- mental state
- functional compatibility with training

Coverage is strongest during recent active observation windows.

The direct RingConn exports extend the preserved historical source layer.

They do not create a second canonical recovery dataset.

Limitations include:

- consumer-device estimation
- historical application and firmware uncertainty
- possible provider algorithm changes
- unresolved timestamp and timezone behavior
- multiple sleep episodes
- provider-defined aggregation
- incomplete source dates
- unresolved field-level quality questions
- absence of a canonical public daily subjective-biomarker dataset

Known restrictions are recorded in:

[`DATA_QUALITY_NOTES.md`](./DATA_QUALITY_NOTES.md)

---

# Nutrition and Supplementation Coverage

The archive contains meaningful context regarding:

- meal timing
- fasting status
- anchor foods and shakes
- hydration
- electrolyte use
- selected macronutrient strategies
- supplement additions, removals, and dose changes

There is no continuous structured record of:

- total calories
- complete macronutrient intake
- micronutrient intake
- food-level intake
- exact daily supplement adherence

Nutrition and supplementation remain contextual explanatory variables rather than complete quantified datasets.

---

# Environmental and Perturbation Coverage

Environmental and ordinary-life factors are documented when salient.

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

These records are useful for perturbation analysis but do not constitute comprehensive environmental monitoring.

The absence of a recorded factor does not establish that all other conditions were controlled.

A structured perturbation-event dataset remains planned.

---

# Model-Error Coverage

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

# Known Gaps and Deferred Layers

Current material gaps include:

- no canonical daily training-block dataset
- no canonical daily subjective-biomarker dataset
- no canonical perturbation-event dataset
- no continuous nutrition logging
- no systematic daily supplementation dataset
- no continuous VO₂ measurement
- incomplete environmental measurement
- irregular low-frequency biological testing
- partial reliance on manual transcription
- incomplete historical software and firmware provenance
- unresolved wearable timestamp and timezone behavior
- unresolved multiple-sleep-episode classification
- potential provider anomalies or later recalculation
- referenced health information not always included publicly
- historical prediction reconstruction separated from the primary prediction dataset
- unresolved sleep-field questions documented in `DATA_QUALITY_NOTES.md`

Deferred but not currently required:

- normalized RingConn sleep sessions
- normalized RingConn activity days
- normalized RingConn vital-sign days
- merged multi-export wearable history

The source-export layer reduces uncertainty about source availability.

It does not eliminate uncertainty about:

- field meaning
- date semantics
- measurement validity
- provider recalculation
- canonical integration
- cross-source equivalence

---

# Data-Quality Boundary

A file may be structurally complete for a represented interval while containing field-specific restrictions.

Coverage and confidence must be evaluated separately.

For example:

- a date may be present
- most fields may remain usable
- one metric may require source reconciliation
- the whole row need not be discarded

Canonical values are not corrected through inference.

Direct provider values are not silently substituted for curated values.

Source-backed corrections follow:

[`../methodology/data-collection.md`](../methodology/data-collection.md)

---

# Interpretation Boundary

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

No conclusion should exceed the:

- coverage
- comparability
- semantic clarity
- source quality
- measurement confidence

of the supporting evidence.

---

# Planned Structured Expansion

Governed future datasets may include:

- `data/daily_biomarkers.csv`
- `data/training_blocks.csv`
- `data/perturbation_events.csv`

Each new canonical dataset must define:

- primary key
- required fields
- units
- date and time rules
- source provenance
- missingness conventions
- correction procedure
- semantic validation rules
- relationship to existing narrative and source evidence

Planned status does not imply that these files currently exist.

Wearable normalization remains deferred and is not part of routine planned expansion.

---

# Status

Coverage is expanding incrementally.

The `2026-07-21` RingConn source-export package adds a materially stronger historical wearable evidence layer.

It does not alter the canonical status of:

- curated sleep
- training exposure
- subjective daily biomarkers
- model-error records
- weekly reports
- phase status

Current wearable maintenance consists of:

- periodic provider exports
- acquisition-specific provenance
- byte preservation
- checksum verification
- targeted reconciliation when justified

A derived wearable dataset will be introduced only when a defined analytical need outweighs its continuing maintenance cost.

Future additions and material coverage changes will be documented in this file and in:

[`../CHANGELOG.md`](../CHANGELOG.md)

---

## Version Note

This document was revised on 2026-07-22 to:

- register completion of the direct RingConn acquisition package
- document verified byte preservation and external ZIP validation
- distinguish source-preserved wearable coverage from canonical structured coverage
- establish periodic immutable exports as the current maintenance model
- defer normalized wearable trackers until a specific analytical need exists
- preserve curated-versus-export source-state distinctions
- document episode, date, timezone, missingness, and provider-behavior limitations
- preserve existing data-quality restrictions
- confirm that canonical sleep data were not modified during source-export ingestion
