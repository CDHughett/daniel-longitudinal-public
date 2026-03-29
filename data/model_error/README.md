# Model Error Data Layer

---

## The Core Idea

> **This layer measures the gap between expectation and reality.**

Not just what happened —  
but whether the model describing what *should* happen was correct.

**The error is the signal.**

---

## Why This Exists

Most datasets record outcomes.

This layer records:

> **Prediction → Outcome → Error**

This enables:

- validation of model behavior  
- detection of systematic bias (under / over)  
- measurement of calibration quality over time  
- identification of when general models fail and subject-specific models emerge  

---

## What This Tests

- Was the prediction correct?  
- Was it directionally accurate?  
- Did it under- or overestimate?  
- Did accuracy improve after calibration?  

---

## System Structure

Each prediction follows a strict lifecycle:

**Prediction (timestamped) → Observation → Resolution → Error calculation**

Predictions are always recorded **before outcomes exist**.

---

## Primary Dataset

### `model_error_gap_v1.csv`

Each row represents a single prediction compared to reality.

Fields include:

- `prediction_value`
- `actual_value`
- `error_absolute`
- `error_direction` (under / over / none)
- `error_pct`
- `model_type` (gen_pop / subject_calibrated)
- `calibration_state` (pre / post)
- `flag` (primary / inferred / reconstructed)
- `prediction_type` (point / range / state)
- `status` (open / closed)
- `notes`

---

## Prediction Types

Predictions are classified into three evaluation-safe categories.

### 1. POINT
- Predicts a specific numeric outcome  
- Example: HRV = 75  
- Evaluated using absolute and percent error  

---

### 2. RANGE
- Predicts a bounded interval  
- Example: Sleep = 400–450 minutes  
- Evaluated based on whether observed values fall inside or outside the interval  

---

### 3. STATE
- Binary or condition-based  
- Example: GI stability maintained  
- Evaluated as correct (0 error) or incorrect (100% error equivalent)  

---

## Evaluation Standard

All prediction scoring rules are defined in:

> `/methodology/prediction_evaluation.md`

This includes:

- error calculation rules  
- range handling  
- state evaluation  
- multi-day window handling  

This file does **not duplicate those rules**.

---

## Valid Prediction Criteria

A prediction is eligible for inclusion only if it meets ALL of the following:

1. **Forward-Looking**
   - Logged before outcome is known  

2. **Time-Bounded**
   - Includes a defined observation window  

3. **Observable**
   - Maps to measurable or clearly observable signals  

4. **Falsifiable**
   - Can be proven wrong  

5. **Domain-Specific**
   - Assigned to a defined system (HRV, sleep, performance, etc.)  

6. **Independent**
   - Does not rely on another prediction to resolve  

7. **Context-Aware**
   - Major confounders are noted if present  

Invalid predictions are not logged.

---

## Prediction Closure Rules

A prediction may be closed ONLY when:

1. The defined observation window has elapsed  
AND  
2. Sufficient data exists to evaluate outcome without ambiguity  

---

### Status Encoding

- `open` → prediction still active or insufficient data  
- `closed` → prediction fully evaluated  

---

### Outcome Classification

Outcome success/failure is determined from:

- error magnitude  
- direction  
- or state match  

No separate `success/fail` column is required.

---

## Data Flow

### 1. Prediction
- Logged immediately  
- Marked as `primary`, `inferred`, or `reconstructed`  
- `status = open`

---

### 2. Observation
- Data collected during defined window  

---

### 3. Resolution
- Prediction evaluated  
- Error fields populated  
- `status = closed`

---

### 4. Aggregation
- Closed predictions contribute to rolling metrics  

---

## Calibration Boundary

### `calibration_events_log.md`

Tracks transition from:

- **gen_pop models** → general population assumptions  
to  
- **subject_calibrated models** → individualized prediction behavior  

This boundary separates:

- pre-calibration performance  
- post-calibration accuracy  

---

## Rolling Error Tracking

### `udi_tracker.csv`

Tracks grouped prediction performance over defined windows.

Fields include:

- directional counts (under / over / none)  
- completion counts  
- prediction type composition  
- UDI (when applicable)  

---

### UDI (Unobstructed Delta Index)

> Average directional error across completed predictions

Used to quantify:

- model alignment  
- deviation from expected baselines  
- convergence toward subject-specific accuracy  

---

### UDI Calculation Constraint

UDI is only calculated when:

- the closure block is primarily quantitative (point + range)  
- prediction types are comparable  

---

### UDI Withholding Rule

UDI is intentionally left blank when:

- the closure block is dominated by state predictions  
- prediction types are mixed without weighting  
- comparison would reduce interpretability  

This is **by design**, not missing data.

---

## Data Integrity Rules

- Predictions must be timestamped before outcomes  
- Open predictions are preserved (no deletion)  
- Reconstructed data is explicitly labeled  
- Primary predictions carry highest weight  
- Closure follows strict window + evidence rules  
- Evaluation rules are applied consistently across all entries  

---

## System Role

This layer is **measurement infrastructure**, not interpretation.

It enables:

- model validation  
- calibration tracking  
- detection of systematic bias  
- identification of model failure conditions  

It does not generate conclusions.

---

## Current State

- Baseline reconstructed  
- Calibration boundary defined (provisional)  
- Subject-calibrated predictions active  
- Mixed prediction types present  
- UDI selectively applied based on methodological validity  

---

## Trajectory

As primary prediction volume increases, this layer transitions from:

- observational error tracking  

to:

- **controlled prediction testing system**

---

## Long-Term Role

> Quantifying the difference between population-based expectation and unobstructed system behavior.

This layer becomes the foundation for:

- model calibration validation  
- subject-specific prediction systems  
- reproducible performance forecasting
