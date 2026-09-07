from pathlib import Path
import csv
import re
import subprocess


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(path: str, old: str, new: str, *, allow_already: bool = True) -> None:
    text = read(path)
    count = text.count(old)
    if count == 1:
        write(path, text.replace(old, new, 1))
        return
    if count == 0 and allow_already and new in text:
        return
    raise SystemExit(f"{path}: expected one match for replacement, found {count}")


def replace_section(path: str, start_heading: str, next_heading: str, new_section: str) -> None:
    text = read(path)
    start = text.find(start_heading)
    if start < 0:
        if new_section.strip() in text:
            return
        raise SystemExit(f"{path}: start heading not found: {start_heading}")
    end = text.find(next_heading, start + len(start_heading))
    if end < 0:
        raise SystemExit(f"{path}: next heading not found: {next_heading}")
    write(path, text[:start] + new_section.rstrip() + "\n\n" + text[end:])


def replace_tail(path: str, start_heading: str, new_tail: str) -> None:
    text = read(path)
    start = text.find(start_heading)
    if start < 0:
        if new_tail.strip() in text:
            return
        raise SystemExit(f"{path}: start heading not found: {start_heading}")
    write(path, text[:start] + new_tail.rstrip() + "\n")


def append_once(path: str, marker: str, rows: str) -> None:
    text = read(path)
    if marker in text:
        return
    write(path, text.rstrip("\n") + "\n" + rows.strip("\n"))


DAILY_ROWS = r'''2026-08-31,234.1,57,47,64,96.49,calm,high,calm,calm,none,none,post_snapshot_recovery;nocturnal_autonomic_variability;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-08-31
2026-09-01,233.4,63,55,65,96.39,calm,high,calm,calm,none,none,post_snapshot_recovery;nocturnal_autonomic_variability;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-09-01
2026-09-02,231.1,49,45,67,96.19,calm,high,calm,calm,none,none,post_snapshot_recovery;low_salience_execution;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-09-02
2026-09-03,232.1,53,57,68,96.85,calm,high,calm,calm,none,none,post_snapshot_recovery;yard_work;high_incidental_activity;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-09-03
2026-09-04,232.3,52,55,65,96.53,calm,high,calm,calm,none,none,post_snapshot_recovery;nocturnal_autonomic_variability;lower_intake_context;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-09-04
2026-09-05,233.1,59,55,67,96.42,calm,high,calm,calm,none,none,post_snapshot_recovery;nocturnal_autonomic_variability;biomarker_function_dissociation;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-09-05
2026-09-06,234.3,63,50,61,96.19,calm,high,calm,calm,none,none,post_snapshot_recovery;strong_overnight_recovery;function_preserved,private_workbook:Daniel_Dataset_v1.29:Daily Biomarkers:2026-09-06'''

SLEEP_ROWS = r'''2026-08-31,410,80,310,20,15,3,93,18.8,4.7,73.0,65,53,Calm,Stable,High,"good_sleep, reduced_sleep_duration, good_sleep_score, normal_sleep_efficiency, normal_sleep_onset, low_rem_sleep, low_rem_confidence, adequate_deep_sleep, elevated_light_sleep, low_sleep_fragmentation, elevated_sleep_hr, transient_hr_spikes, late_night_hr_downregulation, stable_hrv, normal_spo2, normal_respiratory_rate, stable_skin_temperature, good_sleeping_stress, vivid_dreaming, reality_adjacent_dreaming, coherent_dream_narrative, dream_problem_solving, non_emotional_dreaming, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, autonomic_variability, preserved_oxygenation, parasympathetic_recovery, high_training_readiness, training_previous_day",wearable+operator_log
2026-09-01,431,68,313,50,10,4,96,15.4,11.3,71.0,63,53,Calm,Stable,High,"good_sleep, mildly_reduced_sleep_duration, good_sleep_score, normal_sleep_efficiency, normal_sleep_onset, low_rem_sleep, low_rem_confidence, adequate_deep_sleep, elevated_light_sleep, brief_awakenings, early_night_hr_spike, strong_late_night_downregulation, stable_hrv, normal_spo2, normal_respiratory_rate, stable_skin_temperature, good_sleeping_stress, vivid_dreaming, quickly_forgotten_dream, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, autonomic_variability, preserved_oxygenation, parasympathetic_recovery, high_training_readiness, training_previous_day",wearable+operator_log
2026-09-02,436,95,289,52,11,2,95,21.2,11.6,64.7,58,47,Calm,Stable,High,"good_sleep, normal_sleep_duration, good_sleep_score, normal_sleep_efficiency, adequate_sleep_onset, low_rem_sleep, low_rem_confidence, adequate_deep_sleep, elevated_light_sleep, low_awake_time, mildly_reduced_hrv, low_sleep_hr, stable_sleep_hr, normal_spo2, normal_respiratory_rate, mildly_elevated_skin_temperature, good_sleeping_stress, vivid_dreaming, quickly_forgotten_dream, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, autonomic_variability, preserved_oxygenation, parasympathetic_recovery, high_training_readiness, training_previous_day",wearable+operator_log
2026-09-03,406,65,289,52,16,4,92,15.4,12.3,68.5,61,54,Calm,Stable,Medium,"good_sleep, reduced_sleep_duration, sleep_score_75, normal_sleep_efficiency, moderate_sleep_onset, low_rem_sleep, medium_rem_confidence, vivid_dreaming, dream_recall_lost_on_waking, adequate_deep_sleep, light_sleep_dominant, low_awake_time, moderate_sleep_fragmentation, stable_hrv, mildly_elevated_sleeping_hr, early_night_autonomic_activation, late_night_autonomic_settling, normal_spo2, stable_respiratory_rate, mildly_elevated_skin_temperature, normal_skin_temperature_variation, good_sleeping_stress, elevated_pre_sleep_stress, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, preserved_recovery_floor, moderate_training_readiness, training_previous_day",wearable+operator_log
2026-09-04,425,100,275,50,13,3,93,22.8,11.4,62.8,52,55,Calm,Stable,Medium,"good_sleep, mildly_reduced_sleep_duration, sleep_score_71, normal_sleep_efficiency, moderate_sleep_onset, low_rem_sleep, low_rem_confidence, adequate_deep_sleep, elevated_light_sleep, low_awake_time, mildly_reduced_hrv, mildly_elevated_sleep_hr, transient_nocturnal_hr_spike, normal_spo2, normal_respiratory_rate, stable_skin_temperature, good_sleeping_stress, vivid_dreaming, coherent_dream_narrative, recurring_dream, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, autonomic_variability, preserved_oxygenation, parasympathetic_recovery, medium_training_readiness, training_previous_day",wearable+operator_log
2026-09-05,392,80,272,40,24,5,86,19.2,9.6,65.4,73,62,Calm,Stable,Medium,"good_sleep, reduced_sleep_duration, good_sleep_score, normal_sleep_efficiency, delayed_sleep_onset, low_rem_sleep, low_rem_confidence, adequate_deep_sleep, elevated_light_sleep, moderate_sleep_fragmentation, elevated_sleep_hr, transient_nocturnal_hr_spikes, strong_late_night_downregulation, elevated_hrv, preserved_recovery, normal_spo2, normal_respiratory_rate, stable_skin_temperature, good_sleeping_stress, vivid_dreaming, quickly_forgotten_dream, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, autonomic_variability, parasympathetic_recovery, medium_training_readiness, training_previous_day",wearable+operator_log
2026-09-06,492,65,342,85,15,4,95,12.8,16.8,67.4,69,48,Calm,Stable,High,"good_sleep, normal_sleep_duration, good_sleep_score, normal_sleep_efficiency, normal_sleep_onset, adequate_rem_sleep, high_rem_confidence, adequate_deep_sleep, elevated_light_sleep, low_awake_time, brief_awakenings, low_sleeping_hr, strong_hrv, late_night_hrv_peak, stable_hrv, normal_spo2, normal_respiratory_rate, stable_skin_temperature, excellent_sleeping_stress, good_pre_sleep_stress, vivid_dreaming, dream_recall_lost_on_waking, calm_mood, stable_emotional_state, calm_gi, calm_stomach, no_sweating, no_pain, physiological_stability, autonomic_variability, strong_parasympathetic_recovery, high_training_readiness, training_previous_day",wearable+operator_log'''

