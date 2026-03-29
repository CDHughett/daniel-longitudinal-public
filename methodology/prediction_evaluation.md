# Prediction Evaluation Methodology

Daniel Longitudinal Study  
Prediction Evaluation Standard

---

## Purpose

This document defines how predictions are evaluated within the archive.

Its purpose is to ensure that:

- prediction closure is repeatable
- error assignment is auditable
- model comparisons remain structurally consistent
- qualitative and quantitative predictions are not conflated

This methodology applies to all entries in:

- `model_error_gap_v1.csv`
- `udi_tracker.csv`

---

## Prediction Types

Predictions are classified into one of three categories:

1. **Point**
2. **Range**
3. **State**

Each type is evaluated differently.

---

## 1. Point Predictions

Point predictions specify a single expected value.

### Example
- HRV = 75
- recovery_rate = 48
- performance = 1.00

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

Express as a percentage.

### Notes

Point predictions are best used when:
- the target variable is stable
- the observation window is narrow
- the prediction is numerically specific

---

## 2. Range Predictions

Range predictions specify an acceptable interval rather than a single target.

### Example
- sleep_duration = 400-460
- HRV = 68-78
- weight = 220-224
- performance = 1.00-1.10

### Definitions

For any range:

- `lower_bound = L`
- `upper_bound = U`
- `range_center = (L + U) / 2`

### Closure Rule

#### If observed value is inside the range:
- `error_absolute = 0`
- `error_direction = none`
- `error_pct = 0%`

#### If observed value is below the range:
- `error_absolute = L - actual_value`
- `error_direction = under`

#### If observed value is above the range:
- `error_absolute = actual_value - U`
- `error_direction = over`

### Error Percent

For range predictions outside the interval:

- `error_pct = error_absolute / range_center`

Express as a percentage.

### Evaluation Window Rule

If the prediction applies across multiple days:

- use the **mean observed value across the prediction window**
- do not score from a single outlier unless the prediction explicitly refers to a single-day event

### Notes

Range predictions are preferred when:
- the system is expected to vary within normal bounds
- exact point precision would overstate confidence
- the variable has known daily oscillation

---

## 3. State Predictions

State predictions describe whether a condition is present, absent, or maintained.

### Example
- recovery compatibility maintained = 1
- nervous system activation present = 1
- GI stability maintained = 1
- system resilience preserved = 1

### Encoding

Use binary encoding:

- `1 = prediction present / expected condition occurs`
- `0 = prediction absent / expected condition does not occur`

### Closure Rule

- if `actual_value == prediction_value`
  - `error_absolute = 0`
  - `error_direction = none`
  - `error_pct = 0%`

- if `actual_value != prediction_value`
  - `error_absolute = 1`
  - `error_direction = under` by default when expected condition fails
  - `error_pct = 100%`

### Notes

State predictions should be used for:
- behavioral continuity
- physiological compatibility
- disturbance presence/absence
- operational stability calls

State predictions should not be merged directly with quantitative percent-error summaries unless explicitly separated.

---

## Window Handling Rules

Prediction windows must be evaluated according to the structure of the original prediction.

### Single-Day Predictions
Use the observed value from that day.

### Multi-Day Predictions
Use the mean value across the full stated window unless the prediction explicitly references:
- maximum
- minimum
- rebound high
- first occurrence
- threshold crossing

### Incomplete Windows
Do not close the prediction until the stated window has matured.

---

## Status Rules

### Open
Prediction window still active or insufficient evidence available.

### Closed
Prediction window matured and enough evidence exists to evaluate.

---

## Direction Rules

Use direction labels as follows:

- `under` = observed result fell below required prediction boundary or expected state failed
- `over` = observed result exceeded upper prediction boundary
- `none` = observed result matched prediction or remained inside predicted range

---

## UDI Handling Rules

UDI should not be forced across mixed prediction types.

### Allowed
UDI may be calculated when the closure block is primarily:
- point predictions
- range predictions
- or another internally consistent quantitative set

### Not Recommended
UDI should be withheld when the closure block is dominated by:
- binary state predictions
- mixed state + range + point closures without weighting rules

In these cases:
- leave `udi_value` blank
- explain why in the tracker notes

---

## Methodological Priority

When in doubt, prefer:

1. structural consistency
2. reproducibility
3. conservative interpretation

Do not optimize for favorable outcomes.

Optimize for auditability.

---

## Archive Principle

Prediction evaluation is retrospective.

Predictions are not evidence by themselves.

Only closed predictions contribute to model comparison.
