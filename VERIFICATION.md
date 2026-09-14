# Verification Guide

This repository supports external verification at three complementary automated/mechanical levels:

1. **artifact verification** — confirms the identity of registered files
2. **repository validation** — checks the mechanical integrity and governance-protected structure of the archive
3. **machine-readable semantic validation** — checks the current daily/training/event schema contract and cross-file relationships

Human semantic review remains a separate layer after automated validation.

Verification and temporal anchoring are related, but they are not the same layer.

- **verification** confirms file and repository integrity
- **temporal anchoring** explains where an artifact belongs in time
- **interpretation** evaluates what the preserved evidence may mean

These roles should remain separate.

---

# Verification Levels

## Level 1 — Artifact Verification

Artifact verification uses SHA-256 checksums to confirm that a file matches the version registered by the archive.

Examples include:

- laboratory PDFs
- DEXA reports
- Bod Pod images
- VO₂ reports
- snapshot artifacts
- RingConn source exports

A matching checksum confirms file identity.

It does not independently establish:

- clinical validity
- measurement accuracy
- privacy completeness
- causal interpretation
- comparability with another provider or device
- absence of source-side error

---

## Level 2 — Repository Validation

Repository validation checks the archive as an integrated system.

The local validator reviews:

- required repository structure
- Markdown links and anchors
- fenced-code balance
- CSV parsing and row widths
- duplicate CSV headers
- checksum manifests
- canonical sleep continuity
- governed sleep-data warnings
- weekly-report continuity
- exactly one active weekly report, with the latest report required to be active
- current-state alignment across `LATEST.md`, `README.md`, and `INDEX.md`
- live row-count and endpoint alignment between canonical datasets and `data/DATA_COVERAGE.md`
- session-aware endpoint semantics: daily biomarkers and canonical sleep must share the represented endpoint; completed training may end earlier on terminal zero-session days but may not extend beyond daily coverage
- model-error continuity
- preserved closed/adjudicated state of records 041–046
- selected protected actual values and error directions for those closed records
- preserved prospective registration state for records 041–046
- preservation of the original registered prediction narrative for records 041–046
- release-metadata alignment
- RingConn source-export byte preservation

The endpoint distinction is documented in [`docs/VALIDATION_ENDPOINT_SEMANTICS.md`](docs/VALIDATION_ENDPOINT_SEMANTICS.md).

The validator is read-only.

It does not:

- edit files
- repair values
- infer missing observations
- synthesize zero-duration training rows to force endpoint equality
- normalize provider exports
- independently score predictions
- recompute model-error outcomes
- change prediction status
- rewrite history
- alter checksums

---

## Level 3 — Machine-Readable Semantic Validation

The machine-readable validator checks the public daily/training/event layer defined in:

```text
schemas/machine-readable-layer-v1.md
```

Validator path:

```text
tools/validate_machine_readable.py
```

Current protected checks include:

- exact required headers
- continuous daily-biomarker dates across the represented interval
- unique daily dates
- the protected 325-session historical training prefix through 2026-08-30
- unique training `session_id` values across the live appendable dataset
- canonical `private_workbook:` / `private_pdf:` `source_ref` syntax
- date parsing and represented-interval bounds
- numeric-field syntax
- controlled vocabularies
- `snake_case` extensible vocabularies
- v1 `duration_min` expression semantics
- unique context-event IDs across the current event index
- event interval ordering
- related-week syntax
- model-error cross-reference existence
- cross-file date relationships

The historical training prefix through 2026-08-30 remains protected at exactly 325 sessions. Governed rows after that boundary may append without changing the protected prefix; the validator reports both prefix and live-row counts.

This validator is also read-only. It does not infer missing sessions, rewrite source references, classify biological meaning, or repair the archive.

---

## Snapshot-Specific Cross-Layer Validation — August 2026

A completed snapshot may receive a narrow additional validator when the same governed state is represented across multiple layers.

The August 2026 validator is:

```text
tools/validate_august_snapshot.py
```

It protects the completed August snapshot across:

- `data/biomarker_snapshot.csv`
- `data/epigenetic_longitudinal.csv`
- `data/source_provenance/2026-08-trudiagnostic-reconciliation.md`
- `data/model_error/record_043_closure.md`
- `snapshots/2026-08/checksums.txt`
- all seven protected August source artifacts

