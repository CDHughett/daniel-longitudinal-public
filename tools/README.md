# Validation Tools

The repository uses four read-only Python validators.

## Core repository validator

```text
python tools/validate_repository.py
```

Checks repository mechanics, links, CSV structure, checksum manifests, canonical sleep continuity, weekly-report continuity, current-state surface and live-coverage alignment, protected model-error state, release metadata, and source-export integrity.

## Machine-readable layer validator

```text
python tools/validate_machine_readable.py
```

Checks the public daily/training/event layer defined in:

[`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)

The extension checks:

- required headers
- unique daily dates
- daily date continuity
- unique training session IDs
- unique context-event IDs
- date parsing and bounds
- numeric field syntax
- controlled vocabularies
- v1 duration-expression semantics
- `source_ref` syntax
- extensible `snake_case` namespaces
- event interval ordering
- related-week syntax
- related model-error existence
- cross-file date relationships

## August snapshot cross-layer validator

```text
python tools/validate_august_snapshot.py
```

Protects the completed August 2026 snapshot across integrated structured values, epigenetic longitudinal values, source/date reconciliation, Model Error 043 closure, protected source artifacts, and registered SHA-256 identities.

## Post-release coherence validator

```text
python tools/validate_coherence.py
```

Protects a deliberately narrow set of live public-facing relationships that can drift even when lower-level repository checks remain green:

- published `v1.1.0` identity
- finalized version DOI and all-versions DOI across live orientation surfaces
- `CITATION.cff` / `CODEMETA.json` release identity
- current active-week and most-recent-closed-week pointers
- observer/newcomer report pointers
- completed August-state language on live orientation documents
- distinction between the immediate weekly operating posture and the broader canonical Phase 2 substate
- current-facing validation-documentation role consistency, including protection against stale two-validator wording
- first-contact navigation-role separation across README, START_HERE, observer/newcomer guidance, and INDEX
- presence of plain-language current-state bridges on README/LATEST without forcing session-level jargon onto first-contact surfaces
- preservation of the deeper terminology bridge in `docs/CONCEPTS.md`

The coherence validator does not rewrite historical documents merely because they correctly preserve an earlier then-current state.

All validators use only the Python standard library.

None of the validators edits the repository.

A pass means the implemented mechanical/semantic/coherence checks passed. It does not establish biological plausibility, causal interpretation, measurement validity, or clinical meaning.

## CI

`.github/workflows/validate.yml` runs all four validators on pushes to `main`, on pull requests, and by manual workflow dispatch.

The workflow is intentionally lightweight and read-only.
