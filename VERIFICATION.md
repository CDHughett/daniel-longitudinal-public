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
- model-error continuity
- preserved closed/adjudicated state of records 041–046
- selected protected actual values and error directions for those closed records
- preserved prospective registration state for records 041–046
- preservation of the original registered prediction narrative for records 041–046
- release-metadata alignment
- RingConn source-export byte preservation

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

The currently protected closed-record set is:

```text
041
042
043
044
045
046
```

The validator protects the following adjudicated state:

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

The validator therefore protects more than closure status.

It also detects accidental drift in selected committed outcome fields.

For these records it additionally requires:

```text
calibration_state = pre
```

and preservation of the original registered `Prediction:` narrative.

This protection exists to prevent later repository edits from silently:

- reopening a closed record
- erasing an observed outcome
- changing an adjudicated actual state
- changing an error direction
- converting a model miss into a concordant result
- changing a concordant result into a miss
- changing the historical registration state
- replacing a forward prediction with a retrospective closure narrative

The validator does **not** independently determine whether those adjudications were scientifically correct.

---

## Records 041–044 Evaluation Boundary

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

The validator does not independently:

- reconstruct the July–August evidence set
- determine whether record 041 crossed its recovery-capacity failure boundary
- determine whether record 042 satisfied its repeated automaticity threshold
- determine whether record 043 satisfied its biological-translation thresholds
- determine whether the 2026-08-16 Load Integration omission constituted a governance failure
- infer a biological consequence from record 044
- rescore any of records 041–044

Those responsibilities belong to the preregistered evaluation artifact, source evidence, model-error ledger, and retrospective semantic review.

Record 043's criterion-by-criterion adjudication is preserved in:

```text
data/model_error/record_043_closure.md
```

---

## Record 045 Evaluation Boundary

For record 045, the preregistered scoring window closed on 2026-08-16.

The repository records record 045 as closed after scoring under:

```text
methodology/open_prediction_evaluation_plan_045.md
```

The validator protects that historical state.

It requires the row to retain:

```text
calibration_state = pre
```

because record 045 was prospectively registered on 2026-08-12.

It also requires the original registered `Prediction:` narrative to remain at the beginning of the `notes` field.

Closure language may follow that registered text.

The validator does not:

- recalculate the August 13–16 four-day means
- compare those values with the preregistered thresholds
- independently classify functional regression
- independently classify whether a protocol change was recovery-driven
- reinterpret the 2026-08-16 Load Integration omission
- reopen the prediction
- rescore the prediction

The 2026-08-23 catch-up audit identified and authorized correction of a narrow provenance defect in which:

```text
calibration_state:
pre
→
post
```

and the original prediction narrative had been replaced by closure text.

The repair restored registration provenance only.

It did not alter record 045's supported outcome.

---

## Record 046 Evaluation Boundary

Record 046 was prospectively registered on:

```text
2026-08-17
```

under:

```text
methodology/open_prediction_evaluation_plan_046.md
```

Its evidence structure was fixed as:

```text
2026-08-17:
registration context only

2026-08-18 through 2026-08-19:
descriptive unload / re-entry kinetics

2026-08-20 through 2026-08-23:
primary scoring window
```

The scoring window is complete.

The registered four-day favorable thresholds were:

```text
daily HRV >= 59.7 ms
sleep HRV >= 65.3 ms
resting HR <= 49.2 bpm
sleeping HR <= 53.7 bpm
```

The repository records the following four-day means:

```text
daily HRV:
60.25 ms
favorable

sleep HRV:
63.25 ms
unfavorable

resting HR:
52.0 bpm
unfavorable

sleeping HR:
54.0 bpm
unfavorable
```

Threshold result:

```text
1 of 4 favorable
```

The registered support requirement was:

```text
at least 3 of 4 favorable thresholds

AND

no multi-session functional regression

AND

no recovery-driven protocol reduction after normal training resumed
```

The latter two conditions were satisfied.

The quantitative autonomic condition was not.

Record 046 is therefore preserved as:

```text
status = closed
actual_value = failed_autonomic_recompression
error_direction = over
```

The qualitative error direction is `over` because the model overestimated persistence of the favorable record 045 autonomic state through the immediate post-testing reload interval.

The validator protects this committed state.

It does not:

- recalculate the August 20–23 means
- independently determine whether 1 of 4 thresholds was favorable
- reinterpret the post-VO₂ disturbance
- determine whether later autonomic rebound should alter the score
- reopen record 046
- extend its evidence window
- substitute Week 34 evidence
- rescore record 045
- score DEXA, VO₂-max, Bod Pod, TruDiagnostic, or other biological outcomes

Late-window improvement remains part of retrospective interpretation.

It does not change the fixed-window outcome.

Record 046 remains historically prospectively registered and therefore must retain:

```text
calibration_state = pre
```

and the original registered `Prediction:` narrative at the beginning of `notes`.

The validator's role across the model-error layer remains narrow:

```text
protect committed governance state
and registration provenance
from accidental repository drift
```

