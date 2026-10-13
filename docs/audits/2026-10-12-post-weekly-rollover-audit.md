# 2026-10-12 W40/W41 Post-Weekly-Rollover and Integrated Coherence Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Baseline `main`:** `8aa928bc7e418d72a8f864ca0e4b2f15b1f9544f`  
**Rollover branch:** `w40-closeout-w41-rollover`  
**Batch 3 head:** `d0a9ee478963dc19099993297cebd49b75be6778`  
**Pre-audit validation head:** `fe4e842bf8d07c40c3b81a5d0f59b18778417724`  
**Audit date:** 2026-10-12 (rollover date; validation ran 2026-10-13 UTC)  
**Verdict:** **GO to PR preparation only after final audited-head GitHub Actions PASS.** This document records a green five-validator pre-audit head; adding the audit and changelog entries creates a new head that must itself be checked before release review.

---

## Scope and authority

This audit examines the completed W40 (2026-10-05 through 2026-10-11) data ingest, retrospective report closeout, and active W41 (2026-10-12 through 2026-10-18) initialization. It evaluates:

- source identity and source-role boundaries;
- exact append-only preservation of existing machine-readable records;
- time/date continuity, missingness and session-based training semantics;
- mechanical reproduction of closed-week calculations from public structured data;
- evidence versus interpretation for the midweek Load Integration progression;
- sleep and bodyweight measurement-context distinctions;
- report lifecycle, operating posture and cross-document synchronization;
- bounded event indexing and retrospective protocol documentation;
- privacy, governance, model-error, phase and frozen-release constraints;
- all five repository validators, observed failures, correction, and the final-head CI requirement.

The audit does not establish physiological causation, clinical outcomes, a prospective prediction, a maximal capacity result, nutritional sufficiency, or a formal Phase 2D declaration.

---

## 1. Controlling private source and exact identity

The private workbook used for W40 extraction is:

```text
Filename:         Daniel_Dataset_v1.34
Coverage:         2026-10-05 through 2026-10-11
File size:        369,524 bytes
SHA-256:          dc2171850bade2a929108dc39bdadaac0672209b784c6341664004b46ab54ff7
Manifest status:  registered
```

The SHA-256 above was verified against the latest retained uploaded file bytes, not reconstructed from the public CSV. Its exact identity is registered in `data/source_provenance/daniel_dataset_private_manifest.csv`. Row-level provenance uses canonical `private_workbook:Daniel_Dataset_v1.34:...` locators. Date cells with mixed source encodings were normalized into ISO calendar dates in curated public rows without changing earlier records. Canonical sleep remains a separately governed curation of the private Sleep Log and wearable/operator evidence, not a raw RingConn provider export.

The private workbook and the private operator narrative are not added to the public repository. A generated narrative does not replace source measurements.

---

## 2. Exact append-only integrity

GitHub `fetch_file` comparisons between baseline `main` and the rollover branch confirmed that the *entire previous file content* is an exact prefix of each of these five governed targets:

| File | Historical prefix | New W40 rows | Resulting count |
|---|---|---:|---:|
| `data/daily_biomarkers_v1.csv` | Exact, unchanged | 7 | 245 |
| `data/sleep_longitudinal_v1.csv` | Exact, unchanged | 7 | 245 |
| `data/training_blocks_v1.csv` | Exact, unchanged | 13 | 396 |
| `data/context_events_v1.csv` | Exact, unchanged | 1 | 52 |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | Exact, unchanged | 1 | 35 |

No existing governed row was removed, reordered, rewritten, reinterpreted in place, or silently corrected. This is stronger than merely matching row counts.

Data endpoints after W40:

```text
Daily Biomarkers:  2026-02-09 through 2026-10-11, 245 daily rows
Canonical Sleep:   2026-02-09 through 2026-10-11, 245 wake-date rows
Training Blocks:   396 completed sessions, latest 2026-10-11
Context Events:    52 bounded events, latest end date 2026-10-10
```

Context events are not a daily-indexed dataset: their endpoint is not expected to equal the most recent daily observation date.

---

