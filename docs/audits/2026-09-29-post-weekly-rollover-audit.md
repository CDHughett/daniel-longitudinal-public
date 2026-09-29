# 2026-09-29 Post-Weekly-Rollover Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Audit branch:** `w38-batch1-machine-readable`  
**Baseline:** `main` at `6fcd8794cb11cc7ddd334e758544d8a16251fe9c`  
**Pre-audit content head:** `6d643b8513678500803c895b5272dc67a451c499`  
**Validation PR:** #23 — W38 closeout and W39 rollover  
**Audit date:** 2026-09-29  
**Verdict:** **GO**

---

## Scope

This audit reviews the governed Week 38 closeout and Week 39 rollover as a cross-layer repository change.

The review covers:

- exact W38 private-source identity and provenance
- machine-readable append-only preservation
- structured row counts and endpoints
- W38 retrospective arithmetic
- canonical sleep extraction semantics
- W38 training and context-event representation
- weekly report lifecycle
- W39 opening posture
- current-facing state synchronization
- data-quality and source-role boundaries
- release / DOI invariants
- phase and model-error invariants
- privacy / distribution boundaries
- repository validation
- one narrow derived-arithmetic wording correction discovered during audit

The audit does not reinterpret the biological evidence beyond checking whether the public representations remain proportional to the registered source, public structured rows, and declared governance rules.

---

## 1. Source Identity

The controlling closed private source is registered as:

```text
source_version:  v1.32
coverage:        2026-09-21 through 2026-09-27
filename:        Daniel_Dataset_v1.32
size:            368070 bytes
sha256:          a9f03dde03a8b71846ede5fdec3214fe9009b93fca27c54f4bf587107a38a870
hash_status:     registered
```

The source was independently locked before repository mutation. The public manifest entry agrees with that source lock.

The retained source contains mixed date encodings. Public extraction normalizes the date index to ISO form while preserving the associated measured and logged values.

The manifest continues to treat canonical sleep as separately governed rather than fabricating row-level private-workbook provenance that the current sleep schema does not carry.

---

## 2. Append-Only Preservation

The five governed append-only public/provenance files were compared line-for-line against the exact `main` baseline.

Result:

| File | Baseline lines | Audit-branch lines | Appended lines | Historical prefix |
|---|---:|---:|---:|---|
| `data/daily_biomarkers_v1.csv` | 225 | 232 | 7 | exact |
| `data/sleep_longitudinal_v1.csv` | 225 | 232 | 7 | exact |
| `data/training_blocks_v1.csv` | 363 | 374 | 11 | exact |
| `data/context_events_v1.csv` | 50 | 51 | 1 | exact |
| `data/source_provenance/daniel_dataset_private_manifest.csv` | 33 | 34 | 1 | exact |

These line counts include the header row.

No historical row in those files was modified, reordered, replaced, or deleted.

This is stronger than a row-count check: the complete baseline text of each governed file is an exact prefix of the audit-branch file.

---

## 3. Structured Coverage

Post-extension public coverage is:

```text
daily_biomarkers_v1.csv   231 continuous daily rows through 2026-09-27
sleep_longitudinal_v1.csv 231 continuous daily rows through 2026-09-27
training_blocks_v1.csv    373 completed-session rows through 2026-09-26
context_events_v1.csv      50 bounded events through 2026-09-27
```

Training remains session-indexed.

The 2026-09-27 represented day contains zero completed training sessions and therefore correctly has no synthetic training row.

The W38 interval contains:

```text
6 B1 sessions
5 Load Integration sessions
11 completed sessions
556 formal training minutes
330 B1 minutes
226 Load Integration minutes
18.12 B1 miles
```

---

## 4. W38 Arithmetic Reproduction

W38 report controls were independently recalculated from the public structured rows for 2026-09-21 through 2026-09-27.

| Metric | Reproduced value | Public report |
|---|---:|---:|
| Morning bodyweight | 230.233 lb → 230.2 lb | 230.2 lb |
| Daily HRV | 67.143 ms → 67.1 ms | 67.1 ms |
| Daily resting HR | 44.857 bpm → 44.9 bpm | 44.9 bpm |
| Daily average HR | 60.429 bpm → 60.4 bpm | 60.4 bpm |
| Sleep HRV | 73.714 ms → 73.7 ms | 73.7 ms |
| Sleep average HR | 50.714 bpm → 50.7 bpm | 50.7 bpm |
| Total sleep | 448.57 min → 7h29m | 7h29m |
| Deep sleep | 75.57 min → 1h16m | 1h16m |
| REM sleep | 57.71 min → 58m | 58m |
| Total formal training | 556 min | 556 min |
| B1 exposure | 6 sessions / 330 min / 18.12 mi | 6 / 330 / 18.12 |
| Load Integration exposure | 5 sessions / 226 min | 5 / 226 |

All headline W38 quantitative claims reproduce from the public structured layer under the stated reporting precision.

### Bodyweight comparison correction discovered during audit

The underlying Week 37 six-measurement mean is:

```text
232.55 lb → reported as 232.6 lb
```

The underlying Week 38 six-measurement mean is:

