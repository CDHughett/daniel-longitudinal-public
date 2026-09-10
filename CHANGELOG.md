# Changelog

All notable changes to the Daniel Longitudinal Study public archive are documented here.

Historical entries are preserved in:

[`docs/archive/CHANGELOG_ARCHIVE.md`](docs/archive/CHANGELOG_ARCHIVE.md)

Biological interpretation belongs in `/reports`. This file records repository, dataset, methodology, governance, privacy, validation, and archive-integrity changes.

---

## [Unreleased]

### Changed

#### September 10 August molecular snapshot integration and Model Error 043 closure

- Added the three August TruDiagnostic provider-result PDFs to `snapshots/2026-08/` and registered their SHA-256 digests in the existing August checksum manifest.
- Integrated source-backed August biological fields into `data/biomarker_snapshot.csv` and `data/epigenetic_longitudinal.csv` without modifying the provider reports.
- Added `data/source_provenance/2026-08-trudiagnostic-reconciliation.md` and DQ-010 to `data/DATA_QUALITY_NOTES.md` to preserve the source-role distinction between provider-displayed administrative metadata and the contemporaneous collection record.
- Preserved the contemporaneous repository record as canonical for the actual TruDiagnostic sample event: `2026-08-17` at `05:37 local`, including documented preparation conditions. Provider-displayed `Collected: 08/16/2026` and `Fasted: Unknown` remain preserved as administrative metadata and do not overwrite the canonical collection record.
- Closed Model Error 043 under the preregistered records 041–044 evaluation plan as `actual_value=overall_improvement_not_met`, `status=closed`, `error_direction=over`, while preserving the original prospective prediction narrative and `calibration_state=pre` registration provenance.
- Added `data/model_error/record_043_closure.md` with the criterion-by-criterion adjudication and preserved favorable as well as adverse evidence.
- Updated primary trajectory concordance to `2/4 = 0.50`; point/range UDI and state concordance remain unchanged.
- Transitioned `tools/validate_repository.py` from protecting record 043 as open/unscored to protecting its committed closed outcome and error direction.
- Propagated the completed August source-artifact and Model Error 043 state through `LATEST.md`, `README.md`, `INDEX.md`, `SNAPSHOT_LOG.md`, the August Epoch, `EPOCH_INDEX.md`, `docs/CONCEPTS.md`, the active Week 36 report, and the current reports directory guide.
- Consolidated `methodology/README.md` as a current-facing directory guide: removed duplicated historical/live-state prose, redirected volatile state to `LATEST.md` and `data/DATA_COVERAGE.md`, and left the actual preregistered methodology artifacts unchanged.
- Historical weekly reports and audits whose pending/open language was accurate at the time were not retrospectively rewritten.
- Pull-request validation passed after the final Batch 4 documentation state. The validated state retained the expected two governed canonical-sleep warnings and introduced no validation errors.
- No Phase 2D declaration, training-protocol change, release-version change, or DOI change was introduced.

Classification:

```text
Biological source-value alteration:
No

Structured source-backed snapshot integration:
Yes

Prediction outcome change:
Yes — post-outcome adjudication under preregistered rules; original prediction wording unchanged

Phase or protocol change:
No

Release or DOI change:
No

Documentation / provenance / validator propagation:
Yes
```

### Changed

#### September 7 post-rollover verification hardening

- Performed a live post-W35/W36 rollover semantic and verification audit.
- Confirmed the W35 public arithmetic and the synchronized daily, sleep, training, context-event, report, model-error, provenance, snapshot, and current-state layers.
- Removed stale duplicated live-state fields from `methodology/README.md` and redirected volatile weekly/coverage state to `LATEST.md` and `data/DATA_COVERAGE.md`.
- Clarified that the preserved records 041–044 preregistration artifact remains governing for open record 043 and provenance for the closed companion records.
- Hardened the core validator so exactly one weekly report must be active and the active report must be the latest report.
- Added current-state synchronization checks for `LATEST.md`, `README.md`, `INDEX.md`, and the canonical coverage summary in `data/DATA_COVERAGE.md`.
- Updated validation documentation to match the stronger checks.
- Updated CI to current SHA-pinned `actions/checkout` and `actions/setup-python` v7 releases and enabled manual validation dispatch.
- Added a selective post-rollover audit record under `docs/audits/`.

Classification:

```text
Biological-value change:
No

Canonical dataset-value change:
No

Prediction wording or outcome change:
No

Phase or protocol change:
No

Release or DOI change:
No

Documentation / validation / CI hardening:
Yes
```



### Changed

#### September 7 W35 closeout and W36 initialization

