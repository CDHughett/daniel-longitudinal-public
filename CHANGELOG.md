# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Detailed historical entries preceding the v1.1.0 release-candidate freeze are preserved in:

- [`docs/archive/CHANGELOG_PRE_V1.1.0.txt`](docs/archive/CHANGELOG_PRE_V1.1.0.txt)
- [`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records release-level repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### September 21 post-weekly-update validation-documentation drift cleanup

- Reconciled current-facing validation descriptions in `docs/START_HERE.md`, `DATASET_OVERVIEW.md`, `docs/FOR_OBSERVERS.md`, `data/DATA_COVERAGE.md`, and `methodology/README.md` with the live four-validator repository architecture.
- Centralized the evolving full validator inventory in `tools/README.md` and `VERIFICATION.md` where duplication was not necessary.
- Preserved more specific validator descriptions where they directly improve observer or dataset interpretation.
- Historical audits, archived documents, release notes, scientific data, weekly reports, phase state, protocol state, Model Error outcomes, DOI/release identity, and DQ-011 are unchanged.


### September 21 W37 closeout and W38 rollover

- Closed `reports/2026-W37.md` as the retrospective record for 2026-09-14 through 2026-09-20, preserving successful post-travel re-entry and the 2026-09-20 unofficial capacity probe as preliminary reserve evidence rather than an automatic progression trigger.
- Opened `reports/2026-W38.md` for 2026-09-21 through 2026-09-27 with weekly operating posture `Consolidation / reserve-replication observation`.
- Preserved the broader Phase 2 substate as `Consolidation / lock-in observation`; no Phase 2D declaration or protocol expansion was introduced.
- Advanced current-state pointers in `LATEST.md`, `README.md`, `INDEX.md`, `docs/OBSERVER_QUICKSTART.md`, and `docs/NEWCOMER_PATH.md` to W38 active / W37 closed.
- Synchronized README structured-coverage summaries with the governed W37 extension through 2026-09-20.
- Advanced `tools/validate_coherence.py` to protect W38/W37 current-state pointers and the new weekly posture while retaining the published v1.1.0 release identity and broader canonical substate.
- Corrected the live INDEX release orientation from the stale v1.0.0 label to the published v1.1.0 release without altering frozen release identity, tag, or DOI lineage.
- Model Error records 041–046, DQ-011, August snapshot state, release version, Git tag, and DOI state remain unchanged.
- Added `docs/audits/2026-09-21-post-weekly-rollover-audit.md` documenting append-only preservation, W37 arithmetic reproduction, lifecycle synchronization, privacy review, invariant checks, and the final CI gate.


### September 21 W37 machine-readable extension and provenance registration

- Extended governed public daily-biomarker and canonical sleep coverage through `2026-09-20`, producing 224 continuous daily rows in each dataset.
- Added 12 completed W37 training-session rows for 2026-09-15 through 2026-09-20, advancing the training dataset to 362 sessions through `2026-09-20`; 2026-09-14 remains represented as a zero-session day without a synthetic training row.
- Added four bounded W37 context events for the travel/rest continuation, yard-work workload, acute pre-sleep stress exposure, and unofficial end-of-week capacity probe, advancing the context index to 49 events.
- Preserved the corrected `2026-09-18 body_temp_f=96.31` value from the closed v1.31 source.
- Registered exact private-source provenance for `Daniel_Dataset_v1.31` (370,947 bytes; SHA-256 `58828f4a84900fa2cb0b6002539b8f5ae125b237c8c8f1e202427bc28142459a`) covering 2026-09-14 through 2026-09-20.
- Updated `data/DATA_COVERAGE.md` to the new live structured counts and endpoints.
- Reviewed two v1.31 free-text B1 HRV references that differ from the dedicated Daily Biomarkers HRV cells. The canonical public `daily_hrv_ms` extraction remains tied to the dedicated structured cells; private free-text notes remain unchanged and no inferred replacement was introduced.
- Preserved DQ-011 as open for the recorded 2026-09-08 daily resting-heart-rate value; no W37 source evidence resolves that earlier question.
- No weekly-report lifecycle, phase, protocol, model-error, August snapshot, published release, tag, or DOI state is changed by this batch.


### September 14 post-release coherence drift cleanup

- Reconciled `LATEST.md` to the published v1.1.0 version DOI `10.5281/zenodo.22759132` and all-versions DOI `10.5281/zenodo.20815611` rather than the prior v1.0.0 DOI.
- Reconciled `VERSIONING.md` to the published v1.1.0 state, including the finalized version DOI, all-versions DOI, and frozen release commit, while retaining the prior v1.0.0 DOI as historical release identity.
- Reconciled the current release-metadata and CI sections of `VERIFICATION.md` and documented the new fourth read-only coherence-validation layer without rewriting its dated historical version notes.
- Separated the immediate **weekly operating posture** (`Consolidation / re-entry observation`) from the broader Phase 2 **consolidation / lock-in observation** substate so short-term travel re-entry language does not appear to conflict with the canonical phase map.
- Updated observer and newcomer paths to use W36 as the most recent closed week and to describe the August TruDiagnostic / Record 043 state as complete rather than pending.
- Preserved historically correct pending/open language in dated contemporaneous documents rather than rewriting history.
- Added `tools/validate_coherence.py` to protect live release identity, DOI roles, weekly pointers, completed August orientation language, current versioning/verification surfaces, and weekly-versus-broader substate wording.
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
