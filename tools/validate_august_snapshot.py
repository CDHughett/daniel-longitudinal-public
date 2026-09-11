#!/usr/bin/env python3
"""Validate the protected August 2026 snapshot across repository layers.

This validator is intentionally narrow. It protects the completed August
snapshot against silent drift between source artifacts, structured tables,
provenance documentation, and the formal Model Error 043 closure.

It never edits repository files.
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


SNAPSHOT_MONTH = "2026-08"
BIOLOGICAL_DATE = "2026-08-17"
BODPOD_DATE = "2026-08-18"
COLLECTION_TIME = "05:37 local"

EXPECTED_ARTIFACT_HASHES = {
    "2026-08-bodpod-cosmed.jpg":
        "9c8e45cab3913503d89be8bf62ab489fe434382d3f633e961c070c9e22034717",
    "2026-08-dexa-body-comp.jpg":
        "cabb344a66ca9044126e533241d7322c4f72d3c26a13e9fde8ebfc2330b5c3a1",
    "2026-08-dexa-summary.jpg":
        "6b624b80e60192536a965cf53914a9f648b40de13425d3b08822fc6a244311ac",
    "2026-08-vo2-summary.pdf":
        "f6dd377ddd6537e530e86373ea096c0ea4895898e38156f32d73c985fac7bb2a",
    "2026-08-advanced-truage.pdf":
        "9ac47a41bd82ea48db9c4f196350c150837f1d5f18d1102ac9844851166d316d",
    "2026-08-truage.pdf":
        "c0271c82a9d3ed62168909ddd4d9376a15d926f49b347a29c6d4c6975b2d8849",
    "2026-08-truhealth.pdf":
        "66f9313966c99a9dca51367c37c8d7c87f9360d7e2c65ccabc3429285fd03765",
}

EXPECTED_SNAPSHOT_NUMERIC = {
    "chronological_age": "37.3",
    "omicm_age": "33.4",
    "omicm_age_delta_years": "-3.9",
    "dunedin_pace": "0.77",
    "symphony_age": "46.1",
    "blood_age": "44.3",
    "brain_age": "44.0",
    "inflammation_age": "41.3",
    "heart_age": "46.2",
    "hormone_age": "36.0",
    "immune_age": "44.7",
    "kidney_age": "46.4",
    "liver_age": "43.8",
    "metabolic_age": "43.1",
    "lung_age": "47.1",
    "musculoskeletal_age": "40.1",
    "total_mass_lbs": "233.9",
    "body_fat_pct_dexa": "17.1",
    "fat_mass_lbs_dexa": "40.0",
    "lean_mass_lbs_dexa": "185.3",
    "visceral_fat_lbs": "0.71",
    "t_score": "3.00",
    "bodpod_body_fat_pct": "11.3",
    "bodpod_fat_mass_lbs": "26.630",
    "bodpod_ffm_lbs": "208.693",
    "bodpod_body_mass_lbs": "235.323",
    "bodpod_ree_kcal_day": "2491",
    "bodpod_tee_kcal_day": "4334",
    "truhealth_vitamins_score": "58",
    "truhealth_amino_acids_score": "68",
    "truhealth_antioxidants_score": "59",
    "truhealth_fats_membranes_score": "56",
    "truhealth_lipid_peroxidation_score": "47",
    "truhealth_serum_lipids_score": "73",
    "truhealth_blood_pressure_score": "55",
    "truhealth_metabolic_score": "52",
    "truhealth_immune_score": "70",
    "truhealth_neurocognitive_score": "71",
    "truhealth_inflammation_score": "79",
    "truhealth_stress_score": "40",
    "truhealth_toxins_score": "41",
    "truhealth_uric_acid_pathway_score": "51",
    "truhealth_mitochondrial_function_score": "39",
    "truhealth_oxidative_defense_score": "66",
    "truhealth_nad_metabolism_score": "35",
    "truhealth_ketones_score": "34",
    "truhealth_supplements_score": "67",
}

EPIGENETIC_FIELD_MAP = {
    "omicm_age": ("aging", "omicm_age", "TruAge"),
    "chronological_age": ("aging", "chronological_age", "TruAge"),
    "omicm_age_delta_years": ("aging", "omicm_age_delta", "TruAge"),
    "dunedin_pace": ("aging", "dunedin_pace", "TruAge"),
    "symphony_age": ("aging", "symphony_age", "Advanced_TruAge"),
    "blood_age": ("organ_age", "blood_age", "Advanced_TruAge"),
    "brain_age": ("organ_age", "brain_age", "Advanced_TruAge"),
    "inflammation_age": ("organ_age", "inflammation_age", "Advanced_TruAge"),
    "heart_age": ("organ_age", "heart_age", "Advanced_TruAge"),
    "hormone_age": ("organ_age", "hormone_age", "Advanced_TruAge"),
    "immune_age": ("organ_age", "immune_age", "Advanced_TruAge"),
    "kidney_age": ("organ_age", "kidney_age", "Advanced_TruAge"),
    "liver_age": ("organ_age", "liver_age", "Advanced_TruAge"),
    "metabolic_age": ("organ_age", "metabolic_age", "Advanced_TruAge"),
    "lung_age": ("organ_age", "lung_age", "Advanced_TruAge"),
    "musculoskeletal_age": ("organ_age", "musculoskeletal_age", "Advanced_TruAge"),
    "truhealth_vitamins_score": ("truhealth_domain", "vitamins_score", "TruHealth"),
    "truhealth_amino_acids_score": ("truhealth_domain", "amino_acids_score", "TruHealth"),
    "truhealth_antioxidants_score": ("truhealth_domain", "antioxidants_score", "TruHealth"),
    "truhealth_fats_membranes_score": ("truhealth_domain", "fats_membranes_score", "TruHealth"),
    "truhealth_lipid_peroxidation_score": ("truhealth_domain", "lipid_peroxidation_score", "TruHealth"),
    "truhealth_serum_lipids_score": ("truhealth_domain", "serum_lipids_score", "TruHealth"),
    "truhealth_blood_pressure_score": ("truhealth_domain", "blood_pressure_score", "TruHealth"),
    "truhealth_metabolic_score": ("truhealth_domain", "metabolic_score", "TruHealth"),
    "truhealth_immune_score": ("truhealth_domain", "immune_score", "TruHealth"),
    "truhealth_neurocognitive_score": ("truhealth_domain", "neurocognitive_score", "TruHealth"),
    "truhealth_inflammation_score": ("truhealth_domain", "inflammation_score", "TruHealth"),
    "truhealth_stress_score": ("truhealth_domain", "stress_score", "TruHealth"),
    "truhealth_toxins_score": ("truhealth_domain", "toxins_score", "TruHealth"),
    "truhealth_uric_acid_pathway_score": ("truhealth_domain", "uric_acid_pathway_score", "TruHealth"),
    "truhealth_mitochondrial_function_score": ("truhealth_domain", "mitochondrial_function_score", "TruHealth"),
    "truhealth_oxidative_defense_score": ("truhealth_domain", "oxidative_defense_score", "TruHealth"),
    "truhealth_nad_metabolism_score": ("truhealth_domain", "nad_metabolism_score", "TruHealth"),
    "truhealth_ketones_score": ("truhealth_domain", "ketones_score", "TruHealth"),
    "truhealth_supplements_score": ("truhealth_domain", "supplements_score", "TruHealth"),
}


def decimal_equal(actual: str, expected: str) -> bool:
    try:
        return Decimal(actual.strip()) == Decimal(expected)
    except (InvalidOperation, AttributeError):
        return False


def read_dict_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_checksum_manifest(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    pattern = re.compile(r"^([0-9a-fA-F]{64})[ \t]+\*?(.+?)\s*$")
    for line_number, raw in enumerate(
        path.read_text(encoding="utf-8-sig").splitlines(), start=1
    ):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = pattern.match(line)
        if not match:
            raise ValueError(f"Malformed checksum line {line_number}: {raw!r}")
        digest, filename = match.groups()
        entries[filename] = digest.lower()
    return entries


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    snapshot_path = root / "data/biomarker_snapshot.csv"
    epigenetic_path = root / "data/epigenetic_longitudinal.csv"
    dq_path = root / "data/source_provenance/2026-08-trudiagnostic-reconciliation.md"
    closure_path = root / "data/model_error/record_043_closure.md"
    snapshot_dir = root / "snapshots/2026-08"
    checksum_path = snapshot_dir / "checksums.txt"

    required = [
        snapshot_path,
        epigenetic_path,
        dq_path,
        closure_path,
        checksum_path,
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing required August validation source: {path.relative_to(root)}")

    if errors:
        return errors

    # Integrated snapshot row.
    snapshot_rows = read_dict_rows(snapshot_path)
    august_rows = [row for row in snapshot_rows if row.get("date", "").strip() == SNAPSHOT_MONTH]
    if len(august_rows) != 1:
        errors.append(
            f"Expected exactly one {SNAPSHOT_MONTH} integrated snapshot row; found {len(august_rows)}"
        )
    else:
        row = august_rows[0]
        text_expectations = {
            "source": "integrated",
            "dexa_date": BIOLOGICAL_DATE,
            "bodpod_date": BODPOD_DATE,
        }
        for field, expected in text_expectations.items():
            actual = row.get(field, "").strip()
            if actual != expected:
                errors.append(
                    f"August snapshot {field} drift: expected {expected!r}, got {actual!r}"
                )

        for field, expected in EXPECTED_SNAPSHOT_NUMERIC.items():
            actual = row.get(field, "").strip()
            if not actual:
                errors.append(f"August snapshot required field is blank: {field}")
            elif not decimal_equal(actual, expected):
                errors.append(
                    f"August snapshot {field} drift: expected {expected}, got {actual}"
                )

        notes = row.get("notes", "")
        required_notes = [
            "Canonical TruDiagnostic collection: 2026-08-17 05:37 local",
            "Bod Pod values transcribed directly from 2026-08-bodpod-cosmed.jpg",
            "TGV model is provider-reported as Predicted",
        ]
        for snippet in required_notes:
            if snippet not in notes:
                errors.append(f"August snapshot provenance note missing: {snippet!r}")

    # Molecular cross-layer consistency.
    epigenetic_rows = read_dict_rows(epigenetic_path)
    indexed: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in epigenetic_rows:
        if row.get("date", "").strip() != BIOLOGICAL_DATE:
            continue
        key = (row.get("domain", "").strip(), row.get("biomarker", "").strip())
        indexed.setdefault(key, []).append(row)

    for snapshot_field, (domain, biomarker, expected_source) in EPIGENETIC_FIELD_MAP.items():
        matches = indexed.get((domain, biomarker), [])
        if len(matches) != 1:
            errors.append(
                f"Expected one {BIOLOGICAL_DATE} epigenetic row for "
                f"{domain}/{biomarker}; found {len(matches)}"
            )
            continue

        row = matches[0]
        expected_value = EXPECTED_SNAPSHOT_NUMERIC[snapshot_field]
        actual_value = row.get("value", "").strip()
        if not decimal_equal(actual_value, expected_value):
            errors.append(
                f"Epigenetic {domain}/{biomarker} drift: "
                f"expected {expected_value}, got {actual_value!r}"
            )

        actual_source = row.get("source", "").strip()
        if actual_source != expected_source:
            errors.append(
                f"Epigenetic {domain}/{biomarker} source drift: "
                f"expected {expected_source!r}, got {actual_source!r}"
            )

        if august_rows:
            snapshot_value = august_rows[0].get(snapshot_field, "").strip()
            if not decimal_equal(actual_value, snapshot_value):
                errors.append(
                    f"Cross-layer mismatch for {snapshot_field}: "
                    f"biomarker_snapshot={snapshot_value!r}, "
                    f"epigenetic_longitudinal={actual_value!r}"
                )

    # Canonical source/date reconciliation.
    dq_text = dq_path.read_text(encoding="utf-8-sig", errors="replace")
    dq_expectations = [
        "Sample collection date: 2026-08-17",
        "Sample collection time: 05:37 local",
        "public sanitized derivatives",
        "provider-displayed `08/16/2026` header date does not shift structured molecular values to August 16",
    ]
    for snippet in dq_expectations:
        if snippet not in dq_text:
            errors.append(f"DQ-010 required provenance statement missing: {snippet!r}")

    # Formal 043 closure remains aligned to the protected snapshot.
    closure_text = closure_path.read_text(encoding="utf-8-sig", errors="replace")
    closure_expectations = [
        "**Primary biological endpoint:** 2026-08-17",
        "| OMICm age delta | -1.1 y | -3.7 y | -3.9 y |",
        "| DunedinPACE | 0.88 | 0.79 | 0.77 |",
        "| SymphonyAge | 51.2 y | 37.8 y | 46.1 y |",
        "combined:          11 of 30 = 36.7%",
        "actual:          overall_improvement_not_met",
        "error_direction: over",
    ]
    for snippet in closure_expectations:
        if snippet not in closure_text:
            errors.append(f"Record 043 closure alignment missing: {snippet!r}")

    # August artifact identity is explicitly frozen here, not only self-checked
    # against a mutable checksum manifest.
    try:
        manifest = parse_checksum_manifest(checksum_path)
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"Cannot parse August checksum manifest: {exc}")
        manifest = {}

    for filename, expected_hash in EXPECTED_ARTIFACT_HASHES.items():
        path = snapshot_dir / filename
        if not path.is_file():
            errors.append(f"Missing protected August artifact: {filename}")
            continue

        registered = manifest.get(filename)
        if registered != expected_hash:
            errors.append(
                f"August checksum registration drift for {filename}: "
                f"expected {expected_hash}, got {registered!r}"
            )

        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            errors.append(
                f"August artifact byte drift for {filename}: "
                f"expected {expected_hash}, got {actual_hash}"
            )

    missing_registered = sorted(set(EXPECTED_ARTIFACT_HASHES) - set(manifest))
    if missing_registered:
        errors.append(
            "Protected August artifacts missing from checksum manifest: "
            + ", ".join(missing_registered)
        )

    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors = validate(root)

    if errors:
        print(f"August snapshot cross-layer validation: FAIL ({len(errors)} error(s))")
        for error in errors:
            print(f"  ERROR: {error}")
        return 1

    print("August snapshot cross-layer validation: PASS")
    print("  Protected molecular outputs: 35")
    print("  Protected DEXA/Bod Pod numeric fields: 12")
    print("  Protected August source artifacts: 7")
    print("  Canonical TruDiagnostic event: 2026-08-17 05:37 local")
    print("  Model Error 043 alignment: closed / overall_improvement_not_met / over")
    return 0


if __name__ == "__main__":
    sys.exit(main())
