# Open Prediction Evaluation Plan — Record 045

**Status:** Active preregistered evaluation plan  
**Record:** Model Error 045  
**Registration date:** 2026-08-12  
**Prediction type:** Secondary trajectory prediction  
**Domain:** Autonomic reconvergence  
**Model:** `gpt5.6-sol-subject-calibrated`  
**Scoring window:** 2026-08-13 through 2026-08-16  
**Outcome access at registration:** None for the scoring window

---

## Purpose

This document preregisters the evaluation rules for Model Error record 045 before its outcome window begins.

Record 045 tests whether the autonomic-performance divergence observed during 2026-W31 begins to reconverge during the final ordinary pre-snapshot interval.

The prediction is intentionally narrow.

It does not test:

- overall biological improvement
- August TruDiagnostic outcome
- DEXA outcome
- VO₂ max outcome
- Bod Pod outcome
- phase progression
- maximal performance
- grip development
- pull-up automaticity
- overall protocol success

Those questions remain governed by their existing evidence layers and, where applicable, Model Error records 041–044.

Record 045 tests one specific trajectory question:

> Does the autonomic layer partially recover toward its immediately preceding stronger state while functional availability remains preserved under the unchanged ordinary protocol?

---

## Registration Context

Record 045 was registered on:

```text
2026-08-12
```

The prediction was created after retrospective closeout of 2026-W31.

Week 31 showed a measurable divergence between autonomic telemetry and functional performance.

The relevant weekly reference values were:

| Marker | W30 | W31 |
|---|---:|---:|
| Daily biomarker HRV | 62.0 ms | 57.3 ms |
| Sleep HRV | 70.4 ms | 60.1 ms |
| Resting heart rate | 47.0 bpm | 51.4 bpm |
| Sleeping heart rate | 50.9 bpm | 56.4 bpm |

At the same time, W31 preserved:

- seven completed B1 sessions
- seven completed Load Integration sessions
- 700 formal training minutes
- stable subjective mood
- stable GI state
- absent pain
- preserved initiation
- preserved movement quality
- preserved same-day B1 and Load Integration compatibility
- repeated ambient or trait-like execution characteristics
- no recovery-driven protocol reduction
- no rescue intervention

This combination produced the motivating observation:

```text
autonomic compression
+
preserved functional expression
```

Week 31 is therefore **registration context**, not outcome evidence for record 045.

---

## Prospective Boundary

The scoring window is fixed as:

```text
2026-08-13 through 2026-08-16
```

The following observations are known at registration and are excluded from scoring:

```text
all observations through 2026-08-12
```

This explicitly includes:

```text
2026-W31
2026-08-10
2026-08-11
2026-08-12
```

Those observations may explain why the prediction was generated.

They cannot satisfy it.

The following are also excluded from record 045 scoring:

```text
2026-08-17 TruAge / TruHealth results
2026-08-17 DEXA results
2026-08-17 VO₂ max results
2026-08-18 Bod Pod results
any later August biological-snapshot result
```

Record 045 must be scored solely from its prospectively defined August 13–16 window.

---

## Registered Prediction

Prediction:

> The W31 autonomic-performance divergence will partially reconverge during the final ordinary pre-snapshot interval through improvement in the autonomic layer, without multi-session functional regression or a recovery-driven protocol change.

Registered prediction value:

```text
partial_reconvergence
```

This is a trajectory prediction rather than a point prediction.

---

## Reference-State Construction

W30 is used as the immediately preceding stronger autonomic reference.

W31 is used as the immediately preceding compressed autonomic state.

The registered definition of partial reconvergence is:

```text
recovery of at least one-half of the W31-to-W30 autonomic gap
```

No claim is made that W30 represents:

- an ideal physiological state
- a clinical optimum
- a long-term baseline
- a required return target
- complete recovery

It serves only as the fixed local comparison state for this prediction.

---

## Fixed Autonomic Thresholds

### Daily biomarker HRV

Reference values:

```text
W30 = 62.0 ms
W31 = 57.3 ms
```

Gap:

```text
62.0 - 57.3 = 4.7 ms
```

Half-gap:

```text
4.7 / 2 = 2.35 ms
```

Partial-reconvergence boundary:

```text
57.3 + 2.35 = 59.65 ms
```

Registered favorable threshold:

```text
Daily HRV >= 59.7 ms
```

---

### Sleep HRV

Reference values:

```text
W30 = 70.4 ms
W31 = 60.1 ms
```

Gap:

```text
70.4 - 60.1 = 10.3 ms
```

Half-gap:

```text
10.3 / 2 = 5.15 ms
```

