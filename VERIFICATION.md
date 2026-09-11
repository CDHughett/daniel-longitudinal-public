# Verification Guide

This repository supports external verification at four complementary automated/mechanical levels:

1. **artifact verification** — confirms the identity of registered files
2. **repository validation** — checks the mechanical integrity and governance-protected structure of the archive
3. **machine-readable semantic validation** — checks the current daily/training/event schema contract and cross-file relationships
4. **snapshot-specific cross-layer validation** — protects completed snapshot values and provenance from silent divergence across source, structured, and adjudication layers

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
- model-error continuity
- preserved closed/adjudicated state of records 041–046
- selected protected actual values and error directions for those closed records
- preserved prospective registration state for records 041–046
- preservation of the original registered prediction narrative for records 041–046
- release-metadata alignment
- RingConn source-export byte preservation

Validator path:

```text
tools/validate_repository.py
```

The validator is read-only.

It does not:

- edit files
- repair values
- infer missing observations
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

## Level 4 — Snapshot-Specific Cross-Layer Validation

Completed high-value snapshot cycles may receive a dedicated validator when the same governed values are represented across multiple repository layers.

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
- the seven protected August source artifacts

Current August checks include:

- one integrated `2026-08` snapshot row
- canonical TruDiagnostic event date `2026-08-17`
- canonical collection time `05:37 local`
- DEXA date `2026-08-17`
- Bod Pod date `2026-08-18`
- three core aging outputs
- all 11 system/organ ages
- all 19 TruHealth domain scores
- completed DEXA and Bod Pod numeric fields represented in the integrated snapshot
- molecular value agreement between the integrated snapshot and epigenetic longitudinal table
- expected provider-source labels for the molecular rows
- DQ-010 source-role reconciliation language
- Record 043 endpoint/value/outcome alignment
- the exact registered SHA-256 identity of all seven August artifacts

The August validator intentionally hard-codes the committed snapshot state rather than deriving its expected values from the same mutable files it is checking. Otherwise simultaneous drift in multiple downstream layers could become self-consistent and escape detection.

A legitimate future source-backed correction to an August protected value therefore requires an explicit, reviewable update to both the affected source-derived layer and the dedicated validator expectation.

The August validator does not:

- independently interpret the biological meaning of the snapshot
- rescore Record 043
- alter the preregistered 043 thresholds
- infer a missing source value
- regenerate checksums
- alter source artifacts
- declare a phase transition

---

# Local Repository Validators

The validator suite can be run from an extracted repository directory.

`tools/validate_repository.py` additionally supports validating a downloaded GitHub ZIP package directly.

## Requirements

- Python 3.11 or newer is recommended
- no third-party Python packages are required
- run the command from a local clone or extracted repository package

The validators use only the Python standard library.

---

# Validate an Extracted Repository

## Windows — Command Prompt

From the repository root:

```text
python tools\validate_repository.py
python tools\validate_machine_readable.py
python tools\validate_august_snapshot.py
```

A specific repository directory may also be supplied to the core validator:

```text
python tools\validate_repository.py "C:\path\to\daniel-longitudinal-public"
```

## Windows — PowerShell

From the repository root:

```text
python .\tools\validate_repository.py
python .\tools\validate_machine_readable.py
python .\tools\validate_august_snapshot.py
```

A specific directory may also be supplied to the core validator:

```text
python .\tools\validate_repository.py "C:\path\to\daniel-longitudinal-public"
```

## macOS or Linux

From the repository root:

```text
python3 tools/validate_repository.py
python3 tools/validate_machine_readable.py
python3 tools/validate_august_snapshot.py
```

A specific directory may also be supplied to the core validator:

```text
python3 tools/validate_repository.py /path/to/daniel-longitudinal-public
```

---

# Validate a GitHub ZIP

The core repository validator can inspect a repository ZIP directly.

It will:

1. test ZIP CRC integrity
2. reject unsafe archive paths
3. extract the package into a temporary directory
4. identify the repository root
5. run the core repository validation
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

