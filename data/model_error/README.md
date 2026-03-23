# Model Error Data Layer

This directory contains structured records of AI-predicted vs observed outcomes across multiple domains within the Daniel Longitudinal Study.

---

## Purpose

To preserve forward-looking model predictions and compare them against observed outcomes over time.

This enables measurement of directional model error under longitudinal conditions.

---

## Primary File

- `model_error_gap_v1.csv`

This dataset records:

- predicted values  
- observed outcomes  
- error magnitude and direction  
- model type (population vs subject-calibrated)  
- calibration state  
- data quality flags  

---

## Supporting Files

- `calibration_events_log.md`  
  Documents transitions in model interpretation (e.g., population-calibrated → subject-specific)

- `prediction_holding_note.md`  
  Temporary capture location for predictions that cannot be logged immediately

---

## Data Characteristics

- Predictions may be logged before outcomes exist  
- Open rows are completed once corresponding observations are available  
- Data quality is explicitly labeled:
  - `primary`
  - `inferred`
  - `reconstructed`

---

## Role in Archive

This layer functions as measurement infrastructure.

It does not generate conclusions or interpretations.

It preserves prediction-to-outcome relationships as structured artifacts for later analysis.

---

## Status

Early-stage instrumentation layer.

Data density and signal strength will increase over time through consistent capture.
