# 2026-09-21 Post-Weekly-Rollover Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Audit branch:** `w37-closeout-batch1`  
**Baseline:** `main` at `8785e714be800d6574ec14679d3d678e30a42af1`  
**Pre-audit content head:** `f9724c6a44555507ea32c18213aeff8e3db0081c`  
**Validation PR:** #15 — W37 closeout and W38 rollover  
**Audit date:** 2026-09-21  
**Verdict:** **GO, contingent on unchanged branch content and final green CI**

---

## Scope

This audit reviews the governed Week 37 closeout and Week 38 rollover as a cross-layer repository change.

The review covers:

- exact W37 source identity and provenance
- machine-readable append-only preservation
- structured row counts and endpoints
- W37 retrospective arithmetic
- W37 context-event representation
- weekly report lifecycle
- W38 opening posture
- current-facing state synchronization
- data-quality boundaries
- release / DOI invariants
- phase and model-error invariants
- privacy / distribution boundaries
- repository validation

The audit does not reinterpret the underlying biological evidence beyond checking whether the public representations remain proportional to the registered source and structured rows.

---

## 1. Source Identity

The controlling closed private source is registered as:

```text
source_version:  v1.31
coverage:        2026-09-14 through 2026-09-20
filename:        Daniel_Dataset_v1.31
size:            370947 bytes
sha256:          58828f4a84900fa2cb0b6002539b8f5ae125b237c8c8f1e202427bc28142459a
hash_status:     registered
```

The source manifest preserves the W37 source-role note that two free-text B1 HRV references differ from the dedicated Daily Biomarkers HRV cells. The public canonical daily-HRV extraction remains tied to the dedicated structured field rather than inferring a replacement from the free-text notes.

The corrected 2026-09-18 Daily Biomarkers temperature is represented as:

```text
96.31°F
```

No new numbered data-quality issue is required for that corrected closed-source value.

---

## 2. Append-Only Preservation

The five governed append-only public/provenance files were compared line-for-line against `main`.

Result:

| File | Baseline lines | Audit-branch lines | Appended lines | Historical prefix |
|---|---:|---:|---:|---|
| `data/daily_biomarkers_v1.csv` | 218 | 225 | 7 | exact |
| `data/sleep_longitudinal_v1.csv` | 218 | 225 | 7 | exact |
| `data/training_blocks_v1.csv` | 351 | 363 | 12 | exact |
| `data/context_events_v1.csv` | 46 | 50 | 4 | exact |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | 32 | 33 | 1 | exact |

No historical row in those files was modified, reordered, replaced, or deleted.

This is stronger than a count-only check: the complete baseline text of each governed file is an exact prefix of the audit-branch file.

---

## 3. Structured Coverage

Post-extension public coverage is:

```text
daily_biomarkers_v1.csv   224 continuous daily rows through 2026-09-20
sleep_longitudinal_v1.csv 224 continuous daily rows through 2026-09-20
training_blocks_v1.csv    362 completed-session rows through 2026-09-20
context_events_v1.csv      49 bounded events through 2026-09-20
```

Training remains session-indexed.

The 2026-09-14 travel/rest day has no completed training session and therefore has no synthetic training row.

The W37 interval contains:

```text
6 B1 sessions
6 Load Integration sessions
12 completed sessions
600 formal training minutes
330 B1 minutes
270 Load Integration minutes
18.12 B1 miles
```

---

## 4. W37 Arithmetic Reproduction

W37 report controls were independently recalculated from the public structured rows for 2026-09-14 through 2026-09-20.

| Metric | Reproduced value | Public report |
|---|---:|---:|
| Morning bodyweight | 232.55 lb → 232.6 lb | 232.6 lb |
| Daily HRV | 63.43 ms → 63.4 ms | 63.4 ms |
| Daily resting HR | 48.29 bpm → 48.3 bpm | 48.3 bpm |
| Daily average HR | 63.14 bpm → 63.1 bpm | 63.1 bpm |
| Sleep HRV | 70.57 ms → 70.6 ms | 70.6 ms |
| Sleep average HR | 56.57 bpm → 56.6 bpm | 56.6 bpm |
| Total sleep | 472.29 min → 7h52m | 7h52m |
| Deep sleep | 72.0 min → 1h12m | 1h12m |
| REM sleep | 67.29 min → 1h07m | 1h07m |
| Total formal training | 600 min | 600 min |
| B1 distance | 18.12 mi | 18.12 mi |

Morning bodyweight uses six available scale mornings because no travel scale was available on 2026-09-14.

All checked report values reproduce from the structured layer under the stated rounding rules.

---

## 5. Context-Event Review

Four bounded W37 context events were added:

```text
2026-09-14-01  travel/rest continuation
2026-09-16-01  yard work between formal sessions
2026-09-18-01  bounded acute pre-sleep interpersonal/financial stress
2026-09-20-01  unofficial end-of-session capacity probe
```

The event index remains selective rather than diary-like.

The 2026-09-15 post-travel return is preserved in daily/training context tags and the weekly report rather than receiving a redundant separate context-event row.

