# Daniel Longitudinal Study — Index

This repository is a structured public archive of an ongoing single-subject longitudinal observation system focused on:

- biological-system behavior
- performance capacity
- recovery behavior
- protocol continuity
- ordinary-life perturbations
- prediction calibration
- archive governance

Observation occurs under **defined protocol constraints and incomplete real-world environmental control**.

**This is not a coaching product.**  
**This is not a fitness journal.**  
**This is not a clinical trial.**  
**This is a governed, versioned longitudinal archive.**

---

## Archive Model

The repository separates:

```text
Source Artifacts
      ↓
Structured Data
      ↓
Contemporaneous Observations
      ↓
Retrospective Reports
      ↓
Phase and State Interpretation
      ↓
Registered Prediction Evaluation
      ↓
Model Correction
```

Each layer serves a different purpose.

Higher-level interpretation must remain traceable to the evidence beneath it.

---

## Tier 1 — Start Here

These files provide the minimum useful orientation:

- [README.md](README.md) — repository scope, posture, and first reading path
- [docs/START_HERE.md](docs/START_HERE.md) — first five minutes
- [LATEST.md](LATEST.md) — current executive system state
- [docs/OBSERVER_QUICKSTART.md](docs/OBSERVER_QUICKSTART.md) — compact technical inspection route
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md) — what is structured, narrative, partial, contextual, or absent
- [docs/CONCEPTS.md](docs/CONCEPTS.md) — recurring archive terminology

---

## Tier 2 — Observer and Reading Paths

These files define how first-time readers, skeptical observers, and technical reviewers should enter the archive:

- [docs/START_HERE.md](docs/START_HERE.md) — first-contact orientation
- [docs/OBSERVER_QUICKSTART.md](docs/OBSERVER_QUICKSTART.md) — compact inspection route
- [docs/FOR_OBSERVERS.md](docs/FOR_OBSERVERS.md) — broader observer-evaluation framework
- [docs/NEWCOMER_PATH.md](docs/NEWCOMER_PATH.md) — first extended reading pass
- [README.md](README.md) — repository overview
- [LATEST.md](LATEST.md) — current state
- [data/DATA_QUALITY_NOTES.md](data/DATA_QUALITY_NOTES.md) — known unresolved data-quality findings
- [VERIFICATION.md](VERIFICATION.md) — artifact and whole-repository verification procedures

---

## Tier 3 — Core System and Governance

These documents define how the archive operates and how claims are constrained:

- [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md) — system architecture and information flow
- [GOVERNANCE.md](GOVERNANCE.md) — correction, prediction, protocol, and phase rules
- [METHODOLOGY_AND_CONTROLS.md](METHODOLOGY_AND_CONTROLS.md) — study design, stabilized inputs, evidence handling, and limitations
- [ASSUMPTIONS_AND_BOUNDARIES.md](ASSUMPTIONS_AND_BOUNDARIES.md) — interpretive limits and falsifiability conditions
- [STRUCTURAL_PRINCIPLES.md](STRUCTURAL_PRINCIPLES.md) — archive organization and evidence-preservation principles
- [PHASE_DECLARATION_CRITERIA.md](PHASE_DECLARATION_CRITERIA.md) — requirements for retrospective phase declarations
- [RISK_MANAGEMENT.md](RISK_MANAGEMENT.md) — operational and interpretive risk controls
- [PHASE_MAP.md](PHASE_MAP.md) — canonical phase hierarchy and operating-substate boundaries
- [STATE_TRANSITIONS.md](STATE_TRANSITIONS.md) — governed record of structural state changes

---

## Tier 4 — Data, Sources, and Quality

These documents explain what is measured, how it enters the archive, and how quality issues are handled:

- [DATASET_OVERVIEW.md](DATASET_OVERVIEW.md) — evidence classes and dataset structure
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md) — field and terminology definitions
- [MEASUREMENT_SOURCES.md](MEASUREMENT_SOURCES.md) — devices, providers, source states, and capture conditions
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md) — coverage boundaries
- [data/DATA_QUALITY_NOTES.md](data/DATA_QUALITY_NOTES.md) — unresolved quality findings and correction restrictions
- [methodology/data-collection.md](methodology/data-collection.md) — source hierarchy, transcription, missingness, correction, and provenance
- [methodology/anonymization.md](methodology/anonymization.md) — public-artifact sanitization and distribution-remediation rules
- [RECOVERY_MONITORING_FRAMEWORK.md](RECOVERY_MONITORING_FRAMEWORK.md) — recovery-signal interpretation framework
- [CITATION.cff](CITATION.cff) — citation metadata