Partial-reconvergence boundary:

```text
60.1 + 5.15 = 65.25 ms
```

Registered favorable threshold:

```text
Sleep HRV >= 65.3 ms
```

---

### Resting heart rate

Reference values:

```text
W30 = 47.0 bpm
W31 = 51.4 bpm
```

Gap:

```text
51.4 - 47.0 = 4.4 bpm
```

Half-gap:

```text
4.4 / 2 = 2.2 bpm
```

Partial-reconvergence boundary:

```text
51.4 - 2.2 = 49.2 bpm
```

Registered favorable threshold:

```text
Resting heart rate <= 49.2 bpm
```

---

### Sleeping heart rate

Reference values:

```text
W30 = 50.9 bpm
W31 = 56.4 bpm
```

Gap:

```text
56.4 - 50.9 = 5.5 bpm
```

Half-gap:

```text
5.5 / 2 = 2.75 bpm
```

Partial-reconvergence boundary:

```text
56.4 - 2.75 = 53.65 bpm
```

Registered favorable threshold:

```text
Sleeping heart rate <= 53.7 bpm
```

---

## Registered Threshold Table

| Marker | W30 reference | W31 reference | Favorable 045 threshold |
|---|---:|---:|---:|
| Daily biomarker HRV | 62.0 ms | 57.3 ms | ≥59.7 ms |
| Sleep HRV | 70.4 ms | 60.1 ms | ≥65.3 ms |
| Resting heart rate | 47.0 bpm | 51.4 bpm | ≤49.2 bpm |
| Sleeping heart rate | 50.9 bpm | 56.4 bpm | ≤53.7 bpm |

These thresholds are fixed at registration.

They must not be moved after outcome access in order to make the prediction easier or harder to satisfy.

---

## Aggregation Rule

Each autonomic marker will be evaluated using the arithmetic mean of its source values from:

```text
2026-08-13
2026-08-14
2026-08-15
2026-08-16
```

Calculation must use the original unrounded daily values where available.

The sequence is:

```text
source values
→ four-day arithmetic mean
→ threshold comparison
→ reported rounding
```

A displayed rounded intermediate value must not replace the underlying source values during calculation.

Daily biomarker HRV and sleep HRV remain separate metrics.

Resting heart rate and sleeping heart rate remain separate metrics.

Values must not be substituted across measurement domains.

---

## Primary Outcome Rule

Record 045 is **supported** only if all of the following conditions are met.

### Condition A — Autonomic reconvergence

At least:

```text
3 of 4
```

registered autonomic markers must cross their favorable preregistered threshold.

### Condition B — Functional preservation

No multi-session functional regression may occur during the scoring window.

### Condition C — Protocol preservation

No recovery-driven protocol reduction or recovery intervention may be required during the scoring window.

All three conditions are required.

---

## Support Rule

Record 045 is supported when:

```text
at least 3 of 4 autonomic thresholds are met

AND

no multi-session functional regression occurs

AND

no recovery-driven protocol reduction or intervention occurs
```

This outcome would support the model that the W31 divergence represented a state capable of at least partial spontaneous autonomic reconvergence while the installed functional system remained available.

It would not establish:

- complete recovery
- optimal recovery
- absence of accumulated cost
- permanent autonomic normalization
- Phase 2D
- superiority of the protocol
- biological improvement on the August snapshot

---

## Failure Rule A — Persistent Divergence

Record 045 fails through persistent autonomic-performance divergence when:

```text
fewer than 3 of 4 autonomic thresholds are met
```

while functional execution remains preserved and no recovery-driven protocol modification occurs.

Interpretation:

> The model underestimated the duration or persistence of autonomic compression despite continued functional availability.

This is a meaningful model error even if training performance remains strong.

Strong performance must not be used to convert persistent autonomic divergence into a pass.

---

## Failure Rule B — Functional Convergence in the Adverse Direction

Record 045 also fails if the autonomic-performance divergence resolves through deterioration of the functional layer rather than improvement of the autonomic layer.

Failure occurs if either of the following emerges during the scoring window:

```text
multi-session functional regression
```

or:

```text
recovery-driven protocol reduction or intervention
```

Interpretation:

> The model overestimated the persistence of functional decoupling from the accumulated recovery signal.

A legitimate governance decision to reduce workload may still be correct operationally.

That does not convert the prediction into a pass.

---

## Functional Regression Definition

A single weaker session is insufficient.

A single subjective complaint is insufficient.

A single low wearable value is insufficient.

A single disrupted night is insufficient.

For record 045, multi-session functional regression requires repeated evidence across more than one formal training exposure showing a meaningful loss of previously available execution.