The 2026-09-20 probe remains explicitly observational. It does not modify the registered training prescription.

---

## 6. Weekly Lifecycle

The weekly report series remains continuous from W06 through W38.

Lifecycle state after rollover:

```text
2026-W37  Closed
2026-W38  Active
```

W38 covers:

```text
2026-09-21 through 2026-09-27
```

Its immediate weekly operating posture is:

```text
Consolidation / reserve-replication observation
```

The broader Phase 2 substate remains:

```text
Consolidation / lock-in observation
```

The W38 report treats the 2026-09-20 reserve observation as a replication question rather than a progression decision.

---

## 7. Current-State Synchronization

The following current-facing surfaces were reviewed for W38 active / W37 closed alignment:

- `LATEST.md`
- `README.md`
- `INDEX.md`
- `docs/OBSERVER_QUICKSTART.md`
- `docs/NEWCOMER_PATH.md`
- `tools/validate_coherence.py`

The observer and newcomer routes now point to W37 as the most recent closed report.

The current-facing surfaces explicitly distinguish the immediate weekly operating posture from the broader Phase 2 substate.

The README structured-coverage summary is synchronized to the governed 2026-09-20 endpoints.

---

## 8. Data-Quality Boundary

DQ-011 remains open for the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm.

No W37 source evidence resolves DQ-011.

The W37 v1.31 HRV note/field discrepancy is preserved as a source-role review:

- canonical public `daily_hrv_ms` follows the dedicated Daily Biomarkers cell
- differing free-text B1 note references remain preserved in the private source
- no averaging, inferred replacement, or silent rewrite was introduced

The Current Dataset Disposition now explicitly includes DQ-011.

---

## 9. Release, DOI, Phase, and Model-Error Invariants

The rollover does not alter the published release boundary.

The following remain fixed:

```text
published release:       v1.1.0
frozen release commit:   92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
version DOI:             10.5281/zenodo.22759132
all-versions DOI:        10.5281/zenodo.20815611
```

`CITATION.cff`, `CODEMETA.json`, `VERSIONING.md`, the release tag, and the frozen release package are not changed by this rollover.

The live INDEX stale release-orientation label was corrected from v1.0.0 to v1.1.0; this is a current-navigation repair, not a release mutation.

Scientific/governance state also remains fixed:

- Phase 2 — Load Integration
- broader substate: Consolidation / lock-in observation
- Phase 2D: undeclared
- Model Error records 041–046: closed
- Record 043: not supported / `overall_improvement_not_met` / over
- August snapshot adjudication: unchanged

---

## 10. Privacy and Distribution Review

The PR changes 16 public text files and adds no workbook, spreadsheet, image, provider export, or other new private binary artifact.

A scan of all newly added PR text found no:

- email address
- phone number
- Social Security number pattern
- home/container absolute path
- Windows local path
- street-address pattern
- `.xlsx` filename

Historical private-workbook filenames already present in the provenance manifest remain historical metadata and were not newly introduced by this rollover.

The v1.31 manifest entry uses the bounded retained identifier `Daniel_Dataset_v1.31`; the private workbook itself is not published.

The public context representation of the 2026-09-18 stress event remains generalized to interpersonal/financial stress and does not publish private counterpart identity or unnecessary personal detail.

---

## 11. Automated Validation

A draft pull request was opened specifically to execute the repository's actual GitHub Actions validation workflow against the complete rollover branch:

```text
PR #15
W37 closeout and W38 rollover
```

Repository validation run `35659716878` completed successfully on the pre-audit content head.

All workflow validation steps passed:

- core repository validator
- machine-readable layer validator
- August snapshot cross-layer validator
- post-release coherence validator

The audit artifact itself should also receive the same CI workflow after being committed. Final merge readiness therefore requires the branch head to remain unchanged after a green final run.

---

## 12. Diff Boundary

Relative to `main`, the pre-audit rollover branch contained:

```text
19 commits ahead
0 commits behind
16 changed files
569 additions
162 deletions
```

The deletions are confined to replacement of active/current-state prose and conversion of the W37 active skeleton into its closed retrospective. The governed historical CSV/provenance layers are append-only as documented above.

No protected release artifact or model-error record appears in the changed-file set.

---

## Audit Verdict

**GO, contingent on final CI remaining green at the final branch head.**

The W37 closeout and W38 rollover are internally coherent across source provenance, structured evidence, report arithmetic, context classification, weekly lifecycle, current-state surfaces, release boundaries, data-quality governance, and privacy review.

The strongest integrity findings are:

1. historical structured/provenance prefixes are preserved exactly
2. W37 quantitative claims reproduce directly from the public structured rows
3. the unofficial reserve probe remains observational rather than silently becoming protocol
4. W38 opens as a replication question rather than a phase or progression declaration
5. published v1.1.0 release identity remains fixed
6. DQ-011 remains unresolved rather than being cleaned up by inference
7. no new private artifact or direct identifying contact/location information was introduced
8. the repository's own four-layer CI validation passed on the complete pre-audit rollover content

If the final post-audit branch head remains unchanged and its CI run is green, the branch is suitable for merge into `main`.
