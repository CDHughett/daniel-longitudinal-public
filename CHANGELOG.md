# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Detailed historical entries preceding the v1.1.0 release-candidate freeze are preserved in:

- [`docs/archive/CHANGELOG_PRE_V1.1.0.md`](docs/archive/CHANGELOG_PRE_V1.1.0.md)
- [`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records release-level repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

No post-v1.1.0-candidate changes are currently registered.

---

## [1.1.0] - 2026-09-14

### Added

- Completed and integrated the August 2026 coordinated biological/performance snapshot across DEXA, VO₂, Bod Pod/COSMED, TruAge, Advanced TruAge, and TruHealth source artifacts.
- Added snapshot-specific cross-layer validation protecting the August structured row, epigenetic layer, source-role reconciliation, Model Error 043 closure, checksum manifest, and seven protected August source artifacts.
- Added a governed machine-readable public layer for daily biomarkers, training exposure, and contextual events, while retaining canonical sleep as a separately governed daily dataset.
- Added explicit private-source provenance registration for retained `Daniel_Dataset` source states when immutable files were available for hashing.
- Added and maintained bounded data-quality records, including DQ-011 for the recorded 2026-09-08 resting-heart-rate value pending source verification.
- Added post-snapshot, weekly-rollover, and v1.1.0 release-readiness audits.

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

The full pre-v1.1.0 live changelog, including detailed commit-level and audit-level entries accumulated under `[Unreleased]`, is preserved byte-for-byte at [`docs/archive/CHANGELOG_PRE_V1.1.0.md`](docs/archive/CHANGELOG_PRE_V1.1.0.md).

Earlier archived changelog history remains at [`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md).
