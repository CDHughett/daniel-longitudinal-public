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
- `error_direction` (under / over / neutral)
- `error_pct`
- `model_type` (gen_pop / subject_calibrated)
- `calibration_state` (pre / post)
- `flag` (primary / inferred / reconstructed)
- `notes`

---

## Prediction Types

All predictions are classified into one of four types.

Type determines how the prediction is evaluated and when it can be closed.

### 1. POINT
- Predicts a specific numeric outcome  
- Example: HRV = 75  
- Closure: when value is observed or window expires  

### 2. RANGE
- Predicts a bounded interval  
- Example: Sleep = 400–450 minutes  
- Closure: after 2–3 observations within window  

### 3. STATE
- Binary or condition-based  
- Example: Sympathetic spikes without physiological disruption  
- Closure: when condition is clearly confirmed or falsified  

### 4. TRAJECTORY
- Directional or system-level change over time  
- Example: movement toward lock-in  
- Closure: after full observation window or decisive signal  

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

## Prediction Closure Rule

A prediction may be closed ONLY when:

1. The full observation window has elapsed  
AND  
2. Sufficient data exists to evaluate the outcome without ambiguity  

All predictions must resolve as:

- `CLOSED_SUCCESS`  
- `CLOSED_FAIL`  

Early closure is not permitted unless failure is definitive.

---

## Data Flow

### 1. Prediction
- Logged immediately  
- Outcome fields empty  
- Marked as `primary`  

### 2. Observation
- Data collected during defined window  

### 3. Resolution
- Prediction evaluated against observed data  
- Error calculated  

### 4. Aggregation
- Completed rows contribute to rolling metrics  

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

### `udi_rolling_tracker.csv`

Tracks how model error behaves over time.

Focus areas:

- directional bias (under vs over)  
- magnitude of error  
- calibration improvement  

### UDI (Unobstructed Delta Index)

> Average directional error across completed predictions

Used to quantify:

- model alignment  
- deviation from expected human baselines  
- convergence toward subject-specific accuracy  

---

## Data Integrity Rules

- Predictions must be timestamped before outcomes  
- Open predictions are preserved (no silent deletion)  
- Reconstructed data is explicitly labeled  
- Primary data carries highest weight  
- Closure follows strict window + evidence rules  

---

## System Role

This layer is **measurement infrastructure**, not interpretation.

It enables:

- model validation  
- calibration tracking  
- causal signal detection (e.g., interventions like THC removal)  

It does not generate conclusions.

---

## Current State

- Baseline reconstructed  
- Calibration boundary defined (provisional)  
- Subject-calibrated predictions active  
- Intervention-based predictions introduced  
- Rolling tracking initialized  

---

## Trajectory

As primary data accumulates, this layer transitions from:

- observational error tracking  

to:

- **controlled prediction testing system**

Long-term role:

> Quantifying the difference between population-based expectation and unobstructed system behavior.