```text
230.233... lb → reported as 230.2 lb
```

The difference between the **unrounded means** is approximately:

```text
2.3167 lb → 2.3 lb
```

The initial W38 closeout prose said 2.4 lb because it subtracted the separately rounded display means, 232.6 - 230.2.

The audit corrected that sentence to approximately **2.3 lb using the unrounded weekly means** while preserving both displayed weekly means and every underlying daily weight.

This was a derived-wording correction only. No source value, structured row, weekly headline value, body-composition claim, or protocol interpretation changed.

---

## 5. Canonical Sleep Verification

The seven W38 canonical sleep rows were checked for stage arithmetic:

```text
deep_sleep_min + light_sleep_min + rem_sleep_min = total_sleep_min
```

All seven rows satisfy that identity.

The canonical `awake_min` values also preserve the explicit Sleep Log awake totals rather than deriving awake time from time-in-bed minus total sleep:

```text
2026-09-21  22 min
2026-09-22  20 min
2026-09-23  16 min
2026-09-24  11 min
2026-09-25  22 min
2026-09-26  27 min
2026-09-27  24 min
```

The week contains two nights below 6h45m of total sleep:

```text
2026-09-23  402 min = 6h42m
2026-09-26  399 min = 6h39m
```

The longest night is the final represented travel-environment night:

```text
2026-09-27  558 min = 9h18m
```

This supports the report's caution that the 7h29m weekly mean is not a uniformly distributed nightly improvement.

---

## 6. Training and Context-Event Review

W38 completed-session extraction is internally coherent:

- 2026-09-21 through 2026-09-25: five complete B1 + Load Integration days
- 2026-09-26: B1 completed before travel
- 2026-09-26: Load Integration omitted for logistics/context and not represented as a completed session
- 2026-09-27: no structured training and no synthetic session row
- no make-up volume was added

One bounded W38 context event is present:

```text
event_id:         2026-09-26-01
start:            2026-09-26
end:              2026-09-27
type:             travel
subtype:          out_of_town_travel_start
protocol impact:  partial_training_interruption
outcome state:    transient_effect
related week:     2026-W38
```

The event explicitly states that the travel period continued beyond the W38 report boundary.

No redundant event rows were created for the schedule shift, cooler gym environment, shorter-sleep nights, brief B1 heart-rate excursion, or repeated subjective Load Integration ease. Those observations remain in the daily/training/report layers rather than turning the event index into a diary.

---

## 7. Weekly Lifecycle

The weekly report filenames remain continuous from W06 through W39.

Repository validation independently reports:

```text
34 reports continuous from W06 through W39
active = 2026-W39.md
```

Lifecycle state after rollover:

```text
2026-W38  Closed
2026-W39  Active
```

W39 covers:

```text
2026-09-28 through 2026-10-04
```

Its immediate weekly operating posture is:

```text
Consolidation / post-travel return observation
```

The broader Phase 2 substate remains:

```text
Consolidation / lock-in observation
```

W39 explicitly does not open as a progression week.

---

## 8. Current-State Synchronization

The following current-facing surfaces were reviewed for W39 active / W38 closed alignment:

- `LATEST.md`
- `README.md`
- `INDEX.md`
- `docs/OBSERVER_QUICKSTART.md`
- `docs/NEWCOMER_PATH.md`
- `tools/validate_coherence.py`

The observer and newcomer routes now point to W38 as the most recent closed report.

`README.md` and `LATEST.md` reflect the governed structured endpoints:

```text
daily biomarkers  231 rows through 2026-09-27
canonical sleep   231 rows through 2026-09-27
training          373 sessions through 2026-09-26
context events     50 events through 2026-09-27
```

The training endpoint remains intentionally earlier because the layer is session-indexed.

The live surfaces retain plain-language orientation while the more precise session-level execution vocabulary remains in the weekly report, structured layer, and terminology documentation.

---

## 9. Governance Interpretation Boundary

Week 38 opened with reserve replication as an observation target.

The public closeout does **not** claim that reserve was replicated because no second interpretable capacity probe occurred.

Instead, the report records the narrower supported findings:

- five consecutive complete B1 + Load Integration days remained available
- the registered prescription remained unchanged
- repeated subjective ease did not trigger arbitrary escalation
- the prior reserve observation remained preliminary
- end-of-week travel displaced formal exposure without creating training debt
- favorable or less-favorable short-window wearable values did not independently command progression or unloading

The W38 descriptor `governance` is therefore used as a retrospective operating summary, not a new phase declaration or a quantitative biological endpoint.

W39 correctly carries ordinary post-travel return ahead of any progression decision.

---

## 10. Supplementation Context Boundary

The reduced supplementation architecture effective 2026-09-18 remains disclosed as material background protocol context.

The W38 closeout and W39 opening do not attribute sleep, HR, HRV, bodyweight, recovery, or training changes to that transition.

No retrospective supplement-withdrawal experiment, causal label, backdated prediction, or new structured provenance locator was invented during rollover.

---

## 11. Data-Quality and Source-Role Boundary

DQ-011 remains unresolved for the recorded 2026-09-08 daily `resting_hr_bpm=64` value.

