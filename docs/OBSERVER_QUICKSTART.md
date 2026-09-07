# Observer Quickstart

This is the shortest technical inspection route for researchers, data reviewers, engineers, or skeptical readers.

The goal is not to summarize everything. The goal is to test whether the archive's claims, data, provenance, interpretation, and governance remain coherent when inspected from the bottom up.

---

## 1. Establish Scope

Read:

- [`../README.md`](../README.md)
- [`START_HERE.md`](./START_HERE.md)
- [`../ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)

Confirm that the archive describes itself as a single-subject observational system under incomplete environmental control rather than a clinical trial or generalized intervention protocol.

---

## 2. Inspect Current State

Read:

[`../LATEST.md`](../LATEST.md)

Check that current phase, active report, open predictions, pending snapshot evidence, and current data coverage are separated from historical results and future expectations.

---

## 3. Inspect Machine-Readable Coverage

Read:

- [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)
- [`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)

Then inspect the core structured files:

- [`../data/daily_biomarkers_v1.csv`](../data/daily_biomarkers_v1.csv)
- [`../data/sleep_longitudinal_v1.csv`](../data/sleep_longitudinal_v1.csv)
- [`../data/training_blocks_v1.csv`](../data/training_blocks_v1.csv)
- [`../data/context_events_v1.csv`](../data/context_events_v1.csv)

Use [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md) for current row counts and endpoints; they are intentionally not duplicated here.

Check whether:

- identifiers are stable
- missingness remains visible
- subjective and measured fields are distinguishable
- context classification is bounded
- historical duration expressions preserve uncertainty rather than invent precision
- row-level `source_ref` values remain present

---

## 4. Inspect Source Provenance

For direct provider/device evidence, inspect:

[`../data/source_exports/`](../data/source_exports/)

For curated rows derived from private `Daniel_Dataset_v1.x` sources, inspect:

[`../data/source_provenance/`](../data/source_provenance/)

The private-source manifest registers SHA-256 only when the exact retained private file was available. A missing hash is intentionally left missing rather than reconstructed.

---

## 5. Inspect One Closed Report and Its Evidence

Open the most recent closed report:

[`../reports/2026-W35.md`](../reports/2026-W35.md)

Then compare its material values with the applicable structured datasets.

Ask whether the report:

- interprets retrospectively
- preserves unfavorable signals
- distinguishes daily HRV from sleep HRV
- distinguishes resting from sleeping heart rate
- avoids treating one subjective observation as a declared phase transition
- remains proportional to the underlying rows

---

## 6. Inspect One Snapshot

Use:

- [`../snapshots/`](../snapshots/)
- [`../SNAPSHOT_LOG.md`](../SNAPSHOT_LOG.md)
- [`../EPOCH_INDEX.md`](../EPOCH_INDEX.md)
- [`../methodology/2026-08-snapshot-collection-plan.md`](../methodology/2026-08-snapshot-collection-plan.md)

Check source identity, timing, preparation conditions, checksum coverage, missingness, and whether interpretation remains distinct from artifact preservation.

---

## 7. Inspect Prediction Accountability

Read:

- [`../data/model_error/WHAT_THIS_LAYER_IS.md`](../data/model_error/WHAT_THIS_LAYER_IS.md)
- [`../data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)
- [`../docs/methodology/valid_prediction_criteria.md`](../docs/methodology/valid_prediction_criteria.md)

Check whether predictions were logged before their relevant outcomes, remained bounded and falsifiable, and stayed visible when wrong.

For future model-error schema semantics, see:

[`../docs/methodology/model_error_schema_v2.md`](../docs/methodology/model_error_schema_v2.md)

---

## 8. Inspect Governance

Read:

- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)
- [`../PHASE_MAP.md`](../PHASE_MAP.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)

Look for whether corrections, phase decisions, prediction closure, and source conflicts are handled under declared rules rather than outcome preference.

---

## 9. Run Validation

Core mechanical/governance validator:

```text
python tools/validate_repository.py
```

Machine-readable semantic validator:

```text
python tools/validate_machine_readable.py
```

See [`../tools/README.md`](../tools/README.md).

The GitHub Actions workflow runs both validators on pushes to `main` and pull requests.

A validator pass is not a biological-validity claim.

---

## 10. Inspect AI-Assistance Boundary

Read:

[`AI_ASSISTANCE.md`](./AI_ASSISTANCE.md)

AI can assist with structuring, analysis, drafting, code, and governed prediction generation, but it is not an evidence source and cannot override the archive's source hierarchy.

---

## Quick Audit Sequence

```text
README / START_HERE
        ↓
LATEST
        ↓
DATA_COVERAGE
        ↓
machine-readable schema + core CSVs
        ↓
source provenance / source exports
        ↓
one closed report + one snapshot
        ↓
model-error layer
        ↓
governance
        ↓
validators
```

---

## Evaluation Principle

A strong review should move:

```text
evidence
→ structure
→ interpretation
```

not:

```text
narrative
→ search for supporting evidence
```

For the broader observer path, see [`FOR_OBSERVERS.md`](./FOR_OBSERVERS.md). For complete navigation, use [`../INDEX.md`](../INDEX.md).
