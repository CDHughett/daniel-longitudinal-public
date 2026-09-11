# DQ-010 — August 2026 TruDiagnostic Source Reconciliation

**Status:** Confirmed source-role reconciliation  
**Recorded:** 2026-09-10  
**Affected biological sample:** August 2026 TruDiagnostic snapshot

---

## Purpose

This record preserves a source-metadata difference without altering the biological assay results.

The August TruDiagnostic provider reports and the contemporaneous repository collection record serve different evidentiary roles.

Public distribution of the provider PDFs is a separate privacy-governance question and does not determine the source role of the biological values.

---

## Canonical Collection Record

The governed contemporaneous repository record controls the actual testing event:

```text
Sample collection date: 2026-08-17
Sample collection time: 05:37 local
```

Preparation and test-day conditions are governed by the contemporaneous August collection records, including the registered collection plan and August Epoch execution log.

The repository record establishes the collection event before outcome interpretation and is the canonical source for:

- sample date
- sample time
- fasting duration
- morning intake
- recent training
- collection sequence
- other documented test-day preparation conditions

---

## Provider-Displayed Administrative Metadata

The August TruDiagnostic report headers display:

```text
Collected: 08/16/2026
Fasted: Unknown
```

These fields are preserved in the retained provider source reports as provider-displayed administrative metadata.

They are not used to overwrite the governed contemporaneous collection record.

The repository does not assert from this difference alone that the provider header is biologically invalid or that the assay output belongs to a different sample. The biological result set is preserved as reported.

---

## Source-Role Rule

For this August 2026 snapshot:

```text
TruDiagnostic provider reports
    -> assay outputs, provider labels, provider-displayed result metadata

Contemporaneous repository collection record
    -> canonical sample date/time and preparation/testing conditions
```

Accordingly:

- August molecular rows use `2026-08-17` as the canonical sample date.
- The provider-displayed `08/16/2026` header date does not shift structured molecular values to August 16.
- `Fasted: Unknown` in the provider report does not erase the contemporaneously documented fasting state.
- No biological measurement is corrected or altered by this reconciliation.
- Public retention of the raw provider PDFs is not required for this source-role assignment.

---

## Source Reports and Public-Artifact Boundary

The applicable provider source reports are:

- Advanced TruAge
- TruAge
- TruHealth

They were reviewed to support the August structured transcription and Model Error 043 adjudication.

Batch 5 privacy review subsequently identified an unnecessary administrative sample/specimen identifier in the raw provider-report headers. Under `methodology/anonymization.md`, the integration branch therefore removes the three raw public PDF copies and defers public molecular-PDF inclusion until privacy-compliant sanitized derivatives are adopted.

The current public August checksum manifest consequently covers the retained physical source artifacts only.

This privacy action does not modify the structured molecular values or the source-role reconciliation above.

Historical Git-object exposure from earlier public commits is treated separately in:

[`../../docs/audits/2026-09-10-august-snapshot-integration-audit.md`](../../docs/audits/2026-09-10-august-snapshot-integration-audit.md)

---

## Downstream Use

This reconciliation governs downstream structured ingestion and interpretation of the August TruDiagnostic result set.

It does not:

- change the preregistered Model Error 043 thresholds
- change the May 2026 comparison baseline
- change DEXA, VO2, or Bod Pod collection records
- establish a causal explanation for any favorable or unfavorable molecular result
- authorize retrospective rewriting of historical reports
- establish that public-artifact privacy remediation is complete

The distinction is a provenance rule, not a biological interpretation.