TRAINING_ROWS = r'''2026-08-31-B1,2026-08-31,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,nocturnal_autonomic_variability;function_preserved,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-08-31:B1
2026-08-31-LI,2026-08-31,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_like,canonical,low_salience_execution,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-08-31:LI
2026-09-01-B1,2026-09-01,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,nocturnal_autonomic_variability;function_preserved,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-01:B1
2026-09-01-LI,2026-09-01,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_like,canonical,low_salience_execution,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-01:LI
2026-09-02-B1,2026-09-02,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-02:B1
2026-09-02-LI,2026-09-02,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_like,canonical,trance_like_subjective_execution;low_salience_execution;automaticity_deepened,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-02:LI
2026-09-03-B1,2026-09-03,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-03:B1
2026-09-03-LI,2026-09-03,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_level,canonical,yard_work_before_session;ordinary_life_load_absorbed;reserve_capacity_reported,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-03:LI
2026-09-04-B1,2026-09-04,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,less_favorable_overnight_state;function_preserved,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-04:B1
2026-09-04-LI,2026-09-04,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_level,canonical,biomarker_function_dissociation;low_salience_execution,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-04:LI
2026-09-05-B1,2026-09-05,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,less_favorable_overnight_state;function_preserved,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-05:B1
2026-09-05-LI,2026-09-05,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_like,canonical,biomarker_function_dissociation;low_salience_execution,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-05:LI
2026-09-06-B1,2026-09-06,b1,55,L (Z2),110-125,3.02,,4,fasted,ambient,standard_b1,strong_overnight_recovery,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-06:B1
2026-09-06-LI,2026-09-06,load_integration,45,L,95-120,,trap_bar_3x5;pullups_4x4;pushups_3x10;dead_hang_3x30s;mobility_15-20min;incline_walk_10min_nasal,4,fed,trait_like,canonical,low_salience_execution,completed_as_prescribed,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-06:LI'''

EVENT_ROWS = r'''2026-09-02-01,2026-09-02,2026-09-02,other,automaticity_deepening,contextual,"Load Integration was completed with subjectively trance-like, deeply embedded execution while the prescribed work remained unchanged; the observation is retained as increasing automaticity rather than a new formal execution category.",none,absorbed,2026-W35,,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-02:LI
2026-09-03-01,2026-09-03,2026-09-03,ordinary_life_load,yard_work,material,Front- and back-yard work occurred after breakfast and before afternoon Load Integration; the prescribed session remained intact and the operator reported substantial unused workload capacity.,none,absorbed,2026-W35,,private_workbook:Daniel_Dataset_v1.29:Training Blocks:2026-09-03:LI'''

MANIFEST_ROW = r'''v1.29,private_workbook,2026-08-31,2026-09-06,Daniel_Dataset_v1.29,367995,38d4b241c4d8a43a0650379c20839ce3f7f4b8d9940a8a814ae042e6aff0479c,registered,"daily_biomarkers_v1.csv;training_blocks_v1.csv;context_events_v1.csv","SHA-256 computed from the exact retained v1.29 workbook supplied for the 2026-09-07 closeout. Source date cells mix Excel serial dates and day-of-month integers; public extraction normalizes date indices to ISO form without changing biological or training values."'''

append_once("data/daily_biomarkers_v1.csv", "2026-09-06,234.3,63,50,61", DAILY_ROWS)
append_once("data/sleep_longitudinal_v1.csv", "2026-09-06,492,65,342,85", SLEEP_ROWS)
append_once("data/training_blocks_v1.csv", "2026-09-06-LI,2026-09-06", TRAINING_ROWS)
append_once("data/context_events_v1.csv", "2026-09-03-01,2026-09-03", EVENT_ROWS)
append_once("data/source_provenance/daniel_dataset_private_manifest.csv", "v1.29,private_workbook,2026-08-31,2026-09-06", MANIFEST_ROW)

