# Snapshots

This directory contains primary measurement artifacts.

Snapshots represent confirmed capture events under controlled operating conditions.

Once committed, snapshot artifacts are never modified.

---

## Definition of a Snapshot

A snapshot is:

* A date-stamped measurement event
* Captured under normal operating constraints
* Logged without dehydration or artificial manipulation
* Archived with integrity controls

---

## Folder Structure

Each month receives its own subdirectory:

Each subdirectory may contain:

* `README.md` — context for that capture window
* Image or PDF artifacts
* `checksums.txt` — SHA256 hashes for verification

---

## Naming Convention

Artifacts must follow:

YYYY-MM-DD_measurement-type.ext

Examples:

* 2026-02-12_dexa_body-comp.png
* 2026-02-12_bodpod_results.pdf

Lowercase. Hyphen-separated. Date first.

---

## Integrity Policy

* Artifacts are never overwritten.
* Corrections require new commits.
* Hashes must match logged checksums.
* Deviations from capture protocol must be documented.
