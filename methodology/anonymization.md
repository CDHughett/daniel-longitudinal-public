# Anonymization and Public Artifact Sanitization

## Purpose

This document defines how the Daniel Longitudinal Study reduces unnecessary personal exposure while preserving the evidentiary value, provenance, and auditability of public repository artifacts.

The objective is not complete anonymity.

The subject’s public identity is intentionally associated with the project.

The objective is to distinguish:

- information necessary for longitudinal interpretation
- information intentionally public
- information useful only for private source verification
- administrative identifiers that should not remain publicly distributed
- third-party information that should not be exposed without a clear evidentiary need

Privacy reduction must not become biological-data alteration.

Sanitization must preserve the measurements and context required to evaluate the archive.

---

## Scope

This methodology applies to public materials including:

- provider reports
- laboratory reports
- imaging and body-composition reports
- wearable exports
- screenshots
- photographs
- PDFs
- CSV files
- JSON or other structured exports
- checksum manifests
- filenames
- archive packages
- report attachments
- future source-artifact formats

It also applies to distribution surfaces including:

- the current Git working tree
- Git history
- GitHub releases
- forks and mirrors under project control
- downloadable repository archives
- Zenodo deposits
- other intentionally maintained public copies

This document does not require every privately retained source artifact to be published.

---

## Core Principle

The archive may preserve a verified original privately while publishing a clearly identified sanitized derivative when privacy requires it.

A public sanitized derivative must remain:

- traceable to the verified source
- faithful to the biological or performance evidence
- explicit about its derivative status
- free of unsupported reconstruction
- visually and technically reviewed
- checksummed
- documented in relevant snapshot and changelog records

A sanitized artifact must not be represented as an untouched provider original.

---

## Public Identity Boundary

The following subject information is intentionally public within this project:

- full name
- chronological age
- project identity
- relevant observation dates
- biological, recovery, body-composition, and performance measurements
- protocol and phase context
- public repository and citation identity

The continued presence of the subject’s full name or chronological age is not, by itself, an anonymization failure.

Their public inclusion is deliberate and part of the archive’s identity.

---

## Information Normally Removed From Public Artifacts

Unless a specific evidentiary need is documented, public artifacts should not expose:

- full date of birth
- street address
- private telephone number
- private email address
- medical-record number
- patient identifier
- specimen identifier
- accession identifier when personally traceable
- insurance member or policy number
- account number
- billing identifier
- government-issued identifier
- signature
- login or portal identifier
- authentication token
- barcode or QR code containing private identifiers
- precise appointment location when unnecessary
- unrelated emergency-contact information
- unrelated family-member information
- private clinician contact details
- personally identifying administrative notes
- device-account identifiers that are not needed for interpretation

Third-party identifying information should also be minimized when it is not required to establish provenance.

---

## Information Normally Preserved

When relevant to longitudinal interpretation, a sanitized public artifact should preserve:

- measurement date
- collection date
- test name
- analyte name
- measurement value
- unit
- reference interval
- abnormality flag
- specimen type when scientifically relevant
- provider or laboratory organization
- device or instrument class
- preparation or collection conditions
- methodological notes
- page order
- report structure needed to understand the results
- result comments that materially affect interpretation

Sanitization should not remove unfavorable, inconvenient, or contradictory biological findings.

---

## Definitions

### Private Original

The strongest available source artifact retained outside the public repository.

A private original may contain administrative or identifying information not required for public interpretation.

The private original should remain available for:

- source verification
- correction review
- audit support
- confirmation that public sanitization preserved the measured values

Private retention does not guarantee permanent availability and should not be overstated.

---

### Public Original

A source artifact published without substantive privacy modification because it does not contain unnecessary private information.

A public original may still be:

- renamed
- placed into a governed directory
- checksummed
- accompanied by provenance documentation

Renaming alone does not make the file a derivative if its content remains byte-identical.

---

### Public Sanitized Derivative

A public file created from a verified source after removing unnecessary identifying or administrative information.

