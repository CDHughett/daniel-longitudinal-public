# Methodology and Controls

## Overview

The Daniel Longitudinal Study is an ongoing single-subject longitudinal observational archive.

The repository prioritizes:

- continuity over novelty
- durability over peak performance
- repeatable operating conditions over staged presentation
- transparent correction over silent preservation of known error
- longitudinal evidence over isolated measurements
- model calibration over prediction defensiveness

The project documents biological, behavioral, recovery, and performance behavior across time under defined protocol constraints and incomplete real-world environmental control.

It is not:

- a randomized clinical trial
- a controlled laboratory study
- a generalized intervention program
- a substitute for medical care
- evidence that one intervention caused every observed change

The archive is designed so an outside observer can distinguish:

- what was directly measured
- what was contemporaneously observed
- what was manually transcribed
- what was derived
- what was retrospectively interpreted
- what was prospectively predicted
- what remains uncertain

---

## Study Design

**Study type:**  
Longitudinal single-subject observational study with governed self-experimentation components

**Subject:**  
One adult male subject

**Formal archive period:**  
2026 to present

**Broader context:**  
Selected historical measurements and baseline conditions may predate the formal archive period.

**Duration:**  
Multi-year continuous observation, ongoing

**Primary aim:**  
Document how sustained training, recovery discipline, nutrition stability, behavioral consistency, and ordinary-life perturbations relate to biological and functional trajectories across repeated observation windows.

**Secondary aim:**  
Evaluate model quality by registering selected predictions before outcomes are known and comparing them with later observations.

---

## Methodological Posture

The archive uses an artifact-first observational model.

The governing sequence is:

```text
Protocol Inputs
      +
Training Exposure
      +
Recovery Conditions
      +
Behavioral Execution
      +
Ordinary-Life Variability
      ↓
Physiological and Functional Response
      ↓
Source Artifact or Contemporaneous Observation
      ↓
Structured Dataset Entry
      ↓
Retrospective Interpretation
      ↓
Registered Prediction Evaluation
      ↓
Model Correction
```

The repository does not assume that every observed change is attributable to one input.

Interpretation remains bounded by:

- source quality
- measurement comparability
- temporal coverage
- known confounders
- missingness
- environmental variability
- concurrent protocol elements
- device and provider limitations

---

## Primary Outcome Domains

### Biological Aging

Tracked through repeated low-frequency measurements such as:

- DunedinPACE
- OMICm biological-age outputs
- SymphonyAge
- organ and system age estimates
- TruHealth domain scores
- related epigenetic outputs

These measures are interpreted as provider-specific longitudinal signals.

They are not treated as complete clinical descriptions of biological age.

---

### Blood and Metabolic Biomarkers

Tracked through periodic laboratory panels.

Potential domains include:

- metabolic markers
- lipid markers
- hematology
- kidney and liver markers
- inflammatory markers
- hormonal markers
- selected nutrient or health-status markers

Bloodwork is snapshot-based rather than continuous.

Not every referenced health measurement is necessarily included in the public archive.

---

### Body Composition

Tracked through methods such as:

- DEXA
- BodPod
- scale weight
- waist or related anthropometric context
- fat mass
- lean mass
- appendicular lean mass
- method-specific derived outputs

Measurements from different methods are not assumed to be interchangeable.

Comparison should preserve:

- device or provider
- collection date
- preparation conditions
- method limitations
- expected measurement variability

---

### Performance Capacity

Observed through:

- B1 aerobic execution
- formal VO₂ testing
- Load Integration
- pull-ups
- push-ups
- trap-bar work
- dead hangs
- recreational endurance exposure
- movement quality
- workload tolerance
- cross-context execution

Performance interpretation prioritizes:

- repeatability
- recovery compatibility
- mechanical quality
- adaptability
- portability
- reduced operator overhead

Peak output is not the sole performance criterion.

---

### Recovery and Autonomic Regulation

Observed through:

- daily biomarker HRV
- sleep HRV
- resting heart rate
- sleeping heart rate
- total sleep
- sleep continuity
- estimated sleep stages
- subjective morning state
- fatigue
- pain
- GI status
- next-session performance
- response to accumulated workload

