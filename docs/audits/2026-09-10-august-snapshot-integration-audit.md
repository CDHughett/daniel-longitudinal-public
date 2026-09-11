# August Snapshot Integration Audit — 2026-09-10

**Audit type:** Batch 5 final semantic / diff / privacy / release-readiness review  
**Repository:** `CDHughett/daniel-longitudinal-public`  
**Branch:** `snapshot-2026-08-integration`  
**Base branch:** `main`  
**Scope:** August 2026 TruDiagnostic integration, Model Error 043 closure, current-state propagation, methodology-guide consolidation, and public-artifact privacy state

---

## Purpose

This audit reviews the complete August molecular-integration change surface after source-backed structured ingestion and Model Error 043 adjudication.

The review is intended to answer four separate questions:

1. Is the biological/model-error adjudication consistent with the preregistered rules?
2. Are current-facing repository surfaces internally coherent?
3. Did the large `methodology/README.md` consolidation remove governing methodology or only duplicated directory-guide content?
4. Is the branch ready for public merge/release from a privacy and distribution standpoint?

---

## Semantic Verdict

**PASS — Model Error 043 adjudication is consistent with the preserved preregistered rules.**

The original prediction remains unchanged.

The governing plan requires all of the following for measurable overall improvement:

- at least two of three core biological anchors improve beyond their operational thresholds
- any remaining core anchor is stable or improved
- at least 60% of directly comparable supporting metrics are stable or improved
- neither the system-age group nor the TruHealth group contains a materially adverse majority
- no source-quality/comparability issue invalidates the primary comparison

Observed May → August core-anchor classifications are:

```text
OMICm age delta:
-3.7 → -3.9 years
0.2 years more favorable
classification: stable
registered improvement threshold: >= 0.5 years more favorable

DunedinPACE:
0.79 → 0.77
0.02 lower
classification: improved
registered improvement threshold: >= 0.01 lower

SymphonyAge:
37.8 → 46.1 years
8.3 years higher
classification: adverse
registered improvement threshold: >= 1.0 year lower
```

Only one of three core anchors materially improved, and the remaining-anchor condition was not met because SymphonyAge was materially adverse.

The supporting profile also fails its registered breadth requirement:

```text
system/organ ages:
0 improved
0 stable
11 adverse

TruHealth domains:
8 improved
3 stable
8 adverse

combined stable or improved:
11 / 30 = 36.7%

registered requirement:
>= 60%
```

Record 043 therefore correctly closes as:

```text
prediction: moderate_improvement
actual: overall_improvement_not_met
status: closed
support: not supported
error_direction: over
```

The closure does not establish generalized biological deterioration or a causal explanation for the provider-output changes.

---

## Source-Role Verdict

**PASS — canonical collection timing/preparation remains correctly separated from provider administrative metadata.**

The governed contemporaneous collection event remains:

```text
2026-08-17
05:37 local
```

The provider-displayed date/fasting fields remain provider administrative metadata and do not replace the contemporaneous collection record.

No biological value is modified by this reconciliation.

---

## Methodology-Guide Consolidation Review

**PASS — the large deletion count in `methodology/README.md` is a documentation consolidation, not deletion of governing preregistration artifacts.**

The branch reduces a large historical/current hybrid directory guide into a smaller navigation/governance guide while leaving the actual standing and preregistered methodology files intact.

The following governing artifacts are not rewritten by the consolidation:

- `methodology/data-collection.md`
- `methodology/anonymization.md`
- `methodology/prediction_evaluation.md`
- `methodology/open_prediction_evaluation_plan_041_044.md`
- `methodology/open_prediction_evaluation_plan_045.md`
- `methodology/open_prediction_evaluation_plan_046.md`
- `methodology/2026-08-snapshot-collection-plan.md`

The consolidation primarily removes duplicated historical outcome detail and volatile current-state fields that are better maintained in `LATEST.md`, `data/DATA_COVERAGE.md`, the model-error layer, Git history, and the changelog.

---

## Privacy Finding — F01

**MERGE/RELEASE BLOCKER — raw August TruDiagnostic PDFs contained an unnecessary administrative sample/specimen identifier.**