The derivative should preserve the evidentiary content required for interpretation.

Examples include:

- a laboratory PDF with patient and specimen identifiers removed
- a report image with address and contact fields removed
- a structured export with account identifiers deleted
- a screenshot cropped to preserve measurement content while excluding unrelated private material

---

### Redacted Derivative

A sanitized derivative in which content has been intentionally removed or obscured.

A valid redaction must prevent recovery of the removed content from:

- visible layers
- hidden text
- annotations
- metadata
- embedded objects
- file history contained inside the artifact
- selectable text beneath visual covering

A black rectangle placed over readable PDF text is not sufficient if the underlying text remains extractable.

---

### Transformed Derivative

A public artifact recreated into another format while preserving verified source content.

Examples include:

- source PDF converted to page images
- report pages reconstructed into a sanitized PDF
- spreadsheet export normalized into a documented CSV schema

Transformation must be disclosed when it affects:

- appearance
- searchability
- page structure
- metadata
- source fidelity
- comparability

---

### Deidentified Structured Dataset

A structured table containing relevant longitudinal values without unnecessary direct administrative identifiers.

Deidentification does not mean the dataset is anonymous when the repository remains publicly associated with the subject.

---

### Source-Preserving Sanitization

Removal of private administrative content without changing the biological, performance, recovery, or contextual evidence being preserved.

---

## Privacy Classification

Before publication, an artifact should be classified into one of the following states.

### Public as Received

The artifact contains no unnecessary private information and may be preserved publicly without content modification.

### Public After Filename Normalization

The file content is acceptable, but the downloaded filename contains an unnecessary personal or account-facing label.

The content remains byte-preserved.

### Public Sanitized Derivative Required

The artifact contains private administrative or identifying information that can be removed while preserving evidentiary value.

### Private Source Only

Public sanitization would:

- destroy essential context
- create misleading incompleteness
- expose excessive private material
- require unsupported reconstruction
- provide little public value

The artifact should remain private while any public structured values derived from it are clearly documented as source-verified but not fully externally inspectable.

### Public Inclusion Deferred

The artifact requires additional review before a defensible decision can be made.

Deferred publication is preferable to rushed sanitization.

---

## Sanitization Workflow

### Step 1 — Preserve the Source Before Editing

Before public modification:

- retain the verified original privately
- record the original filename
- record the source date
- record the provider or device
- retain the original file hash when appropriate
- avoid editing the only available copy

The original should not be placed in the public repository merely to create a correction trail.

---

### Step 2 — Inventory Sensitive Fields

Review all visible and hidden content for:

- full DOB
- address
- phone number
- email address
- patient identifiers
- specimen identifiers
- account identifiers
- signatures
- barcodes
- QR codes
- third-party information
- filenames containing unnecessary personal labels
- comments or annotations
- embedded metadata
- hidden spreadsheet columns
- document properties
- attachment objects
- thumbnails or previews

The review should consider the artifact as a technical file, not only as a visible page.

---

### Step 3 — Define the Evidence That Must Remain

Before editing, identify the content required to preserve:

- biological values
- units
- reference intervals
- test dates
- specimen context
- provider identity where relevant
- interpretation-relevant comments
- report page continuity
- source provenance

The sanitization plan should be driven by preserving evidence, not by making the document visually cleaner.

---

### Step 4 — Create a Derivative

Create a separate public derivative.

Do not modify the private original.

The derivative should use a stable repository filename that describes:

- date or epoch
- artifact type
- provider or test class when useful

Public filenames should avoid unnecessary personal naming strings.

---

### Step 5 — Remove Content, Not Merely Cover It

For PDFs and images:

- remove or rasterize underlying text when necessary
- verify that redacted text cannot be selected
- remove annotations containing the original information
- remove embedded form fields
- remove hidden layers
- review image edges and page margins
- confirm that cropped material is not retained in the file canvas

For structured files:

- delete prohibited fields
- do not merely hide columns
- remove comments and formulas containing private information
- review sheet names and workbook properties
- review metadata and export history
- preserve column definitions needed for interpretation