The governing treatment remains:

- preserve the recorded value
- do not infer a neighboring replacement
- do not substitute sleep heart rate
- resolve only from originating source evidence

The W37 v1.31 HRV note/field difference also remains source-role documented without averaging or inferred correction.

Two previously identified hardening opportunities remain non-blocking and outside this rollover's data semantics:

1. the legacy `body_temp_f` name can be misread as core body temperature even though current RingConn-derived observations are wearable skin temperature
2. canonical sleep provenance remains less granular than the daily/training/context row-level private-source locator model

Neither issue was silently "fixed" inside the weekly rollover.

---

## 12. Release, DOI, Phase, and Model-Error Invariants

The rollover does not alter the published release boundary.

The following remain fixed:

```text
published release:       v1.1.0
frozen release commit:   92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
version DOI:             10.5281/zenodo.22759132
all-versions DOI:        10.5281/zenodo.20815611
```

`CITATION.cff`, `CODEMETA.json`, `VERSIONING.md`, `PHASE_MAP.md`, `data/model_error/model_error_gap_v1.csv`, and `data/DATA_QUALITY_NOTES.md` are not in the rollover changed-file set.

Scientific/governance state remains:

- Phase 2 — Load Integration
- broader substate: Consolidation / lock-in observation
- Phase 2D: undeclared
- Model Error records 041–046: closed
- Record 043: not supported / `overall_improvement_not_met` / over
- August snapshot adjudication: unchanged
- DQ-011: unresolved

---

## 13. Privacy and Distribution Review

Before the audit artifact itself was added, PR #23 contained 15 changed public text files and no binary artifact.

A scan of all newly added diff lines found no:

- email address
- phone number
- Social Security number pattern
- local Unix/container absolute path
- Windows user/local path
- private spreadsheet filename or extension
- private family names screened during source lock
- named retailer
- lodging brand
- unnecessary memorial-site or deceased-family detail
- exact travel destination
- intimate sexual detail

The exact retained identifier `Daniel_Dataset_v1.32`, byte count, and SHA-256 remain bounded provenance metadata; the private workbook itself is not published.

The public travel representation remains generalized to out-of-town travel, logistics-directed training interruption, and novel sleep environment where relevant.

---

## 14. Automated Validation

Draft PR #23 executes the repository's actual GitHub Actions validation workflow.

After the narrow bodyweight-comparison wording correction, repository validation run:

```text
36647649883
```

completed successfully on the exact pre-audit content head:

```text
6d643b8513678500803c895b5272dc67a451c499
```

All four validation layers passed:

- core repository validator
- machine-readable layer validator
- August snapshot cross-layer validator
- post-release coherence validator

The core validator additionally reported:

```text
34 reports continuous from W06 through W39
active = 2026-W39.md
daily/sleep endpoint = 2026-09-27
training endpoint = 2026-09-26, valid under session-indexed semantics
errors = 0
result = PASS
```

The machine-readable validator reported:

```text
overall = PASS
errors = 0
warnings = 0
daily rows = 231
training rows = 373
unique session IDs = 373
context rows = 50
unique event IDs = 50
```

The audit artifact and changelog entry are part of the final validation boundary. Merge readiness requires the final audited branch head to receive another green validation run without subsequent content changes.

---

## 15. Diff Boundary

Relative to `main`, the exact pre-audit content head contained:

```text
18 commits ahead
0 commits behind
15 changed files
615 additions
184 deletions
```

The changed-file set is limited to:

- the five governed W38 data/provenance append targets
- `data/DATA_COVERAGE.md`
- W38/W39 reports
- current-state/navigation surfaces
- the coherence validator
- changelog

No release metadata file, phase map, Model Error ledger, DQ ledger, August snapshot table, epigenetic table, provider artifact, or protected binary source appears in the changed-file set.

The deletions are confined to replacement of active/current-state prose and conversion of the W38 active skeleton into its closed retrospective form.

---

## Audit Verdict

**GO.**

The W38 closeout and W39 rollover are internally coherent across source provenance, structured evidence, arithmetic, sleep semantics, training exposure, context classification, weekly lifecycle, current-state surfaces, data-quality governance, privacy review, release boundaries, and automated validation.

The strongest integrity findings are:

1. all five governed historical data/provenance prefixes are preserved exactly
2. W38 quantitative claims reproduce directly from the public structured rows
3. explicit Sleep Log awake totals remain preserved rather than reverse-derived
4. zero-session travel days remain zero-session days rather than acquiring synthetic training rows
5. reserve replication remains unresolved rather than being promoted into a progression claim
6. W39 opens with ordinary post-travel return before escalation
7. published v1.1.0 release identity, Phase 2 state, Model Error outcomes, and DQ-011 remain fixed
8. the public travel/context representation remains privacy-minimized
9. the audit identified and corrected one narrow derived-arithmetic wording issue without changing any underlying data
10. all four repository validation layers passed on the corrected pre-audit content head

The branch is suitable for the final merge-readiness gate once the audit artifact and changelog entry themselves have a green repository-validation run.

Any subsequent content change reopens that validation gate.