validator = read("tools/validate_machine_readable.py")
if "PROTECTED_TRAINING_PREFIX_END" not in validator:
    validator = validator.replace(
        'EXPECTED_TRAINING_ROWS = 325',
        'PROTECTED_TRAINING_PREFIX_END = date(2026, 8, 30)\nEXPECTED_PROTECTED_TRAINING_ROWS = 325',
        1,
    )
    validator = re.sub(
        r'\n    if len\(training\) != EXPECTED_TRAINING_ROWS:\n        results\.error\(\n            f"\{TRAINING_PATH\}: expected \{EXPECTED_TRAINING_ROWS\} protected v1 session rows, found \{len\(training\)\}"\n        \)\n',
        '\n',
        validator,
        count=1,
    )
    validator = validator.replace(
        '    for index, row in enumerate(training, start=2):\n',
        '    protected_training_rows = 0\n    for index, row in enumerate(training, start=2):\n',
        1,
    )
    validator = validator.replace(
        '        if parsed:\n            if not session_id.startswith(parsed.isoformat() + "-"):\n',
        '        if parsed:\n            if parsed <= PROTECTED_TRAINING_PREFIX_END:\n                protected_training_rows += 1\n            if not session_id.startswith(parsed.isoformat() + "-"):\n',
        1,
    )
    old_metrics = '''    results.metrics["training_blocks"] = {\n        "rows": len(training),\n        "unique_session_ids": len({row.get("session_id", "") for row in training}),\n        "expected_rows": EXPECTED_TRAINING_ROWS,\n        "canonical_source_refs_required": True,\n    }\n'''
    new_metrics = '''    if protected_training_rows != EXPECTED_PROTECTED_TRAINING_ROWS:\n        results.error(\n            f"{TRAINING_PATH}: expected {EXPECTED_PROTECTED_TRAINING_ROWS} protected sessions "\n            f"through {PROTECTED_TRAINING_PREFIX_END.isoformat()}, found {protected_training_rows}"\n        )\n    results.metrics["training_blocks"] = {\n        "rows": len(training),\n        "unique_session_ids": len({row.get("session_id", "") for row in training}),\n        "protected_prefix_end": PROTECTED_TRAINING_PREFIX_END.isoformat(),\n        "protected_prefix_rows": protected_training_rows,\n        "expected_protected_prefix_rows": EXPECTED_PROTECTED_TRAINING_ROWS,\n        "append_rows": len(training) - protected_training_rows,\n        "canonical_source_refs_required": True,\n    }\n'''
    if old_metrics not in validator:
        raise SystemExit("tools/validate_machine_readable.py: training metrics block not found")
    validator = validator.replace(old_metrics, new_metrics, 1)
    write("tools/validate_machine_readable.py", validator)

coverage = read("data/DATA_COVERAGE.md")
coverage = coverage.replace("203 continuous daily rows, 2026-02-09 through 2026-08-30", "210 continuous daily rows, 2026-02-09 through 2026-09-06")
coverage = coverage.replace("325 session rows across the same represented interval", "339 session rows through 2026-09-06")
coverage = coverage.replace("42 bounded events through 2026-08-29", "44 bounded events through 2026-09-03")
coverage = coverage.replace("2026-02-09 through 2026-08-30\n203 continuous daily rows", "2026-02-09 through 2026-09-06\n210 continuous daily rows")
coverage = coverage.replace("2026-02-09 through 2026-08-30\n325 session rows", "2026-02-09 through 2026-09-06\n339 session rows")
coverage = coverage.replace("42 bounded event rows\nrepresented interval begins 2026-02-09\nlatest current event ends 2026-08-29", "44 bounded event rows\nrepresented interval begins 2026-02-09\nlatest current event ends 2026-09-03")
coverage = coverage.replace("populated through:\n\n```text\n2026-08-30", "populated through:\n\n```text\n2026-09-06")
coverage = coverage.replace("private `Daniel_Dataset_v1.0` through `v1.28` source states", "private `Daniel_Dataset_v1.0` through `v1.29` source states")
coverage = coverage.replace("completed private `Daniel_Dataset_v1.0` through `v1.28` source states", "completed private `Daniel_Dataset_v1.0` through `v1.29` source states")
write("data/DATA_COVERAGE.md", coverage)

schema = read("schemas/machine-readable-layer-v1.md")
schema = re.sub(
    r'Current shared represented interval:\n\n```text\n2026-02-09 through 2026-08-30\n```\n\nA later data extension may advance the end date without changing the v1 field structure\.',
    'The represented machine-readable interval begins on `2026-02-09`. Current live row counts and endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).\n\nA later data extension may advance the end date without changing the v1 field structure.',
    schema,
    count=1,
)
schema = schema.replace(
    'Current dataset: 203 continuous rows, `2026-02-09` through `2026-08-30`.',
    'Current row count and endpoint are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).',
)
schema = schema.replace(
    'Current dataset: 325 session rows, `2026-02-09` through `2026-08-30`.',
    'Current row count and endpoint are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md). The historical prefix through `2026-08-30` is protected at 325 sessions; later governed rows append without changing that prefix.',
)
schema = schema.replace(
    'Current dataset: 42 bounded events, current event coverage through `2026-08-29`.',
    'Current event count and endpoint are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).',
)
write("schemas/machine-readable-layer-v1.md", schema)

prov = read("data/source_provenance/README.md")
prov = prov.replace(
    "A SHA-256 is registered only when the exact private source file was available as a retained file during the 2026-09-06 provenance pass.",
    "A SHA-256 is registered only when the exact private source file is available as retained bytes at the time of registration. The initial historical pass occurred on 2026-09-06; the exact retained v1.29 workbook was registered during the 2026-09-07 weekly closeout.",
)
if "Date-cell normalization" not in prov:
    anchor = "The public files are curated extracts, not byte-identical transformations of the private workbook."
    prov = prov.replace(
        anchor,
        anchor + "\n\nDate-cell normalization is permitted when a retained workbook mixes Excel serial dates and day-of-month integer encodings. The public date index is normalized to the supported calendar date without altering the associated biological, sleep, or training value. This normalization is recorded in the manifest note for the affected source version.",
        1,
    )
write("data/source_provenance/README.md", prov)

ver = read("VERIFICATION.md")
ver = ver.replace("- 203 continuous daily-biomarker rows through 2026-08-30", "- continuous daily-biomarker dates across the represented interval")
ver = ver.replace("- 325 protected v1 training-session rows", "- the protected 325-session historical training prefix through 2026-08-30")
ver = ver.replace("- 325 unique training `session_id` values", "- unique training `session_id` values across the live appendable dataset")
ver = ver.replace("- 42 unique context-event IDs", "- unique context-event IDs across the current event index")
ver = ver.replace(
    "The protected 325-session count is intentional for the currently frozen v1 interval through 2026-08-30. A governed future extension must update the dataset and validator together.",
    "The historical training prefix through 2026-08-30 remains protected at exactly 325 sessions. Governed rows after that boundary may append without changing the protected prefix; the validator reports both prefix and live-row counts.",
)
ver = ver.replace("- all 325 protected v1 training sessions remain present and uniquely identified", "- the protected 325-session training prefix remains present and live session identifiers remain unique")
write("VERIFICATION.md", ver)