---

### Step 6 — Inspect Metadata and Embedded Content

Review when technically available:

- author
- creator
- producer
- title
- subject
- keywords
- comments
- revision history
- embedded filenames
- attachment lists
- annotation objects
- document IDs
- image metadata
- geolocation
- workbook properties
- hidden worksheets
- named ranges
- archived thumbnails

Metadata should be removed when it exposes unnecessary private information.

Provider, device, software, and creation metadata may remain when useful for provenance and not personally sensitive.

---

### Step 7 — Perform Visual Verification

Inspect every page or visible record of the public derivative.

Confirm:

- prohibited fields are not visible
- measurements remain readable
- values were not clipped
- units remain associated with the correct values
- page order remains correct
- reference intervals remain understandable
- no redaction accidentally implies a different result
- no unrelated page was added
- no expected result section was removed

Visual quality defects that do not affect privacy or interpretation may be documented without forcing repeated artifact reconstruction.

---

### Step 8 — Perform Text and Content Verification

When possible, inspect:

- extracted text
- file strings
- selectable text
- embedded object lists
- metadata
- structured fields

Search for known sensitive strings from the private source.

A successful visual review does not substitute for hidden-text review when the format supports hidden content.

---

### Step 9 — Compare Biological Content With the Source

Confirm that sanitization did not alter:

- test values
- units
- flags
- dates
- reference ranges
- comments affecting interpretation
- page associations

When exact automated comparison is not possible, perform a documented manual comparison.

No value should be reconstructed from memory.

---

### Step 10 — Generate a New Checksum

After the public derivative is finalized:

- generate a new SHA-256 digest
- update the relevant checksum manifest
- verify the manifest against the final committed file
- do not reuse the original file’s digest
- rerun repository checksum validation

The checksum identifies the sanitized derivative.

It does not claim identity with the private original.

---

### Step 11 — Document the Change

Material sanitization should be recorded in:

- the relevant snapshot or epoch document
- `CHANGELOG.md`
- a repository audit when applicable
- measurement-source documentation when the public/private source status matters

Documentation should state:

- which artifact was replaced
- what categories of information were removed
- what evidence was preserved
- whether the public file is a sanitized derivative
- whether the checksum changed
- whether distribution-level review remains open

Do not reproduce the removed sensitive values in the changelog or commit message.

---

## File-Type Guidance

### PDF Reports

PDF review should include:

- visible page content
- selectable text
- form fields
- annotations
- attachments
- bookmarks
- metadata
- hidden layers
- embedded images

Where reliable object-level redaction is uncertain, conversion to reviewed page images and reconstruction into a new PDF may be preferable.

The transformation must be documented.

---

### Images and Screenshots

Review:

- status bars
- notification content
- account names
- email addresses
- device identifiers
- location indicators
- gallery thumbnails
- timestamps
- background documents
- reflections
- QR or barcodes
- image metadata
- geolocation

Cropping may be sufficient when it permanently removes excluded pixels and preserves the relevant measurement context.

---

### CSV and Structured Exports

Review:

- headers
- subject-name fields
- account identifiers
- device identifiers
- timezone fields
- hidden metadata rows
- comments
- filenames
- embedded formula content
- direct versus derived values

Downloaded filenames may be normalized without changing the file contents.

When a source export is intended to remain byte-preserved:

- rename only at the filesystem level
- record the original downloaded filename privately or in a non-sensitive provenance note
- compute the checksum after repository naming is finalized
- do not edit the CSV contents merely for aesthetic consistency

A normalized analytical dataset should be stored separately from the immutable source export.

---

### ZIP and Archive Packages

Before public distribution:

- inspect every contained file
- inspect nested archives
- remove operating-system metadata when appropriate
- verify that private originals were not included accidentally
- check for prior versions of sanitized files
- review filenames and directory names
- verify the final archive contents independently

A clean current repository file does not guarantee that a generated archive excludes obsolete private copies.

---

## Blood and Laboratory Reports

