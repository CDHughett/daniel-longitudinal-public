# Post-Release Coherence Drift Cleanup Audit

**Audit date:** 2026-09-14  
**Scope:** live post-v1.1.0 public-facing orientation and coherence controls  
**Repository:** `CDHughett/daniel-longitudinal-public`

---

## Purpose

The v1.1.0 publication and Batch 5B reconciliation correctly established the authoritative GitHub/Zenodo release identity, but a post-release outsider review identified several live-orientation surfaces that had not fully absorbed the new state.

This cleanup is intentionally narrow. It repairs current-facing drift without rewriting historical reports, historical audits, preregistration artifacts, or contemporaneous documents that correctly preserve an earlier then-current state.

---

## Authoritative live release identity

```text
Current published release: v1.1.0
Finalized version DOI:     10.5281/zenodo.22759132
All-versions DOI:          10.5281/zenodo.20815611
Frozen release commit:     92126e1cc882c3822d9e03b30b11cfc1d30b4fbb
```

---

## Drift found

### 1. Live DOI/version surfaces lagged the external publication boundary

`LATEST.md`, `VERSIONING.md`, and the release-metadata section of `VERIFICATION.md` still exposed prior-release wording after Batch 5B had established the authoritative v1.1.0 version DOI and all-versions DOI roles.

### 2. Observer/newcomer pointers lagged the weekly rollover

`docs/OBSERVER_QUICKSTART.md` and `docs/NEWCOMER_PATH.md` still directed readers to W35 as the closed-week example while W36 was already the most recent closed weekly report.

### 3. Observer/newcomer language still implied incomplete August state

The live orientation path still contained wording such as pending snapshot evidence, current open prediction, or still-pending TruDiagnostic state even though records 041–046 are closed and the August molecular/snapshot integration is complete.

Historical documents that were written while those states were genuinely pending remain unchanged.

### 4. Weekly re-entry posture and broader Phase 2 substate were easy to conflate

`LATEST.md` described the immediate weekly posture as consolidation / re-entry observation while `PHASE_MAP.md` described the broader Phase 2 operating substate as consolidation / lock-in observation.

These are not competing phase declarations. The former is the active weekly observation condition following travel; the latter is the canonical broader Phase 2 interpretation.

---

## Repairs

- `LATEST.md`
  - exposes current published release identity
  - exposes both version-specific and all-versions DOI roles
  - separates **weekly operating posture** from **broader Phase 2 substate**
  - explicitly explains their relationship
  - lists the post-release coherence validator in the live verification stack

- `VERSIONING.md`
  - changes the current-release section from v1.0.0 to published v1.1.0
  - records the finalized version DOI, all-versions DOI, and frozen release commit
  - keeps the prior v1.0.0 DOI as historical release identity rather than current state
  - clarifies that post-publication ordinary commits do not move or rewrite the frozen v1.1.0 tag/package

- `VERIFICATION.md`
  - updates the release-metadata section to the published v1.1.0 identities
  - expands the verification architecture from three to four read-only layers
  - documents the post-release coherence validator, local commands, CI execution, and current scope
  - preserves older version-note entries as historical state rather than rewriting them

- `docs/OBSERVER_QUICKSTART.md`
  - points to W36 as the most recent closed report
  - removes stale current-state language implying open/pending August work
  - adds the August retrospective synthesis to the inspection route
  - explains weekly posture versus broader phase-map state
  - adds the coherence validator to the inspection route

- `docs/NEWCOMER_PATH.md`
  - points to W36 as the most recent closed report
  - replaces pending August/Record 043 language with completed-state guidance
  - distinguishes current completion state from historically correct pending-state documents
  - distinguishes immediate weekly posture from broader operating substate
  - adds the coherence validator to the validation path

- `tools/validate_coherence.py`
  - protects the published v1.1.0 identity across live release/orientation surfaces
  - protects version DOI and all-versions DOI relationships
  - protects `CITATION.cff` / `CODEMETA.json` release identity
  - protects `VERSIONING.md` current-release identity and frozen release commit
  - protects `VERIFICATION.md` current DOI identity and coherence-validator documentation
  - protects active-week and most-recent-closed-week pointers
  - prevents observer/newcomer regression to the stale W35 pointer
  - prevents reintroduction of selected stale pending-state phrases
  - protects the explicit weekly-posture / broader-substate distinction

- `.github/workflows/validate.yml`
  - runs the coherence validator on pull requests and pushes to `main`

- `tools/README.md`
  - documents the fourth read-only validation layer

---

## Preservation boundary

This cleanup does **not**:

- rewrite historical weekly reports
- rewrite dated audits
- rewrite the August preregistration/collection plan
- rewrite historically accurate version-note entries in `VERIFICATION.md`
- alter canonical CSV values
- alter source artifacts or checksums
- reopen or rescore Model Error records
- change phase or protocol state
- move the `v1.1.0` tag
- mutate the published GitHub or Zenodo release artifact

A historical document may continue to say that evidence was pending or a prediction was open when that statement was true at the document's original timestamp.

---

## Acceptance gates

The cleanup is acceptable only if:

1. core repository validation passes;
2. machine-readable validation passes;
3. August snapshot cross-layer validation passes;
4. post-release coherence validation passes;
5. no canonical scientific-data or source-artifact file changes;
6. the PR contains only live orientation, versioning/verification, validation, and audit/changelog changes.

---

## Interpretation

The purpose of this cleanup is not to add another governance layer for its own sake. It closes a specific failure mode exposed by the post-release outsider audit: lower-level repository validation can be green while a small number of public-facing orientation statements have drifted behind the authoritative archive state.

The new validator therefore protects only those concrete relationships rather than attempting to make every historical statement dynamically current.
