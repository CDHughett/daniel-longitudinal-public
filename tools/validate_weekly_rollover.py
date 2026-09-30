#!/usr/bin/env python3
"""Read-only validation of the latest completed weekly rollover.

This validator protects the arithmetic and lifecycle boundary that is easiest to
get wrong during an otherwise mechanically valid weekly closeout. It derives the
latest active report and immediately preceding closed report, recomputes the
closed-week public metrics from committed structured data, checks the closed
report's Structured Weekly Metrics table, and verifies the controlling private
source registration for that exact observation window.

It does not interpret biology, score predictions, infer missing data, or decide
whether progression/phase changes are scientifically justified.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

REPORT_DIR = Path("reports")
DAILY_PATH = Path("data/daily_biomarkers_v1.csv")
SLEEP_PATH = Path("data/sleep_longitudinal_v1.csv")
TRAINING_PATH = Path("data/training_blocks_v1.csv")
MANIFEST_PATH = Path("data/source_provenance/daniel_dataset_private_manifest.csv")

REPORT_NAME = re.compile(r"^(\d{4})-W(\d{2})\.md$")
STATUS = re.compile(r"^\*\*Status:\*\*\s*(Active|Closed)\s*$", re.MULTILINE)
WINDOW = re.compile(
    r"^\*\*Observation window:\*\*\s*(\d{4}-\d{2}-\d{2})\s+through\s+"
    r"(\d{4}-\d{2}-\d{2})\s*$",
    re.MULTILINE,
)


class Results:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.metrics: dict[str, object] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)


def parse_iso(value: str, label: str, results: Results) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        results.error(f"{label}: invalid ISO date {value!r}")
        return None


def read_csv(root: Path, relative: Path, results: Results) -> list[dict[str, str]]:
    path = root / relative
    if not path.is_file():
        results.error(f"missing required file: {relative}")
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [
                {key: (value or "").strip() for key, value in row.items()}
                for row in csv.DictReader(handle)
            ]
    except Exception as exc:
        results.error(f"{relative}: unable to parse CSV: {exc}")
        return []


def decimal_mean(rows: list[dict[str, str]], field: str) -> Decimal | None:
    values = [Decimal(row[field]) for row in rows if row.get(field, "") != ""]
    if not values:
        return None
    return sum(values) / Decimal(len(values))


def half_up(value: Decimal, digits: int = 1) -> Decimal:
    quantum = Decimal("1") if digits == 0 else Decimal("1").scaleb(-digits)
    return value.quantize(quantum, rounding=ROUND_HALF_UP)


def fmt_one(value: Decimal | None, suffix: str) -> str | None:
    if value is None:
        return None
    return f"{half_up(value, 1):.1f} {suffix}"


def fmt_minutes(value: Decimal | None) -> str | None:
    if value is None:
        return None
    minutes = int(half_up(value, 0))
    hours, remainder = divmod(minutes, 60)
    if hours:
        return f"{hours}h{remainder:02d}m"
    return f"{remainder}m"


def markdown_metric_rows(text: str) -> dict[str, tuple[str, str, str]]:
    rows: dict[str, tuple[str, str, str]] = {}
    in_section = False
    for line in text.splitlines():
        if line.strip() == "## Structured Weekly Metrics":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            continue
        if cells[0] in {"Metric", "---"} or set(cells[0]) <= {"-", ":"}:
            continue
        rows[cells[0]] = (cells[1], cells[2], cells[3])
    return rows


def report_meta(path: Path, results: Results) -> tuple[str | None, date | None, date | None, str]:
    text = path.read_text(encoding="utf-8-sig")
    status_match = STATUS.search(text)
    window_match = WINDOW.search(text)
    if not status_match:
        results.error(f"{path.relative_to(path.parents[1])}: missing standardized Status line")
        status = None
    else:
        status = status_match.group(1)
    if not window_match:
        results.error(f"{path.relative_to(path.parents[1])}: missing standardized Observation window")
        return status, None, None, text
    start = parse_iso(window_match.group(1), f"{path.name} window start", results)
    end = parse_iso(window_match.group(2), f"{path.name} window end", results)
    return status, start, end, text


def validate(root: Path) -> Results:
    results = Results()

    reports: list[tuple[int, int, Path]] = []
    for path in (root / REPORT_DIR).glob("*.md"):
        match = REPORT_NAME.match(path.name)
        if match:
            reports.append((int(match.group(1)), int(match.group(2)), path))
    reports.sort()

    if len(reports) < 2:
        results.error("fewer than two standardized weekly reports found")
        return results

    _, _, active_path = reports[-1]
    _, _, closed_path = reports[-2]

    active_status, active_start, active_end, _ = report_meta(active_path, results)
    closed_status, closed_start, closed_end, closed_text = report_meta(closed_path, results)

    if active_status != "Active":
        results.error(f"{active_path.name}: latest report must be Active, got {active_status!r}")
    if closed_status != "Closed":
        results.error(f"{closed_path.name}: immediately prior report must be Closed, got {closed_status!r}")

    if closed_start and closed_end:
        if closed_end - closed_start != timedelta(days=6):
            results.error(f"{closed_path.name}: observation window is not seven days")
    if active_start and active_end:
        if active_end - active_start != timedelta(days=6):
            results.error(f"{active_path.name}: observation window is not seven days")
    if closed_end and active_start and active_start != closed_end + timedelta(days=1):
        results.error(
            f"weekly windows are not contiguous: {closed_path.name} ends {closed_end}, "
            f"{active_path.name} starts {active_start}"
        )

    daily = read_csv(root, DAILY_PATH, results)
    sleep = read_csv(root, SLEEP_PATH, results)
    training = read_csv(root, TRAINING_PATH, results)
    manifest = read_csv(root, MANIFEST_PATH, results)

    if not (closed_start and closed_end):
        return results

    start_s, end_s = closed_start.isoformat(), closed_end.isoformat()
    daily_week = [row for row in daily if start_s <= row.get("date", "") <= end_s]
    sleep_week = [row for row in sleep if start_s <= row.get("date", "") <= end_s]
    training_week = [row for row in training if start_s <= row.get("date", "") <= end_s]

    if len(daily_week) != 7:
        results.error(f"{DAILY_PATH}: latest closed week has {len(daily_week)} rows, expected 7")
    if len(sleep_week) != 7:
        results.error(f"{SLEEP_PATH}: latest closed week has {len(sleep_week)} rows, expected 7")

    expected_dates = {(closed_start + timedelta(days=i)).isoformat() for i in range(7)}
    if {row.get("date", "") for row in daily_week} != expected_dates:
        results.error(f"{DAILY_PATH}: latest closed-week date set is incomplete or duplicated")
    if {row.get("date", "") for row in sleep_week} != expected_dates:
        results.error(f"{SLEEP_PATH}: latest closed-week date set is incomplete or duplicated")

    metrics = markdown_metric_rows(closed_text)
    required_rows = {
        "Morning bodyweight",
        "Daily biomarker HRV",
        "Resting heart rate",
        "Daily average heart rate",
        "Sleep HRV",
        "Sleep average heart rate",
        "Total sleep",
        "Deep sleep",
        "REM sleep",
        "B1 sessions",
        "Load Integration sessions",
        "Total formal training",
    }
    missing = sorted(required_rows - set(metrics))
    if missing:
        results.error(f"{closed_path.name}: Structured Weekly Metrics missing rows: {missing!r}")

    expected_values: dict[str, str | None] = {
        "Morning bodyweight": fmt_one(decimal_mean(daily_week, "morning_weight_lb"), "lb"),
        "Daily biomarker HRV": fmt_one(decimal_mean(daily_week, "daily_hrv_ms"), "ms"),
        "Resting heart rate": fmt_one(decimal_mean(daily_week, "resting_hr_bpm"), "bpm"),
        "Daily average heart rate": fmt_one(decimal_mean(daily_week, "daily_avg_hr_bpm"), "bpm"),
        "Sleep HRV": fmt_one(decimal_mean(sleep_week, "hrv_ms"), "ms"),
        "Sleep average heart rate": fmt_one(decimal_mean(sleep_week, "sleep_hr_avg_bpm"), "bpm"),
        "Total sleep": fmt_minutes(decimal_mean(sleep_week, "total_sleep_min")),
        "Deep sleep": fmt_minutes(decimal_mean(sleep_week, "deep_sleep_min")),
        "REM sleep": fmt_minutes(decimal_mean(sleep_week, "rem_sleep_min")),
    }

    b1 = [row for row in training_week if row.get("block_type") == "b1"]
    li = [row for row in training_week if row.get("block_type") == "load_integration"]

    expected_values["B1 sessions"] = str(len(b1))
    expected_values["Load Integration sessions"] = str(len(li))

    scalar_durations: list[Decimal] = []
    non_scalar: list[str] = []
    for row in training_week:
        raw = row.get("duration_min", "")
        try:
            scalar_durations.append(Decimal(raw))
        except Exception:
            non_scalar.append(f"{row.get('session_id', '?')}={raw!r}")
    if non_scalar:
        results.error(
            "latest closed week contains non-scalar duration expressions; weekly arithmetic "
            f"cannot be reproduced automatically: {non_scalar!r}"
        )
        total_training = None
    else:
        total_training = sum(scalar_durations, Decimal("0"))
        expected_values["Total formal training"] = f"{half_up(total_training, 0):.0f} min"

    for label, expected in expected_values.items():
        if expected is None or label not in metrics:
            continue
        actual = metrics[label][0]
        if actual != expected:
            results.error(
                f"{closed_path.name}: {label} mismatch: report={actual!r}, derived={expected!r}"
            )

    if "B1 sessions" in metrics:
        b1_minutes = sum((Decimal(row["duration_min"]) for row in b1), Decimal("0"))
        b1_miles = sum(
            (Decimal(row["distance_mi"]) for row in b1 if row.get("distance_mi", "")),
            Decimal("0"),
        )
        notes = metrics["B1 sessions"][2]
        expected_note = f"{half_up(b1_minutes, 0):.0f} formal minutes / {half_up(b1_miles, 2):.2f} miles"
        if expected_note not in notes:
            results.error(
                f"{closed_path.name}: B1 notes mismatch: expected substring {expected_note!r}"
            )

    if "Load Integration sessions" in metrics:
        li_minutes = sum((Decimal(row["duration_min"]) for row in li), Decimal("0"))
        notes = metrics["Load Integration sessions"][2]
        expected_note = f"{half_up(li_minutes, 0):.0f} formal minutes"
        if expected_note not in notes:
            results.error(
                f"{closed_path.name}: Load Integration notes mismatch: "
                f"expected substring {expected_note!r}"
            )

    if "Total formal training" in metrics:
        expected_sessions = f"{len(training_week)} completed sessions"
        if expected_sessions not in metrics["Total formal training"][2]:
            results.error(
                f"{closed_path.name}: total-training notes mismatch: "
                f"expected substring {expected_sessions!r}"
            )

    matching_sources = [
        row for row in manifest
        if row.get("coverage_start") == start_s
        and row.get("coverage_end") == end_s
        and row.get("hash_status") == "registered"
    ]
    if not matching_sources:
        results.error(
            f"{MANIFEST_PATH}: no registered private source exactly covers "
            f"{start_s} through {end_s}"
        )

    if daily and daily[-1].get("date") != end_s:
        results.error(
            f"{DAILY_PATH}: live endpoint {daily[-1].get('date')!r} does not match "
            f"latest closed-week end {end_s!r}"
        )
    if sleep and sleep[-1].get("date") != end_s:
        results.error(
            f"{SLEEP_PATH}: live endpoint {sleep[-1].get('date')!r} does not match "
            f"latest closed-week end {end_s!r}"
        )
    later_training = [row for row in training if row.get("date", "") > end_s]
    if later_training:
        results.error(
            f"{TRAINING_PATH}: contains completed sessions after latest closed-week end {end_s}"
        )

    results.metrics = {
        "active_report": active_path.name,
        "closed_report": closed_path.name,
        "closed_window": [start_s, end_s],
        "daily_rows_in_closed_window": len(daily_week),
        "sleep_rows_in_closed_window": len(sleep_week),
        "training_sessions_in_closed_window": len(training_week),
        "registered_sources_for_closed_window": [
            row.get("source_version") for row in matching_sources
        ],
        "derived": {key: value for key, value in expected_values.items() if value is not None},
    }
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    results = validate(root)

    print("Weekly rollover validation")
    print(f"Root: {root}")
    for key, value in results.metrics.items():
        print(f"{key}: {value}")

    if results.errors:
        print(f"Result: FAIL ({len(results.errors)} errors)")
        for item in results.errors:
            print(f"ERROR: {item}")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
