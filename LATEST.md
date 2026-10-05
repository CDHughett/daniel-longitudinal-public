# LATEST — Executive System State

Daniel Longitudinal Study  
Public Archive Status Dashboard

Current published release: `v1.1.0`  
Version DOI: https://doi.org/10.5281/zenodo.22759132  
All-versions DOI: https://doi.org/10.5281/zenodo.20815611

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

**Plain-language summary:** Training remains stable and low-overhead. Week 39 closed with the established B1 + Load Integration architecture returning immediately after a short travel interruption and remaining available across five consecutive complete home training days. Week 40 now observes a complete ordinary home week under the unchanged prescription before the separate progression question is reconsidered.

Formal archive labels and governance state:

- **Phase:** Phase 2 — Load Integration
- **Weekly operating posture:** Consolidation / full-home baseline observation
- **Broader Phase 2 substate:** Consolidation / lock-in observation
- **Active window:** 2026-W40
- **Prior window:** 2026-W39 closed
- **Installed architecture:** B1 + Load Integration
- **Supplementation context:** Material simplification effective 2026-09-18 remains documented background protocol context, not a causal explanation for current sleep, autonomic, performance, bodyweight, or biological observations. See [`protocols/supplementation-architecture-2026-09-18.md`](protocols/supplementation-architecture-2026-09-18.md)
- **System posture:** Preserve the unchanged architecture through a complete ordinary home week, observe whether the low operating cost remains stable, and only then review whether a small governed progression experiment is justified
- **Behavioral posture:** Week 39 ended the travel interruption without repayment behavior and restored five consecutive complete B1 + Load Integration days without a staged rebuilding period
- **Recovery posture:** Two unusual early-night cardiovascular episodes during W39 later normalized substantially and were followed by preserved next-day function; recurrence remains an observation target rather than an automatic training veto
- **Bodyweight/intake posture:** Five scale-available W39 mornings averaged 228.7 lb; the lower observed range remains real as a scale observation while composition, mechanism, and sustainable rate remain unresolved
- **Reserve/progression posture:** The Week 37 reserve observation remains preliminary because neither W38 nor W39 contained a second interpretable capacity probe; Week 40 first establishes a clean full-home baseline before progression is reconsidered
- **Model-error posture:** Records 041–046 are closed/scored; record 043 remains closed as not supported (`overall_improvement_not_met`, error direction `over`)
- **Data-quality posture:** DQ-011 remains open for source verification of the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm; the earlier v1.31 HRV note/field differences remain source-role documented without inferred correction
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge, and TruHealth source artifacts archived; Model Error 043 adjudication complete

The weekly operating posture describes the immediate observation condition for the active report. The broader Phase 2 substate remains the canonical phase-map interpretation. Retention, repeated ease, favorable recovery, or one reserve observation does not itself declare progression or a new phase.

Plain-language definitions for reserve, capacity versus exposure, weekly operating posture, B1, and Load Integration are maintained in [`docs/CONCEPTS.md`](docs/CONCEPTS.md).

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 39 Closeout

Observation window:

```text
2026-09-28 through 2026-10-04
```

Completed formal training:

- 5 B1 sessions / 275 minutes / 15.10 miles
- 5 Load Integration sessions / 225 minutes
- 500 total formal training minutes across 10 completed sessions

Structured weekly metrics:

| Marker | W39 |
|---|---:|
| Morning bodyweight | 228.7 lb |
| Daily biomarker HRV | 65.6 ms |
| Resting heart rate | 45.0 bpm |
| Daily average heart rate | 60.7 bpm |
| Sleep HRV | 71.3 ms |
| Sleep average heart rate | 50.7 bpm |
| Total sleep | 7h20m |
| Deep sleep | approximately 1h20m |
| REM sleep | approximately 58m |

Travel remained active on 2026-09-28 and 2026-09-29, and no formal training was performed on either day. No make-up volume was introduced.

Normal home B1 + Load Integration resumed on 2026-09-30. Five consecutive complete two-session days then followed through 2026-10-04 without protective unloading, a staged re-entry, or a documented performance loss.

The strongest W39 additions were:

- immediate restoration of the unchanged architecture after travel
- mild first-return stiffness that did not alter the prescribed work and resolved without intervention
- return of automatic movement setup during Load Integration
- two unusual early-night cardiovascular episodes with substantial later normalization and preserved next-day function
- a lower observed bodyweight range without a demonstrated tissue-composition mechanism
- one brief B1 heart-rate excursion above the nominal target without documented sustained strain or protocol change
- continued restraint: no repeat reserve probe, compensatory volume, or automatic progression was introduced

Week 39 is therefore best summarized as **short-interruption retention under preserved governance**.

Full retrospective record: [`reports/2026-W39.md`](reports/2026-W39.md)

---

## Week 40 Operating Posture

Active window:

```text
2026-10-05 through 2026-10-11
```

Week 40 preserves the same B1 + Load Integration architecture and treats a complete ordinary home week as the immediate observation target.

Observe:

- whether the unchanged architecture remains fully available across the complete home week
- whether low-overhead execution remains stable without travel-transition effects
- whether morning bodyweight stabilizes, rebounds, or continues in the current lower range under normal home conditions
- whether unusual early-night cardiovascular behavior recurs and, if so, whether it again normalizes later and remains dissociated from next-day function
- whether brief B1 heart-rate excursions above the nominal target remain isolated
- whether Load Integration remains inexpensive without subjective ease becoming an automatic progression trigger
- whether the full-home baseline becomes strong enough to justify a later single-variable progression experiment

Do not:

- repay the completed travel interruption
- progress solely because post-travel return was successful
- unload solely because an isolated wearable night is unfavorable
- use favorable wearable values as automatic progression permission
- turn each session into a reserve test
- replace unresolved source values by inference
- reopen or rescore closed Model Error records
- declare Phase 2D from retention, ease, or reserve evidence alone

Active report: [`reports/2026-W40.md`](reports/2026-W40.md)

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
- `Daniel_Dataset_v1.33` is registered in the private-source provenance manifest
- public daily biomarkers and canonical sleep contain 238 continuous rows through 2026-10-04
- public training contains 383 completed-session rows through 2026-10-04
- public context index contains 51 bounded events through 2026-09-29
- August TruDiagnostic provider artifacts remain registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction remains preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)  
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)  
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W40.md`](reports/2026-W40.md) — active week
- [`reports/2026-W39.md`](reports/2026-W39.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture is baseline before escalation: preserve ordinary home operation long enough to determine whether the progression question is ready for a small, registered, interpretable test.
