# Prediction Evaluation Methodology

Daniel Longitudinal Study  
Prediction Evaluation Standard

---

## Purpose

This document defines how eligible predictions are evaluated once their observation windows close.

Its purpose is to ensure that:

- prediction closure is repeatable
- error assignment is auditable
- prediction types are evaluated consistently
- forward-logged records are distinguished from retrospective baseline records

This methodology primarily applies to:

- `data/model_error/model_error_gap_v1.csv`

It may also be referenced when annotating retrospective baseline records, but those records should not be treated as equivalent evaluation evidence.

---

## Evaluation Eligibility

A record is eligible for primary evaluation only if it was:

- logged before the outcome was known
- assigned a defined observation window
- structured clearly enough to resolve against observed data

If a record was reconstructed after the outcome was already known, it may still be preserved historically, but it does not carry the same evidentiary weight as a forward-logged prediction.

---

## Prediction Types

Predictions are classified into one of four categories:

1. `point`
2. `range`
3. `state`
4. `trajectory`

Each type is evaluated differently.

---

## 1. Point Predictions

Point predictions specify a single expected value.

### Example
- HRV = 75
- recovery_rate = 48
- VO2 = 49.5

### Closure Rule

When observed data are available:

- `error_absolute = abs(prediction_value - actual_value)`
- `error_direction =`
  - `under` if actual exceeds predicted value
  - `over` if actual falls below predicted value
  - `none` if exact match

### Error Percent

For point predictions:

- `error_pct = error_absolute / prediction_value`

Express as a percentage when appropriate.

---

## 2. Range Predictions

Range predictions specify an expected interval.

### Example
- sleep = 400–460 minutes
- weight = 220–224

### Closure Rule

If the actual value falls:

- within range → `error_absolute = 0`, `error_direction = none`, `error_pct = 0%`
- above upper bound → `error_absolute = actual - upper_bound`, `error_direction = over`
- below lower bound → `error_absolute = lower_bound - actual`, `error_direction = under`

Range predictions should preserve the actual observed value used for closure.

---

## 3. State Predictions

State predictions describe whether a stated condition held across the defined observation window.

### Example
- recovery compatibility preserved
- GI instability emerges
- training continuity maintained

### Closure Rule

- condition holds → `actual_value = 1`, `error_absolute = 0`, `error_direction = none`, `error_pct = 0%`
- condition fails → `actual_value = 0`, `error_absolute = 1`, `error_direction = under`, `error_pct = 100%`

If the predicted state is explicitly negative rather than positive, the closure note should make that logic clear.

---

## 4. Trajectory Predictions

Trajectory predictions describe whether a stated directional change materially occurred across a defined period.

### Example
- movement toward lock-in
- stabilization across 3–10 days
- improved baseline clarity across a withdrawal window

### Closure Rule

Trajectory predictions should remain open until:

- the stated window has elapsed, and
- there is enough observed evidence to determine whether the directional claim materially held

Trajectory closure should be conservative.

If evidence is partial, the record should remain open.

---

## Closure Standard

A prediction may be closed only when:

1. the full observation window has elapsed, and
2. the archive contains enough evidence to resolve the record without forced interpretation

If either condition is missing, the prediction remains open.

When uncertainty persists:

**do not close**

---

## Attribution Notes

Observed outcomes may include confounders.

When a confounder is known and materially relevant:

- closure may still occur
- the confounder should be documented in `notes`
- the evaluator should distinguish between systemic failure and input-driven disturbance where the evidence supports that distinction

This should be done cautiously.

Notes should clarify context, not rescue failed predictions.

---

## Review Use

Primary review judgments should be based on:

- forward-logged records
- closed records
- repeated patterns across domains and time

Reconstructed or inferred retrospective records may be retained for transparency, but they should not be blended into the same evidentiary tier.

---

## Archive Discipline

This methodology favors:

- delayed closure over forced closure
- traceability over density
- clean record classes over mixed-status aggregation

A smaller clean file is methodologically stronger than a larger mixed one.

---

## Version Note

This version formalizes the separation between:

- forward evaluation records
- retrospective reconstructed baseline records

That distinction is necessary to preserve credibility in the model error layer.
