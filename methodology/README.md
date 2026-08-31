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

The `/methodology` directory contains rules and preregistered plans that directly govern archive operation.

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
- partially resolved preregistered plans that still govern an open record

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

A preregistered multi-record plan may remain operationally relevant when some records have closed and another record governed by the same original artifact remains open.

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

## Preserved Preregistered Evaluation Plan — Records 041–044

### [`open_prediction_evaluation_plan_041_044.md`](open_prediction_evaluation_plan_041_044.md)

This is the preserved preregistered evaluation plan for Model Error records 041–044.

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

Its original registered rules remain preserved.

Current outcomes under this plan are:

```text
041:
closed / supported

042:
closed / not supported — continued adaptation

043:
open / TruDiagnostic provider results pending

044:
closed / not supported — narrow snapshot-directed governance deviation
```

Records 041, 042, and 044 were formally adjudicated at the August snapshot-cycle endpoint.

Record 043 remains open because its primary TruDiagnostic provider-result domain is still pending.

The original preregistration artifact must not be rewritten after those outcomes became known.

Later reports may reference the closed outcomes.

They may not:

- reopen records 041, 042, or 044
- extend their evidence windows
- revise their predictions
- improve or weaken their recorded outcomes
- substitute a new primary endpoint for record 043

Records 045 and 046 do not amend this plan.

The 041–044 evaluation artifact remains preserved under its original filename because renaming or restructuring it after outcome access would weaken provenance.

---

## Record 041 — Closed Recovery-Capacity Evaluation

Record 041 was registered on:

```text
2026-06-25
```

Its domain was:

```text
recovery_capacity
```

Its registered prediction was:

```text
stable
```

Its prediction type was:

```text
primary trajectory
```

The observation block produced measurable autonomic compression.

The registered recovery-capacity failure boundary nevertheless was not crossed.

No qualifying combination of:

- unplanned recovery intervention
- multi-session training regression
- persistent physiological suppression with required functional or subjective deterioration

occurred.

The 2026-08-16 Load Integration omission was testing-directed rather than recovery-driven.

It therefore did not constitute a record 041 recovery-capacity failure.

Record 041 closed as:

```text
actual:
stable

error direction:
none

outcome:
supported
```

This result does not establish:

- costless accumulation
- unlimited recovery capacity
- permanent autonomic normalization
- absence of short-window physiological strain

The original governing rules remain preserved in `open_prediction_evaluation_plan_041_044.md`.

---

## Record 042 — Closed Ambient-Execution Plateau Evaluation

Record 042 was registered on:

```text
2026-06-25
```

Its domain was:

```text
ambient_execution
```

Its registered prediction was:

```text
plateau
```

Its prediction type was:

```text
primary trajectory
```

The preregistered counter-evidence threshold was met across:

- at least three separately dated qualifying observations
- more than 14 calendar days
- multiple contexts
- no substantive explanatory protocol progression

Observed characteristics included:

- voluntary tempo modulation
- positional optionality
- conversational divided attention
- social-context execution
- reduced preparation
- reduced session salience
- automatic bar contact
- automatic movement initiation
- automatic positional organization
- automatic force control
- automatic transitions
- preserved execution across differing short-window autonomic states

Record 042 closed as:

```text
actual:
continued_adaptation

error direction:
under

outcome:
not supported
```

The model underestimated continued adaptation beyond the predicted ambient-execution plateau.

This result does not independently declare Phase 2D.

The original governing rules remain preserved in `open_prediction_evaluation_plan_041_044.md`.

---

## Record 043 — Active August Biological Evaluation

Record 043 remains open under:

### [`open_prediction_evaluation_plan_041_044.md`](open_prediction_evaluation_plan_041_044.md)

Its domain is:

```text
biological_translation
```

Its registered prediction is:

```text
moderate_improvement
```

Its prediction type is:

```text
primary trajectory
```

The primary comparison remains:

```text
May 2026
→
August 2026
```

The primary biological domain remains:

```text
TruDiagnostic
```

The August physical collection is complete.

The TruDiagnostic sample was collected on:

```text
2026-08-17
```

The corresponding provider-result domain remains pending.

Supplemental domains include:

- DEXA
- VO₂ max
- Bod Pod
- bodyweight
- recovery telemetry
- subjective state

No supplemental physical result may substitute for the pending primary TruDiagnostic evidence.

Record 043 must remain open until the required source evidence is available and the preregistered rules are applied.

The record 044 governance outcome does not independently determine record 043.

Record 046 likewise does not determine record 043.

---

## Record 044 — Closed Protocol-Governance Evaluation

Record 044 was registered on:

```text
2026-06-25
```

Its domain was:

```text
protocol_governance
```

Its registered prediction was:

```text
preserved
```

Its prediction type was:

```text
primary state
```

Most of the observation window showed strong governance restraint.

No:

- forced training progression
- direct grip program
- high-volume pull-up test
- manufactured portability test
- recovery-driven reaction to isolated wearable values
- premature phase declaration

was introduced.

A separately registered snapshot-governance boundary nevertheless applied to testing preparation.

On:

```text
2026-08-16
```

Load Integration was intentionally withheld to preserve recovery before the following morning’s testing.

The omission was:

- intentional
- testing-directed
- not provider-required
- not recovery-driven

Because the preregistered collection posture was intended to preserve representative-state biology rather than create unusually favorable testing freshness, the omission conflicted with that snapshot-governance boundary.

Record 044 therefore closed as:

```text
outcome:
not supported

error direction:
under

classification:
narrow snapshot-directed governance deviation
```

This outcome does not establish:

- broad protocol-governance collapse
- biological harm
- invalidity of the August snapshot
- failure of record 041
- failure of record 045

The original governing rules remain preserved in `open_prediction_evaluation_plan_041_044.md`.

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

The same event was separately evaluated under record 044 because record 044 governed snapshot preparation rather than recovery-driven intervention.

Record 044 subsequently closed as not supported.

Record 045 remains closed and unchanged.

Its methodology file remains preserved because it documents the rules that governed the prediction before the outcome was known.

Record 045 does not:

- replace record 041
- redefine recovery-capacity criteria
- score motor automaticity under record 042
- alter the Model Error 043 biological endpoint
- repair or modify record 044
- establish complete recovery
- establish absence of accumulated training cost
- declare Phase 2D
- determine later unload/reload behavior

Later evidence must not reopen or extend record 045.

---

## Completed Evaluation Plan — Record 046

### [`open_prediction_evaluation_plan_046.md`](open_prediction_evaluation_plan_046.md)

This is the preserved preregistered evaluation plan for Model Error record 046.

Record 046 was registered on:

```text
2026-08-17
```

Its domain is:

```text
autonomic_unload_reload
```

Its registered prediction was:

```text
reconvergence_persists_after_unload_reload
```

Its prediction type was:

```text
secondary trajectory
```

Record 046 began where the completed record 045 question ended.

Record 045 asked:

```text
Did partial autonomic reconvergence occur?
```

Record 046 asked:

```text
Does that reconvergence remain broadly preserved
after planned training withdrawal and reload?
```

The known exposure sequence at registration was:

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

was registration context only.

It could not satisfy the prediction.

The plan preserved:

```text
2026-08-18
2026-08-19
```

as descriptive unload and re-entry kinetics.

The fixed primary scoring window was:

```text
2026-08-20 through 2026-08-23
```

Record 046 intentionally reused the same favorable autonomic thresholds as record 045:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

This preserved direct comparability without recalibrating thresholds after the favorable record 045 outcome.

Support required:

```text
at least 3 of 4 autonomic thresholds favorable
across the fixed 2026-08-20 through 2026-08-23 means

AND

no multi-session functional regression after reload

AND

no recovery-driven protocol reduction after normal training resumed
```

The plan explicitly allowed a short-lived autonomic disturbance after the 2026-08-17 maximal VO₂ test.

Such an acute response could be documented.

It could not independently fail record 046.

The plan excluded the measured outcomes of:

- DEXA
- VO₂ max
- Bod Pod
- TruDiagnostic
- TruAge
- TruHealth
- other August biological-snapshot interpretation

