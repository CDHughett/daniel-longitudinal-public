# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Detailed historical entries preceding the v1.1.0 release-candidate freeze are preserved in:

- [`docs/archive/CHANGELOG_PRE_V1.1.0.txt`](docs/archive/CHANGELOG_PRE_V1.1.0.txt)
- [`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records release-level repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### September 14 post-release coherence drift cleanup

- Reconciled `LATEST.md` to the published v1.1.0 version DOI `10.5281/zenodo.22759132` and all-versions DOI `10.5281/zenodo.20815611` rather than the prior v1.0.0 DOI.
- Separated the immediate **weekly operating posture** (`Consolidation / re-entry observation`) from the broader Phase 2 **consolidation / lock-in observation** substate so short-term travel re-entry language does not appear to conflict with the canonical phase map.
- Updated observer and newcomer paths to use W36 as the most recent closed week and to describe the August TruDiagnostic / Record 043 state as complete rather than pending.
- Preserved historically correct pending/open language in dated contemporaneous documents rather than rewriting history.
- Added `tools/validate_coherence.py` to protect live release identity, DOI roles, weekly pointers, completed August orientation language, and weekly-versus-broader substate wording.
- Added the coherence validator to GitHub Actions and documented it in `tools/README.md`.
- Added `docs/audits/2026-09-14-post-release-coherence-drift-cleanup.md` documenting the repair scope and preservation boundary.

### September 14 post-publication reconciliation

- Reconciled `CITATION.cff` to the authoritative finalized v1.1.0 Zenodo version DOI `10.5281/zenodo.22759132` after external publication.
- Recorded the Zenodo all-versions DOI `10.5281/zenodo.20815611` in release-facing metadata and documentation.
- Recorded the published GitHub `v1.1.0` tag boundary at frozen commit `92126e1cc882c3822d9e03b30b11cfc1d30b4fbb` and release-package SHA-256 `f7bad6d466c28d85fc263128083fe37d9039cb116cff67fb1c8a35482d5ce0a9`.
- Added the Batch 5B publication-reconciliation audit and updated the v1.1.0 release notes from candidate state to published state.
- Disclosed the immutable intermediate Zenodo record labeled `v1.1.0` (`10.5281/zenodo.22759127`) while designating `10.5281/zenodo.22759132` as the finalized version-specific DOI for the frozen Batch 5A package.
- Updated release-metadata validation semantics to accept the authoritative post-publication v1.1.0 DOI without changing canonical data, scientific interpretation, phase state, protocol state, or the frozen release tag.

---

## [1.1.0] - 2026-09-14

### Added

- Completed and integrated the August 2026 coordinated biological/performance snapshot across DEXA, VO₂, Bod Pod/COSMED, TruAge, Advanced TruAge, and TruHealth source artifacts.
- Added snapshot-specific cross-layer validation protecting the August structured row, epigenetic layer, source-role reconciliation, Model Error 043 closure, checksum manifest, and seven protected August source artifacts.
- Added a governed machine-readable public layer for daily biomarkers, training exposure, and contextual events, while retaining canonical sleep as a separately governed daily dataset.
- Added explicit private-source provenance registration for retained `Daniel_Dataset` source states when immutable files were available for hashing.
- Added and maintained bounded data-quality records, including DQ-011 for the recorded 2026-09-08 resting-heart-rate value pending source verification.
- Added post-snapshot, weekly-rollover, and v1.1.0 release-readiness audits.
- Added a read-only release-candidate packaging workflow that creates an exact-commit ZIP, reruns all validators from the extracted package, reparses structured CSVs, screens for private spreadsheet/workbook filenames, inventories packaged files, computes SHA-256, and uploads the verified package as a temporary Actions artifact.

### Changed

- Closed the recent protected Model Error block 041–046, including Record 043 as `overall_improvement_not_met` / not supported / `over`, without rewriting the original prediction or scoring window.
- Expanded public structured coverage through 2026-09-13 to 217 daily-biomarker rows, 217 canonical sleep rows, 350 completed training-session rows through 2026-09-12, and 45 bounded context events.
- Corrected training-endpoint validation semantics so a represented day with zero completed training sessions does not require a synthetic training row.
- Hardened repository validation around weekly lifecycle continuity, current-state synchronization, machine-readable schema/provenance rules, protected historical training rows, source-artifact checksums, and August snapshot consistency.
- Completed source-backed August Bod Pod structured fields after Record 043 adjudication; this supplemental completion does not rescore Record 043.
- Aligned release-facing metadata to candidate version `1.1.0` dated 2026-09-14 while retaining the existing Zenodo DOI identifier pending authoritative external version-DOI verification during publication.
- Preserved W37 as the active weekly observation window and W36 as the most recent closed window; no release-driven phase or protocol transition was introduced.

### Release boundaries and limitations

- The archive remains a single-subject longitudinal observational record, not a clinical trial or population-level efficacy claim.
- Open or restricted data-quality items remain disclosed, including historical sleep reconciliation notes and DQ-011; no unsupported replacement values were introduced to make the release cleaner.
- Exact private-source hashes remain unavailable for some historical workbook versions and are explicitly left missing rather than reconstructed.
- The current training architecture remains B1 + Load Integration under Phase 2; Phase 2D remains undeclared.
- The v1.1.0 candidate does not itself create a final Git tag, GitHub release, Zenodo version, or authoritative new version DOI.

Release notes: [`docs/releases/v1.1.0.md`](docs/releases/v1.1.0.md)

---

## Historical detail

The full pre-v1.1.0 live changelog, including detailed commit-level and audit-level entries accumulated under `[Unreleased]`, is preserved byte-for-byte at [`docs/archive/CHANGELOG_PRE_V1.1.0.txt`](docs/archive/CHANGELOG_PRE_V1.1.0.txt).

Earlier archived changelog history remains at [`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md).