Current protected August state includes:

- canonical TruDiagnostic event `2026-08-17` at `05:37 local`
- DEXA date `2026-08-17`
- Bod Pod date `2026-08-18`
- three core aging outputs
- all 11 system/organ ages
- all 19 TruHealth domain scores
- completed DEXA and Bod Pod numeric fields represented in the integrated snapshot
- molecular agreement between the integrated snapshot and longitudinal epigenetic table
- expected molecular source labels
- DQ-010 source-role reconciliation
- Record 043 endpoint/value/outcome alignment
- fixed SHA-256 identities for all seven August artifacts

The validator intentionally uses committed fixed expectations rather than learning expected values from the same mutable files it checks. A legitimate future source-backed correction to a protected August value therefore requires an explicit update to both the affected data/provenance layer and this validator expectation.

It does not interpret the biological result, rescore Record 043, alter preregistered thresholds, regenerate checksums, change source artifacts, or declare a phase transition.

---

# Local Repository Validator

Validator path:

```text
tools/validate_repository.py
```

The validator can inspect either:

- an extracted repository directory
- a downloaded GitHub ZIP package

---

## Requirements

- Python 3.11 or newer is recommended
- no third-party Python packages are required
- run the command from a local clone or extracted repository package

The validator uses only the Python standard library.

---

# Validate an Extracted Repository

## Windows — Command Prompt

From the repository root:

```text
python tools\validate_repository.py
```

A specific repository directory may also be supplied:

```text
python tools\validate_repository.py "C:\path\to\daniel-longitudinal-public"
```

The two additional semantic/cross-layer validators may be run from the repository root with:

```text
python tools\validate_machine_readable.py
python tools\validate_august_snapshot.py
```

---

## Windows — PowerShell

From the repository root:

```text
python .\tools\validate_repository.py
```

A specific directory may also be supplied:

```text
python .\tools\validate_repository.py "C:\path\to\daniel-longitudinal-public"
```

The additional validators may be run with:

```text
python .\tools\validate_machine_readable.py
python .\tools\validate_august_snapshot.py
```

---

## macOS or Linux

From the repository root:

```text
python3 tools/validate_repository.py
```

A specific directory may also be supplied:

```text
python3 tools/validate_repository.py /path/to/daniel-longitudinal-public
```

The additional validators may be run with:

```text
python3 tools/validate_machine_readable.py
python3 tools/validate_august_snapshot.py
```

---

# Validate a GitHub ZIP

The validator can inspect a repository ZIP directly.

It will:

1. test ZIP CRC integrity
2. reject unsafe archive paths
3. extract the package into a temporary directory
4. identify the repository root
5. run the full repository validation
6. remove the temporary extraction when complete

## Windows

```text
python tools\validate_repository.py "C:\path\to\daniel-longitudinal-public-main.zip"
```

## macOS or Linux

```text
python3 tools/validate_repository.py /path/to/daniel-longitudinal-public-main.zip
```

The validator does not modify the ZIP.

---

# Machine-Readable Output

Use `--json` to return structured output.

## Windows

```text
python tools\validate_repository.py --json
```

## macOS or Linux

```text
python3 tools/validate_repository.py --json
```

A ZIP or repository path may be combined with the option:

```text
python tools\validate_repository.py "C:\path\to\repository.zip" --json
```

JSON output includes:

- repository root
- overall result
- error count
- warning count
- validation metrics
- individual findings

The core and machine-readable validators support local command-line execution, and the repository validator supports `--json` structured output. The August snapshot validator also supports local command-line execution with human-readable pass/fail output.

Repository validation is also executed automatically in GitHub Actions as described below.

---

# Exit Codes

The validator distinguishes mechanical failures from governed warnings.

| Exit code | Meaning |
|---:|---|
| `0` | No validation errors |
| `1` | One or more validation errors |

Warnings do not cause a nonzero exit code.

This distinction is intentional.

A documented data-quality warning should not make the repository mechanically invalid.

---

# Result Types

## PASS

A check completed without identifying a mechanical or governance-protected problem.

Examples:

- all checksum entries match
- all CSVs parse
- weekly reports are continuous
- daily biomarkers and canonical sleep share the represented endpoint
- session-indexed training ends on or before the daily endpoint and may legitimately end earlier when terminal represented dates contain no completed session
- RingConn bytes match the registered source package
- records 041–046 retain their protected closed/adjudicated states
- protected closed-record actual values and error directions remain unchanged
- record 043 retains `actual_value=overall_improvement_not_met` and `error_direction=over`
- records 041–046 retain `calibration_state=pre`
- records 041–046 retain their original registered prediction narratives at the beginning of `notes`
- August protected structured values agree across the integrated and longitudinal molecular layers
- August protected artifacts retain their fixed registered identities

---

## WARN

A known or governed limitation remains visible.

Warnings may include:

- DQ-001 awake-minute and awakening-count duplication
- DQ-002 and DQ-003 sleep-stage differences
- no weekly report explicitly marked active
- another documented semantic issue that does not break repository structure

A warning means:

- review the relevant documentation
- preserve the uncertainty
- do not perform automatic correction

It does not necessarily mean repository repair is required.

---

## ERROR

A mechanical or governance-protected validation failed.

Examples include:

- missing required file
- malformed CSV
- checksum mismatch
- missing Markdown target
- duplicate canonical sleep date
- missing date inside the canonical sleep interval
- daily-biomarker and canonical-sleep endpoint mismatch
- training extending beyond the represented daily endpoint
- release-metadata mismatch
- protected closed prediction record reopened
- protected closed prediction record losing its recorded actual outcome
- protected closed prediction record drifting from its registered adjudicated actual value
- protected closed prediction record drifting from its recorded error direction
- protected preregistered record changing `calibration_state` from `pre`
- protected registered prediction narrative being removed, replaced, or altered
- RingConn source bytes changed
- August protected snapshot value or source identity drifting from its committed state
- August structured molecular layers disagreeing with each other
- unsafe ZIP path

Errors require review before the repository should be treated as fully verified.

---

# Expected Governed Warnings

The current archive may report warnings for already documented sleep-quality items.

## DQ-001

Affected interval:

```text
2026-05-18 through 2026-05-31
```

Current issue:

```text
awake_min = awakenings_count
```

The RingConn direct export provides a correction candidate for `awake_min`.

`awakenings_count` remains unresolved.

No automatic correction is authorized.

---

## DQ-002

Affected date:

```text
2026-03-31
```

Current canonical sleep-stage difference:

```text
16 minutes
```

The direct RingConn export provides candidate source evidence for a narrow light-sleep correction.

No correction is made by the validator.

---

## DQ-003

Affected date:

```text
2026-04-02
```

Current canonical sleep-stage difference:

```text
14 minutes
```

The direct RingConn export provides candidate source evidence for a narrow light-sleep correction.

No correction is made by the validator.

---

# Validator Check Inventory

## Repository Structure

The validator checks for required paths including:

- `README.md`
- `CHANGELOG.md`
- `CODEMETA.json`
- `CITATION.cff`
- `PHASE_MAP.md`
- `STATE_TRANSITIONS.md`
- canonical sleep data
- primary model-error data
- reports
- snapshots

It also reports:

- total file count
- zero-byte files

---

## Markdown

The validator checks:

- relative Markdown targets
- internal anchors
- paths escaping the repository root
- fenced-code balance

External web links are not tested by the local validator.

An external URL may fail even when repository validation passes.

---

## CSV Structure

Every CSV is checked for:

- valid parsing
- header presence
- duplicate headers
- consistent row width

The validator does not judge every field for biological plausibility.

Semantic issues remain governed separately.

---

## Checksum Manifests

Every file named:

```text
checksums.txt
```

is evaluated.

The validator checks:

- manifest syntax
- target existence
- repository path safety
- SHA-256 agreement

A mismatch is an error.

The validator does not regenerate manifests.

---

## Canonical Sleep

The validator checks:

- ISO date parsing
- duplicate dates
- missing dates inside the represented interval
- sleep-stage totals
- the governed DQ-001 interval

Known field-level discrepancies are reported as warnings.

The validator does not edit:

```text
data/sleep_longitudinal_v1.csv
```

---

## Current-State Endpoint Alignment

The repository validator derives live coverage from the canonical daily, sleep, training, and context-event datasets and compares those values with `data/DATA_COVERAGE.md`.

Endpoint semantics are intentionally asymmetric because the datasets have different observation grains:

```text
daily_biomarkers_v1.csv:
one row per represented day

sleep_longitudinal_v1.csv:
one row per represented day

training_blocks_v1.csv:
zero to many completed session rows per represented day
```

Therefore:

- daily biomarkers and canonical sleep must end on the same represented day
- training may end earlier if the later represented day or days contain zero completed sessions
- training may not extend beyond the daily represented interval
- `DATA_COVERAGE.md` must report the actual training row count and actual latest completed-session date
- the validator does not create a placeholder session to erase a legitimate zero-session day

See [`docs/VALIDATION_ENDPOINT_SEMANTICS.md`](docs/VALIDATION_ENDPOINT_SEMANTICS.md) for the compact governing rule.

---

## Weekly Reports

The validator checks:

- continuity of `2026-W##.md` report filenames
- missing weekly indices
- the number of reports marked active

More than one active report is an error.

No active report is a warning.

The validator does not close or open a weekly report.

---

## Model-Error Register

The validator checks:

- record-ID parsing
- duplicate IDs
- sequence continuity
- continuity through record 046
- presence of protected closed records 041–046
- closed status of records 041–046
- preservation of their registered predictions
- preservation of their adjudicated actual values
- preservation of their recorded error directions
- preservation of record 043 `actual_value=overall_improvement_not_met`
- preservation of record 043 `error_direction=over`
- preservation of `calibration_state=pre` for records 041–046
- preservation of the exact original registered prediction narrative for records 041–046

The validator treats prediction-registration provenance as distinct from prediction lifecycle.

---

## Registration-Provenance Protection

The currently protected prospective registration block is:

```text
041
042
043
044
045
046
```

Each of these records must retain:

```text
calibration_state = pre
```

This field records the state in which the prediction was registered.

It does **not** mean:

```text
prediction is currently awaiting evaluation
```

and it does not become:

```text
post
```

merely because the prediction has later been scored or closed.

A prospectively registered prediction remains historically:

```text
pre
```

after adjudication.

The validator therefore treats a later mutation such as:

```text
pre
→
post
```

as registration-provenance drift and returns an error.

---

## Registered Prediction-Narrative Protection

For records 041–046, the validator contains the preserved original prospective `Prediction:` narrative.

The `notes` field must begin with that registered narrative.

After an outcome window closes, later information may be appended, for example:

```text
Prediction: [original registered prospective text]

Closure: [later retrospective adjudication]
```

The closure text may supplement the historical record.

It must not replace or rewrite the original prediction.

This protects the distinction:

```text
what was predicted before the outcome
```

from:

```text
what was concluded after the outcome
```

The validator compares the beginning of each protected record's `notes` field with its registered narrative.

If the original narrative is:

- removed
- replaced
- substantively edited
- reordered behind closure text

the validator returns an error.

This protection is intentionally explicit rather than dynamically inferred from current row contents.

Otherwise, a corrupted row could become the validator's own new reference state.

---

## Protected Open Records

No record in the currently protected 041–046 block remains open.

The validator retains an explicit empty protected-open set so that future prospective records can be added deliberately rather than inferred dynamically from current row contents.

---

## Protected Closed Records

The protected closed set currently includes:

```text
041
042
043
044
045
046
```

The validator requires these records to remain closed and protects selected adjudicated fields needed to prevent accidental outcome drift.

Current protected outcomes include:

```text
041:
actual = stable
error_direction = none

042:
actual = continued_adaptation
error_direction = under

043:
actual = overall_improvement_not_met
error_direction = over

044:
actual = 0
error_direction = under

045:
actual = partial_reconvergence
error_direction = none

046:
actual = failed_autonomic_recompression
error_direction = over
```

These checks protect the committed adjudicated state.

They do not cause the validator to independently calculate or rescore the predictions.

---

# RingConn Source Export Protection

The repository contains three preserved RingConn provider exports under:

```text
data/source_exports/ringconn/2026-07-21/
```

The validator protects:

- exact byte size
- SHA-256 identity
- CRLF line endings
- provider header structure
- row count

The repository `.gitattributes` file contains:

```text
data/source_exports/**/*.csv -text
```

This prevents Git from silently normalizing the source-export line endings.

The source export remains an artifact.

It should not be rewritten merely to match a curated schema.

---

# Automated GitHub Validation

Workflow path:

```text
.github/workflows/validate.yml
```

The workflow runs on:

- pushes to `main`
- pull requests
- manual workflow dispatch

It uses read-only repository permissions:

```text
contents: read
```

and executes:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
python tools/validate_august_snapshot.py
```

The workflow is intentionally narrow. It does not edit files, commit corrections, publish releases, or replace human semantic review.

Local execution remains available for audits, ZIP verification, and debugging.

---

# Private-Source Provenance Verification

Private source-file identity, when an exact retained `Daniel_Dataset` source was available for hashing, is documented in:

```text
data/source_provenance/daniel_dataset_private_manifest.csv
```

The manifest separates row-level `source_ref` provenance from file-level SHA-256 identity.

A blank private-source hash is deliberate when the exact immutable historical source file was not available during registration. No digest is reconstructed from a screenshot, later workbook, or public extract.

AI-assisted maintenance is disclosed in:

```text
docs/AI_ASSISTANCE.md
```

AI assistance does not create a new evidence tier and does not override the repository source hierarchy.

---

# Notes

- Verification is reproducible across supported local environments.
- Snapshot directories are intended to remain independently inspectable.
- Source exports remain separate from curated datasets.
- Warnings preserve known uncertainty rather than hiding it.
- Errors identify mechanical or governance-protected failures.
- Validation never authorizes automatic biological correction.
- Open prediction records and scored prediction records require different protected states.
- Prospectively registered records retain their historical registration state after closure.
- Closing a prediction does not convert `calibration_state=pre` to `post`.
- Original registered prediction narratives must remain inspectable after adjudication.
- Closure language may be appended but must not replace the registered prediction.
- Closed prediction records may additionally protect selected adjudicated outcome fields.
- Closing a prediction after its registered outcome boundary does not authorize extending that prediction with later evidence.
- Later favorable evidence does not retrospectively rescue a failed fixed-window prediction.
- A governance miss does not automatically establish a biological effect.
- Snapshot-specific validators protect committed cross-layer state; they do not become source evidence or interpretation layers.
- Interpretation belongs in reports, datasets, model-error evaluation, and designated synthesis layers.

---

## Version Note

This guide was expanded on 2026-07-25 after introduction of:

```text
tools/validate_repository.py
```

The revision added:

- whole-repository validation
- directory and ZIP validation instructions
- JSON output
- exit-code behavior
- distinction between errors and governed warnings
- Markdown, CSV, checksum, sleep, weekly-report, model-error, metadata, and RingConn checks
- source-export byte-preservation verification
- privacy-verification boundaries
- recommended routine audit workflow
- manual-review limitations
- deferred GitHub Actions status

On 2026-08-12, the model-error validation boundary was extended from records 041–044 to records 041–045 after prospective registration of Model Error 045.

The 2026-08-12 update:

- added record 045 to the explicit protected open-record set
- required record 045 to remain open while its outcome window was incomplete
- required its registered prediction to remain present
- required protected actual and error fields to remain blank before scoring
- documented `methodology/open_prediction_evaluation_plan_045.md` as the separate scoring-governance artifact
- did not cause the validator to score record 045
- did not modify records 041–044
- did not alter any biological value, protocol, phase, collection plan, or release metadata

On 2026-08-17, the model-error validation boundary was updated after record 045 reached its preregistered scoring boundary and record 046 was prospectively registered.

The 2026-08-17 update:

- removed record 045 from the protected open-record set after completion of its fixed 2026-08-13 through 2026-08-16 scoring window
- protected record 045 as a closed/scored historical record
- required record 045 to retain its registered prediction
- required record 045 to retain a populated actual outcome
- did not independently recompute or adjudicate the record 045 result
- added record 046 to the explicit protected open-record set
- required record 046 to remain open while its prospective outcome window remained incomplete
- required record 046 to retain its registered prediction
- required record 046 actual and error fields to remain blank before scoring
- extended model-error continuity validation through record 046
- preserved the separation between record 045 closure and the later autonomic unload/reload question
- did not reopen or extend record 045
- did not alter any biological value, phase declaration, release metadata, checksum, or previously registered scoring rule

On 2026-08-18, the model-error validation boundary was aligned after formal adjudication of records 041, 042, and 044 and completion of the August physical artifact layer.

The 2026-08-18 update:

- removed records 041, 042, and 044 from the protected open-record set
- reduced the protected open-record set to records 043 and 046
- required records 043 and 046 to remain open and unscored
- required their protected actual and error fields to remain blank
- added records 041, 042, and 044 to the protected closed-record set alongside record 045
- required records 041, 042, 044, and 045 to remain closed
- protected record 041 actual value `stable` and error direction `none`
- protected record 042 actual value `continued_adaptation` and error direction `under`
- protected record 044 actual value `0` and error direction `under`
- protected record 045 actual value `partial_reconvergence` and error direction `none`
- recorded 041 as closed and supported
- recorded 042 as closed and not supported through continued adaptation
- recorded 044 as closed and not supported through a narrow snapshot-directed governance deviation
- preserved record 045 as closed and supported
- preserved record 043 as open pending TruDiagnostic provider results
- preserved record 046 as open through its fixed prospective evidence window
- did not independently recompute or adjudicate any of those outcomes
- preserved the original `open_prediction_evaluation_plan_041_044.md` artifact unchanged
- preserved the record 045 and 046 preregistration artifacts unchanged
- recorded the August physical source-artifact layer as complete and checksum-governed
- preserved the distinction between artifact verification and Model Error 043 biological interpretation
- left Phase 2 and the consolidation / lock-in observation substate unchanged
- left formal Phase 2D undeclared

On 2026-08-23, the verification boundary was hardened after the catch-up audit identified a narrow registration-provenance defect in record 045.

The 2026-08-23 update:

- recorded that prospectively registered Model Error records retain their registration-state provenance after adjudication
- explicitly protected `calibration_state=pre` for records 041–046
- treated `calibration_state` as registration metadata rather than a prediction-lifecycle field
- prevented a closed prospective prediction from being changed from `pre` to `post`
- protected the original registered `Prediction:` narrative for records 041–046
- required each protected `notes` field to begin with its preserved prospective prediction narrative
- permitted later closure language to be appended after the original prediction
- prevented closure language from replacing the registered prediction narrative
- documented the source-backed restoration of record 045 from `calibration_state=post` to `calibration_state=pre`
- documented restoration of record 045's original registered prediction narrative before its existing closure narrative
- left the record 045 supported outcome unchanged
- left its actual value, error direction, scoring window, thresholds, and calculated four-day means unchanged
- left records 041–044 unchanged
- left record 043 open pending its primary provider result
- left record 046 open and unscored while its prospective window remained active
- did not independently score or rescore any model-error record
- introduced no biological-value correction
- introduced no canonical sleep correction
- introduced no protocol modification
- introduced no phase declaration
- introduced no release increment

The 2026-08-23 provenance protection exists because a mechanically valid closed outcome is not sufficient if the archive loses the state in which the prediction was originally registered.

The validator protects both:

```text
registered prediction
+
later adjudicated outcome
```

as distinct pieces of historical evidence.

On 2026-08-24, the verification boundary was advanced after completion of the prospectively fixed Model Error 046 scoring window.

The 2026-08-24 update:

- removed record 046 from the protected open-record set
- reduced the protected open-record set to record 043 only
- added record 046 to the protected closed-record set
- preserved record 046's original prospective `Prediction:` narrative
- preserved `calibration_state=pre`
- protected record 046 as `status=closed`
- protected record 046 actual value as `failed_autonomic_recompression`
- protected record 046 error direction as `over`
- recorded the fixed 2026-08-20 through 2026-08-23 scoring window as complete
- recorded four-day means of daily HRV 60.25 ms, sleep HRV 63.25 ms, resting HR 52.0 bpm, and sleeping HR 54.0 bpm
- recorded that 1 of 4 autonomic thresholds was favorable
- preserved the finding that no multi-session functional regression occurred
- preserved the finding that normal B1 + Load Integration resumed without recovery-driven protocol reduction
- preserved later autonomic improvement as retrospective context without allowing it to alter the fixed-window score
- did not reopen or rescore record 045
- did not score record 043
- did not use DEXA, VO₂-max, Bod Pod, TruDiagnostic, or other August biological outcomes to score record 046
- did not alter any registered threshold or evidence window
- introduced no canonical sleep correction
- introduced no protocol change
- introduced no phase declaration
- introduced no release increment

The 2026-08-24 update therefore advanced the protected model-error lifecycle state to:

```text
041:
closed / supported

