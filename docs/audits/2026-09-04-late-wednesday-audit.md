# Late Wednesday Repository Audit — 2026-09-04

**Audit type:** Delayed scheduled Wednesday audit  
**Scheduled checkpoint:** 2026-09-02  
**Actual audit date:** 2026-09-04  
**Repository:** `CDHughett/daniel-longitudinal-public`  
**Audit posture:** Read-only review of the repository state as supplied  
**Overall disposition:** `PASS WITH NARROW SEMANTIC REMEDIATION REQUIRED`

---

## Audit Purpose

This audit serves as the delayed Wednesday repository review that was scheduled for 2026-09-02 and actually performed on 2026-09-04.

The audit is intentionally dated to the date on which review occurred.

No backdated September 2 audit is created.

The review evaluates:

- repository mechanical integrity
- exact change surface since the last audited Saturday package
- canonical sleep extension
- Week 34 closeout
- Week 35 initialization
- model-error and prediction-provenance preservation
- artifact and checksum integrity
- phase and protocol governance
- release integrity
- semantic consistency
- unresolved source discrepancies

The audit does not itself modify source data, biological values, prediction outcomes, protocol state, phase state, or release metadata.

---

# Reviewed Package

Current reviewed package:

```text
daniel-longitudinal-public-main (18).zip
```

Package size:

```text
40,135,759 bytes
```

SHA-256:

```text
3de4a952aec36486f510b19b3202d1771b54dd665b9e64d317b09c16587e53cb
```

The last formally audited Saturday reference package was:

```text
daniel-longitudinal-public-main (14).zip
```

Reference package size:

```text
40,138,259 bytes
```

Reference SHA-256:

```text
62935ddd3d663bfff8de3484973c15f52cfc0ddcd6322e91857ab516eba1475f
```

---

# File-Level Delta

Comparison with the August 29 audited package identified:

```text
Added:
1

Changed:
7

Removed:
0
```

Added:

```text
reports/2026-W35.md
```

Changed:

```text
CHANGELOG.md
INDEX.md
LATEST.md
README.md
data/sleep_longitudinal_v1.csv
methodology/README.md
reports/2026-W34.md
```

No change was identified in:

```text
data/model_error/model_error_gap_v1.csv
data/model_error/udi_by_type_tracker.csv
data/model_error/calibration_events_log.md
tools/validate_repository.py
VERIFICATION.md
methodology/open_prediction_evaluation_plan_041_044.md
methodology/open_prediction_evaluation_plan_045.md
methodology/open_prediction_evaluation_plan_046.md
methodology/2026-08-snapshot-collection-plan.md
```

No checksum manifest or binary source artifact changed.

The observed delta is coherent with:

- Week 34 retrospective closeout
- Week 35 initialization
- Week 34 canonical sleep extension
- current-state documentation advancement

---

# Mechanical Validation

## Fresh ZIP

```text
Errors:
0

Warnings:
2

Passes:
10

Result:
PASS
```

## Extracted Repository

```text
Errors:
0

Warnings:
2

Passes:
9

Result:
PASS
```

Validator Python compilation also completed successfully.

---

# Repository Inventory

Current reviewed state:

```text
Repository files:
192

Zero-byte files:
0

Exact duplicate hash groups:
0

Markdown files:
134

Internal Markdown references:
778

CSV files:
11

Registered checksum entries:
33

Canonical sleep rows:
203

Canonical sleep coverage:
2026-02-09 through 2026-08-30

Weekly reports:
30

Weekly range:
2026-W06 through 2026-W35

Active weekly report:
2026-W35.md

Model-error records:
34

Model-error range:
013 through 046
```

Release metadata remains aligned at:

```text
Version:
1.0.0

Release date:
2026-06-23

DOI:
10.5281/zenodo.20815612
```

---

# Governed Validator Warnings

No new mechanical warning was identified.

Existing governed sleep-data warnings remain limited to:

```text
2026-03-31:
+16 min sleep-stage difference

2026-04-02:
+14 min sleep-stage difference

DQ-001:
awake-minute / awakening-count duplication
on 14 historical dates
```

These remain documented data-quality issues.

They do not authorize automatic correction and do not mechanically invalidate the repository.

---

# Artifact Integrity

Artifact readability remains intact.

```text
Images:
24 / 24 readable

PDFs:
7 / 7 readable

PDF pages:
115

Encrypted PDFs:
0
```

Registered checksum state:

```text
33 / 33 PASS
```

No binary source artifact changed relative to the August 29 audited package.

This includes the current:

- August DEXA artifacts
- August VO₂ artifact
- August Bod Pod artifact
- sanitized July 2025 blood artifact
- RingConn source-export package

RingConn byte-preservation controls remain intact.

---

# Canonical Sleep Audit

The previous canonical dataset through 2026-08-23 remains preserved.

Exactly seven new daily rows were appended:

```text
2026-08-24
2026-08-25
2026-08-26
2026-08-27
2026-08-28
2026-08-29
2026-08-30
```

No earlier canonical sleep row was rewritten.

Current canonical coverage is:

```text
2026-02-09 through 2026-08-30
```

with:

```text
203 continuous daily rows
```

The append therefore passes continuity and append-only review.

---

# Week 34 Retrospective Closeout

`reports/2026-W34.md` is correctly closed.

The observation window is:

```text
2026-08-24 through 2026-08-30
```

Independent arithmetic review produced:

```text
Morning bodyweight:
233.79 lb
≈ 233.8 lb

Daily biomarker HRV:
59.14 ms
≈ 59.1 ms

Resting heart rate:
49.57 bpm
≈ 49.6 bpm

Daily average heart rate:
65.43 bpm
≈ 65.4 bpm

Sleep HRV:
65.29 ms
≈ 65.3 ms

Sleeping heart rate:
52.0 bpm

Total sleep:
444.29 min
≈ 7 h 24 min

Time in bed:
483.57 min
≈ 8 h 04 min

Sleep efficiency:
92.0%

Deep sleep:
85.86 min
≈ 1 h 26 min

REM:
58.29 min
≈ 58 min
```

Formal training arithmetic remains coherent:

```text
B1:
7 × 55 min
= 385 min

Approximate B1 distance:
21.14 miles

Load Integration:
7 × 45 min
= 315 min

Total formal training:
700 min
```

No Week 34 arithmetic correction is required.

---

# Week 35 Initialization

`reports/2026-W35.md` is correctly present as the sole active weekly report.

Current lifecycle:

```text
2026-W34:
closed

2026-W35:
active
```

No duplicate active weekly report was identified.

Week 35 remains an observational period under the existing protocol and phase architecture.

---

# Model-Error Register

Current governed prediction state remains:

```text
041
calibration_state = pre
status = closed
outcome = supported

042
calibration_state = pre
status = closed
actual = continued_adaptation
outcome = not supported

043
calibration_state = pre
status = open
outcome = unscored

044
calibration_state = pre
status = closed
outcome = not supported
classification = narrow governance miss

045
calibration_state = pre
status = closed
outcome = supported

046
calibration_state = pre
status = closed
actual = failed_autonomic_recompression
outcome = not supported
```

The original registered `Prediction:` narratives remain preserved.

---

# Record 043 Protection

Model Error 043 remains correctly:

```text
open
unscored
calibration_state = pre
```

Protected actual and error fields remain blank.

Its primary evidence domain remains the pending TruDiagnostic provider-result layer.

No supplemental August result has been substituted for that endpoint.

This includes:

- DEXA
- VO₂ max
- Bod Pod
- bodyweight
- recovery metrics
- subjective observations
- Model Error 046 outcome

Record 043 protection:

```text
PASS
```

---

# Record 046 Historical Boundary

Model Error 046 remains closed under its original fixed scoring boundary.

Its primary scoring interval was:

```text
2026-08-20 through 2026-08-23
```

Its registered four-marker means remain:

