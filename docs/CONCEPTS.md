# Concepts

This document provides plain-language definitions for recurring concepts used throughout the Daniel Longitudinal Study archive.

Its purpose is to:

- improve external legibility
- reduce terminology drift
- distinguish observation from interpretation
- distinguish evidence states from declared system states
- preserve consistent use of phase, prediction, source, and correction language

This glossary explains terms.

It does not independently:

- declare a phase
- score a prediction
- correct a dataset
- establish causality
- authorize protocol progression

Canonical phase architecture is defined in:

[`../PHASE_MAP.md`](../PHASE_MAP.md)

State-transition history is recorded in:

[`../STATE_TRANSITIONS.md`](../STATE_TRANSITIONS.md)

---

# Evidence and Archive Concepts

## Observation

An observation is something recorded about the subject, environment, protocol, or measurement system.

Examples include:

- bodyweight
- wearable values
- laboratory results
- training completion
- pain
- GI state
- movement quality
- sleep description
- travel
- equipment limitations

An observation may be:

- objective
- provider generated
- device generated
- manually transcribed
- subjective
- narrative

An observation does not automatically establish interpretation.

---

## Telemetry

Telemetry is information collected from measurements, observations, and recorded outcomes.

Examples include:

- sleep duration
- HRV
- heart rate
- body composition
- training exposure
- bodyweight
- laboratory values
- subjective recovery
- performance outcomes

Telemetry supplies evidence to the archive.

It does not independently establish:

- causality
- clinical meaning
- phase status
- protocol success
- prediction success

---

## Artifact

An artifact is a preserved file or record that supports an observation.

Examples include:

- provider PDF
- laboratory report
- DEXA report
- Bod Pod image
- wearable CSV export
- screenshot
- weekly report
- audit file
- checksum manifest
- structured dataset

Artifacts vary in source strength and interpretation value.

A source artifact should not be confused with a retrospective summary derived from it.

---

## Artifact-First

Artifact-first means preserving evidence before final interpretation.

The sequence is:

```text
Observation
    ↓
Artifact preservation
    ↓
Source and quality review
    ↓
Interpretation
```

Artifact-first practice reduces the risk that later interpretation changes what is remembered or recorded.

It does not mean that every artifact is error-free.

---

## Collection Layer

The collection layer captures observations near the time they occur.

Examples include:

- wearable data
- bodyweight
- biomarker results
- training notes
- recovery observations
- morning reports
- source screenshots
- provider exports

The collection layer should preserve:

- timing
- source
- units
- uncertainty
- missingness
- contemporaneous context

Collection should remain separate from retrospective interpretation when practical.

---

## Archive Layer

The archive layer organizes evidence into durable records.

Examples include:

- canonical datasets
- weekly reports
- audit reports
- model-error records
- source-export packages
- snapshot directories
- longitudinal summaries
- governance documents

The archive layer preserves both individual observations and patterns across time.

It should not silently transform uncertainty into certainty.

---

## Interpretation Layer

The interpretation layer evaluates what preserved observations may mean.

Examples include:

- weekly retrospective assessment
- snapshot comparison
- phase review
- model-error scoring
- perturbation analysis
- trajectory assessment

Interpretation must remain proportional to:

- source quality
- metric meaning
- measurement conditions
- missingness
- comparability
- contradictory evidence

Interpretation does not alter the underlying source record.

---

# Source and Dataset Concepts

## Source State

A source state is the value or record supplied by a particular evidence pathway at a particular time.

Examples include:

- a value visible in the RingConn application on the observation date
- a later RingConn account export
- a manually transcribed value
- a provider PDF
- a sanitized public derivative

Two source states associated with the same date may differ without either being automatically discarded.

Possible causes include:

- provider recalculation
- software changes
- rounding
- date assignment
- transcription
- aggregation differences

Source states should not be forced into false agreement.

---

## Provider Source Artifact

A provider source artifact is a file created by an external provider, laboratory, facility, or device ecosystem.

Examples include:

- laboratory PDF
- DEXA report
- Bod Pod report
- TruDiagnostic report
- RingConn CSV export

It is generally stronger evidence than unsupported memory or retrospective reconstruction.

It may still contain:

- provider error
- algorithmic estimation
- unclear field definitions
- privacy-sensitive administrative information

---

## Direct Provider Export

A direct provider export is a structured file generated through a provider or device account.

Examples include:

- RingConn sleep export
- RingConn activity export
- RingConn vital-sign export

A direct export preserves the provider’s database state at the time of export.

It may not reproduce values displayed contemporaneously in an earlier application view.

A later direct export does not automatically overwrite earlier curated records.

---

## Source-Preserved

Source-preserved means a provider or device file is retained without analytical modification.

Permitted associated actions may include:

- public filename normalization
- directory placement
- checksum registration
- provenance documentation
- Git controls preventing byte conversion

Source-preserved does not mean:

- clinically validated
- semantically complete
- suitable for immediate canonical integration
- free from provider anomalies

---

## Byte-Preserved

Byte-preserved means the archived file contains the same bytes as the registered source file.

This can be tested through:

- file size
- cryptographic checksum
- direct binary comparison

Byte preservation protects source integrity.

It does not prove that the source measurement itself is correct.

---

## Curated Dataset

A curated dataset is a governed structured table assembled for longitudinal use.

It may contain:

- manually transcribed observations
- archive-defined field names
- confidence labels
- subjective context
- correction notes
- governed date assignments
- fields from more than one evidence mode

A curated dataset is not the same as a raw provider export.

Example:

```text
data/sleep_longitudinal_v1.csv
```

---

## Canonical Dataset

A canonical dataset is the archive-designated structured record for a defined use.

Canonical means:

- governed
- versioned
- schema-defined
- used consistently for its intended analytical purpose

Canonical does not mean:

- perfect
- final
- free from documented quality restrictions
- automatically superior to every source artifact

A field-specific quality issue may exist without invalidating the entire canonical dataset.

---

## Derived Dataset

A derived dataset is produced from other preserved data through an explicit procedure.

Examples include:

- weekly averages
- normalized provider fields
- comparison tables
- model-error calculations
- UDI trackers

A derived dataset should document:

- input sources
- formulas
- transformation rules
- missingness handling
- version
- provenance

Derived values must not be represented as direct measurements.

---

## Normalization

Normalization is the transformation of provider- or source-specific fields into a stable archive-defined structure.

Normalization may include:

- field renaming
- date parsing
- unit standardization
- source-row tracking
- schema alignment

Normalization does not mean changing values to appear more typical.

Within this archive, wearable normalization is currently deferred until a defined analytical need justifies it.

Source exports remain preserved regardless of whether normalization is later performed.

---

## Source Precedence

Source precedence is the rule used to determine which evidence should govern a specific question or correction.

The default hierarchy favors:

1. verified provider or device artifact
2. direct provider export
3. contemporaneous screenshot
4. contemporaneous structured transcription
5. contemporaneous operator note
6. retrospective synthesis
7. unsupported memory

This hierarchy is not automatic.

Correction also requires semantic equivalence.

A later export may be stronger as provider evidence but unsuitable for overwriting a contemporaneous metric with a different definition.

---

## Source-Backed Correction

A source-backed correction is a narrow change supported by stronger, semantically equivalent evidence.

A correction should require:

- affected field identified
- applicable source identified
- compatible units
- compatible date meaning
- documented correction logic
- review of dependent values
- traceable commit history

A correction is archive maintenance.

It is not a new biological observation.

---

## Silent Correction

A silent correction changes a value without preserving:

- the prior state
- supporting evidence
- reasoning
- correction history

Silent correction is prohibited.

---

## Reconciliation

Reconciliation is the comparison of multiple source states to determine:

- whether they refer to the same metric
- whether a difference is meaningful
- whether correction is justified
- whether both values should remain preserved

Reconciliation does not require two sources to agree.

An unresolved difference may remain an appropriate outcome.

---

## Missingness

Missingness means that a value or source row is absent or unavailable.

