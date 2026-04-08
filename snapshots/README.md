## Epoch / Context Files

Some snapshot windows include an accompanying `Epoch.md` file.

These files are **context-only capture notes**, not interpretive reports.

Their purpose is to document:

- what the capture window was
- what operating conditions were present
- what broad training context surrounded the measurement
- which primary artifacts belong to that window

`Epoch.md` files should **not** function as:

- phase declarations
- retrospective verdicts
- performance claims
- synthesis documents

Interpretation belongs in:

- `/reports/`
- phase documents
- methodology and synthesis layers
- longitudinal datasets where applicable

In practice:

- **snapshots** preserve evidence and capture-window context
- **reports** interpret what happened
- **phase documents** define retrospective meaning at the system level

---

## Checksum Standard

Where a snapshot folder contains binary or non-text artifacts
(e.g. `.jpg`, `.png`, `.pdf`), that folder should include a
`checksums.txt` file containing SHA256 hashes for verification.

Checksum files are used only for artifact integrity.

They do not replace:

- the underlying source artifact
- the epoch/context file
- the report layer
- the archive’s interpretive constraints

In practice:

- one `checksums.txt` per snapshot folder
- one SHA256 entry per binary artifact
- filenames recorded relative to that folder
- hashes regenerated only when a binary artifact is added or replaced

This preserves a lightweight verification layer without changing
the archive’s artifact-first posture.
