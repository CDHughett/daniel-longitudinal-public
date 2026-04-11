# Verification Guide

This repository is designed for external verification of all primary snapshot artifacts.

## Artifact Verification (SHA-256)

All binary artifacts (PDFs, images) are accompanied by SHA-256 checksums.

### Windows (Command Prompt)

Run:
certutil -hashfile snapshots\YYYY-MM\filename.pdf SHA256

Then compare the output to:
snapshots/YYYY-MM/checksums.txt

---

### macOS / Linux

Run:
shasum -a 256 snapshots/YYYY-MM/filename.pdf

---

## Verification Scope

- Checksums validate file integrity (no corruption or modification)
- Files are stored as primary source artifacts (not derived exports)
- Git LFS is not used for PDF artifacts

---

## Notes

- All verification is file-level and reproducible across environments
- Snapshot directories are organized by time (YYYY-MM)
- Each snapshot is self-contained and independently verifiable