042:
closed / not supported — continued adaptation

043:
open / unscored

044:
closed / not supported — narrow snapshot-directed governance deviation

045:
closed / supported

046:
closed / failed_autonomic_recompression
```

The update did not alter:

- any source artifact
- any checksum
- any biological value
- any registered prediction value
- any registered prediction threshold
- any prior adjudicated outcome
- the then-pending record 043 outcome
- any physical protocol exposure
- any phase declaration
- any release metadata

---

## 2026-09-07 Machine-Readable Hardening Closeout

The September 7 closeout added the third validation layer and activated lightweight CI.

The live training layer was standardized to 325 canonical private-source `source_ref` values. During the migration, an intermediate commit temporarily contained only 251 training rows. The full 325-row source set was immediately restored, the migration was rerun deterministically, and the validator was hardened with an explicit 325-row guard so that equivalent accidental row loss now fails validation.

GitHub Actions run `34069047100` on commit `5e6801d0c08f506d7fc49ad3852a960d1558dbf3` completed successfully:

```text
core repository validator:
PASS
0 errors
2 governed warnings
9 passes

machine-readable validator:
PASS
0 errors
0 warnings
203 daily rows
325 training rows / 325 unique session IDs
42 context events
canonical source refs required
```

The two core-validator warnings remain the already governed canonical-sleep issues documented in `data/DATA_QUALITY_NOTES.md`.

This hardening did not change biological measurements, canonical sleep values, registered prediction wording, adjudicated model-error outcomes, phase status, physical protocol state, release version, release date, or DOI.

---

## 2026-09-10 Record 043 Closure Protection

The September 10 update advanced the protected Model Error 043 lifecycle after the August TruDiagnostic source reports were archived, integrated, source-reconciled, and evaluated under the preregistered record 043 rules.

The update:

- removed record 043 from the protected open-record set
- left the protected open-record set empty for records 041–046
- added record 043 to the protected closed-record set
- preserved its original prospectively registered `Prediction:` narrative
- preserved `calibration_state=pre`
- protected `status=closed`
- protected `actual_value=overall_improvement_not_met`
- protected `error_direction=over`
- preserved the full criterion-by-criterion adjudication in `data/model_error/record_043_closure.md`
- updated primary trajectory concordance from 2/3 = 0.67 to 2/4 = 0.50
- left point and range UDI unchanged
- left state concordance unchanged
- preserved the August TruDiagnostic source-role reconciliation without modifying the provider PDFs
- did not alter the original 043 prediction wording, registered thresholds, May comparison baseline, physical protocol, phase state, release version, release date, or DOI

The current protected 041–046 lifecycle state is therefore:

```text
041 closed / supported
042 closed / not supported — continued_adaptation
043 closed / not supported — overall_improvement_not_met / over
044 closed / not supported — narrow snapshot-directed governance deviation
045 closed / supported
046 closed / failed_autonomic_recompression
```

---

## 2026-09-10 August Snapshot Cross-Layer Hardening

The post-snapshot cleanup added:

```text
tools/validate_august_snapshot.py
```

The validator protects the completed August snapshot against silent divergence between source-artifact identity, the integrated snapshot table, the longitudinal molecular table, DQ-010 collection provenance, and the formal Record 043 closure.

The existing read-only GitHub Actions workflow now executes all three validators on pull requests, pushes to `main`, and manual workflow dispatch.

This hardening does not change any source artifact byte, checksum registration, biological value, registered prediction wording or threshold, adjudicated outcome, physical protocol exposure, phase state, release version, release date, or DOI.

---

## 2026-09-14 Terminal Zero-Session Endpoint Semantics

The Week 36 closeout exposed a legacy validator assumption that day-indexed daily/sleep coverage and session-indexed training coverage must always share the same latest date.

The validation entry point was narrowed so that:

- daily biomarkers and canonical sleep must still share the represented endpoint
- training may end before that endpoint when terminal represented dates have no completed session
- training still fails validation if it extends beyond daily coverage
- no synthetic zero-duration training row is required to manufacture endpoint equality
- all pre-existing repository checks remain active through the delegated core validator

The change is validator/documentation infrastructure only. It does not append W36 data, alter historical training values, change protocol or phase state, change any model-error record, or change release metadata or DOI.
