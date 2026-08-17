# Methodology — Directory Guide

This directory contains the core operating methodology for the Daniel Longitudinal Study.

These files define how evidence is:

- collected
- preserved
- classified
- sanitized
- corrected
- evaluated
- protected from outcome-driven reinterpretation

The methodology layer governs process.

It does not independently determine biological interpretation, declare a phase, score a prediction, or modify the physical protocol.

---

## Directory Role

The `/methodology` directory contains rules and preregistered plans that directly govern current archive operation.

This includes:

- source hierarchy
- transcription
- provenance
- missingness
- correction
- privacy handling
- prediction evaluation
- collection-condition control
- outcome-access boundaries
- active evaluation plans
- completed preregistered plans retained for provenance

The governing sequence is:

```text
Define the rule
      ↓
Collect under the rule
      ↓
Preserve the source
      ↓
Evaluate after sufficient evidence
      ↓
Interpret retrospectively
```

A later result must not silently rewrite an earlier methodology rule.

A completed preregistered plan should remain preserved after scoring so the original evaluation boundary remains inspectable.

---

# Current Methodology Files

## Data Collection

### [`data-collection.md`](data-collection.md)

Defines how observations enter the archive.

It governs:

- evidence hierarchy
- provider and device sources
- direct exports
- screenshots
- manual transcription
- units
- timing
- provenance
- missingness
- derivation
- source-backed correction
- reconciliation
- preservation of unresolved uncertainty

This file should be consulted before:

- adding a new structured dataset
- correcting a canonical value
- reconciling two source states
- transforming a provider export
- filling or classifying missing data

It prohibits:

- inference presented as observation
- silent correction
- unsupported interpolation
- correction from memory alone
- field substitution without semantic equivalence

---

## Privacy and Public Artifact Handling

### [`anonymization.md`](anonymization.md)

Defines public-artifact sanitization and privacy-remediation rules.

It governs:

- private originals
- public originals
- filename-normalized sources
- sanitized derivatives
- redacted derivatives
- hidden-text inspection
- metadata review
- administrative-identifier removal
- checksum renewal
- Git-history boundaries
- external-distribution review
- controlled-remediation status

This file should be consulted before publishing:

- laboratory reports
- provider PDFs
- screenshots
- wearable exports
- images
- structured account exports
- ZIP packages
- artifacts containing administrative identifiers

The subject’s public identity and chronological age are intentionally associated with the project.

Privacy review instead focuses on unnecessary administrative exposure such as:

- full date of birth
- address
- private contact information
- patient or specimen identifiers
- account identifiers
- signatures
- access tokens
- unrelated third-party information

Sanitization must preserve the biological or performance evidence required for interpretation.

---

## General Prediction Evaluation

### [`prediction_evaluation.md`](prediction_evaluation.md)

Defines the general method for evaluating registered predictions.

It governs:

- valid prediction structure
- observation windows
- admissible evidence
- closure requirements
- state and trajectory comparison
- error classification
- retention of incorrect predictions
- calibration and model correction

This file applies broadly across the model-error layer.

A prediction must not be:

- rewritten after registration
- closed before sufficient evidence exists
- scored from inadmissible evidence
- reframed to preserve apparent success
- removed because it was incorrect

Prediction evaluation is intended to improve calibration rather than maximize an apparent success rate.

---

## Active Evaluation Plan — Records 041–044

### [`open_prediction_evaluation_plan_041_044.md`](open_prediction_evaluation_plan_041_044.md)

This is the preregistered evaluation plan for Model Error records 041–044.

It defines:

- admissible evidence
- observation windows
- repetition requirements
- primary and supplemental endpoints
- missing-test handling
- discordance handling
- scoring protections
- known information at registration
- closure boundaries

Governed records:

- 041 — recovery capacity
- 042 — ambient-execution plateau
- 043 — August biological snapshot
- 044 — protocol governance

The plan was committed before the final outcome windows closed.

Its registered rules remain binding until formal evaluation.

A weekly report may preserve candidate evidence relevant to these records.

