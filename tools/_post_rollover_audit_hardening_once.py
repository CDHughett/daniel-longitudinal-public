from pathlib import Path
import subprocess


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one replacement target, found {count}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


# Remove volatile duplication from the methodology directory guide and align its
# dated current-state checkpoint with the W35 -> W36 rollover.
replace_once(
    "methodology/README.md",
    "# Current Methodology State\n\nAs of 2026-08-31:",
    "# Current Methodology State\n\nAs of the 2026-09-07 W35 → W36 rollover:",
)
replace_once(
    "methodology/README.md",
    "Canonical sleep:\nCurrent endpoint: see `../data/DATA_COVERAGE.md`\n203 daily rows\n\nCurrent weekly window:\n2026-W36\n\nMost recent closed weekly window:\n2026-W35",
    "Canonical sleep:\nCurrent row count and endpoint: see `../data/DATA_COVERAGE.md`\n\nCurrent weekly lifecycle:\nSee `../LATEST.md`",
)
replace_once(
    "methodology/README.md",
    "The 2026-08-31 revision is a live-state alignment only.",
    """The 2026-08-31 revision is a live-state alignment only.

On 2026-09-07, this guide was aligned after Week 35 closeout and Week 36 initialization.

The 2026-09-07 revision:

- advances the current methodology-state checkpoint through the W35 → W36 rollover
- removes duplicated live sleep counts and weekly-window identifiers from this directory guide in favor of `data/DATA_COVERAGE.md` and `LATEST.md`
- preserves record 043 as the sole open and unscored model-error record pending TruDiagnostic provider evidence
- preserves records 041, 042, 044, 045, and 046 as closed historical outcomes
- preserves Phase 2 — Load Integration and the consolidation / lock-in observation substate
- preserves the underlying B1 + Load Integration architecture
- leaves formal Phase 2D undeclared
- does not alter prediction wording, scoring boundaries, biological values, protocol state, phase state, release metadata, or DOI""",
)

# Clarify the status of the shared 041-044 preregistration artifact.
replace_once(
    "reports/README.md",
    "Current rules for records 041–044 are documented in:\n\n[`../methodology/open_prediction_evaluation_plan_041_044.md`](../methodology/open_prediction_evaluation_plan_041_044.md)",
    "The preserved preregistered plan for records 041–044 remains the governing artifact for open record 043 and the provenance artifact for closed records 041, 042, and 044:\n\n[`../methodology/open_prediction_evaluation_plan_041_044.md`](../methodology/open_prediction_evaluation_plan_041_044.md)",
)

# Harden weekly lifecycle validation.
validator = Path("tools/validate_repository.py")
text = validator.read_text(encoding="utf-8")
old_run = "        self.check_weekly_reports()\n        self.check_model_error_register()"
new_run = "        self.check_weekly_reports()\n        self.check_current_state_surfaces()\n        self.check_model_error_register()"
if text.count(old_run) != 1:
    raise SystemExit("validator run-order patch target not found exactly once")
text = text.replace(old_run, new_run, 1)

start = text.find("        if len(active) > 1:\n", text.find("    def check_weekly_reports"))
end = text.find("        if not missing and weekly:\n", start)
if start < 0 or end < 0:
    raise SystemExit("weekly active-state block not found")
replacement = '''        if len(active) != 1:
            if active:
                self.report.error(
                    check,
                    (
                        "Multiple active weekly reports: "
                        f"{', '.join(active)}"
                    ),
                )
            else:
                self.report.error(
                    check,
                    "No weekly report is explicitly marked Active",
                )
        elif numbers:
            expected_active = f"2026-W{max(numbers):02d}.md"
            if active[0] != expected_active:
                self.report.error(
                    check,
                    (
                        "Latest weekly report must be Active: "
                        f"expected {expected_active}, got {active[0]}"
                    ),
                )

'''
text = text[:start] + replacement + text[end:]

marker = "    def check_model_error_register(self) -> None:\n"
if text.count(marker) != 1:
    raise SystemExit("model-error function marker not found exactly once")