## 3. Missingness, units and time semantics

- All seven W40 morning scale observations are available; unlike travel-affected W39, this interval has no missing waking dates.
- The October 11 scheduled LI rest is **not** a completed LI session and does not receive a synthetic training row. B1 was completed on that date.
- The October 9 separately recorded 58-minute nap remains distinct from the overnight sleep period; it is excluded from the seven-night sleep mean.
- October 8's post-B1 weight was **pre-GI clearance**, while the other represented post-B1 measurements in W40 were post-GI clearance. A pooled post-B1 weekly weight is therefore not claimed.
- A lower acute post-exercise scale measurement is not mechanically equivalent to waking bodyweight or direct tissue-composition change.
- Daily biomarker HRV and sleep HRV are distinct series; resting HR and sleeping HR are distinct series.
- Wearable REM and deep-sleep estimates are preserved as stage estimates, with limited certainty. Vivid dream narratives do not validate exact REM duration.
- Daily activity and intermediate training observations may represent different points in the day; an earlier activity estimate should not be misclassified as a conflict with end-of-day totals.

These boundaries prevent false precision without creating unnecessary source rewrites.

---

## 4. Reproduced W40 arithmetic

The actual `tools/validate_weekly_rollover.py` derived the following table from committed structured data and matched it against `reports/2026-W40.md`:

| Closed W40 metric | Reproduced value |
|---|---:|
| Morning bodyweight, seven measurements | **227.0 lb** |
| Daily biomarker HRV | **72.4 ms** |
| Resting heart rate | **43.9 bpm** |
| Daily average heart rate | **59.9 bpm** |
| Sleep HRV | **82.6 ms** |
| Sleep average heart rate | **45.6 bpm** |
| Total overnight sleep | **7h11m** |
| Deep sleep, wearable estimate | **1h36m** |
| REM sleep, wearable estimate | **59m** |
| B1 sessions | **7** |
| Load Integration sessions | **6** |
| Total formal training | **660 min** |

Supporting session accounting:

- B1: 7 × 55 minutes = **385 minutes**, total **21.14 miles**.
- LI: October 5 45; October 6 45; October 7 55; October 8 45; October 9 35; October 10 50 = **275 minutes**.
- Total: **13 completed sessions**, **660 minutes**.
- October 11: B1 only, with scheduled LI rest.

The closed report includes the validator's required B1 distance/minute notes, LI minute notes and completed-session count. The observed 160-minute difference from W39's travel-affected 500 minutes is not attributed solely to the higher resistance-training dose.

---

## 5. Canonical sleep and recovery boundary

For October 5–11, seven overnight records are present with stage-duration arithmetic preserved. Mean overnight sleep was approximately 430.6 minutes, rounded to 7h11m. Three nights were shorter than seven hours; the final night included shorter duration and reduced efficiency relative to several earlier W40 nights. Overnight HRV remained a separate stream from daily biomarker HRV.

The week supplies generally favorable recorded recovery and preserved reported daytime function, but cannot establish that the newly increased LI stimulus is repeatedly recoverable or free of delayed musculoskeletal cost. No recovery-based causal mechanism is assigned to single-night HRV, heart-rate or stage fluctuations.

The protected August snapshot is separate from W40 recovery interpretation. Its original evidence and Model Error 043 closure remain governed by the snapshot-specific validator.

---

## 6. LI progression exposure and prospective/retrospective distinction

The original active W40 report called for an unchanged home-condition baseline before reconsidering progression. W40 execution departed from that opening intention:

| Date | Exposure | Evidence boundary |
|---|---|---|
| 2026-10-07 | Pull-ups increased to 5×4; push-ups to 3×12; two supported-row sets introduced | First exposure; multiple components changed; reported global RPE about 4 |
| 2026-10-08 | Standard LI returned | Next-session function observed; not same-dose replication |
| 2026-10-09 | Technique/reduced-load LI | Intentionally lower dose preserved |
| 2026-10-10 | Trap bar increased to 4×5 at existing load; hangs to 3×45s | First hinge/grip exposure; reported global RPE about 4 |
| 2026-10-11 | Scheduled LI rest | No completed LI session |

