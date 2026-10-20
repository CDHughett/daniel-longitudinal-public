# November 2026 Snapshot Collection Plan — Prospective Governance

**Status:** Prospectively registered collection-governance groundwork; Model Error records 047–050 NOT YET REGISTERED  
**Created:** 2026-10-19  
**Planned collection window:** 2026-11-16 through 2026-11-17  
**Outcome access at registration:** No November 2026 result viewed  
**Declared operating state:** Phase 2 — Load Integration / Consolidation / lock-in observation  
**Formal Phase 2D declaration:** None

---

## Purpose and separation from prediction registration

This document prospectively establishes collection conditions, comparison-source roles, scheduled testing, representative-state safeguards, deviation capture, artifact preservation, privacy and missing-result rules for the November snapshot. It precedes and does not itself constitute a registration of the proposed November Model Error records.

**The four proposed predictions 047–050 remain absent from the primary Model Error register at this stage.** A later atomic commit must append their OPEN rows and their exact evaluation plan together, before November outcome access. Numerical forecasts and their scoring thresholds are not locked by this collection-only plan. Until that later commit exists, conversation forecasts do not represent completed public preregistration.

This plan governs collection; the separately registered companion will govern formal scoring. Neither can silently modify protected earlier predictions, dictate training to obtain favorable results, or declare a phase.

### Governing repository material

- [August 2026 registered collection plan](2026-08-snapshot-collection-plan.md): established framework, not evidence that November has been performed.
- [Prediction-evaluation methodology](prediction_evaluation.md), [valid prediction criteria](../docs/methodology/valid_prediction_criteria.md), and [prediction-to-outcome pipeline](../docs/methodology/prediction_to_outcome_pipeline.md).
- [GOVERNANCE](../GOVERNANCE.md), [MEASUREMENT_SOURCES](../MEASUREMENT_SOURCES.md), [METHODOLOGY_AND_CONTROLS](../METHODOLOGY_AND_CONTROLS.md), and [PHASE_MAP](../PHASE_MAP.md).
- [Phase declaration criteria](../PHASE_DECLARATION_CRITERIA.md), [data-quality notes](../data/DATA_QUALITY_NOTES.md), and [privacy/sanitization methodology](anonymization.md).
- [August TruDiagnostic source-role reconciliation](../data/source_provenance/2026-08-trudiagnostic-reconciliation.md).
- A future evaluation companion, planned as methodology/open_prediction_evaluation_plan_047_050.md, must be created in the separate prediction-registration batch. It is NOT part of this initial collection-plan commit.

---

## Scheduled testing and actual-event boundary

All times below are the planned **local clock time at the relevant collection/test location**, not completed measurement timestamps.

| Date | Planned time | Test | Known booking/source state | Measurement role |
|---|---|---|---|---|
| Monday 2026-11-16 | 05:30 | TruAge and TruHealth sample collection | Kits ordered; self-collection intended, not yet completed | Molecular: proposed 047 DunedinPACE, 048 SymphonyAge if the applicable Advanced TruAge metric is actually supplied |
| Monday 2026-11-16 | 08:00 | DEXA plus laboratory VO₂max appointment | Scheduled and paid; order and separate start times unverified | Proposed 049 DEXA fat/lean mass; 050 measured relative VO₂max |
| Tuesday 2026-11-17 | 08:00 | Tanita body-composition assessment | Planned instead of unavailable Bod Pod; not yet completed | Supplemental only; not an interchangeable Bod Pod or DEXA reading |

The November molecular kit/report products must be verified. A TruAge/TruHealth order does not by itself confirm delivery of a November SymphonyAge result from Advanced TruAge. Retain absence as missing if that specific field is not reported.

DEXA and VO₂ occupy the 08:00 appointment **sequence**; this is not a claim that both tests start at 08:00 or that DEXA always precedes VO₂. Record actual sequence. November DEXA/VO₂ provider, device, software and modality must be confirmed rather than inferred from August's provider.

The intended November Bod Pod assessment was unavailable; Tanita is not a method-identical replacement. No November Bod Pod result may be inferred or entered.

Keep separate fields/dates for sample collection, shipment, provider receipt, laboratory processing, result-release date, report download, repository ingestion and later Model Error scoring.

---

## Existing evidence and comparison baselines

The baseline facts listed here were available **before** the November collection and are not November predictions or results.