It may not independently:

- score them
- close them
- revise their predictions
- change their thresholds
- substitute a new primary endpoint

Records 045 and 046 do not amend this plan.

The 041–044 evaluation block remains preserved as originally registered.

---

## Completed Evaluation Plan — Record 045

### [`open_prediction_evaluation_plan_045.md`](open_prediction_evaluation_plan_045.md)

This is the preserved preregistered evaluation plan for Model Error record 045.

Record 045 was registered on:

```text
2026-08-12
```

Its domain is:

```text
autonomic_reconvergence
```

Its registered prediction was:

```text
partial_reconvergence
```

Its admissible scoring window was:

```text
2026-08-13 through 2026-08-16
```

The plan was created after retrospective closeout of Week 31 but before the admissible record 045 outcome window began.

The following observations were registration context only:

```text
2026-W31
2026-08-10
2026-08-11
2026-08-12
```

They explained why the prediction was generated.

They could not satisfy it.

August 17–18 biological and performance snapshot results were also excluded from record 045 scoring.

The plan defined:

- the W30 and W31 reference states
- fixed partial-reconvergence thresholds
- four-day aggregation rules
- functional-preservation requirements
- recovery-intervention boundaries
- failure classifications
- insufficient-evidence handling
- missing-data handling
- evidence hierarchy
- relationships to records 041–044
- protocol protections
- snapshot-result exclusion
- phase protections
- threshold immutability
- post-window scoring procedure

Registered favorable thresholds were:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

Support required:

```text
at least 3 of 4 autonomic thresholds met

AND

no multi-session functional regression

AND

no recovery-driven protocol reduction or intervention
```

At retrospective scoring after the fixed window closed:

```text
Daily HRV:
63.5 ms

Sleep HRV:
71.25 ms

Resting HR:
46.5 bpm

Sleeping HR:
51.75 bpm

Favorable thresholds:
4 of 4

Multi-session functional regression:
No

Recovery-driven protocol reduction or intervention:
No
```

Record 045 was therefore scored:

```text
supported
```

The 2026-08-16 Load Integration omission was testing-directed because DEXA and VO₂-max testing were scheduled for the following morning.

It was not recovery-driven and therefore did not trigger the record 045 recovery-driven protocol-change failure condition.

That classification is specific to record 045.

The same event remains separately relevant to records 043 and 044 because it represents a pre-snapshot testing-preparation deviation from the ordinary-training posture.

Record 045 is now closed.

Its methodology file remains preserved because it documents the rules that governed the prediction before the outcome was known.

Record 045 does not:

- replace record 041
- redefine recovery-capacity criteria
- score motor automaticity under record 042
- alter the Model Error 043 biological endpoint
- modify record 044 governance criteria
- establish complete recovery
- establish absence of accumulated training cost
- declare Phase 2D
- determine later unload/reload behavior

Later evidence must not reopen or extend record 045.

---

## Active Evaluation Plan — Record 046

### [`open_prediction_evaluation_plan_046.md`](open_prediction_evaluation_plan_046.md)

This is the separate preregistered evaluation plan for Model Error record 046.

Record 046 was registered on:

```text
2026-08-17
```

Its domain is:

```text
autonomic_unload_reload
```

Its registered prediction is:

```text
reconvergence_persists_after_unload_reload
```

Record 046 begins where the completed record 045 question ends.

Record 045 asked:

```text
Did partial autonomic reconvergence occur?
```

Record 046 asks:

```text
Does that reconvergence remain broadly preserved
after planned training withdrawal and reload?
```

The known exposure sequence at registration is:

```text
2026-08-16
B1 completed
Load Integration withheld before testing

2026-08-17
No B1
No Load Integration
DEXA and VO₂-max testing

2026-08-18
No B1
No Load Integration
Bod Pod testing

2026-08-19
Planned return to standard B1
Planned return to standard Load Integration
```

Because 2026-08-17 had already begun before record 046 registration:

```text
2026-08-17
```

is registration context only.

