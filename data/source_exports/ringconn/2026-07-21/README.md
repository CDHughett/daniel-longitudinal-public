# RingConn Source Export — 2026-07-21

## Status

Direct-device source export.

Preserved as a source-data artifact.

---

## Export Event

- Export provider: RingConn
- Primary wearable: RingConn Gen 2
- Export acquisition date: 2026-07-21
- Archive directory: `data/source_exports/ringconn/2026-07-21/`
- Acquisition type: direct user-account export
- Transformation state: unmodified source files

The export was downloaded directly from the RingConn ecosystem and entered into the archive as a source-data package.

The directory date identifies the export-acquisition event. It does not imply that every file begins or ends on that date.

Actual temporal coverage is determined by the rows present in each source file.

---

## Included Files

The source package contains:

- `ringconn-sleep-export.csv`
- `ringconn-activity-export.csv`
- `ringconn-vital-signs-export.csv`
- `checksums.txt`

Each CSV represents a separate vendor-defined export domain.

---

## Preservation Rules

The three CSV files are preserved byte-for-byte as downloaded.

They must not be modified through:

- manual correction
- column renaming
- row sorting
- date normalization
- unit conversion
- missing-value replacement
- encoding conversion
- spreadsheet resaving
- schema reduction
- derived-field insertion

Any normalized, corrected, filtered, or derived dataset must be created separately and must preserve a traceable relationship to these source files.

The source exports remain authoritative for what the RingConn export system provided at the time of acquisition.

---

## Source Versus Canonical Data

These files are source artifacts.

They do not automatically replace or extend existing canonical datasets such as:

- `data/sleep_longitudinal_v1.csv`
- `data/biomarker_snapshot.csv`
- future activity or vital-sign longitudinal trackers

Canonical datasets may contain:

- manually transcribed observations
- archive-defined field names
- confidence annotations
- source-reconciliation notes
- governed corrections
- fields not present in the direct export

Source-export ingestion and canonical-dataset integration are therefore separate operations.

Historical values should enter a canonical tracker only after:

1. the source schema is documented
2. field meanings and units are confirmed
3. date and timestamp behavior is evaluated
4. duplicate and missing-date behavior is assessed
5. source-to-canonical mappings are defined
6. discrepancies with existing records are documented
7. transformation rules are made reproducible

No canonical dataset should be silently overwritten from these exports.

---

## Coverage Boundary

The files are described as an annual export package because they were requested as the available longitudinal RingConn history.

However:

- coverage may differ among the three files
- the first and last represented dates may differ
- some dates may be absent
- some fields may be unavailable for part of the represented period
- device or software behavior may have changed during the interval
- export coverage must be determined from file contents rather than assumed from the request label

No missing date or value should be reconstructed at the source-artifact layer.

---

## Timestamp and Timezone Boundary

Vendor timestamps are preserved exactly as exported.

Unless explicitly documented by RingConn metadata, this archive does not assume that a timestamp represents:

- UTC
- local civil time
- sleep-session start date
- wake date
- device-sync time
- server-processing time

Timezone, daylight-saving, and date-assignment behavior must be evaluated before timestamped source fields are transformed into canonical daily records.

---

## Missingness

Blank fields, absent rows, and vendor-defined missing values are preserved without reinterpretation.

At the source layer:

- blank does not automatically mean zero
- absent does not automatically mean not measured
- missing dates are not inserted
- duplicated rows are not silently removed
- conflicting values are not silently reconciled

Any later treatment of missingness belongs in documented transformation methodology.

---

## Quality and Comparability

Direct export improves provenance but does not establish perfect measurement validity.

Potential limitations include:

- wearable algorithm changes
- firmware or application updates
- incomplete device wear
- synchronization gaps
- vendor-defined aggregation
- undocumented field semantics
- device-specific HRV calculation
- sleep-stage estimation uncertainty
- timestamp and timezone ambiguity

Cross-platform comparisons remain inappropriate unless explicitly governed.

---

## Privacy Review

Before public inclusion, the source files must be reviewed for non-public administrative identifiers, including:

- email addresses
- account identifiers
- device serial numbers
- phone numbers
- precise location fields
- access tokens
- hidden export metadata
- other identifiers not required for longitudinal analysis

Health and wearable observations may be intentionally public within the study.

Administrative identifiers are not presumed public merely because they appear in a direct export.

---

## Integrity Verification

SHA-256 hashes for the source files are recorded in:

[`checksums.txt`](./checksums.txt)

A checksum change indicates that the archived bytes differ from the originally registered source artifact.

Any intentional replacement requires:

- documented reason
- new checksum
- traceable commit
- changelog entry when materially relevant

---

## Interpretation Boundary

These files record vendor-exported observations.

They do not independently establish:

- biological causality
- clinical significance
- phase status
- protocol effectiveness
- prediction outcome
- population-level validity

Interpretation remains governed by:

- [`../../../../GOVERNANCE.md`](../../../../GOVERNANCE.md)
- [`../../../../METHODOLOGY_AND_CONTROLS.md`](../../../../METHODOLOGY_AND_CONTROLS.md)
- [`../../../DATA_QUALITY_NOTES.md`](../../../DATA_QUALITY_NOTES.md)
- [`../../../../methodology/data-collection.md`](../../../../methodology/data-collection.md)

---

## Archive Role

This directory preserves the direct-source layer beneath future structured integration.

The intended sequence is:

```text
Direct RingConn Export
        ↓
Source-Export Integrity and Privacy Review
        ↓
Schema and Coverage Assessment
        ↓
Documented Source-to-Canonical Mapping
        ↓
Derived Longitudinal Dataset
        ↓
Retrospective Reporting and Analysis
```

Source artifacts precede transformation.

Transformation precedes interpretation.
