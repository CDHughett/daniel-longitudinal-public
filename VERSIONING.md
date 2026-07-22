# Versioning Protocol

This repository uses structured version control to preserve longitudinal integrity, provenance, and public-release clarity.

The archive is treated as a governed longitudinal system rather than a personal log.

Versioning distinguishes between:

- ordinary repository commits
- material archive-state changes
- Git tags
- formal public releases
- Zenodo archival deposits
- exceptional privacy or integrity repairs

Not every commit requires a version increment or archival release.

---

## Version Format

Formal releases use semantic versioning:

```text
vMAJOR.MINOR.PATCH
```

Example:

```text
v1.2.1
```

Where:

- `MAJOR` represents a material change to archive architecture or governing interpretation
- `MINOR` represents a new compatible observation, dataset, or evaluation milestone
- `PATCH` represents a compatible correction, repair, or documentation refinement

Git tags include the leading `v`.

Metadata files record the numeric version without requiring the leading `v` unless their format specifies otherwise.

---

## Current Release State

The first DOI-bearing public release is:

```text
v1.0.0
```

Release date:

```text
2026-06-23
```

Zenodo DOI:

```text
10.5281/zenodo.20815612
```

Repository work after that release remains under:

```text
[Unreleased]
```

until a later formal release is declared.

---

# Repository Commits Versus Releases

## Ordinary Commits

Most repository changes are ordinary commits.

Examples include:

- weekly report initialization
- weekly report closeout
- new audit records
- current-state updates
- changelog maintenance
- source-export preservation
- checksum additions
- source-backed corrections
- documentation clarification
- navigation improvements
- model-error candidate-evidence notes

These changes are version controlled immediately but do not automatically require:

- a version-number change
- a new Git tag
- a Zenodo deposit
- a DOI update
- a formal release

Ordinary commits accumulate beneath the active `[Unreleased]` changelog section.

---

## Formal Releases

A formal release represents a meaningful, externally identifiable archive state.

A release should provide a coherent checkpoint rather than merely reflect elapsed time or commit count.

Potential release checkpoints include:

- completion of a coordinated biological snapshot cycle
- closure of a registered model-error block
- publication of a new canonical longitudinal dataset
- completion of a meaningful methodological expansion
- transition to a retrospectively supported phase classification
- a major archive-integrity or governance milestone
- a stable package suitable for external citation

A release should not be created solely because:

- one weekly report was added
- one audit was completed
- one source export was preserved
- minor wording changed
- a routine checksum was updated
- a scheduled date arrived

---

# Version Types

## Patch Release — `vX.Y.Z`

A patch release preserves the existing archive architecture and interpretation model.

Typical patch-release triggers include:

- source-backed correction of canonical values
- correction of dates, units, or field mappings
- repair of broken links or metadata
- checksum or artifact-integrity correction
- privacy remediation
- replacement of an incorrectly distributed artifact
- clarification that does not alter the governing methodology
- correction of release packaging
- non-breaking documentation alignment

Patch releases should not introduce:

- a new major observation cycle
- a new governing prediction framework
- a breaking schema change
- a new phase declaration
- a material reinterpretation of prior outcomes

Example:

```text
v1.0.1
```

---

## Minor Release — `vX.Y.0`

A minor release adds a meaningful compatible archive capability, observation block, or dataset while preserving the existing architecture.

Potential minor-release triggers include:

- completion of a new coordinated biological snapshot cycle
- addition of a new canonical structured dataset
- closure of a registered prediction block
- addition of a reproducible transformation pipeline
- publication of a substantial new longitudinal evidence layer
- completion of a major retrospective report
- addition of a new governed analytical capability
- expansion of public data coverage without breaking existing schemas

Examples may include:

- August 2026 snapshot completion and integration
- publication of new structured wearable datasets, if later justified
- closure and scoring of Model Error records 041–044
- addition of a governed perturbation-event dataset

Example:

```text
v1.1.0
```

A minor release may include accumulated patch-level changes since the previous release.

---

## Major Release — `vX.0.0`

