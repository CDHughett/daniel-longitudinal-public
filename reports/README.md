# Reports

This directory contains structured observational summaries of system state across defined time windows.

Reports operate as the repository’s primary interpretation layer.

They organize preserved evidence without replacing:

- source artifacts
- structured datasets
- contemporaneous collection notes
- formally registered prediction records

Reports may summarize evidence, but they do not supersede the sources beneath them.

---

## Report Modes

The archive contains two primary report modes.

### 1. Active Observation Reports

Active observation reports are in-progress weekly collection documents.

They may record:

- current training exposure
- recovery signals
- sleep and wearable context
- bodyweight and fluid behavior
- subjective morning state
- GI or pain status
- environmental and schedule constraints
- perturbations
- contemporaneous mechanical observations
- candidate evidence relevant to an open model-error record
- reasons for maintaining or withholding protocol changes

Active reports may be updated during the observation window.

Their purpose is to preserve contemporaneous evidence before weekly interpretation is finalized.

Active reports must distinguish:

- direct observation
- source-derived measurement
- provisional interpretation
- candidate model-error evidence
- unresolved uncertainty

An active report may identify that an observation is relevant to an open prediction.

It may not:

- rewrite the registered prediction
- assign an outcome before the observation window closes
- convert candidate evidence into automatic closure
- introduce an unregistered forward prediction
- declare a phase transition from an isolated observation
- create evidence that was not contemporaneously preserved

---

### 2. Retrospective Reports

Retrospective reports are completed after the applicable observation window closes or sufficient evidence accumulates.

They may include:

- weekly closeout interpretation
- comparison across measurement events
- body-composition summaries
- biological snapshot synthesis
- performance and recovery summaries
- perturbation-response analysis
- phase closeout or transition analysis
- model-error evidence summaries
- cross-period synthesis

Retrospective reports remain bounded by:

- preserved source artifacts
- structured datasets
- contemporaneous observations
- known collection conditions
- documented missingness
- measurement comparability
- existing governance rules

Retrospective interpretation must not be used to:

- invent unrecorded events
- replace missing data with memory
- conceal unfavorable outcomes
- revise a prediction after its result is known
- force a phase declaration
- overstate causal certainty

---

## Weekly Report Lifecycle

A weekly report generally moves through the following states:

```text
Initialized
→ Active Collection
→ Weekly Closeout
→ Retrospective Record
```

### Initialized

The report defines:

- current phase context
- active observation targets
- known constraints
- protocol boundaries
- applicable model-error records

Initialization may include registered observation targets.

It must not introduce an informal prediction that bypasses the model-error layer.

### Active Collection

Contemporaneous observations may be added as the week progresses.

Entries should preserve:

- date or temporal context
- observed behavior
- relevant measurement source
- uncertainty
- whether evidence is provisional

### Weekly Closeout

At closeout, the report may synthesize:

- execution
- recovery
- constraints
- bodyweight and fluid context
- sleep
- perturbations
- model-error relevance
- governance outcomes

Interpretation becomes retrospective only after the weekly window closes.

### Retrospective Record

After closeout, the report becomes part of the historical interpretation layer.

Later factual corrections may be made when supported by source evidence and documented through Git history.

Historical interpretation should not be rewritten merely because later outcomes changed the preferred narrative.

---

## Relationship to Source Artifacts

Primary source artifacts are commonly stored in:

- `/snapshots`
- provider reports
- wearable exports
- testing outputs
- checksum-verified binary files

Source artifacts preserve the closest available representation of the original measurement.

Reports may cite or summarize those artifacts.

Reports do not replace them.

When a report conflicts with a verified source artifact:

1. preserve the existing state
2. verify the source
3. determine whether the conflict is transcriptional, structural, or interpretive
4. correct only the affected content
5. preserve the prior version through Git history
6. document material corrections
7. review dependent summaries

---

## Relationship to Structured Data

Canonical structured datasets are generally stored in `/data`.

Structured datasets support:

- continuity checks
- longitudinal comparison
- weekly averages
- derived calculations
- automated validation
- prediction evaluation

Reports may summarize structured data, but the summary should preserve important distinctions.

Examples include:

- daily biomarker HRV versus sleep HRV
- resting heart rate versus sleep average heart rate
- measured bodyweight versus post-training or post-GI-clearance weight
- direct measurements versus derived weekly averages
- provider-generated values versus manually calculated values

A report should not merge distinct metrics merely because they share a familiar label.

---

## Relationship to Contemporaneous Notes

Some meaningful observations are not adequately represented by formal devices or datasets.

Reports may preserve contemporaneous observations such as:

- movement quality
- divided-attention execution
- pain or mechanical signaling
- grip or bar-contact comfort
- subjective effort
- environmental context
- social load
- schedule displacement
- ordinary-life workload
- reasons a session was delayed, paused, or modified

These observations may later contribute to:

- weekly interpretation
- perturbation analysis
- model-error evaluation
- phase analysis

Narrative evidence must remain tied to observed behavior rather than rhetorical framing.

---

## Relationship to the Model-Error Layer

Formally registered forward predictions are maintained in the model-error layer.

Reports may:

- identify evidence relevant to an open record
- preserve candidate counter-evidence
- summarize evidence at closure
- document insufficient evidence
- distinguish prediction support from model failure

Reports may not:

- modify the original prediction
- silently change the evaluation window
- redefine the outcome threshold after results are known
- close a prediction before its governing criteria are met
- treat one favorable event as decisive when repeated evidence is required

