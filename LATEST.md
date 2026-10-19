# LATEST — Executive System State

Daniel Longitudinal Study  
Public Archive Status Dashboard

Current published release: `v1.1.0`  
Version DOI: https://doi.org/10.5281/zenodo.22759132  
All-versions DOI: https://doi.org/10.5281/zenodo.20815611

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

**Plain-language summary:** Week 41 closed with seven aerobic and six Load Integration sessions, including a further prescribed pull-up increase and a repeated expanded hinge/grip session. Training and ordinary activity remained available by report, while overnight recovery measurements varied. Week 42 now examines whether the added work remains manageable without an accumulating recovery cost.

Formal archive labels and governance state:

- **Phase:** Phase 2 — Load Integration
- **Weekly operating posture:** Continued LI progression / recovery-cost and dose-repeatability observation
- **Broader Phase 2 substate:** Consolidation / lock-in observation
- **Active window:** 2026-W42
- **Prior window:** 2026-W41 closed
- **Installed architecture:** B1 + Load Integration, with separate progression, standard, reduced-load and rest sessions
- **Supplementation context:** The simplification effective 2026-09-18 remains documented background context without causal attribution. See [`protocols/supplementation-architecture-2026-09-18.md`](protocols/supplementation-architecture-2026-09-18.md)
- **System posture:** Observe measured completion, movement quality and delayed recovery across additional LI exposures; no automatic further increase
- **Behavioral posture:** W40 controlled expansion preceded W41 conditional repeatability; deliberately lighter and rest boundaries remained intact
- **Recovery posture:** W41 sleep averaged 7h17m, with two nights below seven hours. Daily Biomarkers HRV averaged 70.6 ms and separate overnight HRV averaged 75.7 ms. Sleeping heart rate rose on selected nights without reported loss of training function
- **Bodyweight/intake posture:** Seven W41 waking measurements averaged 226.4 lb versus W40's 227.0 lb; composition and nutritional adequacy are not established
- **Reserve/progression posture:** The W41 pull/press prescription increased to 5×5 pull-ups, while expanded hinge/grip work repeated; favorable reported execution does not establish absent cumulative recovery cost
- **Model-error posture:** Records 041–046 are closed/scored; Record 043 remains closed as not supported (`overall_improvement_not_met`, error direction `over`)
- **Data-quality posture:** DQ-011 remains open for source verification of the 2026-09-08 resting-heart-rate value of 64 bpm; earlier HRV field/note differences remain documented without inferred correction
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge and TruHealth source artifacts archived; Model Error 043 adjudication complete

The weekly operating posture is the open W42 question; the broader Phase 2 substate remains the canonical phase-map interpretation. **Conditional repeatability** is the retrospective W41 descriptor, not a formal phase declaration.

Plain-language definitions for reserve, capacity versus exposure, weekly operating posture, B1 and Load Integration are maintained in [`docs/CONCEPTS.md`](docs/CONCEPTS.md). Current row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 41 Closeout

Observation window:

```text
2026-10-12 through 2026-10-18
```

Completed formal training:

- 7 B1 sessions / 385 formal minutes / 21.14 miles
- 6 Load Integration sessions / 285 formal minutes
- 670 total formal minutes across 13 completed sessions; October 18 scheduled LI rest was not counted

Structured weekly metrics:

| Marker | W41 |
|---|---:|
| Morning bodyweight | 226.4 lb |
| Daily biomarker HRV | 70.6 ms |
| Resting heart rate | 44.6 bpm |
| Daily average heart rate | 61.4 bpm |
| Sleep HRV | 75.7 ms |
| Sleep average heart rate | 51.6 bpm |
| Total overnight sleep | 7h17m |
| Deep sleep (wearable estimate) | 1h18m |
| REM sleep (wearable estimate) | 49m |

W41's opening question asked whether the W40 progression doses could be repeated. October 14 advanced pull-ups from 5×4 to 5×5 prescribed repetitions, rather than performing an identical upper-body dose; October 17 more closely repeated the expanded hinge/grip prescription. Standard and reduced-load work and scheduled LI rest remained bounded. Recovery measurements varied despite reported continued training ease, limiting claims about cumulative cost.

Week 41 is retrospectively summarized as **conditional repeatability**. Source-grounded detail and its limitations are preserved in [`reports/2026-W41.md`](reports/2026-W41.md). The first-exposure reference remains in [`reports/2026-W40.md`](reports/2026-W40.md) and [`protocols/load-integration-progression-exposures-2026-W40.md`](protocols/load-integration-progression-exposures-2026-W40.md).

---

## Week 42 Operating Posture

Active window:

```text
2026-10-19 through 2026-10-25
```

**Open question:** Does the expanded LI workload remain reproducible in actual repetitions, movement quality, delayed recovery and ordinary-day function across further exposures, and what (if any) progression decision does the evidence support?

Observe:

- prescribed versus verified work, loading, movement control and recovery over 24–48 hours
- the W40 5×4 and W41 5×5 pull-up doses as different comparison conditions
- B1 as reference while progression, standard, reduced-load and rest days remain distinct
- overnight HRV, sleeping heart rate, sleep duration, morning function and total ordinary-life work
- standardized waking weight and nutrition uncertainty, without inventing mechanisms

Do not assume new work must be added because the previous session felt easy; do not retroactively register a prediction, declare Phase 2D, create training debt or assign a W42 outcome before its close.

Active report: [`reports/2026-W42.md`](reports/2026-W42.md).

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
- latest weekly rollover validator active
- read-only August snapshot cross-layer validator active
- post-release coherence validator active
- GitHub Actions runs all current validators on pushes to `main` and pull requests
- historical training prefix through 2026-08-30 remains protected at 325 sessions while later governed rows append
- exact retained private-source hashes are registered only when the exact bytes are available
- `Daniel_Dataset_v1.35` is registered in the private-source provenance manifest with exact retained-file identity; the private workbook is not published
- public daily biomarkers and canonical sleep contain 252 continuous rows through 2026-10-18
- public training contains 409 completed-session rows through 2026-10-18
- public context index contains 53 bounded events through 2026-10-14
- August TruDiagnostic provider artifacts remain registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction remains preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)  
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)  
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W42.md`](reports/2026-W42.md) — active week
- [`reports/2026-W41.md`](reports/2026-W41.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture is to measure actual work and delayed recovery across further structured exposures, preserving B1 and the lighter/rest boundaries. Phase 2D remains undeclared.
