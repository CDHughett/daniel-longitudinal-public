# August 2026 Snapshot Collection Plan

**Status:** Preregistered collection plan  
**Created:** 2026-07-25  
**Primary collection window:** 2026-08-17 through 2026-08-18  
**Outcome review status at registration:** No August results viewed  
**Active phase:** Phase 2 — Load Integration  
**Operating substate:** Consolidation / lock-in observation

---

## Purpose

This document preregisters the collection conditions, evidence boundaries, source-artifact requirements, and handling rules for the August 2026 biological and performance snapshot.

Its purpose is to:

- preserve comparability with prior snapshot cycles
- prevent outcome-directed behavior before testing
- distinguish primary and supplemental measurement domains
- document ordinary-life deviations without silently normalizing them
- define source-artifact handling before results are viewed
- preserve the scoring rules already registered for Model Error record 043
- prevent favorable or unfavorable outcomes from changing the collection or interpretation rules
- separate measurement collection from later biological interpretation

This file governs collection.

It does not:

- predict the August result
- modify Model Error record 043
- redefine scoring thresholds
- declare a phase transition
- authorize protocol progression
- establish clinical significance
- determine the final interpretation of discordant results

Interpretation belongs in later reports and model-error evaluation after the complete artifact set is available.

---

# Governing Documents

This plan should be read with:

- [`open_prediction_evaluation_plan_041_044.md`](open_prediction_evaluation_plan_041_044.md)
- [`data-collection.md`](data-collection.md)
- [`../MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)
- [`../METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`../ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`../GOVERNANCE.md`](../GOVERNANCE.md)
- [`../PHASE_MAP.md`](../PHASE_MAP.md)
- [`../PHASE_DECLARATION_CRITERIA.md`](../PHASE_DECLARATION_CRITERIA.md)
- [`../data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)

Where this collection plan and the registered Model Error evaluation plan differ, the preregistered evaluation plan governs formal scoring.

---

# Snapshot Schedule

## 2026-08-17

### TruDiagnostic Collection

Planned collection time:

```text
Approximately 05:30 local time
```

Planned domains may include:

- TruAge
- TruHealth
- OMICm age
- DunedinPACE
- SymphonyAge
- organ- or system-level provider outputs
- other provider-generated metrics included in the ordered panel

The sample-collection date must remain distinct from:

- laboratory-processing date
- result-release date
- report-download date
- repository-ingestion date

---

### DEXA

Provider:

```text
DexaFit
```

Scheduled time:

```text
08:00 local time
```

Expected evidence may include:

- total body mass
- body-fat percentage
- total fat mass
- total lean mass
- regional composition
- visceral-fat output
- bone-mineral measurements
- provider-specific summary fields
- official provider report

The exact machine and software version should be recorded when available.

---

### VO₂ Max

Provider:

```text
DexaFit
```

Scheduled as part of the 08:00 appointment sequence.

Expected evidence may include:

- measured VO₂ max
- test duration
- stage or ramp structure
- peak heart rate
- respiratory-exchange information
- termination reason
- provider interpretation
- equipment and gas-analysis system when available
- official provider report

The actual order of DEXA and VO₂ testing should be recorded.

The archive must not assume the planned sequence if the provider conducts the tests in a different order.

---

## 2026-08-18

### Bod Pod

Provider alias:

```text
BODPOD_SITE_A
```

Scheduled time:

```text
08:30 local time
```

Expected evidence may include:

- measured bodyweight
- body-fat percentage
- fat mass
- fat-free mass
- body-volume output
- thoracic-gas-volume status
- predicted or measured thoracic-gas volume
- official provider printout or report

The exact procedure used should be documented when available.

---

# Primary and Supplemental Domains

## Primary Model Error 043 Domain

The primary domain for Model Error record 043 remains the registered TruDiagnostic comparison.

The May 2026 TruDiagnostic result set remains the primary comparison baseline unless the preregistered evaluation plan states otherwise.

The primary endpoint must not be replaced after outcome review by:

- DEXA
- Bod Pod
- VO₂ max
- bodyweight
- wearable recovery
- subjective state
- whichever August result appears most favorable

No supplemental result may silently become the primary endpoint.

---

## Supplemental Domains

The following provide supporting context:

- DEXA
- VO₂ max
- Bod Pod
- scale bodyweight
- wearable recovery
- sleep
- training continuity
- subjective morning state
- collection-condition deviations

Supplemental domains may:

- support concordance
- reveal discordance
- narrow interpretation
- identify measurement-method differences
- provide context for future hypotheses

They do not independently determine the primary Model Error 043 outcome.

---

# Comparison Baselines

## TruDiagnostic

Primary comparison:

```text
May 2026 snapshot
```

Earlier February 2026 values may provide secondary trajectory context.

February values must not replace May as the primary comparison merely because they produce a larger or more favorable change.

---

## Body Composition

Relevant prior body-composition evidence may include:

- July 2025 Bod Pod
- August 2025 Bod Pod
- February 2026 snapshot
- May 2026 DEXA and Bod Pod
- contemporaneous bodyweight

Cross-method comparison must remain cautious.

DEXA and Bod Pod outputs are not interchangeable measurements of body composition.

---

## VO₂ Max

The August result should be compared only with a prior formal VO₂ result when:

- the prior test method is known
- units are compatible
- testing protocols are sufficiently comparable
- equipment or provider differences are disclosed

The absence of a directly comparable prior result should remain visible.

Training-session heart rate or wearable estimates must not be represented as formal VO₂ comparison data.

---

# Representative-State Objective

The snapshot should capture an ordinary operating state rather than an artificially optimized display.

The collection objective includes:

- ordinary protocol execution
- normal hydration
- ordinary sodium intake
- ordinary carbohydrate and glycogen state
- no acute dehydration strategy
- no deliberate water loading
- no short-term sodium restriction or loading
- no acute glycogen depletion
- no acute glycogen loading
- no unusual sauna exposure before testing
- no compensatory training
- no deliberate taper introduced solely to improve the results
- no new supplement or intervention introduced for the snapshot
- no prediction-directed manipulation

Perfect control is neither claimed nor required.

Material deviations should be documented rather than concealed or retroactively normalized.

---

# Protocol Preservation

The physical protocol should remain unchanged solely because testing is approaching.

Current protocol remains:

- standard B1
- standard Load Integration
- optional recreational activity subordinate to the protocol
- ordinary recovery practices
- no forced recurrence of candidate Phase 2D-type characteristics
- no progression designed to improve the August measurements

The snapshot must not cause:

- added training volume
- reduced training volume solely for result optimization
- unusual intensity
- deliberate overreaching
- proof-seeking demonstrations
- acute bodyweight manipulation
- a change in fasting experiments
- a change in supplementation solely for the outcome

An ordinary scheduling adjustment may occur when necessary.

Any adjustment should be documented with:

- date
- reason
- affected session
- whether the adjustment was provider-required
- whether it materially changed normal exposure

---

# Pre-Collection Conditions

## General Target

The preferred pre-collection state is:

- approximately 10 hours or more fasted when compatible with provider instructions
- normally hydrated
- no caloric intake before the relevant morning testing
- no unusual alcohol or recreational-drug exposure
- no unusual heat exposure
- no acute illness when avoidable
- ordinary supplementation and medication pattern unless provider instructions require otherwise
- ordinary sleep opportunity
- no deliberate body-composition manipulation

This is a comparability objective.

It is not a claim that all prior snapshot cycles used identical conditions.

---

## Final Meal

For each testing morning, record:

- final meal time
- approximate meal composition when materially unusual
- unusual sodium exposure
- unusual carbohydrate exposure
- alcohol exposure, if any
- total fasting duration at collection

The final meal should remain representative of the existing dietary pattern.

No special “clean” meal is required solely for testing.

---

## Hydration

Maintain ordinary hydration.

Record:

- approximate fluid intake after the final meal
- morning fluid intake
- provider instructions affecting water intake
- signs of unusual dehydration
- signs of unusual fluid retention
- edema or swelling when present

Do not deliberately manipulate hydration to improve:

- scale weight
- DEXA lean mass
- Bod Pod body-fat percentage
- blood concentration
- exercise-test performance

---

## Supplements and Medications

Maintain the ordinary regimen unless:

- a provider gives specific instructions
- safety requires a change
- an unavoidable deviation occurs

Record:

- supplements taken
- supplements omitted
- medications taken
- medication deviations
- reason for any deviation
- timing when relevant

No supplement should be added, removed, or acutely dosed solely to influence the snapshot.

The archive does not infer a causal effect from routine supplement exposure.

---

## Training Before Testing

Record all training during the 72 hours before the first collection.

The record should include:

- B1 completion
- Load Integration completion
- optional aquatic or recreational activity
- unusual physical labor
- soreness
- fatigue
- mechanical signals
- session timing

The protocol should not be modified solely to create a favorable test state.

When ordinary scheduling places training near the snapshot, preserve and document it.

---

## Sauna and Heat Exposure

Avoid unusual sauna or deliberate heat exposure immediately before testing.

Ordinary environmental heat should be documented when material.

Do not introduce heat exposure to manipulate:

- bodyweight
- hydration
- plasma volume
- body-composition estimates
- cardiovascular performance

---

## Sleep

Record the night before each testing day using the normal morning-report and wearable process.

Include:

- bedtime and wake context
- total sleep
- sleep HRV
- sleep average heart rate
- readiness or equivalent provider state
- subjective sleep quality
- dream context when ordinarily recorded
- awakenings when available
- confidence limitations
- unusual sleep disruption

No isolated wearable value should automatically invalidate the snapshot.

---

# Test-Day Capture

## Morning Report

Before the first substantive result is known, record:

- morning scale weight
- mental state
- erection quality
- GI state
- stomach state
- sweating
- pain
- dream description
- last meal time
- fasting status
- prior-day training
- unusual context

The morning report should use the ordinary reporting schema.

No special favorable-state language should be introduced because the day is a snapshot day.

---

## Scale Weight

Record scale weight:

- on waking
- under the usual home measurement conditions when practical
- before major food intake
- with GI-clearance status documented
- with clothing status documented when relevant

Additional facility weights may also be recorded.

Different scales and measurement conditions must remain distinguishable.

---

## TruDiagnostic Collection Record

Record:

- collection date
- local collection time
- fasting duration
- hydration context
- collection method
- sample identifier retained privately when necessary
- visible sample quality concerns
- shipment date
- shipment method
- delivery confirmation when available
- provider receipt date
- processing status
- result-release date

Public artifacts should be screened under:

[`anonymization.md`](anonymization.md)

Administrative identifiers should not be added to the public repository merely for provenance.

---

## DEXA Capture Record

Record when available:

- test date
- local time
- provider
- machine model
- software version
- testing order relative to VO₂
- fasting duration
- fluid intake
- recent training
- clothing
- positioning issues
- repeat scans
- operator comments
- technical limitations
- official artifact filename

Do not manually alter provider-generated regional values.

---

## VO₂ Capture Record

Record when available:

- test date
- local start time
- provider
- equipment model
- gas-analysis system
- treadmill or cycle modality
- stage or ramp protocol
- test duration
- peak heart rate
- measured VO₂ max
- respiratory-exchange ratio
- ventilatory thresholds
- termination reason
- perceived exertion
- mask-fit issue
- calibration issue
- provider comments
- official artifact filename

Record whether the test was performed:

- before DEXA
- after DEXA
- after another assessment
- under a changed provider sequence

The actual sequence controls the record.

---

## Bod Pod Capture Record

Record when available:

- test date
- local time
- facility alias
- machine
- software version
- fasting duration
- hydration context
- clothing
- swim cap or hair-compression procedure
- calibration status when visible
- measured bodyweight
- thoracic-gas-volume method
- repeat trials
- operator comments
- official artifact filename

