#!/usr/bin/env python3
"""Read-only post-release coherence checks for live public-facing surfaces.

This validator protects a narrow class of drift discovered after the v1.1.0
publication: release/DOI identity, current report pointers, completed August
state, and the distinction between immediate weekly posture and broader
Phase 2 substate.

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
    versioning = read("VERSIONING.md")
    verification = read("VERIFICATION.md")
    observer = read("docs/OBSERVER_QUICKSTART.md")
    newcomer = read("docs/NEWCOMER_PATH.md")
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
