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

---

## Common Evaluation Boundary

### August Snapshot Date

For this prediction block, the `August snapshot` means the first completed August 2026 biological sample collection intended as the direct follow-up to the May 2026 TruDiagnostic measurement cycle.

The biological observation window ends on the collection date, not the date on which results are received.

Results may be evaluated only after:

- the reports are received
- source artifacts are archived
- measurement comparability is reviewed
- required structured values are entered
- artifact verification is complete

If the intended collection is not completed by 2026-08-31:

- no record automatically rolls into a later testing cycle
- records dependent on the snapshot remain open if evidence is insufficient
- the missed or delayed outcome must be documented
- a later test must not be substituted silently for the August outcome

For records 041, 042, and 044, 2026-08-31 is the maximum observation boundary if no August collection occurs.

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

- the August biological sample-collection date, or
- 2026-08-31 if no August collection occurs

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

- the August biological sample-collection date, or
- 2026-08-31 if no August collection occurs

Evidence recorded before the creation of this companion plan remains admissible only when it was contemporaneously documented.

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

- the verified August source reports
- the August snapshot directory
- the corresponding structured-data entry
- directly comparable outputs from the same testing family

Raw source artifacts control when a structured value conflicts with a source report.

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

The following may be reported as supporting context when collected comparably:

- DEXA body composition
- BodPod body composition
- VO₂ or COSMED outputs
- bodyweight
- HRV
- sleep HR
- recovery telemetry

Supplemental domains cannot rescue failure of the core biological-aging comparison.

They should be interpreted separately when collection dates, devices, preparation conditions, or methodologies differ.

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
- collection-date documentation
- collection-condition documentation
- source-artifact availability
- structured transcription verification

If fewer than two core anchors are directly comparable, record 043 cannot be closed as supported or unsupported.

It remains open pending an explicit audit decision regarding non-evaluability.

---

# Record 044 — Protocol Governance

## Original Domain

`protocol_governance`

## Prediction Class

State

## Evaluation Question

Was protocol governance preserved through the August snapshot without substantive progression, volume expansion, or protocol modification lacking predefined objective support?

---

## Observation Window

2026-06-25 through:

- the August biological sample-collection date, or
- 2026-08-31 if no August collection occurs

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

1. confirm the applicable endpoint date
2. identify all admissible contemporaneous evidence
3. verify source and structured-data consistency
4. document material confounders
5. evaluate each record independently against this plan
6. prepare a traceable evidence summary
7. update the model-error CSV only after evaluation is complete
8. preserve the original prediction fields unchanged
9. document the closure in the changelog and relevant report
10. calculate or update UDI only for eligible evaluable records

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

Its role is to constrain later interpretation, not to predict additional outcomes.