Those outcomes remained independently governed.

After the fixed scoring window closed, the four-day arithmetic means were:

```text
Daily HRV:
60.25 ms
favorable

Sleep HRV:
63.25 ms
unfavorable

Resting HR:
52.0 bpm
unfavorable

Sleeping HR:
54.0 bpm
unfavorable
```

The quantitative threshold result was:

```text
1 of 4 favorable
```

The additional registered conditions remained:

```text
Multi-session functional regression after reload:
No

Recovery-driven protocol reduction after normal training resumed:
No
```

Because support required at least three of four favorable autonomic thresholds in addition to preserved function and protocol continuity, record 046 did not satisfy its registered support criterion.

Record 046 closed as:

```text
status:
closed

actual:
failed_autonomic_recompression

error direction:
over

outcome:
not supported
```

The `over` direction records that the model overestimated persistence of the favorable record 045 autonomic state across the immediate post-testing reload interval.

Late-window autonomic improvement on 2026-08-22 and 2026-08-23 remains meaningful contextual evidence of reversibility.

It does not alter the fixed four-day scoring mean or rescue the registered prediction.

Record 046 does not:

- reopen record 041
- reopen record 042
- alter record 043
- repair record 044
- reopen record 045
- establish clinical overtraining
- establish global recovery collapse
- establish failure of the underlying B1 + Load Integration architecture
- create a new physical training protocol
- declare Phase 2D

The record 046 evaluation plan is complete and retained unchanged as preregistration provenance.

Later evidence must not reopen or extend record 046.

---

## August Snapshot Collection Plan — Physical Collection Complete

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

The physical collection window is now complete.

Actual collection included:

```text
2026-08-17
TruDiagnostic sample collection at 05:37
DEXA at 07:55
VO₂-max testing at approximately 08:10

2026-08-18
Bod Pod at 08:26
```

Current collection state is:

```text
physical collection:
complete

physical source-artifact preservation:
complete

TruDiagnostic sample collection:
complete

TruDiagnostic provider results:
pending

complete biological interpretation:
pending
```

The collection plan does not itself determine the August biological outcome.

It does not:

- alter or score record 043
- reopen or rescore record 046
- authorize protocol progression
- declare Phase 2D
- create a release automatically
- reopen any closed model-error record

The 2026-08-16 Load Integration omission remains documented as a factual collection-condition deviation rather than being removed from the record.

The plan itself must not be retrospectively rewritten to make that deviation appear preregistered.

The governance significance of that omission has already been adjudicated under record 044.

Record 044 closed as not supported.

The biological materiality of the omission remains unknown and must not be inferred from the governance result.

The collection plan remains relevant to record 043 interpretation until the required primary molecular evidence is available.

Any later factual amendment should be:

- dated
- narrow
- factual
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

A multi-record plan may remain partly operational when one governed record remains open after other records in the same original plan have closed.

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

After physical collection is complete, the plan remains evidentially relevant for:

- actual-versus-planned comparison
- deviation review
- outcome interpretation
- provenance

It must not be rewritten after outcome access to make execution appear more compliant than it was.

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
- partially resolved preregistered plan with an open governed record
- retained for provenance

A completed preregistered plan remains evidentially important even when it no longer governs future observations.

It preserves what the scoring boundary was before the result was known.

Historical or completed methodology must not be treated as a current forward-looking rule when a later active document governs a new question.

---

# Active Versus Historical Status

Every methodology file whose operational status could become ambiguous should state near the top when appropriate:

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
- Partially resolved preregistered evaluation plan
- Physical collection complete / interpretation pending
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

Current operating rules, active preregistered plans, partially resolved preregistered plans, and completed preregistered plans retained for governance provenance.

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

Record 046 observed a temporary testing-directed unload/reload sequence.

It did not create that sequence as a new recurring protocol.

---

## Reports

Reports preserve active observations and retrospective weekly interpretation.

Reports operate under methodology.

They must not rewrite preregistered evaluation or collection rules.

Records 041, 042, and 044 are closed.

Later reports may reference them historically.

