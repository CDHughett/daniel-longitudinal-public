# Open Prediction Evaluation Plan — Records 041–044

**Registered:** 2026-07-11  
**Status:** Active prospective evaluation companion  
**Applies to:** Model-error records 041, 042, 043, and 044

---

## Purpose

This document defines the evaluation boundaries for the open July–August 2026 prediction block before the relevant observation windows have closed and before the August biological results are known.

Its purpose is to reduce post-outcome discretion by defining:

- observation-window boundaries
- admissible evidence
- interruption handling
- operational definitions
- support and failure conditions
- missing-data treatment
- closure procedures

This document supplements:

- [`prediction_evaluation.md`](./prediction_evaluation.md)
- [`../docs/methodology/prediction_to_outcome_pipeline.md`](../docs/methodology/prediction_to_outcome_pipeline.md)
- [`../docs/methodology/valid_prediction_criteria.md`](../docs/methodology/valid_prediction_criteria.md)
- [`../data/model_error/model_error_gap_v1.csv`](../data/model_error/model_error_gap_v1.csv)

---

## Registration Context

This plan was registered on 2026-07-11 after limited early-window evidence had already been observed.

Known at registration:

- the Washington travel perturbation had occurred
- formal training had paused during the travel interval
- standard home execution had resumed after travel
- the 2026-07-10 instructional pull-up event had occurred
- that event had been identified as candidate evidence relevant to record 042
- records 041–044 remained open and unscored

Not known at registration:

- the final July–August recovery trajectory
- whether the instructional pull-up characteristics would recur
- whether record 042 would meet its repeated-evidence threshold
- the August TruDiagnostic results
- the August DEXA, VO₂, or BodPod results
- the final outcomes of records 041–044
- whether Phase 2D criteria would later be satisfied

The plan is therefore:

- prospective relative to the unresolved prediction outcomes
- prospective relative to all August biological results
- partially informed by limited early-window contextual evidence

The known 2026-07-10 candidate event did not itself satisfy the record 042 transition threshold because the threshold requires repeated evidence across multiple dates and contexts.

The known Washington perturbation did not determine the outcome of record 041 because the primary standard-input interval had only recently begun and the later accumulated-exposure trajectory remained unresolved.

This disclosure does not modify any prediction or scoring threshold.

---

## Non-Retroactivity Rule

This document does not modify:

- prediction wording
- prediction values
- prediction dates
- prediction types
- prediction status
- model versions
- calibration states
- flags
- previously recorded evidence

Records 041–044 remain unchanged and open.

This plan defines how existing prediction language will be interpreted at closure. It must not be revised in response to favorable or unfavorable outcomes unless a genuine methodological defect is discovered.

Any later change to this plan must:

- be committed before the relevant result is known
- state the exact reason for revision
- preserve the prior version through Git history
- avoid changing rules merely because emerging evidence favors one outcome

Clarification of collection dates, source availability, or test completion does not authorize changing the existing evaluation thresholds.

---

## Common Evaluation Boundary

The August artifact cycle may include measurements collected on more than one date.

This plan therefore distinguishes:

1. the **primary biological endpoint**
2. the **supplemental measurement window**
3. the **snapshot-cycle completion date**

---

### Primary Biological Endpoint

The primary biological endpoint is the August 2026 TruDiagnostic sample-collection date intended as the direct follow-up to the May 2026 TruDiagnostic measurement cycle.

Planned collection date:

- 2026-08-17

If the collection date changes:

- the actual collection date must be documented
- the reason for rescheduling must be recorded
- the new date must not be selected after viewing results
- the later date must not be substituted silently for the planned outcome

The primary biological endpoint controls:

- the core record 043 epigenetic comparison
- the endpoint for the biological observation interval
- the date against which preparation and collection conditions are documented

The observation endpoint is the sample-collection date, not the date on which the laboratory report is received.

---

### Supplemental Measurement Window

The planned supplemental measurement window is:

- 2026-08-17 through 2026-08-18

Planned supplemental tests include:

- DEXA
- formal VO₂ testing
- BodPod
- associated body-composition or performance outputs

These measurements may be collected on different dates from the primary biological endpoint.

Supplemental measurements:

- provide contextual evidence for the August physiological profile
- must retain their actual collection dates
- must retain their preparation and testing conditions
- must not silently replace the primary TruDiagnostic comparison
- must not alter the predefined core biological-anchor rules
- must be interpreted separately when methodology or collection conditions differ

