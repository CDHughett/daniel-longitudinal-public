#!/usr/bin/env python3
"""Read-only semantic validation for the public machine-readable data layer."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

DAILY_PATH = Path("data/daily_biomarkers_v1.csv")
TRAINING_PATH = Path("data/training_blocks_v1.csv")
EVENTS_PATH = Path("data/context_events_v1.csv")
MODEL_ERROR_PATHS = (
    Path("data/model_error/model_error_gap_v1.csv"),
    Path("data/model_error/historical/model_error_gap_reconstructed.csv"),
)

DAILY_HEADER = [
    "date", "morning_weight_lb", "daily_hrv_ms", "resting_hr_bpm",
    "daily_avg_hr_bpm", "body_temp_f", "mood_state", "energy_state",
    "gi_state", "stomach_state", "pain_state", "sweating_state",
    "context_tags", "source_ref",
]
TRAINING_HEADER = [
    "session_id", "date", "block_type", "duration_min", "intensity",
    "hr_range_bpm", "distance_mi", "load_summary", "rpe", "fed_state",
    "execution_state", "equipment_context", "context_tags",
    "protocol_status", "source_ref",
]
EVENTS_HEADER = [
    "event_id", "start_date", "end_date", "event_type", "event_subtype",
    "impact_level", "description", "protocol_impact", "outcome_state",
    "related_week", "related_model_error", "source_ref",
]

DAILY_VOCABS = {
    "mood_state": {
        "", "stable", "sympathetic_leaning", "sympathetic",
        "labile_but_regulated", "calm", "reflective",
    },
    "energy_state": {
        "", "stable", "depleted_but_executed", "low_but_executed",
        "low_downregulated", "low_recovery_limited", "moderate",
        "low_moderate", "moderate_high", "high",
    },
    "gi_state": {"", "calm"},
    "stomach_state": {"", "calm"},
    "pain_state": {"", "none", "transient"},
    "sweating_state": {"", "none"},
}

TRAINING_VOCABS = {
    "block_type": {
        "legacy_firmware_block", "b1_load_integration", "b1",
        "load_integration", "b1_ground_integration", "active_recovery",
        "structured_recreation",
    },
    "fed_state": {"", "fasted", "fed"},
    "execution_state": {
        "", "controlled", "completed", "ambient", "trait_like",
        "trait_level", "recreational",
    },
}

EVENT_VOCABS = {
    "event_type": {
        "testing", "mechanical", "ordinary_life_load", "travel",
        "environmental", "social", "schedule_shift", "equipment_change",
        "other",
    },
    "impact_level": {"contextual", "material", "protocol_altering"},
    "outcome_state": {"absorbed", "resolved", "transient_effect"},
}

SNAKE_CASE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
WEEK_ID = re.compile(r"^\d{4}-W\d{2}$")
MODEL_ID = re.compile(r"^\d{3}$")
EVENT_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-(\d{2})$")
SCALAR_NUMERIC = re.compile(r"^\d+(?:\.\d+)?$")
RANGE_NUMERIC = re.compile(r"^(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)$")
DURATION_COMPOUND_1 = re.compile(r"^\d+(?:\.\d+)? min \+ circuits$")
DURATION_COMPOUND_2 = re.compile(
    r"^\d+(?:\.\d+)? min B1 \+ \d+(?:\.\d+)?-\d+(?:\.\d+)? strength$"
)
CANONICAL_SOURCE_REF = re.compile(
    r"^(?:private_workbook|private_pdf):Daniel_Dataset_v\d+\.\d+:[^:;]+:"
    r"\d{4}-\d{2}-\d{2}(?::[^;]+)?$"
)
LEGACY_TRAINING_SOURCE_REF = re.compile(
    r"^(?:wb|pdf):v\d+\.\d+:TB:\d{4}-\d{2}-\d{2}(?::[^;]+)?$"
)


class Results:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.metrics: dict[str, object] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def read_csv(root: Path, relative: Path, expected_header: list[str], results: Results) -> list[dict[str, str]]:
    path = root / relative
    if not path.exists():
        results.error(f"missing required file: {relative}")
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            header = reader.fieldnames or []
            if header != expected_header:
                results.error(f"{relative}: header mismatch: {header!r}")
            rows = []
            for row in reader:
                rows.append({key: (value or "").strip() for key, value in row.items()})
            return rows
    except Exception as exc:
        results.error(f"{relative}: CSV read failed: {exc}")
        return []


def parse_date(value: str, location: str, results: Results) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        results.error(f"{location}: invalid ISO date {value!r}")
        return None


def require_unique(values: list[str], label: str, results: Results) -> None:
    duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
    if duplicates:
        results.error(f"{label}: duplicate values: {duplicates[:10]!r}")


def validate_float(value: str, location: str, results: Results) -> None:
    if value == "":
        return
    try:
        parsed = float(value)
    except ValueError:
        results.error(f"{location}: expected numeric or blank, got {value!r}")
        return
    if parsed < 0:
        results.error(f"{location}: numeric value must be non-negative, got {value!r}")


def validate_vocab(row: dict[str, str], vocab_map: dict[str, set[str]], location: str, results: Results) -> None:
    for field, allowed in vocab_map.items():
        value = row.get(field, "")
        if value not in allowed:
            results.error(f"{location}.{field}: unregistered vocabulary value {value!r}")


def validate_snake(value: str, location: str, results: Results, *, allow_blank: bool = True) -> None:
    if value == "" and allow_blank:
        return
    if not SNAKE_CASE.fullmatch(value):
        results.error(f"{location}: expected lower-case snake_case, got {value!r}")


def validate_tag_list(value: str, location: str, results: Results) -> None:
    if not value:
        return
    for tag in value.split(";"):
        validate_snake(tag, location, results, allow_blank=False)


def validate_source_ref(value: str, location: str, results: Results, *, allow_legacy_training: bool) -> None:
    if not value:
        results.error(f"{location}: source_ref is required")
        return
    for ref in value.split(";"):
        if CANONICAL_SOURCE_REF.fullmatch(ref):
            continue
        if allow_legacy_training and LEGACY_TRAINING_SOURCE_REF.fullmatch(ref):
            continue
        results.error(f"{location}: unsupported source_ref syntax {ref!r}")


def validate_duration(value: str, location: str, results: Results) -> None:
    if value == "":
        return
    if SCALAR_NUMERIC.fullmatch(value):
        if float(value) < 0:
            results.error(f"{location}: duration cannot be negative")
        return
    match = RANGE_NUMERIC.fullmatch(value)
    if match:
        low, high = map(float, match.groups())
        if low > high:
            results.error(f"{location}: duration range lower bound exceeds upper bound")
        return
    if DURATION_COMPOUND_1.fullmatch(value) or DURATION_COMPOUND_2.fullmatch(value):
        return
    results.error(f"{location}: unsupported v1 duration expression {value!r}")


def validate_rpe(value: str, location: str, results: Results) -> None:
    if value == "" or SCALAR_NUMERIC.fullmatch(value):
        return
    match = RANGE_NUMERIC.fullmatch(value)
    if not match:
        results.error(f"{location}: expected scalar/range numeric RPE or blank, got {value!r}")
        return
    low, high = map(float, match.groups())
    if low > high:
        results.error(f"{location}: RPE range lower bound exceeds upper bound")


def model_error_ids(root: Path, results: Results) -> set[str]:
    ids: set[str] = set()
    for relative in MODEL_ERROR_PATHS:
        path = root / relative
        if not path.exists():
            if relative == MODEL_ERROR_PATHS[0]:
                results.error(f"missing required model-error file: {relative}")
            continue
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as fh:
                for row in csv.DictReader(fh):
                    raw = (row.get("record_id") or "").strip()
                    if raw:
                        ids.add(raw.zfill(3))
        except Exception as exc:
            results.error(f"{relative}: unable to read model-error IDs: {exc}")
    return ids


def validate(root: Path) -> Results:
    results = Results()
    daily = read_csv(root, DAILY_PATH, DAILY_HEADER, results)
    training = read_csv(root, TRAINING_PATH, TRAINING_HEADER, results)
    events = read_csv(root, EVENTS_PATH, EVENTS_HEADER, results)

    daily_dates: list[date] = []
    require_unique([row.get("date", "") for row in daily], f"{DAILY_PATH}.date", results)
    for index, row in enumerate(daily, start=2):
        loc = f"{DAILY_PATH}:{index}"
        parsed = parse_date(row.get("date", ""), f"{loc}.date", results)
        if parsed:
            daily_dates.append(parsed)
        for field in (
            "morning_weight_lb", "daily_hrv_ms", "resting_hr_bpm",
            "daily_avg_hr_bpm", "body_temp_f",
        ):
            validate_float(row.get(field, ""), f"{loc}.{field}", results)
        validate_vocab(row, DAILY_VOCABS, loc, results)
        validate_tag_list(row.get("context_tags", ""), f"{loc}.context_tags", results)
        validate_source_ref(row.get("source_ref", ""), f"{loc}.source_ref", results, allow_legacy_training=False)

    daily_min: date | None = min(daily_dates) if daily_dates else None
    daily_max: date | None = max(daily_dates) if daily_dates else None
    if daily_min and daily_max:
        represented = set(daily_dates)
        cursor = daily_min
        missing: list[str] = []
        while cursor <= daily_max:
            if cursor not in represented:
                missing.append(cursor.isoformat())
            cursor += timedelta(days=1)
        if missing:
            results.error(f"{DAILY_PATH}: missing dates inside represented interval: {missing[:20]!r}")
        results.metrics["daily_biomarkers"] = {
            "rows": len(daily),
            "start_date": daily_min.isoformat(),
            "end_date": daily_max.isoformat(),
            "continuous": not missing,
        }

    require_unique([row.get("session_id", "") for row in training], f"{TRAINING_PATH}.session_id", results)
    legacy_source_refs = 0
    for index, row in enumerate(training, start=2):
        loc = f"{TRAINING_PATH}:{index}"
        session_id = row.get("session_id", "")
        parsed = parse_date(row.get("date", ""), f"{loc}.date", results)
        if parsed:
            if not session_id.startswith(parsed.isoformat() + "-"):
                results.error(f"{loc}.session_id: must begin with session date; got {session_id!r}")
            if daily_min and daily_max and not (daily_min <= parsed <= daily_max):
                results.error(f"{loc}.date: outside daily-biomarker interval")
        validate_vocab(row, TRAINING_VOCABS, loc, results)
        validate_duration(row.get("duration_min", ""), f"{loc}.duration_min", results)
        validate_float(row.get("distance_mi", ""), f"{loc}.distance_mi", results)
        validate_rpe(row.get("rpe", ""), f"{loc}.rpe", results)
        validate_snake(row.get("equipment_context", ""), f"{loc}.equipment_context", results)
        validate_tag_list(row.get("context_tags", ""), f"{loc}.context_tags", results)
        validate_snake(row.get("protocol_status", ""), f"{loc}.protocol_status", results, allow_blank=False)
        source_ref = row.get("source_ref", "")
        validate_source_ref(source_ref, f"{loc}.source_ref", results, allow_legacy_training=True)
        legacy_source_refs += sum(
            1 for ref in source_ref.split(";") if LEGACY_TRAINING_SOURCE_REF.fullmatch(ref)
        )
    results.metrics["training_blocks"] = {
        "rows": len(training),
        "unique_session_ids": len({row.get("session_id", "") for row in training}),
        "legacy_source_refs": legacy_source_refs,
    }

    known_model_ids = model_error_ids(root, results)
    require_unique([row.get("event_id", "") for row in events], f"{EVENTS_PATH}.event_id", results)
    for index, row in enumerate(events, start=2):
        loc = f"{EVENTS_PATH}:{index}"
        event_id = row.get("event_id", "")
        start = parse_date(row.get("start_date", ""), f"{loc}.start_date", results)
        end = parse_date(row.get("end_date", ""), f"{loc}.end_date", results)
        match = EVENT_ID.fullmatch(event_id)
        if not match:
            results.error(f"{loc}.event_id: expected YYYY-MM-DD-##, got {event_id!r}")
        elif start and match.group(1) != start.isoformat():
            results.error(f"{loc}.event_id: date prefix must equal start_date")
        if start and end:
            if end < start:
                results.error(f"{loc}: end_date precedes start_date")
            if daily_min and daily_max and (start < daily_min or end > daily_max):
                results.error(f"{loc}: event interval extends outside daily-biomarker interval")
        validate_vocab(row, EVENT_VOCABS, loc, results)
        validate_snake(row.get("event_subtype", ""), f"{loc}.event_subtype", results, allow_blank=False)
        validate_snake(row.get("protocol_impact", ""), f"{loc}.protocol_impact", results, allow_blank=False)
        weeks = row.get("related_week", "")
        if weeks:
            for week in weeks.split(";"):
                if not WEEK_ID.fullmatch(week):
                    results.error(f"{loc}.related_week: invalid week ID {week!r}")
        related_ids = row.get("related_model_error", "")
        if related_ids:
            for raw in related_ids.split(";"):
                if not MODEL_ID.fullmatch(raw):
                    results.error(f"{loc}.related_model_error: invalid record ID {raw!r}")
                elif raw not in known_model_ids:
                    results.error(f"{loc}.related_model_error: record {raw} not found in model-error archive")
        validate_source_ref(row.get("source_ref", ""), f"{loc}.source_ref", results, allow_legacy_training=False)
    results.metrics["context_events"] = {
        "rows": len(events),
        "unique_event_ids": len({row.get("event_id", "") for row in events}),
    }

    results.metrics["model_error_ids_available"] = len(known_model_ids)
    results.metrics["overall"] = "PASS" if not results.errors else "FAIL"
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=None, help="repository root; defaults to parent of tools/")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    results = validate(root)

    if args.json:
        print(json.dumps({
            "root": str(root),
            "result": "PASS" if not results.errors else "FAIL",
            "error_count": len(results.errors),
            "warning_count": len(results.warnings),
            "metrics": results.metrics,
            "errors": results.errors,
            "warnings": results.warnings,
        }, indent=2))
    else:
        print("Machine-readable layer validation")
        print(f"Root: {root}")
        for message in results.errors:
            print(f"ERROR: {message}")
        for message in results.warnings:
            print(f"WARN: {message}")
        print(json.dumps(results.metrics, indent=2))
        print(f"Result: {'PASS' if not results.errors else 'FAIL'}")
        print(f"Errors: {len(results.errors)}  Warnings: {len(results.warnings)}")

    return 1 if results.errors else 0


if __name__ == "__main__":
    sys.exit(main())
