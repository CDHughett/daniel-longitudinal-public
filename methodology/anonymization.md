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
- JSON and other structured exports
- checksum manifests
- filenames
- archive packages
- report attachments
- future source-artifact formats

It also applies to intentional distribution surfaces including:

- the active Git working tree
- active Git branches and tags
- GitHub repository archives
- GitHub releases
- forks or mirrors under project control
- Zenodo deposits
- project websites
- other deliberately maintained public copies

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

# Public Identity Boundary

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

This policy does not make unrelated administrative identifiers public.

---

# Information Normally Removed From Public Artifacts

Unless a specific evidentiary need is documented, public artifacts should not expose:

- full date of birth
- street address
- private telephone number
- private email address
- medical-record number
- patient identifier
- specimen identifier
- personally traceable accession identifier
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
- device-account identifiers not needed for interpretation

Third-party identifying information should also be minimized when it is not required to establish provenance.

---

# Information Normally Preserved

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

Sanitization must not remove unfavorable, inconvenient, contradictory, or unexpected biological findings.

---

# Definitions

## Private Original

The strongest available source artifact retained outside the public repository.

A private original may contain administrative or identifying information not required for public interpretation.

It may be retained for:

- source verification
- correction review
- audit support
- confirmation that public sanitization preserved measured values

Private retention does not guarantee permanent availability and should not be overstated.

---

## Public Original

A source artifact published without substantive privacy modification because it contains no unnecessary private information.

A public original may still be:

- renamed
- placed in a governed directory
- checksummed
- accompanied by provenance documentation

Filesystem-level renaming alone does not make the contents a derivative when the file remains byte-identical.

---

## Public Filename-Normalized Source

A byte-identical provider or device file whose public filename was changed to remove an unnecessary personal or account-facing naming string.

Filename normalization:

- does not alter file contents
- does not authorize header changes
- does not authorize line-ending conversion
- does not authorize spreadsheet resaving
- should be documented in the acquisition README

---

## Public Sanitized Derivative

A public file created from a verified source after removing unnecessary identifying or administrative information.

The derivative should preserve the evidentiary content required for interpretation.

Examples include:

- a laboratory PDF with patient and specimen identifiers removed
- a report image with address and contact fields removed
- a structured export with account identifiers deleted
- a screenshot cropped to preserve measurement content while excluding unrelated private material

---

## Redacted Derivative

A sanitized derivative in which content has been intentionally removed or obscured.

A valid redaction must prevent recovery of removed content from:

- visible layers
- hidden text
- annotations
- metadata
- embedded objects
- form fields
- file history contained within the artifact
- selectable text beneath visual covering

A black rectangle placed over readable PDF text is not sufficient when the underlying text remains extractable.

---

## Transformed Derivative

A public artifact recreated in another format while preserving verified source content.

Examples include:

- source PDF converted to reviewed page images
- sanitized page images reconstructed into a new PDF
- provider spreadsheet transformed into a separate documented analytical CSV

Transformation must be disclosed when it affects:

- appearance
- searchability
- page structure
- metadata
- source fidelity
- comparability

---

## Deidentified Structured Dataset

A structured table containing longitudinal values without unnecessary direct administrative identifiers.

Deidentification does not mean the dataset is anonymous when the repository remains publicly associated with the subject.

---

## Source-Preserving Sanitization

Removal of private administrative content without changing the biological, performance, recovery, or interpretation-relevant evidence being preserved.

---

# Privacy Classification

Before publication, an artifact should be classified into one of the following states.

## Public as Received

The artifact contains no unnecessary private information and may be preserved publicly without content modification.

## Public After Filename Normalization

The content is acceptable, but the downloaded filename contains an unnecessary personal or account-facing label.

The file contents remain byte-preserved.

## Public Sanitized Derivative Required

The artifact contains private administrative or identifying information that can be removed while preserving evidentiary value.

## Private Source Only

Public sanitization would:

- destroy essential context
- create misleading incompleteness
- expose excessive private material
- require unsupported reconstruction
- provide little public value

The artifact should remain private.

Any public values transcribed from it should be described as source-verified but not fully externally inspectable.

## Public Inclusion Deferred

The artifact requires additional technical or privacy review.

Deferred publication is preferable to rushed sanitization.

---

# Sanitization Workflow

## Step 1 — Preserve the Source Before Editing

Before public modification:

- retain the verified original privately
- record the original filename
- record the source date
- record the provider or device
- retain the original file hash when appropriate
- avoid editing the only available copy

