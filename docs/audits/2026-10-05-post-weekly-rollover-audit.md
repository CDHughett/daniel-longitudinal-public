# 2026-10-05 W39/W40 Post-Weekly-Rollover and Coherence Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Baseline main:** `c3fb7c6f5c6113aa54047b433c0951e477d02df6`  
**Rollover branch:** `w39-closeout-w40-rollover`  
**Pre-audit content head:** `7773bf77cca7739c4e182195048d7e855440f236`  
**Audit date:** 2026-10-05  
**Verdict:** **GO, subject to the final audited-head CI gate**

---

## Scope

This audit reviews the W39 closeout / W40 initialization and replaces the former midweek/weekend manual drift-audit cadence with an integrated rollover-time coherence review.

The review covers:

- exact private-source identity and provenance registration
- append-only preservation of the governed longitudinal data/provenance files
- W39 arithmetic reproduction from the committed public structured layer
- canonical sleep stage arithmetic and source-role boundaries
- session-indexed training representation
- bounded context-event representation
- weekly-report lifecycle and observation-window continuity
- current-state synchronization across public orientation surfaces
- coherence/drift findings exposed by the rollover
- hardening of the post-release coherence validator
- supplementation, data-quality, phase, Model Error, release, tag, and DOI invariants
- privacy and distribution boundaries
- final automated validation requirements

The audit does not rescore biological predictions, infer missing observations, declare a phase transition, or authorize training progression.

---

## 1. Source Lock and Provenance

The controlling private source for the closed W39 interval is:

```text
source:       Daniel_Dataset_v1.33
coverage:     2026-09-28 through 2026-10-04
size:         366,510 bytes
SHA-256:      c49f1806b140d49cfb956b8bd2f083c9e18c20455f1126ce6b5f39e28c76444c
hash status:  registered
```

The exact retained source is registered in:

`data/source_provenance/daniel_dataset_private_manifest.csv`

The public repository does not contain the private workbook itself.

The separately generated closed-summary workbook is not used as the private provenance target. The retained v1.33 source identity above controls the W39 extraction boundary.

---

## 2. Append-Only Preservation

The five governed public/provenance append targets are:

- `data/daily_biomarkers_v1.csv`
- `data/sleep_longitudinal_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`
- `data/source_provenance/daniel_dataset_private_manifest.csv`

Each branch version preserves the complete `main` version as an exact prefix before the W39 append.

No historical governed row was:

- deleted
- reordered
- replaced
- silently corrected
- normalized by inference

W39 adds:

```text
daily biomarkers   +7 rows
canonical sleep    +7 rows
training          +10 completed-session rows
context events     +1 bounded event
private manifest   +1 registered source row
```

The live resulting profiles are:

```text
daily biomarkers   238 rows through 2026-10-04
canonical sleep    238 rows through 2026-10-04
training           383 sessions through 2026-10-04
context events      51 events through 2026-09-29
```

The context endpoint is intentionally earlier than the daily/sleep/training endpoint because the context table is a bounded event index rather than a one-row-per-day diary.

---

## 3. Missingness and Measurement Context

No morning scale value exists for:

```text
2026-09-28
2026-09-29
```

Those values remain missing.

No interpolation or neighboring-value substitution was introduced.

Post-B1 bodyweight conditions also differ inside W39:

- 2026-09-30 was recorded before GI clearance
- 2026-10-01 through 2026-10-04 were recorded after GI clearance

The closed W39 report therefore uses `NA` for a pooled weekly Post-B1 bodyweight value rather than manufacturing a mean from non-equivalent measurement conditions.

---

## 4. W39 Arithmetic Reproduction

The closed W39 report covers:

```text
2026-09-28 through 2026-10-04
```

The committed structured rows independently reproduce:

```text
Morning bodyweight        228.7 lb
Daily biomarker HRV        65.6 ms
Resting heart rate         45.0 bpm
Daily average heart rate   60.7 bpm
Sleep HRV                  71.3 ms
Sleep average heart rate   50.7 bpm
Total sleep                7h20m
Deep sleep                 1h20m
REM sleep                  58m
B1 sessions                5
B1 minutes               275
B1 distance             15.10 mi
Load Integration sessions  5
Load Integration minutes 225
Total sessions             10
Total formal training     500 min
```

The private Weekly Summary whole-number HRV display and the public one-decimal report are not treated as a conflict. The public weekly report uses the independently reproduced one-decimal mean from the seven Daily Biomarkers rows, consistent with the latest-weekly-rollover validator's reporting rule.

---

## 5. Canonical Sleep Arithmetic and Interpretation Boundary

Seven canonical sleep rows are present for W39.

For every appended row:

```text
deep_sleep_min + light_sleep_min + rem_sleep_min
=
total_sleep_min
```

The represented stage percentages also reproduce from the stage-minute values at the stored precision.

No stage-allocation correction was inferred from subjective dream experience.

Wearable REM/deep estimates remain consumer-device stage estimates and are interpreted below:

- total sleep
- overnight cardiovascular behavior
- subjective morning state
- demonstrated next-day function

Two unusual early-night cardiovascular episodes remain visible in the sleep/report layers. Their later normalization and preserved next-day function are recorded without converting that association into a universal rule or causal diagnosis.

---

## 6. Training Representation

No synthetic training rows were created for the two no-training travel days:

```text
2026-09-28
2026-09-29
```

The public training layer remains session-indexed.

From 2026-09-30 through 2026-10-04, the public layer contains:

```text
5 B1 sessions
5 Load Integration sessions
10 completed sessions total
500 formal minutes
```

The W39 closeout does not convert repeated subjective ease, automatic movement setup, or the successful post-travel return into a quantified reserve value.

No second interpretable reserve probe occurred.

---

## 7. Context-Event Representation

One new bounded context event is created:

```text
event_id:         2026-09-28-01
event_type:       travel
event_subtype:    out_of_town_travel_continuation
interval:         2026-09-28 through 2026-09-29
impact_level:     protocol_altering
protocol_impact:  formal_training_paused
outcome_state:    resolved
related_week:     2026-W39
```

The event preserves the analytically relevant fact that travel continued to displace formal training and then resolved with normal home training resuming on 2026-09-30.

The audit confirms that transient stiffness, afternoon tiredness, subjective ease, two overnight cardiovascular events, and the isolated B1 heart-rate excursion were not redundantly promoted into separate event-index rows. Those observations remain in the daily/training/report layers.

This preserves the context table as a bounded event index rather than a diary.

---

## 8. Weekly Lifecycle

The standardized weekly lifecycle after rollover is:

```text
2026-W39  Closed
2026-W40  Active
```

Observation windows are contiguous under the repository's internal week index:

```text
W39: 2026-09-28 through 2026-10-04
W40: 2026-10-05 through 2026-10-11
```

W39 closes with the retrospective descriptor:

```text
retention
```

The supported scope is narrow: a short logistics-directed interruption ended, and the established B1 + Load Integration architecture returned without a staged rebuilding period or training-debt behavior.

The closeout does not claim:

- permanent detraining resistance
- a Phase 2D transition
- replicated quantified reserve
- causal explanation for the lower bodyweight state
- harmlessness of all future overnight cardiovascular anomalies
- automatic progression authorization

W40 opens with:

```text
Consolidation / full-home baseline observation
```

It does not open as a progression week.

---

## 9. Current-State Synchronization

The following current-facing surfaces were advanced to W40 active / W39 closed:

- `README.md`
- `LATEST.md`
- `INDEX.md`
- `docs/OBSERVER_QUICKSTART.md`
- `docs/NEWCOMER_PATH.md`
- `docs/START_HERE.md`
- `docs/CONCEPTS.md`

The current canonical relationship is:

```text
Phase:
Phase 2 — Load Integration

Broader substate:
Consolidation / lock-in observation

Weekly posture:
Consolidation / full-home baseline observation

Active:
2026-W40

Most recent closed:
2026-W39

Phase 2D:
undeclared
```

README and LATEST now expose the governed W39 structured endpoints:

```text
daily biomarkers  238 through 2026-10-04
canonical sleep   238 through 2026-10-04
training          383 through 2026-10-04
context events     51 through 2026-09-29
```

Observer and newcomer routes point to W39 as the newest closed retrospective report.

---

## 10. Coherence/Drift Audit Findings

The integrated rollover audit identified two real current-state drift defects that had survived the previous validator boundary:

1. `docs/START_HERE.md` still exposed the older `Consolidation / reserve-replication observation` weekly posture.
2. `docs/CONCEPTS.md` exposed the same stale current-posture value in its Current Terminology State block.

The root cause was structural rather than scientific.

The prior coherence validator protected the current weekly posture in `LATEST.md` but did not require exact posture synchronization in START_HERE or CONCEPTS.

A second anti-drift opportunity was also confirmed: README/LATEST duplicated live structured-data counts/endpoints for usability, but the coherence validator did not derive and protect those summaries directly from the committed CSVs.

All identified current-facing drift was repaired.

Historical reports, dated audits, changelog history, and conceptual examples that correctly preserve earlier states were not mass-rewritten.

---

## 11. Coherence Hardening

`tools/validate_coherence.py` was hardened rather than adding a sixth Python validator.

The validator now dynamically derives from the live weekly-report lifecycle:

- active week
- immediately preceding closed week
- active weekly posture

It no longer requires a weekly edit to hard-coded W39/W38/post-travel constants.

The validator now requires exact current-state agreement across:

- README
- LATEST
- INDEX
- START_HERE
- CONCEPTS

It also derives the live row counts/endpoints from:

- `data/daily_biomarkers_v1.csv`
- `data/sleep_longitudinal_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`

and protects the corresponding README/LATEST summaries against silent lag.

During implementation review, one pointer-iteration bug in the first hardening commit was detected and corrected before this audit closeout. The final branch implementation uses the corrected dictionary iteration and contains none of the old W39/W38/post-travel hard-coded current-state constants.