They may not reopen or rescore them.

Record 043 remains open pending its required primary source evidence.

For record 045, later reports may preserve the completed August 13–16 score.

They may not use later August evidence to reopen or modify the result.

For record 046, the preserved scoring boundary is:

```text
2026-08-17:
registration context only

2026-08-18 through 2026-08-19:
descriptive unload/re-entry kinetics

2026-08-20 through 2026-08-23:
primary scoring evidence
```

Record 046 is now closed.

Later reports may discuss subsequent recovery or autonomic behavior as new evidence.

They may not use it to:

- reopen record 046
- extend its scoring window
- alter its four-day means
- change its 1-of-4 threshold result
- rescore `failed_autonomic_recompression`

---

## Data

Datasets contain structured observations and derived values.

Methodology defines:

- how values enter
- how missingness is handled
- how corrections occur
- how provenance is retained

The August integrated biological snapshot must not be treated as complete before the pending primary molecular source evidence is verified.

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
043
```

It separately protects the adjudicated closed state of:

```text
041
042
044
045
046
```

with their recorded actual values and error directions preserved where applicable.

It additionally protects registration provenance for records:

```text
041–046
```

including:

```text
calibration_state = pre
```

and preservation of the original registered `Prediction:` narrative.

Validation does not independently recompute or adjudicate those scores.

It does not score record 043.

It does not rescore record 046.

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

Current status under that plan:

```text
041:
closed / supported

042:
closed / not supported — continued adaptation

043:
open / pending TruDiagnostic provider results

044:
closed / not supported — narrow governance deviation
```

The original plan remains preserved unchanged.

For record 045, use:

```text
open_prediction_evaluation_plan_045.md
```

Record 045 is a completed preregistered prediction.

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

Record 046 is also a completed preregistered prediction.

Its preserved boundary remains:

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
VO₂-max measured result
Bod Pod result
TruDiagnostic result
other August biological-snapshot outcomes

Outcome:
failed_autonomic_recompression

Error direction:
over
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

Record 041 has been scored supported.

That result establishes only that its preregistered recovery-capacity failure boundary was not crossed.

It does not independently establish:

- absence of accumulated physiological cost
- unlimited recovery reserve
- permanent autonomic normalization

Record 042 has been scored not supported through continued adaptation.

That result establishes only that the predicted ambient-execution plateau underestimated the observed adaptive transition.

It does not independently establish:

- Phase 2D
- unlimited adaptation
- need for immediate progression

Record 044 has been scored not supported because of a narrow snapshot-directed governance deviation.

That result establishes a governance miss under the registered collection boundary.

It does not independently establish:

- biological harm
- invalidity of the August snapshot
- broad protocol failure
- failure of recovery capacity

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

Record 046 has been scored not supported under its fixed unload/reload boundary.

Its registered autonomic condition produced:

```text
1 of 4 favorable thresholds
```

while:

```text
multi-session functional regression:
No

recovery-driven protocol reduction:
No
```

The formal outcome is:

```text
failed_autonomic_recompression
```

with:

```text
error direction:
over
```

That result establishes only that the model overestimated persistence of the favorable record 045 autonomic state across the fixed immediate post-testing reload interval.

It does not independently establish:

- clinical overtraining
- global recovery collapse
- broad protocol failure
- permanent autonomic suppression
- biological regression
- failure of record 041
- failure of record 045
- termination of Phase 2
- absence of later recovery
- absence of portability
- absence of continued motor consolidation

The observed late-window rebound remains meaningful contextual evidence.

It does not change the preregistered score.

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
2. Is it a standing rule, preregistered plan, completed plan, partially resolved plan, or retrospective note?
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

# Current Methodology State

As of 2026-08-31:

```text
Data collection:
Active standing methodology

Public artifact sanitization:
Active standing methodology

Prediction evaluation:
Active standing methodology

Records 041–044 preregistration artifact:
Preserved and unchanged

Record 041:
Closed / supported

Record 042:
Closed / not supported — continued adaptation

Record 043:
Open / TruDiagnostic provider results pending

