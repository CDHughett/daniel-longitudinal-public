# DQ-010 — August 2026 TruDiagnostic Source Reconciliation

**Status:** Confirmed source-role reconciliation  
**Recorded:** 2026-09-10  
**Affected biological sample:** August 2026 TruDiagnostic snapshot

---

## Purpose

This record preserves a source-metadata difference without altering the biological assay results.

The August TruDiagnostic provider reports and the contemporaneous repository collection record serve different evidentiary roles.

The public repository copies of the three August TruDiagnostic reports are sanitized derivatives of verified provider-source reports. That public-artifact status is separate from the source-role reconciliation documented here.

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

These fields are preserved as provider-displayed administrative metadata in the public sanitized derivatives.

They are not used to overwrite the governed contemporaneous collection record.

The repository does not assert from this difference alone that the provider header is biologically invalid or that the assay output belongs to a different sample. The biological result set is preserved exactly as reported.

---

## Source-Role Rule

For this August 2026 snapshot:

```text
Verified TruDiagnostic provider-source reports
    -> assay outputs, provider labels, provider-displayed result metadata

Public sanitized derivatives
    -> externally inspectable public representations of those result reports

Contemporaneous repository collection record
    -> canonical sample date/time and preparation/testing conditions
```

Accordingly:

- August molecular rows use `2026-08-17` as the canonical sample date.
- The provider-displayed `08/16/2026` header date does not shift structured molecular values to August 16.
- `Fasted: Unknown` in the provider report does not erase the contemporaneously documented fasting state.
- The public sanitized derivatives preserve the biological result content used by the archive while excluding administrative identifying content not required for interpretation.
- No biological measurement is corrected or altered by this reconciliation or by the public-artifact sanitization status.

---

## Public Source Artifacts

The applicable public sanitized derivatives are:

- `snapshots/2026-08/2026-08-advanced-truage.pdf`
- `snapshots/2026-08/2026-08-truage.pdf`
- `snapshots/2026-08/2026-08-truhealth.pdf`

Their SHA-256 values are registered in:

- `snapshots/2026-08/checksums.txt`

Those hashes identify the public derivative copies and do not assert byte identity with the private provider-source reports.

---

## Downstream Use

This reconciliation governs downstream structured ingestion and interpretation of the August TruDiagnostic result set.

It does not:

- change the preregistered Model Error 043 thresholds
- change the May 2026 comparison baseline
- alter the biological assay outputs
- change DEXA, VO2, or Bod Pod collection records
- establish a causal explanation for any favorable or unfavorable molecular result
- authorize retrospective rewriting of historical reports

The distinction is a provenance rule, not a biological interpretation.
