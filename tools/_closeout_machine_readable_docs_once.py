from pathlib import Path
import re


def replace_exact(path_str: str, old: str, new: str) -> None:
    path = Path(path_str)
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path_str}: expected exactly one match, found {count}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def replace_regex(path_str: str, pattern: str, replacement: str) -> None:
    path = Path(path_str)
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, flags=re.S)
    if count != 1:
        raise SystemExit(f"{path_str}: expected exactly one regex match, found {count}")
    path.write_text(updated, encoding="utf-8")


replace_regex(
    "schemas/machine-readable-layer-v1.md",
    r"## Accepted Historical Training Aliases\n.*?(?=\n## File-Level Private Provenance)",
    '''## Standardized Training Provenance

All current live `training_blocks_v1.csv` rows use the canonical private-source forms above.

Historical aliases created during the initial backfill, such as:

```text
wb:v<version>:TB:<YYYY-MM-DD>[:<session_label>]
pdf:v<version>:TB:<YYYY-MM-DD>[:<session_label>]
```

remain visible in Git history only.

They are not accepted in the current live v1 dataset or by the current machine-readable validator.

The 2026-09-07 migration changed `source_ref` provenance locators only; non-`source_ref` training fields were preserved.
'''
)
replace_exact(
    "schemas/machine-readable-layer-v1.md",
    "| `source_ref` | text | provenance | required; canonical or accepted v1 alias |",
    "| `source_ref` | text | provenance | required; canonical private-source form |",
)

replace_exact(
    "DATA_DICTIONARY.md",
    '''Historical training rows may retain accepted v1 aliases:

```text
wb:v<version>:TB:<YYYY-MM-DD>[:label]
pdf:v<version>:TB:<YYYY-MM-DD>[:label]
```

Those aliases remain valid historical provenance but are deprecated for new rows.
''',
    '''All current live training rows use the canonical private-source forms above.

Legacy `wb:v...` and `pdf:v...` aliases remain visible in Git history as provenance of the initial backfill, but they are no longer valid in the live v1 dataset.
'''
)

replace_exact(
    "DATASET_OVERVIEW.md",
    "Historical training rows retain accepted v1 aliases such as `wb:v1.28:TB:...`; those aliases are deprecated for new rows but remain valid historical provenance.",
    "All 325 current training rows now use the canonical `private_workbook:` / `private_pdf:` source-reference grammar. Earlier `wb:v...` / `pdf:v...` aliases remain visible in Git history only.",
)

replace_exact(
    "data/source_provenance/README.md",
    '''or the accepted historical training alias:

```text
wb:v1.28:TB:2026-08-30:LI
```

Those values locate the source version/tab/date.
''',
    '''Training rows use the same canonical locator family, for example:

```text
private_workbook:Daniel_Dataset_v1.28:Training Blocks:2026-08-30:LI
```

Earlier compact `wb:v...` / `pdf:v...` aliases remain in Git history but were standardized out of the live v1 training dataset on 2026-09-07.

These values locate the source version/tab/date.
'''
)

replace_exact(
    "VERIFICATION.md",
    '''This repository supports external verification at two distinct levels:

1. **artifact verification** — confirms the identity of registered files
2. **repository validation** — checks the mechanical integrity and governed structure of the archive
''',
    '''This repository supports external verification at three complementary automated/mechanical levels:

1. **artifact verification** — confirms the identity of registered files
2. **repository validation** — checks the mechanical integrity and governance-protected structure of the archive
3. **machine-readable semantic validation** — checks the current daily/training/event schema contract and cross-file relationships

Human semantic review remains a separate layer after automated validation.
'''
)

replace_exact(
    "VERIFICATION.md",
    '''- alter checksums

---

# Local Repository Validator
''',
    '''- alter checksums

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
- 203 continuous daily-biomarker rows through 2026-08-30
- unique daily dates
- 325 protected v1 training-session rows
- 325 unique training `session_id` values
- canonical `private_workbook:` / `private_pdf:` `source_ref` syntax
- date parsing and represented-interval bounds
- numeric-field syntax
- controlled vocabularies
- `snake_case` extensible vocabularies
- v1 `duration_min` expression semantics
- 42 unique context-event IDs
- event interval ordering
- related-week syntax
- model-error cross-reference existence
- cross-file date relationships

The protected 325-session count is intentional for the currently frozen v1 interval through 2026-08-30. A governed future extension must update the dataset and validator together.

This validator is also read-only. It does not infer missing sessions, rewrite source references, classify biological meaning, or repair the archive.

---

# Local Repository Validator
'''
)

replace_exact(
    "VERIFICATION.md",
    '''This mode may support future local automation.

It does not currently imply a GitHub Actions workflow.
''',
    '''Both validators support local command-line execution, and the repository validator supports `--json` structured output.

Repository validation is also executed automatically in GitHub Actions as described below.
'''
)

