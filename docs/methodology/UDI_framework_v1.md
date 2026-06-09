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
across a defined window for eligible magnitude-based
prediction classes.

`UDI = (1/n) × Σ signed_error_pct`

Where:
- underestimation = positive value
- overestimation = negative value

As of UDI v1.1, UDI is reported by prediction type
rather than as a single composite value.

Current strata:
- `UDI_point`
- `UDI_range`
- `State_concordance`
- `Trajectory_concordance`

State and trajectory predictions are excluded from
magnitude-based UDI calculations because they do not
contain continuous error magnitudes.

Composite UDI remains withheld pending future
methodological review.

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

## Related Methodology

Additional evaluation methods are defined in:

`docs/methodology/concordance_metrics.md`

This document governs state and trajectory prediction
evaluation through concordance metrics and operates
alongside the UDI framework.

## UDI v1.1 Stratified Reporting Amendment

Composite UDI remains withheld.

Beginning with UDI v1.1, UDI is reported only within
prediction-type strata:

- `UDI_point`: signed mean error for closed primary point predictions
- `UDI_range`: signed mean error for closed primary range predictions
- `State_concordance`: pass/fail closure rate for closed primary state predictions
- `Trajectory_concordance`: pass/fail closure rate for closed primary trajectory predictions

State and trajectory predictions are excluded from UDI because
they do not carry continuous magnitude information. They may
support directional calibration review but are not included in
magnitude-based error averages.

Composite UDI will remain withheld until predefined release
criteria are satisfied and a weighting methodology is locked
prior to computation.

Composite UDI release criteria:

- minimum 15 eligible primary point predictions
- minimum 15 eligible primary range predictions
- minimum 15 eligible primary state predictions
- minimum 10 eligible primary trajectory predictions

or

- minimum 50 eligible primary closed predictions overall

whichever threshold occurs later.

Until these criteria are satisfied, stratified reporting
remains the canonical UDI representation.

Compound prediction records are governed through the
methodology documented in:

`data/model_error/udi_reconciliation_032_033.md`

Records 032 and 033 have been reconciled using a
component-level resolution approach and are eligible
for inclusion under the UDI v1.1 framework.

## Caution

This framework is experimental.
It is intended to support structured observation,
reproducibility, and later interpretation.

It does not by itself establish a generalized scientific claim.
