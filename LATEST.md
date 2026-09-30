# LATEST — Executive System State

Daniel Longitudinal Study  
Public Archive Status Dashboard

Current published release: `v1.1.0`  
Version DOI: https://doi.org/10.5281/zenodo.22759132  
All-versions DOI: https://doi.org/10.5281/zenodo.20815611

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

**Plain-language summary:** Training remains stable and low-overhead. Week 38 closed with the existing workload preserved despite repeated ease and a travel interruption; Week 39 is now watching whether normal B1 + Load Integration operation returns cleanly after travel before any progression is considered.

Formal archive labels and governance state:

- **Phase:** Phase 2 — Load Integration
- **Weekly operating posture:** Consolidation / post-travel return observation
- **Broader Phase 2 substate:** Consolidation / lock-in observation
- **Active window:** 2026-W39
- **Prior window:** 2026-W38 closed
- **Installed architecture:** B1 + Load Integration
- **Supplementation context:** Material simplification effective 2026-09-18; the prior broad multi-compound baseline was replaced with a reduced evidence-weighted architecture. This remains a documented protocol-context boundary, not a causal explanation for current sleep, autonomic, performance, bodyweight, or biological observations. See [`protocols/supplementation-architecture-2026-09-18.md`](protocols/supplementation-architecture-2026-09-18.md)
- **System posture:** Let the out-of-town interval finish without repayment behavior, restore the unchanged B1 + Load Integration architecture under ordinary home conditions, and only then revisit whether a governed progression probe is justified
- **Behavioral posture:** Week 38 preserved five consecutive complete two-session days plus a sixth pre-travel B1 session; repeated ease did not trigger escalation, and travel-directed omissions did not become training debt
- **Recovery posture:** Sleep quantity and autonomic telemetry varied while prescribed function remained broadly preserved; neither favorable nor less-favorable short-window values independently changed the program
- **Bodyweight/intake posture:** Morning bodyweight moved into a lower observed range during W38, but composition and mechanism remain unresolved; lower intake and bodyweight remain observational variables rather than stand-alone progression or recovery-intervention triggers
- **Reserve/progression posture:** The W37 reserve observation remains preliminary because W38 did not include a second interpretable capacity probe; progression remains a question to test after ordinary post-travel operation is restored
- **Model-error posture:** Records 041–046 are closed/scored; record 043 remains closed as not supported (`overall_improvement_not_met`, error direction `over`)
- **Data-quality posture:** DQ-011 remains open for source verification of the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm; the earlier v1.31 HRV note/field differences remain source-role documented without inferred correction
- **Formal Phase 2D declaration:** None
- **August snapshot:** DEXA, VO₂, Bod Pod, TruAge/Advanced TruAge, and TruHealth source artifacts archived; Model Error 043 adjudication complete

The weekly operating posture describes the immediate observation condition for the active report. The broader Phase 2 substate remains the canonical phase-map interpretation. A successful post-travel return, repeated ease, or one reserve observation does not itself declare progression or a new phase.

Plain-language definitions for reserve, capacity versus exposure, weekly operating posture, B1, and Load Integration are maintained in [`docs/CONCEPTS.md`](docs/CONCEPTS.md).

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 38 Closeout

Observation window:

```text
2026-09-21 through 2026-09-27
```

Completed formal training:

- 6 B1 sessions / 330 minutes / 18.12 miles
- 5 Load Integration sessions / 226 minutes
- 556 total formal training minutes

Structured weekly metrics:

| Marker | W38 |
|---|---:|
| Morning bodyweight | 230.2 lb |
| Daily biomarker HRV | 67.1 ms |
| Resting heart rate | 44.9 bpm |
| Daily average heart rate | 60.4 bpm |
| Sleep HRV | 73.7 ms |
| Sleep average heart rate | 50.7 bpm |
| Total sleep | 7h29m |
| Deep sleep | approximately 1h16m |
| REM sleep | approximately 58m |

Five consecutive complete B1 + Load Integration days were performed from 2026-09-21 through 2026-09-25. B1 was then completed normally before departure on 2026-09-26; Load Integration that day and all structured training on 2026-09-27 were omitted for logistics/context rather than recovery.

The strongest W38 additions were:

- repeated low-overhead execution across five consecutive complete two-session days
- repeated subjective ease that did not trigger arbitrary volume or intensity escalation
- preservation of the Week 37 reserve observation as preliminary because no second interpretable capacity probe occurred
- a lower observed bodyweight range without a demonstrated functional penalty during the represented window
- preserved prescribed function after two shorter-sleep nights
- a bounded travel interruption that did not create make-up volume or training debt
- continued separation of measurement from command: neither favorable nor less-favorable short-window metrics independently changed the prescription

Week 38 is therefore best summarized as **governed consolidation under visible reserve and changing context**.

Full retrospective record: [`reports/2026-W38.md`](reports/2026-W38.md)

---

## Week 39 Operating Posture

Active window:

```text
2026-09-28 through 2026-10-04
```

Week 39 preserves the same B1 + Load Integration architecture and treats post-travel return as the immediate observation target.

Observe:

- whether the out-of-town interval ends without repayment behavior
- whether ordinary B1 + Load Integration operation returns without protective unloading or a visible reacquisition period
- whether the lower observed bodyweight state stabilizes, rebounds, or continues after home conditions normalize
- whether repeated Load Integration ease persists after travel
- whether an eventual reserve reassessment can be bounded and interpretable rather than becoming repeated informal testing
- sleep and autonomic variation alongside demonstrated next-day function

Do not:

- repay missed travel sessions
- treat the first home session as a required capacity test
- progress solely because W38 felt easy
- unload solely because travel occurred
- use favorable wearable values as automatic progression permission
- replace unresolved source values by inference
- reopen or rescore closed Model Error records
- declare Phase 2D from successful return or reserve evidence alone

Active report: [`reports/2026-W39.md`](reports/2026-W39.md)

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
- `Daniel_Dataset_v1.32` is registered in the private-source provenance manifest
- public daily biomarkers and canonical sleep contain 231 continuous rows through 2026-09-27
- public training contains 373 completed-session rows through 2026-09-26
- public context index contains 50 bounded events through 2026-09-27
- August TruDiagnostic provider artifacts remain registered in the August checksum manifest
- the August provider-header versus contemporaneous collection-record distinction remains preserved in [`data/source_provenance/2026-08-trudiagnostic-reconciliation.md`](data/source_provenance/2026-08-trudiagnostic-reconciliation.md)

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)  
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)  
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W39.md`](reports/2026-W39.md) — active week
- [`reports/2026-W38.md`](reports/2026-W38.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture is return before escalation: finish travel, restore ordinary operation without repayment behavior, and only then decide whether the reserve/progression question is ready for a controlled test.