It cannot satisfy the prediction.

The plan preserves:

```text
2026-08-18
2026-08-19
```

as descriptive unload and re-entry kinetics.

The fixed primary scoring window is:

```text
2026-08-20 through 2026-08-23
```

Record 046 intentionally reuses the same favorable autonomic thresholds as record 045:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

This preserves direct comparability without recalibrating thresholds after the favorable record 045 outcome.

Support requires:

```text
at least 3 of 4 autonomic thresholds favorable
across the fixed 2026-08-20 through 2026-08-23 means

AND

no multi-session functional regression after reload

AND

no recovery-driven protocol reduction after normal training resumes
```

The plan explicitly allows a short-lived autonomic disturbance after the 2026-08-17 maximal VO₂ test.

Such an acute response may be documented.

It does not independently fail record 046.

The plan excludes the measured outcomes of:

- DEXA
- VO₂ max
- Bod Pod
- TruDiagnostic
- TruAge
- TruHealth
- other August biological-snapshot interpretation

Those outcomes are independently governed.

Record 046 does not:

- reopen record 045
- extend record 045
- rescore record 045
- change records 041–044
- alter the August snapshot biological endpoint
- create a new physical training protocol
- authorize an extended deload
- authorize a reload stress test
- declare Phase 2D

The record 046 evaluation plan remains active and prospective.

---

## Active Snapshot Collection Plan

### [`2026-08-snapshot-collection-plan.md`](2026-08-snapshot-collection-plan.md)

This is the preregistered collection plan for the August 17–18, 2026 biological and performance snapshot.

It governs:

- representative-state collection
- test schedule
- primary and supplemental domains
- fasting documentation
- hydration documentation
- recent-training documentation
- supplement and medication boundaries
- source-artifact expectations
- privacy review
- missing or delayed test handling
- invalid or rescheduled test handling
- discordant-result handling
- outcome-access boundaries
- post-collection workflow
- release and phase protections

The plan preserves:

- TruDiagnostic as the primary Model Error 043 domain
- May 2026 as the primary comparison baseline
- DEXA, VO₂ max, Bod Pod, bodyweight, recovery, and subjective state as supplemental evidence
- ordinary rather than snapshot-optimized behavior as the intended collection posture
- separation between collection and interpretation

The collection plan does not contain August results.

It does not:

- predict the result
- alter records 041–046
- change scoring rules
- authorize protocol progression
- declare Phase 2D
- create a release automatically
- determine the outcome of record 046
- reopen record 045

The 2026-08-16 Load Integration omission should remain documented as a factual collection-condition deviation rather than being removed from the record.

The plan itself should not be retrospectively rewritten to make that deviation appear preregistered.

The plan should otherwise remain unchanged unless a factual collection detail changes.

Any amendment should be:

- dated
- narrow
- factual
- committed before the affected result is interpreted when possible
- explicit about whether outcome access had already occurred

---

# Methodology Document Types

Files in this directory may serve different roles.

## Standing Methodology

Standing methodology defines rules intended to govern multiple observation cycles.

Examples:

- `data-collection.md`
- `anonymization.md`
- `prediction_evaluation.md`

Standing methodology should change only when:

- a genuine procedural gap is identified
- archive practice has materially evolved
- a rule creates ambiguity or excessive maintenance burden
- a new evidence type requires governance
- an audit identifies a repeatable weakness

A standing rule should not be changed merely because a current result is inconvenient.

---

## Preregistered Evaluation Plan

A preregistered evaluation plan applies standing methodology to a defined prediction block or outcome window.

Current or preserved examples:

- `open_prediction_evaluation_plan_041_044.md`
- `open_prediction_evaluation_plan_045.md`
- `open_prediction_evaluation_plan_046.md`

It should identify:

- applicable records
- registration date
- known evidence at registration
- unknown outcomes
- admissible evidence
- thresholds
- closure rules
- missingness handling
- discordance handling

Once outcome access begins, substantive scoring rules should remain fixed.

After scoring, the original preregistered plan should remain preserved for provenance.

