# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Detailed historical entries preceding the v1.1.0 release-candidate freeze are preserved in:

- [`docs/archive/CHANGELOG_PRE_V1.1.0.txt`](docs/archive/CHANGELOG_PRE_V1.1.0.txt)
- [`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records release-level repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### September 29 validation-hardening audit

- Added `docs/audits/2026-09-29-validation-hardening-audit.md` covering the legacy temperature-field semantic boundary, the new latest-weekly-rollover validator, validator-inventory anti-drift, release-candidate package coverage, change boundaries, and preserved scientific/release invariants.
- Confirmed the new weekly-rollover validator independently reproduces W38 from committed public data as 230.2 lb morning bodyweight, 67.1 ms daily HRV, 44.9 bpm resting HR, 60.4 bpm daily average HR, 73.7 ms sleep HRV, 50.7 bpm sleep HR, 7h29m total sleep, 1h16m deep sleep, 58m REM, 6 B1 sessions, 5 Load Integration sessions, and 556 formal training minutes.
- Confirmed PR validation passes all five current Python validators on the hardening branch.
- Final merge readiness remains contingent on a green validation run including this audit artifact/changelog entry and, after merge, a successful main-branch release-candidate package verification because that workflow is part of the hardening scope.


### September 29 weekly-rollover and temperature-semantics hardening

- Clarified the legacy v1 `body_temp_f` field across `DATA_DICTIONARY.md`, `schemas/machine-readable-layer-v1.md`, and `MEASUREMENT_SOURCES.md`: RingConn-derived Daily Biomarkers values represent wearable skin temperature, not clinical/core body temperature.
- Preserved the existing `body_temp_f` column and all historical values for v1 backward compatibility; no data rewrite or inferred temperature correction was introduced.
- Added `tools/validate_weekly_rollover.py`, a read-only validator that dynamically identifies the newest active and immediately preceding closed weekly reports, verifies contiguous seven-day windows, recomputes the latest closed report's structured weekly metrics from committed daily/sleep/training data, checks B1/Load Integration exposure notes, and requires an exact registered private-source manifest entry for the closed observation window.
- Added the latest weekly rollover validator to the normal pull-request/push validation workflow and to current observer/verification documentation.
- Hardened `tools/validate_coherence.py` so the weekly-rollover validator cannot silently disappear from current validation documentation or observer navigation.
- Expanded release-candidate package verification to run the complete current validator suite both before packaging and again from the extracted immutable archive, including the previously omitted post-release coherence validator.
- No scientific data row, weekly report result, phase declaration, training prescription, Model Error outcome, DQ status, August snapshot interpretation, published release identity, Git tag, or DOI lineage is changed by this hardening batch.


### September 29 W38/W39 post-rollover audit

- Added `docs/audits/2026-09-29-post-weekly-rollover-audit.md` covering source identity, exact historical-prefix preservation, W38 arithmetic reproduction, canonical sleep semantics, training/context representation, weekly lifecycle, current-state synchronization, privacy, release/phase/model-error invariants, and CI.
- The audit reproduced W38 from the public structured layer: 230.2 lb morning bodyweight, 67.1 ms daily HRV, 44.9 bpm resting HR, 60.4 bpm daily average HR, 73.7 ms sleep HRV, 50.7 bpm sleep HR, 7h29m total sleep, 1h16m deep sleep, 58m REM, and 556 formal training minutes.
- Corrected one narrow derived W38 bodyweight-comparison sentence: the difference between the unrounded W37 and W38 six-measurement means is approximately 2.3 lb. The prior 2.4-lb wording resulted from subtracting separately rounded display means; no underlying daily weight or reported weekly mean changed.
- Confirmed exact append-only preservation of the five governed public/provenance files and retained the 2026-09-27 zero-session day without a synthetic training row.
- Confirmed W39 active / W38 closed lifecycle, `Consolidation / post-travel return observation` weekly posture, unresolved reserve replication, undeclared Phase 2D status, closed Model Error 041–046 state, unresolved DQ-011, and fixed v1.1.0 release/DOI identity.
- Privacy review found no newly introduced direct contact/location identifiers, private names screened during source lock, private binary artifact, or unnecessary travel/family detail.
- The corrected pre-audit content head passed all four repository validation layers. Final merge readiness remains contingent on a green validation run including this audit artifact and changelog entry.


### September 29 W39 current-state synchronization

- Advanced `LATEST.md`, `README.md`, and `INDEX.md` to W39 active / W38 closed while preserving the broader Phase 2 `Consolidation / lock-in observation` substate.
- Reframed the immediate weekly posture as `Consolidation / post-travel return observation`: travel-directed omissions are not training debt, ordinary return is observed before progression, and the unresolved reserve question remains secondary until normal conditions are restored.
- Updated README and LATEST machine-readable summaries to the governed W38 extension: 231 daily rows through 2026-09-27, 231 canonical sleep rows through 2026-09-27, 373 completed training sessions through 2026-09-26, and 50 bounded context events through 2026-09-27.
- Advanced `docs/OBSERVER_QUICKSTART.md` and `docs/NEWCOMER_PATH.md` so the most recent closed report is W38 and the weekly-versus-broader state distinction reflects the W39 posture.
- Advanced `tools/validate_coherence.py` to protect W39 active / W38 closed pointers and the post-travel return posture while retaining the published v1.1.0 release identity and canonical broader substate.
- No scientific data, phase declaration, training prescription, Model Error outcome, DQ status, August snapshot interpretation, published release identity, Git tag, or DOI lineage is changed by this synchronization batch.


### September 29 W38 closeout and W39 initialization

- Closed `reports/2026-W38.md` as the retrospective record for 2026-09-21 through 2026-09-27.
- Preserved the Week 38 reserve-replication question as unresolved because no second interpretable capacity probe occurred; repeated subjective ease was not converted into a progression claim.
- Recorded Week 38's primary retrospective finding as governed consolidation: repeated ease did not trigger escalation, and travel-directed omissions did not trigger compensatory workload or training debt.
- Opened `reports/2026-W39.md` for 2026-09-28 through 2026-10-04 with weekly operating posture `Consolidation / post-travel return observation`.
- Carried forward the lower observed bodyweight state, the unresolved reserve/progression question, the 2026-09-18 supplementation-context boundary, DQ-011, and undeclared Phase 2D status without strengthening any of them beyond the source evidence.
- Preserved Model Error records 041–046 as closed and introduced no new formal prediction, protocol expansion, recovery intervention, release identity, Git tag, or DOI change.
- Current-facing pointer synchronization is handled in the companion rollover batch before this draft PR becomes merge-ready.


### September 29 W38 machine-readable extension and provenance registration

- Extended governed public daily-biomarker and canonical sleep coverage through `2026-09-27`, producing 231 continuous daily rows in each dataset.
- Added 11 completed W38 training-session rows through `2026-09-26`, advancing the training dataset to 373 sessions; 2026-09-27 remains represented as a zero-session day without a synthetic training row.
- Added one bounded W38 travel/context event covering the 2026-09-26 through 2026-09-27 portion of an out-of-town travel period, advancing the context index to 50 events while preserving that the travel interval continued beyond the W38 report window.
- Registered exact source provenance for `Daniel_Dataset_v1.32` (368,070 bytes; SHA-256 `a9f03dde03a8b71846ede5fdec3214fe9009b93fca27c54f4bf587107a38a870`) covering 2026-09-21 through 2026-09-27.
- Preserved mixed source-date encoding through controlled ISO date-index normalization without changing associated biological, sleep, or training values.
- Preserved explicit Sleep Log awake totals rather than deriving `awake_min` from time-in-bed minus total sleep.
- Kept the W38 travel representation privacy-minimized and limited to analytically relevant context.
- Updated `data/DATA_COVERAGE.md` to the new live structured counts and endpoints.
- No W38 report lifecycle, phase, protocol, Model Error, DQ, August snapshot, published release, Git tag, or DOI state is changed by this batch.


### September 22 supplementation-architecture disclosure

- Added `protocols/supplementation-architecture-2026-09-18.md` to preserve a material supplementation transition effective 2026-09-18 and first disclosed to the public archive on 2026-09-22.
- Preserved the distinction between effective exposure date and documentation date; the change was not represented as contemporaneous evidence in the completed `Daniel_Dataset_v1.31` source.
- Added an explicitly labeled post-closeout disclosure to `reports/2026-W37.md` without changing its quantitative values, closeout decision, reserve interpretation, Model Error state, phase state, or DQ-011.
- Added the supplementation transition as active protocol context in `reports/2026-W38.md` and `LATEST.md`, with possible sleep/resting-HR observations retained as hypothesis-generating rather than causal.
- Added direct protocol discoverability in `INDEX.md`.
- Did **not** create a new `data/context_events_v1.csv` row because the current v1 schema requires canonical private-source provenance and the transition was not preserved in v1.31; no source locator was fabricated to manufacture structured completeness.
- No B1 or Load Integration prescription, phase declaration, Model Error outcome, DQ status, August snapshot interpretation, published release identity, Git tag, or DOI lineage is changed by this batch.

### September 21 observer-legibility hardening and simulation audit

- Expanded `tools/validate_coherence.py` rather than creating a fifth validator, adding anti-drift checks for current-facing validation-documentation roles, task-based first-contact navigation, plain-language current-state bridges, and preservation of the deeper terminology layer.
- Protected the distinct roles of README, START_HERE, OBSERVER_QUICKSTART, NEWCOMER_PATH, FOR_OBSERVERS, and INDEX so future edits do not silently recreate competing mandatory reading paths.
- Added checks preventing stale two-validator wording from returning to the current-facing validation documents cleaned in Batch 1.
- Added checks preventing stacked `low-salience`, `trait-like`, and `trait-level` session jargon from returning to README/LATEST while requiring the precise glossary definitions to remain available in `docs/CONCEPTS.md`.
- Updated `tools/README.md` and `VERIFICATION.md` to document the expanded coherence boundary.
- Added `docs/audits/2026-09-21-post-audit-legibility-observer-simulation.md` with casual-reader, skeptical-reviewer, and data-analyst simulations of the completed cleanup stack.
- No scientific data, weekly report evidence, protocol, phase declaration, Model Error outcome, DQ status, release identity, Git tag, or DOI lineage is changed by this batch.


### September 21 live-facing language simplification

- Added a plain-language current-state summary to `README.md` and `LATEST.md` before the formal phase/substate/posture labels.
- Replaced stacked front-surface execution descriptors such as `low-salience / ambient / trait-like / trait-level` with the parent phrase `low-overhead` where a first-contact reader does not need session-level classification detail.
- Preserved the precise execution vocabulary in `docs/CONCEPTS.md`, closed/active weekly reports, and the structured training layer rather than flattening the underlying research record.
- Added direct glossary routing from the live state surfaces for reserve, capacity versus exposure, weekly operating posture, B1, and Load Integration.
- Kept the current W38 reserve-replication question, broader consolidation/lock-in substate, Phase 2 declaration, DQ-011 status, Model Error outcomes, release identity, tag, and DOI lineage unchanged.


### September 21 first-contact navigation compression

- Reduced the README first-contact table to five task-based entry points: understand the project, see current state, inspect structured evidence, audit claims, or browse the full index.
- Removed circular orientation instructions that required readers arriving from README/START_HERE to reread the same front-door documents.
- Established `docs/OBSERVER_QUICKSTART.md` as the single short ordered audit route.
- Reframed `docs/NEWCOMER_PATH.md` as an optional extended learning curriculum rather than a prerequisite.
- Reframed `docs/FOR_OBSERVERS.md` as a skeptical-review reference/checklist rather than a competing linear route.
- Updated `INDEX.md` so first-contact navigation is task-based and the live validator inventory remains centralized in `tools/README.md`.
- No scientific data, weekly report, current system state, protocol, phase declaration, Model Error outcome, DQ status, release identity, tag, or DOI lineage is changed by this batch.


### September 21 terminology bridge and state-label compression

- Expanded `docs/CONCEPTS.md` with plain-language definitions for weekly operating posture, Data-Quality (DQ) records, capacity versus exposure, and reserve as a capacity concept.
- Expanded the B1 and Load Integration glossary entries with concrete current-implementation descriptions while keeping exact prescription details governed by the training record.
- Added a compact state-label hierarchy to `docs/START_HERE.md` showing the relationship among declared phase, broader operating substate, weekly operating posture, and session-level observations.
- Explicitly documented that lower-level evidence such as one reserve observation does not automatically change prescription, substate, or phase.
- No dataset value, weekly report, protocol, phase declaration, Model Error outcome, DQ status, release identity, tag, or DOI lineage is changed by this batch.


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