- Extended the public machine-readable layer through the completed `2026-W35` window using retained `Daniel_Dataset_v1.29` source material.
- Added 7 daily-biomarker rows and 7 canonical sleep rows through `2026-09-06`.
- Added 14 training-session rows through `2026-09-06`, preserving the unchanged 7 B1 + 7 Load Integration architecture.
- Added two selective context-event rows for 2026-09-02 automaticity deepening and 2026-09-03 yard-work exposure.
- Registered the exact retained `Daniel_Dataset_v1.29` workbook in the private-source manifest with file size and SHA-256 identity.
- Replaced the validator's fixed live total of 325 training rows with a protected-prefix rule: exactly 325 historical sessions remain required through `2026-08-30`, while later governed rows may append.
- Closed `reports/2026-W35.md` and opened lean active `reports/2026-W36.md` for `2026-09-07` through `2026-09-13`.
- Advanced `LATEST.md`, `README.md`, and `INDEX.md` to W36 / W35 state.
- Centralized volatile machine-readable row counts and endpoints in `data/DATA_COVERAGE.md`; current-facing orientation, glossary, schema, dictionary, and observer documents now link to that canonical coverage surface instead of repeating counts.
- Preserved continuous canonical CSVs rather than splitting them by week or month.
- Shortened `LATEST.md` back toward dashboard scope and kept detailed W35 interpretation in the weekly report.
- Archived August-31-and-earlier live-changelog detail into `docs/archive/CHANGELOG_ARCHIVE.md` to keep the root changelog operationally current.

Classification:

```text
Biological source-value reconstruction:
No

Canonical sleep extension:
Yes — source-backed append only

Training architecture change:
No

Prediction wording or outcome change:
No

Phase or protocol change:
No

Release or DOI change:
No

Repository/data maintenance:
Yes
```

### Changed

#### September 7 machine-readable hardening closeout

- Standardized all 325 live `data/training_blocks_v1.csv` `source_ref` values to the canonical `private_workbook:` / `private_pdf:` provenance grammar.
- The finalized migration changes provenance locators only; the 325-session set and all non-`source_ref` training field values are preserved.
- Updated `schemas/machine-readable-layer-v1.md`, `DATA_DICTIONARY.md`, `DATASET_OVERVIEW.md`, and `data/source_provenance/README.md` so current documentation no longer treats compact `wb:v...` / `pdf:v...` aliases as valid live-v1 values. Those aliases remain inspectable in Git history.
- Hardened `tools/validate_machine_readable.py` to require the protected 325-session v1 training set and canonical source-reference syntax in addition to its existing identifier, date, vocabulary, numeric, duration, event-interval, cross-file, and model-error-reference checks.
- Revised `VERIFICATION.md` to document three verification levels: artifact verification, core repository validation, and machine-readable semantic validation.
- Confirmed lightweight read-only CI is active through `.github/workflows/validate.yml` on pushes to `main` and pull requests.
- Recorded private `Daniel_Dataset` source-file hashes where exact immutable retained workbooks were available, while leaving unavailable historical hashes explicitly missing rather than reconstructing them.
- Added `docs/AI_ASSISTANCE.md` and preserved AI assistance as a maintenance/analysis aid rather than a source-evidence class.
- Added the future model-error schema design separating registration status from model-calibration scope while leaving current protected v1 records unchanged.
- Canonicalized the current UDI expansion as **Unobstructed Delta Index** on current-facing documentation surfaces.

Migration correction record:

- Commit `aa7297fa6c5dff5f8db528773978ee2bd46ef592` was a transient intermediate source-ref migration state that unintentionally contained 251 rather than 325 training rows.
- The existing validator correctly checked syntax and uniqueness but did not yet protect the expected session count, so that intermediate state passed CI.
- Commit `7dff020bb7763edde880346d05ef7c955368f281` restored the full 325-row training source before migration.
- Commit `5167b4afd743a7594f6cd3bebe490411d09db0a4` then canonicalized 325 source references across 325 rows and verified 325 unique session IDs before committing.
- Commit `5e6801d0c08f506d7fc49ad3852a960d1558dbf3` added the explicit 325-row validator guard and canonical-only source-reference requirement.
- GitHub Actions run `34069047100` on that hardened state completed successfully: core validator PASS with 0 errors, 2 governed sleep warnings, and 9 passes; machine-readable validator PASS with 0 errors and 0 warnings, reporting 203 daily rows, 325 training rows / 325 unique session IDs, and 42 context events.

Classification:

```text
Biological-value change:
No

Canonical sleep change:
No

Training non-provenance field change:
No

Prediction wording or outcome change:
No

Phase or protocol change:
No

Release or DOI change:
No

Provenance/schema/validation hardening:
Yes
```

### Added

#### September 6 machine-readable data-layer expansion

- Added three curated machine-readable datasets:
  - `data/daily_biomarkers_v1.csv`
  - `data/training_blocks_v1.csv`
  - `data/context_events_v1.csv`

- Initialized the new CSV layer from completed Daniel Dataset source files and retrospectively backfilled the available structured history through `Daniel_Dataset_v1.0`–`v1.28`.

- Preserved source provenance through per-row `source_ref` fields rather than copying source-workbook narrative wholesale.

- `data/daily_biomarkers_v1.csv` now contains:

  ```text
  Rows:
  203

  Coverage:
  2026-02-09 through 2026-08-30
  ```

