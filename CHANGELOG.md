# Changelog

All notable changes to the Daniel Longitudinal Study public archive  
are documented in this file.

This changelog reflects **recent structural and repository updates only**.

Historical entries are preserved in:  
[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

---

## Scope

This changelog records:

- repository artifacts and structural updates
- dataset modifications
- methodology changes
- archive integrity adjustments

Biological interpretation belongs in `/reports`.

---

## [Unreleased]

### Added

- Added weekly report closeout for `reports/2026-W25.md`:
  - documents continued Phase 2 consolidation
  - records preserved daily B1 execution across the observation window
  - records preserved daily Load Integration under normal operating parameters
  - documents recovery-floor preservation under formal training, ordinary-life workload, household work, repository stewardship, and administrative demand
  - records lower-back mechanical signaling from W24 as resolved and non-limiting during W25
  - preserves interpretation that W25 represented repetition without degradation rather than performance expansion

- Added weekly report initialization for `reports/2026-W26.md`:
  - carries forward continued Phase 2 consolidation
  - preserves ambient execution monitoring
  - continues recovery-floor durability observation
  - continues trait-level work-capacity monitoring
  - adds holiday / schedule variability as a potential observation layer
  - maintains no-escalation posture during the July–August model-error observation window

- Appended sleep dataset entries for 2026-W25 (`2026-06-22` through `2026-06-28`) to `data/sleep_longitudinal_v1.csv`:
  - direct crossover from the current source dataset
  - no inferred or reconstructed values included
  - schema consistency preserved against longitudinal sleep structure
  - canonical sleep dataset extended through `2026-06-28`

- Added Zenodo DOI badge to `README.md`:
  - DOI: `10.5281/zenodo.20815612`

- Added citation section to `README.md` using the Zenodo-generated citation for `v1.0.0`.

- Added archive DOI reference to `LATEST.md`.

- Added Zenodo DOI to `CITATION.cff` following DOI issuance.

- Added 2026-06-24 Wednesday audit:
  - documents post-DOI repository integrity review
  - records passing checks for structure, links, CSV parsing, sleep continuity, report continuity, snapshot checksum verification, model-error continuity, and metadata presence
  - identifies observer-entry friction as the next documentation improvement layer

- Added `docs/OBSERVER_QUICKSTART.md`:
  - compact technical inspection route for researchers, skeptical readers, and outside observers
  - routes readers through archive posture, current state, data coverage, one report, one snapshot, model-error review, and governance boundaries

- Added open model error records 041–044:
  - recovery capacity during the July–August observation block
  - ambient execution plateau testing through the August snapshot window
  - August 2026 biological snapshot translation
  - protocol governance preservation through the next full snapshot cycle
 
- Added 2026-06-27 Saturday audit:
  - documents full-domain post-DOI repository review
  - records passing checks for structure, Markdown links, CSV parsing, sleep continuity, snapshot checksums, report continuity, model-error continuity, DOI / citation metadata, observer navigation, and governance posture
  - identifies `LATEST.md` active model-error visibility as the only minor current-state alignment recommendation

- Added Event 003 to `data/model_error/calibration_events_log.md`:
  - documents initialization of the July–August / August 2026 forward-prediction block
  - preserves calibration context for open model-error records 041–044
  - clarifies that the block does not change prediction methodology or UDI governance

### Changed

- Updated `LATEST.md` executive system dashboard to reflect:
  - `2026-W25` closed observation window
  - `2026-W26` active observation window
  - W25 sleep observations appended through `2026-06-28`
  - continued Phase 2 consolidation posture
  - recovery-floor durability under daily training and ordinary-life workload
  - resolved lower-back mechanical signaling from W24
  - normal weekly post-DOI archive stewardship
  - ongoing open model-error records 041–044 for the July–August / August 2026 observation window

- Updated current archive posture language from W25 active observation to W26 active observation:
  - replaced lower-back mechanical-resolution monitoring as a primary current emphasis with ambient execution preservation, ordinary-life workload absorption, holiday / schedule variability observation, and trait-level work-capacity monitoring
  - preserved recovery-floor durability as the primary reference condition
  - maintained no forward performance claims or protocol escalation language

- Updated active repository documentation to reflect Zenodo archival publication and post-release DOI availability.

- Improved `README.md` observer entry path:
  - added `First 5 Minutes` reading path
  - added `How to Evaluate This Archive` bridge
  - clarified depth-based routing through `START_HERE.md`, `OBSERVER_QUICKSTART.md`, `NEWCOMER_PATH.md`, and `INDEX.md`
  - routed external observers toward both compact and broader observer review paths

- Rewrote `docs/START_HERE.md` as a true 5-minute observer guide:
  - clarifies what the archive is and is not
  - identifies where evidence lives
  - explains how claims are limited
  - routes readers toward `OBSERVER_QUICKSTART.md`, `FOR_OBSERVERS.md`, `NEWCOMER_PATH.md`, and `INDEX.md`

- Updated `docs/NEWCOMER_PATH.md`:
  - clarified its role as the first 30–60 minute reading path
  - reduced overlap with `START_HERE.md`
  - reordered reading progression from simple orientation toward technical evaluation

- Updated `LATEST.md`:
  - added quick current-state summary
  - added post-DOI observer-pathway documentation posture
  - replaced residual pre-DOI maintenance language with post-DOI documentation-maintenance language
  - routed navigation to `docs/OBSERVER_QUICKSTART.md`

- Updated `docs/FOR_OBSERVERS.md`:
  - routed readers toward the new compact observer quickstart
  - clarified relationship between `OBSERVER_QUICKSTART.md`, `FOR_OBSERVERS.md`, `NEWCOMER_PATH.md`, and `INDEX.md`
  - reinforced evidence-first evaluation boundaries

- Updated `INDEX.md`:
  - added `docs/OBSERVER_QUICKSTART.md` to the complete repository map
  - added an observer evaluation layer
  - clarified first-contact, observer-evaluation, temporal, and full-reading flows
  - aligned the index with the post-DOI observer navigation structure

- Routed primary observer-facing documents and the complete repository index toward `docs/OBSERVER_QUICKSTART.md` to prevent the new quickstart from becoming an orphaned file.

- Expanded the model error layer from stability confirmation toward boundary-condition testing:
  - probes recovery reserve under accumulated stable exposure
  - tests whether ambient execution has reached a current adaptive ceiling
  - evaluates whether prolonged protocol stability translates into measurable biological change
  - audits protocol governance as a potential source of model error
 
- Updated `LATEST.md` to surface active model-error records 041–044:
  - recovery capacity during the July–August observation block
  - ambient execution plateau behavior through the August snapshot window
  - August 2026 biological snapshot translation
  - protocol-governance preservation through the next full snapshot cycle
  - aligned executive dashboard state with the model-error dataset and changelog

- Updated Model Error calibration documentation to reflect the post-DOI transition from completed May / W24 closures into the next active prospective observation block.

---

## [1.0.0] - 2026-06-23

### Added

- Release metadata locked for the initial DOI-bearing archival release:
  - `CODEMETA.json` version set to `1.0.0`
  - `CODEMETA.json` `dateModified` advanced to `2026-06-23`
  - `CITATION.cff` version set to `1.0.0`
  - `CITATION.cff` `date-released` set to `2026-06-23`

- Zenodo DOI minted for Daniel Longitudinal Study:
  - DOI: `10.5281/zenodo.20815612`

- Version `v1.0.0` archived and preserved through Zenodo.

- Repository transitioned to a citable scholarly dataset with permanent archival preservation.

---

### Changed

- `CODEMETA.json` updated:
  - `dateModified` advanced to `2026-06-23`
  - version advanced to `1.0.0`

- `CITATION.cff` updated:
  - version advanced to `1.0.0`
  - release date set to `2026-06-23`
  - DOI left unset until Zenodo DOI issuance

- Audit filename conventions normalized:
  - renamed `2026-06-13_saturday_audit.md`
  - aligned historical audit naming with repository standards

- `CHANGELOG.md` restructured:
  - migrated historical entries to `docs/archive/CHANGELOG_ARCHIVE.md`
  - reduced active changelog scope
  - improved repository legibility ahead of DOI release

- `LATEST.md` updated:
  - aligned repository activity references with changelog archive structure
  - distinguished recent repository activity from historical archived activity
  - clarified relationship between `CHANGELOG.md` and `docs/archive/CHANGELOG_ARCHIVE.md`