current_state_fn = r'''    def check_current_state_surfaces(self) -> None:
        check = "current state surfaces"
        failures = 0

        report_dir = self.root / "reports"
        weekly = sorted(
            (
                path
                for path in report_dir.glob("2026-W*.md")
                if WEEK_RE.match(path.name)
            ),
            key=lambda path: int(WEEK_RE.match(path.name).group(1)),
        )

        if len(weekly) < 2:
            self.report.error(
                check,
                "At least two weekly reports are required for current/prior alignment",
            )
            return

        latest_week = weekly[-1].stem
        prior_week = weekly[-2].stem

        surface_expectations = {
            "LATEST.md": [
                f"- **Active window:** {latest_week}",
                f"- **Prior window:** {prior_week} closed",
            ],
            "README.md": [
                f"Active weekly window:\n{latest_week}",
                f"Most recent closed window:\n{prior_week}",
            ],
            "INDEX.md": [
                f"Active weekly window:\n{latest_week}",
                f"Most recent closed window:\n{prior_week}",
            ],
        }

        for relative_path, expected_snippets in surface_expectations.items():
            path = self.root / relative_path
            if not path.is_file():
                failures += 1
                self.report.error(check, f"Missing current-state surface: {relative_path}")
                continue
            surface_text = path.read_text(encoding="utf-8-sig", errors="replace")
            for snippet in expected_snippets:
                if snippet not in surface_text:
                    failures += 1
                    self.report.error(
                        check,
                        f"{relative_path} is not aligned to {latest_week}/{prior_week}: missing {snippet!r}",
                    )

        def date_profile(relative_path: str, date_field: str) -> tuple[int, str, str]:
            header, rows = read_csv(self.root / relative_path)
            if date_field not in header:
                raise ValueError(f"{relative_path}: missing {date_field}")
            index = header.index(date_field)
            dates = [
                date.fromisoformat(row[index].strip())
                for row in rows
                if len(row) > index and row[index].strip()
            ]
            if not dates:
                raise ValueError(f"{relative_path}: no represented dates")
            return len(rows), min(dates).isoformat(), max(dates).isoformat()

        try:
            daily_rows, daily_start, daily_end = date_profile(
                "data/daily_biomarkers_v1.csv", "date"
            )
            sleep_rows, _, sleep_end = date_profile(
                "data/sleep_longitudinal_v1.csv", "date"
            )
            training_rows, _, training_end = date_profile(
                "data/training_blocks_v1.csv", "date"
            )
            context_rows, _, context_end = date_profile(
                "data/context_events_v1.csv", "end_date"
            )
        except (OSError, UnicodeError, csv.Error, ValueError) as exc:
            self.report.error(check, f"Cannot derive live coverage profile: {exc}")
            return

        if not (daily_end == sleep_end == training_end):
            failures += 1
            self.report.error(
                check,
                (
                    "Aligned daily/sleep/training endpoints diverge: "
                    f"daily={daily_end}, sleep={sleep_end}, training={training_end}"
                ),
            )

        coverage_path = self.root / "data/DATA_COVERAGE.md"
        if not coverage_path.is_file():
            failures += 1
            self.report.error(check, "Missing data/DATA_COVERAGE.md")
        else:
            coverage = coverage_path.read_text(encoding="utf-8-sig", errors="replace")
            expected_coverage = [
                (
                    "daily biomarkers",
                    f"`daily_biomarkers_v1.csv`; {daily_rows} continuous daily rows, {daily_start} through {daily_end}",
                ),
                (
                    "training",
                    f"`training_blocks_v1.csv`; {training_rows} session rows through {training_end}",
                ),
                (
                    "context events",
                    f"`context_events_v1.csv`; {context_rows} bounded events through {context_end}",
                ),
                (
                    "canonical sleep",
                    f"Canonical curated sleep has {sleep_rows} continuous daily rows through {sleep_end}",
                ),
            ]
            for label, snippet in expected_coverage:
                if snippet not in coverage:
                    failures += 1
                    self.report.error(
                        check,
                        f"DATA_COVERAGE.md {label} summary is stale or missing: {snippet!r}",
                    )

        if failures == 0:
            self.report.pass_(
                check,
                (
                    f"{latest_week} active / {prior_week} prior; live coverage aligns at "
                    f"daily={daily_rows}, sleep={sleep_rows}, training={training_rows}, context={context_rows}"
                ),
            )

        self.report.metrics["current_active_week"] = latest_week
        self.report.metrics["current_prior_week"] = prior_week

'''
text = text.replace(marker, current_state_fn + marker, 1)
validator.write_text(text, encoding="utf-8")