Record 044:
Closed / not supported — narrow snapshot-directed governance deviation

Record 045 evaluation plan:
Completed preregistered evaluation plan retained for provenance

Record 045:
Closed / supported

Record 046 evaluation plan:
Completed preregistered evaluation plan retained for provenance

Record 046:
Closed / not supported

Record 046 actual:
failed_autonomic_recompression

Record 046 error direction:
over

Record 046 registration date:
2026-08-17

Record 046 registration-context date:
2026-08-17

Record 046 descriptive unload/re-entry interval:
2026-08-18 through 2026-08-19

Record 046 primary scoring window:
2026-08-20 through 2026-08-23

August 2026 snapshot collection plan:
Physical collection complete; retained for execution comparison and pending record 043 interpretation

August physical source artifacts:
Archived, privacy-reviewed, checksum-manifested, and validator-verified

TruDiagnostic sample:
Collected 2026-08-17

TruDiagnostic provider results:
Pending

Open and unscored model-error records:
043

Closed recent model-error records:
041
042
044
045
046

Canonical sleep:
Continuous through 2026-08-30
203 daily rows

Current weekly window:
2026-W35

Most recent closed weekly window:
2026-W34

Canonical phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
Undeclared

Underlying physical protocol:
B1 + Load Integration preserved

Testing-related withdrawal:
Completed 2026-08-18

Normal training return:
Completed 2026-08-19
```

The current methodology state preserves four distinct governance artifacts:

```text
Original Records 041–044 framework:
open_prediction_evaluation_plan_041_044.md

Completed Record 045:
open_prediction_evaluation_plan_045.md

Completed Record 046:
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
- [`../data/model_error/udi_by_type_tracker.csv`](../data/model_error/udi_by_type_tracker.csv)
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

- recorded record 045 as closed and supported
- preserved `open_prediction_evaluation_plan_045.md` as the completed preregistered governance artifact
- recorded the fixed August 13–16 record 045 scoring values and 4-of-4 favorable threshold result
- preserved the 2026-08-16 Load Integration omission as testing-directed rather than recovery-driven for record 045
- retained the same omission as a separate collection/governance fact for records 043 and 044
- prohibited later unload/reload evidence from reopening or extending record 045
- exposed `open_prediction_evaluation_plan_046.md`
- identified record 046 as a separate prospective autonomic unload/reload trajectory prediction
- recorded 2026-08-17 as registration context only for record 046
- recorded 2026-08-18 through 2026-08-19 as descriptive unload/re-entry kinetics
- recorded 2026-08-20 through 2026-08-23 as the fixed record 046 primary scoring window
- preserved the record 045 autonomic thresholds unchanged for direct 046 comparability
- excluded August biological and performance outcomes from record 046 scoring
- updated the then-protected open prediction set to records 041–044 and 046
- documented record 045 as separately protected in its closed/scored state
- preserved records 041–044 unchanged at that point
- preserved Phase 2 and the consolidation / lock-in observation substate
- preserved the underlying B1 + Load Integration architecture after the temporary testing interruption

On 2026-08-18, this guide was aligned after completion of the August physical collection window and formal adjudication of Model Error records 041, 042, and 044.

The 2026-08-18 revision:

- preserves `open_prediction_evaluation_plan_041_044.md` unchanged as the original preregistration artifact
- records 041 as closed and supported
- records 042 as closed and not supported through continued adaptation
- preserves 043 as open pending the primary TruDiagnostic provider-result domain
- records 044 as closed and not supported through a narrow snapshot-directed governance deviation
- preserves 045 as closed and supported
- preserves 046 as open and unscored
- reduces the current open model-error set to records 043 and 046
- records the August 17–18 physical collection window as complete
- records the August physical source-artifact layer as archived, privacy-reviewed, checksum-manifested, and validator-verified
- preserves the August 16 Load Integration omission as testing-directed rather than recovery-driven
- records that the omission activated the separately registered record 044 snapshot-governance boundary
- does not infer that the governance deviation materially altered an August biological measurement
- preserves record 043 as independently open pending TruDiagnostic provider results
- updates methodology navigation to distinguish closed, open, partially resolved, and completed preregistration states
- updates validator documentation so records 041, 042, 044, and 045 are protected as closed while records 043 and 046 remain open
- preserves the record 046 August 20–23 primary scoring window
- preserves Phase 2 and the consolidation / lock-in observation substate
- leaves formal Phase 2D undeclared

