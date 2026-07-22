# RingConn Source Export — 2026-07-21

## Status

Direct-device source-export package.

Preserved as byte-registered source evidence.

Privacy screened, checksum verified, and externally validated from a fresh GitHub ZIP.

No canonical integration or normalized wearable dataset is currently required.

---

## Export Event

- Export provider: RingConn
- Primary wearable: RingConn Gen 2
- Export acquisition date: 2026-07-21
- Repository ingestion date: 2026-07-22
- Archive directory: `data/source_exports/ringconn/2026-07-21/`
- Acquisition type: direct user-account export
- Transformation state: source CSV contents unmodified
- Integrity state: verified
- Canonical integration state: not performed
- Routine normalization state: deferred

The export was downloaded directly from the RingConn ecosystem and entered into the archive as a source-data package.

The directory date identifies the acquisition event.

It does not imply that:

- every file begins on that date
- every file ends on that date
- every represented date contains an observation
- all three files have identical coverage
- the provider values are unchanged from their original observation dates

Actual temporal coverage is determined from the rows preserved in each source file.

---

## Included Files

The acquisition package contains:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- `README.md`
- `checksums.txt`

Each CSV represents a separate provider-defined export domain.

---

## Public Filename Normalization

The original downloaded filenames contained an unnecessary personal naming string.

The public filenames were normalized to:

```text
ringconn-sleep-export.csv
ringconn-activity-export.csv
ringconn-vital-signs-export.csv
```

Filename normalization occurred at the filesystem level.

The CSV contents were not edited or resaved.

---

## Structural Inventory

| File | Data rows | Fields | Verified bytes |
|---|---:|---:|---:|
| `ringconn-sleep-export.csv` | 366 | 10 | 38,703 |
| `ringconn-activity-export.csv` | 360 | 3 | 8,171 |
| `ringconn-vital-signs-export.csv` | 360 | 10 | 16,059 |

Data-row counts exclude the header row.

The files have different row counts because they represent different provider domains and coverage behavior.

The difference must not be repaired by:

- adding rows
- deleting rows
- forward filling
- inserting zero values
- forcing equal date coverage

---

## Preservation Rules

The three source CSVs are preserved byte-for-byte as downloaded.

They must not be modified through:

- manual correction
- header or column renaming
- row sorting
- date normalization
- timestamp conversion
- unit conversion
- missing-value replacement
- line-ending conversion
- encoding conversion
- spreadsheet resaving
- schema reduction
- deduplication
- derived-field insertion
- provider-anomaly repair

The source exports remain authoritative for what the RingConn export system supplied at the acquisition event.

A source anomaly remains part of the preserved source record.

Any correction, filtering, aggregation, reconciliation, or analysis must occur separately.

---

## Git Byte-Preservation Control

Git text conversion is disabled for provider-source CSVs through the root repository rule:

[`../../../../.gitattributes`](../../../../.gitattributes)

Relevant rule:

```gitattributes
data/source_exports/**/*.csv -text
```

This prevents Git from converting source-export line endings during staging, checkout, or archive generation.

The control applies to current and future CSVs placed beneath:

```text
data/source_exports/
```

---

## Integrity Verification

SHA-256 hashes for the three source CSVs are recorded in:

[`checksums.txt`](./checksums.txt)

Verification confirmed that:

- all three archived CSVs match the original downloaded files byte-for-byte
- original CRLF line endings are retained
- file sizes match the original downloads
- all three SHA-256 values match the existing manifest
- the checksum manifest was not rewritten around converted files
- a fresh GitHub ZIP retained the same bytes
- all source-export checksum entries passed after external download

A checksum change indicates that the archived bytes differ from the registered acquisition artifact.

Any intentional replacement requires:

- documented reason
- new checksum
- traceable commit
- review of whether the acquisition event should remain separate
- changelog entry when materially relevant

The current acquisition package is considered mechanically preserved.

Mechanical integrity does not establish semantic validity for every provider field or row.

---

## Preliminary Privacy Review

Before public inclusion, the source files received a read-only privacy and structure scan.

The scan identified:

- no obvious administrative-identifier terms in the CSV headers
- no email-like values
- expected wearable-domain fields only
- no account, device-serial, phone, address, token, or precise-location field apparent in the headers

The scan did not print health-data rows.

This review reduces obvious public-distribution risk.

It does not establish:

- complete anonymity
- absence of every possible quasi-identifier
- clinical validity
- suitability for population release
- immunity from inference when combined with other public information