| Future record | Domain | Reference observation | Evidence and comparability boundary |
|---|---|---|---|
| 047 | DunedinPACE | August 17, 2026: **0.77**; May: 0.79; February: 0.88 | [Epigenetic longitudinal data](../data/epigenetic_longitudinal.csv), [biomarker snapshot](../data/biomarker_snapshot.csv), archived provider reports; lower measured ratio is the favorable direction |
| 048 | SymphonyAge | August 17, 2026: **46.1 modeled years**; May: 37.8; February: 51.2 | Advanced TruAge provider output and structured data; a modeled clock is not directly observed chronological or organ age |
| 049 | DEXA | August 2026: **40.0 lb fat mass**, **185.3 lb provider-labeled lean mass** | Archived August DEXA reports and structured snapshot; verify provider field definitions and method equivalence |
| 050 | Relative VO₂max | May 11: **45 mL/kg/min**; August 17: **50 mL/kg/min** | Formal-test values in supplied provider-app screenshots; archived May/August provider VO₂ PDFs and checksum manifests exist, but their numerical contents were **not independently extracted in this registration review** |

The May and August formal VO₂ summary PDFs are preserved under snapshots/2026-05 and snapshots/2026-08 with SHA-256 checksum-manifest entries. Screenshot integers may be rounded. Before final scoring, read the complete provider reports and confirm test modality, protocol, precise VO₂ value, units, exertion/termination validity and bodyweight used for normalization.

For VO₂, distinguish measured **relative** output (mL/kg/min), **absolute** uptake (L/min when present), and test-day body mass. A higher relative value can partly reflect lower body mass without equal absolute oxygen-uptake improvement. A wearable VO₂ estimate or training heart-rate proxy may not replace a formal metabolic-cart measurement.

For DEXA, compare November and August only when sufficiently compatible in scan region, instrumentation/algorithm, provider metric definition and collection conditions. Total lean tissue on DEXA is not silently exchanged for another method's fat-free-mass or estimated muscle field.

For molecular clocks, preserve assay name, provider generation, units, reported precision, sample date and source metadata. Do not replace an absent SymphonyAge result with OMICm, a different age clock or a mean of system-level ages.

Provider source files control their reported measurements; a contemporaneous collection log controls actual sample/test timing and preparation when provider administrative metadata differ, as documented in the prior DQ-010 August reconciliation.

The specific November forecasts, pass/fail cutoffs, numerical scoring precision and insufficiency rules must be made immutable in the later 047–050 evaluation companion, before the future outcome is known.

---

## Representative-state objective and pre-2D boundary

The snapshot aims to capture the actual ordinary **Phase 2 Load Integration** state during the pre-2D training workup, not an artificially rested, lighter, heavier, dehydrated, glycogen-manipulated or performance-optimized presentation.

Continue independently governed B1 and LI activity with its actual scheduled standard, progression, technique/reduced-load and rest roles, unless safety or actual provider requirements demand otherwise. Do not create extra work to prove adaptation, skip sessions to optimize scores, add stimulants or supplements for testing, force a taper, modify diet for a leaner scan, or manufacture training debt from legitimate rest.

**Important August precedent:** The earlier 2026-08-16 LI session was intentionally omitted to preserve freshness for the August DEXA/VO₂ testing, not because the provider required it or recovery demanded it. That deviation activated a narrowly defined failure of registered Model Error 044. The November collection must preserve the distinction between a provider-required restriction, an ordinary scheduled rest, a recovery/safety decision and an elective outcome-optimization omission.

Medical safety and provider instructions **supersede the comparability aim**. Confirm test-specific restrictions on exercise, fasting, caffeine, food and medication from each provider. Follow their actual instructions and record the source, timing, affected training or intake and rationale. This file does not authorize a medication change, order exercise contrary to a medical restriction, or assume a particular provider requires a taper.

The pre-2D workup language describes a transition question, NOT a formal Phase 2D declaration. Snapshot success or prediction accuracy cannot automatically advance the phase under [phase declaration criteria](../PHASE_DECLARATION_CRITERIA.md).

### Prior 72 hours before November 16: contemporaneous context

Record dated, actual B1/LI duration, prescribed versus performed exercise dose, missed/modified sessions and why, rest and reduced-load roles, unusual physical work, recent soreness or fatigue, sleep and wearable recovery signals, heat/sauna, illness, travel, hydration, GI condition, medication/supplement deviations and ordinary meal timing.

Keep daily resting heart rate distinct from sleeping heart rate, and daily HRV distinct from overnight HRV. None of these supporting signals can be substituted into the four primary November measurement domains or used after the fact to move a forecast threshold.

---

## Pre-collection preparation and documentation

