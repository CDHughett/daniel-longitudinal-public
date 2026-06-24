# Observer Quickstart

This is a short inspection route for researchers, technical reviewers, or skeptical readers who want to evaluate the archive without reading everything.

Use this only as a quick audit path.

For broader context, see [`FOR_OBSERVERS.md`](./FOR_OBSERVERS.md).

---

## Purpose

This file answers one question:

**What should an outside observer inspect first if they want to test the archive structure?**

The goal is not to summarize the entire repository.

The goal is to provide a compact review route through:

- archive posture
- current state
- data coverage
- one report
- one snapshot
- model-error review
- governance boundaries

---

## 1. Read The Archive Posture

Start with:

- [`README.md`](../README.md)
- [`docs/START_HERE.md`](./START_HERE.md)

Check whether the archive clearly states:

- what it is
- what it is not
- what it claims
- what it does not claim
- where evidence lives
- how interpretation is limited

---

## 2. Inspect Current State

Read:

- [`LATEST.md`](../LATEST.md)

Check whether the current system state is clearly separated from:

- historical reports
- future expectations
- performance claims
- speculative interpretation

The current-state dashboard should describe the active observation window without making forward claims.

---

## 3. Check Data Coverage

Read:

- [`data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)

Check:

- what datasets are public
- what data is excluded
- what is structured longitudinally
- what is referenced but not included
- where data limitations constrain interpretation

Do not evaluate claims without first checking coverage.

---

## 4. Inspect One Report

Open one recent weekly report:

- [`reports`](../reports/)

Suggested starting point:

- the most recent closed weekly report

Check whether the report:

- interprets retrospectively
- references observed conditions
- avoids unsupported forward claims
- distinguishes system-wide patterns from localized events
- remains consistent with the stated archive posture

---

## 5. Inspect One Snapshot

Open the corresponding snapshot window:

- [`snapshots`](../snapshots/)
- [`SNAPSHOT_LOG.md`](../SNAPSHOT_LOG.md)
- [`EPOCH_INDEX.md`](../EPOCH_INDEX.md)

Check whether the snapshot layer supports the report context.

Artifacts should precede interpretation.

---

## 6. Inspect The Model-Error Layer

Read:

- [`data/model_error/WHAT_THIS_LAYER_IS.md`](../data/model_error/WHAT_THIS_LAYER_IS.md)
- [`data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)

Check whether predictions are:

- recorded
- closed retrospectively
- compared against observed outcomes
- preserved even when wrong
- used for calibration rather than promotion

The model-error layer is auxiliary.

It is not the primary evidence layer.

---

## 7. Review Governance

Read:

- [`GOVERNANCE.md`](../GOVERNANCE.md)
- [`STRUCTURAL_PRINCIPLES.md`](../STRUCTURAL_PRINCIPLES.md)
- [`PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)
- [`RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md)

Check whether the repository defines:

- interpretation boundaries
- phase advancement requirements
- evidence hierarchy
- risk controls
- constraints on claims
- separation between artifacts and interpretation

---

## Quick Audit Sequence

```text
README.md
  ↓
docs/START_HERE.md
  ↓
LATEST.md
  ↓
data/DATA_COVERAGE.md
  ↓
one recent report
  ↓
corresponding snapshot window
  ↓
data/model_error
  ↓
governance documents
```

---

## Evaluation Principle

The archive should be evaluated by coherence between:

- what is claimed
- what is measured
- what is preserved
- what is interpreted
- what is explicitly limited

A strong reading should move from evidence toward interpretation.

Not from narrative toward evidence.

---

## Boundary

This file is a shortcut.

It does not replace the full archive map.

For complete navigation, use:

- [`INDEX.md`](../INDEX.md)

For a full first reading pass, use:

- [`docs/NEWCOMER_PATH.md`](./NEWCOMER_PATH.md)