It does not replace prediction adjudication.

---

## Release Metadata

The validator compares:

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

## RingConn Source Exports

The validator checks the source package under:

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

The RingConn source files remain provider-source evidence.

The validator does not:

- normalize them
- correct provider anomalies
- append them to curated sleep data
- classify naps
- invent timezone offsets

---

# August 2026 Snapshot Artifact Verification State

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

These artifacts have been:

- privacy-reviewed
- assigned stable public filenames
- incorporated into `snapshots/2026-08/checksums.txt`
- registered with SHA-256 digests

The three August TruDiagnostic PDFs are public sanitized derivatives of verified provider-source reports. Their registered public hashes identify those derivative copies rather than asserting byte identity with private originals.

The August temporal anchor is:

```text
snapshots/2026-08/2026-08 Epoch.md
```

Current artifact-layer evidence state is:

```text
physical collection:
complete

physical source-artifact preservation:
complete

TruDiagnostic sample collection:
complete

TruDiagnostic provider-result artifacts:
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

The retrospective biological synthesis is preserved in:

```text
reports/2026-08-biological-snapshot.md
```

Artifact verification does not itself adjudicate Model Error 043. The formal 043 adjudication is preserved separately in `data/model_error/record_043_closure.md` and the committed outcome is protected by the repository validator.

The dedicated August cross-layer validator additionally protects agreement between the structured snapshot, molecular longitudinal layer, DQ-010, Record 043 closure, checksum manifest, and fixed artifact identities.

DEXA, VO₂ max, and Bod Pod remain supplemental to the registered 043 primary molecular domain.

---

# Artifact Verification With SHA-256

Binary artifacts and provider-source exports are accompanied by SHA-256 manifests.

The relevant manifest is normally stored in the same directory as the artifact:

```text
checksums.txt
```

---

## Windows — Command Prompt

For a single file:

```text
certutil -hashfile snapshots\YYYY-MM\filename.pdf SHA256
```

Compare the reported digest with:

```text
snapshots\YYYY-MM\checksums.txt
```

Example for a source export:

```text
certutil -hashfile data\source_exports\ringconn\2026-07-21\ringconn-sleep-export.csv SHA256
```

Compare it with:

```text
data\source_exports\ringconn\2026-07-21\checksums.txt
```

---

## Windows — PowerShell

For a single file:

```text
Get-FileHash "snapshots\YYYY-MM\filename.pdf" -Algorithm SHA256
```

For a RingConn source export:

```text
Get-FileHash "data\source_exports\ringconn\2026-07-21\ringconn-sleep-export.csv" -Algorithm SHA256
```

---

## macOS

```text
shasum -a 256 snapshots/YYYY-MM/filename.pdf
```

For a RingConn source export:

```text
shasum -a 256 data/source_exports/ringconn/2026-07-21/ringconn-sleep-export.csv
```

---

## Linux

Either command may be available:

```text
sha256sum snapshots/YYYY-MM/filename.pdf
```

or:

```text
shasum -a 256 snapshots/YYYY-MM/filename.pdf
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
- selected protected actual values and error directions remain unchanged
- prospective registration state remains preserved for records 041–046
- original registered prediction narratives remain preserved for records 041–046
- release metadata agrees
- a downloaded ZIP is mechanically safe and internally consistent
- the current machine-readable daily/training/event layer satisfies its declared schema checks
- the protected 325-session training prefix remains present and live session identifiers remain unique
- current live training `source_ref` values use the canonical private-source grammar
- registered private-source hashes match the exact private bytes when those bytes are independently available for comparison
- the completed August snapshot remains aligned across its designated structured/provenance/adjudication layers
- the seven protected August artifacts remain byte-identical to their fixed registered identities

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

Provider-side cleanup remains a separate verification state.

That status should change only after direct provider confirmation.

---

# Recommended Audit Workflow

For a routine local verification cycle:

1. pull or download the latest repository state
2. run all applicable read-only validators (`tools/validate_repository.py`, `tools/validate_machine_readable.py`, and snapshot-specific validators such as `tools/validate_august_snapshot.py`)
3. review all errors
4. review warnings against `data/DATA_QUALITY_NOTES.md`
5. spot-check recently changed artifacts
6. verify that protected prediction and phase boundaries remain intact
7. verify that preregistered prediction records retain their original registration state and prediction narrative
8. verify that scored predictions remain frozen after their registered outcome boundaries
9. verify that record 043 retains its closed adjudicated state and original prospective registration provenance
10. download and validate a fresh GitHub ZIP after material changes
11. record a formal audit only when the scheduled audit cadence or a material event requires it

The validator reduces repetitive mechanical work.

It does not replace human semantic review.

---

# Manual Review Still Required

The validator cannot fully evaluate:

- whether interpretation exceeds evidence
- whether a provider field is semantically equivalent to a curated field
- whether a prediction was framed fairly
- whether prediction scoring correctly followed its preregistered criteria
- whether closure language accurately describes the evidence
- whether preservation of the original prediction narrative is sufficient to establish fair adjudication
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