replace_exact(
    "VERIFICATION.md",
    '''# GitHub Actions Status

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
''',
    '''# GitHub Actions Status

Lightweight automated validation is active through:

```text
.github/workflows/validate.yml
```

The workflow runs on:

- pushes to `main`
- pull requests

It uses read-only repository permissions:

```text
contents: read
```

and executes:

```text
python tools/validate_repository.py
python tools/validate_machine_readable.py
```

The workflow is intentionally narrow. It does not edit files, commit corrections, publish releases, or replace human semantic review.

Local execution remains available for audits, ZIP verification, and debugging.
'''
)

replace_exact(
    "VERIFICATION.md",
    "2. run the local validator",
    "2. run both read-only validators (`tools/validate_repository.py` and `tools/validate_machine_readable.py`)",
)

replace_exact(
    "VERIFICATION.md",
    '''- a downloaded ZIP is mechanically safe and internally consistent

Verification does not independently establish:
''',
    '''- a downloaded ZIP is mechanically safe and internally consistent
- the current machine-readable daily/training/event layer satisfies its declared schema checks
- all 325 protected v1 training sessions remain present and uniquely identified
- current live training `source_ref` values use the canonical private-source grammar
- registered private-source hashes match the exact private bytes when those bytes are independently available for comparison

Verification does not independently establish:
'''
)

replace_exact(
    "VERIFICATION.md",
    "# Notes\n",
    '''# Private-Source Provenance Verification

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
'''
)

verification = Path("VERIFICATION.md")
vtext = verification.read_text(encoding="utf-8")
closeout_note = '''

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
'''
if "## 2026-09-07 Machine-Readable Hardening Closeout" in vtext:
    raise SystemExit("VERIFICATION.md: closeout note already present unexpectedly")
verification.write_text(vtext.rstrip() + closeout_note + "\n", encoding="utf-8")

changelog = Path("CHANGELOG.md")
ctext = changelog.read_text(encoding="utf-8")
anchor = "## [Unreleased]\n\n### Added\n"
if ctext.count(anchor) != 1:
    raise SystemExit(f"CHANGELOG.md: expected one Unreleased/Added anchor, found {ctext.count(anchor)}")
entry = '''## [Unreleased]

### Changed

#### September 7 machine-readable hardening closeout

- Standardized all 325 live `data/training_blocks_v1.csv` `source_ref` values to the canonical `private_workbook:` / `private_pdf:` provenance grammar.
- The finalized migration changes provenance locators only; the 325-session set and all non-`source_ref` training field values are preserved.
- Updated `schemas/machine-readable-layer-v1.md`, `DATA_DICTIONARY.md`, `DATASET_OVERVIEW.md`, and `data/source_provenance/README.md` so current documentation no longer treats compact `wb:v...` / `pdf:v...` aliases as valid live-v1 values. Those aliases remain inspectable in Git history.
- Hardened `tools/validate_machine_readable.py` to require the protected 325-session v1 training set and canonical source-reference syntax in addition to its existing identifier, date, vocabulary, numeric, duration, event-interval, cross-file, and model-error-reference checks.
- Revised `VERIFICATION.md` to document three verification levels: artifact verification, core repository validation, and machine-readable semantic validation.
- Confirmed lightweight read-only CI is active through `.github/workflows/validate.yml` on pushes to `main` and pull requests.
- Recorded private `Daniel_Dataset` source-file hashes where exact immutable retained workbooks were available, while leaving unavailable historical hashes explicitly missing rather than reconstructing them.
- Added `docs/AI_ASSISTANCE.md` and preserved AI assistance as a maintenance/analysis aid rather than a source-evidence class.
- Added the future model-error schema design separating registration status from model-calibration scope while leaving current protected v1 records unchanged.
- Canonicalized the current UDI expansion as **Unobstructed Delta Index** on current-facing documentation surfaces.

Migration correction record:

- Commit `aa7297fa6c5dff5f8db528773978ee2bd46ef592` was a transient intermediate source-ref migration state that unintentionally contained 251 rather than 325 training rows.
- The existing validator correctly checked syntax and uniqueness but did not yet protect the expected session count, so that intermediate state passed CI.
- Commit `7dff020bb7763edde880346d05ef7c955368f281` restored the full 325-row training source before migration.
- Commit `5167b4afd743a7594f6cd3bebe490411d09db0a4` then canonicalized 325 source references across 325 rows and verified 325 unique session IDs before committing.
- Commit `5e6801d0c08f506d7fc49ad3852a960d1558dbf3` added the explicit 325-row validator guard and canonical-only source-reference requirement.
- GitHub Actions run `34069047100` on that hardened state completed successfully: core validator PASS with 0 errors, 2 governed sleep warnings, and 9 passes; machine-readable validator PASS with 0 errors and 0 warnings, reporting 203 daily rows, 325 training rows / 325 unique session IDs, and 42 context events.

Classification:

```text
Biological-value change:
No

Canonical sleep change:
No

Training non-provenance field change:
No

Prediction wording or outcome change:
No

Phase or protocol change:
No

Release or DOI change:
No

Provenance/schema/validation hardening:
Yes
```

### Added
'''
changelog.write_text(ctext.replace(anchor, entry), encoding="utf-8")

print("closeout documentation aligned")
