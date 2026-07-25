# Verification Guide

This repository supports external verification at two distinct levels:

1. **artifact verification** — confirms the identity of registered files
2. **repository validation** — checks the mechanical integrity and governed structure of the archive

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
- model-error continuity
- protected status of records 041–044
- release-metadata alignment
- RingConn source-export byte preservation

The validator is read-only.

It does not:

- edit files
- repair values
- infer missing observations
- normalize provider exports
- change prediction status
- rewrite history
- alter checksums

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

This mode may support future local automation.

It does not currently imply a GitHub Actions workflow.

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

A check completed without identifying a mechanical problem.

Examples:

- all checksum entries match
- all CSVs parse
- weekly reports are continuous
- RingConn bytes match the registered source package

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
- protected open prediction record no longer open
- RingConn source bytes changed
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

The validator does not close a weekly report.

---

## Model-Error Register

The validator checks:

- record-ID parsing
- duplicate IDs
- sequence continuity
- presence of records 041–044
- open status of records 041–044
- preservation of their registered predictions
- blank protected actual and error fields

The validator does not score predictions.

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
- protected prediction records remain open
- release metadata agrees
- a downloaded ZIP is mechanically safe and internally consistent

Verification does not independently establish:

- biological causality
- clinical significance
- measurement validity
- device accuracy
- phase transition
- prediction success
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
2. run the local validator
3. review all errors
4. review warnings against `data/DATA_QUALITY_NOTES.md`
5. spot-check recently changed artifacts
6. verify that protected prediction and phase boundaries remain intact
7. download and validate a fresh GitHub ZIP after material changes
8. record a formal audit only when the scheduled audit cadence or a material event requires it

The validator reduces repetitive mechanical work.

It does not replace human semantic review.

---

# Manual Review Still Required

The validator cannot fully evaluate:

- whether interpretation exceeds evidence
- whether a provider field is semantically equivalent to a curated field
- whether a prediction was framed fairly
- whether a phase declaration is justified
- whether a screenshot contains unexpected private information
- whether a PDF redaction preserved all necessary context
- whether a weekly narrative introduces unsupported causal claims
- whether a new method creates excessive maintenance burden
- whether a protocol change violates governance

These remain human audit responsibilities.

---

# GitHub Actions Status

Automated GitHub Actions validation is currently deferred.

The local validator should first demonstrate stability across repeated manual audit cycles.

Before remote automation is added, review:

- false-positive rate
- governed-warning behavior
- operating-system consistency
- ZIP-versus-directory consistency
- maintenance burden
- protected-data exposure
- failure-notification behavior

Local read-only validation remains the current operating model.

---

# Notes

- Verification is reproducible across supported local environments.
- Snapshot directories are intended to remain independently inspectable.
- Source exports remain separate from curated datasets.
- Warnings preserve known uncertainty rather than hiding it.
- Errors identify mechanical or governance-protected failures.
- Validation never authorizes automatic biological correction.
- Interpretation belongs in reports, datasets, model-error evaluation, and designated synthesis layers.

---

## Version Note

This guide was expanded on 2026-07-25 after introduction of:

```text
tools/validate_repository.py
```

The revision adds:

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

The revision does not alter:

- any artifact
- any checksum
- any biological value
- any prediction record
- any protocol exposure
- any phase declaration