---

## Current State and Temporal Structure

- [LATEST.md](LATEST.md) — current executive state
- [reports/2026-W31.md](reports/2026-W31.md) — active weekly observation window
- [reports/2026-W30.md](reports/2026-W30.md) — most recent closed weekly report
- [PHASE_MAP.md](PHASE_MAP.md) — phase architecture
- [STATE_TRANSITIONS.md](STATE_TRANSITIONS.md) — recorded phase and state changes
- [EPOCH_INDEX.md](EPOCH_INDEX.md) — temporal index of major observation periods
- [SNAPSHOT_LOG.md](SNAPSHOT_LOG.md) — chronological artifact log
- [docs/WEEK_INDEXING.md](docs/WEEK_INDEXING.md) — internal reporting-week convention
- [VERSIONING.md](VERSIONING.md) — repository release and archive-version rules
- [CHANGELOG.md](CHANGELOG.md) — recent structural and methodology changes
- [docs/archive/CHANGELOG_ARCHIVE.md](docs/archive/CHANGELOG_ARCHIVE.md) — preserved historical changelog entries

### Current preregistered August governance

- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md) — scoring and admissible-evidence rules for records 041–044
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — August 17–18 collection conditions and outcome-access boundaries

These documents were committed before August outcome access.

They do not contain August results or declare a phase transition.

---

## Observer Evaluation Layer

- [docs/OBSERVER_QUICKSTART.md](docs/OBSERVER_QUICKSTART.md) — compact technical inspection
- [docs/FOR_OBSERVERS.md](docs/FOR_OBSERVERS.md) — broader skeptical or technical review
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md) — public data scope and limitations
- [data/DATA_QUALITY_NOTES.md](data/DATA_QUALITY_NOTES.md) — known quality constraints
- [docs/CONCEPTS.md](docs/CONCEPTS.md) — archive terminology
- [docs/audits](docs/audits) — repository audit records
- [VERIFICATION.md](VERIFICATION.md) — verification scope and limitations
- [tools/validate_repository.py](tools/validate_repository.py) — local read-only repository validator
- [GOVERNANCE.md](GOVERNANCE.md) — governing evidence and correction rules
- [ASSUMPTIONS_AND_BOUNDARIES.md](ASSUMPTIONS_AND_BOUNDARIES.md) — claim boundaries

A skeptical observer should distinguish:

- active collection from closed-window interpretation
- source artifacts from structured transcription
- direct measurements from derived values
- candidate evidence from resolved outcomes
- registered predictions from ordinary planning
- source-backed correction from unsupported rewriting
- mechanical validation from semantic review
- a preregistered collection plan from a result report

---

## Reports Layer

- [reports](reports) — active and closed weekly reports
- [reports/README.md](reports/README.md) — report modes, lifecycle, inclusion rules, and correction boundaries
- [reports/2026-W30.md](reports/2026-W30.md) — most recent closed weekly report
- [reports/2026-W31.md](reports/2026-W31.md) — current active weekly report

Reports may contain:

- contemporaneous collection during an active window
- retrospective weekly interpretation after closeout
- candidate evidence relevant to open model-error records
- structured summaries grounded in preserved evidence

Reports do not replace source artifacts or canonical structured datasets.

An active report does not determine its own final interpretation.

---

## Snapshots and Primary Artifacts

- [snapshots](snapshots) — primary biological, body-composition, performance, and source artifacts
- [SNAPSHOT_LOG.md](SNAPSHOT_LOG.md) — chronological snapshot index
- [snapshots/sleep_signal_core_v1.csv](snapshots/sleep_signal_core_v1.csv) — preserved compact sleep-signal artifact
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — preregistered plan for the next snapshot cycle

Snapshot review should consider:

- collection date
- provider or device
- preparation conditions
- source completeness
- checksum status
- comparability with prior artifacts
- direct versus derived status
- public-original versus sanitized-derivative status
- preregistered collection and evaluation boundaries

Checksum validity confirms file identity, not biological or clinical validity.

A collection plan governs capture conditions. It does not become outcome evidence.

---

## Structured and Source-Preserved Data Layer

