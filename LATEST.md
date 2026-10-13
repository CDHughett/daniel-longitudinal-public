# LATEST — Executive System State

Daniel Longitudinal Study  
Public Archive Status Dashboard

Current published release: `v1.1.0`  
Version DOI: https://doi.org/10.5281/zenodo.22759132  
All-versions DOI: https://doi.org/10.5281/zenodo.20815611

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

**Plain-language summary:** Week 40 closed with seven B1 and six Load Integration sessions in a complete ordinary home week. Two defined LI progression variants were completed once each at low reported overall effort, while standard, reduced-load, and scheduled rest boundaries remained intact. Week 41 now observes whether the additional dose remains low-cost and recovery-compatible when repeated.

Formal archive labels and governance state:

- **Phase:** Phase 2 — Load Integration
- **Weekly operating posture:** Structured LI progression / repeatability observation
- **Broader Phase 2 substate:** Consolidation / lock-in observation
- **Active window:** 2026-W41
- **Prior window:** 2026-W40 closed
- **Installed architecture:** B1 + Load Integration, with bounded LI progression variants
- **Supplementation context:** The material simplification effective 2026-09-18 remains documented background protocol context, not a causal explanation for subsequent sleep, autonomic, performance or bodyweight changes. See [`protocols/supplementation-architecture-2026-09-18.md`](protocols/supplementation-architecture-2026-09-18.md)
- **System posture:** Observe whether the already completed LI progression prescriptions remain mechanically controlled, behaviorally low-overhead and recovery-compatible when repeated; preserve standard, reduced-load and rest boundaries
- **Behavioral posture:** W39 retention preceded W40 controlled expansion; neither first-exposure success nor unused capacity requires immediate additional training volume
- **Recovery posture:** W40 overnight sleep averaged 7h11m, with three nights below seven hours; Daily Biomarkers HRV averaged 72.4 ms and distinct Sleep Log HRV averaged 82.6 ms. Favorable first-exposure results do not establish cumulative recovery cost
- **Bodyweight/intake posture:** Seven W40 waking measurements averaged 227.0 lb, versus 228.7 lb from five W39 scale-available mornings; composition, mechanism, sustainable trajectory and nutritional sufficiency under repeat progression remain unresolved
- **Reserve/progression posture:** W40's pull/press and hinge/grip prescriptions were completed once each, not repeatedly validated; no maximal test, clean one-variable dose-response, or prospectively registered public protocol is claimed
- **Model-error posture:** Records 041–046 are closed/scored; record 043 remains closed as not supported (`overall_improvement_not_met`, error direction `over`)
- **Data-quality posture:** DQ-011 remains open for source verification of the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm; earlier v1.31 HRV note/field differences remain source-role documented without inferred correction
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge, and TruHealth source artifacts archived; Model Error 043 adjudication complete

The weekly operating posture describes the immediate observation question, whereas the broader Phase 2 substate remains the canonical phase-map interpretation. Controlled expansion is the retrospective W40 descriptor, not a formal phase declaration.

Plain-language definitions for reserve, capacity versus exposure, weekly operating posture, B1, and Load Integration are maintained in [`docs/CONCEPTS.md`](docs/CONCEPTS.md).

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 40 Closeout

Observation window:

```text
2026-10-05 through 2026-10-11
```

Completed formal training:

- 7 B1 sessions / 385 minutes / 21.14 miles
- 6 Load Integration sessions / 275 minutes
- 660 total formal training minutes across 13 completed sessions; October 11 LI rest was not counted as a training session

Structured weekly metrics:

| Marker | W40 |
|---|---:|
| Morning bodyweight | 227.0 lb |
| Daily biomarker HRV | 72.4 ms |
| Resting heart rate | 43.9 bpm |
| Daily average heart rate | 59.9 bpm |
| Sleep HRV | 82.6 ms |
| Sleep average heart rate | 45.6 bpm |
| Total overnight sleep | 7h11m |
| Deep sleep (wearable estimate) | 1h36m |
| REM sleep (wearable estimate) | 59m |

The original W40 plan called for an unchanged full-home baseline. Within the week, the operator introduced two defined LI progression variants. The closed report preserves the opening intention and the later execution without backdating a prospective public registration.

- October 7: strict pull-ups 5×4, push-ups 3×12 and supported rows 2×10 (using a plate-loaded T-bar row); row plate mass is not calibrated effective machine resistance
- October 10: trap bar 4×5 at existing load and dead hangs 3×45s, with baseline pulling and pressing
- Standard LI, the October 9 technique/reduced-load session and the October 11 scheduled LI rest were preserved
- Neither progression dose was repeated within W40; favorable immediate tolerance does not prove delayed recovery, nutrition adequacy or sustainable reserve

Week 40 is retrospectively summarized as **controlled expansion under retained governance**.

Full retrospective record: [`reports/2026-W40.md`](reports/2026-W40.md)  
Completed progression reference: [`protocols/load-integration-progression-exposures-2026-W40.md`](protocols/load-integration-progression-exposures-2026-W40.md)

---

## Week 41 Operating Posture

Active window:

```text
2026-10-12 through 2026-10-18
```

**Immediate question:** Does the newly increased LI workload remain mechanically controlled, behaviorally inexpensive and recovery-compatible when repeated?

Observe:

- repeatability of the W40 pull/press and hinge/grip prescriptions when actual context and readiness permit
- actual completed workload, tempo, session RPE, movement quality and 24–48-hour soreness/recovery cost
- stable B1 alongside separate standard, reduced-load and scheduled LI rest exposures
- overnight sleep quantity, cardiovascular signals, morning subjective state and ordinary activity
- measured waking bodyweight, GI timing and potential fueling demands without attributing mechanisms

Do not:

- convert one favorable progression week into automatic permission to raise volume or load again
- substitute isolated HRV or low RPE for repeated-dose evidence
- fill recovery sessions with unregistered work merely because additional capacity exists
- convert missed work into repayment, or infer tissue loss from acute scale changes
- reopen Model Error outcomes, retrospectively register forward claims, or declare Phase 2D from trait-level descriptions alone

Active report: [`reports/2026-W41.md`](reports/2026-W41.md)

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
- `Daniel_Dataset_v1.34` is registered in the private-source provenance manifest with exact retained-file identity
- public daily biomarkers and canonical sleep contain 245 continuous rows through 2026-10-11
- public training contains 396 completed-session rows through 2026-10-11
- public context index contains 52 bounded events through 2026-10-10
- August TruDiagnostic provider artifacts remain registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction remains preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)  
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)  
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W41.md`](reports/2026-W41.md) — active week
- [`reports/2026-W40.md`](reports/2026-W40.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture is replication before further escalation: preserve the aerobic anchor and distinct LI workloads while observing whether the first W40 progression doses remain inexpensive when repeated. Phase 2D remains undeclared.