Missing does not automatically mean:

- zero
- no event
- no device wear
- no sleep
- no activity
- normal
- failed collection

Missing values should remain missing unless source evidence supports a specific classification.

---

## Analytical Restriction

An analytical restriction limits how a field, row, or source may be used without deleting it.

Examples include:

- excluding a provider anomaly from stage-percentage analysis
- avoiding quantitative use of a suspected transcription field
- prohibiting timezone analysis when offsets are unknown
- retaining a row for continuity while restricting one affected field

An analytical restriction narrows interpretation.

It does not necessarily invalidate the source or complete record.

---

# Prediction and Calibration Concepts

## Prediction

A prediction is a prospectively recorded statement about a future state or trajectory.

A governed prediction should define:

- registration date
- observation window
- expected state or direction
- scoring conditions
- admissible evidence
- closure requirements

A retrospective explanation is not a prediction.

---

## Model Error

A model error is a documented difference between what was expected and what occurred.

Model error is not treated as personal failure.

It is evidence about the limitations of the current internal model.

A model-error record may identify:

- direction error
- magnitude error
- timing error
- state error
- trajectory error
- confidence error

The purpose is model correction.

---

## Prediction Auditing

Prediction auditing is the process of comparing a registered prediction with later evidence.

The audit asks:

- What was predicted?
- What occurred?
- Was the outcome inside the defined window?
- Was the evidence admissible?
- How large was the difference?
- What should change in the model?

The objective is calibration rather than self-validation.

---

## Prediction Closure

Prediction closure occurs after:

- the observation window ends
- required evidence is available
- the prediction is compared with the outcome
- scoring rules are applied
- limitations are documented

An open prediction must not be scored early merely because favorable or unfavorable evidence appears.

---

## Candidate Evidence

Candidate evidence is an observation that may later support a prediction outcome, phase review, or transition assessment.

Candidate evidence:

- may be recorded contemporaneously
- may recur naturally
- remains provisional
- does not independently close a prediction
- should not be forced for proof

Example:

A divided-attention pull-up observation may be candidate evidence for reduced operator overhead without independently closing the relevant prediction.

---

## Admissible Evidence

Admissible evidence is evidence allowed under the preregistered evaluation rule.

Admissibility may depend on:

- source
- timing
- repetition
- measurement method
- collection conditions
- independence from outcome-directed behavior

Evidence may be interesting without being admissible for formal scoring.

---

## Concordance

Concordance is the degree of agreement between a prediction and an observed outcome.

The archive may distinguish:

- state concordance
- trajectory concordance
- directional concordance
- magnitude concordance

Higher concordance suggests the model described the observed outcome more accurately.

Lower concordance indicates a need for review or revision.

Concordance is not proof of causality.

---

## UDI

UDI means **Uncertainty Delta Index**.

UDI evaluates how prediction uncertainty and observed error behave across governed prediction–outcome records.

Its purpose is not to eliminate uncertainty.

Its purpose is to quantify whether the predictive model is becoming:

- better calibrated
- more directionally accurate
- more appropriately confident
- more useful across repeated cycles

UDI should be interpreted only under its registered eligibility and calculation rules.

---

## Calibration

Calibration describes how closely predicted confidence and expected outcomes match reality over time.

A well-calibrated model:

- is not always correct
- represents uncertainty honestly
- avoids excessive confidence
- improves after error review
- distinguishes strong from weak evidence

Calibration is more important than maintaining a high apparent success rate.

---

## Model Correction

Model correction is an explicit update to the internal or documented understanding after prediction error, source review, or accumulated evidence.

A model correction may change:

- future prediction thresholds
- expected recovery behavior
- interpretation of wearable signals
- phase criteria
- operating rules
- confidence

It should not rewrite the original prediction.

---

# Phase and State Concepts

## Phase

A phase is a canonical operational state defined by a primary system objective and constraint environment.

Current canonical phases include:

- Phase 0 — Baseline Reconstruction
- Phase 1 — Firmware Installation and Stabilization
- Phase 2 — Load Integration
- Phase 3 — External Capability Demonstration, reserved

