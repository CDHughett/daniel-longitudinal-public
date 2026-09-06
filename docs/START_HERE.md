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

## Machine-Readable Core

The current aligned structured layer includes:

| Dataset | Current public coverage |
|---|---|
| [`data/daily_biomarkers_v1.csv`](../data/daily_biomarkers_v1.csv) | 203 continuous daily rows through 2026-08-30 |
| [`data/sleep_longitudinal_v1.csv`](../data/sleep_longitudinal_v1.csv) | 203 continuous daily rows through 2026-08-30 |
| [`data/training_blocks_v1.csv`](../data/training_blocks_v1.csv) | 325 session rows through 2026-08-30 |
| [`data/context_events_v1.csv`](../data/context_events_v1.csv) | 42 bounded contextual events through 2026-08-29 |

The three daily/training/event files are governed by:

[`schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)

Private `Daniel_Dataset_v1.x` source-file provenance is documented in:

[`data/source_provenance/`](../data/source_provenance/)

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

Read-only validation tools:

```text
tools/validate_repository.py
tools/validate_machine_readable.py
```

GitHub Actions runs both on pushes to `main` and on pull requests.

See [`tools/README.md`](../tools/README.md) and [`VERIFICATION.md`](../VERIFICATION.md).

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
