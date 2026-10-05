#!/usr/bin/env python3
"""Read-only post-release coherence checks for live public-facing surfaces.

This validator protects a narrow class of drift discovered after the v1.1.0
publication and subsequent observer-legibility audits: release/DOI identity,
current report pointers, weekly-versus-broader state distinctions, live
structured-count summaries, current validation-documentation roles, and
selected first-contact navigation/language boundaries.

Current week, prior closed week, and immediate weekly posture are derived from
the live weekly-report lifecycle rather than hard-coded into this validator.
That keeps the validator capable of detecting stale orientation surfaces after
a weekly rollover without requiring its own weekly constant update.

It does not edit files, query external services, or reinterpret scientific
outcomes.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VERSION = "1.1.0"
VERSION_DOI = "10.5281/zenodo.22759132"
ALL_VERSIONS_DOI = "10.5281/zenodo.20815611"
FROZEN_RELEASE_COMMIT = "92126e1cc882c3822d9e03b30b11cfc1d30b4fbb"
BROADER_SUBSTATE = "Consolidation / lock-in observation"

WEEK_RE = re.compile(r"^(\d{4})-W(\d{2})\.md$")
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(Active|Closed)\s*$", re.MULTILINE)
POSTURE_RE = re.compile(r"^\*\*Weekly posture:\*\*\s*(.+?)\s*$", re.MULTILINE)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8-sig")


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def current_weekly_state(errors: list[str]) -> tuple[str, str, str]:
    """Derive active/prior report IDs and the active weekly posture."""

    report_dir = ROOT / "reports"
    weekly: list[tuple[int, int, Path]] = []

    for path in report_dir.glob("2026-W*.md"):
        match = WEEK_RE.match(path.name)
        if match:
            weekly.append((int(match.group(1)), int(match.group(2)), path))

    weekly.sort()

    if len(weekly) < 2:
        errors.append("weekly lifecycle: fewer than two standardized weekly reports found")
        return "", "", ""

    active_path = weekly[-1][2]
    closed_path = weekly[-2][2]
    active_text = active_path.read_text(encoding="utf-8-sig")
    closed_text = closed_path.read_text(encoding="utf-8-sig")

    active_status = STATUS_RE.search(active_text)
    closed_status = STATUS_RE.search(closed_text)
    posture_match = POSTURE_RE.search(active_text)

    require(
        errors,
        bool(active_status and active_status.group(1) == "Active"),
        f"{active_path.as_posix()}: newest weekly report is not standardized Active",
    )
    require(
        errors,
        bool(closed_status and closed_status.group(1) == "Closed"),
        f"{closed_path.as_posix()}: immediately prior weekly report is not standardized Closed",
    )
    require(
        errors,
        posture_match is not None,
        f"{active_path.as_posix()}: active Weekly posture line missing",
    )

    return (
        active_path.stem,
        closed_path.stem,
        posture_match.group(1).strip() if posture_match else "",
    )


def csv_profile(
    relative_path: str,
    date_field: str,
    errors: list[str],
) -> tuple[int, str]:
    """Return CSV data-row count and latest represented ISO-date string."""

    path = ROOT / relative_path
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{relative_path}: unable to parse live CSV profile: {exc}")
        return 0, ""

    if not rows:
        errors.append(f"{relative_path}: no data rows available for live profile")
        return 0, ""

    if date_field not in rows[0]:
        errors.append(f"{relative_path}: required live-profile field {date_field!r} missing")
        return len(rows), ""

    dates = [row.get(date_field, "").strip() for row in rows if row.get(date_field, "").strip()]
    if not dates:
        errors.append(f"{relative_path}: no represented {date_field} values")
        return len(rows), ""

    return len(rows), max(dates)


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

    active_week, most_recent_closed, weekly_posture = current_weekly_state(errors)

    daily_rows, daily_end = csv_profile(
        "data/daily_biomarkers_v1.csv",
        "date",
        errors,
    )
    sleep_rows, sleep_end = csv_profile(
        "data/sleep_longitudinal_v1.csv",
        "date",
        errors,
    )
    training_rows, training_end = csv_profile(
        "data/training_blocks_v1.csv",
        "date",
        errors,
    )
    context_rows, context_end = csv_profile(
        "data/context_events_v1.csv",
        "end_date",
        errors,
    )

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
    require(errors, "## Level 6 — Post-Release Coherence Validation" in verification, "VERIFICATION.md: coherence-validation section missing")
    require(errors, "python tools/validate_weekly_rollover.py" in verification, "VERIFICATION.md: weekly-rollover-validator command missing")
    require(errors, "python tools/validate_coherence.py" in verification, "VERIFICATION.md: coherence-validator command missing")
    require(errors, f'doi: "{VERSION_DOI}"' in citation, "CITATION.cff: finalized version DOI drift")
    require(errors, str(codemeta.get("version", "")).strip() == VERSION, "CODEMETA.json: version drift")
    require(errors, str(codemeta.get("identifier", "")).strip() == f"https://doi.org/{VERSION_DOI}", "CODEMETA.json: version identifier drift")
    require(errors, str(codemeta.get("sameAs", "")).strip() == f"https://doi.org/{ALL_VERSIONS_DOI}", "CODEMETA.json: all-versions DOI drift")

    # Current report pointers are derived from the live report lifecycle.
    if active_week and most_recent_closed:
        exact_pointer_expectations = {
            "README.md": (
                readme,
                f"Active weekly window:\n{active_week}",
                f"Most recent closed window:\n{most_recent_closed}",
            ),
            "LATEST.md": (
                latest,
                f"- **Active window:** {active_week}",
                f"- **Prior window:** {most_recent_closed} closed",
            ),
            "INDEX.md": (
                index,
                f"Active weekly window:\n{active_week}",
                f"Most recent closed window:\n{most_recent_closed}",
            ),
        }
        for label, text, active_marker, closed_marker in exact_pointer_expectations.values():
            require(errors, active_marker in text, f"{label}: active-week pointer drift; expected {active_week}")
            require(
                errors,
                closed_marker in text,
                f"{label}: most-recent-closed pointer drift; expected {most_recent_closed}",
            )

        require(
            errors,
            f"reports/{active_week}.md" in latest,
            f"LATEST.md: active report pointer drift; expected reports/{active_week}.md",
        )
        require(
            errors,
            f"reports/{most_recent_closed}.md" in latest,
            f"LATEST.md: closed report pointer drift; expected reports/{most_recent_closed}.md",
        )
        require(
            errors,
            f"reports/{active_week}.md" in index,
            f"INDEX.md: active report pointer drift; expected reports/{active_week}.md",
        )
        require(
            errors,
            f"reports/{most_recent_closed}.md" in index,
            f"INDEX.md: closed report pointer drift; expected reports/{most_recent_closed}.md",
        )

        for label, text in (
            ("docs/OBSERVER_QUICKSTART.md", observer),
            ("docs/NEWCOMER_PATH.md", newcomer),
        ):
            require(
                errors,
                f"reports/{most_recent_closed}.md" in text,
                f"{label}: most recent closed report pointer drift; expected {most_recent_closed}",
            )

    # August completion language should not regress on live orientation surfaces.
    forbidden_current_phrases = {
        "docs/OBSERVER_QUICKSTART.md": ["pending snapshot evidence"],
        "docs/NEWCOMER_PATH.md": ["current open prediction", "still-pending TruDiagnostic"],
    }
    for label, phrases in forbidden_current_phrases.items():
        text = observer if "OBSERVER" in label else newcomer
        for phrase in phrases:
            require(errors, phrase not in text, f"{label}: stale current-state phrase remains: {phrase!r}")

    # Immediate weekly posture is derived from the active report and must agree
    # across every live surface that exposes a current posture. This closes the
    # START_HERE/CONCEPTS drift class found during the W39->W40 rollover audit.
    if weekly_posture:
        posture_expectations = {
            "README.md": (
                readme,
                f"| Weekly operating posture | **{weekly_posture}** |",
            ),
            "LATEST.md": (
                latest,
                f"- **Weekly operating posture:** {weekly_posture}",
            ),
            "INDEX.md": (
                index,
                f"Weekly operating posture:\n{weekly_posture}",
            ),
            "docs/START_HERE.md": (
                start_here,
                f"weekly operating posture\n{weekly_posture}",
            ),
            "docs/CONCEPTS.md": (
                concepts,
                f"Weekly operating posture:\n{weekly_posture}",
            ),
        }
        for label, (text, marker) in posture_expectations.items():
            require(
                errors,
                marker in text,
                f"{label}: current weekly posture drift; expected {weekly_posture!r}",
            )

    require(errors, f"**Broader Phase 2 substate:** {BROADER_SUBSTATE}" in latest, "LATEST.md: broader Phase 2 substate missing or drifted")
    require(errors, BROADER_SUBSTATE in phase_map, "PHASE_MAP.md: canonical broader Phase 2 substate drift")
    require(errors, "weekly operating posture" in observer.lower(), "Observer quickstart: weekly-vs-broader state distinction missing")
    require(errors, "weekly operating posture" in newcomer.lower(), "Newcomer path: weekly-vs-broader state distinction missing")

    # README and LATEST duplicate a small amount of volatile structured-coverage
    # state for usability. Protect those summaries against silent lag by deriving
    # counts/endpoints directly from the committed CSVs.
    if all((daily_end, sleep_end, training_end, context_end)):
        readme_coverage_expectations = (
            (
                f"| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | "
                f"one row per represented day | {daily_rows} continuous rows through {daily_end} |"
            ),
            (
                f"| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | "
                f"one governed wake-date row | {sleep_rows} continuous rows through {sleep_end} |"
            ),
            (
                f"| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | "
                f"one row per completed session/block | {training_rows} rows through {training_end} |"
            ),
            (
                f"| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | "
                f"one bounded context event | {context_rows} rows through {context_end} |"
            ),
        )
        for marker in readme_coverage_expectations:
            require(errors, marker in readme, f"README.md: live structured-coverage summary drift: {marker!r}")

        latest_coverage_expectations = (
            f"- public daily biomarkers and canonical sleep contain {daily_rows} continuous rows through {daily_end}",
            f"- public training contains {training_rows} completed-session rows through {training_end}",
            f"- public context index contains {context_rows} bounded events through {context_end}",
        )
        for marker in latest_coverage_expectations:
            require(errors, marker in latest, f"LATEST.md: live structured-coverage summary drift: {marker!r}")

        require(
            errors,
            daily_rows == sleep_rows and daily_end == sleep_end,
            (
                "live structured coverage: daily/sleep alignment drift; "
                f"daily={daily_rows}@{daily_end}, sleep={sleep_rows}@{sleep_end}"
            ),
        )

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
    require(errors, "tools/validate_weekly_rollover.py" in tools_readme, "tools/README.md: weekly rollover validator inventory missing")
    require(errors, "tools/validate_coherence.py" in tools_readme, "tools/README.md: coherence validator inventory missing")
    require(errors, "tools/validate_weekly_rollover.py" in observer, "Observer quickstart: weekly rollover validator missing")
    require(errors, "tools/validate_weekly_rollover.py" in for_observers, "FOR_OBSERVERS: weekly rollover validator missing")
    require(errors, "tools/validate_weekly_rollover.py" in index, "INDEX.md: weekly rollover validator missing")
    require(errors, "latest weekly rollover validator active" in latest, "LATEST.md: weekly rollover validator state missing")

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
    print(f"active_week={active_week}")
    print(f"most_recent_closed={most_recent_closed}")
    print(f"weekly_posture={weekly_posture}")
    print(f"broader_substate={BROADER_SUBSTATE}")
    print(f"daily_profile={daily_rows}@{daily_end}")
    print(f"sleep_profile={sleep_rows}@{sleep_end}")
    print(f"training_profile={training_rows}@{training_end}")
    print(f"context_profile={context_rows}@{context_end}")
    print("observer_legibility=protected")
    print("live_state_alignment=protected")
    print("live_coverage_summaries=protected")
    print("validation_doc_roles=protected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