W35 = r'''# 2026-W35 — Weekly Report

**Status:** Closed  
**Operating state:** Phase 2 — Load Integration / Consolidation / lock-in observation  
**Observation window:** 2026-08-31 through 2026-09-06

---

## Purpose

This report closes the completed 2026-W35 observation window.

Week 35 preserved the ordinary B1 + Load Integration architecture while tracking recovery variability, bodyweight/intake context, and whether increasingly automatic execution remained available without manufactured challenge or workload escalation.

Interpretation below is retrospective.

---

## Starting State

Week 35 began after a complete ordinary Week 34 with:

- 7 B1 sessions
- 7 Load Integration sessions
- 700 formal training minutes
- approximately 21.14 B1 miles
- increasing automaticity and natural portability
- visible overnight autonomic variability without sustained functional regression
- Model Error 043 still open pending TruDiagnostic provider evidence
- Phase 2D undeclared

The installed physical architecture remained unchanged.

---

## Material Changes From Prior Week

The external workload did not change. The main change was lower apparent management cost of the same work.

Material Week 35 observations:

- 7 B1 + 7 Load Integration sessions completed as prescribed
- 700 formal training minutes completed
- approximately 21.14 B1 miles completed
- B1 remained ambient/background across the week
- Load Integration repeatedly expressed trait-like or trait-level execution
- 2026-09-02 added a deeper low-salience / subjectively trance-like execution observation without creating a new formal execution category
- 2026-09-03 front- and back-yard work occurred between B1 and Load Integration; the prescribed session remained intact and substantial unused workload capacity was reported
- lower reported intake and lower average bodyweight remained background variables without a recovery-directed feeding intervention
- overnight cardiovascular and HRV variability remained visible
- less favorable overnight states did not produce a multi-session functional regression
- no pain, guarding, GI disturbance, or recovery-driven protocol reduction required intervention

A useful descriptive label for the week is **economy**: the same installed workload remained available while requiring less conscious management.

That label is descriptive. It does not declare a phase transition or authorize escalation.

---

## Training Execution

### B1 Aerobic Anchor

**Planned exposure:** 7 sessions  
**Completed exposure:** 7 sessions / 385 minutes / approximately 21.14 miles  
**Execution status:** Preserved

All seven sessions retained the established 55-minute fasted B1 structure.

No B1 session required recovery-driven shortening, pace/incline reduction, graded re-entry, pain-driven modification, respiratory compensation, or abnormal motivational effort.

### Load Integration

**Planned exposure:** 7 sessions  
**Completed exposure:** 7 sessions / 315 minutes  
**Execution status:** Preserved with continued automaticity

The established trap-bar, pull-up, push-up, dead-hang, mobility, and supporting incline-walk structure remained unchanged.

The strongest qualitative observations were:

- **2026-09-02:** deeply embedded, very low-salience execution; classified conservatively as continued trait-like automaticity
- **2026-09-03:** trait-level execution remained available after substantial yard work; perceived reserve capacity increased, but no additional workload was prescribed
- **2026-09-04 through 2026-09-05:** execution remained available across less favorable or mixed overnight recovery signals
- **2026-09-06:** ordinary trait-like execution continued after a strong overnight recovery profile

Reserve capacity was observed rather than spent.

### Recreational and Ordinary-Life Workload

**Material exposure:** 2026-09-03 yard work between B1 and Load Integration.

**Observed effect:** No recovery-driven modification or loss of prescribed execution.

Wearable activity for the week included 89,143 steps and 828 active minutes. Those device-derived activity values remain analytically separate from the 700 minutes of formal B1 + Load Integration.

---

## Recovery and Subjective State

### Recovery posture

- **Mental state:** Calm across the represented week
- **GI/stomach:** Calm
- **Pain/mechanical signals:** None requiring intervention
- **Morning subjective state:** Stable/high readiness context overall
- **Recovery intervention required:** No

### Wearable posture

The week was not autonomically uniform.

Weekly sleep averaged approximately 7h07m, with three nights below seven hours. Sleep HRV averaged 63.0 ms and sleep average heart rate averaged 53.1 bpm.

The clearest mixed profile occurred on 2026-09-05:

- total sleep: 6h32m
- sleep HRV: 73 ms
- sleep average heart rate: 62 bpm

Despite the elevated sleeping heart rate and shorter duration, next-day B1 and Load Integration remained intact. The following night then showed 8h12m total sleep, sleep HRV 69 ms, and sleep average heart rate 48 bpm.

This supports description of variable nocturnal physiology with preserved ordinary function. It does not establish that sleep or autonomic variability is irrelevant.

---

## Structured Weekly Metrics

| Metric | W35 value | Source | Notes |
|---|---:|---|---|
| Morning bodyweight | 232.9 lb average | Daily Biomarkers | 7 days; range 231.1–234.3 lb |
| Daily biomarker HRV | 56.6 ms | Daily Biomarkers | Separate from sleep HRV |
| Resting heart rate | 52.0 bpm | Daily Biomarkers | Weekly average |
| Daily average heart rate | 65.3 bpm | Daily Biomarkers | Weekly average |
| Sleep HRV | 63.0 ms | Sleep Log | Separate from daily HRV |
| Sleep average heart rate | 53.1 bpm | Sleep Log | Weekly average |
| Total sleep | 7h07m | Sleep Log | Nightly average |
| Time in bed | 7h40m | Sleep Log | Nightly average |
| Deep sleep | Approximately 1h19m | Sleep Log | Device-estimated |
| REM sleep | Approximately 50m | Sleep Log | Device-estimated; confidence variable |
| B1 sessions | 7 / 385 min | Training Blocks | Approximately 21.14 miles |
| Load Integration sessions | 7 / 315 min | Training Blocks | Full ordinary architecture |
| Total formal training | 700 min | Training Blocks | B1 + Load Integration |

Week-over-week comparison:

| Marker | W34 | W35 | Direction |
|---|---:|---:|---|
| Morning bodyweight | 233.8 lb | 232.9 lb | Lower |
| Daily biomarker HRV | 59.1 ms | 56.6 ms | Lower |
| Sleep HRV | 65.3 ms | 63.0 ms | Lower |
| Resting heart rate | 49.6 bpm | 52.0 bpm | Higher |
| Sleeping heart rate | 52.0 bpm | 53.1 bpm | Slightly higher |
| Total sleep | 7h24m | 7h07m | Lower |
| Formal training | 700 min | 700 min | Unchanged |

The numerical layer was somewhat less favorable on several weekly averages while the behavioral layer remained stable or became lower-salience.

---

## Perturbations and Deviations

| Date | Event | Observed effect | Resolution |
|---|---|---|---|
| 2026-09-03 | Front/back yard work between B1 and LI | Added ordinary-life physical load; LI remained fully available | Absorbed |
| 2026-09-05 | Shorter sleep with elevated sleeping HR and high sleep HRV | Mixed overnight recovery profile; no next-day protocol modification | Followed by strong overnight recovery on 2026-09-06 |

No material protocol deviation, manufactured portability test, recovery-driven unloading, or compensatory workload occurred.

---

## Bodyweight and Intake Context

Morning bodyweight averaged 232.9 lb, approximately 0.9 lb below Week 34.

Lower caloric intake remained a reported background state. It was not introduced as a recovery intervention, dehydration strategy, autophagy manipulation, or snapshot-directed behavior.

The observed relationship for this window was:

> lower average bodyweight + lower reported intake + complete formal training + preserved mood/GI state + no observed functional regression

This remains descriptive. Short-window scale movement is not treated as direct tissue-composition measurement.

---

## Candidate Model-Error Evidence

### Record 043 — August biological snapshot translation

**Current treatment:** Open / unscored.

The August physical collection is complete. The TruDiagnostic sample was collected, but the required provider-result evidence remains pending.

No Week 35 training, wearable, bodyweight, or subjective observation substitutes for the registered primary TruDiagnostic domain.

No closed model-error record is reopened or rescored.

---

## Governance Review

- **Forced progression introduced:** No
- **Compensatory workload introduced:** No
- **Prediction wording changed:** No
- **Snapshot-directed behavior introduced:** No
- **Unplanned recovery intervention required:** No
- **Premature phase declaration made:** No
- **Source-backed correction performed:** No biological-value correction
- **Unresolved data-quality issue identified:** Private-source date cells used mixed date encodings; public date indices were normalized to ISO calendar dates without changing associated values

Phase 2D remains undeclared.

---

## Weekly Interpretation

Week 35 extends the sequence from recovery and portability toward **task economy**.

The workload stayed the same. What changed was how much active management appeared necessary to produce it.

That distinction matters because the week did not require progression to create a favorable behavioral observation. Automaticity deepened while the protocol remained ordinary, and the most informative reserve-capacity observation was deliberately left unspent.

At the same time, the recovery layer remained variable rather than uniformly favorable. Weekly daily HRV, sleep HRV, resting heart rate, sleeping heart rate, and sleep duration did not all move in a favorable direction. Preserved function therefore should not be rewritten as perfect autonomic stability.

The defensible closeout is narrower:

> The existing B1 + Load Integration architecture remained fully available across a second consecutive complete ordinary week while behavioral execution became increasingly economical despite lower average bodyweight, lower reported intake, and variable overnight physiology.

That is continued consolidation, not a formal phase declaration.

---

## Closeout Decision

**Weekly status:** Closed  
**Protocol decision:** Preserve  
**Recovery decision:** No intervention  
**Model-error decision:** No change; record 043 remains open  
**Phase decision:** No change; Phase 2D remains undeclared

### Closeout rationale

No evidence from Week 35 requires a change to the installed workload. The most useful next observation is whether the same low-overhead organization persists under ordinary life rather than whether additional capacity can be forced into the protocol.

---

## Carryforward to Week 36

Carry forward only:

- ordinary B1 + Load Integration continuity
- persistence of task economy / low-salience execution
- overnight autonomic morphology relative to next-day function
- lower-intake/bodyweight trajectory without deliberate manipulation
- natural portability when ordinary variation occurs
- Model Error 043 pending provider evidence
- Phase 2D undeclared

---

## Source and Correction Notes

Primary private source state for this closeout: `Daniel_Dataset_v1.29`.

The exact retained v1.29 workbook is registered in `data/source_provenance/daniel_dataset_private_manifest.csv` with SHA-256 provenance.

Private workbook date cells used mixed Excel serial and day-of-month encodings. Public daily/session/event dates were normalized to supported ISO dates; associated biological, sleep, and training values were not reconstructed or altered.
'''
write("reports/2026-W35.md", W35)

