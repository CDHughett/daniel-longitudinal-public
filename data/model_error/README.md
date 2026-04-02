# Model Error Data Layer

---

## Purpose

This layer measures the gap between prediction and observed outcome.

It exists to record prediction → outcome relationships as an auxiliary analytical layer within the archive.

The goal is not to prove correctness.
The goal is to preserve prediction → outcome → error as a reviewable structure.

---

## Data Structure

The model error layer is split into two distinct datasets:

### `model_error_gap_v1.csv`
Forward-logged prediction records only.

This file is the primary evaluation dataset and is the only file used for ongoing calibration analysis inside the archive.

### `model_error_gap_reconstructed.csv`
Retrospective baseline records.

These entries were reconstructed after outcomes were already known in order to document an early baseline error profile before the forward-logging layer was fully established.

These records are retained for historical context only.

They are **not** treated as forward-test artifacts and should **not** be used as evidence of predictive integrity or calibration quality.

---

## Core Principle

Only predictions logged before outcomes are known qualify for the primary evaluation layer.

This distinction matters.

The archive preserves reconstructed baseline records for transparency, but forward-logged records and retrospective records are not methodologically equivalent.

---

## What This Layer Tests

For eligible forward-logged predictions, this layer tracks:

- whether the prediction resolved cleanly
- whether the prediction under- or overestimated observed reality
- whether error magnitude improved over time
- whether subject-calibrated expectations outperform generic assumptions

---

## Primary Fields

Each row may include:

- `prediction_value`
- `actual_value`
- `error_absolute`
- `error_direction`
- `error_pct`
- `model_type`
- `calibration_state`
- `flag`
- `prediction_type`
- `status`
- `notes`

---

## Flag Definitions

### `primary`
A forward-logged prediction entered before the outcome was known.

### `secondary`
A forward-logged prediction that is still valid but not treated as a primary calibration anchor.

### `reconstructed`
A retrospective record created after the outcome was already known.

### `inferred`
A retrospective record created from prior reasoning or archived discussion after the outcome was already known.

`reconstructed` and `inferred` records belong in the reconstructed baseline file, not the primary evaluation file.

---

## Prediction Types

### `point`
A specific numerical estimate.

### `range`
A bounded expected interval.

### `state`
A binary or condition-based expectation.

### `trajectory`
A directional prediction expected to resolve across a longer observation window.

---

## Inclusion Standard for `model_error_gap_v1.csv`

A prediction belongs in the primary file only if it is:

1. forward-logged before outcome is known
2. time-bounded
3. observable using archive data
4. falsifiable
5. assigned to a defined domain
6. independently resolvable
7. sufficiently documented to support closure

If any of these conditions are not met, the record does not belong in the primary evaluation file.

---

## Closure Rules

A prediction may be closed only when:

1. the observation window has elapsed, and
2. enough evidence exists to evaluate the outcome without forced interpretation

Status values:

- `open`
- `closed`

When ambiguity remains, the prediction should stay open.

---

## Evaluation Standard

Scoring and closure logic are defined in:

- `/methodology/prediction_evaluation.md`
- `/docs/methodology/prediction_to_outcome_pipeline.md`
- `/docs/methodology/valid_prediction_criteria.md`

This README does not duplicate those rules.

---

## Calibration Boundary

`calibration_events_log.md` documents major shifts in how prediction behavior should be interpreted across time.

This supports distinction between:

- general-population assumptions
- subject-calibrated expectations

---

## Archive Posture

This layer is strongest when it remains narrow, explicit, and honest.

A smaller forward-logged dataset with clean temporal integrity is more valuable than a larger dataset with mixed methodological status.
