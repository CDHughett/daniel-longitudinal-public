# 2026-10-28 W42/W43 Post-Weekly-Rollover Integrated Integrity Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Baseline `main` commit:** `0ecf3e37e25314ad16c4fbb929f81fad72701011`  
**Working branch:** `w42-closeout-w43-rollover`  
**Batch 1 governed data/provenance commit:** `e74bcd94f1085be947c7b5403cfb258293eb9c6f`  
**Batch 2 report-lifecycle commit:** `2022f3a9b5e091954067322580954baa44ed3dd4`  
**Pre-audit Batch 3 / Batch 4 validated head:** `f51b43672bb852110ce1ad9d4a3cc3032b272946`  
**Audit date:** 2026-10-28  
**Audit status at preparation:** **PASS** for source/provenance, append-only preservation, metric reproduction, report lifecycle, current-state coherence, bounded disclosure, protected-governance invariants and the five validators at the *pre-audit* head. **The audit-and-changelog commit creates a new head and requires its own exact-SHA GitHub Actions pass before PR/merge review.**

---

## Scope and authority

This is a **selective credibility-relevant integrity checkpoint** under [audit inclusion criteria](README.md), not a routine training diary or a second biological report. W42 private-source ingestion, governed CSV data, public report closeout, W43 opening, and nine current-facing documents advanced together; that cross-layer change warrants a verifiable reconciliation record.

The audit covers:

- immutable identity of the exact supplied private `Daniel_Dataset_v1.36` source;
- the five governed append-only data/provenance files and comparison with their `main` historical prefixes;
- source-to-CSV numeric reconciliation, distinct sleep/HRV semantics, missingness and training-session enumeration;
- reproducibility of W42 structured weekly report metrics;
- prospective opening boundaries versus retrospectively observed LI variants;
- correct W42 Closed / W43 Active lifecycle and nine synchronized documents;
- context-event classification and material travel/rest distinctions;
- existing warning/data-quality limitations, protected prediction/phase/release identity;
- the actual five-validator GitHub Actions execution at the pre-audit head;
- privacy/publication scope, changed-file inventory and final exact-head gate.

**This audit tests reproducibility of the archive, not independent proof of completed mechanical repetitions, physiological causation, nutritional adequacy, clinically validated sleep architecture, a diagnosis or a formal Phase 2D transition.** Successful technical validation does not imply that all unmeasured scientific questions have been resolved.

---

## 1. Exact controlling private source

The retained uploaded workbook was inspected directly during the W42 rollover.

```text
Private source filename: Daniel_Dataset_v1.36
Source role:             private_workbook
Coverage:                2026-10-19 through 2026-10-25
Exact byte count:        375314
SHA-256:                 85d3025957071ae70a5186267b145dec43296f366c8255de793f8828625304e0
Manifest status:         registered
```

The exact identity is registered as the `v1.36` entry in `data/source_provenance/daniel_dataset_private_manifest.csv`. The manifest advanced **36 → 37 records**. This checksum is for the exact retained workbook bytes, not for a reconstructed file, a newly exported workbook or a historical estimate. No raw workbook or entire private operator narrative was published.

The public daily, sleep, training and event records are curated evidence-bearing representations. In the source workbook, mixed Excel date/serial forms required normalization to supported ISO dates. The normalization is a date-index conversion; it is **not** authorization to invent missing measurements or change values to match a preferred outcome. Public `source_ref` locators and the manifest permit audit back to the controlled private source without disclosing its bytes.

Internal `2026-W42` denotes the repository's established weekly reporting sequence for **October 19–25, 2026**. That period is **ISO 2026-W43**. The internal index is retained and documented; automated external comparisons must not silently assume the two labels are identical. W43 in the internal archive begins October 26.

---

## 2. Exact append-only historical preservation

An independent comparison of the five governed text files on `main` against the pre-audit branch confirmed that each prior file's **entire original content is a byte-for-byte unchanged prefix** of its new version. CSV header rows were identical; all appended rows retained the existing column widths.

