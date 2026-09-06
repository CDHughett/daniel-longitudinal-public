# Model-Error Schema v2 — Future Field Separation

## Status

**Design contract for future schema migration.**

This document does not migrate or rewrite `data/model_error/model_error_gap_v1.csv`.

The current v1 dataset remains the historical source of record for existing prediction registrations and outcomes.

---

## Purpose

The v1 field `calibration_state` accumulated two different concepts during the evolution of the prediction layer:

1. whether a record was prospectively locked before outcome access
2. how much subject-specific information the prediction model had already incorporated

Those are independent dimensions.

A prediction can be:

```text
prospectively registered
+
subject calibrated
```

at the same time.

Future schemas should therefore stop using one field to represent both concepts.

---

# Future Split

## `registration_status`

Describes **temporal/evaluative provenance** of the prediction record.

Proposed controlled values:

### `prospective_locked`

The prediction was committed before the relevant outcome/scoring window was known and is protected from hindsight revision.

### `forward_exploratory`

The statement was made before outcome access but did not satisfy all criteria required for a formally preregistered/locked evaluation.

### `retrospective_reconstructed`

The record was created after outcome access for historical context only and is ineligible for prospective calibration metrics.

---

## `model_calibration_scope`

Describes **what prior information informed the model**, independent of registration timing.

Proposed controlled values:

### `general_population`

The prediction primarily reflects generic/population assumptions rather than subject-specific calibration.

### `subject_calibrated`

The prediction model incorporated prior subject-specific history before generating the prospective estimate.

### `mixed_or_unknown`

The calibration scope cannot be cleanly assigned from the preserved historical record.

---

## Optional `registration_protocol`

A future schema may also include a locator to the governing preregistration/evaluation artifact, for example:

```text
methodology/open_prediction_evaluation_plan_045.md
```

This should be a provenance field, not an outcome field.

---

# v1 Compatibility Rule

The existing `calibration_state` values must not be mechanically rewritten to the new fields without a governed migration.

In particular, records 041–046 currently retain:

```text
calibration_state = pre
```

as protected historical registration provenance.

Those values remain unchanged.

Their model identifiers already show that later prospective records may also be subject-calibrated.

The apparent tension is a v1 schema limitation, not permission to mutate protected rows.

---

# Migration Requirements

A future `model_error_gap_v2.csv` migration must:

1. preserve every v1 record identifier
2. preserve original prediction text
3. preserve registration date
4. preserve closed/open status
5. preserve adjudicated actual values and error directions
6. map registration provenance independently from model calibration scope
7. document ambiguous mappings rather than force them
8. keep historical reconstructed records separate from prospective evaluation records
9. update validator protections before v2 becomes canonical
10. document the migration in `CHANGELOG.md` and applicable release notes

No v2 migration is authorized solely by this design document.

---

# UDI Relationship

UDI is canonically the **Unobstructed Delta Index**.

UDI eligibility should depend on the future `registration_status` and prediction-type rules rather than using model calibration scope as a proxy for temporal validity.

Model calibration scope may then be used as a separate analytical stratifier.

This supports cleaner questions such as:

```text
How do prospectively locked, subject-calibrated predictions perform?
```

without conflating that question with:

```text
Was the prediction actually registered before outcome access?
```

---

# Archive Boundary

This future schema is intended to improve semantic clarity.

It does not:

- rescore any existing prediction
- alter UDI values
- alter concordance values
- reopen a closed record
- close an open record
- change the protected registration state of records 041–046
- establish that historical records can be perfectly reclassified
