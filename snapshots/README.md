# Snapshots

This directory preserves primary measurement artifacts and capture-window context.

Snapshot folders are organized by time using `YYYY-MM`.

---

## Temporal Anchor Standard

Snapshot windows may include an accompanying epoch file.

Standard filename:

- `YYYY-MM Epoch.md`

Example:

- `2026-02 Epoch.md`

This file serves as the **temporal anchor record** for that snapshot window.

Its role is to make each snapshot easy to place in:

- calendar time
- archive phase
- operating conditions
- artifact membership
- verification path
- interpretation path

---

## What the epoch file should contain

Each epoch file should document:

- the snapshot window
- the capture conditions
- the archive position of the window
- the artifacts included in that folder
- where verification is handled
- where interpretation belongs
- related archive links

This file is context, not synthesis.

---

## What the epoch file is not

An epoch file does **not** function as:

- a phase declaration
- a retrospective verdict
- a performance claim
- a longitudinal synthesis
- a substitute for reports
- a substitute for verification records

---

## Separation of roles

- **snapshots/** → preserve evidence and capture-window context
- **checksums.txt** → verify binary artifact integrity
- **reports/** → interpret what occurred
- **phase documents** → define retrospective system-level meaning
- **root navigation files** → orient readers across the archive

---

## Recommended epoch structure

A clean epoch file should include these sections in this order:

1. `Window`
2. `Archive Position`
3. `Operating Conditions`
4. `Included Artifacts`
5. `Verification`
6. `Interpretation Boundaries`
7. `Related Archive Links`
8. `Notes`

This structure is intended to keep snapshot windows legible, comparable, and easy to cross-reference over time.

---

## Checksum Standard

Snapshot folders containing binary or non-text artifacts  
(for example `.jpg`, `.png`, `.pdf`) should include a `checksums.txt` file.

This file contains SHA-256 hashes for artifact verification.

### Purpose

Checksums verify **artifact integrity only**.

They do not replace:

- the source artifact
- the epoch file
- the report layer
- the archive’s interpretive constraints

### Structure

- one `checksums.txt` per snapshot folder
- one SHA-256 entry per binary artifact
- filenames recorded relative to that folder

### Maintenance

- hashes are generated when a binary artifact is added
- hashes are updated only if that artifact changes

This maintains a lightweight verification layer while preserving the archive’s artifact-first structure.
