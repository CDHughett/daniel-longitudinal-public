# LATEST — Executive System State

Daniel Longitudinal Study  
Public Archive Status Dashboard

Current published release: `v1.1.0`  
Version DOI: https://doi.org/10.5281/zenodo.22759132  
All-versions DOI: https://doi.org/10.5281/zenodo.20815611

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

**Plain-language summary:** Training is stable and currently requires little active management. Week 38 is testing whether the extra capacity seen at the end of Week 37 appears again before any progression is considered.

Formal archive labels and governance state:

- **Phase:** Phase 2 — Load Integration
- **Weekly operating posture:** Consolidation / reserve-replication observation
- **Broader Phase 2 substate:** Consolidation / lock-in observation
- **Active window:** 2026-W38
- **Prior window:** 2026-W37 closed
- **Installed architecture:** B1 + Load Integration
- **Supplementation context:** Material simplification effective 2026-09-18; the prior broad multi-compound baseline was replaced with a reduced evidence-weighted architecture. This is a documented protocol-context boundary, not a causal explanation for current sleep, autonomic, performance, or biological observations. See [`protocols/supplementation-architecture-2026-09-18.md`](protocols/supplementation-architecture-2026-09-18.md)
- **System posture:** Keep the current submaximal workload unchanged and observe whether the reserve seen at W37 closeout repeats before any governed escalation
- **Behavioral posture:** Post-travel re-entry resolved without visible reacquisition cost; B1 and Load Integration remained repeatedly low-overhead across six consecutive complete days. Precise session-level labels remain preserved in the weekly report and structured training layer
- **Recovery posture:** Recurrent short-window autonomic variability remains under observation; W37 again showed that overnight disturbance and next-day functional impairment were not interchangeable in the observed cases
- **Bodyweight/intake posture:** Lower intake and bodyweight remain observational variables, not stand-alone progression or recovery-intervention triggers
- **Model-error posture:** Records 041–046 are closed/scored; record 043 remains closed as not supported (`overall_improvement_not_met`, error direction `over`)
- **Data-quality posture:** DQ-011 remains open for source verification of the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm; v1.31 HRV note/field differences are source-role documented without inferred correction
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge, and TruHealth source artifacts archived; Model Error 043 adjudication complete

The weekly operating posture describes the immediate observation condition for the active report. The broader Phase 2 substate remains the canonical phase-map interpretation. A reserve-replication observation does not itself declare progression or a new phase.

Plain-language definitions for reserve, capacity versus exposure, weekly operating posture, B1, and Load Integration are maintained in [`docs/CONCEPTS.md`](docs/CONCEPTS.md).

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 37 Closeout

Observation window:

```text
2026-09-14 through 2026-09-20
```

Completed formal training:

- 6 B1 sessions / 330 minutes / 18.12 miles
- 6 Load Integration sessions / 270 minutes
- 600 total formal training minutes

Structured weekly metrics:

| Marker | W37 |
|---|---:|
| Morning bodyweight | 232.6 lb |
| Daily biomarker HRV | 63.4 ms |
| Resting heart rate | 48.3 bpm |
| Daily average heart rate | 63.1 bpm |
| Sleep HRV | 70.6 ms |
| Sleep average heart rate | 56.6 bpm |
| Total sleep | 7h52m |
| Deep sleep | approximately 1h12m |
| REM sleep | approximately 1h07m |

The week opened with a final travel/rest day on 2026-09-14. Normal B1 + Load Integration operation resumed on 2026-09-15 and remained intact for six consecutive days without make-up volume, a reduced re-entry session, or recovery-directed unloading.

The strongest qualitative additions were:

- ordinary post-travel re-entry without visible reacquisition cost
- repeated low-overhead execution after the interruption, with the precise session-level descriptors preserved in the closed W37 report
- yard work absorbed between B1 and Load Integration on 2026-09-16 without protocol modification
- a bounded 2026-09-18 pre-sleep stress exposure that produced an overnight autonomic response with preserved scheduled training afterward
- an unofficial 2026-09-20 final-set probe of 8 pull-ups and 18 push-ups after programmed work with minimal reported degradation
- explicit preservation of that probe as preliminary reserve evidence rather than a progression authorization

Week 37 is therefore best summarized as **successful ordinary re-entry with preliminary reserve evidence**.

Full retrospective record: [`reports/2026-W37.md`](reports/2026-W37.md)

---

## Week 38 Operating Posture

Active window:

```text
2026-09-21 through 2026-09-27
```

Week 38 preserves the same B1 + Load Integration architecture and treats reserve replication as the immediate observation target.

Observe:

- whether reserve above the current prescription reappears under ordinary conditions
- whether repeat reserve preserves movement quality rather than merely increasing repetition count
- whether apparent reserve coexists with stable recovery, bodyweight, subjective state, and next-day function
- whether the installed architecture remains low-overhead while reserve is present
- naturally occurring ordinary-life workload without manufacturing robustness tests

Do not:

- add routine workload because of one favorable capacity probe
- turn every session into a test
- progress solely because subjective execution feels easy
- unload solely because of one less-favorable wearable night
- replace unresolved source values by inference
- reopen or rescore closed Model Error records
- declare Phase 2D from reserve evidence alone

Active report: [`reports/2026-W38.md`](reports/2026-W38.md)

---

## Model-Error State

| Record | Status |
|---|---|
| 041 | Closed / supported |
| 042 | Closed / not supported — continued adaptation |
| 043 | **Closed / not supported — overall improvement not met / over** |
| 044 | Closed / not supported — narrow snapshot-directed governance deviation |
| 045 | Closed / supported |
| 046 | Closed / failed_autonomic_recompression |

Record 043’s criterion-level adjudication is preserved in [`data/model_error/record_043_closure.md`](data/model_error/record_043_closure.md).

Fixed scoring windows remain fixed. Later evidence does not retroactively rescue a failed prediction or reopen a closed record.

---

## Current Verification and Provenance

- read-only core repository validator active
- read-only machine-readable semantic validator active
- read-only August snapshot cross-layer validator active
- post-release coherence validator active
- GitHub Actions runs all current validators on pushes to `main` and pull requests
- historical training prefix through 2026-08-30 remains protected at 325 sessions while later governed rows append
- exact retained private-source hashes are registered only when the exact bytes are available
- `Daniel_Dataset_v1.31` is registered in the private-source provenance manifest
- public daily biomarkers and canonical sleep contain 224 continuous rows through 2026-09-20
- public training contains 362 completed-session rows through 2026-09-20
- public context index contains 49 bounded events through 2026-09-20
- August TruDiagnostic provider artifacts remain registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction remains preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)  
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)  
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W38.md`](reports/2026-W38.md) — active week
- [`reports/2026-W37.md`](reports/2026-W37.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture is preservation with replication: reserve may be observed, but escalation must be earned by repeat evidence rather than inferred from one favorable session.