Separate prediction blocks should remain in separate preregistration artifacts when their:

- registration dates differ
- evidence windows differ
- primary questions differ
- admissible evidence differs

The existence of a later evaluation plan must not silently rewrite an earlier one.

Record 046 therefore remains separate from record 045 even though both concern autonomic trajectory.

---

## Preregistered Collection Plan

A preregistered collection plan defines how a future measurement event will be captured.

Example:

- `2026-08-snapshot-collection-plan.md`

It should identify:

- collection window
- providers and domains
- preparation objectives
- ordinary-condition boundaries
- required context
- expected artifacts
- deviation handling
- post-collection workflow
- interpretation boundary

A collection plan governs capture.

It does not determine the result.

---

## Retrospective Methodology Note

A retrospective methodology note may explain:

- how an existing process behaved
- why a rule was changed
- what an audit discovered
- what future procedure should improve

A retrospective note must not be represented as though it had been preregistered.

When timing matters, the file should state:

- creation date
- evidence already known
- whether results had been viewed
- what remained unknown

---

## Historical or Completed Methodology

A historical, superseded, inactive, or completed methodology file may remain in the repository for provenance.

It should be labeled clearly when operational ambiguity is possible.

Possible classifications include:

- historical
- superseded
- inactive
- completed preregistered plan
- retained for provenance

A completed preregistered plan remains evidentially important even when it no longer governs future observations.

It preserves what the scoring boundary was before the result was known.

Historical or completed methodology must not be treated as a current forward-looking rule when a later active document governs a new question.

---

# Active Versus Historical Status

Every methodology file whose operational status could become ambiguous should state near the top:

```text
Status:
Created:
Last updated:
Scope:
```

Possible status labels include:

- Active standing methodology
- Active preregistered evaluation plan
- Active preregistered collection plan
- Completed preregistered evaluation plan
- Historical
- Superseded
- Inactive
- Draft
- Retrospective note

A file’s presence in the directory does not prove that it is currently active.

Current status should be established through:

- the file header
- this directory guide
- `LATEST.md`
- `CHANGELOG.md`
- applicable audit records
- the model-error register

---

# Relationship to Repository Governance

Core archive-wide governance remains defined in:

- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`../ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`../STRUCTURAL_PRINCIPLES.md`](../STRUCTURAL_PRINCIPLES.md)

The relationship is:

```text
Repository Governance
        ↓
Standing Methodology
        ↓
Preregistered Evaluation or Collection Plan
        ↓
Active Observation
        ↓
Retrospective Evaluation
```

A methodology file may add operational detail.

It may not override stronger archive-wide governance without an explicit documented revision.

---

# Relationship to Extended Methodology

Extended analytical and conceptual methodology is stored under:

[`../docs/methodology/`](../docs/methodology/)

That layer includes materials such as:

- prediction-validity criteria
- prediction-to-outcome workflow
- UDI framework
- subject baseline context
- analytical overlays
- explanatory models

The distinction is:

### `/methodology`

Current operating rules, active preregistered plans, and completed preregistered plans retained for governance provenance.

### `/docs/methodology`

Extended analytical, conceptual, and explanatory documentation.

The boundary is not absolute.

When file placement is uncertain, prefer `/methodology` when the document directly governs:

- current collection
- correction
- privacy
- scoring
- outcome access
- an upcoming measurement event

Prefer `/docs/methodology` when the document primarily explains:

- theory
- analytical framing
- historical context
- conceptual models
- extended evaluation logic

Neither layer may override verified source evidence.

---

# Relationship to Other Archive Layers

## Governance

Governance defines what the archive permits.

Methodology defines how permitted work is performed.

---

## Protocols

Protocols define physical or behavioral exposure.

Methodology defines how that exposure and its outcomes are recorded and evaluated.

A methodology update does not automatically modify the physical protocol.

Record 046 observes the planned unload/reload sequence.

It does not create that sequence as a new recurring protocol.

---

## Reports

Reports preserve active observations and retrospective weekly interpretation.

Reports operate under methodology.

They must not rewrite preregistered evaluation or collection rules.

For record 045, the Week 32 report may retrospectively score the fixed August 13–16 evidence under the preregistered rules.

It may not use later August evidence to reopen or modify the result.

For record 046:

```text
2026-08-17:
registration context only

