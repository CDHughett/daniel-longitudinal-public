#!/usr/bin/env python3
"""Read-only validation for the Daniel Longitudinal Study repository.

The validator reports mechanical failures separately from governed warnings.
It never edits repository files and exits nonzero only when true errors exist.

Usage:
    python tools/validate_repository.py
    python tools/validate_repository.py /path/to/repository
    python tools/validate_repository.py /path/to/repository.zip
    python tools/validate_repository.py --json
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import tempfile
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path, PurePosixPath
from typing import Sequence
from urllib.parse import unquote, urlsplit


EXPECTED_RINGCONN = {
    "ringconn-sleep-export.csv": {
        "bytes": 38_703,
        "sha256": (
            "2336f95ffdf28eb8cb6ddc0931a1724c"
            "028c2ed6e4bbe7beb82e87e41ab2523c"
        ),
        "rows": 366,
        "header": [
            "Start Time",
            "End Time",
            "Falling Asleep Time",
            "Wake-up time",
            "Sleep Time Ratio(%)",
            "Time Asleep(min)",
            "Sleep Stages - Awake(min)",
            "Sleep Stages - REM(min)",
            "Sleep Stages - Light Sleep(min)",
            "Sleep Stages - Deep Sleep(min)",
        ],
    },
    "ringconn-activity-export.csv": {
        "bytes": 8_171,
        "sha256": (
            "6431d57a58e4c0aecda5be94867bc9a"
            "638daa27759f21605a3873905893c248c"
        ),
        "rows": 360,
        "header": [
            "Date",
            "Steps",
            "Calories(kcal)",
        ],
    },
    "ringconn-vital-signs-export.csv": {
        "bytes": 16_059,
        "sha256": (
            "2e102745289d78a039b9657c4cc72032"
            "2a2b22a29098e860dd7d69e14348d7e9"
        ),
        "rows": 360,
        "header": [
            "Date",
            "Avg. Heart Rate(bpm)",
            "Min. Heart Rate(bpm)",
            "Max. Heart Rate(bpm)",
            "Avg. Spo2(%)",
            "Min. Spo2(%)",
            "Max. Spo2(%)",
            "Avg. HRV(ms)",
            "Min. HRV(ms)",
            "Max. HRV(ms)",
        ],
    },
}

RINGCONN_DIRECTORY = Path(
    "data/source_exports/ringconn/2026-07-21"
)

CHECKSUM_RE = re.compile(
    r"^([0-9a-fA-F]{64})[ \t]+\*?(.+?)\s*$"
)

MARKDOWN_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(([^)]+)\)"
)

HEADING_RE = re.compile(
    r"^(#{1,6})\s+(.+?)\s*#*\s*$"
)

WEEK_RE = re.compile(
    r"^2026-W(\d{2})\.md$"
)

FENCE_RE = re.compile(
    r"^\s*(`{3,}|~{3,})"
)

WINDOWS_DRIVE_RE = re.compile(
    r"^[A-Za-z]:[\\/]"
)


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    message: str


class Report:
    def __init__(self) -> None:
        self.findings: list[Finding] = []
        self.metrics: dict[str, object] = {}

    def error(self, check: str, message: str) -> None:
        self.findings.append(
            Finding("ERROR", check, message)
        )

    def warning(self, check: str, message: str) -> None:
        self.findings.append(
            Finding("WARN", check, message)
        )

    def pass_(self, check: str, message: str) -> None:
        self.findings.append(
            Finding("PASS", check, message)
        )

    @property
    def errors(self) -> list[Finding]:
        return [
            item
            for item in self.findings
            if item.level == "ERROR"
        ]

    @property
    def warnings(self) -> list[Finding]:
        return [
            item
            for item in self.findings
            if item.level == "WARN"
        ]

    @property
    def passes(self) -> list[Finding]:
        return [
            item
            for item in self.findings
            if item.level == "PASS"
        ]


class Validator:
    def __init__(
        self,
        root: Path,
        report: Report,
    ) -> None:
        self.root = root.resolve()
        self.report = report

    def run(self) -> None:
        self.check_required_structure()
        self.check_markdown()
        self.check_csv_files()
        self.check_checksum_manifests()
        self.check_canonical_sleep()
        self.check_weekly_reports()
        self.check_model_error_register()
        self.check_release_metadata()
        self.check_ringconn_source_exports()

    def relative(self, path: Path) -> str:
        try:
            return path.relative_to(
                self.root
            ).as_posix()
        except ValueError:
            return str(path)

    def check_required_structure(self) -> None:
        check = "repository structure"

        required = [
            "README.md",
            "CHANGELOG.md",
            "CODEMETA.json",
            "CITATION.cff",
            "PHASE_MAP.md",
            "STATE_TRANSITIONS.md",
            "data/sleep_longitudinal_v1.csv",
            "data/model_error/model_error_gap_v1.csv",
            "reports",
            "snapshots",
        ]

        missing = [
            item
            for item in required
            if not (self.root / item).exists()
        ]

        if missing:
            for item in missing:
                self.report.error(
                    check,
                    f"Missing required path: {item}",
                )
            return

        files = [
            path
            for path in self.root.rglob("*")
            if path.is_file()
        ]

        zero_byte = [
            self.relative(path)
            for path in files
            if path.stat().st_size == 0
        ]

        if zero_byte:
            for item in zero_byte:
                self.report.error(
                    check,
                    f"Zero-byte file: {item}",
                )
        else:
            self.report.pass_(
                check,
                (
                    f"Required paths present; "
                    f"{len(files)} files and no zero-byte files"
                ),
            )

        self.report.metrics["repository_files"] = len(files)

    def check_markdown(self) -> None:
        check = "Markdown"

        markdown_files = sorted(
            self.root.rglob("*.md")
        )

        missing_targets: list[str] = []
        missing_anchors: list[str] = []
        unsafe_targets: list[str] = []
        unbalanced_fences: list[str] = []
        reference_count = 0

        anchor_cache: dict[Path, set[str]] = {}

        for path in markdown_files:
            text = path.read_text(
                encoding="utf-8-sig",
                errors="replace",
            )

            visible_text, fence_error = strip_fenced_code(
                text
            )

            if fence_error:
                unbalanced_fences.append(
                    self.relative(path)
                )

            visible_text = re.sub(
                r"`[^`\n]*`",
                "",
                visible_text,
            )

            for match in MARKDOWN_LINK_RE.finditer(
                visible_text
            ):
                raw_destination = (
                    normalize_markdown_destination(
                        match.group(1)
                    )
                )

                if (
                    not raw_destination
                    or is_external_destination(
                        raw_destination
                    )
                ):
                    continue

                reference_count += 1

                split = urlsplit(raw_destination)
                decoded_path = unquote(split.path)
                fragment = unquote(split.fragment)

                if WINDOWS_DRIVE_RE.match(decoded_path):
                    unsafe_targets.append(
                        (
                            f"{self.relative(path)} "
                            f"-> {raw_destination}"
                        )
                    )
                    continue

                if decoded_path.startswith("/"):
                    target = (
                        self.root
                        / decoded_path.lstrip("/")
                    ).resolve()
                elif decoded_path:
                    target = (
                        path.parent
                        / decoded_path
                    ).resolve()
                else:
                    target = path.resolve()

                if not path_is_within(
                    target,
                    self.root,
                ):
                    unsafe_targets.append(
                        (
                            f"{self.relative(path)} "
                            f"-> {raw_destination}"
                        )
                    )
                    continue

                if not target.exists():
                    missing_targets.append(
                        (
                            f"{self.relative(path)} "
                            f"-> {raw_destination}"
                        )
                    )
                    continue

                if (
                    fragment
                    and target.is_file()
                    and target.suffix.lower() == ".md"
                ):
                    anchors = anchor_cache.setdefault(
                        target,
                        github_markdown_anchors(target),
                    )

                    if fragment.lower() not in anchors:
                        missing_anchors.append(
                            (
                                f"{self.relative(path)} "
                                f"-> {self.relative(target)}"
                                f"#{fragment}"
                            )
                        )

        for item in unsafe_targets:
            self.report.error(
                check,
                (
                    "Reference escapes repository root: "
                    f"{item}"
                ),
            )

        for item in missing_targets:
            self.report.error(
                check,
                f"Missing relative target: {item}",
            )

        for item in missing_anchors:
            self.report.error(
                check,
                f"Missing internal anchor: {item}",
            )

        for item in unbalanced_fences:
            self.report.error(
                check,
                (
                    "Unbalanced fenced-code block: "
                    f"{item}"
                ),
            )

        if not any(
            (
                unsafe_targets,
                missing_targets,
                missing_anchors,
                unbalanced_fences,
            )
        ):
            self.report.pass_(
                check,
                (
                    f"{len(markdown_files)} files; "
                    f"{reference_count} internal references; "
                    "targets, anchors, and fences pass"
                ),
            )

        self.report.metrics[
            "markdown_files"
        ] = len(markdown_files)

        self.report.metrics[
            "markdown_internal_references"
        ] = reference_count

    def check_csv_files(self) -> None:
        check = "CSV structure"

        csv_files = sorted(
            self.root.rglob("*.csv")
        )

        failures = 0

        for path in csv_files:
            try:
                header, rows = read_csv(path)
            except (
                UnicodeError,
                csv.Error,
                OSError,
            ) as exc:
                failures += 1
                self.report.error(
                    check,
                    (
                        f"Cannot parse "
                        f"{self.relative(path)}: {exc}"
                    ),
                )
                continue

            if not header:
                failures += 1
                self.report.error(
                    check,
                    (
                        "Missing header: "
                        f"{self.relative(path)}"
                    ),
                )
                continue

            duplicates = sorted(
                name
                for name, count
                in Counter(header).items()
                if count > 1
            )

            if duplicates:
                failures += 1
                self.report.error(
                    check,
                    (
                        "Duplicate header(s) in "
                        f"{self.relative(path)}: "
                        f"{', '.join(duplicates)}"
                    ),
                )

            expected_width = len(header)

            bad_rows = [
                index + 2
                for index, row in enumerate(rows)
                if len(row) != expected_width
            ]

            if bad_rows:
                failures += 1
                preview = ", ".join(
                    map(str, bad_rows[:10])
                )
                suffix = (
                    "..."
                    if len(bad_rows) > 10
                    else ""
                )

                self.report.error(
                    check,
                    (
                        "Row-width mismatch in "
                        f"{self.relative(path)} "
                        f"at line(s) {preview}{suffix}"
                    ),
                )

        if failures == 0:
            self.report.pass_(
                check,
                (
                    f"All {len(csv_files)} CSV files "
                    "parsed with consistent row widths"
                ),
            )

        self.report.metrics[
            "csv_files"
        ] = len(csv_files)

    def check_checksum_manifests(self) -> None:
        check = "checksums"

        manifests = sorted(
            self.root.rglob("checksums.txt")
        )

        entries = 0
        failures = 0

        for manifest in manifests:
            lines = manifest.read_text(
                encoding="utf-8-sig",
                errors="replace",
            ).splitlines()

            for line_number, raw_line in enumerate(
                lines,
                start=1,
            ):
                line = raw_line.strip()

                if not line or line.startswith("#"):
                    continue

                match = CHECKSUM_RE.match(line)

                if not match:
                    failures += 1
                    self.report.error(
                        check,
                        (
                            "Malformed checksum entry in "
                            f"{self.relative(manifest)}:"
                            f"{line_number}"
                        ),
                    )
                    continue

                entries += 1

                expected, filename = match.groups()

                target = (
                    manifest.parent
                    / filename
                ).resolve()

                if not path_is_within(
                    target,
                    self.root,
                ):
                    failures += 1
                    self.report.error(
                        check,
                        (
                            "Checksum target escapes "
                            "repository: "
                            f"{self.relative(manifest)} "
                            f"-> {filename}"
                        ),
                    )
                    continue

                if not target.is_file():
                    failures += 1
                    self.report.error(
                        check,
                        (
                            "Missing checksum target: "
                            f"{self.relative(manifest)} "
                            f"-> {filename}"
                        ),
                    )
                    continue

                actual = sha256_file(target)

                if actual.lower() != expected.lower():
                    failures += 1
                    self.report.error(
                        check,
                        (
                            "SHA-256 mismatch: "
                            f"{self.relative(target)} "
                            f"expected {expected.lower()} "
                            f"got {actual}"
                        ),
                    )

        if failures == 0:
            self.report.pass_(
                check,
                (
                    f"{entries} artifact entries across "
                    f"{len(manifests)} manifests pass"
                ),
            )

        self.report.metrics[
            "checksum_manifests"
        ] = len(manifests)

        self.report.metrics[
            "checksum_entries"
        ] = entries

    def check_canonical_sleep(self) -> None:
        check = "canonical sleep"

        path = (
            self.root
            / "data/sleep_longitudinal_v1.csv"
        )

        if not path.is_file():
            self.report.error(
                check,
                (
                    "Missing "
                    "data/sleep_longitudinal_v1.csv"
                ),
            )
            return

        header, raw_rows = read_csv(path)

        rows = [
            dict(
                zip(
                    header,
                    row,
                    strict=False,
                )
            )
            for row in raw_rows
        ]

        date_field = find_column(
            header,
            ["date"],
        )

        if date_field is None:
            self.report.error(
                check,
                "No date column found",
            )
            return

        parsed: list[
            tuple[date, dict[str, str]]
        ] = []

        for line_number, row in enumerate(
            rows,
            start=2,
        ):
            value = row.get(
                date_field,
                "",
            ).strip()

            try:
                parsed.append(
                    (
                        date.fromisoformat(value),
                        row,
                    )
                )
            except ValueError:
                self.report.error(
                    check,
                    (
                        f"Invalid ISO date at line "
                        f"{line_number}: {value!r}"
                    ),
                )

        dates = [
            item[0]
            for item in parsed
        ]

        duplicates = sorted(
            day.isoformat()
            for day, count
            in Counter(dates).items()
            if count > 1
        )

        for item in duplicates:
            self.report.error(
                check,
                f"Duplicate canonical date: {item}",
            )

        missing: list[str] = []

        if dates:
            observed = set(dates)
            cursor = min(dates)

            while cursor <= max(dates):
                if cursor not in observed:
                    missing.append(
                        cursor.isoformat()
                    )
                cursor += timedelta(days=1)

        if missing:
            self.report.error(
                check,
                (
                    "Missing date(s) inside represented "
                    f"interval: {', '.join(missing)}"
                ),
            )

        total_col = find_column(
            header,
            ["total_sleep_min"],
        )

        stage_cols = [
            find_column(
                header,
                ["deep_sleep_min"],
            ),
            find_column(
                header,
                ["light_sleep_min"],
            ),
            find_column(
                header,
                ["rem_sleep_min"],
            ),
        ]

        stage_differences: list[
            tuple[str, int]
        ] = []

        if total_col and all(stage_cols):
            for day, row in parsed:
                values = [
                    parse_int(
                        row.get(
                            name or "",
                            "",
                        )
                    )
                    for name in stage_cols
                ]

                total = parse_int(
                    row.get(
                        total_col,
                        "",
                    )
                )

                if (
                    total is None
                    or any(
                        value is None
                        for value in values
                    )
                ):
                    continue

                difference = total - sum(
                    value
                    for value in values
                    if value is not None
                )

                if difference != 0:
                    stage_differences.append(
                        (
                            day.isoformat(),
                            difference,
                        )
                    )

        awake_col = find_column(
            header,
            ["awake_min"],
        )

        awakenings_col = find_column(
            header,
            ["awakenings_count"],
        )

        duplicated_interval: list[str] = []

        if awake_col and awakenings_col:
            start = date(2026, 5, 18)
            end = date(2026, 5, 31)

            for day, row in parsed:
                if start <= day <= end:
                    awake = row.get(
                        awake_col,
                        "",
                    ).strip()

                    awakenings = row.get(
                        awakenings_col,
                        "",
                    ).strip()

                    if (
                        awake
                        and awake == awakenings
                    ):
                        duplicated_interval.append(
                            day.isoformat()
                        )

        if stage_differences:
            details = ", ".join(
                (
                    f"{day}: "
                    f"{difference:+d} min"
                )
                for day, difference
                in stage_differences
            )

            self.report.warning(
                check,
                (
                    "Governed sleep-stage "
                    f"differences remain: {details}"
                ),
            )

        if duplicated_interval:
            self.report.warning(
                check,
                (
                    "DQ-001 awake/awakening "
                    "duplication remains on "
                    f"{len(duplicated_interval)} dates"
                ),
            )

        if not duplicates and not missing and dates:
            self.report.pass_(
                check,
                (
                    f"{len(dates)} continuous rows "
                    f"from {min(dates).isoformat()} "
                    f"through {max(dates).isoformat()}"
                ),
            )

        self.report.metrics[
            "canonical_sleep_rows"
        ] = len(dates)

        if dates:
            self.report.metrics[
                "canonical_sleep_start"
            ] = min(dates).isoformat()

            self.report.metrics[
                "canonical_sleep_end"
            ] = max(dates).isoformat()

    def check_weekly_reports(self) -> None:
        check = "weekly reports"

        report_dir = self.root / "reports"

        weekly = sorted(
            (
                path
                for path
                in report_dir.glob("2026-W*.md")
                if WEEK_RE.match(path.name)
            ),
            key=lambda path: int(
                WEEK_RE.match(
                    path.name
                ).group(1)
            ),
        )

        numbers = [
            int(
                WEEK_RE.match(
                    path.name
                ).group(1)
            )
            for path in weekly
        ]

        missing: list[int] = []

        if numbers:
            missing = [
                number
                for number
                in range(
                    min(numbers),
                    max(numbers) + 1,
                )
                if number not in numbers
            ]

        if missing:
            self.report.error(
                check,
                (
                    "Missing weekly report(s): "
                    + ", ".join(
                        f"W{x:02d}"
                        for x in missing
                    )
                ),
            )

        active: list[str] = []

        for path in weekly:
            text = path.read_text(
                encoding="utf-8-sig",
                errors="replace",
            )

            if re.search(
                (
                    r"^\*\*Status:\*\*"
                    r"\s*Active\s*$"
                ),
                text,
                flags=(
                    re.MULTILINE
                    | re.IGNORECASE
                ),
            ):
                active.append(path.name)

        if len(active) > 1:
            self.report.error(
                check,
                (
                    "Multiple active weekly reports: "
                    f"{', '.join(active)}"
                ),
            )
        elif len(active) == 0:
            self.report.warning(
                check,
                (
                    "No weekly report is explicitly "
                    "marked Active"
                ),
            )

        if not missing and weekly:
            active_text = (
                active[0]
                if active
                else "none"
            )

            self.report.pass_(
                check,
                (
                    f"{len(weekly)} reports continuous "
                    f"from W{min(numbers):02d} through "
                    f"W{max(numbers):02d}; "
                    f"active={active_text}"
                ),
            )

        self.report.metrics[
            "weekly_reports"
        ] = len(weekly)

        self.report.metrics[
            "active_weekly_reports"
        ] = active

    def check_model_error_register(self) -> None:
        check = "model error"

        path = (
            self.root
            / "data/model_error/"
            "model_error_gap_v1.csv"
        )

        if not path.is_file():
            self.report.error(
                check,
                (
                    "Missing primary model-error "
                    "register"
                ),
            )
            return

        header, raw_rows = read_csv(path)

        rows = [
            dict(
                zip(
                    header,
                    row,
                    strict=False,
                )
            )
            for row in raw_rows
        ]

        id_col = find_column(
            header,
            [
                "record_id",
                "id",
            ],
        )

        status_col = find_column(
            header,
            ["status"],
        )

        prediction_col = find_column(
            header,
            [
                "prediction_value",
                "prediction",
            ],
        )

        if id_col is None or status_col is None:
            self.report.error(
                check,
                (
                    "Required record_id or status "
                    "column missing"
                ),
            )
            return

        ids: list[int] = []
        by_id: dict[
            int,
            dict[str, str],
        ] = {}

        for line_number, row in enumerate(
            rows,
            start=2,
        ):
            raw_id = row.get(
                id_col,
                "",
            ).strip()

            try:
                record_id = int(raw_id)
            except ValueError:
                self.report.error(
                    check,
                    (
                        f"Invalid record ID at line "
                        f"{line_number}: {raw_id!r}"
                    ),
                )
                continue

            ids.append(record_id)
            by_id[record_id] = row

        duplicates = sorted(
            item
            for item, count
            in Counter(ids).items()
            if count > 1
        )

        for item in duplicates:
            self.report.error(
                check,
                (
                    "Duplicate record ID: "
                    f"{item:03d}"
                ),
            )

        missing: list[int] = []

        if ids:
            missing = [
                item
                for item
                in range(
                    min(ids),
                    max(ids) + 1,
                )
                if item not in ids
            ]

        if missing:
            self.report.error(
                check,
                (
                    "Missing record ID(s): "
                    + ", ".join(
                        f"{item:03d}"
                        for item in missing
                    )
                ),
            )

        protected_fields = [
            name
            for name in [
                find_column(
                    header,
                    ["actual_value"],
                ),
                find_column(
                    header,
                    ["error_absolute"],
                ),
                find_column(
                    header,
                    ["error_direction"],
                ),
                find_column(
                    header,
                    ["error_pct"],
                ),
            ]
            if name is not None
        ]

        for record_id in range(41, 45):
            row = by_id.get(record_id)

            if row is None:
                self.report.error(
                    check,
                    (
                        "Protected open record "
                        f"missing: {record_id:03d}"
                    ),
                )
                continue

            status = row.get(
                status_col,
                "",
            ).strip().lower()

            if status != "open":
                self.report.error(
                    check,
                    (
                        f"Record {record_id:03d} "
                        "must remain open"
                    ),
                )

            if (
                prediction_col
                and not row.get(
                    prediction_col,
                    "",
                ).strip()
            ):
                self.report.error(
                    check,
                    (
                        f"Record {record_id:03d} "
                        "prediction is blank"
                    ),
                )

            for field in protected_fields:
                if row.get(
                    field,
                    "",
                ).strip():
                    self.report.error(
                        check,
                        (
                            f"Record {record_id:03d} "
                            "protected field must "
                            f"remain blank: {field}"
                        ),
                    )

        if (
            not duplicates
            and not missing
            and ids
        ):
            self.report.pass_(
                check,
                (
                    f"{len(ids)} records continuous "
                    f"from {min(ids):03d} through "
                    f"{max(ids):03d}; "
                    "041-044 remain open and unscored"
                ),
            )

        self.report.metrics[
            "model_error_records"
        ] = len(ids)

    def check_release_metadata(self) -> None:
        check = "release metadata"

        codemeta_path = (
            self.root
            / "CODEMETA.json"
        )

        citation_path = (
            self.root
            / "CITATION.cff"
        )

        try:
            codemeta = json.loads(
                codemeta_path.read_text(
                    encoding="utf-8-sig",
                )
            )
        except (
            OSError,
            json.JSONDecodeError,
        ) as exc:
            self.report.error(
                check,
                (
                    "Cannot parse CODEMETA.json: "
                    f"{exc}"
                ),
            )
            return

        citation_text = citation_path.read_text(
            encoding="utf-8-sig",
            errors="replace",
        )

        cff_version = cff_scalar(
            citation_text,
            "version",
        )

        cff_date = cff_scalar(
            citation_text,
            "date-released",
        )

        cff_doi = cff_scalar(
            citation_text,
            "doi",
        )

        code_version = str(
            codemeta.get(
                "version",
                "",
            )
        ).strip()

        code_date = str(
            codemeta.get(
                "dateModified",
                "",
            )
        ).strip()

        if not cff_version:
            self.report.error(
                check,
                "CITATION.cff version missing",
            )
        elif cff_version != code_version:
            self.report.error(
                check,
                (
                    "Version mismatch: "
                    f"CODEMETA.json={code_version!r}, "
                    f"CITATION.cff={cff_version!r}"
                ),
            )

        if not cff_date:
            self.report.error(
                check,
                (
                    "CITATION.cff "
                    "date-released missing"
                ),
            )
        elif cff_date != code_date:
            self.report.error(
                check,
                (
                    "Release-date mismatch: "
                    f"CODEMETA.json={code_date!r}, "
                    f"CITATION.cff={cff_date!r}"
                ),
            )

        expected_doi = (
            "10.5281/zenodo.20815612"
        )

        if cff_doi != expected_doi:
            self.report.error(
                check,
                (
                    "Unexpected DOI in "
                    f"CITATION.cff: {cff_doi!r}"
                ),
            )

        if (
            cff_version == code_version
            and cff_date == code_date
            and cff_doi == expected_doi
        ):
            self.report.pass_(
                check,
                (
                    f"Version {code_version}, "
                    f"date {code_date}, "
                    f"DOI {cff_doi} align"
                ),
            )

        self.report.metrics[
            "release_version"
        ] = code_version

        self.report.metrics[
            "release_date"
        ] = code_date

        self.report.metrics[
            "doi"
        ] = cff_doi

    def check_ringconn_source_exports(self) -> None:
        check = "RingConn source exports"

        directory = (
            self.root
            / RINGCONN_DIRECTORY
        )

        if not directory.is_dir():
            self.report.error(
                check,
                (
                    "Missing source directory: "
                    f"{RINGCONN_DIRECTORY.as_posix()}"
                ),
            )
            return

        gitattributes = (
            self.root
            / ".gitattributes"
        )

        rule = (
            "data/source_exports/**/*.csv -text"
        )

        attributes_text = ""

        if gitattributes.is_file():
            attributes_text = (
                gitattributes.read_text(
                    encoding="utf-8-sig",
                    errors="replace",
                )
            )

        if rule not in attributes_text:
            self.report.error(
                check,
                (
                    "Missing .gitattributes "
                    "byte-preservation rule: "
                    f"{rule}"
                ),
            )

        failures = 0

        for filename, expected in (
            EXPECTED_RINGCONN.items()
        ):
            path = directory / filename

            if not path.is_file():
                failures += 1
                self.report.error(
                    check,
                    (
                        "Missing RingConn "
                        f"source file: {filename}"
                    ),
                )
                continue

            data = path.read_bytes()
            actual_hash = hashlib.sha256(
                data
            ).hexdigest()

            if len(data) != expected["bytes"]:
                failures += 1
                self.report.error(
                    check,
                    (
                        "Byte-size mismatch for "
                        f"{filename}: expected "
                        f"{expected['bytes']}, "
                        f"got {len(data)}"
                    ),
                )

            if actual_hash != expected["sha256"]:
                failures += 1
                self.report.error(
                    check,
                    (
                        "SHA-256 mismatch for "
                        f"{filename}: expected "
                        f"{expected['sha256']}, "
                        f"got {actual_hash}"
                    ),
                )

            crlf = data.count(b"\r\n")
            bare_lf = (
                data.count(b"\n")
                - crlf
            )

            if bare_lf != 0:
                failures += 1
                self.report.error(
                    check,
                    (
                        "Bare LF line endings detected "
                        f"in {filename}: {bare_lf}"
                    ),
                )

            header, rows = read_csv(path)

            if header != expected["header"]:
                failures += 1
                self.report.error(
                    check,
                    (
                        "Provider header drift in "
                        f"{filename}: expected "
                        f"{expected['header']!r}, "
                        f"got {header!r}"
                    ),
                )

            if len(rows) != expected["rows"]:
                failures += 1
                self.report.error(
                    check,
                    (
                        "Row-count mismatch for "
                        f"{filename}: expected "
                        f"{expected['rows']}, "
                        f"got {len(rows)}"
                    ),
                )

        if (
            failures == 0
            and rule in attributes_text
        ):
            self.report.pass_(
                check,
                (
                    "Three source CSVs retain "
                    "registered bytes, CRLF line "
                    "endings, provider headers, "
                    "and row counts"
                ),
            )


def read_csv(
    path: Path,
) -> tuple[
    list[str],
    list[list[str]],
]:
    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        reader = csv.reader(handle)

        try:
            header = next(reader)
        except StopIteration:
            return [], []

        return header, list(reader)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for block in iter(
            lambda: handle.read(
                1024 * 1024
            ),
            b"",
        ):
            digest.update(block)

    return digest.hexdigest()


def parse_int(value: str) -> int | None:
    text = value.strip()

    if not text:
        return None

    try:
        return int(float(text))
    except ValueError:
        return None


def find_column(
    header: Sequence[str],
    candidates: Sequence[str],
) -> str | None:
    normalized = {
        name.strip().lower(): name
        for name in header
    }

    for candidate in candidates:
        if candidate.lower() in normalized:
            return normalized[
                candidate.lower()
            ]

    return None


def path_is_within(
    path: Path,
    root: Path,
) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def strip_fenced_code(
    text: str,
) -> tuple[str, bool]:
    output: list[str] = []
    active_marker: str | None = None
    active_length = 0

    for line in text.splitlines():
        match = FENCE_RE.match(line)

        if match:
            fence = match.group(1)
            marker = fence[0]

            if active_marker is None:
                active_marker = marker
                active_length = len(fence)
            elif (
                marker == active_marker
                and len(fence) >= active_length
            ):
                active_marker = None
                active_length = 0

            output.append("")
            continue

        output.append(
            ""
            if active_marker
            else line
        )

    return (
        "\n".join(output),
        active_marker is not None,
    )


def normalize_markdown_destination(
    raw: str,
) -> str:
    value = raw.strip()

    if (
        value.startswith("<")
        and value.endswith(">")
    ):
        value = value[1:-1].strip()
    elif (
        value.startswith("<")
        and ">" in value
    ):
        value = value[
            1:value.index(">")
        ]
    else:
        match = re.match(
            (
                r"^(\S+)"
                r"(?:\s+[\"'].*[\"'])?$"
            ),
            value,
        )

        if match:
            value = match.group(1)

    return value.strip()


def is_external_destination(
    destination: str,
) -> bool:
    lowered = destination.lower()

    if lowered.startswith(
        (
            "http://",
            "https://",
            "mailto:",
            "tel:",
            "data:",
            "ftp://",
        )
    ):
        return True

    if lowered.startswith("//"):
        return True

    return False


def github_markdown_anchors(
    path: Path,
) -> set[str]:
    text, _ = strip_fenced_code(
        path.read_text(
            encoding="utf-8-sig",
            errors="replace",
        )
    )

    seen: Counter[str] = Counter()
    anchors: set[str] = set()

    for line in text.splitlines():
        match = HEADING_RE.match(line)

        if not match:
            continue

        heading = match.group(2)
        base = github_slug(heading)

        if not base:
            continue

        count = seen[base]

        slug = (
            base
            if count == 0
            else f"{base}-{count}"
        )

        seen[base] += 1
        anchors.add(slug)

    return anchors


def github_slug(value: str) -> str:
    text = re.sub(
        r"<[^>]+>",
        "",
        value,
    )

    text = re.sub(
        r"[`*_~]",
        "",
        text,
    )

    text = unquote(
        text
    ).strip().lower()

    text = "".join(
        character
        for character in text
        if (
            character.isalnum()
            or character in " _-"
        )
    )

    text = re.sub(
        r"\s+",
        "-",
        text,
    )

    return text.strip("-")


def cff_scalar(
    text: str,
    key: str,
) -> str:
    match = re.search(
        (
            rf"^{re.escape(key)}:"
            r"\s*(.+?)\s*$"
        ),
        text,
        flags=re.MULTILINE,
    )

    if not match:
        return ""

    value = match.group(1).strip()

    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in {'"', "'"}
    ):
        value = value[1:-1]

    return value


def safe_extract_zip(
    path: Path,
    destination: Path,
    report: Report,
) -> Path | None:
    check = "ZIP safety"

    try:
        with zipfile.ZipFile(path) as archive:
            bad_member = archive.testzip()

            if bad_member:
                report.error(
                    check,
                    (
                        "CRC failure in ZIP member: "
                        f"{bad_member}"
                    ),
                )
                return None

            for info in archive.infolist():
                name = info.filename.replace(
                    "\\",
                    "/",
                )

                pure = PurePosixPath(name)

                if (
                    pure.is_absolute()
                    or ".." in pure.parts
                    or WINDOWS_DRIVE_RE.match(name)
                ):
                    report.error(
                        check,
                        (
                            "Unsafe ZIP member path: "
                            f"{info.filename}"
                        ),
                    )
                    return None

            archive.extractall(destination)

    except (
        OSError,
        zipfile.BadZipFile,
    ) as exc:
        report.error(
            check,
            f"Cannot open ZIP: {exc}",
        )
        return None

    candidates = [
        item
        for item in destination.iterdir()
        if item.is_dir()
    ]

    root = (
        candidates[0]
        if len(candidates) == 1
        else destination
    )

    report.pass_(
        check,
        (
            "CRC and path-safety checks pass "
            f"for {path.name}"
        ),
    )

    return root


def default_root() -> Path:
    script = Path(__file__).resolve()
    candidate = script.parent.parent

    if (
        candidate
        / "README.md"
    ).exists():
        return candidate

    return Path.cwd()


def print_human(
    report: Report,
    root: Path,
) -> None:
    print(f"Repository: {root}")
    print()

    for level in (
        "ERROR",
        "WARN",
        "PASS",
    ):
        items = [
            finding
            for finding in report.findings
            if finding.level == level
        ]

        if not items:
            continue

        print(
            f"{level} ({len(items)})"
        )

        for finding in items:
            print(
                (
                    f"  [{finding.check}] "
                    f"{finding.message}"
                )
            )

        print()

    print("SUMMARY")
    print(
        f"  Errors:   {len(report.errors)}"
    )
    print(
        f"  Warnings: {len(report.warnings)}"
    )
    print(
        f"  Passes:   {len(report.passes)}"
    )
    print(
        (
            "  Result:   "
            + (
                "FAIL"
                if report.errors
                else "PASS"
            )
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
    )

    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=default_root(),
        help=(
            "Repository directory or GitHub ZIP "
            "(default: repository containing "
            "this script)"
        ),
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = Report()

    supplied = (
        args.path
        .expanduser()
        .resolve()
    )

    if not supplied.exists():
        report.error(
            "input",
            (
                "Path does not exist: "
                f"{supplied}"
            ),
        )

        root = supplied

    elif (
        supplied.is_file()
        and supplied.suffix.lower() == ".zip"
    ):
        with tempfile.TemporaryDirectory(
            prefix=(
                "daniel-repo-validation-"
            )
        ) as temp:
            extracted = safe_extract_zip(
                supplied,
                Path(temp),
                report,
            )

            if extracted is not None:
                root = extracted.resolve()
                Validator(
                    root,
                    report,
                ).run()
            else:
                root = supplied

            emit_results(
                args,
                report,
                root,
            )

            return (
                1
                if report.errors
                else 0
            )

    elif supplied.is_dir():
        root = supplied

        Validator(
            root,
            report,
        ).run()

    else:
        report.error(
            "input",
            (
                "Input must be a repository "
                "directory or .zip file"
            ),
        )

        root = supplied

    emit_results(
        args,
        report,
        root,
    )

    return (
        1
        if report.errors
        else 0
    )


def emit_results(
    args: argparse.Namespace,
    report: Report,
    root: Path,
) -> None:
    if args.json:
        payload = {
            "root": str(root),
            "result": (
                "FAIL"
                if report.errors
                else "PASS"
            ),
            "errors": len(report.errors),
            "warnings": len(report.warnings),
            "metrics": report.metrics,
            "findings": [
                asdict(item)
                for item in report.findings
            ],
        }

        print(
            json.dumps(
                payload,
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print_human(
            report,
            root,
        )


if __name__ == "__main__":
    sys.exit(main())