Qualifying evidence may include repeated:

- inability to complete prescribed B1
- inability to complete prescribed Load Integration
- required workload reduction for recovery reasons
- clear technical deterioration
- abnormal initiation resistance
- unusual fatigue materially altering execution
- loss of ordinary same-day B1 and Load Integration compatibility
- recovery-driven session interruption

Minor ordinary variability does not qualify.

---

## Recovery-Driven Intervention Definition

For record 045, a recovery-driven intervention includes an unplanned change introduced because accumulated recovery status is judged insufficient for continued ordinary execution.

Examples include:

- unplanned rest day
- recovery-driven B1 cancellation
- recovery-driven Load Integration cancellation
- deliberate workload reduction
- meaningful load reduction
- meaningful volume reduction
- emergency deload
- added recovery protocol intended to reverse accumulating strain

The following do not automatically qualify:

- ordinary schedule displacement
- helping a family member
- travel logistics
- weather
- facility access
- unrelated appointment conflict
- voluntary recreational variation
- non-recovery administrative scheduling

The reason for the change matters.

---

## Insufficient-Evidence Rule

Record 045 should not be forced into a pass or fail when the intended comparison cannot be evaluated reliably.

Examples include:

- major acute illness
- unrelated injury materially affecting the window
- major external disruption
- device failure
- unrecoverable wearable-data loss
- insufficient observations to construct the registered four-day means
- material source ambiguity that cannot be reconciled before scoring

The appropriate outcome in such cases is:

```text
insufficient_evidence
```

Insufficient evidence is not equivalent to failure.

It is also not equivalent to support.

---

## Missing-Data Rule

The intended evaluation uses four complete daily observations for each of the four autonomic markers.

If a source value appears missing:

1. check the direct wearable source
2. check contemporaneous screenshots or exports
3. check the governed structured dataset
4. document any source-backed correction
5. do not interpolate
6. do not substitute another metric
7. do not infer the missing value from neighboring days

If missingness prevents reliable construction of the registered four-day comparison, use the insufficient-evidence rule.

---

## Evidence Hierarchy

Preferred evidence order:

1. direct provider source artifact or direct wearable display
2. byte-preserved provider export
3. contemporaneous structured transcription
4. canonical governed dataset
5. contemporaneous narrative observation
6. retrospective interpretation

Higher-level interpretation must not override contradictory lower-level source evidence.

Source-backed corrections remain permitted.

Outcome-driven rewriting does not.

---

## Functional Evidence Sources

Functional context may be drawn from contemporaneous:

- B1 records
- Load Integration records
- training-block records
- daily biomarker notes
- ordinary-life observations
- pain reports
- GI reports
- readiness reports
- session-completion evidence
- recovery-intervention records

Functional evidence is used only for Conditions B and C.

It cannot substitute for the four autonomic threshold calculations.

---

## Relationship to Record 041

Record 041 evaluates broader recovery capacity across the July–August observation block.

Record 045 evaluates a narrower prospective autonomic-reconvergence trajectory.

The records are independent.

Possible combinations include:

```text
045 pass / 041 pass
045 fail / 041 pass
045 pass / 041 fail
045 fail / 041 fail
```

For example, autonomic compression may remain persistent enough to fail record 045 while functional recovery capacity remains sufficiently preserved for record 041 to pass.

Record 045 does not amend or redefine record 041.

---

## Relationship to Record 042

Record 042 evaluates the ambient-execution plateau hypothesis.

Record 045 does not score:

- motor automaticity
- pull-up control
- grip expression
- divided attention
- voluntary tempo control
- positional control
- reduced operator overhead
- portability

Those observations may describe preserved function.

They cannot satisfy the autonomic-reconvergence threshold.

Record 045 does not amend or redefine record 042.

---

## Relationship to Record 043

Record 043 evaluates biological translation into the August snapshot.

Record 045 ends before the August biological and performance collection.

The following evidence is explicitly inadmissible for 045:

- TruDiagnostic outcome
- DEXA outcome
- VO₂ max outcome
- Bod Pod outcome
- post-collection biological interpretation

A pass or failure of record 045 has no automatic consequence for record 043.

Record 045 does not amend or redefine record 043.

---

## Relationship to Record 044

Record 044 evaluates protocol-governance preservation.

Record 045 does not authorize:

- workload increase
- workload reduction
- tapering
- deliberate rest
- specialized recovery work
- snapshot preparation
- grip intervention
- added conditioning
- training progression

If ordinary governance independently requires a recovery intervention, that action should be taken and documented according to its own evidence.

