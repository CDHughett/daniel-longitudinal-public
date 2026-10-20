# Open Prediction Evaluation Plan — Model Errors 047–050

**Status:** Prospectively registered evaluation companion; records 047, 048, 049 and 050 to be opened in the SAME commit as this file
**Registration date:** 2026-10-19 (local date at prospective registration)
**Model:** gpt6-subject-calibrated
**Record priority:** All four primary
**Outcome access:** No November 2026 provider results viewed or generated as of registration
**Primary observation event:** 2026-11-16, with provider-result processing and release allowed after the sample/test date
**Project state:** Phase 2 — Load Integration / Consolidation / lock-in observation; Phase 2D undeclared

---

## Purpose and strict temporal boundary

This plan locks four independently resolvable November snapshot forecasts, their baseline/source hierarchy, numerical success and failure definitions, and missing/invalid/comparability conditions. It is an evaluation companion to:
- [The prospective November collection-governance plan](2026-11-snapshot-collection-plan.md).
- [Prediction evaluation methodology](prediction_evaluation.md) and [validity criteria](../docs/methodology/valid_prediction_criteria.md).
- [The primary Model Error registry](../data/model_error/model_error_gap_v1.csv).
- [Protected historical prediction plans 041–044](open_prediction_evaluation_plan_041_044.md), [045](open_prediction_evaluation_plan_045.md) and [046](open_prediction_evaluation_plan_046.md).

**Lock point:** the first Git commit that includes the unchanged-open 047–050 CSV entries AND this complete evaluation plan. Record date is October 19, 2026, not the future testing date. Observations already available by that lock point provide context only, not November outcomes. The dated collection plan is earlier governance groundwork and accurately states the four records were not yet registered *at its initial commit*.

These are four domain-specific predictions, not one composite "overall improvement" claim. Each can fail regardless of favorable results in the other three. They are separately scorable, **not statistically independent**: the molecular outputs share assay/model dependencies and the physical results share body-mass influences.

Prospectively lock source precedence, precision, candidate dates, scoring logic and missingness before any November provider outputs become visible. No favorable or adverse preliminary result can lead to rewriting a threshold, choice of endpoint, provider, method or baseline.

No prediction authorizes a training change, intervention, skipped session for testing freshness, UDI update, phase declaration, diagnosis or clinical inference.

---

## Source hierarchy and fixed baseline provenance

1. **Measurement endpoint:** full, authenticated **November provider report** for the named endpoint with reported numeric units, device/method, date and validity indicators. Direct provider export of the same measurement may serve equivalently if verified. An app card is a secondary representation where the complete report exists. Do not select the most favorable source after result access.
2. **Collection context:** contemporaneous sample/test log for actual test date/time, fasting and hydration, exercise restrictions and sample validity. Preserve conflicting provider header dates as separate administrative metadata; historical August DQ-010 supplies the source-role precedent.
3. **Transcribed rows:** public structured molecular and DEXA data after line-by-line verification with original/sanitized-provider artifacts; later weekly or narrative syntheses are subordinate.
4. **Baselines:** 2026-08-17 DunedinPACE 0.77, SymphonyAge 46.1 years, August DEXA fat mass 40.0 lb and provider-defined lean mass 185.3 lb, August screen-displayed formal-test relative VO2max 50 mL/kg/min. May formal-test displayed VO2max 45 mL/kg/min provides secondary context only.
5. **Known VO2 baseline limitation:** the numeric May/August values are displayed in supplied provider-app screenshots; the archived provider VO2 PDFs under snapshots/2026-05 and snapshots/2026-08 carry checksum manifests, but their quantitative content was not independently extracted during this registration review. This limitation must be resolved at source-admissibility review, not erased by calling the screenshots verified PDFs.

Baseline observations are historical facts available before registration. The November 17 Tanita assessment is supplementary, not a replacement DEXA, Bod Pod or metabolic VO2 endpoint.

### Actual test date and comparability

