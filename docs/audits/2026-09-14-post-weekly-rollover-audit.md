# Post-Weekly Rollover Verification Audit — 2026-09-14

**Audit type:** Post-W36 closeout / W37 initialization verification and semantic audit  
**Repository:** `CDHughett/daniel-longitudinal-public`  
**Branch baseline:** `main`  
**Audit baseline head:** `f3d4065e7fcb82cca92621cc84b87ec994f626c8`  
**Audit posture:** Live-repository verification, arithmetic cross-check, lifecycle review, provenance review, privacy review, and narrow remediation  
**Phase posture:** Phase 2 — Load Integration; no Phase 2D declaration  
**Release posture:** No release-version or DOI change

---

## Purpose

This audit verifies the live repository after the 2026-W36 closeout and 2026-W37 initialization.

The review covers:

- W36 arithmetic and completed training exposure
- canonical daily, sleep, training, and context-event endpoints
- append-only protection of pre-W36 structured evidence
- private-source provenance registration
- weekly report lifecycle integrity
- synchronization of `LATEST.md`, `README.md`, and `INDEX.md`
- W37 initialization and re-entry framing
- DQ-011 handling
- model-error, phase, snapshot, and release boundaries
- public-report privacy minimization
- repository validation state

The audit is not a new biological interpretation layer. It verifies whether the rollover accurately represents already-governed evidence and corrects only narrow documentation defects identified during review.

---

## Verified Live State

At the audited baseline:

- `reports/2026-W36.md` is closed
- `reports/2026-W37.md` is active
- W37 is the latest weekly report
- `LATEST.md`, `README.md`, and `INDEX.md` identify W37 as active and W36 as the most recent closed window
- daily biomarkers contain 217 continuous rows through 2026-09-13
- canonical sleep contains 217 continuous rows through 2026-09-13
- training contains 350 completed-session rows through 2026-09-12
- context events contain 45 bounded rows through 2026-09-13
- the terminal 2026-09-13 date is represented without a synthetic training row because training is session-indexed and no formal session was completed that day
- the protected historical training prefix through 2026-08-30 remains 325 sessions
- `Daniel_Dataset_v1.30` is hash-registered as the retained private W36 source
- DQ-011 remains open for the recorded 2026-09-08 daily resting-heart-rate value of 64 bpm
- Model Error records 041–046 remain closed
- Record 043 remains closed / not supported / `overall_improvement_not_met` / `over`
- Phase 2D remains undeclared
- archived release metadata remain at v1.0.0 pending a separate release-readiness process

---

## W36 Arithmetic Cross-Check

The canonical public W36 rows independently reproduce the principal closeout values.

### Daily biomarkers

Available morning bodyweights:

```text
234.3
234.1
233.6
232.3
233.7
233.0
```

Mean:

```text
233.5 lb
```

No morning bodyweight is present for 2026-09-13 because no travel scale was available.

Seven-day daily biomarker means:

```text
HRV:                  61.0 ms
resting heart rate:   48.9 bpm
average heart rate:   63.1 bpm
```

The resting-heart-rate mean intentionally uses the recorded 2026-09-08 value of 64 bpm. DQ-011 prevents an inferred replacement while source verification remains unresolved.

### Canonical sleep

Seven-night means:

```text
total sleep:          452.6 min ≈ 7h33m
deep sleep:            65.0 min ≈ 1h05m
REM sleep:             77.1 min ≈ 1h17m
sleep HRV:             67.0 ms
sleep average HR:      56.3 bpm
```

Consumer-wearable sleep staging remains a secondary evidence layer and is not strengthened by this arithmetic confirmation.

### Training

W36 completed-session rows reproduce:

```text
B1:                    6 × 55 min = 330 min
Load Integration:      5 × 45 min = 225 min
total sessions:        11
total formal training: 555 min
B1 distance:           6 × 3.02 mi = 18.12 mi
```

There is no LI row on 2026-09-12 and no B1 or LI row on 2026-09-13. The contextual event identifies travel logistics rather than a recovery-, pain-, motivation-, or performance-directed stop.

The report-level post-B1 descriptive mean of 231.5 lb is also reproduced from the six logged post-B1 values, while mixed GI-clearance states continue to limit direct serial comparability.

---

## Append-Only and Provenance Verification

The W36 machine-readable extension remains append-only relative to the pre-W36 structured baseline:

- daily biomarkers added seven W36 rows
- canonical sleep added seven W36 rows
- training added eleven completed-session rows
- context events added one bounded travel event
- no synthetic zero-duration training row was introduced
- no pre-W36 structured row was intentionally rewritten during the W36 extension

The protected training history through 2026-08-30 remains the 325-session prefix established before W35/W36 extension.

The private-source provenance manifest registers:

```text
source version: v1.30
filename:       Daniel_Dataset_v1.30
coverage:       2026-09-07 through 2026-09-13
size:           369318 bytes
SHA-256:        dcc566187f7dd47670d42096ef9e5d8dbed05e32cf5773d6984c35d487b1f7f3
status:         registered
```

The manifest also preserves the private workbook's mixed date-encoding state while the governed public extraction uses normalized ISO dates without altering the associated measurements or training values.

---

## Weekly Lifecycle Verification

The rollover satisfies the repository lifecycle:

```text
2026-W36
Closed / retrospective record

2026-W37
Active / latest report
```

The current-facing surfaces agree on W37 active / W36 prior closed.

W37 preserves the existing B1 + Load Integration architecture. Its active question is whether ordinary cadence returns after travel without:

- compensatory make-up volume
- forced workload progression
- protective unloading unsupported by multi-domain evidence
- manufactured portability testing

The Week 36 travel interruption is therefore carried forward as a natural re-entry observation rather than treated as proof of full travel portability.

---

## Findings and Narrow Remediation

### F01 — Public W36 report exposed unnecessary private travel detail

The closed W36 report named the lodging type and relationship context even though the public machine-readable event had already been correctly sanitized to the analytically relevant fact: out-of-town travel altered training access.

Those details were not required to interpret training availability, recovery, protocol behavior, or portability.

**Disposition:** Corrected. Public W36 wording now uses `out-of-town weekend travel` / `out-of-town travel` while preserving the timing, training interruption, and analytical interpretation unchanged.

This is a privacy-minimization correction, not a source-value, exposure, or outcome correction.

### F02 — W37 starting-state bullet conflicted with the report header and current-state surfaces

The W37 header, `LATEST.md`, `README.md`, and `INDEX.md` identified the current operating substate as:

```text
Consolidation / re-entry observation
```

but one W37 starting-state bullet still said the operating substate remained `Consolidation / lock-in observation`.

**Disposition:** Corrected. The W37 starting-state bullet now matches the active re-entry observation framing. No phase declaration or protocol change is implied.

### F03 — Transient `noop` administrative file exists only in Git history

During Batch 2 setup, a one-byte temporary file named `noop` was accidentally created on `main` and immediately deleted before the rollover branch was created.

**Disposition:** No tree remediation required. The audited repository tree contains no `noop` file. The two commits remain visible in history rather than being rewritten or concealed. They changed no scientific evidence, weekly metrics, phase state, model-error state, or release metadata.

---

## Boundaries Confirmed

This audit does not:

- change any W36 canonical measurement value
- change any completed training exposure
- infer a replacement for the 2026-09-08 resting-heart-rate value
- reopen or rescore Model Error 043 or any other closed record
- alter August snapshot source artifacts or checksum registrations
- declare Phase 2D
- modify the installed B1 + Load Integration protocol
- create a new prediction
- change `CITATION.cff`, `CODEMETA.json`, version number, release date, or DOI

The audit also does not upgrade preserved next-day function into evidence that recurrent early-night cardiovascular excursions are harmless. That pattern remains an observation requiring longitudinal tracking.

---

## Validation Gate

The Batch 2 rollover baseline had already passed repository validation on both the pull-request head and merged `main` state.

This Batch 3 audit/remediation is acceptable only if the final audit branch independently passes the repository's current validation workflow, including:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
python tools/validate_august_snapshot.py
```

The validator pass is a mechanical/governance check. It does not establish biological causality, clinical validity, or correctness of every interpretation.

---

## Audit Decision

**Weekly rollover integrity:** PASS, subject to the two narrow documentation corrections above  
**Machine-readable continuity:** PASS  
**Append-only W36 extension:** PASS  
**Private-source registration:** PASS  
**Current-state synchronization:** PASS  
**Model-error boundary:** PASS  
**Phase boundary:** PASS  
**Public privacy minimization:** PASS after F01 remediation  
**W37 semantic alignment:** PASS after F02 remediation  
**Release readiness:** not evaluated here; reserved for the separate v1.1.0 readiness audit

The repository is therefore ready to proceed to the dedicated v1.1.0 readiness audit without mixing release metadata changes into the weekly rollover process.