`tools/README.md` and `VERIFICATION.md` were updated to document the hardened boundary.

The normal GitHub Actions workflow already executes `tools/validate_coherence.py`; no workflow-architecture change was required.

---

## 12. Supplementation, Data Quality, and Source Roles

The reduced supplementation architecture effective 2026-09-18 remains material background protocol context.

W39/W40 do not attribute bodyweight, HR, HRV, sleep, recovery, or training changes to the supplementation transition.

DQ-011 remains unresolved for the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm.

The governing treatment remains:

- preserve the recorded value
- do not infer a replacement
- do not substitute another heart-rate field
- resolve only from originating source evidence

No W39 source evidence resolves DQ-011.

---

## 13. Release, DOI, Phase, and Model-Error Invariants

The rollover/hardening does not alter the published release boundary.

The following remain fixed:

```text
published release:       v1.1.0
frozen release commit:   92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
version DOI:             10.5281/zenodo.22759132
all-versions DOI:        10.5281/zenodo.20815611
```

Scientific/governance state remains:

- Phase 2 — Load Integration
- broader substate: Consolidation / lock-in observation
- Phase 2D: undeclared
- Model Error records 041–046: closed
- Record 043: not supported / `overall_improvement_not_met` / over
- August snapshot state: unchanged
- DQ-011: unresolved

The rollover does not modify:

- `CITATION.cff`
- `CODEMETA.json`
- `VERSIONING.md`
- `PHASE_MAP.md`
- `data/model_error/model_error_gap_v1.csv`
- `data/DATA_QUALITY_NOTES.md`
- August snapshot or epigenetic datasets
- protected provider/source binary artifacts

---

## 14. Privacy and Distribution Review

The public rollover remains privacy-minimized.

The private workbook is not published.

The public travel representation is limited to analytically relevant terms such as:

- out-of-town travel
- logistics-directed formal-training interruption
- home re-entry

Private family names, retailer detail, lodging detail, memorial/family-event detail, and exact travel-destination detail from the private source narrative are not required for public interpretation and are not introduced into the structured context event or weekly public report.

The exact private-source filename, byte count, and SHA-256 are retained only as bounded provenance metadata.

No new binary private-source artifact is added to the branch.

---

## 15. Pre-Audit Diff Boundary

Relative to `main`, the exact pre-audit content head `7773bf77cca7739c4e182195048d7e855440f236` was:

```text
19 commits ahead
0 commits behind
18 changed files
839 additions
206 deletions
```

The changed-file set was limited to:

- five governed structured/provenance CSV append targets
- `data/DATA_COVERAGE.md`
- W39 closeout and W40 active report
- current-state/navigation surfaces
- coherence validator code
- validator documentation

No release metadata, phase map, Model Error ledger, DQ ledger, August snapshot data, epigenetic data, or protected binary source was in that pre-audit changed-file set.

The larger deletion count is primarily replacement of W39's active skeleton with its closed retrospective report and replacement of volatile current-state prose. It is not a deletion of governed historical evidence.

---

## 16. Final Automated Validation Gate

The final merge-readiness gate is the repository's actual five-validator pull-request workflow:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
python tools/validate_weekly_rollover.py
python tools/validate_august_snapshot.py
python tools/validate_coherence.py
```

The final audited branch head must receive a green pull-request validation run after this audit artifact and its changelog entry are committed.

Required interpretation of that gate:

- validator success establishes implemented repository/mechanical/coherence checks
- it does not establish biological causality or clinical validity
- any subsequent content mutation reopens the final validation gate

At the time this audit artifact is authored, the final audited-head CI run is intentionally pending.

---

## Audit Verdict

**GO, subject to the final audited-head CI gate.**

The W39 closeout / W40 rollover is internally coherent across source provenance, append-only preservation, structured arithmetic, sleep semantics, training/session representation, bounded context, weekly lifecycle, current-state surfaces, privacy, phase/model-error/DQ/release invariants, and the replacement coherence-audit boundary.

The strongest integrity findings are:

1. all five governed historical data/provenance prefixes remain exactly preserved
2. W39 quantitative claims reproduce from the committed public structured rows
3. missing travel weights remain missing
4. mixed post-B1 GI-clearance conditions are not collapsed into a false weekly mean
5. zero-session travel days remain zero-session days
6. W39 closes as short-interruption retention without converting that observation into progression or Phase 2D
7. W40 opens with a full-home baseline before escalation
8. the integrated drift pass found and repaired stale current-posture state in START_HERE and CONCEPTS
9. the coherence validator now derives weekly state dynamically and protects live README/LATEST structured-count summaries
10. v1.1.0 identity, DOI lineage, Phase 2 state, Model Error outcomes, and DQ-011 remain fixed

The branch is suitable for pull-request validation.

Final merge readiness requires the audit artifact and changelog entry themselves to be included in the green CI-tested head.