A phase is not a motivational label or reward.

---

## Operating Substate

An operating substate describes how the active phase is currently expressed.

Examples within Phase 2 include:

- entry
- reintegration
- consolidation
- lock-in observation

An operating substate:

- remains inside the canonical phase
- may change without a phase transition
- may recur
- does not automatically authorize progression

---

## Candidate Characteristic

A candidate characteristic is an observation resembling a possible future substate or transition criterion.

Examples include:

- ambient execution
- automatic mechanics
- divided-attention control
- reduced operator overhead
- portability
- stable reintegration
- voluntary tempo control

A candidate characteristic is evidence to preserve, not a state to declare.

---

## Transition Evidence

Transition evidence is accumulated evidence relevant to a possible formal state change.

It may include:

- repeated protocol continuity
- stable recovery
- preserved mechanics
- cross-context performance
- portability
- biological snapshot support
- model-error outcomes
- governance preservation

One observation is rarely sufficient.

Transition evidence must be reviewed as a pattern.

---

## Phase Transition

A phase transition is a retrospectively declared movement from one canonical phase to another.

A phase transition requires:

- accumulated evidence
- closed observation window
- review of contradictory evidence
- satisfaction of declaration criteria
- explicit documentation

A phase transition is not created by:

- one favorable workout
- one biomarker result
- increased enthusiasm
- an aspirational plan
- candidate terminology

---

## Retrospective Declaration

A retrospective declaration formally records a phase or recognized substate only after the supporting evidence window has been reviewed.

The declaration should identify:

- prior state
- declared state
- evidence window
- supporting evidence
- limitations
- contradictory evidence
- operational consequence

The declaration date may occur after the biological or behavioral pattern began.

---

## Historical Alias

A historical alias is earlier terminology retained in existing reports.

Examples include:

- System Awakening
- Repair, Purification, Stability
- Aerobic Firmware Installation
- Lock-In Confirmation
- Phase 2C

Historical aliases should be interpreted through the current canonical hierarchy.

Historical reports should not be rewritten solely to standardize wording.

---

## Phase 2C

Phase 2C is historical shorthand for consolidation or lock-in observation within Phase 2.

It is not a separate canonical phase.

---

## Phase 2D-Type Characteristic

A Phase 2D-type characteristic is an observation resembling a possible future Phase 2D criterion.

Examples may include:

- trait-like execution
- automatic bar contact
- divided-attention movement control
- low-friction portability
- reduced need for conscious correction

The phrase does not mean Phase 2D has been declared.

---

## Phase 2D

Phase 2D is a possible retrospectively declared Phase 2 substate representing durable, portable, low-overhead capacity.

Current status:

```text
Undeclared
```

Phase 2D-type evidence may accumulate without changing the current phase or protocol.

---

## Reserved Phase

A reserved phase is a future structural category preserved in the architecture but not active.

Phase 3 is reserved.

Reserved does not mean:

- expected
- scheduled
- guaranteed
- earned by favorable results

---

# Training and Adaptation Concepts

## B1

B1 is the archive’s primary aerobic anchor.

Current expression generally includes:

- incline treadmill walking
- controlled speed
- nasal breathing
- repeatable low-intensity exposure
- fasted morning execution when practical

B1 is treated as a stable operating component rather than a performance test.

---

## Load Integration

Load Integration is the structured addition of mechanical loading while preserving the aerobic and recovery platform.

Current examples include:

- trap-bar work
- pull-ups
- push-ups
- dead hangs
- mobility

The objective is not unrestricted workload expansion.

It is stable integration without recovery degradation.

---

## Ambient Execution

Ambient execution describes a session or movement that occurs with low conscious friction.

Possible features include:

- easy initiation
- automatic setup
- familiar mechanics
- low perceived operator demand
- reduced need to mentally rehearse the session

Ambient execution is a subjective and functional observation.

It is not identical to low physiological load.

---

## Trait-Like Execution

Trait-like execution describes capacity that appears increasingly stable and readily available across repeated observations.

