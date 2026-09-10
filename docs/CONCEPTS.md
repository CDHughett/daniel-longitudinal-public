# Concepts

This glossary defines recurring terms used throughout the Daniel Longitudinal Study.

It improves external legibility but does not independently declare a phase, score a prediction, correct a dataset, establish causality, or authorize protocol progression.

Canonical phase architecture is defined in [`../PHASE_MAP.md`](../PHASE_MAP.md).

---

# Evidence and Archive Concepts

## Observation

Something recorded about the subject, environment, protocol, or measurement system.

An observation may be provider-generated, device-generated, manually transcribed, subjective, narrative, or classified.

Observation does not automatically establish interpretation.

## Artifact

A preserved file or record supporting an observation, such as a provider report, screenshot, source export, structured dataset, weekly report, checksum manifest, or audit file.

Artifacts vary in source strength.

## Artifact-First

Preserve evidence before final interpretation whenever practical:

```text
observation
→ artifact/source preservation
→ quality review
→ interpretation
```

Artifact-first does not mean every artifact is error-free.

## Collection Layer

The near-time capture layer for wearable values, bodyweight, subjective state, training notes, testing context, screenshots, and other contemporaneous evidence.

## Archive Layer

The durable organization layer: datasets, reports, snapshots, source exports, prediction records, audits, and governance documents.

## Interpretation Layer

The layer that evaluates what accumulated evidence may mean. Interpretation remains subordinate to source quality, comparability, missingness, contradictions, and alternative explanations.

---

# Source and Data Concepts

## Source Artifact

The closest preserved representation of a measurement or externally generated record, such as a provider PDF, DEXA output, Bod Pod output, laboratory report, or direct RingConn export.

## Source State

The value supplied by a particular evidence pathway at a particular time.

Two source states for one date may differ because of provider recalculation, rounding, date assignment, aggregation, manual transcription, or software behavior.

A difference is investigated rather than silently forced into agreement.

## Curated Structured Dataset

An archive-defined machine-readable file created from governed sources under an explicit schema.

Current examples include:

- `data/daily_biomarkers_v1.csv`
- `data/sleep_longitudinal_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`
- `data/biomarker_snapshot.csv`
- `data/epigenetic_longitudinal.csv`
- `data/bloodwork_longitudinal.csv`
- `data/model_error/model_error_gap_v1.csv`

A curated value remains subordinate to stronger verified source evidence if a source-backed discrepancy is established.

## Source-Preserved Export

A provider/device export retained in its original byte representation.

It preserves the provider state and is not automatically the canonical analytical dataset.

## `source_ref`

A row-level provenance locator used by the current machine-readable daily/training/event layer.

It identifies a source pathway/version/tab/date and, where applicable, a session/row label.

It is not a checksum.

