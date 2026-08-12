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

Record 045 does not amend this plan.

The 041–044 evaluation block remains preserved as originally registered.

---

## Active Evaluation Plan — Record 045

### [`open_prediction_evaluation_plan_045.md`](open_prediction_evaluation_plan_045.md)

This is the separate preregistered evaluation plan for Model Error record 045.

Record 045 was registered on:

```text
2026-08-12
```

Its domain is:

```text
autonomic_reconvergence
```

Its registered prediction is:

```text
partial_reconvergence
```

Its admissible scoring window is:

```text
2026-08-13 through 2026-08-16
```

The plan was created after retrospective closeout of Week 31 but before the admissible record 045 outcome window began.

The following observations are registration context only:

```text
2026-W31
2026-08-10
2026-08-11
2026-08-12
```

They may explain why the prediction was generated.

They cannot satisfy it.

August 17–18 biological and performance snapshot results are also excluded from record 045 scoring.

The plan defines:

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

Registered favorable thresholds are:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

Support requires:

```text
at least 3 of 4 autonomic thresholds met

AND

no multi-session functional regression

AND

no recovery-driven protocol reduction or intervention
```

Record 045 is a secondary trajectory prediction.

It does not:

- replace record 041
- redefine recovery-capacity criteria
- score motor automaticity under record 042
- alter the Model Error 043 biological endpoint
- modify record 044 governance criteria
- authorize a taper
- authorize a deload
- authorize an overload
- authorize recovery manipulation
- declare Phase 2D
- alter the August snapshot collection plan

The plan should remain fixed through its outcome window except for a documented source or factual correction that does not move the prediction boundary after outcome access.

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
- ordinary rather than snapshot-optimized behavior
- separation between collection and interpretation

The collection plan does not contain August results.

It does not:

- predict the result
- alter records 041–045
- change scoring rules
- authorize protocol progression
- declare Phase 2D
- create a release automatically
- determine the outcome of record 045

The plan should remain unchanged unless a factual collection detail changes.

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

Current examples:

- `open_prediction_evaluation_plan_041_044.md`
- `open_prediction_evaluation_plan_045.md`

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

Separate prediction blocks should remain in separate preregistration artifacts when their:

- registration dates differ
- evidence windows differ
- primary questions differ
- admissible evidence differs

The existence of a later evaluation plan must not silently rewrite an earlier one.

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

## Historical or Superseded Methodology

A historical methodology file may remain in the repository for provenance.

It should be labeled clearly as:

- historical
- superseded
- inactive
- retained for provenance

Historical methodology must not be used as a current governing rule when a later active document supersedes it.

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

Current operating rules and preregistered plans.

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

---

## Reports

Reports preserve active observations and retrospective weekly interpretation.

Reports operate under methodology.

They must not rewrite preregistered evaluation or collection rules.

For record 045, reports may preserve the relevant August 13–16 observations.

They may not use Week 31 or August 10–12 as scoring evidence merely because those observations generated the prediction.

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

The local validator explicitly protects records 041–045 while they remain in the current open evaluation state.

Validation does not score those records.

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

For record 045:

```text
Known registration context:
all evidence through 2026-08-12

Admissible scoring window:
2026-08-13 through 2026-08-16

Excluded:
Week 31
2026-08-10 through 2026-08-12
August 17–18 snapshot outcomes
```

A document written after outcome access may still be useful.

It must be labeled retrospective rather than preregistered.

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

A supported record 045 result would establish only that its preregistered short-window partial-reconvergence criteria were met.

It would not independently establish:

- complete recovery
- optimal recovery
- absence of accumulated cost
- permanent autonomic normalization
- Phase 2D
- favorable August biological results

A failed record 045 result likewise would not independently establish:

- recovery collapse
- protocol failure
- biological regression
- failure of records 041–044
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
2. Is it a standing rule, preregistered plan, or retrospective note?
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

---

# Current Active Methodology State

As of 2026-08-12:

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
Active and binding before its 2026-08-13 scoring-window start

August 2026 snapshot collection plan:
Active and binding before outcome access

Records 041–045:
Open and unscored

Record 045 scoring window:
2026-08-13 through 2026-08-16

Canonical phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
Undeclared

Physical protocol:
Unchanged
```

The current methodology state preserves three separate August governance artifacts:

```text
Records 041–044:
open_prediction_evaluation_plan_041_044.md

Record 045:
open_prediction_evaluation_plan_045.md

August biological and performance collection:
2026-08-snapshot-collection-plan.md
```

These artifacts have different scopes and should not be collapsed into one retrospective document.

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

- exposes `open_prediction_evaluation_plan_045.md`
- preserves `open_prediction_evaluation_plan_041_044.md` unchanged as the governing plan for records 041–044
- identifies record 045 as a separate secondary trajectory prediction
- records the 2026-08-12 registration date
- records the 2026-08-13 through 2026-08-16 admissible scoring window
- preserves Week 31 and August 10–12 as registration context only
- excludes August 17–18 snapshot outcomes from record 045 scoring
- documents the fixed record 045 autonomic thresholds
- documents the relationship between record 045 and records 041–044
- documents validator protection through record 045
- advances the current open prediction set to records 041–045
- preserves the August collection plan as a separate governance artifact
- preserves the existing physical protocol and phase state

The revision changes methodology navigation and active-governance documentation only.

It does not alter:

- any source artifact
- any canonical value
- records 041–044
- any closed prediction
- any physical protocol exposure
- the August snapshot collection conditions
- any phase declaration
- any release metadata