2026-08-18 through 2026-08-19:
descriptive unload/re-entry kinetics

2026-08-20 through 2026-08-23:
primary scoring evidence
```

Reports must preserve those boundaries.

---

## Data

Datasets contain structured observations and derived values.

Methodology defines:

- how values enter
- how missingness is handled
- how corrections occur
- how provenance is retained

---

## Source Artifacts

Source artifacts preserve provider- or device-generated evidence.

Methodology defines:

- source precedence
- public-versus-private status
- sanitization
- checksum handling
- transformation boundaries

---

## Schemas

Schemas define expected document or table structure.

Methodology defines the rules that give those fields meaning.

A valid schema does not guarantee valid interpretation.

---

## Audits and Validation

Validation checks mechanical integrity.

Audits review mechanical and semantic governance.

Methodology provides the rules against which both are evaluated.

See:

- [`../VERIFICATION.md`](../VERIFICATION.md)
- [`../tools/validate_repository.py`](../tools/validate_repository.py)
- [`../docs/audits/`](../docs/audits/)

The local validator currently protects the open/unscored state of:

```text
041
042
043
044
046
```

It separately protects record 045 as:

```text
closed
```

with its recorded outcome preserved.

Validation does not independently recompute or adjudicate the record 045 score.

It does not score record 046.

---

# Source and Correction Boundary

Methodology must preserve the distinction among:

```text
Source artifact
      ↓
Structured transcription
      ↓
Derived value
      ↓
Retrospective interpretation
```

A later layer must not be represented as an earlier one.

For correction:

```text
Preserve current state
      ↓
Locate stronger source
      ↓
Confirm semantic equivalence
      ↓
Document the issue
      ↓
Correct narrowly
      ↓
Preserve Git history
      ↓
Validate dependent outputs
```

A correction is not authorized merely because:

- another value appears more plausible
- a stage total does not reconcile
- a later export differs
- a neighboring day contains a usable value
- a summary would look cleaner after replacement

Unresolved evidence should remain unresolved.

---

# Preregistration Boundary

A document is preregistered only when its governing rules were committed before the relevant outcome was accessed.

Preregistration should preserve:

- timestamped repository history
- explicit scope
- known information
- unknown outcome
- primary endpoint
- admissible evidence
- closure conditions
- missingness and discordance rules

The timing boundary is specific to the prediction or collection question being governed.

For records 041–044, use:

```text
open_prediction_evaluation_plan_041_044.md
```

For record 045, use:

```text
open_prediction_evaluation_plan_045.md
```

Record 045 is now a completed preregistered prediction.

Its fixed boundary remains:

```text
Registration:
2026-08-12

Known registration context:
all evidence through 2026-08-12

Admissible scoring window:
2026-08-13 through 2026-08-16

Excluded:
Week 31
2026-08-10 through 2026-08-12
August 17–18 snapshot outcomes

Outcome:
supported
```

For record 046, use:

```text
open_prediction_evaluation_plan_046.md
```

Its prospective boundary is:

```text
Registration:
2026-08-17

Registration context only:
2026-08-17

Descriptive unload/re-entry kinetics:
2026-08-18 through 2026-08-19

Primary scoring window:
2026-08-20 through 2026-08-23