- The daily-biomarker layer preserves machine-readable daily fields including:
  - morning bodyweight where available
  - daily HRV
  - resting heart rate
  - daily average heart rate where available
  - body temperature
  - selected mood / energy / GI / pain / sweating state fields where supported
  - bounded context tags
  - source provenance

- Erection-quality data is intentionally excluded from `data/daily_biomarkers_v1.csv`.

- Verbose free-text source fields are not copied wholesale into the public daily-biomarker layer, preventing excluded private fields from being reintroduced indirectly through narrative text.

- `data/training_blocks_v1.csv` now contains:

  ```text
  Session rows:
  325
  ```

- The training-block layer preserves actual historical training architecture rather than forcing earlier phases into the current B1 + Load Integration vocabulary.

- Historical block types therefore remain distinguishable where supported, including:
  - legacy firmware blocks
  - combined B1 + Load Integration blocks
  - B1 + ground-integration blocks
  - active-recovery blocks
  - later discrete B1 blocks
  - later discrete Load Integration blocks
  - structured recreational exposures where they were explicitly recorded

- True no-training days were not fabricated into training rows.

- `data/context_events_v1.csv` now contains:

  ```text
  Curated events:
  42
  ```

- Context-event inclusion is deliberately selective rather than exhaustive.

- Events are included when they materially alter or contextualize:
  - training availability or timing
  - testing conditions
  - travel
  - meaningful ordinary-life workload
  - equipment context
  - mechanical signals
  - environmental conditions
  - recovery state
  - other bounded events relevant to longitudinal interpretation

- Presence in `context_events_v1.csv` does not imply that an event was adverse or caused a biological outcome.

- The source Daniel Dataset files were not modified to support the new CSV layer.

- The three CSVs are downstream structured projections of the existing source record and do not create a new operator logging requirement.

- Missing or unsupported fields remain blank rather than being reconstructed from memory or neighboring observations.

- This machine-readable expansion does not:
  - change any biological source value
  - alter canonical sleep data
  - modify a model-error record
  - modify UDI or concordance values
  - change the B1 + Load Integration architecture
  - declare Phase 2D
  - activate Phase 3
  - create a new formal release

#### September 4 delayed Wednesday audit

- Added `docs/audits/2026-09-04-late-wednesday-audit.md`.

- The audit records the delayed Wednesday repository review scheduled for `2026-09-02` and actually performed on `2026-09-04`.

- No backdated September 2 audit was created.

- The audit reviewed:

  ```text
  Package:
  daniel-longitudinal-public-main (18).zip

  Size:
  40,135,759 bytes

  SHA-256:
  3de4a952aec36486f510b19b3202d1771b54dd665b9e64d317b09c16587e53cb
  ```

- The most recent prior audited Saturday reference remained:

  ```text
  Package:
  daniel-longitudinal-public-main (14).zip

  Size:
  40,138,259 bytes

  SHA-256:
  62935ddd3d663bfff8de3484973c15f52cfc0ddcd6322e91857ab516eba1475f
  ```

- The reviewed August 29-to-current change surface was:

  ```text
  Added:
  1

  Changed:
  7

  Removed:
  0
  ```

- The audit confirmed:
  - fresh-ZIP validator `PASS`
  - extracted-directory validator `PASS`
  - Python validator compilation `PASS`
  - 192 repository files
  - zero zero-byte files
  - zero exact duplicate hash groups
  - 134 Markdown files
  - 11 CSV files
  - 33 of 33 registered checksums passing
  - 203 continuous canonical sleep rows
  - canonical sleep coverage through `2026-08-30`
  - weekly-report continuity through active `2026-W35`
  - model-error continuity through record `046`
  - record `043` preserved open and unscored
  - record `046` preserved closed as `failed_autonomic_recompression`
  - records `041–046` preserving `calibration_state=pre`
  - preserved original prospective prediction narratives
  - 24 of 24 images readable
  - 7 of 7 PDFs readable
  - 115 readable PDF pages
  - zero encrypted PDFs
  - release metadata aligned
  - RingConn byte-preservation controls intact

- The audit independently rechecked Week 34 arithmetic and found no numerical correction required.

- The audit identified three narrow issues:

  ```text
  1.
  a post-window record_046 tag
  on the 2026-08-24 canonical sleep row

  2.
  testing-related causal language
  stronger than the archive's standing
  causal-attribution boundary

  3.
  the already-disclosed unresolved
  2026-08-17 morning-bodyweight
  source discrepancy
  ```

- Audit disposition:

  ```text
  PASS WITH NARROW SEMANTIC REMEDIATION REQUIRED
  AND ONE PRESERVED SOURCE DISCREPANCY
  ```

- The audit did not authorize:
  - biological-value reconstruction
  - Model Error 046 rescoring
  - Model Error 043 closure
  - prediction-threshold modification
  - scoring-window modification
  - protocol modification
  - Phase 2D declaration
  - Phase 3 activation
  - release-version modification