- [data](data) — canonical, curated, model-error, and source-export data layers
- [data/sleep_longitudinal_v1.csv](data/sleep_longitudinal_v1.csv) — canonical sleep dataset
- [data/biomarker_snapshot.csv](data/biomarker_snapshot.csv) — integrated snapshot values
- [data/bloodwork_longitudinal.csv](data/bloodwork_longitudinal.csv) — longitudinal bloodwork structure
- [data/epigenetic_longitudinal.csv](data/epigenetic_longitudinal.csv) — longitudinal epigenetic structure
- [data/source_exports](data/source_exports) — immutable provider and device source-export packages
- [data/source_exports/ringconn/2026-07-21](data/source_exports/ringconn/2026-07-21) — byte-preserved RingConn acquisition package
- [data/DATA_COVERAGE.md](data/DATA_COVERAGE.md) — structured, narrative, and source-preserved coverage boundaries
- [data/DATA_QUALITY_NOTES.md](data/DATA_QUALITY_NOTES.md) — known semantic-quality issues

Structured data support:

- continuity checking
- longitudinal comparison
- derived calculations
- validation
- prediction evaluation

Source-preserved exports support:

- provenance
- integrity verification
- targeted reconciliation
- future reproducible analysis when justified

A structurally valid dataset may still contain semantic or source-verification issues.

A direct provider export does not automatically replace a curated dataset.

---

## Prediction and Model-Error Layer

- [data/model_error](data/model_error) — prediction and calibration records
- [data/model_error/WHAT_THIS_LAYER_IS.md](data/model_error/WHAT_THIS_LAYER_IS.md) — model-error purpose and boundaries
- [data/model_error/model_error_gap_v1.csv](data/model_error/model_error_gap_v1.csv) — primary model-error register
- [data/model_error/udi_by_type_tracker.csv](data/model_error/udi_by_type_tracker.csv) — UDI summary by eligible prediction type
- [data/model_error/calibration_events_log.md](data/model_error/calibration_events_log.md) — major calibration events
- [data/model_error/historical](data/model_error/historical) — reconstructed historical records
- [methodology/prediction_evaluation.md](methodology/prediction_evaluation.md) — general prediction-evaluation methodology
- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md) — registered evaluation plan for open records 041–044
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — preregistered collection plan relevant to record 043
- [docs/methodology/prediction_to_outcome_pipeline.md](docs/methodology/prediction_to_outcome_pipeline.md) — prediction-to-outcome workflow
- [docs/methodology/valid_prediction_criteria.md](docs/methodology/valid_prediction_criteria.md) — valid-prediction requirements
- [docs/methodology/UDI_framework_v1.md](docs/methodology/UDI_framework_v1.md) — UDI methodology

Registered predictions are permitted only within the governed model-error layer.

They must remain:

- time- or state-bounded
- preserved after registration
- evaluated after sufficient evidence exists
- open when evidence is insufficient
- retained when incorrect

A collection plan may protect a prediction from outcome-directed manipulation.

It does not modify the prediction itself.

---

## Methodology Structure

Methodology is split across two connected layers.

### `/methodology`

Core operating methodology and active preregistration artifacts:

- [methodology/README.md](methodology/README.md) — methodology directory guide
- [methodology/data-collection.md](methodology/data-collection.md) — source, transcription, missingness, and correction rules
- [methodology/anonymization.md](methodology/anonymization.md) — artifact sanitization and privacy-remediation rules
- [methodology/prediction_evaluation.md](methodology/prediction_evaluation.md) — general prediction-evaluation rules
- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md) — active evaluation plan
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — active snapshot collection plan

This layer governs:

- current collection
- source handling
- privacy handling
- correction
- prediction evaluation
- preregistered collection conditions
- outcome-access boundaries

### `/docs/methodology`

Extended analytical and conceptual overlays, including:

- prediction validity
- prediction-to-outcome workflow
- UDI
- subject baseline context
- later analytical frameworks

The distinction is not absolute, but it helps separate:

- rules governing current collection and evaluation
- supporting analytical documentation

Neither layer may override verified source evidence.

A retrospective document must not silently rewrite an earlier preregistered rule.

---

## Protocol Layer

- [protocols](protocols) — active, historical, and superseded protocol documents
- [protocols/hybrid-expansion-phase-v2.md](protocols/hybrid-expansion-phase-v2.md) — historical, superseded, and inactive protocol retained for provenance

A protocol file remaining in the repository does not prove that the protocol is currently active.

Each protocol should identify its status.

Current execution state should be confirmed through:

- [LATEST.md](LATEST.md)
- the active weekly report
- current governance documents

---

## Experiment Layer

