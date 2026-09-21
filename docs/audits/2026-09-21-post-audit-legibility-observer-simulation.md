# 2026-09-21 Post-Audit Legibility / Observer-Simulation Review

**Repository:** `CDHughett/daniel-longitudinal-public`  
**Review branch:** `post-audit-hardening-batch5`  
**Baseline for cleanup stack:** `main` at `af33962e925cb4c6443b8d94f21546e1b0eeee1e`  
**Review date:** 2026-09-21  
**Scope:** post-weekly-update documentation drift, terminology density, navigation, and current-facing legibility  
**Method:** simulated observer review plus mechanical cross-document checks  
**Verdict:** **PASS — materially lower entry cost without loss of technical depth**

---

## Purpose

This review evaluates the completed five-batch post-weekly-update cleanup as an external-facing system rather than as a scientific-data update.

The questions are:

1. Can a casual reader determine what the repository is, what is happening now, and where to go next without being forced through several overlapping orientation documents?
2. Can a skeptical reviewer move from current claims to structured evidence, provenance, data-quality notes, closed interpretation, and validation without relying on narrative trust?
3. Can a data-oriented reader reach the machine-readable layer, schema, source references, coverage boundaries, and data-quality constraints with minimal navigation ambiguity?
4. Do plain-language first-contact surfaces preserve access to the more precise archive vocabulary rather than replacing it?
5. Is the documentation architecture less likely to drift back toward stale validator inventories or competing mandatory reading paths?

This is a simulated observer exercise, not a usability study with independent human participants.

---

## Cleanup Stack Reviewed

The reviewed stack contains four legibility/maintenance batches before this hardening pass:

```text
Batch 1
validation-documentation drift cleanup

Batch 2
terminology bridge / state-label compression

Batch 3
first-contact navigation compression

Batch 4
live-facing language simplification
```

Relative to the pre-cleanup `main` baseline, those four batches changed current-facing documentation only. No structured scientific data, weekly report evidence, protocol state, phase declaration, Model Error outcome, DQ status, release identity, Git tag, or DOI lineage was changed.

---

## 1. Validation-Documentation Drift Check

The following current-facing documents were reviewed:

- `docs/START_HERE.md`
- `DATASET_OVERVIEW.md`
- `docs/FOR_OBSERVERS.md`
- `data/DATA_COVERAGE.md`
- `methodology/README.md`

Result:

```text
stale "runs both" language:                 absent
stale "Two read-only validators" language: absent
tools/README.md authoritative reference:   present in all five
VERIFICATION.md authoritative reference:  present in all five
```

The current validator inventory remains centralized in:

- `tools/README.md`
- `VERIFICATION.md`

Domain documents may still mention an individual validator when it directly improves interpretation of that domain.

This reduces the maintenance surface if the validator suite changes again.

---

## 2. Orientation-Role Separation

The current first-contact documents now have non-overlapping primary jobs:

| Surface | Primary job |
|---|---|
| `README.md` | public front door and task selection |
| `docs/START_HERE.md` | five-minute conceptual orientation |
| `LATEST.md` | volatile current system state |
| `docs/OBSERVER_QUICKSTART.md` | shortest ordered skeptical audit route |
| `docs/NEWCOMER_PATH.md` | optional extended learning curriculum |
| `docs/FOR_OBSERVERS.md` | skeptical-review reference/checklist |
| `INDEX.md` | exhaustive repository navigation |

Mechanical review confirmed:

- README explicitly says its entry points are alternatives rather than a required reading sequence
- START_HERE tells readers arriving from README not to reread README
- START_HERE says the deeper documents are not mandatory sequential prerequisites
- OBSERVER_QUICKSTART explicitly owns the ordered audit route
- the old `README / START_HERE` audit-chain text is absent from OBSERVER_QUICKSTART
- NEWCOMER_PATH is explicitly optional
- FOR_OBSERVERS is explicitly a reference/checklist and no longer contains a competing `Recommended Review Path`
- INDEX describes first-contact navigation as task-based rather than sequential

The repository therefore no longer presents four partially overlapping orientation documents as if they were all prerequisites.

---

## 3. Plain-Language / Precision Layering

The live first-contact surfaces now contain a plain-language bridge before the formal archive vocabulary.

README states, in substance, that training remains stable and low-overhead and that the active week is watching whether the extra capacity observed at the prior closeout repeats before progression is considered.

LATEST provides the same idea before listing the formal state fields.

On the two live first-contact surfaces:

```text
low-salience: 0 occurrences
trait-like:   0 occurrences
trait-level:  0 occurrences
```

The parent phrase `low-overhead` is used instead where session-level classification detail is not necessary.

The precise vocabulary remains preserved one layer deeper:

- `docs/CONCEPTS.md` retains Ambient Execution, Trait-Like Execution, and Trait-Level Expression
- `reports/2026-W37.md` retains its original low-salience / ambient / trait-like / trait-level wording
- `reports/2026-W38.md` retains the active-report terminology
- the structured training layer remains unchanged

This is progressive disclosure rather than vocabulary deletion.

---

## 4. Terminology Bridge Check

The glossary now independently defines the terms that a current observer is most likely to encounter without context:

- Weekly Operating Posture
- Data-Quality Record (DQ)
- Capacity Versus Exposure
- Reserve (Capacity)
- Ambient Execution
- Trait-Like Execution
- Trait-Level Expression
- B1
- Load Integration

START_HERE also provides the state hierarchy:

```text
declared phase
    ↓
broader operating substate
    ↓
weekly operating posture
    ↓
session-level observations
```

