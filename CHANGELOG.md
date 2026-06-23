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

_No unreleased changes._

---

## [1.0.0] - 2026-06-23

### Added

- Weekly report for 2026-W25 initialized to maintain forward archive continuity during continued Phase 2 consolidation, recovery-floor durability monitoring, lower-back mechanical-resolution observation, and trait-level work-capacity monitoring.

- Appended sleep dataset entries for 2026-W24 (2026-06-15 through 2026-06-21):
  - direct crossover from source dataset
  - no inferred or reconstructed values included
  - schema consistency preserved against longitudinal sleep structure
  - canonical sleep dataset extended through 2026-06-21

- Release metadata locked for the initial DOI-bearing archival release:
  - `CODEMETA.json` version set to `1.0.0`
  - `CODEMETA.json` `dateModified` advanced to `2026-06-23`
  - `CITATION.cff` version set to `1.0.0`
  - `CITATION.cff` `date-released` set to `2026-06-23`

---

### Changed

- `reports/2026-W24.md` finalized to reflect:
  - completed post-travel reintegration window
  - preserved ambient B1 execution under restored home-environment conditions
  - stable Load Integration under ordinary-life workload exposure
  - continued upper-body integration stability
  - localized lower-back mechanical signaling contained without protocol retreat
  - preserved recovery floor despite repository, administrative, household, training, and localized mechanical variability
  - recovery-floor durability confirmation under normal-life workload conditions

- `reports/2026-W25.md` initialized to reflect:
  - active W25 observation window
  - continued Phase 2 consolidation posture
  - recovery-floor durability monitoring
  - lower-back mechanical-resolution observation
  - continued ambient execution observation
  - trait-level work-capacity monitoring under ordinary-life conditions

- `LATEST.md` executive system dashboard updated to reflect:
  - W24 closed observation window
  - W25 active observation window
  - W24 sleep observations appended through 2026-06-21
  - continued Phase 2 consolidation posture
  - recovery-floor durability and ordinary-life workload absorption following W24 closeout
  - lower-back mechanical-resolution monitoring entering W25

- `data/sleep_longitudinal_v1.csv` extended through 2026-06-21 to preserve weekly continuity across the W24 observation window.

- `CODEMETA.json` updated:
  - `dateModified` advanced to `2026-06-23`
  - version advanced to `1.0.0`

- `CITATION.cff` updated:
  - version advanced to `1.0.0`
  - release date set to `2026-06-23`
  - DOI intentionally omitted pending Zenodo DOI issuance

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