Consumer wearable outputs are treated as longitudinal estimates rather than definitive clinical measurements.

Daily HRV and sleep HRV remain distinct metrics and should be labeled separately.

---

### Behavioral Stability

Observed through:

- protocol continuity
- return to execution after disruption
- response to missed or constrained sessions
- absence of compensatory behavior
- adherence under ordinary-life variability
- repository stewardship
- distinction between valid constraint and behavioral failure
- resistance to proof-seeking progression

Behavioral stability is not defined as uninterrupted perfection.

It includes the ability to resume normal operation without identity threat, narrative repair, or unnecessary compensation.

---

## Stabilized Inputs

The archive attempts to keep selected inputs reasonably stable where practical.

Examples include:

- recurring B1 structure
- recurring Load Integration structure
- broadly stable training frequency
- stable core supplementation
- recurring meal and feeding patterns
- hydration consistency
- repeated sleep opportunity
- consistent measurement methods where available
- recurring weekly reporting
- governed data-entry procedures

These are **stabilized inputs**, not proof of complete environmental control.

A stabilized input may still vary because of:

- travel
- schedule displacement
- household demands
- equipment access
- social context
- illness
- environmental exposure
- meal timing
- hydration
- GI timing
- sleep environment
- device behavior

The repository should not describe normal-life observation as occurring under tightly controlled environmental conditions.

---

## Environmental Context

Observation takes place primarily under ordinary real-world conditions.

Relevant environmental or contextual variables may include:

- travel
- work or administrative demands
- household labor
- family events
- social activity
- altered sleep environment
- heat
- air quality
- sodium exposure
- hydration variation
- meal timing
- equipment availability
- scale access
- illness or irritation
- recreational physical activity

These variables are documented when known and material.

The absence of a recorded contextual factor does not prove that all other conditions were controlled.

Environmental context may explain uncertainty without being used to excuse every unfavorable result.

---

## Intervention Philosophy

Protocol changes are introduced conservatively.

A substantive modification may be considered when supported by evidence such as:

1. repeated adaptation plateau
2. repeated recovery-compatible capacity increase
3. objective biological or performance feedback
4. mechanical limitation requiring correction
5. formal phase transition
6. repeated perturbation evidence supporting a new operator rule

A change should not be introduced solely because:

- one session felt easy
- one metric improved
- progression is psychologically appealing
- a prediction outcome is desired
- a snapshot is approaching
- additional complexity is available

Substantive changes should be:

- documented before implementation
- bounded
- observable
- reversible where practical
- compatible with recovery
- separated from proof-seeking behavior

Detailed governance requirements are defined in:

[`GOVERNANCE.md`](./GOVERNANCE.md)

---

## Protocol Continuity

The archive distinguishes:

- active protocol
- historical protocol
- proposed protocol
- paused experiment
- optional recreational activity
- ordinary-life physical workload

A historical or superseded protocol may remain in the repository for provenance.

It must not be treated as active merely because the file remains present.

An intervention should not be used to explain an outcome unless documented exposure occurred during the relevant observation window.

---

## Collection Methodology

Data may enter the archive through:

- provider-generated source artifacts
- direct device exports
- screenshots
- manual structured transcription
- contemporaneous collection notes
- weekly reports
- derived analysis

The preferred source hierarchy is:

1. verified primary source artifact
2. direct provider or device export
3. contemporaneous structured transcription
4. contemporaneous collection note
5. weekly retrospective report
6. later synthesis grounded in preserved evidence
7. unsupported memory

Unsupported memory is insufficient to overwrite a governed value.

Detailed collection procedures are defined in:

[`methodology/data-collection.md`](./methodology/data-collection.md)

---

## Structured Data and Narrative Evidence

The repository distinguishes structured coverage from narrative coverage.

### Structured Data

Machine-readable files support:

- continuity checks
- longitudinal comparison
- reproducible calculation
- automated validation
- prediction scoring

### Narrative Evidence

Reports and collection notes preserve:

- mechanical observations
- subjective state
- environmental context
- training quality
- perturbations
- candidate evidence
- reasons for protocol decisions

