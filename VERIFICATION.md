# Verification Guide

This repository is designed for external verification of primary snapshot artifacts.

Verification and temporal anchoring are related, but they are not the same layer.

- **verification** confirms artifact integrity
- **temporal anchoring** explains where a snapshot belongs in time and archive structure

---

## Artifact Verification (SHA-256)

Binary artifacts such as PDFs and images are accompanied by SHA-256 checksums.

### Windows (Command Prompt)

Run:

    certutil -hashfile snapshots\YYYY-MM\filename.pdf SHA256

Then compare the output to:

    snapshots/YYYY-MM/checksums.txt

### macOS / Linux

Run:

    shasum -a 256 snapshots/YYYY-MM/filename.pdf

Then compare the output to the corresponding `checksums.txt` file.

---

## Temporal Anchor Relationship

Many snapshot folders also include an epoch file such as:

    snapshots/YYYY-MM/YYYY-MM Epoch.md

That file serves as the temporal anchor record for the capture window.

It documents:

- when the snapshot belongs
- what operating conditions applied
- which artifacts belong to that window
- where interpretation belongs
- how the snapshot connects to the rest of the archive

Checksums verify the files.  
Epoch files contextualize the files.

These roles should remain separate.

---

## Verification Scope

- Checksums validate file integrity
- Files are preserved as primary source artifacts
- Snapshot folders are organized by time using `YYYY-MM`
- Epoch files provide capture-window context, not interpretation
- Reports and phase documents remain separate interpretive layers

---

## Notes

- All verification is file-level and reproducible across environments
- Snapshot directories are intended to be self-contained and independently verifiable
- Verification does not imply interpretation
- Interpretation belongs in reports, datasets, and other designated synthesis layers
