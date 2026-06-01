# EPOCH INDEX

A temporal index of snapshot epochs currently represented in the public archive.

This document tracks **artifact windows and archive position**.

It does **not** define phase logic, interpretive conclusions, or structural bias shifts.

For phase architecture, see [`PHASE_MAP.md`](./PHASE_MAP.md).  
For chronological artifact listing, see [`SNAPSHOT_LOG.md`](./SNAPSHOT_LOG.md).

---

## Purpose

This file exists to make the snapshot layer easier to navigate.

It provides:

- a clean temporal index of snapshot epochs
- a stable bridge between current system state and archived artifact windows
- a non-interpretive entry point into the snapshot layer

---

## Epoch Index

| Epoch | Folder | Anchor Record | Archive Role |
|-------|--------|---------------|--------------|
| 2025-05 | [`snapshots/2025-05/`](./snapshots/2025-05/) | [`2025-05 Epoch.md`](./snapshots/2025-05/2025-05%20Epoch.md) | early structured archive baseline |
| 2025-07 | [`snapshots/2025-07/`](./snapshots/2025-07/) | [`2025-07 Epoch.md`](./snapshots/2025-07/2025-07%20Epoch.md) | mid-Phase 1 artifact window |
| 2025-08 | [`snapshots/2025-08/`](./snapshots/2025-08/) | [`2025-08 Epoch.md`](./snapshots/2025-08/2025-08%20Epoch.md) | continued Phase 1 stabilization window |
| 2025-09 | [`snapshots/2025-09/`](./snapshots/2025-09/) | [`2025-09 Epoch.md`](./snapshots/2025-09/2025-09%20Epoch.md) | late Phase 1 progression window |
| 2025-10 | [`snapshots/2025-10/`](./snapshots/2025-10/) | [`2025-10 Epoch.md`](./snapshots/2025-10/2025-10%20Epoch.md) | pre-closeout consolidation window |
| 2025-11 | [`snapshots/2025-11/`](./snapshots/2025-11/) | [`2025-11 Epoch.md`](./snapshots/2025-11/2025-11%20Epoch.md) | Phase 1 completion baseline |
| 2026-02 | [`snapshots/2026-02/`](./snapshots/2026-02/) | [`2026-02 Epoch.md`](./snapshots/2026-02/2026-02%20Epoch.md) | Phase 2 early load-integration window |
| 2026-05 | [`snapshots/2026-05/`](./snapshots/2026-05/) | [`2026-05 Epoch.md`](./snapshots/2026-05/2026-05%20Epoch.md) | Phase 2 testing-window artifact capture |

---

## Structural Role

`EPOCH_INDEX.md` sits between the live system-state layer and the artifact record.

Recommended navigation flow:

LATEST.md  
→ EPOCH_INDEX.md  
→ SNAPSHOT_LOG.md  
→ specific epoch folders and anchor records

---

## Boundary

This file is an index layer only.

It does **not**:

- declare phases
- summarize reports
- interpret biological meaning
- replace the snapshot log

Interpretation remains subordinate to artifacts and belongs in [`reports/`](./reports/).

---

_Last reviewed during May 2026 snapshot completion._