W36 = r'''# 2026-W36 — Weekly Report

**Status:** Active  
**Operating state:** Phase 2 — Load Integration / Consolidation / lock-in observation  
**Observation window:** 2026-09-07 through 2026-09-13

---

## Purpose

This report records the active 2026-W36 observation window.

Week 36 begins after two consecutive complete ordinary weeks of the installed B1 + Load Integration architecture. Week 35 closed with preserved 700-minute formal training exposure, continued automaticity, lower apparent management cost, variable overnight physiology, and no recovery-driven intervention.

No new perturbation, performance test, recovery intervention, model-error record, or phase transition is introduced at opening.

---

## Starting State

Carryforward state:

- Phase 2 — Load Integration
- operating substate: Consolidation / lock-in observation
- B1 + Load Integration remains the installed architecture
- Week 35 closed with 7 B1 + 7 LI sessions / 700 formal minutes
- task economy / low-salience execution strengthened descriptively
- lower-intake and lower-bodyweight context remains observational
- nocturnal autonomic variability remains visible without a sustained multi-session functional regression
- Model Error 043 remains open pending TruDiagnostic provider evidence
- records 041, 042, 044, 045, and 046 remain closed historical outcomes
- Phase 2D remains undeclared

---

## Week 36 Observation Priorities

Observe ordinary continuity rather than manufacture a stronger demonstration.

Primary questions:

- Does B1 remain background/ambient under the unchanged structure?
- Does Load Integration retain low-salience, trait-like organization without workload escalation?
- Do ordinary schedule, activity, equipment, or attention changes provide natural portability evidence?
- How do overnight HR/HRV patterns relate to next-day initiation, execution, mood, GI state, and ordinary function?
- Does the lower-intake/bodyweight trajectory remain compatible with the installed workload without recovery intervention?

No single wearable value independently determines system state.

---

## Training Posture

Preserve the existing B1 + Load Integration architecture.

Do not add workload solely because reserve capacity was reported in Week 35.

Do not unload solely because of one less-favorable wearable night while multi-domain function remains preserved.

Do not manufacture:

- extra grip testing
- additional dead-hang volume
- high-volume pull-up testing
- artificial equipment disruption
- schedule disruption for portability proof
- compensatory training because bodyweight is lower

Capacity may remain observed without becoming prescribed workload.

---

## Recovery and Bodyweight Boundary

Continue to keep:

- daily HRV distinct from sleep HRV
- resting heart rate distinct from sleep average heart rate
- wearable recovery distinct from demonstrated function
- lower reported intake distinct from a formal intervention
- short-window scale movement distinct from measured tissue composition

No recovery threshold or bodyweight target is preregistered for this weekly window.

---

## Model-Error and Snapshot Boundary

Record 043 remains:

**Open / unscored — TruDiagnostic provider evidence pending.**

August DEXA, VO₂, Bod Pod, bodyweight, wearable recovery, and training performance remain supplemental under the existing registered evaluation framework.

Do not score record 043 until the required primary source evidence is available.

Closed records remain closed.

---

## Governance Review — Active Boundary

During Week 36:

- preserve ordinary exposure
- preserve favorable and unfavorable observations
- do not force progression from favorable execution
- do not rescue or reinterpret closed model-error outcomes
- do not declare Phase 2D from isolated favorable sessions
- register any genuinely new forward prediction before its outcome window if formal evaluation is intended

---

## Closeout Requirements

At closeout, summarize only material deltas, verified weekly metrics, perturbations, governance outcomes, unresolved uncertainty, and carryforward items.

Do not repeat standing methodology merely to increase report length.

---

## Active Observation Summary

The current longitudinal sequence is:

```text
Week 31 — divergence
Week 32 — elasticity
Week 33 — absorption
Week 34 — embedding
Week 35 — economy
Week 36 — ordinary continuity observation
```

These labels are retrospective descriptors, not formal phase declarations.

The next useful evidence remains ordinary life under the unchanged architecture.
'''
write("reports/2026-W36.md", W36)

