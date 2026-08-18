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
- [reports/2026-W33.md](reports/2026-W33.md) — active weekly observation window
- [reports/2026-W32.md](reports/2026-W32.md) — most recent closed weekly report
- [PHASE_MAP.md](PHASE_MAP.md) — phase architecture
- [STATE_TRANSITIONS.md](STATE_TRANSITIONS.md) — recorded phase and state changes
- [EPOCH_INDEX.md](EPOCH_INDEX.md) — temporal index of major observation periods
- [SNAPSHOT_LOG.md](SNAPSHOT_LOG.md) — chronological artifact log
- [docs/WEEK_INDEXING.md](docs/WEEK_INDEXING.md) — internal reporting-week convention
- [VERSIONING.md](VERSIONING.md) — repository release and archive-version rules
- [CHANGELOG.md](CHANGELOG.md) — recent structural and methodology changes
- [docs/archive/CHANGELOG_ARCHIVE.md](docs/archive/CHANGELOG_ARCHIVE.md) — preserved historical changelog entries

### Current August governance

- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md) — preserved preregistered scoring and admissible-evidence rules for records 041–044
- [methodology/open_prediction_evaluation_plan_045.md](methodology/open_prediction_evaluation_plan_045.md) — completed preregistered plan retained for closed record 045
- [methodology/open_prediction_evaluation_plan_046.md](methodology/open_prediction_evaluation_plan_046.md) — active prospective evaluation plan for autonomic unload/reload record 046
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — August 17–18 collection plan and recorded execution conditions

The records 041–044 evaluation plan and August snapshot collection plan were committed before their respective outcome access.

Current record state is:

```text
041:
closed / supported

042:
closed / not supported — continued adaptation

043:
open / TruDiagnostic provider results pending

044:
closed / not supported — narrow snapshot-directed governance deviation

045:
closed / supported

046:
open / unscored
```

Records 041, 042, and 044 were formally adjudicated at the August snapshot-cycle endpoint.

Their original preregistered evaluation artifact remains unchanged for provenance.

Record 043 remains open under the same original framework because its primary TruDiagnostic provider-result evidence is still pending.

Record 045 was registered on 2026-08-12 before its fixed admissible scoring window of:

```text
2026-08-13 through 2026-08-16
```

Record 045 is:

```text
closed / supported
```

Its completed evaluation plan remains preserved for provenance.

Record 046 was registered separately on 2026-08-17.

Its evidence structure is:

```text
2026-08-17:
registration context only

2026-08-18 through 2026-08-19:
descriptive unload / re-entry kinetics

2026-08-20 through 2026-08-23:
primary scoring window
```

Record 046 does not reopen or extend record 045.

Later Week 33 evidence does not reopen records 041, 042, or 044.

These documents do not themselves declare a phase transition.

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
- open predictions from completed scored predictions
- source-backed correction from unsupported rewriting
- mechanical validation from semantic review
- a preregistered collection plan from a result report
- an observation that generated a prediction from future evidence permitted to score that prediction
- a completed prediction from a later related prediction with a new evidence boundary
- governance failure from biological failure
- a model miss caused by underestimation from deterioration of the observed system

---

## Reports Layer

- [reports](reports) — active and closed weekly reports
- [reports/README.md](reports/README.md) — report modes, lifecycle, inclusion rules, and correction boundaries
- [reports/2026-W32.md](reports/2026-W32.md) — most recent closed weekly report
- [reports/2026-W33.md](reports/2026-W33.md) — current active weekly report

Reports may contain:

- contemporaneous collection during an active window
- retrospective weekly interpretation after closeout
- candidate evidence relevant to open model-error records
- structured summaries grounded in preserved evidence
- completed prediction scoring when the preregistered evidence boundary has closed
- historical reference to previously closed prediction outcomes when relevant to the current observation

Reports do not replace source artifacts or canonical structured datasets.

An active report does not determine its own final interpretation.

A completed prediction must not be extended merely because related observations continue afterward.

---

## Snapshots and Primary Artifacts