The 2026-08-18 revision does not alter:

- any source artifact
- any canonical biological value
- the original prediction wording of records 041–044
- the original 041–044 preregistration rules
- the registered wording or thresholds of record 045
- the registered wording or thresholds of record 046
- the pending record 043 outcome
- the underlying physical protocol
- the original August snapshot collection-plan language
- any phase declaration
- any release metadata

On 2026-08-24, this guide was aligned after Week 33 closeout and formal adjudication of Model Error 046.

The 2026-08-24 revision:

- preserves `open_prediction_evaluation_plan_046.md` unchanged as the original record 046 preregistration artifact
- reclassifies the record 046 plan from active/prospective to completed and retained for provenance
- records record 046 as closed and not supported
- records `actual=failed_autonomic_recompression`
- records `error_direction=over`
- preserves `calibration_state=pre`
- preserves the fixed `2026-08-20` through `2026-08-23` scoring window
- records the four fixed-window arithmetic means
- records the 1-of-4 favorable autonomic threshold result
- records preserved function after reload
- records the absence of recovery-driven protocol reduction
- preserves late-window autonomic improvement as context rather than rescoring evidence
- prohibits later evidence from reopening or extending record 046
- reduces the current open model-error set to record 043
- advances the protected closed set to records 041, 042, 044, 045, and 046
- advances canonical sleep coverage through `2026-08-23`
- advances the active weekly window to `2026-W34`
- records `2026-W33` as closed
- records normal B1 + Load Integration return as completed on `2026-08-19`
- preserves record 043 as open pending TruDiagnostic provider results
- preserves the primary state and trajectory concordance summaries unchanged because record 046 is secondary
- preserves Phase 2 and the consolidation / lock-in observation substate
- leaves formal Phase 2D undeclared

The 2026-08-24 revision does not alter:

- the original record 046 preregistration artifact
- any record 046 registered threshold
- the record 046 scoring window
- any source artifact
- any artifact checksum
- the pending record 043 outcome
- primary UDI or concordance values
- the underlying B1 + Load Integration architecture
- any formal phase declaration
- release metadata

On 2026-08-31, this guide was aligned after Week 34 closeout and Week 35 initialization.

The 2026-08-31 revision:

- advances the current methodology-state date through `2026-08-31`
- advances canonical sleep coverage through `2026-08-30`
- records 203 continuous canonical sleep rows
- records `2026-W34` as the most recent closed weekly window
- advances `2026-W35` to the current active weekly window
- preserves record 043 as the sole open and unscored model-error record
- preserves records 041, 042, 044, 045, and 046 as closed historical outcomes
- preserves the original records 041–044 preregistration artifact unchanged
- preserves the completed record 045 preregistration artifact unchanged
- preserves the completed record 046 preregistration artifact unchanged
- preserves all registered record 045 and 046 scoring boundaries
- preserves record 046 as `failed_autonomic_recompression`
- preserves record 046 `error_direction=over`
- preserves the August snapshot collection plan as physically complete but still relevant to pending record 043 interpretation
- preserves TruDiagnostic provider results as pending
- preserves Phase 2 — Load Integration
- preserves the consolidation / lock-in observation substate
- preserves the underlying B1 + Load Integration architecture
- leaves formal Phase 2D undeclared

The 2026-08-31 revision is a live-state alignment only.

It does not alter:

- standing methodology
- source hierarchy
- correction rules
- privacy rules
- prediction-evaluation rules
- any preregistered prediction wording
- any preregistered threshold
- any prediction scoring window
- any adjudicated model-error outcome
- any source artifact
- any artifact checksum
- any canonical biological value
- the pending record 043 outcome
- primary UDI or concordance values
- the underlying physical protocol
- any formal phase declaration
- release metadata
