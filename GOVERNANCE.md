# Governance Protocol

The Daniel Longitudinal Study is maintained as a structured longitudinal archival system.

This repository documents one human system across time under:

- defined protocol constraints
- repeated measurement
- governed interpretation
- incomplete real-world environmental control

It is not a marketing vehicle.  
It is not a coaching funnel.  
It is not a social narrative.  
It is not a clinical trial or generalized intervention program.

All entries are governed by the constraints below.

---

## Core Principles

1. Durability over performance.
2. Repeatability over peak output.
3. Normal operating conditions over staged presentation.
4. Longitudinal trend over isolated result.
5. Archival integrity over aesthetic impression.
6. Traceable correction over silent preservation of known error.
7. Model calibration over prediction defensiveness.
8. Explicit uncertainty over forced closure.
9. Evidence-earned progression over proof-seeking intervention.
10. Source artifacts over later narrative.

---

## Environmental-Control Boundary

The archive does not claim laboratory-grade environmental control.

Observation occurs under ordinary-life conditions that may include:

- travel
- schedule variation
- household workload
- social and administrative demands
- altered sleep environment
- equipment or scale-access limitations
- hydration and sodium variation
- meal and GI timing
- illness or transient environmental exposure
- incomplete measurement of external variables

Protocol inputs may be stabilized where practical, but stabilized inputs must not be described as complete environmental control.

Known deviations that materially affect interpretation should be recorded.

The absence of a documented deviation does not establish that all external variables were controlled.

---

## Capture Constraints

Biometric and performance captures should reflect normal operating conditions whenever practical.

The following are prohibited when performed solely to improve presentation or force an outcome:

- dehydration before a scan or measurement
- sodium manipulation for cosmetic effect
- artificial glycogen depletion
- acute stimulant escalation
- unusual fasting introduced only for testing
- short-term training manipulation intended to alter a snapshot
- intentional protocol shift designed to produce a favorable result
- selective omission of an unfavorable but valid capture

If collection conditions differ materially from prior comparison points, the deviation must be documented.

Relevant collection context may include:

- sample or testing date
- fasting state
- hydration status
- recent training
- meal timing
- sleep
- illness
- travel
- medication or supplementation changes
- testing provider
- device or software version
- known protocol deviations

Normal preparation required by a testing provider does not constitute manipulation when it is applied consistently and documented.

---

## Source and Evidence Hierarchy

When records conflict, interpretation should generally prioritize:

1. verified primary source artifacts
2. direct provider or device exports
3. contemporaneous structured transcription
4. contemporaneous collection notes
5. weekly retrospective reports
6. later synthesis grounded in preserved evidence
7. unsupported memory

A later narrative cannot create an event or measurement that was not otherwise recorded.

Structured data remain subordinate to the verified source artifact when a source-backed discrepancy is established.

Detailed collection and correction procedures are defined in:

[`methodology/data-collection.md`](./methodology/data-collection.md)

---

## Data Integrity

The following are prohibited:

- silent alteration of recorded values
- outcome-driven rewriting
- deletion of unfavorable valid outcomes
- selective reporting intended to distort the longitudinal record
- unsupported replacement of suspicious values
- manipulation of measurement definitions after an outcome is known
- retrospective revision of a prediction to better match its result
- backfilling values from memory without clear labeling and provenance
- presenting inferred values as directly observed measurements

The archive permits traceable correction when source evidence confirms that a recorded value is inaccurate.

A source-backed correction must:

- identify the affected file, date, and field
- use the strongest available source evidence
- change only the affected value or representation
- preserve unrelated valid data
- preserve the prior state through Git history
- document the correction in the applicable data-quality note
- document material corrections in `CHANGELOG.md`
- rerun relevant validation
- review derived outputs that may depend on the corrected value

Correction is archive maintenance.

It is not a new biological observation and must not be used to conceal an unfavorable result.