| Governed file | Prior rows | Appended | New rows | Last represented date / identity |
|---|---:|---:|---:|---|
| `data/daily_biomarkers_v1.csv` | 252 | 7 | **259** | 2026-10-25 |
| `data/sleep_longitudinal_v1.csv` | 252 | 7 | **259** | 2026-10-25 |
| `data/training_blocks_v1.csv` | 409 | 10 | **419** | 2026-10-24 |
| `data/context_events_v1.csv` | 53 | 2 | **55** | 2026-10-25 |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | 36 | 1 | **37** | v1.36 |

**Total appended governed records: 27. Deleted historical CSV lines: zero.**

Daily biomarkers and canonical sleep represent all seven dates October 19–25, in strictly increasing order. Completed training is session-indexed rather than day-indexed. There were **six genuine B1** and **four genuine LI** records. October 23's LI rest, October 24's omitted LI and October 25's omitted B1 and LI were **not converted into synthetic training sessions**. Consequently, training properly stops on October 24 while daily/sleep/context data extend to October 25.

The original 325-session training prefix through August 30 retains its independently protected historical identity. No historical training row, pre-existing context event, closed report or source manifest entry was rewritten to create apparent completeness.

---

## 3. Independent source-to-public reconciliation

The audit compared **94 individual source-grounded values** across the newly appended daily, sleep and completed-training observations:

- 35 daily-value checks: seven waking weight/HRV/resting HR/daily average HR/temperature positions, with missing October 25 weight respected;
- 49 sleep-value checks: seven nights of total sleep, REM, deep, light, awakening count, overnight HRV and sleeping HR;
- 10 completed-session checks: day, type and logged duration for each completed B1 or LI session.

**Result: 94 of 94 comparisons matched.** Seven sleep-stage duration totals and seven corresponding REM/deep/light percentage triples were independently recomputed and also matched the governed sleep rows. CSV structural validation separately reported zero machine-readable errors and warnings.

These checks verify transcription and arithmetic within the recorded source definitions. They do not independently validate the accuracy of consumer wearables or an operator's set-by-set physical performance.

---

## 4. Independent W42 metric reproduction

The latest-weekly-rollover validator independently derives the structured W42 metric table from the committed public CSVs, while manual independent arithmetic produced the following:

| Metric | Reproduced W42 value | Interpretation boundary |
|---|---:|---|
| Standardized morning bodyweight | **226.3 lb** | Six measured mornings; October 25 missing/no scale |
| Daily Biomarkers HRV | **74.7 ms** | Daily series, different from overnight HRV |
| Daily resting heart rate | **44.6 bpm** | Seven-day mean |
| Daily average heart rate | **58.4 bpm** | Seven-day mean |
| Overnight Sleep Log HRV | **76.6 ms** | Separate seven-night series |
| Average sleeping heart rate | **47.7 bpm** | Separate from daily resting HR |
| Mean total sleep | **7h58m** | 3344 minutes/7; final night 616 minutes |
| Mean estimated deep sleep | **1h42m** | Consumer stage estimate |
| Mean estimated REM sleep | **1h04m** | Consumer stage estimate, low confidence on six nights |
| B1 sessions | **6** | 330 minutes / 18.12 recorded miles |
| LI sessions | **4** | 180 minutes |
| Total formal training | **510 minutes** | 10 real completed sessions |

W41's corresponding formal training total was 670 minutes, making W42 lower by **160 minutes (23.9%)**. This is a reduction in registered **exposure**, materially affected by scheduled recovery and travel; it is not proof that exercise capacity declined.

Seven nightly total-sleep values were **519, 457, 443, 447, 450, 412, 616 minutes**. The W42 mean rounds to 7h58m, but the median is **7h30m** and the first six nights average approximately 7h35m. The final 10h16m estimate occurred with reported fragmentation in an uncomfortable treehouse environment. Mean duration alone is not evidence of uniformly improved subjective sleep quality.