The private original should not be committed merely to create a correction trail.

---

## Step 2 — Inventory Sensitive Fields

Review visible and hidden content for:

- full date of birth
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

The artifact should be reviewed as a technical file, not only as a visible page.

---

## Step 3 — Define the Evidence That Must Remain

Before editing, identify content required to preserve:

- biological values
- units
- reference intervals
- test dates
- specimen context
- provider identity where relevant
- interpretation-relevant comments
- report page continuity
- source provenance

The sanitization plan should be driven by preserving evidence rather than making the artifact visually cleaner.

---

## Step 4 — Create a Separate Derivative

Create a separate public derivative.

Do not modify the private original.

The derivative should use a stable repository filename that describes:

- date or epoch
- artifact type
- provider or test class when useful

Public filenames should avoid unnecessary personal naming strings.

---

## Step 5 — Remove Content, Not Merely Cover It

For PDFs and images:

- remove or rasterize underlying text when necessary
- verify that redacted text cannot be selected
- remove annotations containing original information
- remove embedded form fields
- remove hidden layers
- review image edges and page margins
- confirm cropped material is not retained outside the visible canvas

For structured files:

- delete prohibited fields from the derivative
- do not merely hide columns
- remove comments and formulas containing private information
- review sheet names and workbook properties
- review metadata and export history
- preserve columns necessary for interpretation

---

## Step 6 — Inspect Metadata and Embedded Content

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
- annotations
- document identifiers
- image metadata
- geolocation
- workbook properties
- hidden worksheets
- named ranges
- archived thumbnails

Metadata should be removed when it exposes unnecessary private information.

Provider, device, software, and creation metadata may remain when useful for provenance and not personally sensitive.

---

## Step 7 — Perform Visual Verification

Inspect every page or visible record.

Confirm:

- prohibited fields are not visible
- measurements remain readable
- values are not clipped
- units remain associated with the correct values
- page order remains correct
- reference intervals remain understandable
- redaction does not imply a different result
- no unrelated page was added
- no expected result section was removed

Visual defects that do not affect privacy or interpretation may be documented without forcing repeated artifact reconstruction.

---

## Step 8 — Perform Text and Content Verification

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

## Step 9 — Compare Evidence With the Source

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

## Step 10 — Generate and Verify a New Checksum

After finalizing the public derivative:

- generate a new SHA-256 digest
- update the relevant checksum manifest
- verify the manifest against the final file
- do not reuse the private original’s digest
- rerun repository checksum validation

The checksum identifies the public derivative.

It does not claim byte identity with the private original.

---

## Step 11 — Document the Change

Material sanitization should be recorded in:

- the relevant snapshot or epoch document
- `CHANGELOG.md`
- a repository audit when applicable
- measurement-source documentation when public/private status matters

Documentation should state:

- which artifact was replaced
- which categories of information were removed
- which evidence was preserved
- whether the public file is a sanitized derivative
- whether the checksum changed
- whether historical or provider-side cleanup remains pending

Do not reproduce removed sensitive values in:

- the changelog
- commit messages
- audit prose
- support evidence intended for public inclusion

---

# File-Type Guidance

## PDF Reports

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

## Images and Screenshots

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
- QR codes
- barcodes
- image metadata
- geolocation

Cropping may be sufficient when it permanently removes excluded pixels and preserves relevant measurement context.

---

## CSV and Structured Exports

Review:

- headers
- subject-name fields
- account identifiers
- device identifiers
- timezone fields
- location fields
- hidden metadata rows
- comments
- filenames
- embedded formulas
- direct versus derived values

Downloaded filenames may be normalized without changing file contents.

When a source export is intended to remain byte-preserved:

- rename only at the filesystem level
- retain the original filename privately or describe it without reproducing unnecessary personal text
- compute the checksum from the final byte-preserved public file
- prevent Git line-ending conversion
- do not edit or resave the CSV for aesthetic consistency
- store any transformed analytical table separately

---

## ZIP and Archive Packages

Before public distribution:

- inspect every contained file
- inspect nested archives
- remove operating-system metadata when appropriate
- verify that private originals were not included
- check for obsolete sensitive versions
- review filenames and directory names
- verify the archive independently after creation or download
- compare expected and actual file inventories
- rerun checksum validation within the distributed archive

A clean current repository file does not prove that every generated archive excludes obsolete private copies.

---

