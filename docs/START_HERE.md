# START HERE

This is the 5-minute orientation for the Daniel Longitudinal Study.

---

## In One Sentence

This is a governed, DOI-preserved, single-subject longitudinal observational archive documenting one human system across time through source artifacts, machine-readable data, retrospective interpretation, and prospectively registered prediction review.

---

## What This Is

- a public longitudinal archive
- a single-subject observational record
- a versioned evidence structure
- a machine-readable longitudinal data layer
- a retrospective interpretation system
- a prediction-audit and calibration record
- a governed archive of repeated measurement, observation, correction, and review

## What This Is Not

- not a protocol recommendation
- not a coaching product
- not a clinical study
- not a universal longevity claim
- not a theory-first archive
- not proof that one intervention caused every observed change

---

## What To Read First

1. [`README.md`](../README.md) — repository overview and current archive posture
2. [`LATEST.md`](../LATEST.md) — current system state
3. [`data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md) — what is and is not publicly structured
4. [`docs/OBSERVER_QUICKSTART.md`](./OBSERVER_QUICKSTART.md) — compact technical inspection route
5. [`docs/FOR_OBSERVERS.md`](./FOR_OBSERVERS.md) — broader skeptical-review path
6. [`docs/CONCEPTS.md`](./CONCEPTS.md) — recurring archive terminology

For the complete repository map, use [`INDEX.md`](../INDEX.md).

---

## How The Current State Labels Fit Together

The archive uses several state labels at different levels. They are not competing phase names.

```text
declared phase
Phase 2 — Load Integration
        ↓
broader operating substate
Consolidation / lock-in observation
        ↓
weekly operating posture
Consolidation / reserve-replication observation
        ↓
session-level observations
ambient / trait-like / trait-level execution, reserve evidence, etc.
```

In plain language:

- the **phase** is the largest declared operating architecture
- the **broader substate** describes how that phase is currently being expressed over a longer window
- the **weekly operating posture** is the narrower question being watched right now
- **session-level observations** describe what happened in particular sessions or contexts

Evidence at a lower level does not automatically promote the level above it. For example, one reserve observation does not automatically change the weekly prescription, declare a new substate, or create a new phase.

Recurring terms are defined in [`docs/CONCEPTS.md`](./CONCEPTS.md).

---

## Machine-Readable Core

The current aligned structured layer includes:

- [`data/daily_biomarkers_v1.csv`](../data/daily_biomarkers_v1.csv)
- [`data/sleep_longitudinal_v1.csv`](../data/sleep_longitudinal_v1.csv)
- [`data/training_blocks_v1.csv`](../data/training_blocks_v1.csv)
- [`data/context_events_v1.csv`](../data/context_events_v1.csv)

Live row counts and coverage endpoints are maintained in [`data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

Schema: [`schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)
Private-source provenance: [`data/source_provenance/`](../data/source_provenance/)

---

## Where The Evidence Lives

- [`snapshots`](../snapshots/) — primary testing and measurement artifacts
- [`data`](../data/) — curated machine-readable longitudinal datasets
- [`data/source_exports`](../data/source_exports/) — byte-preserved provider/device exports
- [`data/source_provenance`](../data/source_provenance/) — private-source provenance without publishing private workbooks
- [`reports`](../reports/) — active collection and closed retrospective interpretation
- [`data/model_error`](../data/model_error/) — prediction versus observed-outcome review
- [`docs`](./) and [`methodology`](../methodology/) — governance, methodology, concepts, observer guidance, and audits

Artifacts and source evidence precede interpretation.

Structured datasets organize evidence; they do not silently override stronger verified sources.

---

## How Claims Are Limited

No claim extends beyond the recorded single-subject archive without separate evidence.

The repository does not claim laboratory-grade control, population-level efficacy, or universal transferability.

Missingness remains visible. Unfavorable evidence remains visible. Source-backed corrections remain traceable. Closed predictions remain closed.

---

## Verification

The repository maintains a current read-only validation suite under [`tools/README.md`](../tools/README.md).

GitHub Actions runs the current suite on pushes to `main` and on pull requests.

For validator roles, local execution, scope, and limitations, see [`VERIFICATION.md`](../VERIFICATION.md).

---

## AI Assistance

AI may assist with repository maintenance, structuring, code, analysis, and formally governed prediction work, but AI output is not a source-evidence class and cannot override the archive's source hierarchy.

Disclosure:

[`docs/AI_ASSISTANCE.md`](./AI_ASSISTANCE.md)

---

## Recommended Navigation By Depth

- [`docs/START_HERE.md`](./START_HERE.md) — first 5 minutes
- [`docs/OBSERVER_QUICKSTART.md`](./OBSERVER_QUICKSTART.md) — compact technical audit route
- [`docs/NEWCOMER_PATH.md`](./NEWCOMER_PATH.md) — extended first reading pass
- [`docs/FOR_OBSERVERS.md`](./FOR_OBSERVERS.md) — skeptical/technical evaluation guidance
- [`INDEX.md`](../INDEX.md) — complete repository map

---

## Public Posture

Traceable.
Conservative.
Machine-readable.
Auditable.
Longitudinal.
Artifact-first.
