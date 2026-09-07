# Validation Tools

The repository uses two read-only Python validators.

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

Both validators use only the Python standard library.

Neither validator edits the repository.

A pass means the implemented mechanical/semantic checks passed. It does not establish biological plausibility, causal interpretation, measurement validity, or clinical meaning.

## CI

`.github/workflows/validate.yml` runs both validators on pushes to `main`, on pull requests, and by manual workflow dispatch.

The workflow is intentionally lightweight and read-only.