### Provider requirements and historical comparison

Follow each provider's actual preparation instructions, with safety paramount. Where compatible, preserve August's ordinary-state comparison aim: **approximately 10 or more hours fasted**, normally hydrated, ordinary sodium/carbohydrate/glycogen state, familiar sleep opportunity and absence of deliberate acute body-mass manipulation. The approximate fasting duration is an archival comparator, **not a blanket medical instruction**; a different provider requirement overrides it.

Do not intentionally water-load, dehydrate, salt-restrict/load, acutely carbohydrate-deplete/load, introduce unusual sauna exposure or alter normal supplements and training merely to improve the image, clock output or VO₂ result.

Document:
- final meal and fluid timing; materially unusual meal, caffeine or other exposure;
- actual fasting duration **at each separate molecular, DEXA, VO₂ and Tanita event**, not a single invented common duration;
- hydration context, illness, unusual sweating/edema and provider-imposed water restrictions;
- routine medications and supplements taken/omitted and why, without unnecessary public medication details;
- previous 72-hour training and ordinary manual work, including any provider-required reduction;
- sleep, wearable data completeness and subjective symptoms.

No isolated favorable or unfavorable wearable value automatically invalidates a valid provider test. Conversely, favorable training function does not establish recovery costlessness.

### Sleep and home waking weight

Use the ordinary morning-report and wearable schema the night before each test. Record bedtime/wake context, sleep duration, overnight HRV, sleeping HR, readiness, awakenings, subjective sleep/dream state and device-confidence limitations where available.

Record the home **waking** scale weight under ordinary conditions, including GI clearance and clothing state. Keep provider-facility DEXA/Tanita weight separate and do not infer tissue composition from an acute post-exercise scale change.

---

## Event capture: November 16

**All values in this section are pending; nothing below is a completed result.**

### Molecular collection

At collection record actual local time for each relevant kit, specimen/collection method and quality issues, final meal and morning fluid intake, fasting duration, shipping/receipt/processing dates and test/panel products. Retain tracking, specimen and accession numbers privately. Record whether Advanced TruAge/SymphonyAge is included and actually returned.

Preserve any conflicting provider header date separately from the dated contemporaneous collection record. Do not silently shift a sample to a provider administrative date or rewrite its biological outputs.

### DEXA

Capture actual start time, provider, manufacturer/model/software, scan settings/region, clothing and position, test-day weight, prior activity, fasting/hydration, movement/repeat scan flags, technical quality notes and official file/report identity. Preserve exact source units and labels of fat mass, lean mass and total mass.

### Formal VO₂ test

Capture actual start and DEXA order, provider and modality (treadmill/cycle), ramp/stages, gas-analysis instrumentation and calibration or provider-validity statements where supplied, duration, measured VO₂max in mL/kg/min, absolute L/min if available, bodyweight normalization, peak HR, respiratory exchange ratio or maximal-effort criteria, termination reason, symptoms, technical limitations and full provider report identity.

If November's formal protocol is materially noncomparable with August, retain the November result as an observation but do not force a same-protocol predictive score. The eventual locked 050 evaluation plan must say how to classify insufficient comparability; it cannot be invented at closure.

---

## Event capture: November 17

### Tanita supplemental test

Record actual time, provider/facility alias, model and software, impedance method/settings where shown, weight, body fat and muscle/fat-free output with exact labels/units, food/hydration/GI status, clothing, prior-day strenuous-test context and any quality notes.

Record **Bod Pod unavailable** as the reason for the changed testing modality. Tanita is not an equivalent Bod Pod method and cannot be used to resolve the primary DEXA prediction 049. There is no proposed 047–050 Tanita endpoint.

---

## Source hierarchy and privacy-preserving artifact workflow

For measurement outputs use the validated original provider report/direct export when available, ahead of an app screenshot, structured transcription or summary. Contemporaneous event notes control actual collection/fasting/training context; provider headers control what they display administratively. Preserve both when they differ and write a source reconciliation for a material conflict.

Preserve in this order:

1. Receive full source/provider reports; retain unmodified private originals where identification material exists.
2. Capture actual procedure times and deviations contemporaneously, not reconstructed from outcome.
3. Screen PDFs, images and metadata for date of birth, private address, phone/email, account/medical/billing IDs, specimen and tracking IDs, barcodes/QR codes, signatures and unrelated third parties.
4. Make visibly labeled sanitized public derivatives **only** when appropriate; review both visible pages and embedded content. Do not change measurements during redaction.
5. Hash the exact bytes retained or published, explicitly distinguishing a private original from a public derivative; register source identity appropriately.
6. Confirm metric, unit, date, provider definition and result validity; then transcribe into the appropriate November snapshot or longitudinal dataset.
7. Preserve favorable, adverse, discordant and absent results. Formal Model Error evaluation occurs separately after admissible evidence is complete.