The planned test event is November 16, 2026: 05:30 local TruAge/TruHealth collection and 08:00 local combined DEXA/VO2 appointment, with actual procedure start times to be logged separately. Provider reporting dates may be later. A provider-valid result from the collected November 16 sample/test can be used after release. If the appointment is missed, delayed, retested, materially reordered or moved to a new device/protocol, preserve the original planned test and the distinct actual event. **Do not silently replace the fixed November 16 endpoint with a more favorable retest**; any admissibility decision must be documented under fixed rules and cannot be tailored to result direction.

The November molecular test products must actually include the named TruAge DunedinPACE and Advanced TruAge SymphonyAge outputs. Ordered TruAge/TruHealth alone does not prove Advanced TruAge is included. A missing field is missing, not a proxy.

For DEXA, preserve scanner/site/region, body-comp definitions, hydration/preparation and provider validity. Same-labeled measurements are not necessarily comparable if instruments or algorithms differ materially; document comparability before scoring.

For VO2, require formal metabolic testing, distinguish relative mL/kg/min from absolute L/min, record modality, ramp/stage method, mask and calibration/effort issues, provider validity, termination reason and test-day bodyweight. An app rounded number must not override more precise values in a full authenticated report. If method differs materially or the test is not provider-valid, do not pretend it is a comparable improvement.

---

## Registered forecasts — exact immutable registry note text

**Record 047 prediction (exact locked text):** Prediction: The November 16, 2026 TruAge collection will yield a provider-reported DunedinPACE value of 0.76 (ratio), compared with the August 17, 2026 baseline of 0.77. This is a numeric point forecast, not a binary improvement guarantee; only the registered DunedinPACE field is admissible.

**Record 048 prediction (exact locked text):** Prediction: The November 16, 2026 Advanced TruAge result will report SymphonyAge between 40.0 and 44.0 years inclusive, compared with the August 17, 2026 baseline of 46.1 years. The range tests partial reversal of the August rebound; neither a different age clock nor a proxy result may satisfy it.

**Record 049 prediction (exact locked text):** Prediction: The November 16, 2026 DEXA provider report will show total fat mass at or below 36.0 lb AND provider-defined lean mass at or above 183.0 lb, compared with August 17, 2026 DEXA values of 40.0 lb and 185.3 lb respectively. Both components must hold in a valid comparable DEXA assessment; Tanita and Bod Pod are excluded.

**Record 050 prediction (exact locked text):** Prediction: The November 16, 2026 valid formal metabolic-test report will show relative VO2max of at least 52.0 mL/kg/min, compared with the August 17, 2026 provider-app displayed value of 50 mL/kg/min. Source-reported precision and method comparability control scoring; a wearable estimate or absolute VO2 cannot substitute.

These four exact note narratives are prefixed by "Prediction: " in the registry. The validator protects each registered narrative and numerical prediction field. When each record is still open, its notes must match the prospective text exactly; a future governed closure may append "Closure: ..." without changing the original prefix.

---

## Record 047 — DunedinPACE numerical point