- [snapshots](snapshots) — primary biological, body-composition, performance, and source artifacts
- [SNAPSHOT_LOG.md](SNAPSHOT_LOG.md) — chronological snapshot index
- [snapshots/sleep_signal_core_v1.csv](snapshots/sleep_signal_core_v1.csv) — preserved compact sleep-signal artifact
- [snapshots/2026-08/2026-08 Epoch.md](snapshots/2026-08/2026-08%20Epoch.md) — August 2026 temporal anchor
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — preregistered plan and execution record for the August snapshot cycle

The August physical collection window is complete.

Current preserved physical source artifacts include:

```text
2026-08-dexa-body-comp.jpg
2026-08-dexa-summary.jpg
2026-08-vo2-summary.pdf
2026-08-bodpod-cosmed.jpg
```

The physical artifact set has been:

- privacy-reviewed
- assigned stable filenames
- incorporated into the August checksum manifest
- repository-validator verified

Current August state:

```text
physical collection:
complete

physical source-artifact preservation:
complete

TruDiagnostic sample collection:
complete

TruDiagnostic provider results:
pending

complete biological interpretation:
pending
```

Snapshot review should consider:

- collection date
- provider or device
- preparation conditions
- actual versus planned training exposure
- source completeness
- checksum status
- comparability with prior artifacts
- direct versus derived status
- public-original versus sanitized-derivative status
- preregistered collection and evaluation boundaries
- documented collection-condition deviations

Checksum validity confirms file identity, not biological or clinical validity.

A collection plan governs capture conditions.

It does not become outcome evidence.

Documented deviations remain visible rather than being retrospectively absorbed into the original plan.

---

## Structured and Source-Preserved Data Layer

- [data](data) — canonical, curated, model-error, and source-export data layers
- [data/sleep_longitudinal_v1.csv](data/sleep_longitudinal_v1.csv) — canonical sleep dataset, current through 2026-08-16
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

The August integrated biological snapshot must not be treated as complete until the pending primary molecular source evidence is available and verified.

---

## Prediction and Model-Error Layer

- [data/model_error](data/model_error) — prediction and calibration records
- [data/model_error/WHAT_THIS_LAYER_IS.md](data/model_error/WHAT_THIS_LAYER_IS.md) — model-error purpose and boundaries
- [data/model_error/model_error_gap_v1.csv](data/model_error/model_error_gap_v1.csv) — primary model-error register
- [data/model_error/udi_by_type_tracker.csv](data/model_error/udi_by_type_tracker.csv) — UDI and concordance summary by eligible prediction type
- [data/model_error/calibration_events_log.md](data/model_error/calibration_events_log.md) — major calibration events
- [data/model_error/historical](data/model_error/historical) — reconstructed historical records
- [methodology/prediction_evaluation.md](methodology/prediction_evaluation.md) — general prediction-evaluation methodology
- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md) — preserved preregistered evaluation plan for records 041–044
- [methodology/open_prediction_evaluation_plan_045.md](methodology/open_prediction_evaluation_plan_045.md) — completed preregistered evaluation plan for closed record 045
- [methodology/open_prediction_evaluation_plan_046.md](methodology/open_prediction_evaluation_plan_046.md) — active preregistered evaluation plan for open record 046
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — preregistered collection plan relevant to record 043
- [docs/methodology/prediction_to_outcome_pipeline.md](docs/methodology/prediction_to_outcome_pipeline.md) — prediction-to-outcome workflow
- [docs/methodology/valid_prediction_criteria.md](docs/methodology/valid_prediction_criteria.md) — valid-prediction requirements
- [docs/methodology/UDI_framework_v1.md](docs/methodology/UDI_framework_v1.md) — UDI methodology

Current open records are:

```text
043
046
```

Recently completed records are:

```text
041
042
044
045
```

### Record 041

Record 041 predicted:

```text
recovery_capacity:
stable
```

The recorded outcome is:

```text
actual:
stable

error direction:
none

status:
closed / supported
```

Accumulated loading produced measurable autonomic compression.

