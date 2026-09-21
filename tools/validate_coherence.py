#!/usr/bin/env python3
"""Read-only post-release coherence checks for live public-facing surfaces.

This validator protects a narrow class of drift discovered after the v1.1.0
publication and subsequent observer-legibility audit: release/DOI identity,
current report pointers, completed August state, weekly-versus-broader state
distinctions, current validation-documentation roles, and selected
first-contact navigation/language boundaries.

It does not edit files, query external services, or reinterpret scientific
outcomes.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VERSION = "1.1.0"
VERSION_DOI = "10.5281/zenodo.22759132"
ALL_VERSIONS_DOI = "10.5281/zenodo.20815611"
FROZEN_RELEASE_COMMIT = "92126e1cc882c3822d9e03b30b11cfc1d30b4fbb"
ACTIVE_WEEK = "2026-W38"
MOST_RECENT_CLOSED = "2026-W37"
WEEKLY_POSTURE = "Consolidation / reserve-replication observation"
BROADER_SUBSTATE = "Consolidation / lock-in observation"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8-sig")


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    readme = read("README.md")
    latest = read("LATEST.md")
    index = read("INDEX.md")
    start_here = read("docs/START_HERE.md")
    observer = read("docs/OBSERVER_QUICKSTART.md")
    newcomer = read("docs/NEWCOMER_PATH.md")
    for_observers = read("docs/FOR_OBSERVERS.md")
    concepts = read("docs/CONCEPTS.md")
    dataset_overview = read("DATASET_OVERVIEW.md")
    coverage = read("data/DATA_COVERAGE.md")
    methodology_readme = read("methodology/README.md")
    tools_readme = read("tools/README.md")
    versioning = read("VERSIONING.md")
    verification = read("VERIFICATION.md")
    phase_map = read("PHASE_MAP.md")
    citation = read("CITATION.cff")
    codemeta = json.loads(read("CODEMETA.json"))

    # Published release identity.
    for label, text in (
        ("README.md", readme),
        ("LATEST.md", latest),
        ("VERSIONING.md", versioning),
        ("VERIFICATION.md", verification),
    ):
        require(errors, f"v{VERSION}" in text, f"{label}: current release v{VERSION} missing")
        require(errors, VERSION_DOI in text, f"{label}: version DOI {VERSION_DOI} missing")
        require(errors, ALL_VERSIONS_DOI in text, f"{label}: all-versions DOI {ALL_VERSIONS_DOI} missing")

    require(errors, "The current published release is:" in versioning, "VERSIONING.md: current-release declaration missing")
    require(errors, FROZEN_RELEASE_COMMIT in versioning, "VERSIONING.md: frozen v1.1.0 commit missing")
    require(errors, "## Level 4 — Post-Release Coherence Validation" in verification, "VERIFICATION.md: coherence-validation section missing")
    require(errors, "python tools/validate_coherence.py" in verification, "VERIFICATION.md: coherence-validator command missing")
    require(errors, f'doi: "{VERSION_DOI}"' in citation, "CITATION.cff: finalized version DOI drift")
    require(errors, str(codemeta.get("version", "")).strip() == VERSION, "CODEMETA.json: version drift")
    require(errors, str(codemeta.get("identifier", "")).strip() == f"https://doi.org/{VERSION_DOI}", "CODEMETA.json: version identifier drift")
    require(errors, str(codemeta.get("sameAs", "")).strip() == f"https://doi.org/{ALL_VERSIONS_DOI}", "CODEMETA.json: all-versions DOI drift")

    # Current report pointers.
    for label, text in (("README.md", readme), ("LATEST.md", latest)):
        require(errors, ACTIVE_WEEK in text, f"{label}: active week {ACTIVE_WEEK} missing")
        require(errors, MOST_RECENT_CLOSED in text, f"{label}: most recent closed week {MOST_RECENT_CLOSED} missing")

    for label, text in (("docs/OBSERVER_QUICKSTART.md", observer), ("docs/NEWCOMER_PATH.md", newcomer)):
        require(errors, f"reports/{MOST_RECENT_CLOSED}.md" in text, f"{label}: most recent closed report pointer drift")
        require(errors, "reports/2026-W36.md" not in text, f"{label}: stale W36 closed-report pointer remains")

    # August completion language should not regress on live orientation surfaces.
    forbidden_current_phrases = {
        "docs/OBSERVER_QUICKSTART.md": ["pending snapshot evidence"],
        "docs/NEWCOMER_PATH.md": ["current open prediction", "still-pending TruDiagnostic"],
    }
    for label, phrases in forbidden_current_phrases.items():
        text = observer if "OBSERVER" in label else newcomer
        for phrase in phrases:
            require(errors, phrase not in text, f"{label}: stale current-state phrase remains: {phrase!r}")

    # Immediate weekly posture and broader canonical substate must be explicit.
    require(errors, f"**Weekly operating posture:** {WEEKLY_POSTURE}" in latest, "LATEST.md: weekly operating posture missing or drifted")
    require(errors, f"**Broader Phase 2 substate:** {BROADER_SUBSTATE}" in latest, "LATEST.md: broader Phase 2 substate missing or drifted")
    require(errors, BROADER_SUBSTATE in phase_map, "PHASE_MAP.md: canonical broader Phase 2 substate drift")
    require(errors, "weekly operating posture" in observer.lower(), "Observer quickstart: weekly-vs-broader state distinction missing")
    require(errors, "weekly operating posture" in newcomer.lower(), "Newcomer path: weekly-vs-broader state distinction missing")

    # Validation-documentation inventory should remain centralized rather than
    # drifting back to stale two-validator descriptions on current-facing docs.
    current_validation_docs = {
        "docs/START_HERE.md": start_here,
        "DATASET_OVERVIEW.md": dataset_overview,
        "docs/FOR_OBSERVERS.md": for_observers,
        "data/DATA_COVERAGE.md": coverage,
        "methodology/README.md": methodology_readme,
    }
    for label, text in current_validation_docs.items():
        lowered = text.lower()
        require(errors, "runs both" not in lowered, f"{label}: stale two-validator 'runs both' language returned")
        require(errors, "two read-only validators" not in lowered, f"{label}: stale two-validator inventory language returned")
        require(errors, "tools/readme.md" in lowered, f"{label}: authoritative tools/README.md validation reference missing")
        require(errors, "verification.md" in lowered, f"{label}: authoritative VERIFICATION.md reference missing")

    # First-contact surfaces have distinct jobs. Protect the role separation
    # discovered during the post-weekly-update cognitive-density audit.
    require(errors, "These are alternatives, not a required reading sequence." in readme, "README.md: task-based first-contact framing drift")
    require(errors, "you do not need to read the README again." in start_here, "START_HERE: circular README reread instruction returned")
    require(errors, "not intended to be read sequentially as mandatory prerequisites." in start_here, "START_HERE: mandatory-chain language drift")
    require(errors, "This document is the audit route." in observer, "Observer quickstart: short-audit route ownership drift")
    require(errors, "README / START_HERE" not in observer, "Observer quickstart: stale chained front-door audit sequence returned")
    require(errors, "optional extended learning path" in newcomer, "Newcomer path: optional-curriculum role drift")
    require(errors, "skeptical-review reference and checklist" in for_observers, "FOR_OBSERVERS: reference/checklist role drift")
    require(errors, "## Recommended Review Path" not in for_observers, "FOR_OBSERVERS: competing linear review path returned")
    require(errors, "Choose by task rather than reading every orientation document in sequence:" in index, "INDEX.md: task-based first-contact framing drift")
    require(errors, "orientation documents are alternatives with distinct jobs, not a mandatory chain." in index, "INDEX.md: mandatory orientation-chain drift")

    # Live-facing state surfaces should lead with plain language while precise
    # session-level vocabulary remains available one layer deeper.
    for label, text in (("README.md", readme), ("LATEST.md", latest)):
        require(errors, "**Plain-language summary:**" in text, f"{label}: plain-language current-state bridge missing")
        lowered = text.lower()
        for jargon in ("low-salience", "trait-like", "trait-level"):
            require(errors, jargon not in lowered, f"{label}: stacked session-level jargon returned to first-contact surface: {jargon}")

    required_concepts = (
        "## Weekly Operating Posture",
        "## Data-Quality Record (DQ)",
        "## Capacity Versus Exposure",
        "## Reserve (Capacity)",
        "## Ambient Execution",
        "## Trait-Like Execution",
        "## Trait-Level Expression",
    )
    for heading in required_concepts:
        require(errors, heading in concepts, f"docs/CONCEPTS.md: required terminology bridge missing: {heading}")

    require(errors, "## How The Current State Labels Fit Together" in start_here, "START_HERE: state-label hierarchy bridge missing")
    require(errors, "tools/validate_coherence.py" in tools_readme, "tools/README.md: coherence validator inventory missing")

    if errors:
        print("POST-RELEASE COHERENCE: FAIL")
        for item in errors:
            print(f"ERROR: {item}")
        return 1

    print("POST-RELEASE COHERENCE: PASS")
    print(f"release=v{VERSION}")
    print(f"version_doi={VERSION_DOI}")
    print(f"all_versions_doi={ALL_VERSIONS_DOI}")
    print(f"frozen_release_commit={FROZEN_RELEASE_COMMIT}")
    print(f"active_week={ACTIVE_WEEK}")
    print(f"most_recent_closed={MOST_RECENT_CLOSED}")
    print(f"weekly_posture={WEEKLY_POSTURE}")
    print(f"broader_substate={BROADER_SUBSTATE}")
    print("observer_legibility=protected")
    print("validation_doc_roles=protected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