# Align verification/tool documentation with the stronger checks.
replace_once(
    "tools/README.md",
    "Checks repository mechanics, links, CSV structure, checksum manifests, canonical sleep continuity, weekly-report continuity, protected model-error state, release metadata, and source-export integrity.",
    "Checks repository mechanics, links, CSV structure, checksum manifests, canonical sleep continuity, weekly-report continuity, current-state surface and live-coverage alignment, protected model-error state, release metadata, and source-export integrity.",
)
replace_once(
    "tools/README.md",
    "`.github/workflows/validate.yml` runs both validators on pushes to `main` and on pull requests.",
    "`.github/workflows/validate.yml` runs both validators on pushes to `main`, on pull requests, and by manual workflow dispatch.",
)
replace_once(
    "VERIFICATION.md",
    "- weekly-report continuity\n- model-error continuity",
    "- weekly-report continuity\n- exactly one active weekly report, with the latest report required to be active\n- current-state alignment across `LATEST.md`, `README.md`, and `INDEX.md`\n- live row-count and endpoint alignment between canonical datasets and `data/DATA_COVERAGE.md`\n- model-error continuity",
)

# Record this hardening in the operational changelog.
changelog = Path("CHANGELOG.md")
ctext = changelog.read_text(encoding="utf-8")
anchor = "## [Unreleased]\n"
if ctext.count(anchor) != 1:
    raise SystemExit("CHANGELOG Unreleased anchor not found exactly once")
entry = '''## [Unreleased]

### Changed

#### September 7 post-rollover verification hardening

- Performed a live post-W35/W36 rollover semantic and verification audit.
- Confirmed the W35 public arithmetic and the synchronized daily, sleep, training, context-event, report, model-error, provenance, snapshot, and current-state layers.
- Removed stale duplicated live-state fields from `methodology/README.md` and redirected volatile weekly/coverage state to `LATEST.md` and `data/DATA_COVERAGE.md`.
- Clarified that the preserved records 041–044 preregistration artifact remains governing for open record 043 and provenance for the closed companion records.
- Hardened the core validator so exactly one weekly report must be active and the active report must be the latest report.
- Added current-state synchronization checks for `LATEST.md`, `README.md`, `INDEX.md`, and the canonical coverage summary in `data/DATA_COVERAGE.md`.
- Updated validation documentation to match the stronger checks.
- Updated CI to current SHA-pinned `actions/checkout` and `actions/setup-python` v7 releases and enabled manual validation dispatch.
- Added a selective post-rollover audit record under `docs/audits/`.

Classification:

```text
Biological-value change:
No

Canonical dataset-value change:
No

Prediction wording or outcome change:
No

Phase or protocol change:
No

Release or DOI change:
No

Documentation / validation / CI hardening:
Yes
```

'''
changelog.write_text(ctext.replace(anchor, entry, 1), encoding="utf-8")

baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
audit = f'''# Post-Weekly Rollover Verification Audit — 2026-09-07

**Audit type:** Post-W35 closeout / W36 initialization verification and semantic audit
**Repository:** `CDHughett/daniel-longitudinal-public`
**Branch:** `main`
**Audit baseline head:** `{baseline}`
**Prior completed rollover head:** `98308e330401252ecd5ed3ba636b65c3c47fe34b`
**Audit posture:** Live-repository verification, semantic alignment, maintenance review, and narrow remediation
**Validation status:** PENDING_FINAL_VALIDATION

---

## Purpose

This audit verifies the live repository after the 2026-W35 closeout and 2026-W36 initialization, then records narrow maintenance work justified by the post-rollover state.

The review covers:

- weekly lifecycle integrity
- W35 public arithmetic and training exposure
- canonical CSV continuity and current endpoints
- private-source provenance registration
- current-state navigation surfaces
- model-error and snapshot boundaries
- CI and validator behavior
- redundant volatile state
- documentation growth and future maintenance burden

No biological result, training exposure, prediction outcome, protocol state, phase state, release metadata, or DOI is changed by this audit.

---

## Verified Live State

The rollover state is coherent:

- `reports/2026-W35.md` is closed
- `reports/2026-W36.md` is active
- `LATEST.md`, `README.md`, and `INDEX.md` identify W36 as active and W35 as the prior closed window
- daily biomarkers contain 210 continuous rows through 2026-09-06
- canonical sleep contains 210 continuous rows through 2026-09-06
- training contains 339 session rows through 2026-09-06
- context events contain 44 bounded rows through 2026-09-03
- the protected historical training prefix remains 325 sessions through 2026-08-30
- private source v1.29 remains hash-registered
- Model Error 043 remains open and unscored pending required TruDiagnostic provider evidence
- records 041, 042, 044, 045, and 046 remain closed
- Phase 2D remains undeclared

---

## W35 Arithmetic Cross-Check

The public W35 source rows independently reproduce the principal closeout values:

- morning bodyweight: approximately 232.9 lb
- daily biomarker HRV: approximately 56.6 ms
- resting heart rate: 52.0 bpm
- daily average heart rate: approximately 65.3 bpm
- sleep HRV: 63.0 ms
- sleep average heart rate: approximately 53.1 bpm
- total sleep: approximately 7h07m
- deep sleep: approximately 1h19m
- REM sleep: approximately 50m
- B1: 7 sessions × 55 minutes = 385 minutes; 7 × 3.02 miles = 21.14 miles
- Load Integration: 7 sessions × 45 minutes = 315 minutes
- total formal training: 700 minutes

`Time in bed` remains a report-level Sleep Log metric rather than a field exposed in the canonical public sleep CSV; this audit therefore does not manufacture an independent public recomputation of that value.

---

## Findings and Remediation

### F01 — Current methodology guide retained stale volatile state

`methodology/README.md` still contained a stale 203-row canonical-sleep count inside its current-state section even though the canonical sleep dataset had advanced to 210 rows. It also duplicated the current and prior weekly identifiers.

**Disposition:** Corrected. The guide now delegates live sleep counts/endpoints to `data/DATA_COVERAGE.md` and weekly lifecycle state to `LATEST.md`. This reduces future synchronization burden.

### F02 — Weekly validator could pass a stale active-week assignment

The core validator rejected multiple active reports but treated zero active reports only as a warning and did not require the active report to be the latest report.

**Disposition:** Corrected. Exactly one active weekly report is now required, and it must be the highest current weekly index.

### F03 — Current-state surfaces and live coverage were not cross-validated

The validators could confirm individual files while still allowing a stale `LATEST.md`, `README.md`, `INDEX.md`, or `DATA_COVERAGE.md` summary to survive a rollover.

**Disposition:** Corrected. The core validator now cross-checks current/prior weekly state and derives canonical live row counts/endpoints before accepting the current coverage summary.

### F04 — CI action runtime was behind current maintained major versions

The validation workflow still used older action majors that produced Node-runtime deprecation warnings during rollover work.

**Disposition:** Corrected before this audit remediation. CI now uses SHA-pinned current v7 action releases and supports manual dispatch.

### F05 — Methodology directory guide remains larger than its navigational role requires

`methodology/README.md` remains a large historical/current hybrid and duplicates substantial outcome detail that also exists in preregistration artifacts, model-error records, and historical changelog/audit layers.

**Disposition:** Deferred. A future dedicated documentation-refactor pass should compress this guide around file roles, status, and governance boundaries while preserving historical provenance elsewhere. This is not required for W36 operation.

### F06 — Repository rule protection is not represented by a visible repository ruleset

The repository rulesets endpoint returned no configured rulesets. Traditional branch-protection state could not be inspected through the connected integration.

**Disposition:** Deferred. No protection change is made during this audit because the current maintenance model intentionally performs governed direct-to-main updates and automated self-cleaning commits. Protection policy should be designed separately rather than introduced incidentally.

---

## Decisions

No new release is justified at this time. The August TruDiagnostic provider result remains pending and record 043 remains open, so the August integrated biological interpretation is not complete.

No weekly/monthly split of the canonical longitudinal CSVs is justified. Their continuous form is still analytically and operationally preferable at current size.

No new model-error record, protocol escalation, recovery intervention, or Phase 2D declaration is created from the W35 closeout.

The principal next external-evidence event remains receipt and verification of the August TruDiagnostic provider result.

---

## Validation Requirement

This audit is accepted only if all of the following pass after the remediation is applied:

```text
python -m py_compile tools/validate_repository.py tools/validate_machine_readable.py
python tools/validate_repository.py
python tools/validate_machine_readable.py
git diff --check
```

The one-time remediation workflow is removed after a successful commit so the live repository returns to its ordinary permanent-workflow state.
'''
Path("docs/audits/2026-09-07-post-weekly-rollover-audit.md").write_text(audit, encoding="utf-8")

print("Post-rollover audit hardening prepared")