LATEST = r'''# LATEST — Executive System State

Daniel Longitudinal Study  
Public Archive Status Dashboard

Archive DOI: https://doi.org/10.5281/zenodo.20815612

> Week labels follow the repository’s internal reporting index rather than strict ISO calendar weeks. See [`docs/WEEK_INDEXING.md`](docs/WEEK_INDEXING.md).

---

## Current State

- **Phase:** Phase 2 — Load Integration
- **Operating substate:** Consolidation / lock-in observation
- **Active window:** 2026-W36
- **Prior window:** 2026-W35 closed
- **Installed architecture:** B1 + Load Integration
- **System posture:** Ordinary continuity after two consecutive complete 700-minute training weeks
- **Behavioral posture:** Increasingly economical / low-salience execution under unchanged workload
- **Recovery posture:** Overnight autonomic variability remains visible; weekly averages are not uniformly favorable, while ordinary function has remained preserved across the recently observed window
- **Bodyweight/intake posture:** Lower average bodyweight and lower reported intake remain observational background variables, not a recovery or testing intervention
- **Open model-error record:** 043 — August biological snapshot translation
- **TruDiagnostic status:** Sample collected; provider result required for 043 remains pending
- **Recently closed records:** 041, 042, 044, 045, 046
- **Formal Phase 2D declaration:** None
- **August physical snapshot:** DEXA, VO₂, and Bod Pod collection complete and archived

Current machine-readable row counts and endpoints are maintained in [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md).

---

## Week 35 Closeout

Observation window:

```text
2026-08-31 through 2026-09-06
```

Completed formal training:

- 7 B1 sessions / 385 minutes / approximately 21.14 miles
- 7 Load Integration sessions / 315 minutes
- 700 total formal training minutes

Structured weekly metrics:

| Marker | W35 |
|---|---:|
| Morning bodyweight | 232.9 lb |
| Daily biomarker HRV | 56.6 ms |
| Resting heart rate | 52.0 bpm |
| Daily average heart rate | 65.3 bpm |
| Sleep HRV | 63.0 ms |
| Sleep average heart rate | 53.1 bpm |
| Total sleep | 7h07m |
| Time in bed | 7h40m |
| Deep sleep | approximately 1h19m |
| REM sleep | approximately 50m |

Week 35 did **not** produce uniformly more favorable recovery telemetry. Relative to Week 34, average bodyweight, daily HRV, sleep HRV, and total sleep were lower, while resting and sleeping heart rate were higher.

At the same time, the prescribed behavioral architecture remained fully available.

The strongest qualitative additions were:

- deeper low-salience / subjectively trance-like Load Integration execution on 2026-09-02
- trait-level execution after substantial yard work on 2026-09-03
- visible unused workload capacity without converting that reserve into additional prescribed work
- preserved B1 + LI after mixed or less-favorable overnight recovery profiles
- strong overnight recovery on 2026-09-06 after the shorter/mixed 2026-09-05 sleep profile

The week is therefore best summarized as **task economy under variable physiology**, not perfect autonomic stability.

Full retrospective record: [`reports/2026-W35.md`](reports/2026-W35.md)

---

## Week 36 Operating Posture

Active window:

```text
2026-09-07 through 2026-09-13
```

Week 36 preserves the same B1 + Load Integration architecture.

Observe:

- persistence of low-salience execution
- overnight HR/HRV morphology relative to next-day function
- lower-intake/bodyweight compatibility without deliberate manipulation
- natural portability only when ordinary variation occurs
- any genuine mechanical, GI, mood, or recovery signal requiring action

Do not:

- escalate workload solely because reserve capacity is visible
- unload solely because of one wearable night
- manufacture portability tests
- convert short-window scale movement into a tissue-composition claim
- score record 043 without required TruDiagnostic provider evidence
- declare Phase 2D from isolated favorable sessions

Active report: [`reports/2026-W36.md`](reports/2026-W36.md)

---

## Model-Error State

| Record | Status |
|---|---|
| 041 | Closed / supported |
| 042 | Closed / not supported — continued adaptation |
| 043 | **Open / unscored — provider evidence pending** |
| 044 | Closed / not supported — narrow snapshot-directed governance deviation |
| 045 | Closed / supported |
| 046 | Closed / failed_autonomic_recompression |

Fixed scoring windows remain fixed. Later evidence does not retroactively rescue a failed prediction or reopen a closed record.

---

## Current Verification and Provenance

- read-only core repository validator active
- read-only machine-readable semantic validator active
- GitHub Actions runs both on pushes to `main` and pull requests
- the historical training prefix through 2026-08-30 remains protected at 325 sessions while later governed rows append
- exact retained private-source hashes are registered only when the exact bytes are available
- v1.29 private-source identity is registered in the provenance manifest

Verification guide: [`VERIFICATION.md`](VERIFICATION.md)  
Private-source provenance: [`data/source_provenance/`](data/source_provenance/)  
Current coverage: [`data/DATA_COVERAGE.md`](data/DATA_COVERAGE.md)

---

## Fast Navigation

- [`README.md`](README.md) — archive overview
- [`docs/START_HERE.md`](docs/START_HERE.md) — first-contact orientation
- [`reports/2026-W36.md`](reports/2026-W36.md) — active week
- [`reports/2026-W35.md`](reports/2026-W35.md) — most recent closed week
- [`INDEX.md`](INDEX.md) — complete repository map

The current governing posture remains observation under an unchanged architecture.
'''
write("LATEST.md", LATEST)

README_STATE = r'''# Current Archive State

Current declared state:

```text
Phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Active weekly window:
2026-W36

Most recent closed window:
2026-W35

Open model-error record:
043

Recently closed:
041 — supported
042 — not supported / continued_adaptation
044 — not supported / narrow governance deviation
045 — supported
046 — not supported / failed_autonomic_recompression

August physical snapshot:
complete

August TruDiagnostic provider results:
pending

Formal Phase 2D declaration:
none
```

The installed physical architecture remains:

```text
B1
+
Load Integration
```

For current biological, training, recovery, and report details, use [`LATEST.md`](./LATEST.md).

---
'''
README_CORE = r'''# Machine-Readable Core

The public archive contains an aligned daily/session/event layer:

| Dataset | Unit |
|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | one row per represented day |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | one canonical governed wake-date row |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | one row per training/session block |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | one row per bounded contextual event |

**Live row counts and coverage endpoints are maintained in one place:** [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md).

The daily/training/event datasets are curated public extracts derived primarily from governed private `Daniel_Dataset_v1.x` source states. They are not raw provider exports.

Schema: [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)  
Private-source provenance: [`data/source_provenance/`](./data/source_provenance/)

---
'''
replace_section("README.md", "# Current Archive State", "# Machine-Readable Core", README_STATE)
replace_section("README.md", "# Machine-Readable Core", "# Evidence Architecture", README_CORE)

