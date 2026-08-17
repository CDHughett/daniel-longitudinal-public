# Open Prediction Evaluation Plan — Record 046

**Registered:** 2026-08-17  
**Status:** Active prospective evaluation companion  
**Applies to:** Model-error record 046  
**Domain:** autonomic_unload_reload  
**Prediction type:** Secondary trajectory  
**Registered prediction:** `reconvergence_persists_after_unload_reload`

---

## Purpose

This document defines the prospective evaluation boundary for Model Error record 046.

Record 046 follows the completed scoring of record 045.

Record 045 established that the Week 31 autonomic-performance divergence partially reconverged during its fixed 2026-08-13 through 2026-08-16 scoring window.

Record 046 asks a different question:

> Does that autonomic reconvergence remain broadly preserved after a planned testing-related training withdrawal and after the standard B1 plus Load Integration architecture resumes?

The purpose of this plan is to prevent the subsequent unload/reload sequence from being interpreted retrospectively after its outcome is known.

This document defines:

- registration context
- admissible evidence
- descriptive unload and re-entry observations
- the primary scoring window
- fixed autonomic thresholds
- functional-preservation requirements
- reload requirements
- failure conditions
- insufficient-evidence handling
- VO₂-max perturbation handling
- missing-data handling
- relationships to records 041–045
- phase and protocol protections

This document supplements:

