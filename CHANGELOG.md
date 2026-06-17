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

- Weekly report for 2026-W24 initialized to maintain forward archive continuity during post-travel reintegration observation, recovery-floor durability monitoring, and continued Phase 2 consolidation.

- Appended sleep dataset entries for 2026-W23 (2026-06-08 through 2026-06-14):
  - direct crossover from source dataset
  - no inferred or reconstructed values included
  - schema consistency preserved against longitudinal sleep structure
  - canonical sleep dataset extended through 2026-06-14

---

### Changed

- `reports/2026-W23.md` finalized to reflect:
  - completed travel variability exposure window
  - preserved ambient B1 execution
  - stable Load Integration under travel and environmental variability
  - successful recreational movement absorption
  - preserved recovery floor despite environmental sleep disruption and meaningful life stress exposure
  - recovery-floor portability confirmation under reduced environmental control

- `reports/2026-W24.md` initialized to reflect:
  - active W24 observation window
  - post-travel reintegration monitoring
  - recovery-floor durability observation
  - continued ambient execution observation
  - restored home-environment variability monitoring under Phase 2 consolidation conditions

- `LATEST.md` executive system dashboard updated to reflect:
  - W23 closed observation window
  - W24 active observation window
  - W23 sleep observations appended through 2026-06-14
  - continued Phase 2 consolidation posture
  - post-travel reintegration observation following W23 travel variability exposure

- `data/sleep_longitudinal_v1.csv` extended through 2026-06-14 to preserve weekly continuity across the W23 observation window.

- `CODEMETA.json` updated:
  - `dateModified` advanced to `2026-06-17`
  - version advanced to `1.0.0-rc2`

- Audit filename conventions normalized:
  - renamed `2026-06-13_saturday_audit.md`
  - aligned historical audit naming with repository standards

- `CHANGELOG.md` restructured:
  - migrated historical entries to `docs/archive/CHANGELOG_ARCHIVE.md`
  - reduced active changelog scope
  - improved repository legibility ahead of DOI release
