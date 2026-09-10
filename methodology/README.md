# Methodology — Directory Guide

This directory contains the core operating methodology and preserved preregistered plans for the Daniel Longitudinal Study.

The methodology layer governs **process**: how evidence is collected, preserved, sanitized, reconciled, evaluated, and protected from outcome-driven reinterpretation. It does not independently determine biological meaning, declare a phase, or modify the physical protocol.

---

## Directory Role

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

A later result must not silently rewrite an earlier rule. Completed preregistered plans remain preserved after scoring so the original evaluation boundary stays inspectable.

Volatile current-state information is intentionally centralized elsewhere:

- current phase / weekly / model-error posture → [`../LATEST.md`](../LATEST.md)
- machine-readable coverage → [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- prediction outcomes → [`../data/model_error/`](../data/model_error/)
- repository change history → [`../CHANGELOG.md`](../CHANGELOG.md)

This guide therefore describes methodology roles rather than duplicating every live count or weekly state.

---

# Standing Methodology

## [`data-collection.md`](data-collection.md)

Defines how observations enter the archive, including:

- evidence hierarchy
- provider/device sources
- screenshots and direct exports
- manual transcription
- units and timing
- provenance
- missingness
- derivation
- source-backed correction
- source reconciliation

It prohibits inference presented as observation, silent correction, unsupported interpolation, correction from memory alone, and field substitution without semantic equivalence.

---

## [`anonymization.md`](anonymization.md)

Defines public-artifact sanitization and privacy-remediation rules, including:

- public/private source handling
- sanitized/redacted derivatives
- hidden-text and metadata review
- administrative-identifier removal
- checksum renewal
- Git-history boundaries
- external-distribution review

The subject’s public identity and chronological age are intentionally associated with the project. Privacy review instead focuses on unnecessary administrative exposure such as full date of birth, address, private contact information, patient/specimen/account identifiers, signatures, access tokens, and unrelated third-party information.

Sanitization must preserve the biological or performance evidence required for interpretation.

---

## [`prediction_evaluation.md`](prediction_evaluation.md)

Defines the general method for evaluating registered predictions, including:

- valid prediction structure
- observation windows
- admissible evidence
- closure requirements
- state / trajectory comparison
- error classification
- retention of incorrect predictions
- calibration review

A prediction must not be rewritten after registration, closed before sufficient evidence exists, scored from inadmissible evidence, reframed to preserve apparent success, or removed because it was incorrect.

---

# Preserved Preregistered Evaluation Plans

## Records 041–044

### [`open_prediction_evaluation_plan_041_044.md`](open_prediction_evaluation_plan_041_044.md)

This is the preserved preregistered evaluation artifact for:

- 041 — recovery capacity
- 042 — ambient-execution plateau
- 043 — August biological translation
- 044 — protocol governance

All four records are now closed. Their current adjudicated outcomes are maintained in the model-error layer rather than by rewriting this preregistration artifact.

Current disposition:

```text
041
closed / supported

042
closed / not supported — continued_adaptation

043
closed / not supported — overall_improvement_not_met
error_direction = over

044
closed / not supported — narrow snapshot-directed governance deviation
```

Record 043’s criterion-by-criterion closure is preserved in:

[`../data/model_error/record_043_closure.md`](../data/model_error/record_043_closure.md)

The original 041–044 plan remains unchanged after outcome access. Its filename is retained for provenance even though no governed record in the block remains open.

---

## Record 045

### [`open_prediction_evaluation_plan_045.md`](open_prediction_evaluation_plan_045.md)

Completed preregistered evaluation plan retained for provenance.

Registered scoring window:

```text
2026-08-13 through 2026-08-16
```

Outcome:

```text
closed / supported
```

The 2026-08-16 Load Integration omission was testing-directed rather than recovery-driven for the record 045 scoring rule. That same event was evaluated separately under record 044 because 044 governed snapshot preparation rather than recovery intervention.

Later evidence does not reopen or extend record 045.

---

## Record 046

### [`open_prediction_evaluation_plan_046.md`](open_prediction_evaluation_plan_046.md)

Completed preregistered evaluation plan retained for provenance.

Preserved evidence structure:

```text
2026-08-17
registration context only

2026-08-18 through 2026-08-19
descriptive unload / re-entry kinetics

2026-08-20 through 2026-08-23
primary scoring window
```

Outcome:

```text
closed / not supported
actual = failed_autonomic_recompression
error_direction = over
```

The plan explicitly excludes DEXA, VO₂-max, Bod Pod, TruDiagnostic, and other August biological-snapshot outcomes from record 046 scoring.

Later evidence does not reopen or extend record 046.

---

# August 2026 Snapshot Collection Plan

## [`2026-08-snapshot-collection-plan.md`](2026-08-snapshot-collection-plan.md)

This preregistered collection plan governs the August 17–18 biological and performance snapshot.

It preserves:

- representative-state collection intent
- TruDiagnostic as the primary Model Error 043 domain
- May 2026 as the primary 043 comparison baseline
- DEXA, VO₂ max, Bod Pod, bodyweight, recovery, and subjective state as supplemental domains
- fasting / intake / recent-training documentation
- source-artifact and privacy requirements
- delayed/missing/invalid test handling
- separation between collection and interpretation

The physical and molecular source-artifact collection cycle is complete.

The canonical contemporaneous collection sequence remains:

```text
2026-08-17
TruDiagnostic sample: 05:37 local
DEXA: 07:55
VO₂ max: approximately 08:10

2026-08-18
Bod Pod: 08:26
```

The contemporaneous repository record controls the actual TruDiagnostic sample date/time and preparation conditions. Provider-displayed administrative metadata are preserved but do not overwrite that record. The source-role reconciliation is documented in:

[`../data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](../data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

The collection plan does not itself determine the biological outcome and must not be retrospectively rewritten to improve apparent compliance.

---

# Methodology Document Types

Methodology files may serve different roles:

- **standing methodology** — recurring archive rules
- **preregistered evaluation plan** — fixed scoring rules for a defined future outcome
- **preregistered collection plan** — capture rules for a defined future measurement event
- **retrospective methodology note** — later explanation or procedural review
- **completed / historical methodology** — retained for provenance after its operational window ends

A file’s presence in this directory does not prove it is currently active. Where status may be ambiguous, establish current state from the file header, `LATEST.md`, `CHANGELOG.md`, and the applicable model-error record.

The `open_prediction_` filename prefix may remain after closure when retaining the original preregistration filename better preserves provenance than outcome-aware renaming.

---

# Source and Correction Boundary

Methodology preserves the distinction:

```text
Source artifact
      ↓
Structured transcription
      ↓
Derived value
      ↓
Retrospective interpretation
```

For corrections:

```text
Preserve current state
      ↓
Locate stronger source
      ↓
Confirm semantic equivalence
      ↓
Document the discrepancy
      ↓
Correct narrowly
      ↓
Preserve Git history
      ↓
Validate dependent outputs
```

A correction is not authorized merely because another value appears more plausible, a later export differs, a stage total does not reconcile, or a neighboring day contains a usable value.

Unresolved evidence remains unresolved.

---

# Preregistration Boundary

A document is preregistered only when its governing rules were committed before the relevant outcome was accessed.

Preregistration should preserve:

- repository timestamp/history
- explicit scope
- known information
- unknown outcome
- primary endpoint
- admissible evidence
- thresholds / closure conditions
- missingness and discordance rules

After outcome access begins, substantive scoring rules remain fixed.

A later related question should receive a new prospective record rather than extending a completed prediction window.

---

# Interpretation Boundary

Methodology documents do not independently establish:

- biological causality
- clinical significance
- protocol efficacy
- permanent adaptation
- phase transition
- generalizability
- absence of measurement error

Current protected outcomes remain bounded by their registered questions. In particular:

- 041 support does not establish costless accumulation or unlimited recovery reserve.
- 042 failure does not independently declare Phase 2D.
- 043 failure means the preregistered breadth-of-improvement rule was not met; it does not establish generalized biological deterioration or causal mechanism.
- 044 failure records a narrow governance miss and does not establish biological harm.
- 045 support does not establish complete or permanent recovery.
- 046 failure does not establish clinical overtraining, global recovery collapse, or failure of the underlying B1 + Load Integration architecture.

---

# Relationship to Other Archive Layers

## Governance

Archive-wide governance is defined in:

- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`../ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`../STRUCTURAL_PRINCIPLES.md`](../STRUCTURAL_PRINCIPLES.md)

Methodology may add operational detail but cannot silently override stronger archive-wide governance.

## Protocols

Protocols define physical or behavioral exposure. A methodology update does not automatically modify the physical protocol.

## Reports

Reports preserve active observations and retrospective weekly interpretation. Historical reports may correctly describe a prediction as open when that was its state at the time; later closure does not require rewriting those historical records.

## Data

Datasets contain structured observations and derived values. Methodology defines how values enter, how missingness is handled, how corrections occur, and how provenance is retained.

## Source Artifacts

Source artifacts preserve provider- or device-generated evidence. Methodology governs source precedence, sanitization, checksum handling, and transformation boundaries.

## Validation

Read-only validation is documented in:

- [`../VERIFICATION.md`](../VERIFICATION.md)
- [`../tools/validate_repository.py`](../tools/validate_repository.py)
- [`../tools/validate_machine_readable.py`](../tools/validate_machine_readable.py)

The core validator now protects records 041–046 as closed/scored historical outcomes while preserving `calibration_state=pre` and the original registered `Prediction:` narratives. It does not independently adjudicate those outcomes.

---

# Extended Methodology

Extended analytical and conceptual methodology is stored under:

[`../docs/methodology/`](../docs/methodology/)

Use `/methodology` when a document directly governs collection, correction, privacy, scoring, outcome access, or an upcoming measurement event. Use `/docs/methodology` when a document primarily explains theory, analytical framing, historical context, conceptual models, or extended evaluation logic.

Neither layer may override verified source evidence.

---

# File Naming Guidance

Use stable, descriptive lowercase filenames where practical.

Examples:

```text
descriptive-method-name.md
YYYY-MM-descriptive-plan.md
YYYY-MM-DD-descriptive-record.md
open_prediction_evaluation_plan_###.md
open_prediction_evaluation_plan_###_###.md
```

Avoid outcome-aware renaming of preregistered artifacts after results are known when retaining the original filename better preserves provenance.

---

# Adding a New Methodology File

Before adding a new file, determine:

1. What operational problem does it solve?
2. Is it standing, preregistered, completed, historical, or retrospective?
3. Does an existing file already govern the issue?
4. Is it being written before or after outcome access?
5. What evidence layer does it constrain?
6. Does it create unnecessary maintenance?
7. Which navigation surfaces must link to it?
8. Does it require a changelog entry?
9. Does it require validator changes?
10. Does it change protocol, prediction, phase, or release status?

---

# Current Methodology State

As of 2026-09-10:

```text
Data collection:
Active standing methodology

Public artifact sanitization:
Active standing methodology

Prediction evaluation:
Active standing methodology

Records 041–044 preregistration artifact:
Completed / preserved unchanged for provenance

Record 041:
Closed / supported

Record 042:
Closed / not supported — continued_adaptation

Record 043:
Closed / not supported — overall_improvement_not_met
Error direction: over

Record 044:
Closed / not supported — narrow snapshot-directed governance deviation

Record 045 evaluation plan:
Completed / preserved for provenance

Record 045:
Closed / supported

Record 046 evaluation plan:
Completed / preserved for provenance

Record 046:
Closed / not supported — failed_autonomic_recompression
Error direction: over

August 2026 snapshot collection plan:
Collection complete; retained for execution comparison and provenance

August physical source artifacts:
Archived and checksum-governed

August TruDiagnostic provider-result artifacts:
Archived and checksum-governed

August TruDiagnostic source-role reconciliation:
Complete — contemporaneous 2026-08-17 05:37 local collection record controls event timing/preparation conditions

Open protected model-error records 041–046:
None

Canonical phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
Undeclared

Underlying physical protocol:
B1 + Load Integration preserved
```

Current weekly and machine-readable coverage details are intentionally not duplicated here; use [`../LATEST.md`](../LATEST.md) and [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

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
- [`../data/model_error/record_043_closure.md`](../data/model_error/record_043_closure.md)
- [`../data/model_error/udi_by_type_tracker.csv`](../data/model_error/udi_by_type_tracker.csv)
- [`../data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](../data/source_provenance/2026-08-trudiagnostic-reconciliation.md)
- [`../PHASE_MAP.md`](../PHASE_MAP.md)
- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)
- [`../VERIFICATION.md`](../VERIFICATION.md)
- [`../CHANGELOG.md`](../CHANGELOG.md)
- [`../docs/methodology/`](../docs/methodology/)

---

## Version Note

On 2026-09-10 this directory guide was consolidated after completion of the August molecular-source integration and Model Error 043 adjudication.

The consolidation:

- preserves all preregistered methodology artifacts unchanged
- records the completed 041–046 lifecycle state
- records 043 as closed / not supported with `error_direction=over`
- links the separate 043 closure and TruDiagnostic source-role reconciliation records
- removes stale duplicated pending/open state from the current-facing directory guide
- reduces repeated volatile weekly/coverage state in favor of `LATEST.md` and `data/DATA_COVERAGE.md`
- preserves Phase 2 — Load Integration, the consolidation / lock-in observation substate, and the underlying B1 + Load Integration architecture
- introduces no biological-value correction, protocol change, phase declaration, release increment, or DOI change

Earlier directory-guide states and their dated transitions remain inspectable in Git history and `CHANGELOG.md`.