If a supplemental test is delayed beyond the planned window:

- the actual date must be documented
- the delayed test must not be silently represented as contemporaneous
- comparability must be reviewed before inclusion
- the result may remain supplemental even if it is excluded from the tightly bounded August snapshot cycle

---

### Snapshot-Cycle Completion Date

The snapshot-cycle completion date is the latest completed planned test date within the documented August supplemental measurement window.

Under the current plan, the expected snapshot-cycle completion date is:

- 2026-08-18

If one or more planned supplemental tests are not completed:

- the last completed planned test date becomes the provisional cycle-completion date
- the missing test must be documented
- no uncompleted test may be treated as favorable, adverse, or stable
- the absence of a supplemental test does not automatically invalidate the core TruDiagnostic comparison

Records 041, 042, and 044 use the snapshot-cycle completion date as their normal observation-window endpoint.

Record 043 uses the primary biological endpoint for its core biological anchors and the supplemental window for contextual profile evidence.

---

### Result Review Boundary

Results may be evaluated only after:

- the relevant reports are received
- source artifacts are archived
- collection dates are verified
- preparation and testing conditions are documented
- measurement comparability is reviewed
- required structured values are entered
- transcription is checked
- artifact verification is complete

No result should be scored from a screenshot preview, partial portal display, verbal summary, or incomplete report set when the missing information could affect interpretation.

---

### Failure to Complete the August Cycle

If the intended primary biological collection is not completed by 2026-08-31:

- no record automatically rolls into a later testing cycle
- records dependent on the biological snapshot remain open if evidence is insufficient
- the missed or delayed outcome must be documented
- a later test must not be substituted silently for the August outcome

If the primary biological endpoint occurs but one or more supplemental tests do not occur:

- record 043 may still be evaluable from the core anchors if comparability requirements are met
- missing supplemental domains must remain visibly missing
- records 041, 042, and 044 may close at the documented cycle-completion date when sufficient evidence exists
- the absence of a supplemental test must not be converted into a favorable or unfavorable outcome

For records 041, 042, and 044, 2026-08-31 is the maximum observation boundary if the planned snapshot cycle is not completed earlier.

---

## Evidence Hierarchy

Closure should prioritize evidence in the following order:

1. **Primary source artifacts**
   - laboratory reports
   - wearable exports
   - verified testing artifacts
   - structured datasets derived directly from source material

2. **Contemporaneous collection records**
   - daily biomarker entries
   - training-session notes
   - dated collection notes
   - perturbation records

3. **Weekly reports**
   - contemporaneous weekly observations
   - weekly closeout synthesis
   - explicitly labeled candidate evidence

4. **Later retrospective synthesis**
   - admissible only when grounded in preserved contemporaneous evidence
   - insufficient by itself to establish a new event or transition

Unrecorded memory should not be used to close a prediction.

A later summary may organize existing evidence but may not create evidence that was not contemporaneously preserved.

---

## General Closure Rules

Each record must be evaluated independently.

Evidence supporting one record does not automatically determine another.

A record may close only when:

- its observation window has elapsed
- sufficient evidence is available
- the prediction can be resolved without forced interpretation
- known confounders are documented
- the original prediction remains unchanged

If evidence remains materially incomplete or noncomparable:

- the record remains open
- the reason must be documented
- no favorable or unfavorable outcome should be inferred

A single unusual day should not resolve a trajectory prediction unless the original prediction explicitly concerns a single event.

---

# Record 041 — Recovery Capacity

## Original Domain

`recovery_capacity`

## Prediction Class

Trajectory

## Evaluation Question

Did accumulated B1 and Load Integration exposure remain compatible with recovery through the July–August observation block without requiring an unplanned recovery intervention, producing multi-session training regression, or causing persistent physiological suppression under otherwise stable inputs?

---

## Observation Window

### Calendar Observation Window

2026-07-01 through:

- the August snapshot-cycle completion date, or
- 2026-08-31 if the snapshot cycle is not completed earlier

### Primary Standard-Input Interval

2026-07-08 through the observation-window endpoint.

This interval begins with documented return to normal home execution after the pre-existing Washington travel block.

### Treatment of 2026-07-01 Through 2026-07-07

The Washington travel period remains part of the calendar record and may provide perturbation and recovery evidence.

It is not treated as a standard-input accumulated-training interval because it included:

- travel
- environmental disruption
- loss of normal training access
- formal training pause
- altered scale access
- altered schedule and intake context

The travel period cannot be used to manufacture a pass or failure.

Its effects remain relevant if they produce persistent suppression or functional regression after standard execution resumes.

---

## Operational Definitions

### Unplanned Recovery Intervention

An unplanned recovery intervention is a deliberate reduction, suspension, or modification of the normal protocol because accumulated physiological or mechanical strain is judged incompatible with continued standard execution.

Examples include:

- recovery-driven deload
- recovery-driven suspension of B1
- recovery-driven suspension of Load Integration
- material volume reduction caused by systemic suppression
- added rest days introduced because normal execution is no longer recovery-compatible
- protocol repair introduced to reverse an accumulating adverse trend

The following do not automatically qualify:

- missed training caused by travel or equipment inaccessibility
- ordinary schedule conflicts
- routine mobility
- ordinary hydration or nutrition
- normal sleep prioritization
- isolated technique refinement
- optional recreational movement
- a single conservative session adjustment without evidence of accumulating suppression

### Multi-Session Training Regression

Multi-session training regression requires:

- reduced ability to execute the established protocol across at least two consecutive planned exposures
- a decline attributable to physiological or mechanical limitation rather than external access or scheduling
- observable loss of previously established movement quality, tolerance, or completion capacity

An isolated poor session is insufficient.

### Persistent Physiological Suppression

Persistent physiological suppression requires a cluster lasting at least three consecutive days and must include:

1. recovery telemetry materially worse than the preceding 28-day personal distribution
2. at least one corroborating functional or subjective signal

Qualifying telemetry may include:

- HRV at or below the preceding 28-day 25th percentile
- sleep HR at or above the preceding 28-day 75th percentile
- repeated recovery-score suppression
- sustained deterioration in sleep continuity

Corroborating signals may include:

- unusual fatigue
- persistent pain
- loss of normal B1 compatibility
- loss of normal Load Integration compatibility
- meaningful mood or cognitive disruption
- persistent GI or systemic disturbance

Wearable deviation without functional corroboration is insufficient by itself.

---

## Support Condition

Record 041 is supported if the observation window closes with:

- no unplanned recovery intervention
- no multi-session training regression
- no persistent physiological suppression under otherwise stable inputs
- continued ability to sustain the established B1 and Load Integration architecture

Normal variability, isolated low-readiness days, externally constrained missed sessions, and transient perturbation responses do not invalidate the prediction when recovery compatibility remains preserved.

---

## Failure Condition

Record 041 is not supported if any of the following occurs under otherwise stable inputs:

- accumulated exposure requires an unplanned recovery intervention
- established training capacity regresses across multiple consecutive planned exposures
- persistent physiological suppression develops
- normal protocol execution must be materially reduced because recovery reserve is insufficient

A recovery intervention may be correctly governed and still constitute failure of record 041.

Record 041 evaluates recovery capacity, not whether the response to impaired recovery was responsible.

---

## Insufficient-Evidence Condition

Record 041 remains open if:

- a major illness, injury, or external disruption occupies a substantial portion of the window
- wearable and functional evidence are unavailable
- standard B1 and Load Integration exposure is absent for reasons unrelated to recovery
- the window does not contain enough accumulated exposure to test the prediction fairly

---

# Record 042 — Ambient-Execution Plateau

## Original Domain

`ambient_execution`

## Prediction Class

Trajectory

## Evaluation Question

Did execution quality remain stable without another distinct qualitative transition toward greater automaticity, or did spontaneous evidence demonstrate continued nervous-system adaptation beyond the predicted plateau?

---

## Observation Window

2026-06-25 through:

- the August snapshot-cycle completion date, or
- 2026-08-31 if the snapshot cycle is not completed earlier

Evidence recorded before the creation of this companion plan remains admissible only when it was contemporaneously documented.

The 2026-07-10 instructional pull-up event was known at registration and remains one candidate observation rather than a completed transition.

---

## Stable Execution

Stable execution includes:

- preserved movement quality
- preserved protocol completion
- ordinary reduction in effort through familiarity
- routine session-to-session ease
- isolated low-salience performance
- continued ambient initiation without a new class of behavior

Stable execution supports the plateau prediction.

Simple repetition, improved comfort, or a single smooth session is not automatically a distinct qualitative transition.

---