It suggests the behavior may be becoming an installed characteristic rather than a temporary favorable state.

The phrase remains observational unless supported by repeated cross-context evidence.

---

## Operator Overhead

Operator overhead is the conscious effort required to initiate, regulate, remember, or complete a protocol.

Examples include:

- mentally negotiating whether to train
- repeatedly checking technique
- needing extensive preparation
- consciously indexing every set
- using substantial attention to maintain ordinary execution

Reduced operator overhead may indicate increasing integration.

It should not be confused with reduced physiological effort.

---

## Movement Optionality

Movement optionality is the ability to vary execution without losing control.

Examples include:

- tempo changes
- pauses
- positional holds
- divided-attention demonstration
- altered equipment context

Optionality is different from mandatory progression.

A capability may be available without being converted into required workload.

---

## Portability

Portability is the ability of a protocol or capability to remain available across changes in:

- schedule
- environment
- equipment
- travel
- social context
- sequence of activities

Portability requires more than success in one familiar setting.

---

## Reintegration

Reintegration is the return to standard protocol execution after interruption, travel, illness, or altered environment.

A low-friction reintegration may include:

- no graded re-entry
- no compensatory workload
- preserved mechanics
- stable recovery
- rapid return to ordinary operation

Reintegration is an operating condition within a phase, not necessarily a transition.

---

## Recovery Floor

Recovery floor describes the lowest functional state reached during disruption.

Improvement may appear as:

- a higher minimum state
- less performance degradation
- faster return to baseline
- reduced intervention need
- preserved ordinary function

Recovery floor is different from peak recovery.

---

## Spare Capacity

Spare capacity is capability available beyond the workload currently required by the protocol.

Spare capacity may appear as:

- optional recreational activity
- additional movement control
- reduced perceived effort
- preserved performance under mild perturbation

Spare capacity should not automatically become required workload.

---

## Protocol Governance

Protocol governance is the set of rules preventing reactive, impulsive, or outcome-directed changes to physical execution.

Examples include:

- no compensation after missed sessions
- no progression merely because a session felt easy
- no forcing candidate evidence
- no changing behavior to improve a scheduled measurement
- no premature phase declaration

Governance protects interpretability.

---

## Protocol Progression

Protocol progression is a deliberate increase in:

- load
- volume
- density
- duration
- complexity
- novelty
- performance demand

Progression should be distinguished from spontaneous expression of existing capacity.

A tempo variation or optional recreational activity does not automatically constitute formal progression.

---

# Context and Perturbation Concepts

## Perturbation

A perturbation is a change in ordinary operating conditions that may test system stability.

Examples include:

- travel
- poor sleep
- schedule disruption
- environmental heat
- illness
- social activity
- equipment loss
- unusual workload
- dietary variation

Perturbations may be planned or unplanned.

They are not automatically experiments.

---

## Naturalistic Perturbation

A naturalistic perturbation occurs through ordinary life rather than deliberate experimental design.

Examples include:

- travel
- family obligations
- altered gym access
- social events
- yard work

Naturalistic perturbations can reveal portability and recovery behavior while preserving real-world relevance.

They provide limited causal control.

---

## Controlled Exposure

A controlled exposure is a deliberately bounded protocol input.

Examples include:

- standard B1
- standard Load Integration
- a defined testing condition
- a preregistered collection procedure

Controlled does not mean every external variable is held constant.

---

## Representative State

Representative state is the ordinary operating condition the archive attempts to measure rather than an artificially optimized display.

Examples of avoiding artificial optimization include:

- no acute dehydration
- no unusual sodium manipulation
- no short-term glycogen strategy
- no outcome-directed training change

Representative state remains an objective, not a claim of perfect control.

---

# Privacy and Integrity Concepts

## Public Original

A public original is a source artifact published without substantive privacy modification.

It may be renamed and checksummed while remaining byte-identical.

---

## Filename-Normalized Source

A filename-normalized source is a byte-identical file whose public filename was changed to remove unnecessary personal or account-facing text.