Excluded from scoring:
DEXA result
VO2-max measured result
Bod Pod result
TruDiagnostic result
other August biological-snapshot outcomes
```

A document written after outcome access may still be useful.

It must be labeled retrospective rather than preregistered.

A completed prediction must not be extended merely because a related future question remains unanswered.

The related future question should receive a new prospective record.

---

# Interpretation Boundary

Methodology documents do not independently establish:

- biological causality
- clinical significance
- protocol efficacy
- prediction success
- permanent adaptation
- phase transition
- generalizability
- absence of measurement error

Interpretation must remain proportional to:

- source quality
- timing
- metric semantics
- collection conditions
- comparability
- missingness
- contradictory evidence
- registered evaluation rules

Record 045 has been scored supported.

That result establishes only that its preregistered short-window partial-reconvergence criteria were met.

It does not independently establish:

- complete recovery
- optimal recovery
- absence of accumulated cost
- permanent autonomic normalization
- Phase 2D
- favorable August biological results
- persistence after unloading
- persistence after return to normal training

Record 046 is designed to evaluate the final two questions separately.

A supported record 046 result would establish only that the favorable autonomic state remained broadly preserved under its fixed unload/reload evaluation boundary.

It would not independently establish:

- absence of training cost
- unlimited recovery reserve
- permanent autonomic adaptation
- biological snapshot success
- Phase 2D

A failed record 046 result would not independently establish:

- clinical overtraining
- global recovery collapse
- protocol failure
- failure of records 041–044
- biological regression
- termination of Phase 2

---

# File Naming Guidance

Use stable, descriptive lowercase filenames.

Standing methodology:

```text
descriptive-method-name.md
```

Dated collection or evaluation plans:

```text
YYYY-MM-descriptive-plan.md
```

Event-specific documents may use:

```text
YYYY-MM-DD-descriptive-record.md
```

Record-specific active plans may use:

```text
open_prediction_evaluation_plan_###.md
```

or a bounded record range when the records share the same registration and evaluation framework:

```text
open_prediction_evaluation_plan_###_###.md
```

The `open_prediction_` filename prefix may remain after a record closes when preserving the original preregistered artifact name is preferable to renaming historical evidence after outcome access.

Operational status should then be established by the document header, this README, the model-error register, and current repository navigation.

Avoid filenames based only on:

- `new`
- `final`
- `updated`
- `latest`
- versionless generic terms that may become ambiguous

When a file is superseded, preserve the historical file when it contributes provenance and clearly label its status.

---

# Adding a New Methodology File

Before adding a new file, determine:

1. What operational problem does it solve?
2. Is it a standing rule, preregistered plan, completed plan, or retrospective note?
3. Does an existing file already govern the issue?
4. Is the document being written before or after outcome access?
5. What evidence layer does it constrain?
6. Does it create unnecessary maintenance?
7. Which files must link to it?
8. Does it require a changelog entry?
9. Does it require validator changes?
10. Does it change protocol, prediction, phase, or release status?

A new methodology file should normally be linked from:

- this README
- `INDEX.md`
- `LATEST.md` when actively relevant
- `CHANGELOG.md` when material

A new prediction-specific plan should remain separate from an older preregistered plan when combining them would blur registration timing or admissible evidence.

Record 046 is an example of this rule.

It was created as a separate prediction rather than extending the already completed record 045 boundary.

---

# Current Active Methodology State

As of 2026-08-17:

```text
Data collection:
Active standing methodology

Public artifact sanitization:
Active standing methodology

Prediction evaluation:
Active standing methodology

Records 041–044 evaluation plan:
Active and binding

Record 045 evaluation plan:
Completed preregistered evaluation plan retained for provenance

Record 045 status:
Closed / supported

Record 046 evaluation plan:
Active and prospective

Record 046 registration date:
2026-08-17

Record 046 registration-context date:
2026-08-17

Record 046 descriptive unload/re-entry interval:
2026-08-18 through 2026-08-19

Record 046 primary scoring window:
2026-08-20 through 2026-08-23

August 2026 snapshot collection plan:
Active and binding through the collection workflow

Open and unscored model-error records:
041
042
043
044
046

Canonical phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
Undeclared

Underlying physical protocol:
B1 + Load Integration preserved

Current temporary testing schedule:
2026-08-17 — no B1 / no LI
2026-08-18 — no B1 / no LI
2026-08-19 — planned normal B1 + LI return
```

The current methodology state preserves four distinct governance artifacts:

```text
Records 041–044:
open_prediction_evaluation_plan_041_044.md

