# 2026-09-29 Validation and Temperature-Semantics Hardening Audit

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Baseline main:** `22b8c0ca662569fb4f9c03cedd2fc27c0ed10db2`  
**Hardening branch:** `hardening-weekly-rollover-temperature-semantics`  
**Pre-audit hardening head:** `17f1ff2823738978b5976cc36d520667cc5cc583`  
**Pull request:** #24 — Harden weekly rollover validation and temperature semantics  
**Audit date:** 2026-09-29  
**Verdict:** **GO**

---

## Scope

This audit reviews the first post-W38/W39 repository-hardening batch.

The hardening is deliberately separated from the completed weekly rollover. It does not modify the scientific closeout that was merged through PR #23.

The review covers:

- semantics of the legacy `body_temp_f` field
- backward-compatibility treatment of the v1 machine-readable schema
- the new latest-weekly-rollover validator
- current validation documentation
- normal CI integration
- release-candidate package validation coverage
- post-release coherence protection of the validator inventory
- repository change boundaries
- preservation of scientific, phase, prediction, DQ, release, tag, and DOI state

---

## 1. Temperature-Field Semantic Hardening

The public v1 dataset retains the column:

```text
body_temp_f
```

No column rename or historical value rewrite is performed.

Three current semantic surfaces now agree:

- `DATA_DICTIONARY.md`
- `schemas/machine-readable-layer-v1.md`
- `MEASUREMENT_SOURCES.md`

The clarified rule is:

> `body_temp_f` is a legacy v1 source-transcribed temperature field. For RingConn-derived Daily Biomarkers rows, the represented value is wearable skin temperature, not clinical/core body temperature.

The documentation explicitly prevents RingConn-derived values from being interpreted as:

- oral temperature
- tympanic temperature
- rectal temperature
- ingestible/core temperature
- a clinical fever measurement

Historical rows remain source-transcribed and provenance-governed.

The hardening intentionally avoids claiming that every historical `body_temp_f` row is RingConn skin temperature. Where the controlling source is RingConn-derived, the skin-temperature interpretation applies; other historical rows remain governed by their own provenance.

A possible future field such as `wearable_skin_temp_f` is documented only as a schema-evolution option. It is not introduced into v1.

---

## 2. No Scientific Data Mutation

Relative to `main`, the pre-audit hardening branch does not modify:

- `data/daily_biomarkers_v1.csv`
- `data/sleep_longitudinal_v1.csv`
- `data/training_blocks_v1.csv`
- `data/context_events_v1.csv`
- `data/source_provenance/daniel_dataset_private_manifest.csv`
- `data/biomarker_snapshot.csv`
- `data/epigenetic_longitudinal.csv`
- `data/model_error/model_error_gap_v1.csv`
- `data/DATA_QUALITY_NOTES.md`
- any weekly report

The hardening therefore changes semantic documentation and validation architecture, not evidence values or retrospective weekly interpretation.

---

## 3. Latest Weekly Rollover Validator

The batch adds:

```text
tools/validate_weekly_rollover.py
```

The validator is read-only and dynamically identifies:

1. the newest weekly report
2. the immediately preceding weekly report

It then requires the newest report to be `Active` and the preceding report to be `Closed`.

For the newest closed observation window, it verifies:

- both active and closed windows are seven days
- the active window begins the day after the closed window ends
- seven Daily Biomarkers rows exist for the closed window
- seven canonical sleep rows exist for the closed window
- the Daily Biomarkers and canonical sleep date sets exactly match the closed window
- the closed report contains the standardized `Structured Weekly Metrics` rows
- bodyweight, daily HRV, resting HR, daily average HR, sleep HRV, sleep average HR, total sleep, deep sleep, and REM are recomputed from the public CSVs
- B1 and Load Integration session counts are recomputed
- scalar closed-week training minutes are recomputed
- B1 minutes and miles agree with the report note
- Load Integration minutes agree with the report note
- the total completed-session count agrees with the report note
- the latest daily and sleep endpoints equal the latest closed-week endpoint
- there are no completed training rows later than the latest closed-week endpoint
- at least one `registered` private-source manifest row exactly covers the closed observation window

The validator uses decimal half-up reporting precision rather than Python binary floating-point rounding for one-decimal and whole-minute report values.

It does not:

- infer missing observations
- fabricate zero-session rows
- decide whether an omitted session was appropriate
- interpret biological significance
- score Model Error records
- authorize progression
- declare a phase transition

---

## 4. Live W38/W39 Validator Reproduction

On the current repository state, the new validator derives:

```text
active_report: 2026-W39.md
closed_report: 2026-W38.md
closed_window: 2026-09-21 through 2026-09-27
daily_rows_in_closed_window: 7
sleep_rows_in_closed_window: 7
training_sessions_in_closed_window: 11
registered_sources_for_closed_window: v1.32
```