Health and wearable observations are intentionally public within the study.

Administrative identifiers are not presumed public merely because they occur in a provider export.

---

## Source Versus Curated Data

These files are provider-source artifacts.

They do not automatically replace, correct, or extend curated datasets such as:

- [`../../../sleep_longitudinal_v1.csv`](../../../sleep_longitudinal_v1.csv)
- [`../../../biomarker_snapshot.csv`](../../../biomarker_snapshot.csv)

The source exports and curated datasets serve different roles.

### Provider Source Exports

The source exports preserve:

- provider-defined field names
- provider-defined units
- provider-defined timestamps
- provider-defined date assignment
- provider-defined aggregation
- provider missingness
- provider row ordering
- original byte representation
- provider database state at export time

### Curated Datasets

Curated datasets may preserve:

- archive-defined field names
- contemporaneously transcribed observations
- governed observation dates
- subjective context
- confidence labels
- readiness values
- awakening counts
- dreams
- mental, GI, or pain state
- source-reconciliation notes
- traceable corrections
- fields not supplied by the export

Neither source state should silently overwrite the other.

---

## Canonical Sleep Boundary

The direct sleep export must not be appended directly to:

[`../../../sleep_longitudinal_v1.csv`](../../../sleep_longitudinal_v1.csv)

The curated sleep dataset is governed as a one-row-per-date observation layer.

The RingConn sleep export is session based and may contain:

- more than one episode associated with a date
- overnight sleep
- daytime sleep
- naps
- provider-detected secondary sessions
- timestamps with differing precision
- provider-specific date behavior
- rows without complete stage classification

Canonical sleep data remained unchanged during this source-export ingestion.

Narrow source-backed corrections may be made later through dedicated commits when:

- the applicable source session is identified
- field semantics match
- dates align
- provider-state limitations are considered
- dependent values are reviewed
- the correction is documented

A full historical import is not authorized by this package.

---

## Coverage Boundary

The files are described as an annual export package because they were requested as the available longitudinal RingConn history.

Coverage differs by domain.

### Sleep Export

The sleep export contains:

- 366 episode rows
- 358 unique provisional wake dates
- represented provisional wake-date range from 2025-07-21 through 2026-07-21
- eight dates containing more than one episode
- eight absent provisional wake dates
- no explicit UTC offsets
- no provider-supplied primary-sleep or nap classification

The file is session based.

Its row count is not equivalent to covered calendar days.

### Activity Export

The activity export contains:

- 360 daily rows
- 360 unique provider dates
- represented date range from 2025-07-21 through 2026-07-20
- no rows from 2026-01-04 through 2026-01-08
- no row for 2026-07-21

### Vital-Signs Export

The vital-signs export contains:

- 360 daily rows
- 360 unique provider dates
- represented date range from 2025-07-21 through 2026-07-20
- missing dates matching the activity export
- daily minimum, average, and maximum heart-rate fields
- daily minimum, average, and maximum SpO₂ fields
- daily minimum, average, and maximum HRV fields

Missing source rows remain missing.

An absent row does not establish:

- zero activity
- no sleep
- no device wear
- no measurement
- synchronization failure
- intentional non-use
- a biological event

---

## Timestamp and Timezone Boundary

Provider timestamps are preserved exactly as exported.

The sleep export does not supply explicit UTC offsets.

The represented interval includes travel.

The archive therefore does not assume that a timestamp represents:

- UTC
- America/New_York
- local civil time at the measurement location
- the date sleep began
- the date sleep ended
- the date displayed in the RingConn application
- device synchronization time
- provider processing time

Some source rows contain second-level timestamps.

Others contain minute-level timestamps.

Timestamp precision must not be increased through inference.

No timezone conversion or universal daily date assignment is currently applied.

---

## Multiple Sleep Episodes

More than one source sleep episode occurs for some provisional wake dates.

These rows are not presumed duplicates.

The source package does not:

- discard secondary episodes
- select the longest episode as canonical
- sum all episodes
- classify naps
- merge session stages
- force one row per day

A session-selection or aggregation rule may be created later only when a defined analysis requires it.

The source file remains unchanged regardless of analytical treatment.

---

## Missingness

Blank fields, absent rows, and provider-defined missing values remain preserved without reinterpretation.

At the source layer:

- blank does not automatically mean zero
- absent does not automatically mean not measured
- zero does not automatically mean a valid measured absence
- missing dates are not inserted
- multiple rows are not silently deduplicated
- conflicting values are not silently reconciled
- provider anomalies are not repaired in place