Public blood and laboratory artifacts should normally preserve:

- collection date
- report date when relevant
- test names
- values
- units
- reference intervals
- flags
- clinically relevant comments
- laboratory identity
- specimen type when relevant

They should normally remove:

- full DOB
- address
- phone
- email
- patient ID
- specimen ID when personally traceable and not analytically required
- billing or insurance details
- signatures
- private clinician contact information
- unrelated administrative material

The subject’s public name and age may remain under the project’s explicit identity policy.

---

## Wearable Exports

Direct wearable exports should be reviewed for:

- subject name
- account name
- email
- device serial number
- user ID
- timezone or location data
- filenames containing private labels
- hidden account metadata
- provider-specific identifiers

When contents are privacy-acceptable but filenames contain unnecessary personal text:

- normalize the public filename
- preserve the file contents byte-for-byte
- document the export date and source
- generate source-export checksums
- store normalized analytical tables separately

Daily physiological values should not be removed merely because they are personal.

They are part of the intended longitudinal evidence.

---

## Current Canonical Public Artifact

When a sanitized derivative replaces a prior public artifact:

- the derivative becomes the current canonical public artifact
- its checksum becomes the current public checksum
- the snapshot documentation should identify its derivative status
- the private original remains the source-verification artifact
- the replacement does not create new biological evidence

Historical publication exposure requires separate review.

---

## Git-History Boundary

Replacing a file in the current branch does not necessarily remove earlier versions from Git history.

A privacy correction should therefore distinguish:

### Current-Tree Remediation

The active branch contains the sanitized derivative and no longer displays the sensitive version in its current state.

### Historical-Object Remediation

Earlier Git objects containing the prior file have been evaluated and, when necessary, removed through an intentional history-rewrite procedure.

History rewriting may affect:

- commit hashes
- forks
- local clones
- open pull requests
- tags
- release references
- external links

It should be performed deliberately and documented separately from ordinary file editing.

A current-tree correction must not be described as full historical removal unless that work has been verified.

---

## External Distribution Boundary

The project should separately inspect intentional public distribution surfaces, including:

- GitHub history
- GitHub releases
- repository ZIP downloads under project control
- Zenodo deposits
- mirrors
- project websites
- published supplemental archives

A prior public copy may remain outside direct control through:

- forks
- clones
- caches
- downloaded archives
- third-party mirrors
- citation attachments

The archive should not claim guaranteed erasure from uncontrolled external copies.

It should document:

- surfaces reviewed
- remediation attempted
- surfaces updated
- limitations that remain

---

## Zenodo and DOI-Bearing Releases

A DOI-bearing release is a distinct public distribution surface.

When privacy remediation affects an artifact contained in a deposited release:

- inspect the deposited files directly
- determine whether the sensitive version is present
- review available restriction, replacement, or support procedures
- preserve the DOI and scientific record where possible
- document any new corrected release
- avoid describing a later repository commit as automatically correcting the earlier deposit

An updated future Zenodo version does not, by itself, prove that the prior deposited file became inaccessible.

---

## Correction Classification

A privacy-motivated public replacement should be classified as:

- archive maintenance
- privacy remediation
- source-preserving sanitization
- checksum-changing artifact replacement
- not new biological evidence
- not a protocol change
- not a phase event
- not a new observation

A replacement should be treated as biological correction only when measured content itself changes from source-supported evidence.

---

## Commit and Changelog Guidance

Commit messages should describe the action without repeating removed information.

Appropriate example:

```text
docs(changelog): record blood artifact sanitization
```

Appropriate artifact example:

```text
privacy(snapshot): replace blood panel with sanitized derivative
```

Avoid commit messages containing:

- full DOB
- patient ID
- address
- removed specimen number
- private contact information

The changelog should describe categories of removed information rather than reproducing the values.

---

## Verification States

A public artifact may be described using the following states.

### Privacy Review Pending

The artifact has not completed the full review process.

### Current-File Sanitized

The current public file was reviewed and unnecessary private content was removed.