A public Git branch is itself a disclosure surface. No private raw kit paperwork, shipping labels, accession numbers, unreviewed reports or private household data should be committed just to demonstrate provenance.

After actual collection, potential downstream structured files include November snapshot artifacts, checksum manifest, molecular longitudinal rows and biomarker snapshot rows. **None is created or populated by this preparation-only batch.**

---

## Outcome access and independent closure boundary

Before any November result is available, register all four exact forecasts and their evaluation rules together with open primary registry rows in a later commit. Date that commit at the actual registration time; do not backdate to this collection-plan date.

After a result becomes visible, preserve its timestamp and source. Do not revise the applicable prediction, threshold, comparator, precision, evaluation window or admissibility criteria. If only one report arrives, the remaining domains stay open and missing; no cross-domain favorable result can rescue another domain's failed prediction.

DunedinPACE and SymphonyAge are separate modeled endpoints but are not statistically independent assays. DEXA and relative VO₂ are separate performance/composition outcomes but can share body-mass dependency. Scoring is separate even when source and biological dependencies are correlated.

A missed test, provider-invalidated assay, insufficient/missing molecular panel, DEXA field omission, inadequate exercise-test validity or incompatible test method does not become a fabricated pass or failure. Record the event and retain the prediction open until the separately registered insufficiency/closure procedure permits a defensible outcome.

### Specific contingencies

- **Missed appointment:** retain planned date, reason, actual status and new date if any; do not invent values.
- **Late TruDiagnostic results:** retain sample date separately from result-release date; do not close from a partial portal preview.
- **Missing SymphonyAge:** do not substitute OMICm, other clocks or averaged organ ages.
- **Missing DEXA fat/lean component:** retain observed component(s) without Tanita substitution; use the locked conjunction/missingness logic later.
- **VO₂ not directly comparable:** retain reported number with protocol differences; do not assert calibrated improvement from unlike tests.
- **Invalidated test:** preserve provider notice/reason and clearly distinguish an invalid attempt from an unfavorable valid result.
- **Rescheduling or repeat testing:** preserve original appointment, new event date, provider, restrictions and exposure differences; do not silently choose the more favorable attempt.
- **Conflicting administrative dates:** preserve both provider metadata and contemporaneous test-date evidence.
- **Discordant outcomes:** report separately rather than forcing one overall biological success or narrative.

---

## Preparation checklist and future operations

- [ ] Confirm provider-specific collection/fasting/medication/activity instructions and verify the Advanced TruAge/SymphonyAge product field is expected.
- [ ] Confirm actual DEXA/VO₂ facility, scanner, lab modality and expected report formats; obtain information needed to evaluate protocol comparability with May and August.
- [ ] Independently inspect archived formal VO₂ provider reports for source-reported numeric values and precision; until verified, May 45 and August 50 retain provider-app screenshot source status.
- [ ] Confirm Tanita model and November 17 appointment; do not reclassify it as Bod Pod.
- [ ] Atomically create prospective 047–050 OPEN registry entries with their own fixed evaluation companion, BEFORE outcome access.
- [ ] Log ordinary preceding training, provider-required changes, meal/fasting/hydration and daily wearable context, without intervention for favorable scores.
- [ ] Record actual test times and order, validity/technical issues, missingness, completion and provider result dates.
- [ ] Preserve original sources privately as necessary; check sanitized derivatives and exact-byte checksums before any public upload.
- [ ] Independently evaluate each completed domain later using ONLY its pre-locked prediction/criteria.

### Historical, phase and release invariants

This groundwork does not modify existing Model Error 013–046 history or the protected 041–046 closed outcomes; UDI/concordance history; historical snapshot files; W41 Closed/W42 Active lifecycle; source quality issue DQ-011; Phase 2/lock-in declared state or Phase 2D criteria; training prescriptions; or the published v1.1.0 Git tag, version DOI and all-versions DOI.

**Initial prospective registration statement (2026-10-19):** The November collection schedule and evidence-processing rules are documented before outcomes. Four domain-specific predictions have been discussed but are NOT registered until their future evaluation companion and four exact OPEN registry rows are committed together. This document does not authorize outcome-driven data revisions, phase advancement, medical treatment changes or a new release.