Waking-weight values were **225.7, 226.7, 225.3, 226.0, 227.0 and 227.0 lb**, with no value on October 25. Post-B1 scale readings are under different exercise/GI conditions and were **not** merged into the standardized waking-weight average or interpreted as tissue-mass change.

Daily Biomarkers HRV values were **78, 79, 65, 71, 74, 63, 93 ms**. The final 93 ms materially influences the weekly 74.7 ms mean; the preceding six average approximately **71.7 ms**. Overnight Sleep Log HRV values were **88, 78, 72, 72, 74, 72, 80 ms**, mean 76.6 ms. These streams are not interchangeably sourced or averaged as one series. The October 25 separately reported evening HRV value and the historical DQ-011 question were **not silently corrected** from those two public series.

The wearable sleeping-heart-rate sequence **48, 57, 47, 45, 46, 45, 46 bpm** averages 47.7 bpm. October 20's transient elevated period remains visible. The data do not identify its cause or justify treating the lower mean versus W41 as proof of load adaptation in a week with fewer LI exposures.

---

## 5. Progression evidence versus prospective registration

The original active W42 report asked whether expanded LI work would remain reproducible without unobserved recovery cost. The closed report **retains the original starting-state and observation-priority material**, labels those passages as preserved opening context and separately documents actual outcomes. The original prospective question also remains inspectable in the prior Git revision.

The completed sessions included:

- **October 19, Pull / Press Intensity:** weighted strict pull-ups **4×4 at +10 lb**, feet-elevated push-ups **3×10**, chest-supported rows **3×10**; operator reported completed work with limited moments of additional attention.
- **October 20, Standard LI:** familiar 3×5 trap bar / 4×4 unweighted pull-ups / 3×10 push-ups / 3×30-second hangs, reported easy.
- **October 21, Technique / Reduced Load:** lower-dose trap-bar, pulling, pressing and hanging work, performed with deliberate slower control and reported ease.
- **October 22, Higher-Load LI:** trap bar **3×5 with a prescribed 2.5–5% working-load increase**, baseline pulling/pressing and **3×45-second hangs**, with pronounced perceived grip automaticity.

The numeric trap-bar working mass was **not independently registered**, and exact repetition/technique fidelity is not externally verified. W41's 5×5 unweighted pulling is not an identical dose to W42's 4×4 weighted pulling. Fewer trap-bar repetitions with a higher intended load cannot be classified as a precise workload change without actual mass and execution measurements.

No prospective Model Error record, protocol declaration or phase transition is backdated from these retrospective exposures. Subjective movement economy and grip automaticity are distinct from measured maximal strength, mechanical reserve and tissue-adaptation proof.

---

## 6. Event classification and travel boundary

Exactly two source-grounded events were appended:

| Event ID | Window | Public interpretation |
|---|---|---|
| `2026-10-19-01` | October 19–22 | Material differentiated LI loading and movement variation, retrospectively documented |
| `2026-10-24-01` | October 24–25 | Airbnb-related LI-only then B1-plus-LI interruption, with environmental sleep disruption |

No separate event was manufactured for each routine workout, for a normal rest boundary or for each wearable fluctuation. The event layer is a bounded perturbation/protocol-context index, **not** a continuous daily diary.

October 23 was a **scheduled resistance-training rest day** during which B1 remained completed. October 24 retained B1 and omitted LI for travel logistics. October 25 contained neither completed formal component. There is no recorded compensatory training debt or requirement to restore the missed weekly total.

Recorded W42 ordinary movement was **79,110 steps and 594 active minutes** from the private operator record. Wearable activity calories, steps and active minutes provide context, not a calibrated dose equivalence with externally loaded resistance work.

---

## 7. Report lifecycle and nine-surface synchronization

The branch currently contains:

- `reports/2026-W42.md` — **Closed**, October 19–25, retrospective descriptor **selective continuity**.
- `reports/2026-W43.md` — **Active**, October 26–November 1, weekly posture **Post-travel return / lumbar movement-tolerance observation**.

The windows are contiguous and seven days each. There is one newest active report, and the latest closed report is immediately prior. The internal week labels have the established non-ISO offset and are documented as such.