The machine-readable and August snapshot validators currently run against an extracted checkout rather than accepting a ZIP path directly.

---

# Machine-Readable Output

Use `--json` with the core repository validator to return structured output.

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

The machine-readable validator and August snapshot validator emit human-readable pass/fail output and nonzero exit status on error.

Repository validation is also executed automatically in GitHub Actions as described below.

---

# Exit Codes

The validator suite distinguishes failures from governed warnings.

| Exit code | Meaning |
|---:|---|
| `0` | No validation errors |
| `1` | One or more validation errors |

Warnings in the core repository validator do not cause a nonzero exit code.

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
- RingConn bytes match the registered source package
- records 041–046 retain their protected closed/adjudicated states
- protected closed-record actual values and error directions remain unchanged
- record 043 retains `actual_value=overall_improvement_not_met` and `error_direction=over`
- records 041–046 retain `calibration_state=pre`
- records 041–046 retain their original registered prediction narratives at the beginning of `notes`
- August integrated snapshot values match the protected cross-layer molecular state
- August artifact bytes and registered hashes match the dedicated snapshot expectations
- DQ-010 and Record 043 remain aligned to the canonical August collection event

---

## WARN

A known or governed limitation remains visible.

Warnings may include:

- DQ-001 awake-minute and awakening-count duplication
- DQ-002 and DQ-003 sleep-stage differences
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
- release-metadata mismatch
- protected closed prediction record reopened
- protected closed prediction record losing its recorded actual outcome
- protected closed prediction record drifting from its registered adjudicated actual value
- protected closed prediction record drifting from its recorded error direction
- protected preregistered record changing `calibration_state` from `pre`
- protected registered prediction narrative being removed, replaced, or altered
- RingConn source bytes changed
- August protected snapshot value drifting from its committed source-backed state
- August structured molecular layers disagreeing with each other
- August DQ-010 canonical date/time provenance disappearing or changing unexpectedly
- August artifact bytes or checksum registrations drifting from the protected identities
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

# Core Validator Check Inventory

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

It also reports total file count and zero-byte files.

## Markdown

The validator checks:

- relative Markdown targets
- internal anchors
- paths escaping the repository root
- fenced-code balance

External web links are not tested by the local validator.

## CSV Structure

Every CSV is checked for:

- valid parsing
- header presence
- duplicate headers
- consistent row width

The validator does not judge every field for biological plausibility.

## Checksum Manifests

Every file named `checksums.txt` is evaluated for:

- manifest syntax
- target existence
- repository path safety
- SHA-256 agreement

A mismatch is an error.

The validator does not regenerate manifests.

## Canonical Sleep

The validator checks:

- ISO date parsing
- duplicate dates
- missing dates inside the represented interval
- sleep-stage totals
- the governed DQ-001 interval

Known field-level discrepancies are reported as warnings.

The validator does not edit `data/sleep_longitudinal_v1.csv`.

## Weekly Reports

The validator checks:

- continuity of `2026-W##.md` report filenames
- missing weekly indices
- exactly one report marked active
- the latest weekly report is the active report

The validator does not close or open a weekly report.

## Current-State Surfaces

The validator checks alignment across:

- `LATEST.md`
- `README.md`
- `INDEX.md`
- `data/DATA_COVERAGE.md`
- daily, sleep, training, and context-event dataset endpoints

This protects current-facing state from drifting away from the canonical data layer.

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

# Registration-Provenance Protection

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

It does not mean the prediction is currently awaiting evaluation, and it does not become `post` merely because the prediction has later been scored or closed.

For records 041–046, the validator also contains the preserved original prospective `Prediction:` narrative. The `notes` field must begin with that registered narrative.

Closure text may be appended after the original prediction. It must not replace or rewrite the original prediction.

This protects the distinction between what was predicted before the outcome and what was concluded after the outcome.

---

# Protected Open and Closed Records

No record in the currently protected 041–046 block remains open.

The protected closed-record state is:

```text
041
actual_value = stable
error_direction = none

042
actual_value = continued_adaptation
error_direction = under

043
actual_value = overall_improvement_not_met
error_direction = over

044
actual_value = 0
error_direction = under

045
actual_value = partial_reconvergence
error_direction = none

046
actual_value = failed_autonomic_recompression
error_direction = over
```

For these records the validator additionally requires:

```text
calibration_state = pre
```

and preservation of the original registered `Prediction:` narrative.

The validator does not independently determine whether those adjudications were scientifically correct.

---

# Records 041–044 Evaluation Boundary

For records 041–044, formal scoring was performed retrospectively against the preserved preregistered rules in:

```text
methodology/open_prediction_evaluation_plan_041_044.md
```

Current status under that original framework is:

```text
041:
closed / supported

042:
closed / not supported — continued adaptation

043:
closed / not supported — overall improvement not met
error_direction = over

044:
closed / not supported — narrow snapshot-directed governance deviation
```

The original preregistration artifact remains preserved.

Record 043's criterion-by-criterion adjudication is preserved in:

```text
data/model_error/record_043_closure.md
```

The validators do not reconstruct or rescore these predictions.

---

# Record 045 Evaluation Boundary

Record 045 was prospectively registered on 2026-08-12 under:

```text
methodology/open_prediction_evaluation_plan_045.md
```

Its fixed scoring window was 2026-08-13 through 2026-08-16.

The repository records it as closed / supported with `actual_value=partial_reconvergence` and `error_direction=none`.

The validator protects that historical state and registration provenance but does not recalculate the four-day means or rescore the prediction.

---

# Record 046 Evaluation Boundary

Record 046 was prospectively registered on 2026-08-17 under:

```text
methodology/open_prediction_evaluation_plan_046.md
```

Its primary scoring window was 2026-08-20 through 2026-08-23.

The repository records:

```text
daily HRV: 60.25 ms — favorable
sleep HRV: 63.25 ms — unfavorable
resting HR: 52.0 bpm — unfavorable
sleeping HR: 54.0 bpm — unfavorable

1 of 4 favorable thresholds
```

Record 046 remains:

```text
status = closed
actual_value = failed_autonomic_recompression
error_direction = over
```

The validator protects this committed state without rescoring it or extending the evidence window.

---

# Release Metadata

The core validator compares:

- `CODEMETA.json`
- `CITATION.cff`

It checks alignment of:

- release version
- release date
- DOI

Current registered DOI:

```text
10.5281/zenodo.20815612
```

The validator checks repository metadata.

It does not query Zenodo or prove the current server-side deposit state.

---

# RingConn Source Exports

The core validator checks the source package under:

```text
data/source_exports/ringconn/2026-07-21/
```

It verifies:

- expected files
- registered byte sizes
- SHA-256 digests
- original CRLF line endings
- absence of bare-LF conversion
- provider header preservation
- expected source row counts
- the `.gitattributes` preservation rule

Required Git rule:

```gitattributes
data/source_exports/**/*.csv -text
```

The source files remain provider-source evidence and are not normalized or corrected by validation.

---

# August 2026 Snapshot Verification State

The August collection window was completed across:

```text
2026-08-17
2026-08-18
```

Current preserved source artifacts are:

```text
snapshots/2026-08/2026-08-dexa-body-comp.jpg
snapshots/2026-08/2026-08-dexa-summary.jpg
snapshots/2026-08/2026-08-vo2-summary.pdf
snapshots/2026-08/2026-08-bodpod-cosmed.jpg
snapshots/2026-08/2026-08-advanced-truage.pdf
snapshots/2026-08/2026-08-truage.pdf
snapshots/2026-08/2026-08-truhealth.pdf
```

These artifacts have been privacy-reviewed, assigned stable public filenames, incorporated into `snapshots/2026-08/checksums.txt`, and registered with SHA-256 digests.

The three TruDiagnostic PDFs are public sanitized derivatives of verified provider-source reports. Their public checksums identify the derivative copies rather than asserting byte identity with private originals.

The August temporal anchor is:

```text
snapshots/2026-08/2026-08 Epoch.md
```

Current evidence state is:

```text
physical collection:
complete

physical source-artifact preservation:
complete

TruDiagnostic sample collection:
complete

TruDiagnostic provider-result public derivatives:
complete and checksum-registered

integrated DEXA / Bod Pod structured snapshot:
complete for the represented fields

structured core / organ / TruHealth integration:
complete for the fields currently represented

Model Error 043:
closed / not supported — overall_improvement_not_met
```

The August TruDiagnostic source-role reconciliation is preserved in:

```text
data/source_provenance/2026-08-trudiagnostic-reconciliation.md
```

The retrospective synthesis is preserved in:

```text
reports/2026-08-biological-snapshot.md
```

Artifact verification does not itself adjudicate Model Error 043. The formal 043 adjudication is preserved separately in `data/model_error/record_043_closure.md`.

DEXA, VO₂ max, and Bod Pod remain supplemental to the registered 043 primary molecular domain.

---

# Artifact Verification With SHA-256

Binary artifacts and provider-source exports are accompanied by SHA-256 manifests.

The relevant manifest is normally stored in the same directory as the artifact:

```text
checksums.txt
```

## Windows — Command Prompt

```text
certutil -hashfile snapshots\YYYY-MM\filename.pdf SHA256
```

Compare the reported digest with the applicable `checksums.txt` manifest.

## Windows — PowerShell

```text
Get-FileHash "snapshots\YYYY-MM\filename.pdf" -Algorithm SHA256
```

## macOS / Linux

```text
shasum -a 256 snapshots/YYYY-MM/filename.pdf
```

or, where available:

```text
sha256sum snapshots/YYYY-MM/filename.pdf
```

---

# Temporal Anchor Relationship

Many snapshot folders contain an epoch file such as:

```text
snapshots/YYYY-MM/YYYY-MM Epoch.md
```

The epoch file serves as the temporal anchor for the capture window.

It may document:

- when the snapshot belongs
- the operating conditions
- which artifacts belong to the window
- public-versus-private artifact status
- where interpretation belongs
- how the snapshot connects to the broader archive

Checksums verify file identity.

Epoch files contextualize file placement.

Reports and model-error records interpret longitudinal significance.

These roles should remain separate.

---

# Verification Scope

Verification may establish that:

- a file matches its registered checksum
- a source export retains registered bytes
- repository CSVs parse
- internal Markdown links resolve
- weekly reports are continuous
- protected closed prediction records retain their committed adjudicated states
- prospective registration state remains preserved for records 041–046
- original registered prediction narratives remain preserved for records 041–046
- release metadata agrees
- a downloaded ZIP is mechanically safe and internally consistent
- the current machine-readable daily/training/event layer satisfies its declared schema checks
- the protected 325-session training prefix remains present and live session identifiers remain unique
- current live training `source_ref` values use the canonical private-source grammar
- August protected snapshot values agree across the designated structured layers
- August DQ-010 and Record 043 remain aligned to the canonical sample event
- August protected artifact bytes match both the checksum manifest and dedicated fixed expectations

Verification does not independently establish:

- biological causality
- clinical significance
- measurement validity
- device accuracy
- phase transition
- whether a recorded prediction outcome was scientifically correct
- whether record 044 materially altered an August biological result
- population generalizability
- universal privacy erasure
- provider-side deletion of unreachable Git or LFS objects
- removal from prior uncontrolled downloads or mirrors

---

# Privacy Verification Boundary

The local validator checks the current repository package.

It cannot prove deletion from:

- old local clones
- prior downloads
- third-party mirrors
- browser caches
- search-engine caches
- GitHub provider-controlled unreachable objects
- residual Git LFS storage
- other uncontrolled copies

Provider-side cleanup remains a separate verification state and should change only after direct provider confirmation.

---

# Recommended Audit Workflow

For a routine local verification cycle:

1. pull or download the latest repository state
2. run all applicable read-only validators (`tools/validate_repository.py`, `tools/validate_machine_readable.py`, and snapshot-specific validators such as `tools/validate_august_snapshot.py`)
3. review all errors
4. review warnings against `data/DATA_QUALITY_NOTES.md`
5. spot-check recently changed artifacts and structured rows
6. verify that protected prediction and phase boundaries remain intact
7. verify that preregistered prediction records retain their original registration state and prediction narrative
8. verify that scored predictions remain frozen after their registered outcome boundaries
9. verify that record 043 retains its closed adjudicated state and original prospective registration provenance
10. download and validate a fresh GitHub ZIP after material changes when package-level verification is needed
11. record a formal audit when the scheduled cadence or a material event requires it

The validators reduce repetitive mechanical work.

They do not replace human semantic review.

---

# Manual Review Still Required

The validators cannot fully evaluate:

- whether interpretation exceeds evidence
- whether a provider field is semantically equivalent to a curated field
- whether a prediction was framed fairly
- whether prediction scoring correctly followed its preregistered criteria
- whether closure language accurately describes the evidence
- whether record 041 was substantively supported
- whether record 042 satisfied its qualitative-transition threshold
- whether record 043 was substantively adjudicated correctly
- whether the record 044 deviation was correctly classified
- whether the record 044 deviation materially affected a measured biological result
- whether record 046 was substantively adjudicated correctly
- whether a protocol deviation belongs to one governance category or another
- whether a phase declaration is justified
- whether a screenshot contains unexpected private information
- whether a PDF redaction preserved all necessary context
- whether a weekly narrative introduces unsupported causal claims
- whether a new method creates excessive maintenance burden
- whether a protocol change violates governance
- whether a retrospective environmental hypothesis explains a molecular result

These remain human audit responsibilities.

---

# GitHub Actions Status

Lightweight automated validation is active through:

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

The workflow is intentionally read-only. It does not edit files, commit corrections, publish releases, or replace human semantic review.

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
- Snapshot-specific validators protect committed cross-layer state; they do not become new evidence sources.
- A legitimate protected snapshot correction requires source-backed review and an explicit validator update rather than silent expectation drift.
- Interpretation belongs in reports, datasets, model-error evaluation, and designated synthesis layers.

---

## Version Note

This guide was expanded on 2026-07-25 after introduction of `tools/validate_repository.py` to document whole-repository validation, directory/ZIP validation, JSON output, error-versus-warning behavior, and the principal repository checks.

On 2026-08-12 through 2026-08-24, the model-error validation boundary was progressively extended through records 041–046 as their prospective windows opened and closed. The validator preserved the distinction between protected open records, closed outcomes, and preregistered evidence windows without independently rescoring those records.

On 2026-08-23, registration-provenance protection was hardened after a catch-up audit identified a narrow record 045 provenance defect. The validator thereafter explicitly protected `calibration_state=pre` and the original registered `Prediction:` narrative for records 041–046 while allowing later closure language to remain appended.

On 2026-09-07, the verification system gained the machine-readable semantic validator, protected historical training-prefix logic, canonical private-source reference checks, and active GitHub Actions execution.

On 2026-09-10, Record 043 protection was advanced from open/unscored to its committed closed state after source-backed August adjudication. The validator preserved `actual_value=overall_improvement_not_met`, `error_direction=over`, `calibration_state=pre`, and the original prospective prediction narrative.

On 2026-09-10, the post-snapshot cleanup added `tools/validate_august_snapshot.py` as a fourth, snapshot-specific validation layer. The new validator protects the completed August source-artifact identities, integrated DEXA/Bod Pod values, core aging outputs, 11 system ages, 19 TruHealth domains, molecular cross-layer agreement, DQ-010 canonical collection provenance, and Record 043 alignment. It is executed by the existing read-only GitHub Actions workflow alongside the core and machine-readable validators.

These verification-layer revisions do not alter source measurements, source artifact bytes, checksum registrations, preregistered prediction thresholds, adjudicated outcomes, protocol exposure, phase status, release version, or DOI.
