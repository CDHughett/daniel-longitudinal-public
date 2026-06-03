# Concordance Metrics

This document defines evaluation methods for prediction classes that do not produce meaningful magnitude-based error calculations.

It exists to complement the UDI v1.1 framework and provide transparent handling for state and trajectory predictions.

---

## Purpose

The Unified Deviation Index (UDI) is designed for prediction classes where observed outcomes can be compared against predicted values using magnitude-based error calculations.

Examples:

- point predictions
- range predictions

Some prediction classes do not produce meaningful magnitude errors.

Examples:

- state predictions
- trajectory predictions

These prediction classes are evaluated through concordance metrics rather than UDI.

---

## Scope

This document applies only to:

- state predictions
- trajectory predictions

Point and range predictions remain governed by:

`docs/methodology/UDI_framework_v1.md`

and

`methodology/prediction_evaluation.md`

---

## State Concordance

### Definition

State Concordance measures whether a predicted state occurred.

State predictions are binary.

Examples:

- stable / unstable
- present / absent
- achieved / not achieved

Magnitude calculations are not applicable.

---

### Formula

State Concordance:

```text
correct state predictions
-------------------------
total closed state predictions
```

---

### Example

Prediction:

```text
Recovery remains stable.
```

Observed outcome:

```text
Recovery remains stable.
```

Result:

```text
correct
```

---

Prediction:

```text
Recovery remains stable.
```

Observed outcome:

```text
Recovery destabilized.
```

Result:

```text
incorrect
```

---

## Trajectory Concordance

### Definition

Trajectory Concordance measures whether the predicted directional trend occurred.

Trajectory predictions evaluate directional behavior rather than absolute magnitude.

Examples:

- increase
- decrease
- improve
- worsen
- accelerate
- decelerate

Magnitude calculations are not required.

---

### Formula

Trajectory Concordance:

```text
directionally correct trajectories
----------------------------------
total closed trajectory predictions
```

---

### Example

Prediction:

```text
HRV improves over the evaluation period.
```

Observed outcome:

```text
HRV improves.
```

Result:

```text
correct
```

---

Prediction:

```text
HRV improves over the evaluation period.
```

Observed outcome:

```text
HRV declines.
```

Result:

```text
incorrect
```

---

## Relationship to UDI

UDI and concordance metrics evaluate different prediction classes.

| Prediction Class | Evaluation Method |
|---|---|
| Point | UDI |
| Range | UDI |
| State | State Concordance |
| Trajectory | Trajectory Concordance |

No weighting relationship is currently defined between these systems.

---

## Composite Metrics

No composite reliability metric is currently approved.

Examples of intentionally withheld metrics include:

- composite UDI
- unified reliability score
- aggregate prediction index

Publication of any composite metric requires separate methodology approval.

---

## Governance

Concordance metrics exist to preserve methodological consistency while avoiding inappropriate application of magnitude-based error calculations.

State and trajectory predictions are therefore evaluated independently from UDI calculations.

---

## Status

Active.

This document defines the current repository methodology for state and trajectory prediction evaluation.