Nine public current-facing paths have been synchronized:

```text
README.md
LATEST.md
INDEX.md
docs/START_HERE.md
docs/CONCEPTS.md
docs/OBSERVER_QUICKSTART.md
docs/NEWCOMER_PATH.md
data/DATA_COVERAGE.md
CHANGELOG.md
```

All active/closed navigation pointers, exact weekly operating-posture strings, structured row counts and coverage endpoints were checked. A stale canonical sleep interval in `data/DATA_COVERAGE.md` was discovered and fixed **before Batch 3 was committed**, without changing the source CSVs or validators. Current public daily/sleep end date is October 25; completed training ends October 24; the bounded event index ends October 25.

W43 contains already-known October 26–27 operator reports of lumbar stiffness, position restriction and unusually costly hinge execution, distinguished from comparatively preserved pulling/grip. Those observations are **not** W42 symptoms, not retroactively preregistered predictions and not proof of any causal mechanism. No W43 data were appended during the W42 closed-window rollover; the current validator prohibits premature completed-session rows beyond October 25.

---

## 8. Exact five-validator execution on the pre-audit head

The pre-audit branch head was:

```text
f51b43672bb852110ce1ad9d4a3cc3032b272946
```

GitHub Actions ran the existing `.github/workflows/validate.yml` as a branch **push** event, with checkout of exactly that SHA.

```text
Workflow name:    Repository validation
Workflow run:     40680373055
Workflow URL:     https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/40680373055
Job ID:           122789284963
Event:            push
Status:           completed
Conclusion:       success
Head SHA:         f51b43672bb852110ce1ad9d4a3cc3032b272946
```

Actual job steps and decoded logs were inspected, not merely inferred from the green status:

| Existing validator command | Verified outcome |
|---|---|
| `python tools/validate_repository.py` | **PASS** — ten core passes, zero errors; two known historical sleep warnings |
| `python tools/validate_machine_readable.py` | **PASS** — zero errors, zero warnings |
| `python tools/validate_weekly_rollover.py` | **PASS** — W43 Active, W42 Closed, v1.36 matched to closed interval and metrics |
| `python tools/validate_august_snapshot.py` | **PASS** — protected August artifacts and Record 043 alignment intact |
| `python tools/validate_coherence.py` | **PASS** — W43/W42 pointers, current posture, row counts and release identity coherent |

Two pre-existing core warnings remain:

1. Governed sleep-stage total differences on **2026-03-31 (+16 min)** and **2026-04-02 (+14 min)**.
2. Historical **DQ-001 awake/awakening duplication** on 14 dates.

They were not new W42 additions, and no unreviewed correction was made. W42's seven added sleep stage totals and their calculated percentages were independently checked against the governed source values. The validation suite and its workflow definitions were **not edited** to achieve success.

**This run is conclusive for pre-audit commit `f51b436...`, not for the new audit-bearing commit.** A new exact-head CI check is required after this document and the changelog annotation are committed.

---

## 9. Protected science/governance and frozen release identity

A complete recursive Git tree comparison between baseline `main` and pre-audit branch was not truncated. It identified exactly 16 expected changed paths and **zero unexpected paths**. In particular, **35 protected files** across phase/governance, Model Error, snapshot, source, workflow, DQ and publication categories retained **identical Git blob identities**.

Protected interpretation and prediction state:

- Declared phase: **Phase 2 — Load Integration**. Broader Phase 2 substate: **Consolidation / lock-in observation**. Formal Phase 2D remains **undeclared**.
- Model Error records **041–046 remain closed**. Record **043** retains its **not supported / `overall_improvement_not_met` / `over`** adjudication; no historical scoring is altered.
- Prospectively locked November Model Error records **047–050 remain Open**, with forecasts, registered dates, evaluation rules and outcome/error missingness unchanged. No W42 observation is counted as a November outcome.
- **DQ-011 remains open** for the separate 2026-09-08 resting-heart-rate provenance question. W42 contains no authoritative correction for it.
- August source artifacts, snapshot cross-layer interpretation, independent provider provenance, and the 2026-09-18 supplementation context were not rewritten.

