# Prediction → Outcome → Calibration Pipeline

---

## Purpose

This document defines the internal workflow used to generate, evaluate, and refine predictions within the Daniel Longitudinal Study.

It exists to ensure that:

- predictions are consistently structured
- outcomes are objectively recorded
- model error is measurable
- calibration is traceable across time

This pipeline is **mechanical, not interpretive**.  
It governs how predictions interact with reality inside the archive.

---

## Core Principle

Predictions are not claims.

They are **testable artifacts** that must resolve into one of two states:

- **Closed (validated or invalidated)**
- **Invalid (excluded based on criteria)**

No prediction remains permanently open.

---

## Pipeline Overview

The system operates through the following sequence:

prediction (forward artifact)  
→ outcome (observed reality)  
→ error measurement  
→ calibration update  
→ future prediction refinement  

Each stage is versioned and traceable.

---

## Stage 1 — Prediction Creation

Predictions are generated under controlled structure.

Each prediction must include:

- timestamp
- domain (sleep, HRV, performance, etc.)
- predicted value or range
- defined observation window
- classification type (e.g. inferred, reconstructed, direct)

Predictions must be:

- falsifiable
- time-bound
- measurable within the dataset

---

## Stage 2 — Holding State

After creation, predictions enter a **holding state**.

During this phase:

- no modification is allowed
- no retroactive adjustment is permitted
- prediction remains fixed until outcome is available

This preserves dataset integrity.

---

## Stage 3 — Outcome Recording

Once the observation window is complete:

- actual observed value is recorded
- source must be traceable (device, dataset, snapshot)

Outcomes must be:

- objective
- timestamp-aligned
- consistent with measurement definitions

---

## Stage 4 — Error Calculation

Error is calculated as the difference between prediction and outcome.

Standard fields include:

- absolute error
- directional error (over / under)
- percentage error (when applicable)

This creates a measurable gap between:

**model expectation vs observed reality**

---

## Stage 5 — Prediction Closure

Every prediction must resolve into one of the following:

### Closed — Valid
- prediction met acceptable error bounds

### Closed — Invalid
- prediction failed to meet acceptable bounds

### Excluded
- prediction removed due to invalid structure or missing data

Closure is mandatory.  
No prediction remains indefinitely open.

---

## Stage 6 — Calibration Layer

Closed predictions feed into calibration.

Calibration operates by:

- identifying systematic bias (over/under trends)
- adjusting expectation ranges
- refining future prediction inputs

Calibration is:

- incremental
- evidence-based
- version-aware

---

## Stage 7 — Dataset Integration

All predictions, outcomes, and errors are stored in:

`/data/model_error/`

This creates a growing record of:

- prediction accuracy
- model drift
- system-specific behavior

The dataset is:

- append-only
- machine-readable
- historically preserved

---

## Valid Prediction Criteria

For a prediction to be included in the dataset, it must:

- be time-bound
- be measurable using available data
- include a defined outcome window
- be recorded before outcome is known
- remain unmodified during holding state

Predictions that fail these criteria are excluded.

---

## Calibration Discipline

Calibration is not immediate.

The system avoids:

- overfitting to single outcomes
- reactive adjustment
- short-term bias correction

Instead, calibration requires:

- repeated evidence across multiple predictions
- consistent directional error patterns
- stability across time

---

## System Constraints

This pipeline enforces the following:

- no forward claims are treated as truth
- all predictions must resolve against reality
- interpretation cannot override data
- historical records remain unchanged

---

## Archive Role

This pipeline transforms the archive from:

**documentation → evaluation system**

It enables:

- measurable accuracy tracking
- subject-specific model refinement
- reproducible prediction frameworks

---

## Summary

The prediction → outcome → calibration pipeline ensures that:

- all forward statements are testable
- all results are recorded objectively
- all errors are measurable
- all improvements are evidence-based

This maintains:

- dataset integrity
- methodological clarity
- long-term credibility of the archive