The governing distinction is explicit: evidence at a lower level does not automatically promote the level above it.

That protects against a common outsider misunderstanding in the current archive state: reading one favorable reserve observation as equivalent to a protocol progression, substate transition, or new phase declaration.

---

## 5. Simulated Observer A — Casual Technical Reader

### Questions

Can this reader answer:

1. What is this?
2. What is happening now?
3. Why should I take the archive seriously?
4. Where do I go if I want more depth?

### Route

```text
README
→ optionally START_HERE
→ LATEST if current detail is wanted
```

### Simulated perception

**What is this?**

A governed single-subject longitudinal observational archive rather than a clinical trial, coaching product, or generalized intervention protocol.

**What is happening now?**

The current training architecture is stable; the active Week 38 question is whether extra capacity observed at Week 37 closeout repeats before progression is considered.

**Why take it seriously?**

The front-facing material exposes provenance, machine-readable data, failed/not-supported predictions, data-quality restrictions, correction rules, validation, and frozen release identity rather than presenting only favorable outcomes.

**Where next?**

The reader can choose current state, structured evidence, skeptical audit, or exhaustive navigation directly from the README.

### Result

**PASS.**

The casual reader no longer needs to decode the full session-level vocabulary before understanding the current question.

---

## 6. Simulated Observer B — Skeptical Researcher / Reviewer

### Questions

Can this reader move from a current claim to the evidence beneath it without being asked to trust the narrative first?

### Route

```text
OBSERVER_QUICKSTART
→ LATEST
→ DATA_COVERAGE
→ machine-readable schema + core CSVs
→ source provenance / source exports
→ DATA_QUALITY_NOTES
→ most recent closed report
→ model-error layer
→ governance
→ validators
```

### Simulated perception

The archive presents the skeptical review route as evidence-first rather than narrative-first.

The reviewer can distinguish:

- source artifact from curated row
- measurement from subjective state
- context tag from bounded context event
- active observation from retrospective closeout
- candidate evidence from scored outcome
- correction from retrospective rewriting
- weekly posture from broader substate and phase
- mechanical validation from biological validity

The observer reference remains available when those distinctions need explanation, but it no longer competes with the quickstart as a second ordered route.

### Result

**PASS.**

The skeptical reviewer has one primary audit path and a separate reference document rather than two overlapping procedures.

---

## 7. Simulated Observer C — Data Analyst / Reuser

### Questions

Can this reader quickly determine:

1. what public tables exist?
2. their units of observation?
3. their current coverage?
4. the schema and provenance semantics?
5. where uncertainty / data-quality restrictions are recorded?

### Route

```text
README
→ DATA_COVERAGE
→ machine-readable-layer-v1 schema
→ core CSVs
→ source_provenance
→ DATA_QUALITY_NOTES
```

### Simulated perception

The structured-data route is direct.

The analyst is not required to read the weekly narrative first. The coverage document identifies the represented public layer; the schema explains row semantics and `source_ref`; provenance separates private-source identity from public extracts; data-quality notes preserve unresolved restrictions.

### Result

**PASS.**

The archive now makes it easier to approach the repository as a reusable data object rather than only as a narrative record.

---

## 8. Remaining Cognitive Density

The cleanup reduces entry cost; it does not make the repository simple.

That is appropriate.

Technical density remains in the deeper layers because the archive genuinely contains:

- multiple evidence classes
- several units of observation
- prospective and retrospective reasoning
- source reconciliation
- model-error governance
- phase/substate/posture distinctions
- release and DOI boundaries
- private-source provenance
- validation and audit history

The remaining density is now more often **optional depth** rather than **front-door friction**.

The most important residual maintenance risk is not document length by itself. It is future duplication: if current validator inventories, weekly-state explanations, or reading sequences begin to be copied across many documents again, the same drift can return.

---

## 9. Anti-Drift Hardening

`tools/validate_coherence.py` was expanded in this batch to protect selected legibility relationships without creating a fifth validator.

New protected relationships include:

- absence of stale two-validator wording on current-facing validation documents
- presence of authoritative `tools/README.md` and `VERIFICATION.md` references
- task-based first-contact navigation
- absence of the prior circular/mandatory orientation chain
- OBSERVER_QUICKSTART ownership of the short audit route
- optional-curriculum role for NEWCOMER_PATH
- reference/checklist role for FOR_OBSERVERS
- plain-language current-state summaries on README and LATEST
- absence of stacked `low-salience`, `trait-like`, and `trait-level` jargon on those two first-contact surfaces
- preservation of the corresponding precise terminology bridge in `docs/CONCEPTS.md`
- preservation of the START_HERE state-label hierarchy

The validator still does not reinterpret historical documents or require old reports/audits to adopt current navigation language.

---

## 10. Observer-Simulation Verdict

**PASS — materially lower entry cost without loss of technical depth.**

The cleanup changed the observer experience in three important ways:

1. **fewer competing doors** — a new reader can choose a task instead of being handed a long list of equally prominent repository subsystems
2. **plain language before archive language** — current state is understandable before the reader learns the precise internal taxonomy
3. **one audit route, one reference layer** — skeptical inspection is procedural rather than navigationally ambiguous

The repository still asks serious readers to learn its vocabulary, but that learning is now staged rather than front-loaded.

The resulting perception is closer to:

> a governed longitudinal research archive with a clear public front door and inspectable deeper machinery

than:

> a dense internal operating system that outsiders must decode before they can decide where to start

No scientific claim is strengthened by this review. The result concerns documentation coherence, observer legibility, and maintenance architecture only.