# Blood and Laboratory Reports

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

- full date of birth
- address
- phone number
- email address
- patient identifier
- personally traceable specimen identifier
- billing or insurance details
- signatures
- private clinician contact information
- unrelated administrative material

The subject’s public name and chronological age may remain under the project’s explicit identity policy.

---

# Wearable Exports

Direct wearable exports should be reviewed for:

- subject name
- account name
- email address
- device serial number
- user identifier
- timezone or precise location data
- filenames containing unnecessary personal labels
- hidden account metadata
- provider-specific administrative identifiers

When contents are privacy-acceptable but filenames contain unnecessary personal text:

- normalize the public filename
- preserve file contents byte-for-byte
- document the export date and source
- prevent Git text conversion
- generate source-export checksums
- verify the distributed repository archive
- store transformed analytical tables separately

Daily physiological values should not be removed merely because they are personal.

They are part of the intended longitudinal evidence.

---

# Current Canonical Public Artifact

When a sanitized derivative replaces a prior public artifact:

- the derivative becomes the current canonical public artifact
- its checksum becomes the current public checksum
- snapshot documentation identifies its derivative status
- the private original remains the source-verification artifact
- the replacement does not create new biological evidence

Historical publication exposure requires separate evaluation.

---

# Git-History Boundary

Replacing a file in the active branch does not remove prior versions from Git history.

Privacy remediation should distinguish:

## Current-Tree Remediation

The active branch contains the sanitized derivative and does not display the sensitive version in its current state.

## Active-Ref Remediation

The sensitive artifact has been removed from:

- the active branch
- applicable maintained branches
- applicable release tags

Sanitized files and manifests have been restored where required.

## Historical-Object Remediation

Earlier Git objects containing the prior artifact have been removed from reachable history through an intentional rewrite.

History rewriting may affect:

- commit hashes
- tags
- local clones
- forks
- open pull requests
- release references
- external commit links
- audit references containing old hashes

After a rewrite:

- old clones must not be merged or pushed back
- users should create fresh clones
- old commit hashes should be treated as obsolete
- documentation containing hard-coded hashes may require later review
- remote refs should be independently compared with rewritten local refs

## Provider-Side Object Cleanup

A history rewrite does not prove immediate removal of:

- unreachable Git objects retained by the host
- Git LFS objects
- cached archives
- server-side object storage
- search or interface caches

Provider support may be required.

This status must remain separate from active-ref remediation.

---

# External Distribution Boundary

The project should inspect intentional public distribution surfaces individually, including:

- active GitHub branch
- relevant Git tags
- GitHub repository ZIP downloads
- GitHub releases
- Zenodo deposits
- mirrors under project control
- project websites
- supplemental archives

A prior public copy may remain outside direct control through:

- forks
- clones
- downloaded archives
- browser caches
- search-engine caches
- third-party mirrors
- citation attachments
- provider-controlled storage

The archive must not claim guaranteed erasure from uncontrolled copies.

It should document:

- surfaces reviewed
- remediation performed
- surfaces verified
- support requests submitted
- limitations that remain

---

# Zenodo and DOI-Bearing Releases

A DOI-bearing release is a distinct public distribution surface.

When privacy remediation affects a deposited artifact:

- inspect the deposited archive directly
- determine whether the sensitive version is present
- restrict access temporarily when needed
- use available file-replacement or support procedures
- preserve the DOI and scientific record where possible
- rebuild the release package from a verified repository state
- upload the corrected archive
- download the published archive independently
- compare file structure and checksums
- document that an in-place privacy repair is not new biological evidence

A later repository commit does not automatically correct an earlier Zenodo package.

A future Zenodo version also does not prove that a prior deposit became inaccessible.

The deposited file itself must be reviewed.

---

# Correction Classification

A privacy-motivated public replacement should be classified as:

- archive maintenance
- privacy remediation
- source-preserving sanitization
- checksum-changing artifact replacement
- not new biological evidence
- not a protocol change
- not a phase event
- not a new observation

A replacement should be treated as a biological correction only when measured content itself changes through source-supported evidence.

---

# Commit and Changelog Guidance

Commit messages should describe the action without repeating removed information.

Appropriate examples:

```text
privacy(snapshot): replace blood panel with sanitized derivative
```

```text
privacy(history): remove prior blood artifact from active refs
```

```text
docs(changelog): record privacy remediation
```

Avoid commit messages containing:

- full date of birth
- patient identifier
- address
- removed specimen number
- private contact information
- other sensitive administrative values

The changelog should describe categories of removed information rather than reproduce the values.

---

# Verification States

A public artifact or remediation event may use the following states.

## Privacy Review Pending

The artifact has not completed the full review process.

## Current File Sanitized

The current public file was reviewed and unnecessary private content was removed.

## Checksum Verified

The final public artifact matches its checksum manifest.

## Active Refs Remediated

The sanitized artifact is present across applicable active branches and tags, and the sensitive artifact is no longer reachable from those refs.

## Controlled Distribution Remediation Completed

Intentional distribution surfaces under direct project control have been reviewed and corrected.

This may include:

- active branch
- active tags
- current repository ZIP
- DOI-bearing archive package

This state does not imply deletion from uncontrolled copies or provider-owned residual storage.

## Provider Cleanup Pending

A repository host or archival provider has been asked to remove or expire residual objects, caches, or LFS content that cannot be removed solely through normal repository operations.

## Provider Cleanup Confirmed

The provider has explicitly confirmed completion of the requested residual cleanup.

This state must not be claimed before direct confirmation.

## Uncontrolled-Copy Limitation

Prior clones, downloads, caches, mirrors, or third-party copies may continue to exist outside project control.

---

# Sanitization Verification Checklist

Before declaring a current public artifact sanitized, verify:

- [ ] Private original retained outside the public repository
- [ ] Public derivative created separately
- [ ] Full date of birth reviewed
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
- [ ] Current-tree status recorded
- [ ] Historical-ref status recorded
- [ ] External-distribution status recorded
- [ ] Provider-side cleanup status recorded

---

# Source Preservation Boundary

The private original should not be altered merely to match the public derivative.

The public derivative should not be used to claim that the original never contained administrative information.

The archive should preserve the distinction among:

- private original evidence
- public representation
- source export
- curated data
- derived data
- retrospective interpretation

Where external observers cannot inspect the private original, that limitation should remain visible.

---

# Data Minimization

Public inclusion should be limited to information contributing to:

- provenance
- longitudinal interpretation
- measurement comparability
- auditability
- model evaluation
- scientific context

Information should not be published merely because it appears on a provider report.

Data minimization does not require removal of the longitudinal measurements that define the archive.

---

# Safety and Legal Boundary

This methodology is an internal archive-governance procedure.

It is not legal advice and does not guarantee compliance with every:

- privacy law
- platform policy
- provider agreement
- records-management requirement
- archival policy

When exposure may be materially harmful or legally consequential, professional guidance or platform support may be required.

Immediate containment may take priority over ordinary one-file-and-one-commit sequencing.

---

# Relationship to Other Documents

This methodology should be read with:

- [`GOVERNANCE.md`](../GOVERNANCE.md)
- [`ASSUMPTIONS_AND_BOUNDARIES.md`](../ASSUMPTIONS_AND_BOUNDARIES.md)
- [`METHODOLOGY_AND_CONTROLS.md`](../METHODOLOGY_AND_CONTROLS.md)
- [`MEASUREMENT_SOURCES.md`](../MEASUREMENT_SOURCES.md)
- [`data-collection.md`](data-collection.md)
- [`data/DATA_QUALITY_NOTES.md`](../data/DATA_QUALITY_NOTES.md)
- [`DATASET_OVERVIEW.md`](../DATASET_OVERVIEW.md)
- [`VERSIONING.md`](../VERSIONING.md)
- [`CHANGELOG.md`](../CHANGELOG.md)

When privacy reduction and evidence preservation conflict, the repository should seek the least-destructive public representation that preserves valid longitudinal interpretation.

---

# Current Application

## July 2025 Blood-Panel Artifact

The public July 2025 blood-panel artifact was replaced with a sanitized derivative that:

- removes full date of birth
- removes patient and specimen identifiers
- removes address and contact information
- removes ordering-physician identity
- preserves measured laboratory values
- preserves units, reference intervals, flags, dates, and report structure
- intentionally retains the subject’s public name and chronological age
- uses a newly generated checksum
- remains classified as privacy remediation rather than new biological evidence

Current public artifact:

```text
snapshots/2025-07/2025-07-full-blood-panel.pdf
```

Verified public SHA-256:

```text
e3fe18d94b003217f2d9024ee1952117305f1b48dc72bebf183269ec60a375cb
```

---

## Git-History Remediation

