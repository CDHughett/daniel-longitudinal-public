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

- Added 2026-07-11 Saturday audit:
  - documents full-spectrum review of repository structure, links, datasets, checksums, reporting continuity, model-error continuity, protocol state, methodology, metadata, and August release readiness
  - confirms mechanical integrity across Markdown links, CSV parsing, snapshot checksums, weekly reports, and model-error records
  - identifies targeted semantic data-quality questions in the longitudinal sleep dataset
  - identifies stale protocol and experiment-status wording requiring correction
  - defines a proportionate cleanup sequence while protecting historical evidence and open prediction records
  - preserves records 041–044 unchanged and open
  - distinguishes immediate remediation from deferred architecture work

- Added `methodology/open_prediction_evaluation_plan_041_044.md`:
  - defines prospective evaluation rules for open model-error records 041–044
  - establishes common August snapshot boundaries and evidence hierarchy
  - defines recovery-capacity evaluation rules for record 041
  - defines repeated-evidence thresholds for ambient-execution record 042
  - establishes pre-outcome biological-anchor and magnitude rules for record 043
  - defines protocol-governance criteria for record 044
  - preserves all original model-error prediction fields unchanged
  - prevents outcome-driven reinterpretation after August results are known

- Added `data/DATA_QUALITY_NOTES.md`:
  - documents the unresolved 2026-05-18 through 2026-05-31 sleep-field duplication question
  - documents sleep-stage total discrepancies for 2026-03-31 and 2026-04-02
  - defines source-reconciliation requirements
  - prohibits inferred correction of unresolved source values
  - preserves the canonical sleep dataset unchanged pending source verification
  - establishes status labels and a traceable correction procedure for future data-quality findings

- Added weekly report closeout for `reports/2026-W26.md`:
  - documents continued Phase 2 consolidation under less controlled travel / holiday conditions
  - records preserved B1 execution during the available home / pre-travel portion of the week
  - records preserved Load Integration during the available home / pre-travel portion of the week
  - documents formal training pause during travel as valid environmental constraint rather than behavioral failure
  - records recovery-floor preservation despite travel disruption, scale-access loss, transient fluid retention, and repository cadence delay
  - documents conservative interpretation of bodyweight increase under travel, sodium, hydration timing, GI timing, scale loss, and edema context
  - preserves interpretation that W26 represented stable system coherence under non-ideal conditions rather than performance expansion

- Added weekly report initialization for `reports/2026-W27.md`:
  - carries forward continued Phase 2 consolidation
  - initializes post-travel return-to-standard monitoring
  - preserves ambient B1 and Load Integration monitoring
  - continues recovery-floor durability observation
  - continues trait-level work-capacity monitoring
  - adds post-travel fluid / bodyweight normalization as an observation layer
  - maintains no-compensation posture following travel constraint
  - continues July–August model-error observation without premature closure pressure

- Appended sleep dataset entries for 2026-W26 (`2026-06-29` through `2026-07-05`) to `data/sleep_longitudinal_v1.csv`:
  - direct crossover from the current source dataset
  - no inferred or reconstructed values included
  - schema consistency preserved against longitudinal sleep structure
  - canonical sleep dataset extended through `2026-07-05`

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

- Added minimal `.gitignore`:
  - prevents accidental commits of operating system files, editor settings, Python cache files, Jupyter checkpoints, virtual environments, and log files
  - preserves all repository datasets, documentation, reports, and research artifacts
  - completes standard repository hygiene without changing archive content or methodology

- Added 2026-07-02 delayed Wednesday audit:
  - documents delayed Wednesday repository integrity review
  - records passing checks for structure, Markdown links, CSV parsing, sleep continuity, snapshot checksum verification, model-error continuity, DOI / citation metadata, current-state alignment, and `.gitignore` archive safety
  - confirms repository remains healthy after minimal `.gitignore` addition
  - preserves normal stewardship cadence following a missed Wednesday audit