Unresolved values remain unresolved rather than being reconstructed for completeness.

Known data-quality questions are recorded in:

[`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

---

## Structural and Methodological Changes

Material changes to collection, schema, measurement, interpretation, or validation methodology require documentation.

Depending on scope, updates may be required in:

- [`VERSIONING.md`](./VERSIONING.md)
- [`CHANGELOG.md`](./CHANGELOG.md)
- [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)
- [`MEASUREMENT_SOURCES.md`](./MEASUREMENT_SOURCES.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- applicable audit records

A structural change must not be represented as though it had governed earlier data unless the historical record supports that claim.

New rules may govern future collection without retroactively redefining prior observation conditions.

---

## Interpretation Separation

Source artifacts, structured data, contemporaneous observations, and retrospective interpretation occupy separate layers.

### Source Artifacts

Snapshots preserve provider reports, testing outputs, images, and other primary evidence.

### Structured Data

Datasets preserve machine-readable values derived from governed sources.

### Collection Notes

Contemporaneous notes preserve relevant events, context, and subjective observations not adequately represented by formal devices or reports.

### Reports

Reports provide bounded retrospective interpretation after evidence accumulates.

### Model-Error Layer

The model-error layer preserves formally registered predictions and compares them with later observed outcomes.

Language may provide context and clarity, but it cannot override, distort, or replace observable evidence.

Biological interpretation remains artifact-bound and retrospective.

---

## Prediction Governance

Forward predictions are permitted only within the formally governed model-error layer.

A valid forward prediction must be:

- registered before the relevant outcome is known
- specific enough to evaluate
- attached to a defined observation window or state
- preserved without hindsight revision
- evaluated only after sufficient evidence exists
- allowed to remain open when evidence is insufficient
- retained when wrong as model-correction evidence

Candidate evidence may be recorded in weekly reports or collection notes during an open window.

Candidate evidence must not automatically:

- modify the prediction
- determine its outcome
- trigger early closure
- justify a phase declaration
- justify proof-seeking protocol changes

Evaluation rules for the current open prediction block are documented in:

[`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)

Prediction accuracy is not treated as proof of certainty.

Prediction error is preserved as evidence about the model.

---

## Protocol Governance

Protocol changes must remain separate from the desire to produce a particular result.

Substantive changes may include recurring alterations to:

- training load
- volume
- density
- frequency
- aerobic duration or intensity
- movement selection
- nutrition architecture
- fasting structure
- supplementation
- recovery interventions
- testing preparation

A substantive progression or protocol modification should require:

- repeated evidence rather than one favorable session
- corroboration across more than one evidence layer
- recovery compatibility
- a documented rationale
- bounded implementation
- reversibility where practical
- absence of a proof-seeking motive

The following do not automatically constitute substantive protocol changes:

- technique refinement
- ordinary warm-up or mobility selection
- one-time schedule adjustment
- externally constrained missed training
- household or recreational activity
- repository maintenance
- source-backed data correction
- conservative response to an acute safety issue

Repository cleanup must not be misclassified as biological protocol progression.

Improved capacity does not itself create an obligation to increase workload.

---

## Phase Governance

Phase language is retrospective and evidence-earned.

A phase transition must not be declared solely from:

- one favorable measurement
- one high-quality session
- subjective confidence
- elapsed time
- prediction accuracy
- a single candidate observation
- a temporary reduction in effort
- an isolated increase in available capacity

Phase declarations must follow:

[`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)

Open prediction outcomes may contribute evidence toward a phase decision but cannot independently declare one.

Until formal criteria are met, observations suggesting a later phase remain candidate characteristics rather than confirmed state transitions.

---

## Missingness and Uncertainty

Missing information must remain visible.

The archive must not use zero, copied values, or retrospective estimation to conceal missingness.

When evidence is incomplete:

- the field may remain missing
- the record may remain open
- the analysis may be restricted
- the limitation must be disclosed
- no favorable or unfavorable outcome should be forced

Uncertainty is part of the archive.

It is not a defect to be removed through unsupported inference.

---

## Public Archive Boundary

Not every privately retained source must be published.

The public archive may contain:

- primary source artifacts
- redacted public derivatives
- structured values transcribed from privately retained originals
- reports grounded in verified but nonpublic sources
- contextual evidence sufficient for auditability

Publication decisions should balance:

- evidentiary usefulness
- source traceability
- data minimization
- archive integrity
- long-term maintainability

Public omission does not remove the requirement for source verification.

---

## Update Cadence

- Snapshots are logged after confirmed capture and source verification.
- Structured datasets are updated after governed entry or source-backed correction.
- Weekly reports are interpreted at closeout.
- Candidate evidence may be added during an active weekly window when clearly labeled.
- `LATEST.md` is updated after weekly rollover or material state change.
- `CHANGELOG.md` records notable structural, dataset, methodology, and archive-integrity changes.
- Audits verify continuity without rewriting the evidence being audited.
- Release metadata changes only during an intentional versioned release or documented correction cycle.

Cadence serves continuity.

It must not create urgency-driven errors.

---

## Scope Boundary

This repository does not:

- provide medical advice
- recommend generalized interventions
- establish clinical efficacy
- establish population-level causality
- guarantee outcomes
- claim laboratory-grade control
- optimize for external approval
- treat consumer-device outputs as definitive clinical measures
- convert one subject’s response into universal guidance
- treat prediction accuracy as proof of authority

It documents one longitudinal system under defined constraints and incomplete environmental control.

---

## Permanence Standard

This archive is intended to remain readable, inspectable, and structurally coherent ten years from now.

Long-term coherence requires:

- stable paths where practical
- documented corrections
- visible uncertainty
- preserved historical context
- explicit active versus historical protocol status
- versioned methodology
- traceable source relationships
- avoidance of unnecessary duplication
- restrained use of transient platform-specific conventions

---

## Artifact Integrity

Binary or non-text snapshot artifacts should be accompanied by SHA-256 verification when appropriate.

Checksum manifests must:

- identify the intended artifact
- contain the correct SHA-256 digest
- be updated atomically when a governed artifact replacement occurs
- remain consistent with the public snapshot state

Checksums verify file identity.

They do not establish measurement validity, source quality, or interpretive correctness.

---

## Enforcement Standard

When a governance conflict is identified:

1. preserve the current state
2. identify the governing source
3. distinguish data error from interpretive disagreement
4. avoid unsupported correction
5. document the issue
6. correct only when evidence supports correction
7. rerun applicable validation
8. preserve the audit trail

The archive should favor narrow, traceable remediation over broad historical rewriting.

---

## Related Documents

- [`STRUCTURAL_PRINCIPLES.md`](./STRUCTURAL_PRINCIPLES.md)
- [`PHASE_DECLARATION_CRITERIA.md`](./PHASE_DECLARATION_CRITERIA.md)
- [`RISK_MANAGEMENT.md`](./RISK_MANAGEMENT.md)
- [`VERSIONING.md`](./VERSIONING.md)
- [`DATASET_OVERVIEW.md`](./DATASET_OVERVIEW.md)
- [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)
- [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)
- [`methodology/data-collection.md`](./methodology/data-collection.md)
- [`methodology/open_prediction_evaluation_plan_041_044.md`](./methodology/open_prediction_evaluation_plan_041_044.md)
- [`CHANGELOG.md`](./CHANGELOG.md)

---

## Version Note

This governance document was aligned on 2026-07-15 with the archive’s current:

- source-backed correction procedure
- incomplete environmental-control boundary
- registered prediction layer
- candidate-evidence handling
- protocol-governance rules
- retrospective phase-declaration standard

The revision does not alter any existing source value, prediction record, closed outcome, protocol exposure, or phase status.