On 2026-07-22, the affected file path was removed from repository history through a dedicated sensitive-data rewrite.

The completed process included:

- identification of affected commits and tags
- removal of the historical artifact path from rewritten history
- restoration of the sanitized derivative to `main`
- restoration of the sanitized derivative to applicable surviving tags
- restoration and verification of the associated checksum manifest
- confirmation that the previously affected commits were no longer reachable from active local refs
- force-update of rewritten branch and tag refs
- comparison of remote refs with the rewritten local refs
- creation of support evidence documenting the rewrite
- use of a fresh clone for subsequent repository work

Old clones containing pre-rewrite history must not be merged or pushed into the remediated repository.

All commit hashes changed as a consequence of the rewrite.

Documents containing old hard-coded commit hashes may require later review.

---

## GitHub Provider-Side Status

A GitHub Support request was submitted for removal of residual Git LFS or other provider-controlled objects associated with the prior artifact.

Current status:

**Provider cleanup pending**

Until GitHub directly confirms completion, the archive does not claim that:

- every unreachable Git object has been deleted
- every LFS object has been purged
- every provider cache has expired
- every historical archive generated by the platform is inaccessible

This limitation does not negate successful remediation of active repository refs and current GitHub ZIP distribution.

---

## Zenodo v1.0.0 Remediation

The Zenodo v1.0.0 record associated with:

```text
10.5281/zenodo.20815612
```

was restricted during repair.

The release package was rebuilt so that:

- the sanitized derivative replaced the prior artifact
- the corrected snapshot checksum was included
- the intended v1.0.0 file inventory was preserved
- no unrelated archive content changed

Corrected archive:

```text
daniel-longitudinal-public-v1.0.0.zip
```

Verified corrected archive digests:

```text
MD5:    4dd3838c5c1f90003e1c98d72fec812e
SHA-256: 0c00fc1c7ea7a708d6fe6224c88fc33b6a4b853e6fbc127c88a0432b5bc8d330
```

The corrected published package was independently downloaded and verified for:

- archive structure
- expected top-level root
- expected file count
- sanitized blood-panel contents
- internal checksum agreement
- absence of unrelated archive differences

The DOI and biological interpretation of v1.0.0 remained unchanged.

---

## RingConn Source Exports

The 2026-07-21 RingConn package underwent read-only privacy screening before public inclusion.

The review identified:

- no obvious administrative-identifier fields in headers
- no email-like values
- expected wearable-domain fields only
- no apparent account, serial-number, token, address, or precise-location field in the exported schema

The original downloaded filenames contained an unnecessary personal naming string.

The public filenames were normalized without altering CSV contents.

The source exports were then:

- protected from Git line-ending conversion
- preserved byte-for-byte
- registered with SHA-256 checksums
- verified against the original downloads
- verified from a fresh GitHub ZIP

The package remains source evidence rather than a normalized analytical dataset.

---

## Current Distribution Status

Current verified remediation state:

| Surface | Status |
|---|---|
| Active GitHub `main` branch | Remediated and verified |
| Applicable maintained Git tags | Remediated and verified |
| Fresh GitHub repository ZIP | Remediated and verified |
| Zenodo v1.0.0 package | Replaced and independently verified |
| GitHub residual or orphaned objects | Support request pending |
| Prior uncontrolled clones or downloads | Not controllable |
| Third-party caches or mirrors | Not guaranteed removed |

Appropriate overall classification:

**Controlled distribution remediation completed, with GitHub provider-side cleanup pending and uncontrolled-copy limitations disclosed.**

---

## Version Note

This methodology was revised on 2026-07-22 after completion of the archive’s first material public-artifact sanitization, Git-history rewrite, DOI-package repair, and byte-preserved wearable-source ingestion.

The revision:

- defines public sanitized derivatives and filename-normalized sources
- preserves the intentional public identity boundary
- documents true redaction and hidden-content requirements
- defines current-tree, active-ref, historical-object, and provider-side remediation separately
- records completion of the July 2025 blood-panel sanitization
- records completion of active Git branch and tag remediation
- records the pending GitHub Support cleanup state
- records correction and verification of the Zenodo v1.0.0 package
- records privacy and byte-integrity review of the RingConn source exports
- defines controlled-distribution and uncontrolled-copy limitations
- prohibits claims of provider-side deletion before confirmation

The revision does not alter:

- any biological measurement
- any curated longitudinal value
- any prediction record
- any closed outcome
- any protocol exposure
- any phase status