Frozen public release identity:

```text
Published version:      v1.1.0
Frozen release commit:  92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
Version DOI:            10.5281/zenodo.22759132
All-versions DOI:       10.5281/zenodo.20815611
```

This weekly update is an ongoing-archive update, **not** a new publication, tag, DOI release, scoring event or formal protocol/phase change.

---

## 10. Privacy and public-distribution scope

The 16 pre-audit changed paths were exactly: five governed data/provenance files, two weekly reports and nine current-facing documentation/changelog files. This audit adds one markdown document and a changelog annotation; no source workbook, raw private-provider export, full private narrative or independent private household file has been added.

The six principal public data/report files were screened for recognizable email addresses, phone numbers, credential-token patterns and the exact private narrative title; **no matches were found**. That limited pattern screening is not a guarantee of anonymity, absence of all sensitive details or universal privacy approval.

The published W43 report **does** include bounded operator-reported lumbar symptoms and exercise-specific limitations. That is an intentional public observation-layer disclosure inside the established study architecture. Reviewers should separately confirm that the chosen disclosure is within the user's intended public scope before final merge. Symptom text contains no independently established diagnosis or causal assignment.

The SHA-256, source filename and private-workbook row locators expose provenance identity without publishing the underlying private source bytes. Review of the complete diff found no unexpected private binary or operator-narrative artifact paths.

---

## 11. Findings and remaining limitations

**Integrity findings: PASS.** The exact retained v1.36 source is registered; the original five governed-file prefixes are unchanged; 27 source-grounded records append with correct units/date windows; 94 value comparisons, seven sleep-stage totals and seven stage-percentage checks match; W42's twelve weekly structured markers reproduce; travel/rest missingness is represented without fake sessions; current state is synchronized; the protected 35-file set retains identical blob identities; and all five pre-audit validators completed successfully on the exact documented commit.

**Scientific and operational limits remain open:** numeric trap-bar working weights and independently witnessed repetition fidelity, sustainable mechanical load after interruption, significance of nocturnal excursions, low-confidence wearable REM, physiological cost of the expanded prescriptions, and measured protein/energy availability. The final W42 day had no completed exercise-performance test. W43's subsequent lumbar report demands new movement-specific observation; it cannot be backdated as W42 discomfort or assigned a verified travel/hinge mechanism.

The original weekly question is preserved separately from the retrospective answer. **Selective continuity** is an interpretive descriptor supported by the execution/rest/travel sequence, not a claim that full-dose post-travel retention was proved.

No new source-grounded W42 inconsistency justified changes to the historical data, protected prediction register, validators or frozen release.

---

## 12. Publication decision and exact final-head gate

**Provisional verdict: INTEGRITY PASS for the pre-audit branch head. Recommendation: CONDITIONAL GO to final-head CI and PR review only. No authorization to merge yet.**

The combined audit-and-changelog change is a new commit and must meet all gates independently:

1. Commit this audit and the corresponding changelog annotation on `w42-closeout-w43-rollover`.
2. Obtain the new commit's **exact SHA** from the live branch.
3. Observe a completed GitHub Actions run on that exact SHA with all five unmodified Python validators successful.
4. Verify the final diff against baseline `main` contains only the originally approved 16 rollover paths, this audit, and no unexpected files. Changelog remains one of the original nine paths.
5. Confirm no protected scientific, governance, phase, model-error, prediction, DQ, release/tag/DOI or source-export artifact was changed.
6. Review any public disclosure concerns before PR approval. Open/merge a reviewed PR only after the prior gates pass.
7. After merge, verify the resulting `main` commit, navigation and the post-merge GitHub Actions result; do not claim a new DOI/release.

At the time this document was authored, **only the pre-audit head's five-validator success is verified**. An automatic CI run triggered by committing this audit cannot be pre-claimed. This audit is **not** an instruction to merge, issue a release, alter a forecast, declare Phase 2D or treat exercise completion as medical clearance.