```text
Daily biomarker HRV:
60.25 ms

Sleep HRV:
63.25 ms

Resting heart rate:
52.0 bpm

Sleeping heart rate:
54.0 bpm
```

Threshold result:

```text
1 of 4 favorable
```

Registered support required:

```text
at least 3 of 4 favorable
```

with preserved function and no recovery-driven reduction after reload.

The fixed-window result remains:

```text
failed_autonomic_recompression
```

Later Week 34 observations do not reopen, rescue, or rescore the record.

Record 046 historical closure:

```text
PASS
```

---

# Registration-Provenance Protection

Records 041 through 046 retain:

```text
calibration_state = pre
```

The original registered prospective `Prediction:` narratives remain present.

The validator continues to protect:

- open/closed lifecycle state
- selected adjudicated outcomes
- selected error directions
- registration-state provenance
- original prediction narratives

Temporary destructive-control testing confirmed that the validator fails appropriately when protected state is synthetically altered.

Registration-provenance protection:

```text
PASS
```

---

# Phase and Protocol Governance

Current canonical phase remains:

```text
Phase 2 — Load Integration
```

Current operating substate remains:

```text
Consolidation / lock-in observation
```

Current transition state remains:

```text
Phase 2D:
undeclared

Phase 3:
reserved and inactive
```

The underlying formal protocol remains:

```text
B1
+
Load Integration
```

No automatic progression, recovery-driven intervention, direct grip program, manufactured portability test, or phase declaration was introduced by the Week 34 update.

Phase and protocol governance:

```text
PASS
```

---

# Finding 1 — Post-Window Record 046 Sleep Tag

A new narrow semantic inconsistency was identified in the canonical sleep append.

The 2026-08-24 row includes:

```text
record_046
```

within `sleep_tags`.

Record 046's fixed scoring window ended on:

```text
2026-08-23
```

August 24 therefore lies outside the registered scoring interval.

The repository otherwise correctly preserves later evidence as incapable of reopening or rescuing record 046.

The tag is therefore temporally misleading.

Classification:

```text
Biological value error:
NO

Record 046 scoring error:
NO

Date-continuity error:
NO

Semantic tag inconsistency:
YES
```

Recommended narrow correction:

```text
Remove only:
record_046

from:
2026-08-24 sleep_tags
```

No other field in that row should change.

Disposition:

```text
NARROW CORRECTION REQUIRED
```

---

# Finding 2 — Testing Causal-Language Boundary

The archive continues to contain wording that exceeds its standing causal-attribution boundary.

Examples include wording equivalent to:

```text
The maximal VO₂ test produced measurable autonomic carryover.
```

and:

```text
The August testing window produced a real but bounded autonomic perturbation.
```

Related shorthand such as:

```text
maximal-testing perturbation
```

appears in current-facing documentation.

The repository's standing interpretation boundary distinguishes temporal association from established causality.

The evidence supports language such as:

```text
post-testing autonomic disturbance
```

or:

```text
A measurable autonomic disturbance followed the
August 17 maximal VO₂ test and persisted into the
reload interval.
```

The semantic correction does not alter:

- physiological observations
- Model Error 046 scoring
- Model Error 046 failure
- protocol state
- phase state
- August artifact validity

Disposition:

```text
NARROW SEMANTIC CORRECTION REQUIRED
```

---

# Finding 3 — August 17 Bodyweight Source Discrepancy

The Week 33 record preserves two competing August 17 morning-bodyweight values:

```text
Daniel_Dataset_v1.27:
234.1 lb

earlier Week 33 / August collection record:
235.1 lb
```

The current Week 33 weekly calculation uses:

```text
234.1 lb
```

and therefore reports approximately:

```text
235.4 lb weekly mean
```

If the `235.1 lb` value were ultimately confirmed as the stronger contemporaneous source, the weekly mean would instead be approximately:

```text
235.5 lb
```

The difference does not affect Model Error 046 scoring.

No source hierarchy decision is authorized from inference alone.