Repository privacy methodology intentionally permits the subject's public name and chronological age, but normally excludes unnecessary patient/specimen/account-style administrative identifiers from public artifacts.

Batch 5 inspection of all three August provider reports found such an identifier in the report header.

No full date of birth, private telephone number, private email address, or subject street address was identified in the reviewed report text. Provider organizational contact information is not the subject's private contact information.

The issue is therefore narrow but material under the repository's own public-artifact policy.

### Current-branch remediation

The three raw provider PDFs were removed from `snapshot-2026-08-integration`, and their entries were removed from the August checksum manifest.

The current branch therefore no longer intentionally distributes those raw provider files.

Structured August molecular values remain source-backed and unchanged. Their removal is a privacy/distribution action, not a biological-value correction.

### Candidate sanitized derivatives

As a technical verification exercise, candidate sanitized derivatives were created from retained user-provided copies of all three provider reports using true PDF redaction of the unnecessary administrative identifier.

Verification showed:

- the identifier was absent from extracted text after redaction
- normalized extracted text was otherwise identical to each corresponding retained source copy
- representative first, middle, and final pages rendered successfully
- no biological value was intentionally altered

Those candidate derivatives are **not adopted as the canonical public repository artifacts in this batch** because the retained user-provided source-file bytes differ from the previously published repository PDF blobs. A future adoption should either sanitize the exact retained canonical source or explicitly register the derivative/source relationship before checksum publication.

---

## Historical-Distribution Boundary — F02

**OPEN / EXPLICIT AUTHORIZATION REQUIRED.**

Deleting the raw PDFs from the current integration branch does not remove earlier public Git objects from history.

The repository's anonymization methodology distinguishes:

```text
current-tree remediation
active-ref remediation
historical-object remediation
provider-side object cleanup
```

Batch 5 performs branch current-tree remediation only.

It does **not** perform a force rewrite of `main`, tags, or repository history. It also does not claim provider-cache or third-party clone removal.

A history rewrite would change commit identities and may affect local clones, tags, open references, audit links, and external copies. It therefore requires a separate explicit decision rather than being performed incidentally inside this audit.

---

## Current-State Coherence

The August structured data and Model Error 043 state are internally coherent after Batch 4 propagation:

- record 043 is closed / not supported / `over`
- original prediction wording remains preserved
- `calibration_state=pre` remains registration provenance
- primary trajectory concordance is 2/4 = 0.50
- Phase 2 — Load Integration remains unchanged
- Phase 2D remains undeclared
- the underlying B1 + Load Integration architecture remains unchanged

Current-facing snapshot documentation is updated in Batch 5 to distinguish:

- complete molecular source review and structured integration
- public raw-provider-PDF deferral for privacy
- separate historical-distribution remediation

Historical reports and audits whose earlier `043 open/pending` wording was accurate at the time remain unchanged.

---

## Release-Readiness Decision

**NOT READY FOR MERGE/RELEASE AS A FULLY CLOSED PRIVACY REMEDIATION CYCLE.**

Biological/model-error integration is semantically ready.

Current-branch raw-PDF exposure is remediated by deletion.

However, the earlier public Git-history exposure requires a separate decision before the repository should describe the August molecular artifact privacy cycle as fully resolved.

The pull request should remain draft until that decision is made.

No new Zenodo release should be created from this state.

---

## Validation Requirement

Final acceptance of the Batch 5 branch requires successful GitHub Actions execution of:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
```

Known governed canonical-sleep warnings may remain if unchanged from prior validated states.

A mechanical PASS does not override the privacy/history boundary documented above.

---

## Final Batch 5 Classification

```text
Biological source-value correction:
No

Model Error 043 adjudication:
Confirmed

Preregistered prediction wording change:
No

Methodology preregistration artifact rewrite:
No

Current-branch public raw TruDiagnostic PDFs:
Removed pending compliant sanitized derivatives

Historical Git-object remediation:
Not performed

Protocol change:
No

Phase change:
No

Release / DOI change:
No

Merge readiness:
Blocked pending explicit privacy-history disposition
```
