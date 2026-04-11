## Epoch / Context Files

Some snapshot windows include an accompanying `Epoch.md` file.

These files capture **context only**.  
They do not perform interpretation.

### Purpose

`Epoch.md` documents:

- the capture window  
- operating conditions at the time of measurement  
- surrounding training context  
- which artifacts belong to that window  

### Boundaries

`Epoch.md` files do **not** function as:

- phase declarations  
- retrospective verdicts  
- performance claims  
- synthesis or interpretation  

### Separation of roles

- **snapshots** → preserve evidence and capture-window context  
- **reports** → interpret what occurred  
- **phase documents** → define retrospective system-level meaning  

---

## Checksum Standard

Snapshot folders containing binary or non-text artifacts  
(e.g. `.jpg`, `.png`, `.pdf`) should include a `checksums.txt` file.

This file contains SHA256 hashes for artifact verification.

### Purpose

Checksums exist solely to verify **artifact integrity**.

They do not replace:

- the underlying source artifact  
- the `Epoch.md` context file  
- the report layer  
- the archive’s interpretive constraints  

### Structure

- one `checksums.txt` per snapshot folder  
- one SHA256 entry per binary artifact  
- filenames recorded relative to that folder  

### Maintenance

- hashes are generated when a binary artifact is added  
- hashes are updated only if that artifact changes  

This maintains a lightweight verification layer while preserving the archive’s artifact-first structure.