- [experiments](experiments) — intervention-specific experiment records
- [experiments/EXP-001-autophagy-endurance.md](experiments/EXP-001-autophagy-endurance.md) — paused experiment with a documented active observation window

Experiment status may be:

- proposed
- active
- paused
- completed
- superseded

An inactive or paused experiment must not be used as a current explanatory variable without documented exposure.

---

## Schemas and Validation

- [schemas](schemas) — file and reporting structures
- [schemas/weekly-report-template.md](schemas/weekly-report-template.md) — weekly report template
- [VERIFICATION.md](VERIFICATION.md) — artifact and repository verification procedures
- [tools/validate_repository.py](tools/validate_repository.py) — local read-only validator
- [docs/audits](docs/audits) — completed integrity and governance audits

The validator may check:

- ZIP CRC and safe paths
- required repository structure
- Markdown links and anchors
- fenced-code balance
- CSV syntax and row widths
- date continuity
- model-error sequence continuity
- protected open-record status
- checksum validity
- release metadata
- RingConn source-byte preservation
- governed semantic warnings

Validation is divided into:

```text
Artifact identity
      ↓
Repository mechanics
      ↓
Human semantic review
      ↓
Interpretation
```

Mechanical validity does not establish interpretive correctness.

The validator does not:

- edit files
- infer replacement values
- normalize provider exports
- score predictions
- declare phases
- replace scheduled human audits

---

## Dashboards and Derived Views

- [dashboards](dashboards) — derived summaries and non-primary views
- [LATEST.md](LATEST.md) — executive current-state dashboard

Dashboards compress lower-level evidence.

They must not introduce claims stronger than the reports, data, artifacts, or preregistered rules they summarize.

---

## Roadmap

- [roadmap](roadmap) — planned repository and analytical development

Roadmap items are not current evidence.

They represent possible future work and remain subordinate to:

- operator capacity
- archive governance
- active biological observation
- release priorities
- demonstrated need

---

## Archive Structure

| Path | Role |
|---|---|
| `/snapshots` | Primary source artifacts and milestone evidence |
| `/data` | Canonical, curated, model-error, and source-export data layers |
| `/data/source_exports` | Byte-preserved provider and device exports |
| `/reports` | Active collection and closed retrospective interpretation |
| `/data/model_error` | Registered predictions, outcomes, and calibration |
| `/methodology` | Core collection, privacy, evaluation, and preregistration rules |
| `/docs/methodology` | Extended analytical methodology |
| `/protocols` | Active, historical, and superseded protocols |
| `/experiments` | Defined intervention-specific experiments |
| `/schemas` | Templates and structural definitions |
| `/tools` | Read-only local validation and future archive utilities |
| `/dashboards` | Derived and compressed views |
| `/docs/audits` | Repository integrity and governance audits |
| `/roadmap` | Planned future work |
| `/docs` | Observer guidance, concepts, audits, and extended context |

---

## Reading the Archive

Use:

- `/snapshots` for **primary evidence**
- `/data` for **structured longitudinal tracking and preserved source exports**
- `/reports` for **system behavior across time**
- `/data/model_error` for **prediction versus observed outcome review**
- `/methodology` for **collection, privacy, preregistration, and evaluation rules**
- `/protocols` for **protocol history and status**
- `/experiments` for **experiment state and provenance**
- `/tools` for **local mechanical validation**
- `/docs` for **observer guidance, concepts, audits, and extended methodology**

---

## Recommended First-Contact Flow

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
data/DATA_QUALITY_NOTES.md
  ↓
docs/FOR_OBSERVERS.md
```

---

## Recommended Evidence-Inspection Flow

```text
LATEST.md
  ↓
Relevant Closed Report
  ↓
Canonical Structured Dataset
  ↓
Source Snapshot or Source Export
  ↓
Data-Quality Notes
  ↓
Governance and Methodology
```

---

## Recommended Prediction-Review Flow

```text
data/model_error/model_error_gap_v1.csv
  ↓
Applicable Evaluation Plan
  ↓
Applicable Collection Plan
  ↓
Contemporaneous Reports and Notes
  ↓
Source Outcome Artifacts
  ↓
Closure Record
  ↓
UDI and Calibration Updates
```

---

## Recommended August Snapshot Review Flow

Before results:

```text
methodology/open_prediction_evaluation_plan_041_044.md
  ↓
methodology/2026-08-snapshot-collection-plan.md
  ↓
Ordinary Active Observation
  ↓