INDEX_STATE = r'''# Current State

```text
Active phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Active weekly window:
2026-W36

Most recent closed window:
2026-W35

Open model-error record:
043

Recently closed:
041, 042, 044, 045, 046

Formal Phase 2D:
undeclared

August physical snapshot:
complete

August TruDiagnostic provider results:
pending
```

Current state source: [`LATEST.md`](./LATEST.md)

---
'''
INDEX_CORE = r'''# Machine-Readable Core

The structured public layer is:

| Dataset | Role |
|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | daily physiology + bounded subjective state |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | canonical sleep |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | session-level training exposure |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | bounded contextual/perturbation events |
| [`data/model_error/model_error_gap_v1.csv`](./data/model_error/model_error_gap_v1.csv) | prediction → outcome → error |

Live row counts/endpoints: [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md)  
Schema: [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)  
Definitions: [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md)  
Quality notes: [`data/DATA_QUALITY_NOTES.md`](./data/DATA_QUALITY_NOTES.md)

---
'''
INDEX_REPORTS = r'''# Reports

- [`reports/README.md`](./reports/README.md) — report lifecycle
- [`reports/2026-W36.md`](./reports/2026-W36.md) — current active report
- [`reports/2026-W35.md`](./reports/2026-W35.md) — most recent closed report
- [`reports/2026-W34.md`](./reports/2026-W34.md) — prior ordinary continuity window
- [`reports/2026-W33.md`](./reports/2026-W33.md) — August testing/reload window
- [`reports/`](./reports/) — full weekly report series

Reports interpret recorded evidence. They do not replace source artifacts or canonical datasets.

---
'''
replace_section("INDEX.md", "# Current State", "# Machine-Readable Core", INDEX_STATE)
replace_section("INDEX.md", "# Machine-Readable Core", "# Provenance", INDEX_CORE)
replace_section("INDEX.md", "# Reports", "# Prediction and Model-Error Layer", INDEX_REPORTS)

DATASET_CORE = r'''## Current Public Machine-Readable Core

The September 2026 structured-data expansion created an aligned daily/session/event layer from governed source material.

| Dataset | Unit of observation |
|---|---|
| [`data/daily_biomarkers_v1.csv`](./data/daily_biomarkers_v1.csv) | one row per represented day |
| [`data/sleep_longitudinal_v1.csv`](./data/sleep_longitudinal_v1.csv) | one canonical governed wake-date row |
| [`data/training_blocks_v1.csv`](./data/training_blocks_v1.csv) | one row per training/session block |
| [`data/context_events_v1.csv`](./data/context_events_v1.csv) | one row per bounded contextual event |

Current row counts and coverage endpoints are maintained in [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md), rather than duplicated across orientation documents.

The newer datasets are curated public extracts derived primarily from private `Daniel_Dataset_v1.x` source states and governed contemporaneous evidence. They are not raw provider exports.

Schema contract: [`schemas/machine-readable-layer-v1.md`](./schemas/machine-readable-layer-v1.md)  
Private-source identity: [`data/source_provenance/daniel_dataset_private_manifest.csv`](./data/source_provenance/daniel_dataset_private_manifest.csv)

---
'''
replace_section("DATASET_OVERVIEW.md", "## Current Public Machine-Readable Core", "## Study Scope", DATASET_CORE)
text = read("DATASET_OVERVIEW.md")
text = text.replace(
    "All 325 current training rows now use the canonical `private_workbook:` / `private_pdf:` source-reference grammar. Earlier `wb:v...` / `pdf:v...` aliases remain visible in Git history only.",
    "The protected historical training prefix contains 325 sessions through 2026-08-30. All live training rows use the canonical `private_workbook:` / `private_pdf:` source-reference grammar; later governed rows append without changing that protected prefix. Earlier `wb:v...` / `pdf:v...` aliases remain visible in Git history only.",
)
write("DATASET_OVERVIEW.md", text)

DICT_CORE = r'''# Machine-Readable Core

The aligned public structured layer currently includes:

```text
daily biomarkers
+
canonical sleep
+
training sessions
+
context events
+
model-error outcomes
```

Current row counts and coverage endpoints are maintained in [`data/DATA_COVERAGE.md`](./data/DATA_COVERAGE.md).

These files have different units of observation and are not row-for-row equivalent.

---
'''
replace_section("DATA_DICTIONARY.md", "# Machine-Readable Core", "# Field Evidence Classes", DICT_CORE)

START_CORE = r'''## Machine-Readable Core

The current aligned structured layer includes:

- [`data/daily_biomarkers_v1.csv`](../data/daily_biomarkers_v1.csv)
- [`data/sleep_longitudinal_v1.csv`](../data/sleep_longitudinal_v1.csv)
- [`data/training_blocks_v1.csv`](../data/training_blocks_v1.csv)
- [`data/context_events_v1.csv`](../data/context_events_v1.csv)

Live row counts and coverage endpoints are maintained in [`data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

Schema: [`schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md)  
Private-source provenance: [`data/source_provenance/`](../data/source_provenance/)

---
'''
replace_section("docs/START_HERE.md", "## Machine-Readable Core", "## Where The Evidence Lives", START_CORE)

FOR_CORE = r'''## Current Machine-Readable Core

The current public structured layer contains:

- [`daily_biomarkers_v1.csv`](../data/daily_biomarkers_v1.csv)
- [`sleep_longitudinal_v1.csv`](../data/sleep_longitudinal_v1.csv)
- [`training_blocks_v1.csv`](../data/training_blocks_v1.csv)
- [`context_events_v1.csv`](../data/context_events_v1.csv)

Live row counts and coverage endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md). The schema is defined in [`../schemas/machine-readable-layer-v1.md`](../schemas/machine-readable-layer-v1.md).

This materially improves machine readability, but it does not make the archive exhaustive or experimentally controlled.

---
'''
replace_section("docs/FOR_OBSERVERS.md", "## Current Machine-Readable Core", "## Governing Distinctions", FOR_CORE)

replace_once(
    "docs/NEWCOMER_PATH.md",
    "The current aligned interval includes 203 daily biomarker rows, 203 canonical sleep rows, 325 training-session rows, and 42 context-event rows.",
    "Current row counts and coverage endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md) rather than repeated here.",
)
replace_once("docs/NEWCOMER_PATH.md", "[`../reports/2026-W34.md`](../reports/2026-W34.md)", "[`../reports/2026-W35.md`](../reports/2026-W35.md)")