Record whether thoracic gas volume was:

- directly measured
- predicted
- not reported
- unknown

Do not infer the method from the numerical output alone.

---

# Source-Artifact Requirements

Expected source artifacts include, when supplied:

- TruDiagnostic provider report
- DEXA provider report
- VO₂ provider report
- Bod Pod provider report or printout
- relevant provider screenshots
- shipping or collection confirmation when useful
- contemporaneous morning-report evidence
- wearable screenshots or export records
- scale-weight record

Each public artifact must be reviewed for:

- full date of birth
- patient or account identifier
- specimen identifier
- address
- phone
- email
- signatures
- barcodes
- QR codes
- provider-account information
- unrelated third-party information

A private original may be retained while a sanitized public derivative is published.

Sanitization must not alter the biological or performance measurements.

---

# Evidence-Preservation Sequence

The preferred ingestion sequence is:

```text
Receive source artifact
        ↓
Retain verified private original when necessary
        ↓
Perform privacy review
        ↓
Create public derivative only when required
        ↓
Verify visible and hidden content
        ↓
Generate SHA-256 checksum
        ↓
Add artifact provenance
        ↓
Transcribe structured values
        ↓
Perform source comparison
        ↓
Interpret after the complete domain is available
```

Do not begin with retrospective narrative interpretation.

---

# Structured Data Targets

Potential structured targets include:

- `data/biomarker_snapshot.csv`
- `data/epigenetic_longitudinal.csv`
- `data/bloodwork_longitudinal.csv`
- relevant snapshot-local structured tables
- Model Error outcome fields after formal evaluation

A structured value should be entered only after:

- source artifact review
- field definition confirmation
- unit confirmation
- date confirmation
- provider-result confirmation

No value should be transcribed from memory.

---

# Outcome-Access Boundary

## Before Result Access

Before viewing a result, preserve:

- collection conditions
- deviations
- expected source artifacts
- test completion status
- sequence of testing
- relevant subjective state

Do not revise:

- prediction thresholds
- expected direction
- primary endpoint
- comparison baseline
- phase criteria
- admissible evidence

---

## After Partial Result Access

If one result becomes available before the others:

- preserve the result
- do not close Model Error 043
- do not produce a final multi-domain interpretation
- do not change the protocol in response
- do not reframe another domain as primary
- document that the artifact set is incomplete

Partial-result discussion must remain explicitly provisional.

---

## After Complete Result Access

Interpretation should begin only after:

- all completed-test artifacts are collected
- missing or delayed tests are identified
- privacy review is complete
- source values are verified
- collection deviations are documented
- the comparison baseline is confirmed
- the registered scoring plan is re-read

The final result should preserve:

- favorable evidence
- unfavorable evidence
- discordant domains
- missing tests
- collection-condition differences
- provider and method limitations

---

# Missing, Delayed, or Invalid Test Handling

## Missed Test

When a test is not completed:

- record the reason
- record whether it was rescheduled
- retain the original scheduled date
- do not invent a value
- do not replace it with a weaker metric without disclosure
- apply the registered missing-test rule

---

## Delayed Result

When processing or result release is delayed:

- preserve collection date
- preserve shipment and provider-receipt dates when available
- keep the prediction open when required evidence is unavailable
- do not use the delay as evidence of biological outcome

---

## Provider-Invalidated Test

When the provider invalidates a sample or performance test:

- preserve the invalidation notice
- document the stated reason
- distinguish provider invalidation from unfavorable outcome
- document recollection or retest conditions separately
- do not silently substitute the repeat test for the original attempt

---

## Incomplete Domain

When only part of a provider report is available:

- preserve the available source
- identify missing fields
- do not infer the missing provider values
- avoid domain-level conclusions beyond the received evidence

---

## Rescheduled Test

A rescheduled test becomes a distinct collection event.

Record:

- original appointment
- reason for rescheduling
- new date and time
- changed preparation conditions
- changed training context
- changed fasting or hydration context

