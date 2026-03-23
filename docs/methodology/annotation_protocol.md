# Annotation Protocol — Model Error Layer v1

## Objective

To ensure all forward-looking AI trajectory statements are
captured in a consistent format for later comparison against
observed outcomes.

## Rule

All new AI predictions should be logged as close to time of
generation as possible.

Unlogged predictions reduce signal quality and retroactive
accuracy.

## Logging Priority

### Priority 1 — Live Capture
Log new predictions at time of generation.

### Priority 2 — Retroactive Annotation
Return to archived conversations and reconstruct older
predictions where possible.

## Live Capture Protocol

After any AI session that produces a trajectory statement:

Step 1: Copy the exact statement  
Step 2: Identify domain  
Step 3: Extract or estimate the predicted value  
Step 4: Log immediately to `model_error_gap_v1.csv`  
Step 5: Flag as `primary` if explicit, `inferred` if directional only  
Step 6: Note model version and date

Minimum time to log: under 2 minutes per prediction.

If time is not available immediately:
- paste the raw AI statement into `prediction_holding_note.md`
- tag with date and domain
- log within 24 hours

## Minimum Required Fields

- `date`
- `domain`
- `model_version`
- `prediction_value` or directional statement
- `model_type`
- `calibration_state`
- `flag`
- `notes`

## Open Predictions

Predictions may be logged before observed outcomes are available.

In those cases:
- leave `actual_value` blank
- leave `error_absolute` blank
- leave `error_direction` blank
- leave `error_pct` blank

Complete those fields only after the corresponding observed outcome is recorded.

## Flag Definitions

- `primary`: explicit prediction logged at time of generation
- `inferred`: direction stated, value estimated from context
- `reconstructed`: extracted from archived material after the fact

## Evidence Hierarchy

Prediction records should be interpreted according to the following strength order:

1. `primary`
   - explicit prediction logged at time of generation before outcome known

2. `inferred`
   - directional or partially quantified prediction logged near time of generation

3. `reconstructed`
   - prediction extracted from archived material after the fact

For any external interpretation, primary records should carry the greatest evidentiary weight.

## Domain Guidance

Examples:
- `HRV`
- `sleep`
- `body_comp`
- `performance`
- `recovery_rate`

## Comparison Rule

A logged prediction should later be matched to the nearest
valid observed outcome in the corresponding dataset or snapshot.

## Principle

The error itself is the signal.
This layer exists to preserve that signal in machine-readable form.
