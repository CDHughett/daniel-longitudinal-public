# LATEST — Executive System State

Daniel Longitudinal Study
Public Archive Status Dashboard

Archive DOI: https://doi.org/10.5281/zenodo.20815612

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

- **Phase:** Phase 2 — Load Integration
- **Operating substate:** Consolidation / lock-in observation
- **Active window:** 2026-W36
- **Prior window:** 2026-W35 closed
- **Installed architecture:** B1 + Load Integration
- **System posture:** Ordinary continuity after two consecutive complete 700-minute training weeks
- **Behavioral posture:** Increasingly economical / low-salience execution under unchanged workload
- **Recovery posture:** Overnight autonomic variability remains visible; weekly averages are not uniformly favorable, while ordinary function has remained preserved across the recently observed window
- **Bodyweight/intake posture:** Lower average bodyweight and lower reported intake remain observational background variables, not a recovery or testing intervention
- **Model-error posture:** Records 041–046 are closed/scored; record 043 closed on 2026-09-10 as not supported (`overall_improvement_not_met`, error direction `over`)
- **TruDiagnostic status:** August provider-result artifacts archived, checksum-registered, source-reconciled, and represented in the current structured snapshot layers
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge, and TruHealth source artifacts archived; Model Error 043 adjudication complete

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 35 Closeout

Observation window:

```text
2026-08-31 through 2026-09-06
```

Completed formal training:

- 7 B1 sessions / 385 minutes / approximately 21.14 miles
- 7 Load Integration sessions / 315 minutes
- 700 total formal training minutes

Structured weekly metrics:

| Marker | W35 |
|---|---:|
| Morning bodyweight | 232.9 lb |
| Daily biomarker HRV | 56.6 ms |
| Resting heart rate | 52.0 bpm |
| Daily average heart rate | 65.3 bpm |
| Sleep HRV | 63.0 ms |
| Sleep average heart rate | 53.1 bpm |
| Total sleep | 7h07m |
| Time in bed | 7h40m |
| Deep sleep | approximately 1h19m |
| REM sleep | approximately 50m |

Week 35 did **not** produce uniformly more favorable recovery telemetry. Relative to Week 34, average bodyweight, daily HRV, sleep HRV, and total sleep were lower, while resting and sleeping heart rate were higher.

At the same time, the prescribed behavioral architecture remained fully available.

The strongest qualitative additions were:

- deeper low-salience / subjectively trance-like Load Integration execution on 2026-09-02
- trait-level execution after substantial yard work on 2026-09-03
- visible unused workload capacity without converting that reserve into additional prescribed work
- preserved B1 + LI after mixed or less-favorable overnight recovery profiles
- strong overnight recovery on 2026-09-06 after the shorter/mixed 2026-09-05 sleep profile

The week is therefore best summarized as **task economy under variable physiology**, not perfect autonomic stability.

Full retrospective record: [`reports/2026-W35.md`](reports/2026-W35.md)

---

## Week 36 Operating Posture

Active window:

```text
2026-09-07 through 2026-09-13
```

Week 36 preserves the same B1 + Load Integration architecture.

Observe:

- persistence of low-salience execution
- overnight HR/HRV morphology relative to next-day function
- lower-intake/bodyweight compatibility without deliberate manipulation
- natural portability only when ordinary variation occurs
- any genuine mechanical, GI, mood, or recovery signal requiring action

Do not:

- escalate workload solely because reserve capacity is visible
- unload solely because of one wearable night
- manufacture portability tests
- convert short-window scale movement into a tissue-composition claim
- reopen or rescore record 043 from later favorable or unfavorable evidence
- declare Phase 2D from isolated favorable sessions

Active report: [`reports/2026-W36.md`](reports/2026-W36.md)

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
- GitHub Actions runs both on pushes to `main` and pull requests
- the historical training prefix through 2026-08-30 remains protected at 325 sessions while later governed rows append
- exact retained private-source hashes are registered only when the exact bytes are available
- v1.29 private-source identity is registered in the provenance manifest
- August TruDiagnostic provider artifacts are registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction is preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W36.md`](reports/2026-W36.md) — active week
- [`reports/2026-W35.md`](reports/2026-W35.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture remains observation under an unchanged architecture.