The registered recovery-capacity failure boundary nevertheless was not crossed because the physiological change did not converge with the required recovery-driven intervention, multi-session functional regression, or persistent suppression with qualifying functional or subjective deterioration.

Record 041 does not establish costless or unlimited recovery capacity.

---

### Record 042

Record 042 predicted:

```text
ambient_execution:
plateau
```

The recorded outcome is:

```text
actual:
continued_adaptation

error direction:
under

status:
closed / not supported
```

The registered qualitative-transition threshold was met across repeated dates, more than 14 calendar days, multiple contexts, and without substantive explanatory protocol progression.

The model underestimated continued adaptation beyond the predicted ambient-execution ceiling.

Record 042 does not independently declare Phase 2D.

---

### Record 043

Record 043 remains:

```text
open / unscored
```

Its primary comparison remains:

```text
May 2026
→
August 2026
```

The August physical collection is complete.

The TruDiagnostic sample was collected on 2026-08-17.

The corresponding provider-result domain remains pending.

DEXA, VO₂ max, Bod Pod, bodyweight, recovery telemetry, and subjective state remain supplemental under the registered evaluation structure.

No supplemental result may substitute for the pending primary TruDiagnostic evidence.

---

### Record 044

Record 044 predicted:

```text
protocol_governance:
preserved
```

The recorded outcome is:

```text
status:
closed / not supported

classification:
narrow snapshot-directed governance deviation

error direction:
under
```

Most of the observation window showed strong governance restraint.

However:

```text
2026-08-16
Load Integration intentionally withheld
to preserve recovery before VO₂ testing
```

The omission was testing-directed, intentional, not provider-required, and not recovery-driven.

Because the preregistered collection posture contained a separate snapshot-manipulation boundary, the pre-test omission constituted a governance miss.

The outcome does not establish broad protocol collapse, biological harm, or invalidity of the August snapshot.

---

### Record 045

Record 045 was registered on:

```text
2026-08-12
```

Its fixed scoring window was:

```text
2026-08-13 through 2026-08-16
```

Week 31 and observations from 2026-08-10 through 2026-08-12 were registration context only.

August 17–18 snapshot results were excluded.

The recorded outcome is:

```text
supported
```

The four preregistered autonomic thresholds were all favorable across the fixed scoring means.

Record 045 is closed.

Its result must not be altered by later unload/reload evidence.

---

### Record 046

Record 046 was separately registered on:

```text
2026-08-17
```

Its registered prediction is:

```text
reconvergence_persists_after_unload_reload
```

Evidence boundaries:

```text
2026-08-17:
registration context only

2026-08-18 through 2026-08-19:
descriptive unload / re-entry kinetics

2026-08-20 through 2026-08-23:
primary scoring window
```

Record 046 retains the same four autonomic thresholds used under record 045 for direct comparability.

It does not use August biological or performance outcomes for scoring.

It does not reopen records 041, 042, 044, or 045.

Registered predictions are permitted only within the governed model-error layer.

They must remain:

- time- or state-bounded
- preserved after registration
- evaluated after sufficient evidence exists
- open when evidence is insufficient
- retained when incorrect
- closed when their registered evaluation boundary is complete
- protected from later evidence that belongs to a new question

A collection plan may protect a prediction from outcome-directed manipulation.

It does not modify the prediction itself.

---

## Current Prediction Calibration State

The August 18 closure batch changed the eligible primary state and trajectory concordance layers.

Current tracked values are:

```text
Primary state concordance:
11 / 14
0.79

Primary trajectory concordance:
2 / 3
0.67
```

The change reflects:

```text
041:
trajectory / concordant

042:
trajectory / under-direction miss

044:
state / under-direction miss
```

Point and range magnitude UDI values remain unchanged by this closure batch.

Prediction calibration summaries are not measures of biological success.

They describe model agreement with registered outcomes.

---

## Methodology Structure

Methodology is split across two connected layers.

### `/methodology`

Core operating methodology and preregistration artifacts:

- [methodology/README.md](methodology/README.md) — methodology directory guide
- [methodology/data-collection.md](methodology/data-collection.md) — source, transcription, missingness, and correction rules
- [methodology/anonymization.md](methodology/anonymization.md) — artifact sanitization and privacy-remediation rules
- [methodology/prediction_evaluation.md](methodology/prediction_evaluation.md) — general prediction-evaluation rules
- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md) — preserved preregistered plan for records 041–044
- [methodology/open_prediction_evaluation_plan_045.md](methodology/open_prediction_evaluation_plan_045.md) — completed preregistered plan retained for record 045 provenance
- [methodology/open_prediction_evaluation_plan_046.md](methodology/open_prediction_evaluation_plan_046.md) — active prospective evaluation plan for record 046
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md) — August snapshot collection plan with actual execution conditions recorded

This layer governs:

- current collection
- source handling
- privacy handling
- correction
- prediction evaluation
- preregistered collection conditions
- outcome-access boundaries

The 041–044, 045, and 046 plans remain separate artifacts because their:

- registration dates differ
- evidence windows differ
- evaluation questions differ

The original 041–044 filename remains unchanged even though records 041, 042, and 044 are now closed.

Preserving the original committed artifact protects provenance and prevents outcome-driven rewriting.

Record 043 remains open under that framework until its required primary biological evidence is available.

The completed 045 plan likewise remains in place because preserving its original filename and content protects provenance.

Record 046 was added instead of extending 045 retrospectively.

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

## August Snapshot Governance

The August biological and performance collection is governed by:

- [methodology/open_prediction_evaluation_plan_041_044.md](methodology/open_prediction_evaluation_plan_041_044.md)
- [methodology/2026-08-snapshot-collection-plan.md](methodology/2026-08-snapshot-collection-plan.md)

The primary physical collection window was completed across:

```text
2026-08-17:
TruDiagnostic sample collection
DEXA
VO₂ max

2026-08-18:
Bod Pod
```

The underlying installed architecture remains:

```text
B1
+
Load Integration
```

The actual testing transition was:

```text
2026-08-16:
B1 completed
Load Integration intentionally withheld before testing

2026-08-17:
No B1
No Load Integration
TruDiagnostic
DEXA
VO₂ max

2026-08-18:
No B1
No Load Integration
Bod Pod

2026-08-19:
Planned return to normal B1 + Load Integration
```

The 2026-08-16 Load Integration omission and August 17–18 training withdrawal remain visible as actual collection-condition facts.

They are not retrospectively rewritten into the original representative-state collection posture.

The governance significance of the August 16 omission has already been adjudicated under record 044.

Record 044 closed as not supported because the testing-directed omission conflicted with the registered snapshot-manipulation boundary.

That governance result does not establish whether the deviation materially changed any August biological measurement.

Record 043 therefore remains open pending its primary TruDiagnostic evidence.

The biological snapshot and record 046 remain analytically separate.

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

The underlying current architecture remains:

```text
B1
+
Load Integration
```

The August testing-related interruption is a temporary exposure deviation rather than a newly declared recurring protocol.

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
- protected open-record status for records 043 and 046
- preserved closed/scored state and adjudicated outcomes for records 041, 042, 044, and 045
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
- independently score predictions
- declare phases
- replace scheduled human audits

For records 041, 042, 044, and 045, the validator protects their already adjudicated closed state.

For records 043 and 046, it protects the open/unscored prospective state.

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

For records 041–044, the preserved preregistered evaluation plan is:

```text
methodology/open_prediction_evaluation_plan_041_044.md
```

Current outcomes under that plan are:

```text
041:
closed / supported

042:
closed / not supported — continued adaptation

043:
open / pending primary evidence

044:
closed / not supported — governance deviation
```

For completed record 045, the applicable historical scoring plan is:

```text
methodology/open_prediction_evaluation_plan_045.md
```

For open record 046, the applicable prospective evaluation plan is:

```text
methodology/open_prediction_evaluation_plan_046.md
```

These plans must not be merged retrospectively because their registration boundaries differ.

---

## Recommended August Snapshot Review Flow

### Biological and performance collection