replace_once(
    "docs/OBSERVER_QUICKSTART.md",
    "Current public coverage includes 203 aligned daily biomarker rows, 203 canonical sleep rows, 325 training-session rows, and 42 bounded context-event rows across the current represented interval.",
    "Use [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md) for current row counts and endpoints; they are intentionally not duplicated here.",
)
replace_once("docs/OBSERVER_QUICKSTART.md", "[`../reports/2026-W34.md`](../reports/2026-W34.md)", "[`../reports/2026-W35.md`](../reports/2026-W35.md)")

CONCEPT_TAIL = r'''# Current Terminology State

As of the current September 2026 archive state:

```text
Active phase:
Phase 2 — Load Integration

Operating substate:
Consolidation / lock-in observation

Phase 2D:
undeclared

Current open model-error record:
043

Recently closed model-error records:
041, 042, 044, 045, 046

UDI canonical name:
Unobstructed Delta Index
```

Current machine-readable row counts and endpoints are maintained in [`../data/DATA_COVERAGE.md`](../data/DATA_COVERAGE.md).

Historical documents may retain terminology that was correct for their original date/state.

Current-facing documents should use the definitions in this glossary and the governing schema/methodology files.
'''
replace_tail("docs/CONCEPTS.md", "# Current Terminology State", CONCEPT_TAIL)

method = read("methodology/README.md")
method = method.replace("Current weekly window:\n2026-W35", "Current weekly window:\n2026-W36", 1)
method = method.replace("Most recent closed weekly window:\n2026-W34", "Most recent closed weekly window:\n2026-W35", 1)
method = method.replace("Canonical sleep:\nContinuous through 2026-08-30", "Canonical sleep:\nCurrent endpoint: see `../data/DATA_COVERAGE.md`", 1)
write("methodology/README.md", method)

changelog = read("CHANGELOG.md")
entry_heading = "#### September 7 W35 closeout and W36 initialization"
if entry_heading not in changelog:
    anchor = "## [Unreleased]\n"
    pos = changelog.find(anchor)
    if pos < 0:
        raise SystemExit("CHANGELOG.md: Unreleased anchor missing")
    insert_at = pos + len(anchor)
    entry = r'''

### Changed

#### September 7 W35 closeout and W36 initialization

- Extended the public machine-readable layer through the completed `2026-W35` window using retained `Daniel_Dataset_v1.29` source material.
- Added 7 daily-biomarker rows and 7 canonical sleep rows through `2026-09-06`.
- Added 14 training-session rows through `2026-09-06`, preserving the unchanged 7 B1 + 7 Load Integration architecture.
- Added two selective context-event rows for 2026-09-02 automaticity deepening and 2026-09-03 yard-work exposure.
- Registered the exact retained `Daniel_Dataset_v1.29` workbook in the private-source manifest with file size and SHA-256 identity.
- Replaced the validator's fixed live total of 325 training rows with a protected-prefix rule: exactly 325 historical sessions remain required through `2026-08-30`, while later governed rows may append.
- Closed `reports/2026-W35.md` and opened lean active `reports/2026-W36.md` for `2026-09-07` through `2026-09-13`.
- Advanced `LATEST.md`, `README.md`, and `INDEX.md` to W36 / W35 state.
- Centralized volatile machine-readable row counts and endpoints in `data/DATA_COVERAGE.md`; current-facing orientation, glossary, schema, dictionary, and observer documents now link to that canonical coverage surface instead of repeating counts.
- Preserved continuous canonical CSVs rather than splitting them by week or month.
- Shortened `LATEST.md` back toward dashboard scope and kept detailed W35 interpretation in the weekly report.
- Archived August-31-and-earlier live-changelog detail into `docs/archive/CHANGELOG_ARCHIVE.md` to keep the root changelog operationally current.

Classification:

```text
Biological source-value reconstruction:
No

Canonical sleep extension:
Yes — source-backed append only

Training architecture change:
No

Prediction wording or outcome change:
No

Phase or protocol change:
No

Release or DOI change:
No

Repository/data maintenance:
Yes
```
'''
    changelog = changelog[:insert_at] + entry + changelog[insert_at:]

archive_anchor = "#### August 31 Week 34 closeout and Week 35 initialization"
archive_marker = "## Archived from root changelog on 2026-09-07 — August 31 and earlier"
if archive_anchor in changelog:
    split_at = changelog.index(archive_anchor)
    historical = changelog[split_at:].rstrip() + "\n"
    changelog = changelog[:split_at].rstrip() + "\n"
    archive = read("docs/archive/CHANGELOG_ARCHIVE.md")
    if archive_marker not in archive:
        archive = archive.rstrip() + "\n\n---\n\n" + archive_marker + "\n\n" + historical
        write("docs/archive/CHANGELOG_ARCHIVE.md", archive)
write("CHANGELOG.md", changelog)


def csv_rows(path: str) -> list[dict[str, str]]:
    with Path(path).open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

assert len(csv_rows("data/daily_biomarkers_v1.csv")) == 210
assert len(csv_rows("data/sleep_longitudinal_v1.csv")) == 210
assert len(csv_rows("data/training_blocks_v1.csv")) == 339
assert len(csv_rows("data/context_events_v1.csv")) == 44
assert csv_rows("data/daily_biomarkers_v1.csv")[-1]["date"] == "2026-09-06"
assert csv_rows("data/sleep_longitudinal_v1.csv")[-1]["date"] == "2026-09-06"
assert csv_rows("data/training_blocks_v1.csv")[-1]["session_id"] == "2026-09-06-LI"
assert csv_rows("data/context_events_v1.csv")[-1]["event_id"] == "2026-09-03-01"
assert "2026-W36" in read("LATEST.md")
assert "**Status:** Closed" in read("reports/2026-W35.md")
assert "**Status:** Active" in read("reports/2026-W36.md")

current_faces = [
    "README.md", "INDEX.md", "LATEST.md", "DATASET_OVERVIEW.md", "DATA_DICTIONARY.md",
    "docs/START_HERE.md", "docs/FOR_OBSERVERS.md", "docs/NEWCOMER_PATH.md",
    "docs/OBSERVER_QUICKSTART.md", "docs/CONCEPTS.md", "schemas/machine-readable-layer-v1.md",
]
for path in current_faces:
    text = read(path)
    if "203 continuous" in text or "325 sessions through 2026-08-30" in text or "42 bounded events through 2026-08-29" in text:
        raise SystemExit(f"{path}: volatile historical coverage count remains on current-facing surface")

print("W35 -> W36 rollover files prepared")
