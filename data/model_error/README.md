# Model Error Data Layer

---

## The Core Idea

> **This layer measures the gap between expectation and reality.**

---

## Why This Exists

Most datasets record outcomes.

This layer records **expectations vs outcomes** — and measures the difference.

**That difference is the signal.**

---

## What This Tests

Not just what happened.

But whether the model describing what *should* happen was correct.

- Was it directionally accurate?  
- Did it systematically under- or overestimate?  
- Did accuracy change after calibration?  

---

## System Structure

**Prediction → Timestamp → Outcome → Error**

Each prediction is captured **before** the outcome exists.  
Each outcome is later matched and scored.

---

## Primary Dataset

### `model_error_gap_v1.csv`

Each row represents a single prediction compared to reality.

Includes:

- predicted value  
- observed value  
- error magnitude  
- error direction (under / over / neutral)  
- model type (population vs subject-calibrated)  
- calibration state (pre / post)  
- data quality (primary / inferred / reconstructed)  

---

## Calibration Boundary

### `calibration_events_log.md`

Models change.

At some point, predictions stop behaving like:

> general population assumptions

and start behaving like:

> subject-specific behavior

This boundary is logged and used to separate:

- pre-calibration  
- post-calibration  

---

## Rolling Error Tracking

### `udi_rolling_tracker.csv`

Tracks how model error behaves over time.

Focus:

- directional bias  
- magnitude of error  
- calibration effects  

**UDI (Unobstructed Delta Index)** = average directional error across completed predictions.

---

## Data Flow

### 1. Prediction
Logged immediately  
→ outcome fields empty  
→ marked as `primary`  

### 2. Outcome
Row is completed when observed  
→ error calculated  

### 3. Aggregation
Completed rows contribute to rolling UDI tracking  

---

## Data Integrity

- Predictions are timestamped before outcomes  
- Open predictions are preserved  
- Reconstructed data is explicitly labeled  
- Primary data has highest weight  

---

## System Role

This layer is **measurement infrastructure**.

It enables:

- validation of model behavior  
- detection of calibration shifts  
- quantification of prediction accuracy  

It does not generate conclusions.

---

## Status

- Baseline reconstructed  
- Calibration boundary defined (provisional)  
- Primary prediction capture active  
- Rolling tracking initialized  

Signal quality increases as primary data accumulates.
