# LATEST — Executive System State

Daniel Longitudinal Study
Public Archive Status Dashboard

Archive DOI: https://doi.org/10.5281/zenodo.20815612

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

- **Phase:** Phase 2 — Load Integration
- **Operating substate:** Consolidation / re-entry observation
- **Active window:** 2026-W37
- **Prior window:** 2026-W36 closed
- **Installed architecture:** B1 + Load Integration
- **System posture:** Preserve the installed architecture after an ordinary-life travel interruption; observe whether cadence returns without compensation or protective unloading
- **Behavioral posture:** Trait-like / ambient execution remained repeatedly present when training occurred in W36; W37 now tests ordinary re-entry rather than manufactured portability
- **Recovery posture:** Recurrent early-night autonomic variability remains visible, while next-day function has repeatedly remained more stable than the nocturnal signal alone would imply
- **Bodyweight/intake posture:** Lower intake and bodyweight remain observational variables, not progression or recovery-intervention triggers
- **Model-error posture:** Records 041–046 are closed/scored; record 043 closed on 2026-09-10 as not supported (`overall_improvement_not_met`, error direction `over`)
- **Data-quality posture:** DQ-011 remains open for source verification of the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge, and TruHealth source artifacts archived; Model Error 043 adjudication complete

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 36 Closeout

Observation window:

```text
2026-09-07 through 2026-09-13
```

Completed formal training:

- 6 B1 sessions / 330 minutes
- 5 Load Integration sessions / 225 minutes
- 555 total formal training minutes

Structured weekly metrics:

| Marker | W36 |
|---|---:|
| Morning bodyweight | 233.5 lb |
| Daily biomarker HRV | 61.0 ms |
| Resting heart rate | 48.9 bpm* |
| Daily average heart rate | 63.1 bpm |
| Sleep HRV | 67.0 ms |
| Sleep average heart rate | 56.3 bpm |
| Total sleep | 7h33m |
| Deep sleep | approximately 1h05m |
| REM sleep | approximately 1h17m |

\*The weekly RHR mean uses the recorded 2026-09-08 value of 64 bpm. DQ-011 keeps that source value intact while its originating field is verified.

W36 did not reproduce the prior two weeks' complete 700-minute architecture because ordinary-life travel removed LI on 2026-09-12 and both B1 and LI on 2026-09-13. The reduction was contextual rather than recovery-directed.

The strongest qualitative additions were:

- five consecutive full B1 + LI days from 2026-09-07 through 2026-09-11 with preserved execution quality
- repeated ambient / trait-like Load Integration execution, described as owned by 2026-09-11
- a recorded 2026-09-09 pull-up set showing controlled bottom, midpoint, and top positional ownership
- an unsolicited external-observer point on 2026-09-09 when an unfamiliar gym-goer initiated a conversation about the recurring treadmill routine
- recurrent early-night HR excursions with later-night normalization and no clear multi-domain next-day functional collapse
- a natural travel interruption that separated actual exposure from apparent capacity without triggering compensatory training

Week 36 is therefore best summarized as **consolidation with a natural interruption**. It supports preserved system state under reduced exposure, but it does not independently prove full travel portability because the installed architecture was not executed in the travel environment on 2026-09-13.

Full retrospective record: [`reports/2026-W36.md`](reports/2026-W36.md)

---

## Week 37 Operating Posture

Active window:

```text
2026-09-14 through 2026-09-20
```

Week 37 preserves the same B1 + Load Integration architecture and treats post-travel return as a natural re-entry observation.

Observe:

- whether ordinary cadence returns without make-up volume
- whether B1 and LI immediately retain their prior ambient / trait-like quality
- overnight HR/HRV morphology relative to actual next-day function
- lower-intake/bodyweight compatibility across performance, appetite, GI state, mood, and ordinary activity
- naturally occurring portability/context changes without manufacturing tests

Do not:

- compensate for missed W36 volume
- increase workload solely because reserve capacity is visible
- unload solely because of one less-favorable wearable night
- manufacture portability tests
- replace the DQ-011 source value by inference
- reopen or rescore closed Model Error records
- declare Phase 2D from isolated favorable sessions

Active report: [`reports/2026-W37.md`](reports/2026-W37.md)

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
- `Daniel_Dataset_v1.30` is registered in the private-source provenance manifest
- August TruDiagnostic provider artifacts are registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction is preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W37.md`](reports/2026-W37.md) — active week
- [`reports/2026-W36.md`](reports/2026-W36.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture is ordinary re-entry under an unchanged architecture, with capacity and exposure kept analytically separate.
