# Versioning Protocol

This repository follows structured version control to preserve longitudinal integrity.

The archive is treated as a governed system, not a personal log.

---

## Version Types

### Patch (vX.X.1)

Minor documentation updates.
Formatting corrections.
No change to data or interpretation.

---

### Minor (vX.1.0)

Addition of:

* New snapshot capture
* New report file
* New experiment entry

No structural changes to repository architecture.

---

### Major (vX.0.0)

Structural modifications to:

* Repository architecture
* Folder organization
* Measurement definitions
* Governance rules
* Schema updates

Major versions indicate system evolution.

---

## Release Practice

Version tags should reflect material structural states of the repository.

Example:

v0.1 — Initial governed archive structure  
v0.2 — First multi-snapshot cycle complete  
v1.0 — Confirmed multi-phase longitudinal continuity  

---

## Snapshot vs Report

Snapshots:
Immutable primary data.

Reports:
Interpretive layer derived from snapshots.

They are committed separately.

---

## Change Logging

All material commits must be reflected in:

`CHANGELOG.md`

Changes affecting definitions must also update:

`DATA_DICTIONARY.md`
`MEASUREMENT_SOURCES.md`