### Checksum Verified

The final public file matches its checksum manifest.

### Distribution Verification Pending

The current file is sanitized, but Git history or external archives have not been fully reviewed.

### Distribution Remediation Completed

All intentional distribution surfaces under project control were reviewed and appropriate remediation was completed.

This status should not imply erasure from uncontrolled forks, clones, caches, or prior downloads.

---

## Sanitization Verification Checklist

Before declaring a current public artifact sanitized, verify:

- [ ] Private original retained outside the public repository
- [ ] Public derivative created separately
- [ ] Full DOB reviewed
- [ ] Address reviewed
- [ ] Phone and email reviewed
- [ ] Patient and specimen identifiers reviewed
- [ ] Account and billing identifiers reviewed
- [ ] Signatures reviewed
- [ ] Barcodes and QR codes reviewed
- [ ] Third-party information reviewed
- [ ] Filenames reviewed
- [ ] Visible pages reviewed
- [ ] Hidden text reviewed where applicable
- [ ] Metadata reviewed where applicable
- [ ] Comments and annotations reviewed
- [ ] Biological values compared with source
- [ ] Units and reference intervals preserved
- [ ] Page order preserved
- [ ] New SHA-256 digest generated
- [ ] Checksum manifest verified
- [ ] Snapshot documentation updated
- [ ] Changelog updated
- [ ] Distribution verification status recorded

---

## Source Preservation Boundary

The private original should not be altered merely to match the public derivative.

The public derivative should not be used to claim that the original source never contained administrative information.

The archive should preserve the distinction among:

- original evidence
- public representation
- normalized data
- retrospective interpretation

Where external observers cannot inspect the private original, that limitation should remain visible.

---

## Data Minimization

Public inclusion should be limited to information that contributes to:

- provenance
- longitudinal interpretation
- measurement comparability
- auditability
- model evaluation
- scientific context

Information should not be published merely because it appears on the provider report.

Data minimization does not require removal of the longitudinal measurements that define the archive.

---

## Safety and Legal Boundary

This methodology is an internal archive-governance procedure.

It is not legal advice and does not guarantee compliance with every privacy law, platform policy, provider agreement, or records-management requirement.

When exposure may be materially harmful or legally consequential, professional guidance or platform support may be required.

Immediate removal and containment may take priority over ordinary one-file-and-one-commit sequencing.

---

## Relationship to Other Documents

This methodology should be read with:

- [`GOVERNANCE.md`](../GOVERNANCE.md)
- [`ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)
- [`methodology/data-collection.md`](data-collection.md)
- [`data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)
- [`DATASET_OVERVIEW.md`](../DATASET_OVERVIEW.md)
- [`VERSIONING.md`](../VERSIONING.md)
- [`CHANGELOG.md`](../CHANGELOG.md)

When privacy reduction and evidence preservation conflict, the repository should seek the least-destructive public representation that preserves valid longitudinal interpretation.

---

## Current Application

The July 2025 public blood-panel artifact was replaced with a sanitized derivative that:

- removes full date of birth
- removes patient and specimen identifiers
- removes address and contact information
- removes ordering-physician identity
- preserves the measured laboratory values
- intentionally retains the subject’s public name and chronological age
- uses a newly generated checksum
- remains classified as privacy remediation rather than new biological evidence

Current-tree sanitization has been completed.

Git-history and prior archival-distribution verification remain separate tasks until directly reviewed.

---

## Version Note

This methodology was expanded on 2026-07-22 after the archive completed its first material public-artifact sanitization and acquired direct annual wearable exports requiring explicit public/private source boundaries.

The expansion defines:

- public sanitized derivatives
- private-original retention
- direct-export handling
- true redaction requirements
- hidden-content inspection
- source-value preservation
- checksum renewal
- changelog requirements
- Git-history boundaries
- archival-distribution verification
- privacy-status terminology

The revision does not alter:

- any biological measurement
- any curated longitudinal value
- any prediction record
- any closed outcome
- any protocol exposure
- any phase status