The discrepancy must remain visible until the strongest contemporaneous source is reconciled.

Downstream current-state documents should qualify the Week 33 bodyweight comparison when using the current structured value.

Disposition:

```text
OPEN SOURCE RECONCILIATION
```

No biological-value correction is authorized by this audit.

---

# Changelog Compression Review

The active `CHANGELOG.md` became materially shorter during the reviewed update.

The audit specifically examined whether the compaction removed governing provenance.

No loss of authoritative evidence was identified.

Detailed historical state remains preserved in:

- formal audit files
- methodology files
- model-error records
- weekly reports
- snapshot epoch files
- checksum manifests
- privacy-governance documentation

The active changelog therefore remains a navigation and change-summary layer rather than the sole evidence source.

Classification:

```text
ACCEPTABLE
```

No restoration of removed repetitive changelog material is required solely for archive integrity.

---

# Privacy and Release Review

Current controlled-distribution privacy state remains unchanged.

The project continues to classify its privacy-remediation posture as:

> Controlled distribution remediation completed, with GitHub provider-side cleanup pending and uncontrolled-copy limitations disclosed.

No new privacy artifact entered the reviewed change surface.

Release metadata remains:

```text
Version:
1.0.0

Release date:
2026-06-23

DOI:
10.5281/zenodo.20815612
```

No release increment is warranted from the reviewed weekly closeout or this audit.

---

# Audit Disposition

```text
ZIP integrity:
PASS

Repository mechanics:
PASS

Expected change surface:
PASS

Canonical sleep continuity:
PASS

Week 34 append-only integrity:
PASS

Week 34 arithmetic:
PASS

Week 34 training totals:
PASS

Week 35 lifecycle:
PASS

Artifact readability:
PASS

Checksum integrity:
PASS

RingConn source preservation:
PASS

Model-error continuity:
PASS

041–046 registration provenance:
PASS

Record 043 protection:
PASS

Record 046 historical closure:
PASS

Protocol governance:
PASS

Phase governance:
PASS

Release governance:
PASS

Privacy state:
PASS

Post-window record 046 sleep tag:
NARROW CORRECTION REQUIRED

Testing causal-language boundary:
NARROW SEMANTIC CORRECTION REQUIRED

August 17 bodyweight:
OPEN SOURCE RECONCILIATION
```

Overall:

```text
PASS WITH NARROW SEMANTIC REMEDIATION REQUIRED
AND ONE PRESERVED SOURCE DISCREPANCY
```

---

# Authorized Follow-Up

This audit authorizes the following narrow repository-maintenance sequence:

1. preserve this audit artifact before remediation
2. remove `record_046` from the `2026-08-24` canonical sleep tag field only
3. narrow testing-causality wording to temporal-association language
4. qualify downstream Week 33 bodyweight references while the August 17 source discrepancy remains unresolved
5. update the changelog after the above corrections
6. obtain a fresh GitHub ZIP
7. run final post-remediation repository verification

This audit does **not** authorize:

- selecting `234.1 lb` or `235.1 lb` without source reconciliation
- modifying any other biological value
- rescoring Model Error 046
- closing Model Error 043
- changing any registered prediction threshold
- changing any preregistered evaluation window
- altering the physical protocol
- declaring Phase 2D
- activating Phase 3
- changing release metadata

---

# Final Audit Statement

The repository remains mechanically coherent and structurally healthy.

The reviewed Week 34 update preserved:

- append-only canonical sleep history
- prediction provenance
- model-error closure boundaries
- source-artifact integrity
- protocol governance
- phase governance
- release integrity

The identified issues are narrow and traceable:

```text
1.
one stale post-window semantic tag

2.
testing-related causal language that should be narrowed

3.
one already-disclosed unresolved bodyweight source discrepancy
```

None alters the current biological evidence, Model Error 046 adjudication, Model Error 043 status, physical protocol, phase state, or release state.

The repository is therefore classified:

```text
PASS WITH NARROW SEMANTIC REMEDIATION REQUIRED
```
