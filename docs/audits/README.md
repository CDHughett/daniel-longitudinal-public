# Audits

## Purpose

This directory contains select audit records documenting moments where the archive was evaluated under real conditions.

These are not routine logs.

They exist to capture:

- continuity after disruption
- identification or correction of structural issues
- dataset integrity review
- verification-layer review
- model-error or methodology-layer review
- confirmation that archive structure held under active operation

Each file represents a meaningful integrity checkpoint, not a scheduled diary entry.

---

## Inclusion Criteria

An audit file is created only when at least one of the following conditions is met:

- an audit cycle was missed, delayed, disrupted, or intentionally documented
- a structural or data-layer issue was identified or corrected
- a credibility-relevant layer was evaluated or modified  
  (for example: model error dataset, longitudinal data, verification systems, or methodology boundaries)
- a record is needed to demonstrate continuity under non-ideal conditions
- the audit itself materially improves external readability of the archive

---

## Exclusion Criteria

Audit files are not created for:

- routine checks with no meaningful findings
- normal operation under stable conditions
- minor edits or non-critical adjustments
- commentary that belongs in weekly reports

Absence of an audit file does not indicate absence of review.

---

## Structure

All files follow a simple naming convention:

YYYY-MM-DD-audit-type.md

Examples:

- `2026-05-02-saturday-audit.md`
- `2026-05-06-wednesday-audit.md`

Audit type should describe the role of the review, not create a mandatory schedule.

No subdirectories are used.

---

## Interpretation

This directory should be read as a set of high-signal integrity events, not a complete log of all maintenance activity.

Each audit reflects a point where the archive was tested, evaluated, corrected, or confirmed under real operating conditions.

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
- traceability of changes
- selective, verifiable documentation when it matters

Audits are recorded when they add signal.

Not when they satisfy routine.
