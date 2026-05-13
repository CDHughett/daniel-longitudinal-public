# What This Layer Is

The model-error layer tracks forward-logged predictions generated during longitudinal observation and compares them against later observable outcomes.

It exists to evaluate calibration over time.

This layer is not a claim of certainty, authority, or predictive superiority. It is an exploratory evaluation structure for comparing model-generated expectations against lived artifacts under explicit closure rules.

## Purpose

The purpose of this layer is to document:

- when a prediction was made
- what model generated it
- what outcome would count as confirmation, partial confirmation, or failure
- what observation window applies
- whether the prediction was later closed
- how the model’s projection compared with the observed result

The goal is not simply to track whether predictions were “right” or “wrong.”

The goal is to preserve a calibration trail between:

- forward-logged projections
- structured observation windows
- later archive artifacts
- retrospective outcome review

## What Counts as a Valid Prediction

A prediction is only suitable for this layer when it is:

- forward-logged before the outcome window
- time-bounded
- specific enough to evaluate
- linked to observable criteria
- assigned a closure condition
- separated from later retrospective interpretation

Additional criteria are defined in:

[`docs/methodology/valid_prediction_criteria.md`](../../docs/methodology/valid_prediction_criteria.md)

## Model Version Field

The `model_version` field identifies the model that generated the projection.

This matters because the layer is partly a calibration record across model states. Different models may produce different projections, confidence levels, or framing styles.

The field should be interpreted as part of the audit trail, not as a claim that the model has independent authority over the archive.

## Feedback Loop

This layer functions as a feedback loop between model output and observed reality.

Predictions are generated from the available context at the time. Later outcomes are evaluated against the defined criteria. The resulting closure record becomes part of the archive’s calibration history.

Over time, this allows review of:

- model overconfidence
- model underconfidence
- range accuracy
- trajectory accuracy
- timing errors
- ambiguous or poorly scoped predictions
- domains where projection quality improves or degrades

## Constraints

This layer does not replace the archive’s governed structure.

It does not create forward claims for the project as a whole.

It does not turn speculative statements into validated findings.

It does not override reports, snapshots, raw data, or governance documents.

The model-error layer is auxiliary. It exists to make prediction quality visible, reviewable, and falsifiable over time.

## Related Documents

- [`model_error_gap_v1.csv`](model_error_gap_v1.csv)
- [`docs/methodology/valid_prediction_criteria.md`](../../docs/methodology/valid_prediction_criteria.md)
- [`docs/methodology/prediction_to_outcome_pipeline.md`](../../docs/methodology/prediction_to_outcome_pipeline.md)
- [`methodology/prediction_evaluation.md`](../../methodology/prediction_evaluation.md)
- [`GOVERNANCE.md`](../../GOVERNANCE.md)
