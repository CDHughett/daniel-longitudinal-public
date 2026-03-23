Model Error Data Layer

This directory contains structured records of AI-predicted vs observed outcomes across multiple domains within the Daniel Longitudinal Study.

---

Purpose

To preserve forward-looking model predictions and compare them against observed outcomes over time.

This enables direct measurement of:

- directional model error
- magnitude of deviation between prediction and reality
- changes in model accuracy under longitudinal conditions

---

System Overview

This layer introduces a comparative measurement structure:

Prediction → Timestamp → Observed Outcome → Error Calculation

Unlike standard tracking systems, this layer captures expected vs actual system behavior, not just outcomes.

---

Primary Dataset

"model_error_gap_v1.csv"

Core dataset containing individual prediction records.

Each row represents a single prediction-to-outcome comparison.

Fields include:

- prediction value
- observed value
- error magnitude
- error direction (under / over / neutral)
- model type ("population_calibrated" vs "subject_calibrated")
- calibration state ("pre" / "post")
- data quality ("primary", "inferred", "reconstructed")

---

Calibration Layer

"calibration_events_log.md"

Documents transition points where model behavior shifts.

Example:

- population-based interpretation → subject-specific interpretation

These events define pre- and post-calibration regimes used in analysis.

---

Rolling Error Monitoring

"udi_rolling_tracker.csv"

Tracks aggregate model error over time using a rolling window.

Purpose:

- monitor directional bias (underestimation vs overestimation)
- observe calibration effects
- track signal stability across time windows

Metric:

- UDI (Unobstructed Delta Index) = average directional error across completed rows

Only completed prediction rows are used in UDI calculation.

---

Prediction Capture Workflow

1. Prediction Generated

- Logged immediately in "model_error_gap_v1.csv"
- Marked as "primary" where applicable
- Outcome fields left blank

2. Observation Occurs

- Row is completed with:
  - actual value
  - error magnitude
  - direction

3. Rolling Update

- Completed rows are incorporated into "udi_rolling_tracker.csv"
- Typically updated on scheduled review days (Wednesday / Saturday / Sunday)

---

Data Characteristics

- Open predictions are expected and tracked
- Rows are completed asynchronously as outcomes occur
- Data quality is explicitly labeled:
  - "primary" → forward-logged prediction
  - "inferred" → reconstructed from context
  - "reconstructed" → backfilled historical estimate

---

System Role

This layer functions as measurement infrastructure, not interpretation.

It enables:

- validation of predictive models
- detection of calibration shifts
- quantification of model reliability

No conclusions are generated within this layer.

All interpretation occurs downstream in reports.

---

Status

Active instrumentation layer.

Transitioned from reconstructed baseline → primary prediction capture.

Signal quality and reliability will increase as:

- primary prediction density increases
- post-calibration data accumulates
- rolling UDI tracking stabilizes

---

Notes

This system is designed for longitudinal integrity.

All entries are:

- timestamped
- version-controlled
- non-retroactive (for primary predictions)

The goal is not prediction accuracy in isolation, but measurable alignment between model expectation and observed system behavior over time.
