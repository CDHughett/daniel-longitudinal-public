# 2026-10-19 November Model Error 047–050 Prospective Registration Audit

**Repository:** CDHughett/daniel-longitudinal-public  
**Working branch:** \`w42-model-error-rollover\`  
**Baseline \`main\` commit:** \`2af0ab9d824e822047ae3a4a64cf6d55d09b9626\`  
**Batch 1 collection-governance commit:** \`26fee040594025ef74fe1ea5735e7a3e5d597fe0\`  
**Batch 2 atomic registration commit:** \`36936f042e2a37a011efe18e7ffda7fc2ee3c22a\`  
**Batch 3 public-documentation commit:** \`0a68b964d728b41241f60113919dc1fe29f9c354\`  
**Audit date:** 2026-10-19 local registration day  
**Audit standing at document preparation:** **Pre-audit integrity PASS; final audit-commit GitHub Actions run required separately**

---

## Why this selective audit is warranted

The primary prospective Model Error registry, its locked scoring companion, validation safeguards and nine current-facing public navigation/governance surfaces have changed in one registration initiative. This is a credibility-relevant **model-error and methodology** checkpoint under [the repository's audit inclusion criteria](README.md), not a routine weekly report or a finding that a prediction is already supported.

This audit examines chronological registration, historical exact-prefix integrity, all four independently scorable forecasts, endpoint provenance and precision, missing/invalid result behavior, privacy, unchanged UDI/concordance and scientific phase boundaries, protected publication assets and pre-audit CI. The scientific outcomes remain unknown. Passing a repository validator is evidence of mechanical integrity, **not** evidence that any forecast is likely, physiologically causal, or clinically meaningful.

---

## 1. Prospective commit ordering, date and lock boundary

Verified live Git commit ancestry and UTC commit metadata:

| Sequence | Git commit | UTC timestamp | Governing role |
|---|---|---|---|
| Existing published \`main\` | \`2af0ab9d824e822047ae3a4a64cf6d55d09b9626\` | prior baseline | No November registration |
| Batch 1 | \`26fee040594025ef74fe1ea5735e7a3e5d597fe0\` | 2026-10-20 00:06:22Z | Collection, preparation, provider and missingness governance |
| Batch 2 | \`36936f042e2a37a011efe18e7ffda7fc2ee3c22a\` | 2026-10-20 00:17:07Z | Four registry rows **and** exact scoring companion in one atomic commit; validator hardening |
| Batch 3 | \`0a68b964d728b41241f60113919dc1fe29f9c354\` | 2026-10-20 00:23:43Z | Public status/documentation sync |

All three timestamps correspond to **October 19 evening at UTC−04:00**, consistent with the v1 registry's \`date=2026-10-19\`; they are not attempts to represent a November test as already completed. The actual batch-2 Git commit, not a conversation, is the immutable registered prediction boundary. The collection plan at batch 1 correctly states **047–050 were not yet registered at its original commit**. No November 16 outcome existed at this point.

A prospective registration can only be shown to precede *future results* by preserving these records and later comparing outcome-access timestamps; this audit cannot attest in advance to the accuracy or validity of November results.

---

## 2. Exactly preserved Model Error historical registry

Compared the full current \`data/model_error/model_error_gap_v1.csv\` against the exact \`main\` baseline version, rather than sampling recent lines.

| Property | Baseline | Registered branch | Result |
|---|---:|---:|---|
| Header schema | 15 fields | Same 15 fields | Unchanged |
| Total data records | 34 | 38 | Four appended |
| Historical IDs | 013–046 | 013–046 unchanged | Exact byte-for-byte preserved prefix |
| New IDs | None | 047–050 | Exactly four unique contiguous IDs |
| New statuses | — | All \`open\` | Correct |
| New provenance | — | All \`pre\` | Correct |
| New outcome/error cells | — | All four fields blank per record | Correct |

All four additions are marked \`flag=primary\`, \`model_type=subject_calibrated\`, \`model_version=gpt6-subject-calibrated\` and \`date=2026-10-19\`. The v1 \`calibration_state=pre\` field means prospectively registered before outcome access, **not** an uncalibrated model type and **not** an open/closed status. It remains \`pre\` after eventual closure.

The existing closed 041–046 adjudications and their original \`Prediction:\` narrative prefixes are preserved; Record 043 remains **not supported / \`overall_improvement_not_met\` / \`over\`**. Earlier retrospectively reconstructed prediction history remains separate.

---

## 3. Exact registered forecast and locked evaluation match

All four v1 \`notes\` fields matched the corresponding **exact original forecast text** in \`methodology/open_prediction_evaluation_plan_047_050.md\`, not merely the same numerical thresholds.

| ID | v1 type / value | Full locked condition and admissible November domain | Audit result |
|---|---|---|---|
| **047** | \`point / 0.76\` | November 16 TruAge sample yields provider-reported **DunedinPACE 0.76** | Registered; no outcome |
| **048** | \`range / 40.0-44.0\` | Advanced TruAge **SymphonyAge 40.0–44.0 modeled years**, inclusive | Registered; no outcome |
| **049** | \`state / 1\` | November 16 comparable **DEXA fat mass ≤36.0 lb AND provider-defined lean mass ≥183.0 lb** | Registered; no outcome |
| **050** | \`state / 1\` | November 16 comparable **formal relative VO₂max ≥52.0 mL/kg/min** | Registered; no outcome |

For 049 and 050, stored \`prediction_value=1\` is the predicted **binary state**, not the numeric fat/lean or relative-VO₂ field; those values are frozen within the exact note text and scoring companion. The four targets have separate closure and failure rules. A successful aerobic or DEXA result cannot rescue a failed methylation-clock prediction or vice versa.

The exact registered evaluation companion's Git-blob identity is:

\`\`\`text
8513ec37bd145f8b5304483bb71bb5219947efee
\`\`\`

The core repository validator checks that blob's entire byte identity, not just cherry-picked words, and separately hard-codes the original note narratives and registration fields. The validator requires all four records to remain \`open\` with blank outcome/error columns until a **separate, openly governed future closure**; it does not confer a future outcome result.

---

## 4. Independent scoring-boundary probes

These are **synthetic examples** used to test the semantics of the locked plan, **not November measurements** and not new prediction outcomes.

| Record | Synthetic example | Correct classification under prelocked rules |
|---|---|---|
| 047 | DunedinPACE \`0.760\` | Exact numeric point, zero absolute error |
| 047 | \`0.755\` | Point error \`0.005\`; direction \`over\` (observed lower than predicted) |
| 047 | \`0.800\` | Point error \`0.040\`; direction \`under\` (observed higher than predicted) |
| 048 | SymphonyAge \`40.0\` or \`44.0\` | Inside **inclusive** interval |
| 048 | \`39.9\` | Miss below range; direction \`over\`, not “supported because more favorable” |
| 048 | \`44.1\` | Miss above range; direction \`under\` |
| 049 | Fat \`35\`, lean \`184\` | Conjunctive state true, binary actual \`1\` |
| 049 | Fat \`37\`, lean \`184\` | False; failure of either condition suffices |
| 049 | Fat \`35\`, lean missing | **Insufficient**, not success |
| 049 | Fat missing, valid lean \`182\` | False if source/method admissible: one confirmed failing conjunct is enough |
| 050 | Full report \`51.6\`, app card rounded to \`52\` | False; full authenticated report has priority |
| 050 | Full report \`52.0\` | True if protocol/provider validity and comparability hold |

For 047 the reported precision is retained; neither an apparently near hit nor an unexpectedly favorable miss is reclassified post hoc. For 048, distance outside the relevant interval boundary—not an invented after-the-fact midpoint—governs interval-error magnitude. 049 and 050 retain binary state/concordance semantics rather than falsely entering continuous magnitude UDI.

These conceptual probes confirm that the locked companion's described rules are internally intelligible. They do **not** substitute for future original-source-based scoring or independently prove validator mutation resistance under arbitrary adversarial edits.

---

## 5. Historical source-basis and unresolved admissibility conditions

Independently read governed \`data/biomarker_snapshot.csv\` and \`data/epigenetic_longitudinal.csv\`, confirming:

| Domain | February 2026 | May 2026 | August 2026 | November eligibility condition |
|---|---:|---:|---:|---|
| DunedinPACE | 0.88 | 0.79 | **0.77** | November same-named TruAge output |
| SymphonyAge | 51.2 years | 37.8 | **46.1** | November **Advanced TruAge SymphonyAge** field actually supplied |
| DEXA fat mass | 33.2 lb | 35.3 lb | **40.0 lb** | Matched provider definition / valid scan |
| DEXA lean mass | 183.0 lb | 184.9 lb | **185.3 lb** | Matched provider definition / valid scan |
| Formal relative VO₂max | Not part of current structured snapshot | **45 shown in provider-app screenshot** | **50 shown in provider-app screenshot** | Full provider report, method and precision verification |

VO₂ numerical baseline limitation: exact source names \`snapshots/2026-05/2026-05-vo2-summary.pdf\` and \`snapshots/2026-08/2026-08-vo2-summary.pdf\` exist; their May/August SHA-256 manifest entries are \`6a96fa1880eff1582d015eeed4b1cff02fad74b9f3dc16e80d87689534e88e37\` and \`f6dd377ddd6537e530e86373ea096c0ea4895898e38156f32d73c985fac7bb2a\` respectively. **The numbers 45 and 50 are evidenced in user-supplied app screenshots and have not yet been independently extracted and compared from those PDF bytes through this GitHub interface.** The audit does not upgrade app-display source fidelity into a verified full-report precision claim.

Provider test/report domain rules are fixed before outcome availability. Specific remaining admissibility work includes:
- Confirm whether the ordered November TruAge/TruHealth products return a SymphonyAge field from **Advanced TruAge**, not a substituted clock.
- Retain provider model/version and method comparability for both molecular outputs.
- Match DEXA field definitions, scanner/software where relevant, fasting/hydration conditions and scan quality; don't substitute November Tanita.
- Match VO₂ formal testing method, protocol/validity, exact numeric precision, normalized mass and absolute uptake if available; relative gain may partly reflect lower body mass.
- Differentiate **November 16, 05:30** intended TruAge/TruHealth collection and **November 16, 08:00** DEXA/VO₂ appointment sequence; preserve actual execution times rather than assume both procedures began at 08:00.
- Record **November 17, 08:00 Tanita** as supplemental, not a November Bod Pod procedure or primary 049 endpoint.
- Distinguish provider-required medical/test preparation from discretionary result-optimization/tapering. August's test-directed LI omission and Model Error 044 outcome remain historical and unchanged.
- Log missing, late, invalid, repeated or rescheduled tests without choosing a favorable replacement after results are visible.

These are scientifically substantive **source limits and upcoming evidence gates**, not identified current registration-integrity failures. They must remain visible to external reviewers. A forecast may remain open when an admissible score cannot be justified.

---

## 6. Scientific governance and permissible interpretation

The forecasts test four separately resolvable measurements, not a collective assertion that a training system caused biological age reversal, recomposition or improved peak aerobic oxygen uptake. The historical August Model Error 043 outcome remains unchanged despite favorable DunedinPACE history.

Potential dependencies are disclosed:
- 047 and 048 derive from related DNA-methylation/provider modeling rather than independent biological experiments.
- 049 and 050 both depend in part on total body mass and its measurement conditions.
- Bodyweight, hydration and DEXA lean-mass estimation may be confounded by fluid/glycogen state.
- Model Error numerical scores describe **forecast error**, not physiological effect size or clinical significance.

Opening a model-error record does not order additional exercise, compel testing under unsafe conditions, override provider preparation, change the currently registered LI training regime, or declare Phase 2D. The phase remains **Phase 2 — Load Integration**, with broader **Consolidation / lock-in observation**. The weekly lifecycle remains **2026-W41 Closed / 2026-W42 Active**.

No new 051 autonomic prediction was created. No November snapshot, provider-derived new biomarker row, closure or UDI/concordance recomputation was performed.

---

## 7. File inventory and immutable-protection checks

The complete branch comparison before this audit showed **three commits ahead of \`main\`**, zero behind, and exactly **13 intended changed file paths**:

- **2 new methodology files:** November collection plan and locked 047–050 evaluation plan.
- **1 append-only registry file:** \`data/model_error/model_error_gap_v1.csv\`.
- **1 core validator update:** \`tools/validate_repository_core.py\`.
- **9 synchronized documentation and governance files:** README, LATEST, INDEX, \`data/model_error/README.md\`, \`methodology/README.md\`, GOVERNANCE, observer quickstart, newcomer path and CHANGELOG.

No private raw PDF, workbook, personal kit screenshot, identity-bearing provider document, specimen identifier or November result artifact is introduced by this branch. All newly changed text files were screened for ordinary email, phone, Social Security number and private absolute-path patterns; **none were detected**. This is a bounded check, not a promise of universal anonymity in a public N-of-1 archive.

Comparing Git blob IDs at baseline and branch head found these protected files **identical**:

- \`PHASE_MAP.md\` and \`PHASE_DECLARATION_CRITERIA.md\`;
- \`CITATION.cff\`, \`CODEMETA.json\`, \`VERSIONING.md\` and \`.github/workflows/validate.yml\`;
- \`data/model_error/record_043_closure.md\`, \`data/model_error/udi_by_type_tracker.csv\`, \`data/model_error/calibration_events_log.md\`;
- \`data/biomarker_snapshot.csv\`, \`data/epigenetic_longitudinal.csv\`, \`data/DATA_QUALITY_NOTES.md\`;
- \`reports/2026-W41.md\` and \`reports/2026-W42.md\`.

The published **v1.1.0** tag continues to reference frozen commit \`92126e1cc882c3822d9e03b30b11cfc1d30b4fbb\`, and the latest published release remains v1.1.0. Neither \`10.5281/zenodo.22759132\` nor \`10.5281/zenodo.20815611\` is changed, reassigned or newly published.

---

## 8. Pre-audit five-validator result and final-head rule

Verified pre-audit branch-head GitHub Actions run:

- **Run:** [39347390100](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/39347390100).
- **Head:** \`0a68b964d728b41241f60113919dc1fe29f9c354\`.
- **Status:** completed, success.
- **All five original steps passed:** core repository; machine-readable semantic layer; latest weekly rollover; August snapshot cross-layer; post-release coherence.
- The validation script inventory and workflow triggers were **not** weakened.

The audit record itself will be a new Git commit. Therefore this prior five-validator success **cannot** be presented as the result for the final audited commit. The exact GitHub Actions run with \`head_sha\` equal to the **post-audit** commit must independently pass all five checks before this batch is complete or PR publication work begins.

---

## 9. Findings, publication posture and next steps

**Registration-integrity findings: PASS.** All four intended forecasts were atomically registered, have immutable source-and-scoring narratives matching the companion, preserve the full prior prediction registry, remain unscored, and are discoverable from synchronized public-facing documentation. The preparation-governance document precedes the formal registration, with correct local-date versus UTC commit interpretation.

**Evidence limitations retained:** SymphonyAge's presence in the actual November kit/report is not yet verified; August formal VO₂ provider-PDF quantitative comparison is pending; November scanner/gas-testing protocol and result validity are not yet established; measuring a biomarker does not independently prove physiological mechanism. These conditions must not become a post hoc excuse to discard an otherwise admissible unfavorable result.

**No current defect was found requiring a change to the locked forecast, historical outcomes, validator assertions, or collection plan.** Accordingly the audit should add only this retrospective integrity document and a narrow prospective-registration changelog annotation.

**Provisional verdict: PASS, conditional on an exact final-audit-head five-validator GitHub Actions SUCCESS.** Once this condition is met, Batch 4 may close and the branch may proceed to the separately authorized Batch 5 PR/merge checks. This audit does not open a PR, merge to main, score an outcome, register 051, change a release, create a DOI, or declare Phase 2D.
