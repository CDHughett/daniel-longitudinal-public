# Newcomer Reading Path

This is the first full reading pass for the Daniel Longitudinal Study.

Use this after the 5-minute orientation in [`docs/START_HERE.md`](./START_HERE.md).

This path is intended for a reader who wants more than the first-contact summary but does not need the complete repository map.

---

## Role Of This File

Use these based on depth:

- [`docs/START_HERE.md`](./START_HERE.md) — first 5 minutes
- [`docs/NEWCOMER_PATH.md`](./NEWCOMER_PATH.md) — first 30–60 minutes
- [`INDEX.md`](../INDEX.md) — complete repository map

`START_HERE.md` explains what the archive is.

`NEWCOMER_PATH.md` shows how to begin reading it.

`INDEX.md` maps the full repository.

---

## Step 1 — Understand The Project

Read:

- [`README.md`](../README.md)

Purpose:

Understand what the archive is, why it exists, what it contains, and what it does not claim.

---

## Step 2 — Establish Current State

Read:

- [`LATEST.md`](../LATEST.md)

Purpose:

Understand the active observation window, current phase, recent archive updates, and current system emphasis.

This prevents the reader from entering the archive only through historical material.

---

## Step 3 — Understand Data Coverage

Read:

- [`data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md)

Purpose:

Understand what data is included, what data is excluded, what is public, and where interpretation is limited by available evidence.

This should come before technical interpretation.

---

## Step 4 — Understand Observer Evaluation

Read:

- [`docs/FOR_OBSERVERS.md`](./FOR_OBSERVERS.md)

Purpose:

Understand how a skeptical or technical reader should evaluate the archive.

This provides the basic audit posture before entering deeper system documents.

---

## Step 5 — Understand System Structure

Read:

- [`SYSTEM_OVERVIEW.md`](../SYSTEM_OVERVIEW.md)
- [`DATASET_OVERVIEW.md`](../DATASET_OVERVIEW.md)

Purpose:

Understand how information moves through the archive and how datasets relate to reports, snapshots, and governance.

---

## Step 6 — Understand Evidence And Artifacts

Read:

- [`EPOCH_INDEX.md`](../EPOCH_INDEX.md)
- [`SNAPSHOT_LOG.md`](../SNAPSHOT_LOG.md)
- [`snapshots`](../snapshots/)
- [`reports`](../reports/)

Purpose:

Understand the temporal structure of the archive and how primary artifacts support retrospective interpretation.

Suggested order:

1. Review the epoch index.
2. Review the snapshot log.
3. Inspect one snapshot window.
4. Inspect the corresponding weekly report.

---

## Step 7 — Understand The Model-Error Layer

Read:

- [`data/model_error/WHAT_THIS_LAYER_IS.md`](../data/model_error/WHAT_THIS_LAYER_IS.md)
- [`data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)

Purpose:

Understand how predictions are compared against observed outcomes and how model error is preserved for calibration.

This layer is auxiliary.

It is not the primary evidence layer.

---

## Step 8 — Understand Uncertainty And Calibration

Read:

- [`docs/methodology/UDI_framework_v1.md`](./methodology/UDI_framework_v1.md)

Purpose:

Understand how uncertainty, prediction performance, state concordance, and trajectory concordance are evaluated.

This should be read after the model-error layer, not before it.

---

## Step 9 — Understand Recurring Concepts

Read:

- [`docs/CONCEPTS.md`](./CONCEPTS.md)

Purpose:

Understand recurring archive terms and internal concepts used across reports, methodology, and observer-facing documents.

---

## Step 10 — Explore The Archive

Suggested areas:

- weekly reports
- audit reports
- findings
- model-error records
- longitudinal summaries
- governance documents
- snapshot windows

At this point, most recurring concepts used throughout the archive should be understandable.

---

## Reading Principle

Move from simple to technical:

```text
orientation
  ↓
current state
  ↓
data coverage
  ↓
observer evaluation
  ↓
system structure
  ↓
artifacts and reports
  ↓
model-error layer
  ↓
uncertainty framework
  ↓
full archive exploration
```

The goal is not to read everything immediately.

The goal is to understand enough structure to inspect the archive intelligently.