A major release represents a breaking or conceptually material evolution of the archive.

Potential major-release triggers include:

- fundamental repository-architecture change
- breaking canonical-schema revision
- redefinition of core measurement semantics
- replacement of the governing prediction or calibration framework
- material change to phase-declaration rules
- change to the primary archive evidence hierarchy
- migration that makes earlier analytical procedures incompatible
- change in the fundamental scope or purpose of the archive

Examples may include:

- replacing the current model-error framework with an incompatible successor
- restructuring canonical datasets in a way that breaks prior consumers
- redefining the meaning of primary observation dates
- introducing a materially different archive-governance model

Example:

```text
v2.0.0
```

A major release should include explicit migration and compatibility notes.

---

# Changes That Do Not Automatically Trigger a Release

The following normally remain ordinary commits:

- weekly reports
- `LATEST.md` updates
- routine audits
- new acquisition-date source-export folders
- checksum manifests
- README navigation
- typo corrections
- formatting changes
- clarification of already-governed concepts
- preservation of candidate evidence
- open data-quality notes
- planned-work documentation
- changes to inactive or historical protocol descriptions

These changes may still be included in the next formal release.

---

# Source-Export Versioning

Periodic provider exports are preserved by acquisition date.

Example:

```text
data/source_exports/ringconn/2026-07-21/
```

A new source-export acquisition should include:

- original provider files
- acquisition README
- checksum manifest
- changelog entry when materially relevant

A periodic export does not require a repository release by itself.

Overlapping exports remain separate acquisition events.

A later export does not overwrite an earlier export.

Source exports become part of the next formal archive package unless a separate release is justified by a material analytical or preservation need.

---

# Snapshot and Report Versioning

## Snapshots

Snapshots preserve primary measurement artifacts and capture context.

Examples include:

- DEXA
- Bod Pod
- laboratory testing
- TruDiagnostic outputs
- VO₂ testing
- milestone artifacts

Snapshots are source evidence.

A new snapshot artifact does not automatically require an immediate release.

A coordinated snapshot cycle may justify a minor release after:

- all planned artifacts are collected
- checksums are verified
- privacy review is complete
- structured values are integrated
- interpretation is closed retrospectively
- applicable model-error records are evaluated
- metadata and changelog are aligned

---

## Reports

Reports are interpretive and documentary layers derived from observation, structured data, and source evidence.

Weekly reports are committed as ordinary repository work.

They do not independently trigger minor releases.

A major retrospective synthesis or phase-closeout report may contribute to a minor or major release when it marks a material archive-state transition.

Snapshots and reports should normally be committed separately to preserve provenance.

---

# Data and Schema Versioning

## Canonical Datasets

Canonical dataset filenames may include explicit schema versions.

Example:

```text
sleep_longitudinal_v1.csv
```

A filename version identifies the dataset schema, not the repository release.

Small source-backed corrections do not require a new dataset filename when:

- the field structure is unchanged
- field meanings are unchanged
- corrections remain compatible with existing consumers

A new dataset schema version is required when:

- columns are removed or materially redefined
- primary-key behavior changes
- date semantics change
- units change incompatibly
- missingness conventions change incompatibly
- prior rows cannot be interpreted under the new definition

Example:

```text
sleep_longitudinal_v2.csv
```

The prior schema should remain preserved or accompanied by migration documentation.

---

## Source Exports

Source exports are not assigned archive-defined schema versions.

They retain:

- provider field names
- provider structure
- original bytes
- acquisition-date provenance

Any future normalized or transformed dataset must be versioned separately from its source export.

---

# Prediction and Model-Error Versioning

Open prediction records are not rewritten to match later outcomes.

Corrections to administrative fields may be made only when:

- the correction is source-supported
- the original prediction meaning is preserved
- the correction is documented
- outcome knowledge does not influence prediction wording

Closing or scoring a model-error record does not require an immediate repository release.

Closure of a coherent prediction block may justify a minor release.

Changes to the underlying prediction-evaluation framework may justify:

- a minor release when compatible
- a major release when earlier records become methodologically incompatible

---

# Phase Versioning

Phase declarations are retrospective archive states.

A phase label must not be advanced merely to support a release.

A retrospectively supported phase transition may justify a minor release when:

- phase criteria are satisfied
- supporting evidence is documented
- applicable observation windows have closed
- contradictory evidence is addressed
- the declaration does not depend on release timing

A fundamental redefinition of the phase framework may require a major release.

---

# Changelog Requirements

`CHANGELOG.md` records notable repository, dataset, methodology, governance, and archive-integrity changes.

Not every commit requires a separate changelog bullet.

The changelog should capture changes that materially affect:

- archive interpretation
- public evidence coverage
- canonical datasets
- source availability
- methodology
- governance
- privacy
- artifact integrity
- model-error state
- release state

Routine commits may be grouped under one coherent changelog entry.

Historical changelog entries are preserved in:

```text
docs/archive/CHANGELOG_ARCHIVE.md
```

---

# Definition and Source Documentation

Changes affecting measurement definitions should update the applicable documents.

Potentially affected files include:

- `DATA_DICTIONARY.md`
- `MEASUREMENT_SOURCES.md`
- `METHODOLOGY_AND_CONTROLS.md`
- `methodology/data-collection.md`
- `data/DATA_COVERAGE.md`
- `data/DATA_QUALITY_NOTES.md`
- `GOVERNANCE.md`

Not every definition clarification requires a version release.

The release level depends on compatibility and materiality.

---

# Release Candidate Tags

Release-candidate tags may be used before a formal release.

Format:

```text
vX.Y.Z-rc1
vX.Y.Z-rc2
```

Release candidates may be used to verify:

- archive packaging
- checksums
- metadata
- links
- privacy
- source-artifact inclusion
- dataset parsing
- release reproducibility

Release-candidate tags are not formal public releases unless explicitly published as such.

They may be replaced during pre-release verification.

The final release tag should identify the approved archival state.

---

# Git Tags

Formal release tags should be annotated when practical.

Example:

```text
v1.1.0
```

A release tag should correspond to:

- a clean working tree
- verified repository state
- completed release audit
- aligned metadata
- aligned changelog
- privacy-reviewed public artifacts
- validated checksums
- the exact source used to create the archival package

Tags should not normally be moved after public release.

Exceptions are limited to controlled privacy or integrity remediation.

---

# Zenodo Release Practice

Zenodo deposits represent formal archival releases, not routine repository activity.

A new Zenodo version should normally be created when:

- a formal repository release is declared
- the archive reaches a meaningful stable checkpoint
- new public evidence materially expands the citable archive
- a completed biological snapshot cycle is integrated
- a prediction block is formally closed
- a major dataset or methodology becomes public

The Git tag, repository metadata, and Zenodo version should align.

Relevant metadata may include:

- `CITATION.cff`
- `CODEMETA.json`
- `README.md`
- `LATEST.md`
- `CHANGELOG.md`

---

# Privacy and Integrity Repairs

Privacy or artifact-integrity failures are exceptional.

When sensitive or incorrect material has entered public distribution:

1. restrict access when possible
2. preserve sanitized replacement evidence
3. determine affected branches, tags, releases, and external archives
4. rewrite Git history when required
5. restore sanitized artifacts to applicable surviving refs
6. regenerate checksums
7. verify all rewritten branches and tags
8. force-update remote refs only after local verification
9. contact hosting support for inaccessible cached or orphaned objects when appropriate
10. repair external archival packages
11. document the event without reproducing the sensitive content

A privacy repair may be handled as:

- an in-place release repair when the archival platform explicitly permits controlled file editing
- a patch release when an immutable new version is required
- a history rewrite when the sensitive object remains reachable through Git refs

The release number need not change when:

- the platform permits a controlled repair of the existing deposit
- the substantive findings and interpretation remain unchanged
- the repair replaces sensitive material with the intended sanitized artifact
- the repair is fully verified and documented

Such an action must still be recorded in:

- the repository changelog
- the applicable audit
- privacy or anonymization documentation
- release notes when appropriate

---

# History Rewrite Rules

Git history rewrites are prohibited for ordinary cleanup.

They are reserved for cases such as:

- sensitive-data removal
- malicious content removal
- legally required removal
- severe repository-corruption repair
- invalid large-file objects that prevent repository operation

Before rewriting history:

- create isolated working copies
- preserve sanitized current artifacts
- record pre-rewrite refs
- inspect all branches and tags
- identify affected releases
- prepare recovery evidence
- verify tool version and procedure

After rewriting history:

- verify old sensitive commits are unreachable from active refs
- restore required sanitized artifacts
- verify checksums
- verify branch and tag maps
- force-update the remote in a controlled sequence
- notify collaborators that old clones must not be merged or pushed
- obtain hosting-provider assistance for cached or orphaned objects when necessary

Old clones must be discarded or permanently isolated after a privacy rewrite.

---

# Release Preparation Checklist

Before a formal release:

1. confirm the intended version number
2. close or defer applicable open work
3. verify repository status is clean
4. parse all structured datasets
5. validate schema and row consistency
6. verify relative links
7. verify artifact checksums
8. review data-quality notes
9. review privacy and anonymization
10. verify model-error status
11. verify phase language
12. update `CHANGELOG.md`
13. update `LATEST.md`
14. update `README.md` when needed
15. update `CITATION.cff`
16. update `CODEMETA.json`
17. create a release candidate when useful
18. generate the release archive from the approved commit
19. inspect archive contents
20. verify archive hashes
21. create the final Git tag
22. publish the corresponding archival deposit
23. download and verify the published archive
24. record the release outcome in an audit

---

# Release Audit

Every formal release should have a release audit confirming:

- exact commit
- exact tag
- exact package
- file inventory
- CSV parsing
- link integrity
- checksum integrity
- privacy disposition
- metadata alignment
- model-error disposition
- unresolved limitations
- public archive status

The audit should distinguish:

- repository integrity
- data integrity
- semantic confidence
- privacy status
- release readiness

---

# Release Cadence

The repository does not use a mandatory calendar-based release cadence.

Releases are milestone based.

Likely release opportunities include:

- coordinated biological snapshot cycles
- completed prediction blocks
- phase closeouts
- major structured-data additions
- significant methodological stabilization

Routine weekly work remains available through the live repository without requiring a new DOI-bearing release.

---

# Versioning Examples

## Weekly Closeout Only

Changes:

- close weekly report
- initialize next week
- update `LATEST.md`
- update sleep rows

Disposition:

```text
Ordinary commits under [Unreleased]
No release required
```

---

## Source Export Added

Changes:

- add periodic RingConn CSV exports
- add acquisition README
- add checksums
- update coverage and data-quality documentation

Disposition:

```text
Ordinary commits under [Unreleased]
No immediate release required
```

---

## Source-Backed Data Correction

Changes:

- correct several canonical sleep fields
- document source
- update data-quality status
- update changelog

Disposition:

```text
Ordinary correction commits
Include in next release
Patch release optional if immediate public correction is required
```

---

## Completed August Snapshot

Changes:

- add TruDiagnostic artifacts
- add DEXA
- add VO₂ max
- add Bod Pod
- integrate structured results
- evaluate applicable model-error records
- complete retrospective report

Potential disposition:

```text
Minor release candidate
Example: v1.1.0
```

The release number should be assigned only after the completed archive state is reviewed.

---

## Breaking Schema Migration

Changes:

- redefine canonical sleep date
- replace schema
- require downstream migration
- make prior processing incompatible

Potential disposition:

```text
Major release candidate
Example: v2.0.0
```

---

# Governing Principle

Version numbers should describe meaningful archive states.

They should not be used as a reward for activity, a substitute for evidence, or a reason to force interpretation.

The live repository may change frequently.

Formal releases should remain:

- stable
- auditable
- reproducible
- privacy reviewed
- externally meaningful
- proportionate to the actual archive transition