The original and rescheduled conditions should not be treated as identical without review.

---

# Discordant Result Handling

Discordance is expected to remain possible across:

- TruDiagnostic metrics
- DEXA
- Bod Pod
- VO₂
- bodyweight
- wearable recovery
- subjective state

When domains disagree:

- preserve each result
- retain metric-specific interpretation
- avoid forcing one composite story
- distinguish method variance from biological disagreement when possible
- avoid selecting only the most favorable domain
- document unresolved discordance
- preserve uncertainty

DEXA and Bod Pod disagreement does not automatically establish that one is wrong.

Different TruDiagnostic outputs may move in different directions without being collapsed into one average biological-age claim.

---

# Model Error 043 Protection

The August collection plan does not modify the registered prediction.

The following remain frozen until formal evaluation:

- prediction wording
- primary endpoint
- May comparison baseline
- directional rules
- magnitude rules
- primary-versus-supplemental hierarchy
- missing-test handling
- discordance handling
- scoring window

The result must not be graded before:

- the relevant observation window closes
- required evidence is available
- source review is complete
- collection deviations are documented
- the registered evaluation plan is applied

No UDI update should occur before formal closure.

---

# Relationship to Records 041, 042, and 044

## Record 041

Recovery evidence collected around the snapshot may contribute to record 041.

The snapshot itself does not independently close the recovery-capacity window.

---

## Record 042

Performance or execution observations during the testing period may be candidate evidence.

A laboratory or body-composition result does not independently establish ambient or trait-like execution.

---

## Record 044

Protocol governance remains preserved when:

- behavior is not altered to chase favorable results
- prediction language remains unchanged
- no compensatory workload is introduced
- no outcome-directed intervention occurs
- discordant evidence is retained
- phase status is not changed prematurely

The collection process itself may therefore provide evidence relevant to governance preservation.

It does not automatically close record 044.

---

# Phase Boundary

The August snapshot does not automatically authorize:

- Phase 2D declaration
- completion of Phase 2
- Phase 3 activation
- workload progression
- new testing demands
- public capability demonstration

A favorable snapshot may become transition evidence.

It is not a phase declaration by itself.

Current protected state remains:

```text
Phase 2 — Load Integration
Operating substate: consolidation / lock-in observation
Phase 2D: undeclared
Phase 3: reserved and inactive
```

---

# Collection-Day Deviation Log

For each day, complete the following when applicable.

## 2026-08-17

```text
Wake time:
Morning weight:
GI-clearance status:
Last meal time:
Fasting duration:
Morning fluid intake:
Mental state:
EQ:
GI state:
Stomach state:
Pain:
Sweating:
Dream or sleep context:
Prior-day training:
Sleep duration:
Sleep HRV:
Sleep average heart rate:
Readiness:
TruDiagnostic collection time:
DEXA start time:
VO₂ start time:
Actual test order:
Unexpected delay:
Provider instruction deviation:
Supplement or medication deviation:
Hydration deviation:
Illness or mechanical signal:
Source artifacts received:
Other material context:
```

---

## 2026-08-18

```text
Wake time:
Morning weight:
GI-clearance status:
Last meal time:
Fasting duration:
Morning fluid intake:
Mental state:
EQ:
GI state:
Stomach state:
Pain:
Sweating:
Dream or sleep context:
Prior-day testing and activity:
Sleep duration:
Sleep HRV:
Sleep average heart rate:
Readiness:
Bod Pod start time:
Clothing:
Hair-compression procedure:
Thoracic-gas-volume method:
Unexpected delay:
Provider instruction deviation:
Supplement or medication deviation:
Hydration deviation:
Illness or mechanical signal:
Source artifacts received:
Other material context:
```

Blank items remain blank or are marked unknown.

They should not be reconstructed later from assumption.

---

# Post-Collection Workflow

After collection:

1. retain all original provider files privately or publicly as appropriate
2. perform privacy review
3. create sanitized derivatives only when necessary
4. assign stable filenames
5. generate checksums
6. verify artifact readability
7. transcribe values into structured files
8. perform field-by-field source verification
9. document collection-condition deviations
10. compare with the registered baselines
11. preserve discordant results
12. evaluate Model Error 043 only under the registered plan
13. review relevance to records 041, 042, and 044
14. update the appropriate snapshot epoch record
15. update the changelog
16. update release metadata only when an intentional release is created
17. avoid phase declaration until separate retrospective review

---

# Release Boundary

The August snapshot may justify a later archival release.

Collection alone does not create a release.

A release decision should occur only after:

- source artifacts are complete
- privacy review is complete
- checksums pass
- structured values are verified
- reports are complete
- prediction outcomes are evaluated when appropriate
- changelog entries are accurate
- repository validation passes
- versioning rules are applied

No version number is preregistered by this plan.

---

# Governance Checklist

Before collection:

- [ ] Collection plan committed before outcome access
- [ ] Model Error 043 wording unchanged
- [ ] Evaluation thresholds unchanged
- [ ] Primary endpoint unchanged
- [ ] May comparison baseline unchanged
- [ ] Protocol unchanged for result optimization
- [ ] No new snapshot-directed intervention introduced
- [ ] Providers and appointments confirmed
- [ ] Source-artifact expectations recorded

After collection but before interpretation:

- [ ] Collection times recorded
- [ ] Fasting duration recorded
- [ ] Hydration context recorded
- [ ] Recent training recorded
- [ ] Deviations recorded
- [ ] Test order recorded
- [ ] Missing or rescheduled tests recorded
- [ ] Source artifacts retained
- [ ] Privacy review completed
- [ ] Checksums generated
- [ ] Structured transcription source-verified
- [ ] Registered scoring plan re-read

Before final closeout:

- [ ] All available domains reviewed
- [ ] Discordant evidence preserved
- [ ] Missingness preserved
- [ ] No primary-endpoint substitution
- [ ] No outcome-driven threshold change
- [ ] Model Error 043 scored only when eligible
- [ ] Records 041, 042, and 044 reviewed separately
- [ ] Phase status reviewed separately
- [ ] Changelog updated
- [ ] Local repository validator passed
- [ ] Fresh repository ZIP verified when materially changed

---

# Protected Boundaries

This collection plan does not authorize modification of:

- Model Error records 041–044
- registered prediction wording
- registered scoring thresholds
- May 2026 primary comparison baseline
- current protocol exposure
- current phase declaration
- canonical sleep data
- RingConn source exports
- prior snapshot artifacts
- historical reports
- closed model-error outcomes
- current release metadata

Any later change requires separate evidence and governance.

---

# Interpretation Boundary

The August snapshot will produce measurement evidence.

It will not independently establish:

- causality
- protocol efficacy
- permanent adaptation
- clinical diagnosis
- population-level validity
- Phase 2D
- Phase 3
- correctness of every provider algorithm
- absence of measurement error

Interpretation must remain proportional to:

- source quality
- collection conditions
- measurement comparability
- missingness
- provider behavior
- discordance
- the preregistered scoring rules

---

# Current Registration Statement

As of 2026-07-25:

- the August results have not been viewed
- the scheduled collection dates are known
- the providers and testing domains are known
- the primary and supplemental evidence hierarchy is preserved
- the physical protocol remains unchanged
- Model Error records 041–044 remain open and unscored
- no Phase 2D declaration has occurred
- no August release version has been selected

This plan is therefore registered before outcome access.

---

## Version Note

This collection plan was created on 2026-07-25 before the scheduled August 17–18 measurement window.

It preregisters:

- collection dates
- testing domains
- representative-state objectives
- fasting and hydration documentation
- training and supplement boundaries
- source-artifact handling
- missing and delayed test treatment
- discordant-result handling
- primary and supplemental endpoint separation
- Model Error 043 protection
- phase-declaration boundaries
- post-collection workflow

The plan does not alter:

- any biological value
- any prediction
- any scoring threshold
- any protocol exposure
- any phase declaration
- any existing artifact
