# Audits

## Purpose

This directory contains select audit records documenting moments where the archive was evaluated under real conditions.

These are not routine logs.

They exist to capture:
- continuity after disruption  
- identification or correction of structural issues  
- validation of dataset integrity  
- confirmation of system behavior under imperfect conditions  

Each file represents a meaningful integrity checkpoint, not a scheduled event.

---

## Inclusion Criteria

An audit file is created only when at least one of the following conditions is met:

- An audit cycle was missed, delayed, or disrupted  
- A structural or data-layer issue was identified or corrected  
- A credibility-relevant layer was evaluated or modified  
  (e.g., model error dataset, longitudinal data, verification systems)  
- A record is needed to demonstrate continuity under non-ideal conditions  

---

## Exclusion Criteria

Audit files are not created for:

- routine weekly checks with no findings  
- normal operation under stable conditions  
- minor edits or non-critical adjustments  

Absence of an audit file does not indicate absence of review.

---

## Structure

All files follow a simple naming convention:

YYYY-MM-DD-saturday-audit.md

Only Saturday (deep audit) records are expected to appear here, and only when inclusion criteria are met.

No subdirectories are used.

---

## Interpretation

This directory should be read as a set of high-signal integrity events, not a complete log of all maintenance activity.

Each audit reflects a point where the system was tested, evaluated, or corrected—and held.

---

## Relationship to Other Layers

- `/reports/` → interpretive summaries of system behavior  
- `/snapshots/` → primary artifact storage and evidence  
- `/data/` → raw and structured datasets  
- `/docs/audits/` → selective integrity confirmations across those layers  

---

## Philosophy

The archive does not rely on frequency of logging for credibility.

It relies on:
- consistency of structure  
- stability of inputs  
- and selective, verifiable documentation when it matters  

Audits are recorded when they add signal.

Not when they satisfy routine.