Such an intervention may cause record 045 to fail while record 044 remains supported because appropriate governance was preserved.

Record 045 does not amend or redefine record 044.

---

## Protocol Boundary

Record 045 is observational.

It creates no treatment instruction.

The installed physical protocol remains unchanged.

Do not modify:

- B1
- Load Integration
- training density
- exercise selection
- nutrition
- hydration
- supplementation
- sleep opportunity
- recovery behavior
- recreational activity

for the purpose of satisfying record 045.

Do not reduce ordinary work to manufacture autonomic rebound.

Do not increase ordinary work to stress-test the prediction.

The scoring window should remain representative of ordinary pre-snapshot operation.

---

## August Snapshot Boundary

The August collection remains separately governed by:

[`2026-08-snapshot-collection-plan.md`](2026-08-snapshot-collection-plan.md)

and records 041–044 remain governed by:

[`open_prediction_evaluation_plan_041_044.md`](open_prediction_evaluation_plan_041_044.md)

Record 045 does not modify either document.

The snapshot remains scheduled separately from this prediction.

The outcome of 045 cannot:

- change collection conditions
- change the May comparison baseline
- modify Model Error 043 scoring
- alter snapshot evidence hierarchy
- authorize peaking
- authorize tapering
- create a release automatically

---

## Phase Boundary

Record 045 is not a phase-transition test.

A supported result does not declare:

```text
Phase 2D
```

A failed result does not terminate:

```text
Phase 2 — Load Integration
```

Current state remains:

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

Any future phase declaration requires separate retrospective review using the applicable declaration criteria.

---

## Threshold Immutability

The following values are locked at registration:

```text
Daily HRV >= 59.7 ms
Sleep HRV >= 65.3 ms
Resting HR <= 49.2 bpm
Sleeping HR <= 53.7 bpm
```

They must not be altered after outcome access because:

- the result is unexpectedly favorable
- the result is unexpectedly unfavorable
- another threshold would produce a cleaner narrative
- later biological results appear concordant or discordant
- functional performance remains unusually strong
- the August snapshot changes interpretation

A true source error discovered in the underlying historical reference values must be documented explicitly.

It must not silently move the registered threshold after outcome access.

---

## Scoring Procedure

After the 2026-08-16 observation period is complete:

1. preserve the four daily source values for each autonomic marker
2. reconcile any source discrepancy before interpretation
3. calculate each four-day arithmetic mean from unrounded source values
4. compare each result with its fixed registered threshold
5. count the number of favorable threshold crossings
6. review the scoring window for multi-session functional regression
7. review the scoring window for recovery-driven protocol intervention
8. evaluate whether an insufficient-evidence condition applies
9. assign the record outcome
10. populate the Model Error register without modifying the original prediction
11. document any calibration implication separately

No outcome should be entered before the scoring window closes.

---

## Outcome Classes

Permitted outcome classifications:

```text
supported
failed_persistent_divergence
failed_functional_regression
insufficient_evidence
```

If both autonomic and functional failure criteria occur, document both mechanisms while retaining a single failed record status.

---

## Interpretation Boundary

A supported record would indicate:

> Partial short-window autonomic reconvergence occurred under continued ordinary execution.

A failed persistent-divergence record would indicate:

> Autonomic compression persisted longer than the model predicted despite preserved functional expression.

A failed functional-regression record would indicate:

> Functional availability began converging with the accumulated recovery signal before the model expected.

An insufficient-evidence result would indicate:

> The preregistered question could not be evaluated reliably from the available evidence.

None of those outcomes independently establishes a medical diagnosis, physiological mechanism, phase transition, or causal effect of the protocol.

---

## Governance Statement

Record 045 was created prospectively after W31 produced a meaningful unresolved observation.

The archive intentionally preserves the distinction between:

```text
observation that generated the question
```

and:

```text
future evidence permitted to answer the question
```

Therefore:

- W31 remains retrospective evidence
- August 10–12 remain known registration context
- August 13–16 form the prospective scoring window
- August 17–18 snapshot outcomes remain excluded
- records 041–044 remain unchanged
- protocol behavior remains ordinary
- no outcome-dependent threshold movement is permitted

This boundary is the primary methodological purpose of the record.

---

## Registration State

At registration:

```text
Record:
045

Date:
2026-08-12

Domain:
autonomic_reconvergence

Prediction:
partial_reconvergence

Prediction type:
trajectory

Calibration state:
pre

Flag:
secondary

Status:
open

Scoring window:
2026-08-13 through 2026-08-16

Actual value:
blank

Error fields:
blank

Outcome:
unknown
```

The prediction is now fixed before its admissible outcome window begins.
