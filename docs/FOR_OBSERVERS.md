# For Observers

This is the broader skeptical and technical review path for the Daniel Longitudinal Study.

For the shortest route, see [`OBSERVER_QUICKSTART.md`](./OBSERVER_QUICKSTART.md).

---

## What You Are Looking At

This repository is an active single-subject longitudinal archive under continuous observation, retrospective interpretation, explicit correction governance, and isolated prospective prediction testing.

It is not:

- a completed scientific framework
- a clinical trial
- a generalized protocol
- a coaching product
- a performance-marketing archive

Its appropriate evaluation target is the coherence among:

```text
source evidence
→ curated data
→ contemporaneous context
→ retrospective interpretation
→ registered prediction evaluation
→ model correction
```

---

## Current Machine-Readable Core

The current public structured layer contains:

- [`daily_biomarkers_v1.csv`](../data/daily_biomarkers_v1.csv)
- [`sleep_longitudinal_v1.csv`](../data/sleep_longitudinal_v1.csv)
- [`training_blocks_v1.csv`](../data/training_blocks_v1.csv)
- [`context_events_v1.csv`](../data/context_events_v1.csv)

Live row counts and coverage endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md). The schema is defined in [`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md).

This materially improves machine readability, but it does not make the archive exhaustive or experimentally controlled.

---

## Governing Distinctions

### Source Artifact Versus Curated Dataset

A provider report/export or other verified source artifact occupies a different evidentiary layer from a curated CSV row.

When a source-backed discrepancy is established, stronger source evidence governs under the declared source hierarchy.

A CSV is not automatically correct because it parses successfully.

### Measurement Versus Subjective State

The daily structured layer includes both source-transcribed measurements and bounded subjective fields.

The schema explicitly labels evidence classes so consumers do not silently convert subjective state into objective measurement.

### Context Tag Versus Context Event

Daily/training `context_tags` provide compact contextual labels.

`context_events_v1.csv` is a narrower bounded event index. It does not duplicate every tag or every ordinary-life occurrence.

An event row is created only when the context materially improves interpretation of training, recovery, testing, protocol state, portability, prediction evaluation, or source reconciliation.

### Observation Versus Interpretation

An active report may preserve observations while a window is open.

Final weekly interpretation remains retrospective after closeout.

### Planning Versus Prediction

Operational planning may be forward-looking.

Physiological/performance predictions intended for evaluation belong in the governed model-error layer and must be registered before the relevant outcome boundary.

### Candidate Evidence Versus Outcome

An observation can be relevant to an open prediction or future phase without resolving it.

Candidate evidence does not automatically pass/fail a prediction, close a record, authorize protocol progression, or declare a phase.

### Correction Versus Rewriting

The archive permits narrow source-backed correction and prohibits outcome-driven rewriting.

Historical repository states remain visible through Git history.

---

## How to Inspect the Data

Read:

- [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- [`../DATA_DICTIONARY.md`](../DATA_DICTIONARY.md)
- [`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)

Then inspect the relevant CSVs directly.

Ask:

- Are identifiers unique and stable?
- Are date semantics clear?
- Is missingness visible?
- Are source-transcribed, subjective, and classified fields distinguishable?
- Are units explicit?
- Does `source_ref` identify the source pathway?
- Do context classifications remain descriptive rather than causal?
- Does historical uncertainty remain visible rather than being normalized into false precision?

### Training Duration Caveat

In `training_blocks_v1.csv`, the v1 field `duration_min` is a **source-preserving duration expression**, not a uniformly numeric field.

Scalar values can be treated as minutes. Historical ranges and compound expressions must not be converted to a point value without a separately documented transformation.

---

## How to Inspect Provenance

### Public Provider/Device Sources

Use:

[`../data/source_exports/`](../data/source_exports/)

The RingConn acquisition package preserves original provider bytes and checksum identity separately from the curated daily datasets.

### Private Daniel Dataset Sources

Use:

[`../data/source_provenance/`](../data/source_provenance/)

The public row-level `source_ref` identifies private source version/tab/date. The private-source manifest registers file-level SHA-256 only for exact retained files that were actually available for hashing.

Missing private hashes remain missing; they are not reconstructed from screenshots, later workbooks, or extracted rows.

Private source omission reduces complete external reproducibility for those rows, and that limitation should remain visible.

---

## How to Evaluate Closed Reports

A closed weekly report may summarize:

- training exposure
- recovery behavior
- sleep
- bodyweight
- contextual perturbations
- mechanical observations
- candidate phase evidence
- model-error relevance

Observers should check whether reported arithmetic and qualitative claims remain consistent with the underlying rows and whether unfavorable signals are preserved.

Reports should organize evidence, not create it.

---

## How to Evaluate Snapshots

Snapshot review should consider:

- provider/source identity
- collection date/time
- preparation conditions
- privacy handling
- checksum presence
- comparability with earlier tests
- missing pages/fields
- transcription accuracy
- software/algorithm changes
- whether an artifact is primary, derived, or redacted

A checksum establishes file identity, not clinical validity or measurement accuracy.

---

## Prediction and Model-Error Review

Read:

- [`../data/model_error/WHAT_THIS_LAYER_IS.md`](../data/model_error/WHAT_THIS_LAYER_IS.md)
- [`../data/model_error/README.md`](../data/model_error/README.md)
- [`../data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)
- [`methodology/valid_prediction_criteria.md`](./methodology/valid_prediction_criteria.md)

The strongest prediction records are those that were:

- logged before the relevant outcome
- time/state bounded
- observable
- falsifiable
- sufficiently specific
- preserved after registration
- left open when evidence was insufficient
- retained when wrong

A correct prediction is not scientific authority. A wrong prediction is not an archive defect when it is preserved and used for calibration.

---

## UDI

UDI canonically means **Unobstructed Delta Index**.

The current framework evaluates signed directional prediction error for eligible magnitude-based prediction classes.

Current reporting is stratified:

- `UDI_point`
- `UDI_range`
- `State_concordance`
- `Trajectory_concordance`

State and trajectory predictions are not forced into magnitude UDI because they do not provide continuous magnitude error in the same way.

Composite UDI remains withheld under the framework's predefined sample-size criteria.

UDI is a model-calibration construct, not a biological score.

See:

[`methodology/UDI_framework_v1.md`](./methodology/UDI_framework_v1.md)

---

## Model-Error Schema Semantics

The v1 field `calibration_state` accumulated historical semantic debt because registration provenance and subject-specific model calibration are separate concepts.

For the protected recent prospective records, `calibration_state=pre` records prospective registration provenance and remains unchanged after closure.

A future schema design separates:

```text
registration_status
```

from:

```text
model_calibration_scope
```

See:

[`methodology/model_error_schema_v2.md`](./methodology/model_error_schema_v2.md)

That design document does not migrate, rescore, or rewrite existing records.

---

## AI Assistance

AI/LLM systems may assist with source-backed structuring, drafting, analysis, validator code, audits, and formally governed prediction generation.

AI output is not a source-evidence class.

It may not invent missing observations, fabricate provenance, override verified source artifacts, rewrite protected predictions, or strengthen claims beyond the evidence.

Disclosure:

[`AI_ASSISTANCE.md`](./AI_ASSISTANCE.md)

---

## Validation

Current read-only validators:

```text
tools/validate_repository.py
tools/validate_machine_readable.py
```

The first checks repository mechanics and selected governance-protected state.

The second checks the machine-readable daily/training/event layer for identifier, date, vocabulary, duration-expression, source-reference, event-interval, and cross-file relationship rules.

GitHub Actions runs both on pushes to `main` and pull requests.

A validator pass means the implemented checks passed. It does not establish biological plausibility, causality, or clinical validity.

---

## Environmental-Control Boundary

The archive operates under ordinary-life conditions with selected stabilized inputs rather than laboratory isolation.

Relevant unmeasured or incompletely measured factors may include:

- travel
- schedule displacement
- household workload
- social demands
- altered sleep environment
- hydration/sodium variation
- nutrition variation
- illness/irritation
- equipment access
- environmental exposure
- device/provider behavior
- unmeasured biological fluctuation

Context may explain uncertainty; it should not be used to excuse every unfavorable outcome.

---

## Phase Review

Phase language is retrospective.

Observers should distinguish:

```text
candidate characteristic
→ accumulated transition evidence
→ retrospective declaration
```

from an aspirational progression narrative.

Current public posture remains Phase 2 — Load Integration, consolidation/lock-in observation, with Phase 2D undeclared.

---

## What a Skeptical Observer Should Test

A skeptical review should ask whether:

- source artifacts remain traceable
- machine-readable rows preserve provenance
- missingness remains visible
- active reports remain provisional
- closed reports remain retrospective
- source corrections are documented
- unfavorable observations persist in the record
- prediction wording survives outcome access
- fixed scoring windows stay fixed
- phase claims remain proportional
- private-source limitations are acknowledged
- AI assistance is disclosed without granting AI source authority
- validator checks are reproducible
- documentation agrees with the live data architecture

Warning signs would include silent value changes, invented missing data, vague post-outcome prediction wording, dashboard claims stronger than the sources, manufactured perturbations presented as natural evidence, or administrative complexity that no longer improves traceability.

---

## Recommended Review Path

```text
README
  ↓
LATEST
  ↓
DATA_COVERAGE
  ↓
machine-readable schema + core CSVs
  ↓
source provenance / source exports
  ↓
DATA_QUALITY_NOTES
  ↓
one closed report + one snapshot
  ↓
model-error layer
  ↓
governance
  ↓
validators
```

For complete navigation, use [`../INDEX.md`](../INDEX.md).

---

## Status

**Public archive:** Active
**Structured-data posture:** Daily/session/event machine-readable core active
**Interpretation model:** Retrospective and artifact-bound
**Prediction model:** Registered and isolated
**UDI canonical name:** Unobstructed Delta Index
**Environmental posture:** Defined protocol constraints with incomplete control
**Correction posture:** Source-backed and traceable
**AI-assistance posture:** Disclosed, subordinate to source evidence
**Phase posture:** Retrospectively declared
**Validation posture:** Local read-only validation + lightweight CI + human semantic review
