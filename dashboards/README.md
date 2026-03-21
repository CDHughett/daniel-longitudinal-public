# Dashboards

This directory contains **derived visualization surfaces** built from the Daniel Longitudinal Study archive.

Dashboards are **not primary evidence**.  
They are interpretive summaries of underlying artifacts.

All dashboard outputs must be traceable to `/snapshots` and aligned with structured interpretation in `/reports`.

---

## Purpose

Dashboards provide:

- high-level system visibility  
- simplified views of longitudinal metrics  
- public-facing signal summaries  

They do not replace source data or formal analysis.

---

## Data Hierarchy

The archive operates under a strict evidence hierarchy:

1. **Snapshots** (`/snapshots`)  
   Primary artifacts: raw, date-bound measurements  
   (DEXA, BodPod, biomarkers, and other captured signals)

2. **Reports** (`/reports`)  
   Structured interpretation: weekly summaries, phase analysis, synthesis documents  

3. **Dashboards** (`/dashboards`)  
   Derived outputs: visual summaries and monitoring surfaces  

Dashboards summarize signals.  
They do not generate them.

---

## Design Constraints

All dashboards must:

- maintain traceability to source artifacts  
- avoid speculative or narrative-driven interpretation  
- preserve longitudinal continuity  
- prioritize clarity over visual complexity  

If a metric cannot be traced to artifact continuity, it does not belong here.

---

## Current Status

Dashboard development is intentionally minimal.

The archive prioritizes:

- artifact continuity  
- measurement integrity  
- structured reporting  

Visualization layers are introduced only after sufficient data stability exists.

---

## Forward Surfaces

As the archive matures, dashboards may include:

- recovery signal trends (HRV, sleep architecture)  
- training exposure aggregates  
- phase progression indicators  
- longitudinal system stability views  

All additions will follow the established hierarchy and traceability constraints.

---

## Archive Principle

Artifacts first.  
Interpretation second.  
Visualization last.
