# Unobstructed Delta Index (UDI) Framework v1

## Purpose

This document defines the experimental framework used to
quantify directional model error when population-calibrated
AI predictions are compared against observed outcomes in a
longitudinal single-subject system.

## Working Hypothesis

Population-calibrated models may systematically underestimate
observed outcomes in this system during periods of stable
execution, adaptation, and reduced interference.

This is treated as a working hypothesis under measurement,
not a fixed conclusion.

## Core Schema

Primary dataset:
`/data/model_error/model_error_gap_v1.csv`

Fields:
- `record_id`
- `date`
- `domain`
- `model_version`
- `prediction_value`
- `actual_value`
- `error_absolute`
- `error_direction`
- `error_pct`
- `model_type`
- `calibration_state`
- `flag`
- `notes`

## Error Definitions

- `error_absolute = |actual_value - prediction_value|`
- `error_direction = under | over`
- `error_pct = (error_absolute / prediction_value) * 100`

Interpretation:
- `under` = model underestimated observed outcome
- `over` = model overestimated observed outcome

## UDI Definition

UDI is a signed average of prediction error percentages
across a defined window.

`UDI = (1/n) × Σ signed_error_pct`

Where:
- underestimation = positive value
- overestimation = negative value

## Intended Use

UDI is used to evaluate:
1. Whether model error is directional rather than random
2. Whether model error changes after subject-specific calibration
3. Whether residual positive error persists after calibration

## Data Quality Flags

- `primary` = explicit prediction recorded at time of generation
- `inferred` = directional statement translated into an estimated value
- `reconstructed` = retroactively extracted from archive

## Calibration Events

Calibration events are logged in:
`/data/model_error/calibration_events_log.md`

These events define the comparison boundary between
pre-calibration and post-calibration interpretation.

## Caution

This framework is experimental.
It is intended to support structured observation,
reproducibility, and later interpretation.

It does not by itself establish a generalized scientific claim.