- [`prediction_evaluation.md`](./prediction_evaluation.md)
- [`open_prediction_evaluation_plan_041_044.md`](./open_prediction_evaluation_plan_041_044.md)
- [`open_prediction_evaluation_plan_045.md`](./open_prediction_evaluation_plan_045.md)
- [`2026-08-snapshot-collection-plan.md`](./2026-08-snapshot-collection-plan.md)
- [`../data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)

---

## Registration Context

Record 046 was registered on 2026-08-17.

The registration occurs after record 045 reached its fixed 2026-08-13 through 2026-08-16 scoring boundary.

Known at registration:

- Week 31 had produced a multi-marker autonomic-performance divergence
- record 045 had prospectively predicted partial autonomic reconvergence
- record 045 met all four registered autonomic thresholds across 2026-08-13 through 2026-08-16
- functional availability remained preserved during the record 045 scoring window
- no recovery-driven protocol reduction or intervention occurred during that scoring window
- the 2026-08-16 Load Integration session was withheld because DEXA and VO₂-max testing were scheduled for the following morning
- the 2026-08-16 omission was testing-directed rather than recovery-driven
- no B1 or Load Integration was planned for 2026-08-17
- no B1 or Load Integration was planned for 2026-08-18
- normal B1 plus Load Integration was planned to resume on 2026-08-19
- DEXA and VO₂-max testing were scheduled for 2026-08-17
- Bod Pod testing was scheduled for 2026-08-18

Because 2026-08-17 had already begun before this plan was registered, no 2026-08-17 observation may satisfy record 046.

The day remains registration context only.

The biological and performance outcomes of the August snapshot are not known to or governed by this prediction.

Record 046 does not predict:

- DEXA outcome
- VO₂-max value
- Bod Pod outcome
- TruDiagnostic outcome
- body-composition direction
- biological-age direction

Those outcomes remain independently governed.

---

## Prediction Boundary

The registered prediction is:

```text
The autonomic reconvergence supported in record 045 will remain broadly preserved
through the planned testing-related training withdrawal and after the normal
B1 plus Load Integration architecture resumes, rather than reverting to the
Week 31 compressed autonomic state.
```

The prediction concerns persistence after unloading and reload.

It does not predict that every individual autonomic value will remain favorable.

It does not require monotonic improvement.

It does not require the absence of a temporary post-testing disturbance.

It does require the favorable autonomic state to remain broadly present after normal training has resumed.

---

## Observation Structure

Record 046 separates the upcoming sequence into three evidence layers.

### Registration context

```text
2026-08-17
```

This date may be documented descriptively.

It cannot satisfy the prediction.

---

### Descriptive unload and re-entry kinetics

```text
2026-08-18
2026-08-19
```

These dates may describe:

- continued training withdrawal
- autonomic response to unloading
- possible delayed response to VO₂-max testing
- sleep response after the testing day
- return to standard B1
- return to standard Load Integration
- immediate reload response
- subjective restoration
- functional availability

These dates cannot satisfy the primary autonomic threshold test.

Their role is descriptive.

They establish how the system moves into the fixed reload scoring window.

---

### Primary scoring window

```text
2026-08-20 through 2026-08-23
```

Only these four dates may satisfy the primary quantitative autonomic condition for record 046.

The window is fixed at registration.

It must not be shifted because:

- the values are favorable
- the values are unfavorable
- an adjacent day would improve the result
- the VO₂-max response lasts longer than expected
- a later day produces a cleaner narrative
- the August biological snapshot appears concordant or discordant

---

## Intended Exposure Sequence

The known planned sequence at registration is:

```text
2026-08-16
B1 completed
Load Integration withheld before testing

2026-08-17
No B1
No Load Integration
DEXA and VO₂-max testing

2026-08-18
No B1
No Load Integration
Bod Pod testing

2026-08-19
Planned return to standard B1
Planned return to standard Load Integration

2026-08-20 through 2026-08-23
Standard B1 plus Load Integration architecture expected
Primary record 046 scoring window
```

Record 046 does not create this exposure sequence.

The test schedule and planned training interruption already existed before the prediction was registered.

The prediction observes the response to that sequence.

---

## Primary Autonomic Measures

Record 046 uses the same four autonomic measures used for record 045:

1. daily biomarker HRV
2. sleep HRV
3. resting heart rate
4. sleeping heart rate

These remain distinct measurement streams.

Do not substitute:

- daily HRV for sleep HRV
- sleep HRV for daily HRV
- resting heart rate for sleeping heart rate
- sleeping heart rate for resting heart rate

Each field must retain its source semantics.

---

## Fixed Favorable Thresholds

For direct comparability with record 045, record 046 preserves the same favorable thresholds:

| Marker | Favorable threshold |
|---|---:|
| Daily biomarker HRV | ≥59.7 ms |
| Sleep HRV | ≥65.3 ms |
| Resting heart rate | ≤49.2 bpm |
| Sleeping heart rate | ≤53.7 bpm |

These thresholds were inherited unchanged from the preregistered record 045 boundary.

They are not recalibrated from the favorable August 13–16 result.

They must not be modified after registration.

---

## Quantitative Aggregation Rule

For each autonomic marker:

1. use the source observations from 2026-08-20 through 2026-08-23
2. preserve the unrounded daily source values
3. calculate the arithmetic mean
4. compare the unrounded mean with the fixed favorable threshold
5. round only for reporting after the comparison

The calculation sequence is:

```text
source values
→ four-day arithmetic mean
→ fixed threshold comparison
→ reported rounding
```

Do not:

- average rounded weekly summaries
- substitute a neighboring date
- use August 18 or August 19 in the primary mean
- extend the window to obtain four favorable days
- remove an unfavorable valid observation
- combine daily and sleep metrics

---

## Support Rule

Record 046 is supported only when all three conditions are satisfied.

### Condition A — Autonomic persistence

At least:

```text
3 of 4
```

four-day autonomic means must remain on the favorable side of their registered thresholds during:

```text
2026-08-20 through 2026-08-23
```

---

### Condition B — Functional preservation after reload

No multi-session functional regression may occur after normal B1 plus Load Integration resumes.

Relevant regression may include a repeated pattern of:

- inability to complete prescribed B1
- inability to complete prescribed Load Integration
- materially elevated perceived effort across multiple sessions
- repeated loss of previously stable movement quality
- repeated loss of positional ownership
- repeated grip regression
- repeated abnormal cardiovascular behavior during B1
- repeated initiation resistance
- persistent pain affecting execution
- reduced ordinary-life availability clearly converging with the recovery signal

A single unusual session does not independently establish multi-session regression.

A transient test-related fatigue state does not independently establish failure.

---

### Condition C — Reload preserved

The standard B1 plus Load Integration architecture must actually resume.

The planned return date is:

```text
2026-08-19
```

If normal training resumes as planned and remains available through the scoring window, the reload condition is satisfied.

If normal training is reduced or withheld after 2026-08-19 because accumulated recovery status is judged insufficient, record 046 fails through recovery-driven protocol reduction.

If normal training does not resume because of a major unrelated external disruption, illness, injury, facility-access issue, or other event that prevents the intended reload test from occurring, use the insufficient-evidence rule rather than moving the scoring window.

---

## Failure Conditions

Record 046 fails if any of the following occurs.

### Persistent autonomic re-compression

Fewer than:

```text
3 of 4
```

registered autonomic thresholds are favorable across the fixed 2026-08-20 through 2026-08-23 four-day means.

This outcome indicates that the favorable autonomic state observed during record 045 did not remain broadly preserved after unloading and reload.

---

### Functional convergence

A multi-session functional regression occurs after normal training resumes.

This may indicate that the previously buffered functional layer has begun converging with the recovery signal.

---

### Recovery-driven reload reduction

Normal B1 plus Load Integration is reduced, cancelled, or meaningfully modified after the planned reload because recovery capacity is judged insufficient.

Examples include:

- recovery-driven B1 cancellation
- recovery-driven Load Integration cancellation
- emergency rest day
- meaningful reduction in load
- meaningful reduction in volume
- emergency deload
- recovery intervention replacing ordinary training

The reason for the change matters.

---

## VO₂-Max Perturbation Rule

The 2026-08-17 VO₂-max test is a known maximal physiological exposure.

A short-lived autonomic disturbance after that test is admissible and should be documented.

Possible observations include:

- temporarily lower HRV
- temporarily higher resting heart rate
- temporarily lower sleep HRV
- temporarily higher sleeping heart rate
- altered sleep continuity
- transient muscular fatigue

Such an acute response does not independently fail record 046.

This is one reason the primary scoring window does not begin immediately after the VO₂-max test.

The primary question is whether the favorable autonomic state remains broadly available after:

```text
testing
→ unloading
→ return to normal training
→ initial reload exposure
```

The actual measured VO₂-max result is inadmissible for scoring record 046.

Only the test's role as a known physiological exposure may be used as contextual evidence.

---

## Biological Snapshot Exclusion

The following outcomes cannot satisfy or fail record 046:

- TruDiagnostic results
- TruAge results
- TruHealth results
- DEXA body-composition results
- DEXA regional results
- VO₂-max measured value
- Bod Pod body-composition result
- later biological interpretation of the August snapshot

These results belong to separate biological and performance domains.

Record 046 concerns autonomic unload/reload persistence only.

A favorable August snapshot cannot convert an unfavorable 046 autonomic result into support.

An unfavorable August snapshot cannot convert a favorable 046 autonomic result into failure.

---

## Recovery-Driven Intervention Definition

For record 046, a recovery-driven intervention is an unplanned change introduced after the expected return to normal training because accumulated recovery status is judged insufficient for ordinary execution.

Examples include:

- unplanned rest day after reload
- recovery-driven B1 cancellation
- recovery-driven Load Integration cancellation
- meaningful training-volume reduction
- meaningful load reduction
- emergency deload
- added recovery protocol intended to reverse autonomic deterioration

The following do not automatically qualify:

- ordinary schedule displacement
- unrelated appointment conflict
- facility closure
- weather
- family responsibility
- unrelated travel
- unrelated illness
- unrelated acute injury
- administrative scheduling

The reason must be preserved contemporaneously.

---

## Reload-Date Deviation Rule

The planned normal-training return date is:

```text
2026-08-19
```

If normal B1 plus Load Integration does not resume on that date:

### Recovery-driven delay

If the delay occurs because recovery status is judged insufficient:

```text
record 046 fails
```

through the recovery-driven protocol-reduction criterion.

### Major unrelated disruption

If the delay occurs because of a major unrelated event that prevents the intended reload observation:

```text
insufficient_evidence
```

may be appropriate.

The primary scoring window must not simply be shifted forward to compensate.

### Ordinary minor schedule displacement

A minor schedule shift that does not materially change the intended reload exposure may remain admissible if:

- the reason is documented
- the installed workload is still completed
- the fixed August 20–23 scoring window remains interpretable

No decision should be made after viewing the scoring-window outcome.

---

## Insufficient-Evidence Rule

Record 046 should not be forced into support or failure if the intended comparison cannot be evaluated reliably.

Examples include:

- major acute illness
- unrelated injury materially affecting the scoring interval
- major external disruption
- device failure
- unrecoverable wearable-data loss
- inability to calculate the registered four-day means
- failure of the intended reload exposure for reasons unrelated to recovery
- material source ambiguity that cannot be reconciled

The appropriate outcome is:

```text
insufficient_evidence
```

Insufficient evidence is neither support nor failure.

The scoring window must not be moved merely to avoid insufficient evidence.

---

## Missing-Data Rule

The primary comparison requires four daily observations for each of the four autonomic markers.

If a source value is missing:

1. check the direct wearable display or provider source
2. check contemporaneous screenshots or exports
3. check the governed structured dataset
4. document any source-backed correction
5. do not interpolate
6. do not substitute another autonomic field
7. do not infer the value from neighboring dates

If missingness prevents reliable construction of the registered comparison, use the insufficient-evidence rule.

---

## Evidence Hierarchy

Preferred evidence order:

1. direct provider source artifact or wearable display
2. byte-preserved provider export
3. contemporaneous structured transcription
4. canonical governed dataset
5. contemporaneous training or daily-state observation
6. weekly report
7. retrospective synthesis

A later interpretation must not override contradictory lower-level source evidence.

Source-backed factual correction remains permitted.

Outcome-driven rewriting does not.

---

## Functional Evidence Sources

Functional evidence may be drawn from contemporaneous:

- B1 records
- Load Integration records
- training-block entries
- daily biomarker notes
- pain reports
- GI reports
- readiness reports
- ordinary-life observations
- session-completion evidence
- recovery-intervention records

Functional evidence is used for the functional-preservation and reload conditions.

It cannot substitute for the four autonomic calculations.

---

## Relationship to Record 041

Record 041 evaluates broader recovery capacity across the July–August observation block.

Record 046 evaluates a narrower unload/reload persistence question.

Possible outcomes remain independent.

Record 046 may provide candidate evidence relevant to record 041.

It does not:

- redefine record 041
- change the record 041 observation window
- change the record 041 support or failure criteria
- automatically close record 041

---

## Relationship to Record 042

Record 042 evaluates the ambient-execution plateau hypothesis.

Record 046 does not score:

- motor automaticity
- pull-up control
- grip expression
- divided attention
- positional control
- voluntary tempo control
- reduced operator overhead
- portability

Those observations may describe functional preservation during reload.

They cannot satisfy the autonomic threshold requirement.

Record 046 does not amend record 042.

---

## Relationship to Record 043

Record 043 evaluates biological translation into the August snapshot.

Record 046 excludes all August biological and performance outcomes from scoring.

The two records may later be interpreted together.

They remain independently evaluated.

A supported record 046 result cannot cause record 043 to pass.

A failed record 046 result cannot cause record 043 to fail.

---

## Relationship to Record 044

Record 044 evaluates protocol governance through the August snapshot cycle.

The testing-related training withdrawal is separately relevant to record 044 because:

- Load Integration was withheld on 2026-08-16
- no B1 or Load Integration was planned for 2026-08-17
- no B1 or Load Integration was planned for 2026-08-18
- normal training was planned to resume on 2026-08-19

Record 046 does not decide whether those choices satisfy record 044 governance.

It observes autonomic response to the documented exposure sequence.

Record 044 remains independently evaluated.

---

## Relationship to Record 045

Record 045 is closed.

Its fixed scoring window was:

```text
2026-08-13 through 2026-08-16
```

Its outcome is:

```text
supported
```

Record 046 does not:

- reopen record 045
- extend record 045
- rescore record 045
- alter the 045 thresholds
- incorporate August 17 or later evidence into 045
- reinterpret the August 16 result after later observations

Record 045 answered:

```text
Did partial autonomic reconvergence occur?
```

Record 046 asks:

```text
Does that reconvergence persist after unloading and reload?
```

The distinction must remain explicit.

---

## Protocol Boundary

Record 046 is observational.

It does not authorize a new physical protocol.

After the planned testing interruption, the intended baseline remains the previously installed:

```text
B1
+
Load Integration
```

architecture.

Do not change:

- B1 structure
- Load Integration structure
- training density
- exercise selection
- training volume
- nutrition
- hydration
- supplementation
- sleep opportunity
- recovery behavior

for the purpose of satisfying record 046.

Do not extend the deload merely to produce more favorable telemetry.

Do not increase workload merely to stress-test the reload.

Ordinary governance remains independently binding.

---

## Phase Boundary

Record 046 is not a phase-transition test.

A supported result does not declare:

```text
Phase 2D
```

A failed result does not terminate:

```text
Phase 2 — Load Integration
```

Current protected state remains:

```text
Phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
Undeclared

Phase 3:
Reserved and inactive
```

Any future phase declaration requires separate retrospective review under the applicable phase criteria.

---

## Threshold Immutability

The following thresholds are locked at registration:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

They must not be changed because:

- the unload response is larger than expected
- the unload response is smaller than expected
- the VO₂-max test produces an acute disturbance
- reload produces an unexpected value
- a later date would generate a pass
- a later date would generate a fail
- biological snapshot results appear favorable
- biological snapshot results appear unfavorable

The reuse of the record 045 thresholds is intentional.

It preserves direct comparability rather than recalibrating the test after observing the favorable 045 result.

---

## Scoring Procedure

After 2026-08-23 is complete:

1. preserve August 18 and August 19 as descriptive unload/re-entry observations
2. preserve the August 20–23 source values for each autonomic marker
3. reconcile any source discrepancy before interpretation
4. calculate each four-day arithmetic mean from unrounded source values
5. compare each mean with its fixed threshold
6. count favorable threshold crossings
7. confirm whether normal B1 plus Load Integration resumed
8. review the post-reload interval for multi-session functional regression
9. review the post-reload interval for recovery-driven protocol reduction
10. determine whether an insufficient-evidence condition applies
11. assign the record outcome
12. populate the Model Error register without modifying the original prediction
13. document broader calibration implications separately

No primary outcome should be entered before the fixed scoring window closes.

---

## Outcome Classes

Permitted outcome classifications are:

```text
supported
failed_autonomic_recompression
failed_functional_regression
failed_recovery_driven_reload_reduction
insufficient_evidence
```

If more than one failure condition occurs, document each mechanism while retaining a single failed record state.

---

## Interpretation Boundary

A supported result would indicate:

> The autonomic reconvergence observed under record 045 remained broadly preserved after the planned testing-related unloading interval and return to the standard training architecture.

A failed autonomic-recompression result would indicate:

> The favorable autonomic state did not remain broadly preserved after reload and returned toward a more compressed state faster than predicted.

A failed functional-regression result would indicate:

> Functional availability began deteriorating across multiple sessions after reload even if the autonomic threshold pattern remained mixed.

A failed recovery-driven reload-reduction result would indicate:

> The planned return to ordinary training could not be preserved because recovery status required workload reduction.

An insufficient-evidence result would indicate:

> The intended unload/reload comparison could not be evaluated reliably under the preregistered boundary.

None of these outcomes independently establishes:

- a medical diagnosis
- a causal physiological mechanism
- overtraining
- absence of accumulated training cost
- complete recovery
- permanent autonomic adaptation
- biological snapshot success
- Phase 2D
- completion of Phase 2

---

## Governance Statement

Record 046 exists because the close of record 045 leaves a new question unanswered.

The archive intentionally preserves:

```text
045:
partial autonomic reconvergence during a fixed pre-snapshot window
```

separately from:

```text
046:
persistence of that reconvergence after planned unloading and reload
```

The distinction prevents later testing and return-to-training observations from being appended retrospectively to a prediction whose scoring boundary has already closed.

Therefore:

- record 045 remains closed
- August 17 is registration context only
- August 18–19 are descriptive unload/re-entry observations
- August 20–23 are the fixed primary scoring window
- the four record 045 autonomic thresholds remain unchanged
- August biological outcomes remain excluded
- records 041–044 remain unchanged
- Phase 2 remains unchanged
- no new physical training protocol is created

The purpose of record 046 is calibration.

It should remain answerable by future evidence rather than by reinterpretation of evidence already observed at registration.