Source-Artifact Capture
```

After results become available:

```text
Complete Source Artifact Set
  ↓
Privacy and Checksum Review
  ↓
Structured Transcription
  ↓
Collection-Condition Comparison
  ↓
Registered Model-Error Evaluation
  ↓
Retrospective Snapshot Interpretation
  ↓
Separate Phase Review
```

No result should bypass the preregistered collection and evaluation layers.

---

## Recommended Verification Flow

```text
Download or Pull Current Repository
  ↓
Run tools/validate_repository.py
  ↓
Review Errors
  ↓
Review Governed Warnings
  ↓
Perform Human Semantic Spot Check
  ↓
Record Formal Audit When Scheduled or Materially Required
```

See:

- [VERIFICATION.md](VERIFICATION.md)
- [tools/validate_repository.py](tools/validate_repository.py)
- [docs/audits](docs/audits)

---

## Recommended Temporal Flow

```text
LATEST.md
  ↓
EPOCH_INDEX.md
  ↓
SNAPSHOT_LOG.md
  ↓
Relevant Weekly Reports
  ↓
/snapshots/YYYY-MM/
```

---

## Recommended Full Reading Flow

```text
docs/START_HERE.md
  ↓
docs/NEWCOMER_PATH.md
  ↓
INDEX.md
  ↓
Core Governance
  ↓
Data and Source Layers
  ↓
Reports
  ↓
Model-Error Layer
```

---

## Correction Path

When a possible error is identified:

```text
Preserve Current State
  ↓
Locate Strongest Source
  ↓
Classify the Issue
  ↓
Document the Finding
  ↓
Correct Only if Source-Supported
  ↓
Preserve Git History
  ↓
Rerun Validation
  ↓
Review Dependent Summaries
```

Relevant documents:

- [GOVERNANCE.md](GOVERNANCE.md)
- [methodology/data-collection.md](methodology/data-collection.md)
- [data/DATA_QUALITY_NOTES.md](data/DATA_QUALITY_NOTES.md)
- [VERIFICATION.md](VERIFICATION.md)
- [CHANGELOG.md](CHANGELOG.md)

---

## Archive Standard

This repository is organized to preserve:

- continuity
- traceability
- interpretive restraint
- visible uncertainty
- source-backed correction
- prediction accountability
- longitudinal readability
- evidence-first evaluation
- reproducible mechanical validation
- distinction among artifacts, datasets, reports, dashboards, predictions, protocols, experiments, and governance

Where uncertainty exists:

- verified source evidence takes precedence
- missingness remains visible
- predictions remain open when necessary
- candidate evidence remains provisional
- phase declarations wait for retrospective criteria
- preregistered rules remain fixed through outcome review
- mechanical validation does not substitute for semantic judgment
- no claim extends beyond the recorded single-subject archive

---

## Current Archive Posture

- **Observation model:** Continuous and artifact-first
- **Environmental posture:** Defined protocol constraints with incomplete control
- **Interpretation:** Retrospective and evidence-bound
- **Prediction layer:** Formally registered and separately governed
- **August collection governance:** Preregistered before outcome access
- **Correction model:** Source-backed, narrow, and traceable
- **Phase model:** Retrospectively declared
- **Validation model:** Local read-only mechanical validation followed by human semantic review
- **Public scope:** Bounded single-subject archive
- **Release posture:** Versioned and DOI-preserved

---

## Version Note

This index was aligned on 2026-08-03 with the repository’s current:

- Phase 2 operating state
- W30 retrospective closeout
- W31 active observation window
- canonical sleep coverage through 2026-08-02
- August snapshot preregistration
- open prediction evaluation plan
- source-preserved RingConn layer
- methodology-directory structure
- local repository validator
- expanded verification workflow
- privacy and correction boundaries
- observer-evaluation paths

The revision:

- advances the active weekly-report link from W30 to W31
- identifies W30 as the most recent closed weekly report
- aligns the temporal and reports sections with the current repository state
- advances the index alignment date to 2026-08-03
- records canonical sleep coverage through 2026-08-02
- preserves central access to the August collection plan
- preserves central access to the local validator
- preserves the methodology directory guide
- distinguishes structured data from source-preserved exports
- distinguishes collection plans from outcome evidence
- preserves the dedicated August snapshot and verification reading flows
- improves navigation and current-state representation only

It does not alter:

- any source value
- any canonical dataset value
- any protocol exposure
- any report observation
- any prediction record
- any scoring threshold
- any closed outcome
- any phase status
- any release metadata