This is a **bounded within-week protocol change**. The separate `protocols/load-integration-progression-exposures-2026-W40.md` file is retrospective exposure documentation. It does **not** backdate formal public preregistration, assert a single-variable experiment, authorize a further increase, or declare Phase 2D.

The plate-loaded T-bar row entries preserve plate mass references, not verified effective machine resistance. Actual trap-bar numeric working load is not invented where the source uses the existing-load descriptor.

W41 remains Active under the exact weekly posture **Structured LI progression / repeatability observation**. It focuses on repeatability of the already introduced doses, actual completed work and delayed recovery rather than automatic escalation.

---

## 7. Bounded event-index representation

One event, `2026-10-07-01`, indexes the October 7–10 first progression exposures as `other / structured_li_progression_first_exposures` with protocol-altering relevance. The training rows remain the authoritative record of completed sessions.

The context-event index is intentionally sparse. Routine B1, standard LI, nightly fluctuations, a scheduled LI rest day, and ordinary household activity are not converted into redundant context events simply to increase the event count.

---

## 8. Weekly report lifecycle

- `reports/2026-W40.md`: **Closed**, window 2026-10-05 through 2026-10-11.
- `reports/2026-W41.md`: **Active**, window 2026-10-12 through 2026-10-18.
- No date gap or overlap between these standardized weekly intervals.
- W40 closeout includes retrospective interpretation, quantitative metrics, a protocol decision, recovery boundary, and unresolved questions.
- W41 opening preserves prospectively open outcomes. It does not contain invented completed W41 sessions, determined recovery outcomes or a fabricated phase transition.
- Historical W39 and earlier weekly reports remain preserved.

The W40 retrospective descriptor is **controlled expansion**. W41 does not have a completed retrospective descriptor while its observation window remains open.

---

## 9. Current-facing document synchronization

The following nine current-facing files were updated in Batch 3 and checked against the actual report lifecycle and structured CSV endpoints:

- `README.md`
- `LATEST.md`
- `INDEX.md`
- `docs/START_HERE.md`
- `docs/CONCEPTS.md`
- `docs/OBSERVER_QUICKSTART.md`
- `docs/NEWCOMER_PATH.md`
- `data/DATA_COVERAGE.md`
- `CHANGELOG.md`

All current pointers represent W41 Active / W40 Closed. The immediate posture is **Structured LI progression / repeatability observation**. The broader Phase 2 substate remains **Consolidation / lock-in observation**.

Batch 3 cross-document checks previously verified all nine intended paths, 23 current-state/metric conditions and 302 internal relative links with no unresolved target after including directory entries. One pre-existing duplicated training explanation in `README.md` was corrected without altering protected data.

---

## 10. Coherence finding and correction

**Finding:** The first GitHub Actions run for this audit initially returned four validator passes and one coherence failure.

- Run: [38327422581](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/38327422581)
- Commit: `81c43ef94574a53524c158af6cb07520f0dc541b`
- Core repository validator: PASS.
- Machine-readable layer validator: PASS.
- Latest weekly rollover validator: PASS.
- August snapshot cross-layer validator: PASS.
- Post-release coherence validator: **FAIL**, with exact diagnostic:
  `LATEST.md: stacked session-level jargon returned to first-contact surface: trait-level`.

This was a **first-contact presentation** failure, not a structured-measurement discrepancy. The offending phrase appeared in the active executive dashboard's governance list; its content was replaced with the plain-language expression “subjective ease.” The original validator rule was retained unchanged.

**Correction commit:** `fe4e842bf8d07c40c3b81a5d0f59b18778417724`.

**Second GitHub Actions run:** [38327489774](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/38327489774) completed successfully at that correction commit, with **all five validator job steps passing**. The corrected wording preserves the same phase/governance decision without violating the first-contact role separation.

---

## 11. Exact validator execution