Candidate evidence remains provisional until evaluated under the applicable methodology.

Current rules for records 041–044 are documented in:

[`../methodology/open_prediction_evaluation_plan_041_044.md`](../methodology/open_prediction_evaluation_plan_041_044.md)

---

## Relationship to Phase Interpretation

Reports may describe characteristics associated with a possible later operating state.

Examples include:

- reduced operator overhead
- greater portability
- spare attentional capacity
- automatic correction
- recovery-compatible capacity
- cross-context execution

Such observations should remain labeled as:

- candidate characteristics
- emerging evidence
- provisional signals

They do not independently establish a phase transition.

Formal phase declarations must follow:

[`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)

---

## Evidence Hierarchy

When report content conflicts with another record, the preferred hierarchy is:

1. verified primary source artifact
2. direct provider or device export
3. contemporaneous structured transcription
4. contemporaneous collection note
5. weekly report
6. later synthesis grounded in preserved evidence
7. unsupported memory

A report may organize evidence from lower layers.

It may not elevate unsupported memory above preserved evidence.

---

## Inclusion Criteria

The following belong in this directory:

- active weekly observation reports
- closed weekly reports
- comparative biological or performance reports
- snapshot synthesis reports
- perturbation-response reports
- phase closeout reports
- structured longitudinal synthesis
- model-error evidence summaries grounded in preserved records

---

## Exclusion Criteria

The following generally do not belong in this directory:

- raw PDFs
- source images
- device exports
- unstructured screenshots
- canonical CSV datasets
- checksum manifests
- active protocol definitions
- model-error source records
- unsupported speculation
- generalized coaching guidance
- forward projections outside the registered prediction layer
- promotional or performance-display content

Source artifacts belong in `/snapshots` or another governed source location.

Canonical structured data belong in `/data`.

Protocols belong in `/protocols`.

Prediction records belong in `/data/model_error`.

---

## Reporting Constraints

All reports must:

- remain grounded in preserved evidence
- distinguish observation from interpretation
- distinguish direct values from derived values
- maintain numerical consistency
- preserve relevant context
- disclose material missingness
- identify meaningful comparability limitations
- avoid causal certainty unsupported by the design
- avoid selective omission of unfavorable valid evidence
- align with current governance and methodology
- preserve the open status of unresolved predictions
- avoid unregistered forward claims

Retrospective reports must additionally:

- reflect a closed or sufficiently mature observation window
- identify the evidence used
- avoid rewriting prior observations
- preserve uncertainty where evidence remains incomplete
- distinguish candidate characteristics from confirmed transitions

---

## Correction Rules

Reports are historical records, but they are not exempt from source-backed correction.

Permitted corrections may include:

- transcription errors
- incorrect dates
- mislabeled metrics
- broken references
- inaccurate source attribution
- factual inconsistencies confirmed by stronger evidence

A correction must:

- be narrow
- use identifiable source evidence
- preserve the prior state through Git history
- avoid changing unrelated interpretation
- be documented when material
- trigger review of dependent summaries

Outcome-driven narrative revision is prohibited.

A later interpretation may add context without pretending that the new context was known during the original window.

---

## Environmental-Control Language

Reports should not describe ordinary-life observation as fully controlled.

Preferred language includes:

- defined protocol constraints
- stabilized inputs
- ordinary-life conditions
- incomplete environmental control
- documented perturbation
- reduced or altered access
- contextual variability

Terms such as `controlled conditions` should be used only when the relevant controls are explicitly defined.

---

## Dashboards and Derived Views

Dashboards and executive summaries provide compressed views of the archive.

The hierarchy is:

```text
Source Artifacts
→ Structured Data
→ Contemporaneous Notes
→ Reports
→ Dashboards
```

Dashboards should remain traceable to the underlying report and data layers.

A dashboard must not introduce a stronger claim than the report it summarizes.

---

## Purpose

The reports layer exists to:

- preserve weekly and cross-period system behavior
- integrate quantitative and contextual evidence
- document recovery and execution under ordinary-life variability
- support phase and model-error evaluation
- record uncertainty
- provide an interpretable bridge between source artifacts and higher-level archive state

Reports describe the system across time.

They do not define reality independently of the evidence beneath them.

---

## Archive Principle

Source evidence preserves what was captured.  
Structured data organize what was recorded.  
Reports interpret what accumulated.  
Predictions test the model.  
Governance constrains every layer.

Nothing supersedes a verified source without documented evidence and a traceable correction.

---

## Related Documents

- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`../SYSTEM_OVERVIEW.md`](../SYSTEM_OVERVIEW.md)
- [`../DATASET_OVERVIEW.md`](../DATASET_OVERVIEW.md)
- [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)
- [`../methodology/data-collection.md`](../methodology/data-collection.md)
- [`../methodology/prediction_evaluation.md`](../methodology/prediction_evaluation.md)
- [`../methodology/open_prediction_evaluation_plan_041_044.md`](../methodology/open_prediction_evaluation_plan_041_044.md)
- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)

---

## Version Note

This document was aligned on 2026-07-15 with the archive’s current:

- active and retrospective report distinction
- source-backed correction rules
- registered prediction layer
- candidate-evidence handling
- incomplete environmental-control boundary
- phase-declaration governance
- structured and narrative evidence hierarchy

The revision does not alter any weekly observation, source value, prediction record, closed outcome, protocol exposure, or phase status.