The file contents remain unchanged.

---

## Sanitized Derivative

A sanitized derivative is a public artifact created from a verified private source after removing unnecessary administrative identifiers.

A sanitized derivative should preserve:

- measurements
- units
- dates
- reference intervals
- flags
- interpretation-relevant structure

It must be identified as a derivative rather than an untouched provider original.

---

## Controlled Distribution Remediation

Controlled distribution remediation means intentional public surfaces under project control were reviewed and corrected.

Examples may include:

- active branch
- maintained tags
- current repository ZIP
- Zenodo package

This status does not imply deletion from uncontrolled prior copies or provider-retained residual storage.

---

## Checksum

A checksum is a cryptographic digest used to verify file identity.

This archive primarily uses SHA-256.

A matching checksum confirms that file bytes match the registered artifact.

It does not independently establish:

- source validity
- clinical accuracy
- privacy completeness
- correct interpretation

---

## Integrity

Integrity means that evidence remains:

- identifiable
- traceable
- unaltered or transparently transformed
- correctly checksummed
- documented
- reviewable

Integrity is broader than file validity.

It includes procedural and interpretive discipline.

---

# Governance Principles

## No Inference as Observation

A calculated, estimated, or reconstructed value must not be presented as directly observed.

Inference must be labeled.

Missing values remain missing unless source evidence supports correction.

---

## No Outcome-Driven Rewriting

Outcome-driven rewriting changes earlier predictions, rules, or interpretations after seeing the result.

This is prohibited.

Later interpretation may correct the model while preserving the original record.

---

## No Forced Proof

No forced proof means a candidate capability should not be deliberately repeated merely to create confirming evidence unless a governed test is separately defined.

Natural recurrence is stronger evidence of integration than performance staged for validation.

---

## Evidence Proportionality

Evidence proportionality means conclusions should not exceed the strength, scope, or comparability of their supporting evidence.

Examples:

- one session does not establish a trait
- one biomarker does not establish causality
- a consumer wearable does not establish diagnosis
- one favorable snapshot does not establish permanent adaptation

---

## Governance Preservation

Governance preservation means the system continues following its rules even when:

- performance improves
- enthusiasm rises
- favorable measurements appear
- external attention increases
- the subject becomes impatient

Governance preservation is itself a meaningful archive outcome.

---

# Current Terminology State

As of 2026-07-25:

```text
Canonical phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D-type characteristics:
Candidate evidence only

Formal Phase 2D declaration:
None

Phase 3:
Reserved and inactive

Model Error records 041–044:
Open and unscored

Wearable architecture:
Periodic byte-preserved exports with optional future derivation

Canonical sleep:
Curated dataset preserved separately from later provider exports
```

---

# Related Documents

- [`../PHASE_MAP.md`](../PHASE_MAP.md)
- [`../STATE_TRANSITIONS.md`](../STATE_TRANSITIONS.md)
- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)
- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`../ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`../MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)
- [`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)
- [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)
- [`../methodology/data-collection.md`](../methodology/data-collection.md)
- [`../methodology/anonymization.md`](../methodology/anonymization.md)
- [`../methodology/open_prediction_evaluation_plan_041_044.md`](../methodology/open_prediction_evaluation_plan_041_044.md)

---

## Version Note

This glossary was expanded on 2026-07-25 to align archive terminology with the current phase hierarchy, source architecture, data-quality model, privacy governance, and prediction-calibration framework.

The revision adds definitions for:

- phase
- operating substate
- candidate characteristic
- transition evidence
- retrospective declaration
- historical alias
- Phase 2C
- Phase 2D-type characteristics
- source state
- curated and canonical datasets
- direct provider exports
- normalization
- reconciliation
- source-backed correction
- missingness
- analytical restriction
- admissible evidence
- prediction closure
- operator overhead
- movement optionality
- portability
- spare capacity
- perturbation
- sanitized derivatives
- controlled distribution remediation

The revision does not alter:

- any observation
- any biological measurement
- any prediction wording
- any prediction outcome
- any protocol exposure
- any phase declaration