Canonical syntax and accepted historical training aliases are defined in [`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md).

## Private Source Provenance

Public documentation that records identity and extraction relationships for private source files without publishing those files.

Current private Daniel Dataset provenance lives in [`../data/source_provenance/`](../data/source_provenance/).

Exact-file SHA-256 is recorded only when the retained historical file was actually available for hashing.

## Machine-Readable Core

The aligned structured layer currently combining:

```text
daily biomarkers
+
canonical sleep
+
training sessions
+
context events
+
model-error outcomes
```

The files have different units of observation and should not be treated as row-for-row equivalent.

---

# Field Evidence Concepts

## Measurement / Source-Transcribed Field

A numeric or categorical value copied from a governed measurement/source field.

This classification describes provenance, not clinical validity.

## Subjective Field

A contemporaneous operator-reported state, such as mood, energy, GI state, pain, or execution texture.

Subjective data may be structured without becoming objective measurement.

## Contextual / Classified Field

An archive label used to organize preserved context, such as `context_tags`, equipment state, protocol status, event type, or event impact.

Classification should remain bounded by source evidence and must not create causal certainty.

## Provenance Field

A field describing where a row or value came from, such as `source_ref`.

---

# Missingness and Correction

## Missingness

Absence of a governed value.

Missing does not mean zero, normal, no event, or no device wear.

Missing values remain missing unless source-backed evidence supports correction or later structured inclusion.

## Source-Backed Correction

A narrow correction made because identifiable stronger source evidence establishes that a recorded value, label, date, or representation is inaccurate.

Correction preserves prior repository state through Git history and is not new biological evidence.

## Source Reconciliation

The process of comparing competing source states under the archive hierarchy and determining whether one controls, the conflict remains unresolved, or a narrow correction is justified.

---

# Reporting and State Concepts

## Active Report

An open weekly collection surface.

It may contain contemporaneous observations and candidate evidence but must not present the unfinished window as a closed retrospective outcome.

## Closed Report

A completed weekly or event report interpreted retrospectively after the observation boundary ends.

## Candidate Evidence

An observation that may be relevant to an open prediction, future operating substate, or phase review but does not independently determine an outcome.

## Current State

The presently declared archive/system posture, summarized in [`../LATEST.md`](../LATEST.md).

Current state should not be inferred from an old report or historical audit.

---

# Training and Behavioral Concepts

## B1

The recurring aerobic anchor in the current Phase 2 architecture.

## Load Integration

The recurring structured resistance/movement layer currently paired with B1.

The public `training_blocks_v1.csv` now provides a machine-readable session layer for these and historical training blocks.

## Ambient Execution

Execution that occurs with reduced conscious management or attentional salience under the established behavior.

It is a descriptive behavioral observation, not a clinical state or automatic phase declaration.

## Trait-Like Execution

Repeated behavior-specific execution that appears increasingly stable and low-overhead across time/context.

The term does not mean immutable trait or universal transferability.

## Trait-Level Expression

A stronger session-level descriptive label used when execution appears deeply embedded across the observed session context.

It remains an observation unless separately incorporated into retrospective phase review.

## Operator Overhead

The active cognitive/behavioral management cost required to initiate, sequence, pace, or maintain a practiced behavior.

Reduced operator overhead is descriptive evidence of behavioral consolidation, not proof of a specific neurological mechanism.

## Portability

Preserved execution across a changed context such as equipment, room, schedule, travel, or ordinary-life workload.

Natural portability evidence is preferred to manufactured proof tests.

---

# Context and Perturbation Concepts

## Context Tag

A compact `snake_case` label attached to a daily or training row.

It is descriptive and does not automatically create a formal event.

## Context Event

A bounded event in `data/context_events_v1.csv` whose inclusion materially improves interpretation of training availability, recovery, testing, protocol state, portability, prediction evaluation, or source reconciliation.

The event dataset is an index, not a complete diary.

## Perturbation

A meaningful change in ordinary conditions such as travel, illness, schedule displacement, environmental exposure, equipment access, or unusual physical workload.

Perturbations need not be deliberately engineered.

## Absorbed

A retrospective context-event outcome indicating that the event occurred without a persistent observed loss of ordinary function within the represented window.

It does not mean the event had zero physiological effect.

---

# Phase Concepts

## Phase

A retrospectively declared operating architecture defined under `PHASE_MAP.md` and `PHASE_DECLARATION_CRITERIA.md`.

Current phase:

```text
Phase 2 — Load Integration
```

## Operating Substate

A descriptive mode within the active phase.

Current operating substate:

```text
Consolidation / lock-in observation
```

## Phase 2D-Type Characteristic

An observation resembling a possible future Phase 2D criterion.

It does not mean Phase 2D is active or inevitable.

## Phase 2D

A reserved possible retrospective substate within Phase 2 describing durable, portable, low-overhead expression of installed capacity.

Formal Phase 2D remains undeclared.

## Phase Declaration

A retrospective archive decision requiring closed observation, supporting evidence, contradictory-evidence review, recovery/mechanical compatibility, governance review, and explicit documentation.

---

# Prediction and Calibration Concepts

## Prediction

A forward expectation intended for evaluation.

Clean prospective prediction records are registered before relevant outcome access, bounded, observable, falsifiable, and preserved without hindsight revision.

## Model Error

A material difference between registered expectation and observed outcome.

Model error is evidence about the prediction/model, not automatically evidence of biological deterioration.

## Error Direction

For eligible records:

- `under` — the model underestimated the observed result/state in the defined comparison
- `over` — the model overestimated it
- `none` — no directional error under the applicable rule

Meaning remains domain-specific.

## Registration Provenance

Whether and how a prediction was fixed relative to outcome access.

For the protected recent records 041–046, `calibration_state=pre` is preserved as historical prospective-registration provenance.

## Model Calibration Scope

How much prior subject-specific information informed the model generating the prediction.

This is conceptually distinct from registration provenance.

The future model-error schema separates these concepts explicitly in [`methodology/model_error_schema_v2.md`](./methodology/model_error_schema_v2.md).

## UDI

UDI means **Unobstructed Delta Index**.

It is an experimental signed directional prediction-error framework for eligible magnitude-based records.

Current canonical reporting is stratified:

- `UDI_point`
- `UDI_range`
- `State_concordance`
- `Trajectory_concordance`

State and trajectory predictions are excluded from magnitude UDI because they do not contain directly comparable continuous error magnitudes.

Composite UDI remains withheld under the framework's predefined release criteria.

UDI is not a biological score.

## Concordance

Agreement between a state/trajectory prediction and its governed outcome classification.

Concordance is a calibration signal, not certainty.

---

# Validation and Governance Concepts

## Mechanical Validation

Read-only checks of repository structure, links, CSV parsing, checksum manifests, continuity, and protected state.

## Machine-Readable Validation

Read-only semantic checks specific to daily/training/event datasets: identifiers, dates, vocabularies, numeric syntax, source references, event intervals, and cross-file relationships.

Tool:

`tools/validate_machine_readable.py`

## Semantic Review

Human/model-assisted review of whether fields, interpretations, state language, and source relationships actually mean what the repository claims they mean.

Mechanical validation cannot replace semantic review.

## Governance Miss

Failure of a declared operational/governance condition.

A governance miss does not automatically imply biological harm.

---

# AI Assistance

## AI-Assisted Maintenance

Use of an AI/LLM to help structure source-backed data, draft documentation, calculate summaries, identify inconsistencies, write validation code, or support audits.

AI assistance is not a source-evidence class.

## AI-Generated Prediction

A prediction generated with AI assistance that enters the governed model-error layer only if it independently satisfies prospective registration and evaluation rules.

Model version may be retained as part of the audit trail.

AI disclosure:

[`AI_ASSISTANCE.md`](./AI_ASSISTANCE.md)

---

# Current Terminology State

As of the current September 2026 archive state:

```text
Active phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
undeclared

Current open model-error records:
none in protected block 041–046

Recently closed model-error records:
041, 042, 043, 044, 045, 046

Record 043:
closed / not supported — overall_improvement_not_met / over

UDI canonical name:
Unobstructed Delta Index
```

Current machine-readable row counts and endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

Historical documents may retain terminology that was correct for their original date/state.

Current-facing documents should use the definitions in this glossary and the governing schema/methodology files.
