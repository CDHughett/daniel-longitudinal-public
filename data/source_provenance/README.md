# Source Provenance

## Purpose

This directory records provenance for source states that support public curated rows without requiring every underlying source to be published in its original form.

Its primary historical role is provenance for private `Daniel_Dataset_v1.x` workbooks. It may also contain narrow source-reconciliation records when two source states have different metadata roles that must remain explicit.

The public structured layer may therefore distinguish:

```text
public row locator
+
private source version
+
private file identity when available
```

from public distribution of the private source itself.

---

## Manifest

Primary private-source manifest:

[`daniel_dataset_private_manifest.csv`](./daniel_dataset_private_manifest.csv)

The manifest records:

- private source version
- source form
- represented date interval
- immutable private filename when an exact retained file was available
- file size
- SHA-256 when the exact retained private file was available for hashing
- hash-registration status
- public extraction targets
- provenance notes

---

## Provider-Source Reconciliation Records

Current reconciliation record:

[`2026-08-trudiagnostic-reconciliation.md`](./2026-08-trudiagnostic-reconciliation.md)

This record preserves the August 2026 distinction between:

- verified TruDiagnostic provider-source reports as the source for assay outputs and provider-displayed result metadata
- public sanitized derivatives as the externally inspectable repository copies of those reports
- the governed contemporaneous repository record as the canonical source for the sample collection date/time and preparation/testing conditions

The public August TruDiagnostic derivatives are checksum-registered under `snapshots/2026-08/`. Their public hashes identify the derivative copies rather than asserting byte identity with private provider originals.

A reconciliation record does not change the biological result or rewrite the governed collection event.

---

## Hash Boundary

A SHA-256 is registered only when the exact private source file is available as retained bytes at the time of registration. The initial historical pass occurred on 2026-09-06; the exact retained v1.29 workbook was registered during the 2026-09-07 weekly closeout.

No hash is reconstructed from:

- screenshots
- remembered filenames
- public extracted CSVs
- a later workbook version
- a workbook recreated from source rows

When the exact file was not available, the manifest records:

```text
hash_status = not_available_for_hash_registration
```

and leaves the digest blank.

This is deliberate missingness, not a failed checksum.

If the exact historical private file becomes available later, a hash may be added through a traceable manifest update without changing the public biological values.

---

## Relationship to `source_ref`

Public rows use a `source_ref` locator such as:

```text
private_workbook:Daniel_Dataset_v1.28:Daily Biomarkers:2026-08-30
```

Training rows use the same canonical locator family, for example:

```text
private_workbook:Daniel_Dataset_v1.28:Training Blocks:2026-08-30:LI
```

Earlier compact `wb:v...` / `pdf:v...` aliases remain in Git history but were standardized out of the live v1 training dataset on 2026-09-07.

These values locate the source version/tab/date.

They are not file hashes.

The manifest provides file-level identity when available.

See:

[`../../schemas/machine-readable-layer-v1.md`](../../schemas/machine-readable-layer-v1.md)

---

## Extraction Relationship

The private sources may contribute rows to:

- `data/daily_biomarkers_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`

Not every private source version necessarily contributes an event row.

`context_events_v1.csv` contains only context that meets the event-classification boundary.

The public files are curated extracts, not byte-identical transformations of the private workbook.

Date-cell normalization is permitted when a retained workbook mixes Excel serial dates and day-of-month integer encodings. The public date index is normalized to the supported calendar date without altering the associated biological, sleep, or training value. This normalization is recorded in the manifest note for the affected source version.

---

## Privacy Boundary

Publishing a private-source hash does not publish the private file.

The manifest intentionally excludes:

- account identifiers
- private file URLs
- private storage locations
- hidden workbook content
- credentials
- personal administrative identifiers not required for provenance

A hash confirms identity only when the same private bytes are available for comparison.

It does not establish measurement validity or public reproducibility of fields sourced only from private material.
