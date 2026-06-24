# Daniel Longitudinal Study — Index

This repository is a structured public archive of an ongoing longitudinal self-observation system focused on biological system behavior, performance capacity, recovery behavior, and protocol evolution under controlled constraints.

**This is not a coaching product.**  
**This is not a fitness journal.**  
**This is a governed, versioned archive.**

---

## Tier 1 — Start Here

These files are sufficient for initial understanding of the system:

- [README.md](README.md)
- [docs/START_HERE.md](docs/START_HERE.md)
- [LATEST.md](LATEST.md)
- [docs/OBSERVER_QUICKSTART.md](docs/OBSERVER_QUICKSTART.md)
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md)
- [docs/CONCEPTS.md](docs/CONCEPTS.md)

---

## Tier 2 — Observer + Reading Paths

These files define how first-time readers, skeptical observers, and technical reviewers should enter the archive:

- [docs/START_HERE.md](docs/START_HERE.md) — first 5 minutes
- [docs/OBSERVER_QUICKSTART.md](docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
- [docs/FOR_OBSERVERS.md](docs/FOR_OBSERVERS.md) — broader observer evaluation path
- [docs/NEWCOMER_PATH.md](docs/NEWCOMER_PATH.md) — first full reading pass
- [README.md](README.md) — repository overview
- [LATEST.md](LATEST.md) — current system state

---

## Tier 3 — Core System Understanding

These define how the system operates:

- [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [METHODOLOGY_AND_CONTROLS.md](METHODOLOGY_AND_CONTROLS.md)
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md)
- [MEASUREMENT_SOURCES.md](MEASUREMENT_SOURCES.md)

---

## Tier 4 — Reference and Extended Context

These provide additional structure, context, and supporting detail:

- [WHY_PUBLIC.md](WHY_PUBLIC.md)
- [STRUCTURAL_PRINCIPLES.md](STRUCTURAL_PRINCIPLES.md)
- [RISK_MANAGEMENT.md](RISK_MANAGEMENT.md)
- [PHASE_DECLARATION_CRITERIA.md](PHASE_DECLARATION_CRITERIA.md)
- [RECOVERY_MONITORING_FRAMEWORK.md](RECOVERY_MONITORING_FRAMEWORK.md)
- [STATE_TRANSITIONS.md](STATE_TRANSITIONS.md)
- [docs/WEEK_INDEXING.md](docs/WEEK_INDEXING.md) — explains internal reporting week labels and calendar-week offset

---

## System State + Temporal Structure

- [LATEST.md](LATEST.md) — current system state
- [PHASE_MAP.md](PHASE_MAP.md) — phase architecture and progression model
- [EPOCH_INDEX.md](EPOCH_INDEX.md) — temporal index of snapshot epochs
- [SNAPSHOT_LOG.md](SNAPSHOT_LOG.md) — chronological artifact record
- [VERSIONING.md](VERSIONING.md) — release and archive versioning rules

---

## Observer Evaluation Layer

- [docs/OBSERVER_QUICKSTART.md](docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
- [docs/FOR_OBSERVERS.md](docs/FOR_OBSERVERS.md) — broader skeptical or technical review path
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md) — public data scope and limitations
- [docs/CONCEPTS.md](docs/CONCEPTS.md) — recurring archive terminology
- [docs/audits](docs/audits) — repository audit records

---

## Measurement + Methodology

- [METHODOLOGY_AND_CONTROLS.md](METHODOLOGY_AND_CONTROLS.md)
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md)
- [MEASUREMENT_SOURCES.md](MEASUREMENT_SOURCES.md)
- [RECOVERY_MONITORING_FRAMEWORK.md](RECOVERY_MONITORING_FRAMEWORK.md)
- [methodology/prediction_evaluation.md](methodology/prediction_evaluation.md)
- [docs/methodology/UDI_framework_v1.md](docs/methodology/UDI_framework_v1.md)
- [CITATION.cff](CITATION.cff)

---

## Methodology Structure

Methodology is intentionally split across two layers:

- `/methodology/` → core observational rules, constraints, and evaluation boundaries
- `/docs/methodology/` → analytical overlays applied after artifact collection

This separation distinguishes:

- what governs the system
- what is used to interpret recorded outcomes

Extended methodology does not modify system behavior and remains subordinate to the core observational layer.

---

## Data + Evaluation Layer

- [/data](data) — structured longitudinal datasets
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md) — data scope and public inclusion boundaries
- [/data/model_error](data/model_error) — prediction vs. observed outcome review layer
- [data/model_error/WHAT_THIS_LAYER_IS.md](data/model_error/WHAT_THIS_LAYER_IS.md) — model-error layer context
- [data/model_error/model_error_gap_v1.csv](data/model_error/model_error_gap_v1.csv) — primary model-error tracking file

---

## Archive Structure

- [/snapshots](snapshots) — primary artifact archive and immutable evidence
- [/reports](reports) — active observation logs and retrospective interpretation
- [/experiments](experiments) — intervention-specific experiment files
- [/schemas](schemas) — naming rules and structure definitions
- [/methodology](methodology) — core methodological rules
- [/dashboards](dashboards) — derived metric summaries and non-primary views
- [/docs](docs) — governance, observer context, concepts, audits, and extended methodology

---

## Reading The Archive

Use:

- `/snapshots` for **primary evidence**
- `/reports` for **system behavior across time**
- `/data` for **structured longitudinal tracking**
- `/data/model_error` for **prediction versus observed outcome review**
- `/docs` for **governance, concepts, observer context, and audits**

Recommended first-contact flow:

```text
README.md
  ↓
docs/START_HERE.md
  ↓
LATEST.md
  ↓
docs/OBSERVER_QUICKSTART.md
  ↓
data/DATA_COVERAGE.md
  ↓
docs/FOR_OBSERVERS.md
```

Recommended temporal flow:

```text
LATEST.md
  ↓
EPOCH_INDEX.md
  ↓
SNAPSHOT_LOG.md
  ↓
/snapshots/YYYY-MM/
```

Recommended full reading flow:

```text
docs/START_HERE.md
  ↓
docs/NEWCOMER_PATH.md
  ↓
INDEX.md
```

Artifacts precede interpretation.

---

## Archive Standard

This public repository is organized to preserve:

- continuity
- traceability
- interpretive restraint
- longitudinal readability
- evidence-first evaluation
- separation between artifacts, reports, datasets, dashboards, prediction review, and governance

Where uncertainty exists, artifacts take precedence over narrative.

No claim extends beyond the recorded single-subject archive.