## Distinct Qualitative Transition

A distinct transition toward greater automaticity requires repeated evidence rather than one isolated observation.

The threshold requires all of the following:

1. at least three separately dated observations
2. evidence spanning at least 14 calendar days
3. expression in at least two contexts, movements, or environmental conditions
4. no substantive protocol progression that plausibly explains the change
5. at least two of the following characteristics:
   - meaningful reduction in conscious setup or cueing
   - preserved execution during divided attention
   - preserved execution while speaking or instructing
   - spontaneous positional control under social or environmental load
   - skill portability beyond the usual isolated setting
   - automatic correction without deliberate troubleshooting
   - preservation of quality during an unplanned contextual demand
   - execution that reflects a new operating mode rather than ordinary familiarity

A single event may be recorded as candidate evidence but cannot resolve the prediction.

---

## Support Condition

Record 042 is supported if:

- execution remains stable through the observation window
- no distinct qualitative transition meets the repeated-evidence threshold
- apparent improvements remain within the existing class of ambient execution

This outcome indicates that the modeled plateau was approximately correct for the current protocol and window.

---

## Failure Condition — Continued Adaptation

Record 042 is not supported if the distinct-transition threshold is met.

This would indicate that the model underestimated continued adaptation beyond the predicted ambient-execution ceiling.

The prediction should not be rescued by relabeling the new behavior as ordinary stability after the threshold has been met.

---

## Failure Condition — Degradation

Record 042 is also not supported if execution materially degrades rather than remaining stable.

Degradation requires more than isolated variability and should include repeated loss of previously established execution quality.

This represents a different error from continued adaptation and must be described separately at closure.

---

## Insufficient-Evidence Condition

Record 042 remains open if:

- there are too few relevant exposures
- candidate observations are not contemporaneously documented
- a substantive protocol change prevents comparison
- environmental disruption prevents fair observation across the window

---

# Record 043 — August Biological Translation

## Original Domain

`biological_translation`

## Prediction Class

Trajectory

## Evaluation Question

Does the August 2026 biological snapshot show measurable overall improvement relative to May 2026, with improvement smaller than the February-to-May interval?

---

## Observation Endpoint

The core record 043 comparison is anchored to the primary biological endpoint:

- the August 2026 TruDiagnostic sample-collection date
- currently planned for 2026-08-17

Supplemental DEXA, VO₂, BodPod, bodyweight, and recovery evidence may be collected during the documented supplemental measurement window.

Supplemental evidence does not change the collection date of the primary biological endpoint.

---

## Comparison Artifacts

### February Baseline

Primary structured baseline:

- `data/biomarker_snapshot.csv`
- row identified as `2026-02`

Supporting artifacts:

- `snapshots/2026-02/`

### May Comparison Point

Primary structured comparison:

- `data/biomarker_snapshot.csv`
- row identified as `2026-05`

Supporting artifacts:

- `snapshots/2026-05/`

### August Outcome

The August result must be based on:

- the verified August TruDiagnostic source reports
- the documented primary biological sample date
- the August snapshot directory
- the corresponding structured-data entry
- directly comparable outputs from the same testing family

Raw source artifacts control when a structured value conflicts with a source report.

Supplemental measurements must retain their separate collection dates and methodologies.

---

## Core Biological Anchors

The primary evaluation set is:

1. `omicm_age_delta_years`
2. `dunedin_pace`
3. `symphony_age`

Direction of improvement:

- `omicm_age_delta_years` — more negative is favorable
- `dunedin_pace` — lower is favorable
- `symphony_age` — lower is favorable

Operational minimum changes:

- OMICm age delta: at least 0.5 years more favorable
- DunedinPACE: at least 0.01 lower
- SymphonyAge: at least 1.0 year lower

Changes smaller than these thresholds are classified as stable for this evaluation.

These are archive-level operational thresholds. They are not claims about formal clinical significance or assay precision.

---

## Supporting Profile Domains

When directly comparable August values are available, the supporting profile includes:

### System and Organ Ages

- blood age
- brain age
- inflammation age
- heart age
- hormone age
- immune age
- kidney age
- liver age
- metabolic age
- lung age
- musculoskeletal age

Operational classification:

- improvement: decrease of at least 1.0 year
- stable: change smaller than 1.0 year in either direction
- adverse: increase of at least 1.0 year

### TruHealth Domain Scores

When the same score is present in February, May, and August:

- improvement: increase of at least 5 points
- stable: change smaller than 5 points in either direction
- adverse: decrease of at least 5 points

The supporting profile may strengthen or weaken the overall interpretation but may not replace the core biological anchors.

---

## Supplemental Domains

The following may be reported as supporting context when collected comparably within the documented supplemental measurement window:

- DEXA body composition
- BodPod body composition
- VO₂ or COSMED outputs
- bodyweight
- daily biomarker HRV
- sleep HRV
- sleep HR
- recovery telemetry

Supplemental domains cannot rescue failure of the core biological-aging comparison.

They should be interpreted separately when:

- collection dates differ
- devices differ
- preparation conditions differ
- methodologies differ
- comparison artifacts are unavailable
- the test occurs outside the planned supplemental window

A favorable supplemental test must not be used to relabel a non-improving core epigenetic profile as support for record 043.

A discordant supplemental result must still be reported even when the core anchors support the prediction.

---

## Overall Improvement Rule

The August profile qualifies as measurable overall improvement only if all of the following are true:

1. at least two of the three core biological anchors improve beyond their operational thresholds
2. any remaining core anchor is stable or improved
3. at least 60% of directly comparable supporting metrics are stable or improved
4. neither the system-age group nor the TruHealth group shows a majority of materially adverse changes
5. no source-quality or comparability issue invalidates the primary comparison

One adverse secondary domain does not automatically invalidate the overall profile.

A broad adverse cluster cannot be ignored because several selected values improved.

Supplemental DEXA, BodPod, and VO₂ outcomes provide context but are not included in the percentage rule unless explicitly represented in a later separately defined analysis layer.

---

## Magnitude Comparison

The February-to-May interval is the reference improvement interval.

For each comparable core anchor:

`August improvement ratio = absolute favorable May-to-August change ÷ absolute favorable February-to-May change`

Reference February-to-May changes:

- OMICm age delta: 2.6 years more favorable
- DunedinPACE: 0.09 lower
- SymphonyAge: 13.4 years lower

The median ratio across at least two comparable core anchors determines the magnitude class.

### Smaller Improvement

`0 < median ratio < 1.0`

### Equal or Greater Improvement

`median ratio >= 1.0`

### No Improvement

`median ratio <= 0`

A ratio is calculated only when the August change is directionally interpretable and the February-to-May reference is available.

---

## Support Condition

Record 043 is supported if:

- the overall-improvement rule is met
- the median improvement ratio is greater than 0
- the median improvement ratio is less than 1.0

This corresponds to measurable improvement that is smaller than the February-to-May interval.

---

## Failure Condition — Model Underestimation

Record 043 is not supported through underestimation if:

- the overall-improvement rule is met
- the median core-anchor improvement ratio is at least 1.0

This means improvement was equal to or greater than the February-to-May interval.

---

## Failure Condition — Model Overestimation

Record 043 is not supported through overestimation if:

- the overall-improvement rule is not met
- the core profile remains effectively flat
- the profile materially worsens
- improvement is too narrow to qualify as an overall physiological improvement

A favorable isolated marker is insufficient if the broader predefined rule is not met.

---

## Comparability Requirements

Before evaluation, confirm:

- the same testing provider or directly comparable assay family
- matching metric definitions
- no silent unit changes
- no known algorithm change that invalidates comparison
- primary biological collection-date documentation
- supplemental test-date documentation
- collection-condition documentation
- source-artifact availability
- structured transcription verification
- separation of core and supplemental outcome classes

If fewer than two core anchors are directly comparable, record 043 cannot be closed as supported or unsupported.

It remains open pending an explicit audit decision regarding non-evaluability.

---

# Record 044 — Protocol Governance

## Original Domain

`protocol_governance`

## Prediction Class

State

## Evaluation Question

Was protocol governance preserved through the August snapshot cycle without substantive progression, volume expansion, or protocol modification lacking predefined objective support?

---

## Observation Window

2026-06-25 through:

- the August snapshot-cycle completion date, or
- 2026-08-31 if the snapshot cycle is not completed earlier

The observation window includes preparation behavior through the final planned supplemental test because snapshot-directed protocol manipulation may occur before any component of the cycle.

---

## Substantive Protocol Change

A substantive change includes a planned recurring alteration to:

- training load
- training volume
- training density
- training frequency
- aerobic duration or intensity
- recurring movement selection
- nutrition architecture
- fasting structure
- supplementation architecture
- recovery intervention structure
- testing-preparation behavior
- any protocol element intended to materially alter adaptation

The following do not automatically qualify:

- isolated accidental duration variation
- normal movement-quality refinement
- ordinary warm-up or mobility selection
- technique correction
- externally constrained missed sessions
- household or recreational activity
- repository cleanup
- measurement documentation
- artifact correction
- one-time schedule adjustment
- conservative response to an acute safety issue

---

## Predefined Governance Criteria

A substantive progression or modification is governed only if all of the following are present before implementation:

1. **Repeated evidence**
   - the relevant signal appears across at least three exposures or seven calendar days

2. **Independent corroboration**
   - evidence appears in at least two layers, such as:
     - performance
     - recovery telemetry
     - subjective function
     - biological measurement
     - repeated mechanical observation

3. **Recovery compatibility**
   - no unresolved suppression, active injury signal, or multi-day recovery instability is present

4. **Documented rationale**
   - the reason, scope, and intended effect are recorded before the change

5. **Bounded implementation**
   - the change is limited, observable, and capable of reversal

6. **No proof-seeking motive**
   - the change is not introduced to force a prediction outcome, phase declaration, visual result, or snapshot result

A biological snapshot may justify later protocol reconsideration only after the result is received, archived, and interpreted.

It cannot justify a pre-snapshot change retroactively.

---

## Support Condition

Record 044 is supported if:

- no substantive protocol change occurs
- or any substantive change is supported by all predefined governance criteria before implementation
- no progression is introduced primarily to force proof
- no snapshot manipulation is introduced
- repository work remains separate from biological protocol modification

---

## Failure Condition

Record 044 is not supported if:

- substantive training progression occurs without the predefined evidence threshold
- volume or density is expanded because execution feels easy
- a new intervention is introduced to accelerate or force the August result
- protocol changes are justified only after implementation
- governance language is used to rationalize an already desired escalation
- snapshot conditions are intentionally manipulated to improve presentation

Governance failure does not require biological harm.

The record evaluates decision discipline rather than whether an unauthorized change happened to produce a favorable outcome.

---

## Relationship to Record 041

Records 041 and 044 are independent.

Examples:

- recovery may deteriorate, causing record 041 to fail, while a properly governed recovery response allows record 044 to pass
- recovery may remain stable, allowing record 041 to pass, while an unjustified progression causes record 044 to fail
- both may pass
- both may fail

One outcome must not be used to rescue the other.

---

# Closure Procedure

When the observation windows end:

1. confirm the primary biological endpoint date
2. confirm the supplemental measurement dates
3. confirm the applicable snapshot-cycle completion date
4. identify all admissible contemporaneous evidence
5. verify source and structured-data consistency
6. document material confounders
7. document missing or delayed tests
8. evaluate each record independently against this plan
9. prepare a traceable evidence summary
10. update the model-error CSV only after evaluation is complete
11. preserve the original prediction fields unchanged
12. document the closure in the changelog and relevant report
13. calculate or update UDI only for eligible evaluable records

The following fields must not be rewritten at closure:

- `record_id`
- `date`
- `domain`
- `model_version`
- `prediction_value`
- `model_type`
- `calibration_state`
- `flag`
- `prediction_type`
- original prediction text contained in `notes`

Closure may populate:

- `actual_value`
- `error_absolute`
- `error_direction`
- `error_pct`
- `status`
- an appended closure note

---

## Phase Boundary

Closure of records 041–044 does not independently declare Phase 2D.

Any later phase declaration requires the separate criteria defined in:

- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)

Prediction outcomes may contribute evidence toward a phase decision, but they cannot substitute for:

- repeatability
- snapshot evidence
- structural confirmation
- risk review
- retrospective phase closeout

---

## Version Note

This plan was registered on 2026-07-11 while records 041–044 remained open and before the August 2026 biological results were known.

At registration:

- the Washington travel perturbation was already known
- the 2026-07-10 instructional pull-up was already known as one candidate observation
- the August biological and performance outcomes remained unknown
- the final trajectories of records 041–044 remained unresolved

This revision documents registration context and clarifies the multi-date August collection boundary.

It does not change:

- any original prediction
- any scoring threshold
- any support or failure rule
- any existing outcome field
- the open status of records 041–044

Its role is to constrain later interpretation, not to predict additional outcomes.