Narrative evidence may be strong without being numerically complete.

A weekly report is not a substitute for a canonical daily training export.

A structured dataset is not automatically more trustworthy than the source artifact from which it was transcribed.

Coverage boundaries are documented in:

[`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)

---

## Missingness

Missing data remain visibly missing.

The archive does not use:

- zero as a substitute for unknown
- copied neighboring values
- unsupported interpolation
- retrospective estimation
- assumed routine behavior
- calculated reconstruction presented as direct observation

Derived or imputed values may exist only in a separate analysis layer and must be labeled clearly.

Missingness may limit evaluation without invalidating the entire observation window.

---

## Data Corrections

Historical source values are not silently rewritten.

However, the archive permits source-backed correction when evidence confirms that a structured value or representation is inaccurate.

A correction must:

1. identify the affected date, field, or artifact
2. use the strongest available source evidence
3. change only the affected content
4. preserve unrelated valid values
5. preserve the previous repository state through Git history
6. document the correction
7. update applicable quality notes
8. rerun relevant validation
9. review dependent analyses

Corrections are archive-maintenance events.

They are not new biological observations.

A suspicious value remains unresolved when the original source is unavailable.

Known quality questions are documented in:

[`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

---

## Measurement Comparability

Measurements should be compared only after reviewing:

- provider
- device
- assay family
- field definition
- unit
- software or algorithm version
- collection timing
- preparation conditions
- source completeness
- transcription accuracy

A shared field name does not guarantee longitudinal comparability.

Changes in device software, provider reporting, or algorithm behavior should be documented in:

[`MEASUREMENT_SOURCES.md`](./MEASUREMENT_SOURCES.md)

---

## Derived Values

Derived values may include:

- weekly averages
- percentage change
- trend estimates
- prediction error
- recovery duration
- comparison ratios
- composite summaries

A derived value should:

- identify its source fields
- use a documented formula
- preserve the underlying observations
- remain reproducible
- be labeled as derived

Derived values must not silently replace source values.

---

## Interpretation Framework

Interpretation occurs after evidence accumulates.

Interpretive priority is generally:

1. source integrity
2. temporal continuity
3. repeated evidence
4. cross-domain agreement
5. functional consequence
6. plausible contextual explanation
7. uncertainty and alternative interpretations

Interpretation should avoid:

- causal certainty from correlation
- overreaction to one wearable value
- extrapolation from one favorable session
- treating absence of symptoms as proof of unlimited reserve
- interpreting all variability as regression
- interpreting all favorable variability as progression
- relabeling an unfavorable result after the fact

Weekly reports remain retrospective at closeout.

Candidate evidence may be recorded during an active week when clearly identified as provisional.

---

## Prediction and Model-Error Layer

The archive permits formally registered forward predictions within the model-error layer.

Registered predictions must be:

- stated before the relevant outcome is known
- time-bounded
- sufficiently specific to evaluate
- preserved without hindsight revision
- allowed to remain open when evidence is insufficient
- retained when incorrect

Candidate evidence may be documented while a record remains open.

Candidate evidence does not automatically:

- change the prediction
- determine the outcome
- justify early closure
- authorize protocol progression
- establish a phase transition

Prediction evaluation methodology is documented in:

- [`methodology/prediction_evaluation.md`](./methodology/prediction_evaluation.md)
- [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

The purpose of prediction tracking is model calibration, not demonstration of certainty.

---

## Drift Monitoring Framework

Potential negative trajectory drift is monitored through clusters of evidence rather than isolated values.

Relevant signals may include:

- sustained sleep disruption
- HRV suppression
- elevated sleeping or resting heart rate
- persistent fatigue
- pain or connective-tissue signaling
- loss of normal B1 compatibility
- loss of Load Integration quality
- reduced completion capacity
- mood or cognitive disruption
- GI or systemic disturbance
- need for unplanned recovery intervention

A single unusual night or session is insufficient to establish persistent drift.

Corrective action prioritizes:

- safety
- recovery
- protocol stability
- source verification
- proportional response

Corrective action may still count as failure of a recovery prediction even when it represents good governance.

---

## Perturbation Handling

Perturbations may include:

- travel
- illness
- disrupted sleep
- environmental exposure
- schedule loss
- equipment inaccessibility
- unusual physical workload
- family or social events

Perturbations are not engineered merely to prove resilience.

Natural perturbations may provide evidence regarding:

- portability
- recovery slope
- return to baseline
- constraint recognition
- behavioral stability
- protocol robustness

Missed execution due to genuine environmental constraint is not automatically classified as behavioral failure.

The response after the perturbation remains part of the observation.

---

## Phase Interpretation

Phases describe retrospectively identified operating states.

A phase transition is not established by:

- one measurement
- one session
- one week
- prediction accuracy
- subjective confidence
- elapsed time alone
- isolated reduced effort
- candidate future-phase characteristics

Phase declaration requires the criteria defined in:

[`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

Open prediction outcomes may contribute evidence but do not independently declare a phase.

---

## Versioning and Change Control

Material changes should be documented when they affect:

- training architecture
- nutrition architecture
- supplementation
- recovery strategy
- measurement methodology
- dataset schema
- collection procedure
- correction procedure
- prediction evaluation
- interpretation framework
- phase governance
- release structure

Depending on scope, updates may be recorded in:

- `CHANGELOG.md`
- `VERSIONING.md`
- dataset annotations
- methodology documents
- snapshot documentation
- audit records

Minor day-to-day variability does not automatically constitute protocol change.

A new rule must not be represented as though it governed historical data unless the record supports that claim.

---

## Audit Framework

Audits may examine:

- repository structure
- link integrity
- CSV syntax
- schema continuity
- date continuity
- semantic field consistency
- source reconciliation
- checksums
- report continuity
- prediction continuity
- metadata
- governance alignment
- navigation
- release readiness

Audits identify and constrain correction.

They should not rewrite the evidence they are evaluating.

Audit cadence currently includes periodic Wednesday and Saturday reviews, with additional checks around:

- weekly rollover
- snapshot integration
- major methodology changes
- versioned releases

---

## Reproducibility Considerations

The archive may contain practices that are operationally transferable, such as:

- consistent data capture
- explicit governance
- source preservation
- progressive training management
- recovery prioritization
- uncertainty documentation
- prediction auditing

Biological outcomes remain subject-specific.

Important individual factors include:

- genetics
- medical history
- prior training history
- body size and composition
- psychology and adherence
- medication and supplementation
- environment
- measurement context

The repository should be interpreted as a governed case study rather than a universal prescription.

---

## Limitations

Important limitations include:

- single-subject design
- absence of randomized controls
- incomplete environmental control
- concurrent interventions
- consumer wearable limitations
- low-frequency biological testing
- partial manual transcription
- incomplete historical structured data
- method and provider variability
- missing public source material
- inability to isolate many causal mechanisms
- potential observer and operator bias

Repeated measurement and transparent governance reduce some limitations.

They do not eliminate them.

---

## Scope Boundary

This repository does not:

- provide medical advice
- establish clinical efficacy
- guarantee outcomes
- establish population-level causality
- prove that one intervention caused a result
- provide a protocol suitable for direct replication without independent review
- treat a favorable biomarker as proof of total-system improvement
- treat prediction accuracy as proof of authority

It documents one longitudinal system under defined constraints and incomplete environmental control.

---

## Related Documents

- [`GOVERNANCE.md`](./GOVERNANCE.md)
- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)
- [`DATASET_OVERVIEW.md`](./DATASET_OVERVIEW.md)
- [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- [`methodology/prediction_evaluation.md`](./methodology/prediction_evaluation.md)
- [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)
- [`MEASUREMENT_SOURCES.md`](./MEASUREMENT_SOURCES.md)
- [`VERSIONING.md`](./VERSIONING.md)
- [`CHANGELOG.md`](./CHANGELOG.md)

---

## Version Note

This document was aligned on 2026-07-15 with the archive’s current:

- incomplete environmental-control boundary
- source hierarchy
- structured and narrative evidence layers
- source-backed correction procedure
- registered prediction framework
- phase-governance standard
- audit methodology

The revision does not alter any source value, protocol exposure, prediction record, closed outcome, or phase status.