The existing `.github/workflows/validate.yml` executes exactly:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
python tools/validate_weekly_rollover.py
python tools/validate_august_snapshot.py
python tools/validate_coherence.py
```

To run those original commands before opening a pull request, the workflow's push-branch pattern was expanded from `main` only to include `w*-rollover` branches. This is a bounded **CI trigger change**, not a revision of validator rules or scientific evidence. The workflow remains independently runnable by manual dispatch and on pull requests. It allows each new audit/changelog commit to obtain a genuinely matched branch-head GitHub Actions result.

The green pre-audit execution is documented above. **A new audited-head run must pass after this audit is committed.** CI is an implementation integrity gate, not proof of clinical or scientific validity.

---

## 12. Source quality and open limitations

- DQ-011 remains open for the previously recorded September 8 resting-heart-rate source question. The current audit does not change its value, status or adjudication.
- The workbook's mixed date encodings are normalized only for public ISO indexing.
- Timing distinctions for weight, activity, sleep and nap observations are preserved without artificial pooling.
- The source does not contain a direct measurement of the tissue composition of short-window weight movement.
- One formal progression exposure per variant is not a repeatability result.
- The current dataset does not provide a continuous measured nutritional-intake or energy-availability series from which adequacy could be established.
- Nightly cardiovascular anomalies are not diagnosed or dismissed based on successful daytime exercise alone.
- Model Error prediction boundaries remain separate from observational LI progression.

These are constraints on inference rather than defects requiring retrospective source rewrites.

---

## 13. Protected governance, frozen release and publication identity

Direct Git blob comparisons between `main` and the branch confirmed identical content for the sampled protected files:

- `reports/2026-W39.md`
- `PHASE_MAP.md`
- `GOVERNANCE.md`
- `data/model_error/record_043_closure.md`
- `VERSIONING.md`
- `VERIFICATION.md`
- `CITATION.cff`
- `CODEMETA.json`

Release identity remains:

```text
Published version:      v1.1.0
Frozen release commit:  92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
Version DOI:            10.5281/zenodo.22759132
All-versions DOI:       10.5281/zenodo.20815611
```

No release tag, immutable archive, DOI metadata, scoring rubric, closed Model Error outcome, declared phase or historical report is rewritten by the W40/W41 rollover. Phase 2D remains undeclared; the W40 first-exposure record is not a new stage decision.

---

## 14. Privacy and public-distribution boundary

Changed paths belong to governed public CSVs, source-provenance text, weekly reports, a narrow retrospective protocol note, current-facing orientation documentation, changelog, CI trigger and this audit.

The private v1.34 workbook is referenced by its filename/hash and row locators but **not uploaded**. The private operator narrative is not committed. No medical provider raw export, personal message, or non-public household source is introduced by this rollover. Public reports use bounded observational interpretation rather than copying the private extended narrative.

---

## 15. Changed-file boundary and final gate

Pre-audit branch changes relative to `main` are confined to:

- five governed append-only CSV/source-manifest targets;
- two weekly reports;
- one retrospective LI progression-exposure protocol note;
- nine current-facing documentation/changelog files;
- the `.github/workflows/validate.yml` rollover-branch push trigger.

The short `LATEST.md` wording correction is within the existing current-facing document scope. This audit file adds one additional changed path. No release artifacts are included in the intended diff.

The audit was prepared from a green five-validator pre-audit branch head. Before any PR or merge action, check the latest branch SHA and the GitHub Actions run against **that same SHA**. Every validator must pass. A result from an earlier SHA is not a valid final-head gate.

---

## Audit verdict

**Conditional GO: proceed to PR preparation only after the audit/changelog commit produces a green final-head five-validator run.**

The completed W40 data and provenance are append-only; the report lifecycle and W41 posture are consistent; the original W40 intent and its actual progression are distinguishable; model-error, phase, privacy and frozen-publication boundaries remain intact. The sole detected validator issue was a first-contact wording violation, corrected without changing data or validator rules. Repeatability and delayed recovery remain legitimate open W41 observation questions rather than inferred results.

The final publication review still belongs to Batch 5. This audit does **not** authorize merging into `main`, moving v1.1.0, changing a DOI, or declaring Phase 2D.