Missingness classification belongs to the specific reconciliation or analysis that requires it.

---

## Known Quality Boundaries

Direct export improves provenance but does not establish perfect measurement validity.

Potential limitations include:

- wearable algorithm changes
- firmware or application changes
- retrospective provider recalculation
- incomplete device wear
- synchronization gaps
- provider-defined aggregation
- undocumented field semantics
- device-specific HRV calculation
- sleep-stage estimation uncertainty
- timestamp and timezone ambiguity
- multiple sleep sessions
- missing dates
- application-versus-export differences
- a November 17 session with reported sleep duration but no classified stage minutes

Detailed restrictions are recorded in:

[`../../../DATA_QUALITY_NOTES.md`](../../../DATA_QUALITY_NOTES.md)

---

## Periodic Export Policy

Periodic direct exports are the current wearable-preservation model.

Future acquisitions should use separate acquisition-date directories:

```text
data/source_exports/ringconn/YYYY-MM-DD/
```

Each acquisition package should contain:

- original provider-export files
- acquisition README
- checksum manifest

A later export:

- does not overwrite this package
- may overlap the same historical dates
- remains a separate provider-state observation
- may contain later recalculated values
- does not automatically replace curated data
- does not require an immediate merged dataset

No mandatory export cadence is imposed.

Reasonable acquisition triggers include:

- a major biological snapshot cycle
- annual archive review
- a device or provider change
- a defined reconciliation need
- a publication requirement
- concern about future provider-data availability

---

## Normalization and Derived Data

No normalized RingConn dataset is currently active, required, or scheduled.

Previously considered files such as:

```text
data/wearable_sleep_sessions_v1.csv
data/wearable_activity_daily_v1.csv
data/wearable_vitals_daily_v1.csv
```

remain deferred.

A derived wearable layer may become justified when:

- repeated historical analysis requires merging multiple exports
- provider schemas change
- automated comparison becomes necessary
- publication requires stable archive-defined fields
- a model-error question requires broader historical evidence
- repeated manual reconciliation becomes burdensome

Any future derived layer must be:

- separate from the source package
- reproducible
- versioned
- source-row traceable
- explicit about date assignment
- explicit about timezone uncertainty
- explicit about multiple-session behavior
- explicit about missingness
- non-destructive to all acquisition packages

The absence of a normalized tracker is not currently a data-quality or coverage failure.

---

## Interpretation Boundary

These files record provider-exported observations.

They do not independently establish:

- biological causality
- clinical significance
- phase status
- protocol effectiveness
- prediction outcome
- population-level validity
- cross-device comparability
- field-level equivalence with curated metrics
- absence of provider error

Interpretation remains governed by:

- [`../../../../GOVERNANCE.md`](../../../../GOVERNANCE.md)
- [`../../../../METHODOLOGY_AND_CONTROLS.md`](../../../../METHODOLOGY_AND_CONTROLS.md)
- [`../../../DATA_QUALITY_NOTES.md`](../../../DATA_QUALITY_NOTES.md)
- [`../../../../methodology/data-collection.md`](../../../../methodology/data-collection.md)
- [`../../../../MEASUREMENT_SOURCES.md`](../../../../MEASUREMENT_SOURCES.md)
- [`../../../../DATA_DICTIONARY.md`](../../../../DATA_DICTIONARY.md)

---

## Archive Role

This directory preserves a direct provider-source acquisition event.

The current operating sequence is:

```text
Periodic Byte-Preserved RingConn Export
                  ↓
Privacy, Structure, and Integrity Review
                  ↓
Acquisition README and SHA-256 Registration
                  ↓
Targeted Reconciliation or Analysis When Needed
                  ↓
Optional Reproducible Derived Layer, If Justified
                  ↓
Retrospective Reporting or Model Evaluation
```

Source preservation does not require immediate transformation.

Transformation does not occur without a defined need.

Interpretation remains subordinate to preserved evidence.

---

## Version Note

This README was revised on 2026-07-22 after completion of the source-export ingestion and integrity review.

The revision:

- records completion of repository ingestion
- documents public filename normalization
- records exact row counts and verified byte sizes
- documents the `.gitattributes` byte-preservation control
- records successful SHA-256 verification
- records verification from a fresh GitHub ZIP
- documents the completed preliminary privacy scan
- establishes periodic acquisition packages as the current maintenance model
- defers normalized wearable trackers
- preserves provider timestamp, missingness, multiple-session, and source-state limitations
- confirms that no curated dataset was modified during ingestion
