# Prediction → Outcome Review Pipeline

---

## Purpose

This document defines how predictions enter the archive, remain fixed, resolve against observed outcomes, and become eligible for post-outcome review.

Its purpose is to protect temporal integrity.

The pipeline exists so that recorded predictions can be reviewed against observed reality without retroactive adjustment.

---

## Scope

This document applies to the **forward-logged prediction layer**.

It governs records intended for inclusion in:

- `data/model_error/model_error_gap_v1.csv`

It does **not** govern retrospective baseline reconstruction, which is preserved separately for historical context in:

- `data/model_error/model_error_gap_reconstructed.csv`

Those reconstructed records may support archive transparency, but they are not methodologically equivalent to forward-logged predictions.

---

## Core Principle

A valid prediction enters the primary evaluation layer only if it is recorded before the outcome is known.

That record then remains fixed until the observation window closes.

The archive does not treat retroactive prediction-writing as equivalent to forward logging.

---

## Pipeline Overview

The forward review pipeline operates as:

prediction creation  
→ holding state  
→ outcome capture  
→ error calculation  
→ closure  
→ post-outcome review

Each stage should be traceable through the archive.

---

## Stage 1 — Prediction Creation

A valid forward prediction must include:

- prediction date
- domain
- predicted value, range, or state
- defined observation window
- prediction type
- enough context to support later closure

At creation time, the outcome must still be unknown.

If the outcome is already known, the record may be preserved separately as retrospective context, but it does not qualify for the primary evaluation layer.

---

## Stage 2 — Holding State

After logging, the prediction enters a fixed holding state.

During this phase:

- the prediction is not rewritten
- the value, range, or state is not adjusted
- the observation window remains fixed
- outcome knowledge does not alter the original record

This protects temporal integrity.

---

## Stage 3 — Outcome Capture

Once the observation window has elapsed:

- the actual outcome is recorded
- the source must be traceable
- closure must rely on observable archive evidence

Outcome sources may include:

- device data
- logs
- snapshots
- structured reports tied to underlying artifacts

---

## Stage 4 — Error Calculation

After outcome capture, error may be calculated using the prediction type.

Standard fields may include:

- `error_absolute`
- `error_direction`
- `error_pct`

These fields express the gap between predicted and observed results.

---

## Stage 5 — Closure

Each forward-logged prediction should resolve to one of the following archive states:

- `closed`
- `open`

A prediction should remain open if the observation window is incomplete, the outcome evidence is insufficient, or resolution would require forced interpretation.

The archive should prefer delayed closure over premature closure.

---

## Stage 6 — Post-Outcome Review

Only properly forward-logged and closed records should inform post-outcome review.

This includes:

- directional error review
- repeated bias detection
- review of differences between subject-calibrated and generic assumptions

Retrospective baseline records may support historical understanding, but they should not be treated as equivalent evaluation evidence.

---

## Stage 7 — Historical Preservation

The model error layer may preserve two different classes of records:

### Forward evaluation records
Stored in `model_error_gap_v1.csv`

### Reconstructed baseline records
Stored in `model_error_gap_reconstructed.csv`

These two classes must remain segregated.

They serve different purposes and should not be blended into one evaluation dataset.

---

## Constraints

This pipeline enforces the following:

- forward statements are not treated as truth
- all eligible predictions must resolve against observed outcomes
- retroactive reconstruction is not treated as forward evidence
- interpretation cannot override observable outcome
- historical records remain preserved once logged

---

## Summary

The prediction review pipeline exists to make error review possible without weakening archive integrity.

Its value depends on one rule above all others:

**forward-logged records and retrospective records are not the same thing**