**ID:** 047
**Domain:** epigenetic_pace
**Model / state:** gpt6-subject-calibrated / primary / pre / point
**Predicted value in v1:** \`0.76\`
**Reference:** 2026-08-17 provider DunedinPACE \`0.77\` (May \`0.79\`, February \`0.88\` contextual)
**Observation:** original November 16, 2026 TruAge sample; provider-reported DunedinPACE ratio when processing completes.

**Resolution:** compare the exact provider-reported DunedinPACE numeric value with 0.76 at the original report precision. The point forecast need not equal a binary pass/fail improvement state. When admissible and full window complete, error_absolute = abs(actual - 0.76); error_pct = abs(actual - 0.76) / 0.76 * 100, displayed with sufficient precision to avoid masking small misses. error_direction = under if actual > 0.76; over if actual < 0.76; none if exact equality. Here *under* means predicted a lower (more favorable) pace than observed, and *over* means observed pace was more favorable than predicted. Preserve reported precision; do not coerce a 0.755 to 0.76 in order to call an exact hit.

**Insufficient evidence:** missing DunedinPACE field, provider-invalidated sample, unverifiable assay identity or unusable source. A different methylation-age clock, TruHealth score or remembered estimate is not admissible. A provider-valid reported 0.80 must score as a model overoptimistic miss; it is **not** excused by an otherwise favorable DEXA or VO2 result.

---

## Record 048 — SymphonyAge bounded range

**ID:** 048
**Domain:** epigenetic_symphony_age
**Model / state:** gpt6-subject-calibrated / primary / pre / range
**Predicted interval in v1:** \`40.0-44.0\` years, inclusive
**Reference:** 2026-08-17 SymphonyAge 46.1 provider-modeled years (May 37.8, February 51.2 contextual)
**Observation:** November 16, 2026 collected sample's provider-reported Advanced TruAge **SymphonyAge**, when available.

**Resolution:** inclusive interval [40.0, 44.0] at provider-reported precision. If 40.0 <= actual <= 44.0, error_absolute=0; error_direction=none; error_pct=0%. If actual >44.0, error_absolute=actual - 44.0 and direction=under (model predicted a value too low / biologically more favorable than realized); if actual <40.0, error_absolute=40.0 - actual and direction=over (a numerically more favorable result than the forecast range). For out-of-range cases compute optional descriptive percent against the violated boundary and identify it explicitly; do not invent a midpoint-error convention after seeing the actual. Both above and below count as interval misses, regardless of whether the miss is biologically favorable.

**Insufficient evidence:** Advanced TruAge/SymphonyAge not included or not returned, incompatible changed provider-model output, invalid sample or missing verifiable value. No substitution with OMICm, DNAm age, system-age averages or a new clock. Preserve model version if reported; the output is a provider-modeled measure, not direct organ-age truth.

---

## Record 049 — DEXA lean-preserving fat reduction (conjunctive state)

**ID:** 049
**Domain:** dexa_body_composition
**Model / state:** gpt6-subject-calibrated / primary / pre / state
**Predicted state in v1:** \`1\` (both locked conditions true)
**Reference:** August 17 DEXA total fat mass 40.0 lb, lean mass 185.3 lb
**Primary observation:** provider-valid, comparably defined November 16 DEXA report.

**Two simultaneous conditions:**
1. DEXA total **fat mass <=36.0 lb**.
2. DEXA provider-defined total **lean mass >=183.0 lb**.

**Resolution:** only a valid, method-compatible DEXA with both defined components can support the combined state. If both hold, actual_value=1, error_absolute=0, error_direction=none, error_pct=0%. If either reliably observed component violates its condition on a valid comparable DEXA, the conjunction is disproved regardless of a missing second component: actual_value=0, error_absolute=1, error_direction=under, error_pct=100%. If an observed component passes while the other is missing or invalid, the result is insufficient evidence and the record remains open. Separately record the actual fat and lean values even when the binary state fails, without concealing which condition was violated.

**Ineligible substitutes:** Tanita, Bod Pod, household scale, a derived lean mass from an incompatible compartment definition, or a DEXA result whose source labels/scan mode do not permit comparison. Source-valid worsening must not be discarded because intake, glycogen or hydration might be explanatory; document material confounders but preserve the failure.

---

## Record 050 — Formal relative VO2max threshold (state)

**ID:** 050
**Domain:** vo2max_relative
**Model / state:** gpt6-subject-calibrated / primary / pre / state
**Predicted state in v1:** \`1\` (relative VO2max meets threshold)
**Reference:** provider-app displayed August 17 formal VO2max 50 mL/kg/min; May 11: 45 mL/kg/min
**Primary observation:** provider-valid, sufficiently comparable November 16 formal metabolic test.

**Numerical condition:** relative VO2max **>=52.0 mL/kg/min**, using the complete provider report's original numeric precision, not rounding chosen after seeing the result.

**Resolution:** if a comparable valid November formal provider value is >=52.0, actual_value=1, error_absolute=0, error_direction=none, error_pct=0%. If below 52.0, actual_value=0, error_absolute=1, error_direction=under, error_pct=100%. For a reported integer 52 with no available additional report precision, score the reported integer only if the provider report directly supplies 52 and all method-validity conditions are met; note reported precision. If the full report supplies 51.6 and a separate app card rounds it to 52, score the authoritative 51.6 as failure. Do not recover an ineligible prediction by switching to a wearable estimate, absolute VO2, a training-derived value or the highest of repeated attempts.

**Secondary, descriptive only:** capture peak absolute oxygen uptake in L/min, testing weight, peak HR, modality, gas-analyzer method, protocol and termination quality if available. A relative gain can partly reflect decreased denominator mass; record this without automatically claiming greater absolute uptake.

**Insufficient evidence:** test invalidity, absent formal value, materially incompatible modality/protocol lacking defensible comparison, source precision not adequate for a reliable threshold determination, or unverified test identity. Preserve actual results as observations, not retrospectively score an unrelated metric.

---

## Cross-domain scoring and confidence boundaries

1. All four entries must remain **OPEN**, with actual_value, error_absolute, error_direction and error_pct **blank** until their distinct observation windows and source-evidence requirements are met. The registration provenance \`calibration_state=pre\` is permanent registration metadata, not changed to \`post\` at closure.
2. For each record, preserve baseline, test identity, provider precision, comparison validity and reported numeric outcome separately. No result can be inferred from subjective effort, wearable sleep staging, a pre-2D training descriptor, or model narrative.
3. Do not invent statistical independence: DunedinPACE/SymphonyAge share methylation-report dependencies, and body composition/relative VO2 have body-mass-related dependencies. Each is nevertheless a separate registered claim with a separately recorded error.
4. Unfavorable yet valid test results must count as misses wherever the locked condition fails. Provider uncertainty, confounders, illness and technical limitations can restrict or qualify adjudication only under the predefined validity/missingness logic, not serve as post-hoc rescues.
5. If the original appointment is missed or the test rescheduled, keep the original November 16 observation boundary intact. Log new dates, reasons, changes in method and candidate evidence; a new test is not silently deemed the original source. A future formal governance amendment may specify a handling rule but cannot be retroactively favorable.
6. Model error calibration/UDI and concordance trackers are **not** updated when the prediction records are opened. Only completed, eligible, formally adjudicated outcomes enter evaluation statistics under the existing UDI methodology.
7. One metric supporting a preferred "overall improvement" narrative does not overwrite other failed metrics. Historical Record 043 stays closed and unchanged.
8. No 047–050 outcome is scored against November 17 Tanita; it supplies only separately labeled context, not substitute DEXA or Bod Pod evidence.
9. No open prediction, favorable biomarker value, or improved VO2 independently declares Phase 2D or changes the ongoing Phase 2 training prescription.

---

## Future closure checklist (not performed at registration)

- [ ] Original registration commit and its four OPEN CSV entries verified unchanged.
- [ ] Full provider reports for specific November tests available and sanitized appropriately; checksums and source roles documented.
- [ ] Actual collection/test dates, source labels, preparation, missed/rescheduled tests and deviations reconciled.
- [ ] Provider-specific method comparability, assay output availability, units, and original precision checked.
- [ ] Actual observed endpoint entered from primary source, not a selected card or later narrative.
- [ ] Fixed point/range/state scoring applied independently, preserving unfavorable outcomes.
- [ ] Any missing or invalid test retained open unless a separately governed formal inability-to-score disposition is warranted.
- [ ] Adjudication notes append to the exact original "Prediction:" narrative; the registration date, domain, model/version and numerical forecast never change.
- [ ] Any alteration of validator OPEN-status protection happens in the separate, documented closure commit with an audit trail; locked forecast/narrative checks remain in force.
- [ ] Only formally closed eligible records may affect subsequent concordance or UDI recalculation.

## Registration statement

**2026-10-19:** Four forecasts are intended to be registered together as prospective primary Model Error records 047–050 in the same Git commit as this file. All November outcomes are unknown at registration. This companion defines their evaluation rules, distinct event dates, source hierarchy, precision and insufficiency boundaries before result access. Its complete bytes are protected by a Git-blob identity assertion in the repository validator after the atomic registration commit.
