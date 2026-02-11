# Versioning Protocol

This repository follows structured version control to maintain archival integrity.

The Daniel Longitudinal Study is treated as a living system, not a static log.

All changes are intentional, time-stamped, and minimally interpreted.

---

## File Categories

### Snapshots
Raw or minimally processed captures tied to a specific date.
Examples:
- DEXA scans
- Bod Pod readings
- Biomarker panels
- HRV summaries

Snapshots are immutable once committed.

---

### Reports
Structured interpretations of one or more snapshots.
Reports may evolve as additional data provides context.

Reports are versioned when materially updated.

---

### Experiments
Defined interventions with:
- Hypothesis
- Protocol
- Duration
- Outcome metrics

Experiments are logged at initiation and conclusion.

---

## Version Increments

### Patch (vX.X.1)
Minor clarifications or formatting updates.
No change to data or interpretation.

### Minor (vX.1.X)
Addition of new snapshot or experiment.
No structural change to system architecture.

### Major (v1.X.X → v2.0.0)
Structural changes to:
- Repository architecture
- Measurement definitions
- Core methodology
- Data schema

Major versions reflect system evolution.

---

## Update Cadence

Snapshots:
- Occur upon confirmed capture.

Reports:
- Updated after confirmed interpretation.

LATEST.md:
- Updated weekly or upon material change.

CHANGELOG.md:
- Updated with every material commit.

---

## Integrity Constraints

- No retroactive data manipulation.
- No dehydration or artificial peak manipulation prior to capture.
- No theatrical optimization for presentation.
- All values recorded under normal operating conditions.

This repository is archival, not performative.