```text
methodology/open_prediction_evaluation_plan_041_044.md
  ↓
methodology/2026-08-snapshot-collection-plan.md
  ↓
Documented Actual Collection Conditions
  ↓
Source-Artifact Capture
  ↓
Privacy and Checksum Review
  ↓
Structured Transcription
  ↓
Registered Model-Error Evaluation
```

Current state:

```text
Physical source-artifact collection:
complete

TruDiagnostic sample collection:
complete

TruDiagnostic provider results:
pending

Record 043:
open
```

### Closed July–August records

```text
Record 041
recovery capacity
→ closed / supported

Record 042
ambient-execution plateau
→ closed / not supported
→ continued adaptation

Record 044
protocol governance
→ closed / not supported
→ narrow snapshot-directed governance deviation
```

These outcomes are historical and must not be rescored from later Week 33 evidence.

### Completed record 045

Record 045 was evaluated separately before later snapshot evidence could alter its scoring boundary:

```text
methodology/open_prediction_evaluation_plan_045.md
  ↓
2026-08-13 through 2026-08-16 source observations
  ↓
4-day means
  ↓
4 of 4 favorable thresholds
  ↓
Record 045 closed / supported
```

August 17–18 snapshot outcomes remain inadmissible for record 045.

### Active record 046

The later autonomic question is governed separately:

```text
methodology/open_prediction_evaluation_plan_046.md
  ↓
2026-08-17 registration context
  ↓
2026-08-18 through 2026-08-19 descriptive kinetics
  ↓
2026-08-20 through 2026-08-23 primary scoring
  ↓
Retrospective Record 046 Evaluation
```

August biological and performance outcomes are excluded from record 046 scoring.

After the complete August source-artifact set becomes available:

```text
Complete Source Artifact Set
  ↓
Privacy and Checksum Review
  ↓
Structured Transcription
  ↓
Collection-Condition Comparison
  ↓
Record 043 Evaluation
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
- completed predictions retain their original scoring boundary
- incorrect predictions remain visible as incorrect
- candidate evidence remains provisional until governed closure
- phase declarations wait for retrospective criteria
- preregistered rules remain fixed through outcome review
- mechanical validation does not substitute for semantic judgment
- observations that generate predictions remain distinct from future evidence permitted to score them
- later related observations require a new prospective boundary rather than reopening a completed prediction
- documented deviations remain visible
- governance misses remain distinct from biological outcomes
- no claim extends beyond the recorded single-subject archive

---

## Current Archive Posture

- **Observation model:** Continuous and artifact-first
- **Environmental posture:** Defined protocol constraints with incomplete control
- **Interpretation:** Retrospective and evidence-bound
- **Prediction layer:** Formally registered and separately governed
- **Open prediction set:** Records 043 and 046
- **Recently closed predictions:** 041 supported; 042 not supported / continued adaptation; 044 not supported / narrow governance deviation; 045 supported
- **Record 043 posture:** Primary August biological-translation prediction awaiting TruDiagnostic provider results
- **Record 046 posture:** Secondary prospective autonomic unload/reload trajectory probe
- **Record 046 primary scoring window:** 2026-08-20 through 2026-08-23
- **August physical collection:** Complete
- **August physical artifact preservation:** Complete and checksum-verified
- **August TruDiagnostic:** Sample collected; provider results pending
- **August collection governance:** Preregistered before outcome access; actual execution conditions preserved
- **Correction model:** Source-backed, narrow, and traceable
- **Primary state concordance:** 0.79
- **Primary trajectory concordance:** 0.67
- **Phase model:** Retrospectively declared
- **Current phase:** Phase 2 — Load Integration
- **Operating substate:** Consolidation / lock-in observation
- **Formal Phase 2D declaration:** None
- **Validation model:** Local read-only mechanical validation followed by human semantic review
- **Public scope:** Bounded single-subject archive
- **Release posture:** Versioned and DOI-preserved

---

## Version Note

This index was previously aligned on 2026-08-12 after prospective registration of Model Error 045.

That revision:

- exposed `methodology/open_prediction_evaluation_plan_045.md`
- advanced the then-current open model-error set from records 041–044 to records 041–045
- preserved `methodology/open_prediction_evaluation_plan_041_044.md` unchanged
- preserved `methodology/2026-08-snapshot-collection-plan.md`
- recorded Week 31 and 2026-08-10 through 2026-08-12 as registration context rather than scoring evidence for record 045
- fixed 2026-08-13 through 2026-08-16 as the prospective record 045 scoring window
- excluded August 17–18 snapshot outcomes from record 045 scoring
- extended validator protection through record 045

On 2026-08-17, this index was aligned with the completed Week 32 and current Week 33 governance state.

The 2026-08-17 revision:

- closed 2026-W32 and advanced 2026-W33 to the active weekly window
- advanced canonical sleep coverage through 2026-08-16
- recorded record 045 as closed and supported
- preserved the fixed record 045 scoring window and historical preregistration artifact
- removed record 045 from the open prediction set
- set the then-current open prediction set to records 041–044 and 046
- exposed `methodology/open_prediction_evaluation_plan_046.md`
- recorded 2026-08-17 as record 046 registration context only
- recorded 2026-08-18 through 2026-08-19 as descriptive unload/re-entry kinetics
- recorded 2026-08-20 through 2026-08-23 as the record 046 primary scoring window
- preserved the record 045 thresholds unchanged for direct 046 comparability
- separated the completed 045 question from the new unload/reload question
- updated validator documentation to protect records 041–044 and 046 as open at that time
- recorded record 045 as separately protected in its closed/scored state
- preserved the August 16 testing-directed Load Integration omission as an explicit collection-condition fact
- preserved the August 17–18 temporary training withdrawal as an explicit testing-related exposure state
- preserved the August biological and performance snapshot as independently governed from record 046
- preserved Phase 2 and the consolidation / lock-in observation substate
- left formal Phase 2D undeclared

The 2026-08-17 revision did not alter:

- any source value
- any canonical biological value
- records 041–044
- the registered prediction or scoring thresholds of record 045
- the registered prediction or scoring thresholds of record 046
- any completed outcome other than accurately documenting its current state
- the underlying B1 + Load Integration architecture
- the August snapshot collection plan
- any phase declaration
- any release metadata

On 2026-08-18, this index was aligned after formal adjudication of records 041, 042, and 044 and completion of the August physical snapshot collection layer.

The 2026-08-18 revision:

- records 041 as closed and supported
- records 042 as closed and not supported through continued adaptation
- records 044 as closed and not supported through a narrow snapshot-directed governance deviation
- preserves 045 as closed and supported
- reduces the current open prediction set to records 043 and 046
- preserves record 043 as open pending the primary TruDiagnostic provider-result domain
- preserves record 046 as open and unscored through its prospective reload window
- preserves `methodology/open_prediction_evaluation_plan_041_044.md` as the unchanged preregistered source governing the original evaluation
- records the August 17–18 physical collection window as complete
- records the August physical artifact set as archived, privacy-reviewed, checksum-manifested, and validator-verified
- preserves the August 16 Load Integration omission as testing-directed rather than recovery-driven
- records that the omission activated the separately preregistered record 044 snapshot-governance boundary
- does not infer that the governance deviation materially altered any August biological measurement
- preserves the primary-versus-supplemental boundary for record 043
- updates primary state concordance to 0.79 after record 044 closure
- updates primary trajectory concordance to 0.67 after records 041 and 042 closure
- leaves point and range magnitude UDI values unchanged
- updates validator documentation to protect records 041, 042, 044, and 045 as closed while records 043 and 046 remain open
- preserves Phase 2 and the consolidation / lock-in observation substate
- leaves formal Phase 2D undeclared

The 2026-08-18 revision does not alter:

- source artifacts
- canonical biological measurements
- the original prediction wording of records 041–044
- the frozen record 045 scoring boundary
- the frozen record 046 scoring boundary
- the pending record 043 outcome
- the underlying B1 + Load Integration architecture
- the original August collection-plan language
- any release metadata
- any formal phase declaration