Completed Record 045:
open_prediction_evaluation_plan_045.md

Active Record 046:
open_prediction_evaluation_plan_046.md

August biological and performance collection:
2026-08-snapshot-collection-plan.md
```

These artifacts have different registration dates, purposes, and evidence boundaries.

They should not be collapsed into one retrospective document.

---

# Related Documents

- [`../INDEX.md`](../INDEX.md)
- [`../LATEST.md`](../LATEST.md)
- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`../ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`../MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)
- [`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)
- [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)
- [`../data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)
- [`../PHASE_MAP.md`](../PHASE_MAP.md)
- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)
- [`../VERIFICATION.md`](../VERIFICATION.md)
- [`../CHANGELOG.md`](../CHANGELOG.md)
- [`../docs/methodology/`](../docs/methodology/)

---

## Version Note

This directory guide was expanded on 2026-07-29 to reflect the methodology layer’s current operational role.

That revision:

- indexed the active methodology files
- distinguished standing methodology from preregistered plans
- distinguished active, retrospective, historical, and superseded documents
- exposed the August snapshot collection plan
- exposed the active evaluation plan for records 041–044
- defined the relationship between `/methodology` and `/docs/methodology`
- defined source, correction, privacy, and interpretation boundaries
- added file-placement and naming guidance
- defined expectations for future methodology additions

On 2026-08-12, this guide was updated after prospective registration of Model Error 045.

The 2026-08-12 revision:

- exposed `open_prediction_evaluation_plan_045.md`
- preserved `open_prediction_evaluation_plan_041_044.md` unchanged as the governing plan for records 041–044
- identified record 045 as a separate secondary trajectory prediction
- recorded the 2026-08-12 registration date
- recorded the 2026-08-13 through 2026-08-16 admissible scoring window
- preserved Week 31 and August 10–12 as registration context only
- excluded August 17–18 snapshot outcomes from record 045 scoring
- documented the fixed record 045 autonomic thresholds
- documented the relationship between record 045 and records 041–044
- documented validator protection through record 045
- advanced the then-current open prediction set to records 041–045
- preserved the August collection plan as a separate governance artifact
- preserved the existing physical protocol and phase state

On 2026-08-17, this guide was updated after the record 045 scoring boundary closed and Model Error 046 was prospectively registered.

The 2026-08-17 revision:

- records record 045 as closed and supported
- preserves `open_prediction_evaluation_plan_045.md` as the completed preregistered governance artifact
- records the fixed August 13–16 record 045 scoring values and 4-of-4 favorable threshold result
- preserves the 2026-08-16 Load Integration omission as testing-directed rather than recovery-driven for record 045
- retains the same omission as a separate collection/governance fact for records 043 and 044
- prohibits later unload/reload evidence from reopening or extending record 045
- exposes `open_prediction_evaluation_plan_046.md`
- identifies record 046 as a separate prospective autonomic unload/reload trajectory prediction
- records 2026-08-17 as registration context only for record 046
- records 2026-08-18 through 2026-08-19 as descriptive unload/re-entry kinetics
- records 2026-08-20 through 2026-08-23 as the fixed record 046 primary scoring window
- preserves the record 045 autonomic thresholds unchanged for direct 046 comparability
- excludes August biological and performance outcomes from record 046 scoring
- updates the protected open prediction set to records 041–044 and 046
- documents record 045 as separately protected in its closed/scored state
- preserves records 041–044 unchanged
- preserves Phase 2 and the consolidation / lock-in observation substate
- preserves the underlying B1 + Load Integration architecture after the temporary testing interruption

The revision changes methodology navigation and current-governance documentation only.

It does not alter:

- any source artifact
- any canonical biological value
- records 041–044
- the registered wording or thresholds of record 045
- the registered wording or thresholds of record 046
- any closed prediction other than documenting its already completed state
- the underlying physical protocol
- the August snapshot collection plan
- any phase declaration
- any release metadata
