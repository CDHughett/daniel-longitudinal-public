# Private Source Provenance

## Purpose

This directory records provenance for private `Daniel_Dataset_v1.x` sources that support public curated rows without publishing the private workbooks themselves.

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

Primary manifest:

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

## Hash Boundary

A SHA-256 is registered only when the exact private source file was available as a retained file during the 2026-09-06 provenance pass.

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