It independently reproduces:

```text
Morning bodyweight       230.2 lb
Daily biomarker HRV       67.1 ms
Resting heart rate        44.9 bpm
Daily average heart rate  60.4 bpm
Sleep HRV                 73.7 ms
Sleep average heart rate  50.7 bpm
Total sleep               7h29m
Deep sleep                1h16m
REM sleep                 58m
B1 sessions               6
Load Integration sessions 5
Total formal training     556 min
```

The validator passes against the completed W38/W39 rollover without requiring hardcoded W38 values.

---

## 5. Validation Architecture

The current read-only Python validation suite is now five validators:

```text
tools/validate_repository.py
tools/validate_machine_readable.py
tools/validate_weekly_rollover.py
tools/validate_august_snapshot.py
tools/validate_coherence.py
```

The new validator is represented in:

- `tools/README.md`
- `VERIFICATION.md`
- `docs/FOR_OBSERVERS.md`
- `docs/OBSERVER_QUICKSTART.md`
- `INDEX.md`
- `LATEST.md`

The verification guide now distinguishes six automated/mechanical verification levels because artifact checksum verification remains a separate non-Python verification layer.

---

## 6. Coherence Anti-Drift

`tools/validate_coherence.py` was hardened so current documentation cannot silently drop the weekly-rollover validator.

The coherence validator now requires:

- the weekly rollover validator command in `VERIFICATION.md`
- the weekly rollover validator in `tools/README.md`
- the weekly rollover validator in the observer quickstart
- the weekly rollover validator in the skeptical-observer reference
- the weekly rollover validator in the repository index
- the current validator-active statement in `LATEST.md`

The post-release coherence heading check was also advanced from Verification Level 4 to Level 6 to match the expanded verification architecture.

---

## 7. Release-Candidate Package Verification

A separate audit finding was addressed in the same hardening batch.

Before this change, `.github/workflows/release-candidate-package.yml` reran:

```text
validate_repository.py
validate_machine_readable.py
validate_august_snapshot.py
```

but did not rerun the post-release coherence validator, despite current archive documentation describing the package workflow as rerunning all validators.

The workflow now runs the complete current five-validator suite:

- before package construction
- again from the extracted immutable archive

This includes both:

- `validate_weekly_rollover.py`
- `validate_coherence.py`

The release-candidate package workflow runs on pushes to `main`, so final confirmation of this path is a post-merge gate rather than a pre-merge PR event.

---

## 8. Pull-Request Validation

PR #24 validation run:

```text
36648886791
```

completed successfully on pre-audit hardening head:

```text
17f1ff2823738978b5976cc36d520667cc5cc583
```

All five validator steps passed:

- core repository validator
- machine-readable layer validator
- latest weekly rollover validator
- August snapshot cross-layer validator
- post-release coherence validator

The weekly-rollover validator specifically reported:

```text
active_report = 2026-W39.md
closed_report = 2026-W38.md
closed_window = 2026-09-21 through 2026-09-27
daily rows = 7
sleep rows = 7
training sessions = 11
registered source = v1.32
Result = PASS
```

---

## 9. Change Boundary

Relative to the exact post-PR-23 `main` baseline, the pre-audit hardening branch changes only documentation, validator code, validation workflows, and changelog state.

No scientific CSV, weekly report, Model Error ledger, DQ ledger, snapshot dataset, epigenetic dataset, phase map, release metadata, Git tag, or DOI record is changed.

The hardening therefore does not create a new biological observation or a new research intervention.

---

## 10. Invariants

The following remain unchanged:

```text
Active weekly report:        2026-W39
Most recent closed report:   2026-W38
Phase:                       Phase 2 — Load Integration
Broader substate:            Consolidation / lock-in observation
Phase 2D:                    undeclared
Model Error 041–046:         closed
DQ-011:                      unresolved
Published release:           v1.1.0
Version DOI:                 10.5281/zenodo.22759132
All-versions DOI:            10.5281/zenodo.20815611
Frozen v1.1.0 commit:        92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
```

---

## Audit Verdict

**GO.**

The hardening improves two distinct repository-integrity boundaries without mutating the evidence layer:

1. a legacy temperature field can no longer be reasonably read as a universal core-body-temperature measurement when the controlling source is RingConn-derived
2. the newest closed weekly report now has a dedicated mechanical arithmetic/lifecycle/provenance validator rather than relying on manual weekly audit alone

The PR is suitable for final merge-readiness review after this audit artifact and its changelog entry themselves pass the full five-validator pull-request workflow.

After merge, the main-branch release-candidate package workflow must also pass because this batch changes that workflow's validator inventory. Any content change after the final green audited head reopens the validation boundary.
