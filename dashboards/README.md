# Dashboards

This directory contains public summary views of selected metrics derived from the Daniel Longitudinal Study archive.

Dashboards are **derived artifacts**, not primary evidence.

All dashboard summaries must be traceable to underlying artifacts stored in `/snapshots` and interpreted through structured documents in `/reports`.

---

## Purpose

Dashboards exist to provide:

- high-level system visibility
- simplified metric summaries
- public interpretive surfaces

They are not intended to replace primary artifacts or structured reports.

---

## Data Hierarchy

The archive follows a strict evidence hierarchy:

1. **Snapshots** (`/snapshots`)
   - primary measurement artifacts
   - DEXA scans
   - BodPod outputs
   - biomarker captures
   - other date-bound evidence

2. **Reports** (`/reports`)
   - structured interpretation
   - weekly summaries
   - phase synthesis documents

3. **Dashboards** (`/dashboards`)
   - derived metric summaries
   - visualization surfaces
   - simplified public monitoring views

Dashboards summarize signals.  
They do not generate them.

---

## Design Constraints

Dashboards in this archive must:

- remain traceable to artifact sources
- avoid speculative interpretation
- preserve longitudinal continuity
- prioritize clarity over visual complexity

If a metric cannot be traced to artifact continuity, it should not appear here.

---

## Current Status

As of the current archive state, dashboard surfaces remain minimal.

The archive prioritizes **artifact continuity and structured reporting** before introducing derived visualization layers.

Future dashboards may include:

- recovery signal summaries
- training exposure aggregates
- phase progression indicators
- longitudinal trend surfaces

These will be introduced only when sufficient artifact continuity exists.

---

## Archive Principle

Artifacts first.  
Interpretation second.  
Visualization last.