- Added 2026-07-08 Wednesday audit:
  - documents repository-wide audit following late W26 weekly closeout
  - records passing checks for repository structure, W26 closeout integrity, W27 initialization, Markdown links, CSV parsing, sleep continuity, snapshot checksum verification, weekly report continuity, model-error continuity, DOI / citation metadata, current-state alignment, changelog alignment, observer navigation, and governance posture
  - confirms repository is aligned to `2026-W26` closed and `2026-W27` active
  - confirms canonical sleep dataset continuity through `2026-07-05`
  - confirms no corrective action is required before continued normal W27 operation

### Changed

- Updated `reports/2026-W27.md`:
  - clarified that weekly biological interpretation remains retrospective
  - confined forward predictions to the formally registered model-error layer
  - replaced the blanket prohibition on forward claims with a prohibition on unregistered forward claims
  - added the 2026-07-11 pull-up observation as candidate evidence relevant to record 042
  - records preserved execution during verbal instruction, divided attention, positional pauses, and social / environmental load
  - explicitly states that the observation is insufficient to modify, pass, fail, or close record 042
  - preserves record 042 unchanged and open pending repeated spontaneous evidence

- Updated `experiments/EXP-001-autophagy-endurance.md`:
  - corrected the active observation window from `January 2026 – present` to January 2026 through April 16, 2026
  - clarified that the experiment is paused and not an active explanatory variable
  - distinguished the broader biomarker snapshot from isolated intervention effects
  - clarified that reactivation is optional and not currently scheduled
  - added requirements for any future comparable reactivation cycle

- Updated `protocols/hybrid-expansion-phase-v2.md`:
  - marked the protocol as historical, superseded, and not active
  - preserved the original 12-week design for provenance
  - separated historical prescriptions from current Phase 2 Load Integration governance
  - clarified that historical calorie, training, step, sauna, and autophagy targets should not explain current outcomes without documented exposure
  - clarified that any future expansion phase would require a new prospective protocol document

- Updated `README.md`:
  - replaced the inaccurate `No forward claims` statement
  - clarified that biological interpretation remains retrospective and artifact-bound
  - documented the governed role of explicitly registered forward predictions
  - added direct navigation to the open-prediction evaluation plan and data-quality notes
  - expanded repository structure to include protocols, roadmap, and methodology layers
  - clarified prediction governance, phase boundaries, public scope, and non-prescriptive posture
  - aligned archive language with defined protocol constraints and incomplete environmental control

- Updated `DATASET_OVERVIEW.md`:
  - replaced the claim of tightly constrained environmental variables
  - describes defined protocol constraints under incomplete real-world environmental control
  - expanded the archive model to include structured data and the model-error layer
  - added evidence hierarchy, environmental context, limitations, and correction-aware data-integrity language
  - clarified that provider-generated reports may be primary archive evidence without constituting raw instrument data
  - distinguished source artifacts, structured datasets, reports, predictions, and milestone context

- Expanded `methodology/data-collection.md`:
  - replaced the intentionally minimal placeholder with an active collection methodology
  - defines primary artifacts, direct exports, manual transcription, contemporaneous notes, and retrospective interpretation
  - establishes source hierarchy, temporal handling, units, field definitions, and missingness rules
  - defines manual-entry, screenshot, device-version, derived-value, and inferred-value procedures
  - defines semantic data-quality review and source-backed correction procedures
  - separates collection statements from interpretation
  - defines how candidate model-error evidence enters through the normal collection layer
  - establishes provenance expectations and requirements for future structured exports

- Updated `LATEST.md` executive system dashboard to reflect:
  - `2026-W26` closed observation window
  - `2026-W27` active observation window
  - W26 sleep observations appended through `2026-07-05`
  - continued Phase 2 consolidation posture
  - recovery-floor durability under travel disruption and reduced environmental control
  - post-travel return-to-standard execution monitoring
  - conservative post-travel bodyweight / fluid normalization monitoring
  - repository cadence restoration after travel and limited internet access
  - ongoing open model-error records 041–044 for the July–August / August 2026 observation window

- Updated current archive posture language from W26 active observation to W27 active observation:
  - replaced holiday / schedule variability observation as the primary current emphasis with post-travel return-to-standard monitoring
  - added bodyweight / fluid normalization monitoring after transient W26 edema and travel-related variability
  - preserved recovery-floor durability as the primary reference condition
  - maintained no forward performance claims, compensation pressure, or protocol escalation language

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
