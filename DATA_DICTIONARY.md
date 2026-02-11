# Data Dictionary

This document defines measurement terms and logging rules used in this repository.

All definitions prioritize repeatability and longitudinal comparability.

---

## Global Conventions

### Dates
- Format: `YYYY-MM-DD`
- If capture spans multiple days, use the collection/capture date.

### Time
- Local timezone: America/New_York
- If time is relevant, record in 24h format: `HH:MM`

### Units
- Weight: pounds (lb)
- Time: minutes (min)
- Speed: miles per hour (mph)
- Incline: percent (%)
- Temperature: Fahrenheit (°F)
- Distance: miles (mi) unless otherwise noted

---

## Capture States

### Fasted
Defined as:
- No caloric intake for ≥ 10 hours prior to capture
- Water permitted
- Electrolytes permitted only if non-caloric and normal routine
- Caffeine and stimulants must be logged if used (prefer none prior to capture)

### Normal Operating Conditions
Defined as:
- No dehydration protocol
- No sodium manipulation for cosmetic effect
- No acute glycogen depletion strategy
- No protocol changes intended to influence the capture

If any deviation occurs, it must be recorded in the associated report notes.

---

## Body Composition Terms

### DEXA Total Mass
- Definition: Total body mass measured by DEXA at time of scan
- Unit: lb

### DEXA Lean Mass
- Definition: Lean soft tissue mass reported by DEXA (excludes fat mass; bone mineral is reported separately)
- Unit: lb
- Notes:
  - Can vary with glycogen and hydration state
  - Interpret longitudinally

### DEXA Fat Mass
- Definition: Total fat mass reported by DEXA
- Unit: lb

### DEXA Body Fat %
- Definition: Percent body fat reported by DEXA
- Unit: %

### DEXA Bone Mineral Content (BMC)
- Definition: Bone mineral content reported by DEXA
- Unit: lb (or g depending on report; record as given)

### DEXA Bone Mineral Density (BMD)
- Definition: Bone mineral density reported by DEXA
- Unit: g/cm² (record as given)

### DEXA Visceral Fat
- Definition: Visceral fat metric reported by DEXA (unit depends on provider output)
- Unit: record exactly as reported (e.g., lb, area, or proprietary score)

### Bod Pod Body Fat %
- Definition: Percent body fat estimated via air displacement plethysmography
- Unit: %

### Bod Pod Fat Mass
- Definition: Fat mass estimated by Bod Pod
- Unit: lb

### Bod Pod Fat-Free Mass (FFM)
- Definition: All non-fat mass estimated by Bod Pod (includes water, bone, organs, muscle)
- Unit: lb
- Notes:
  - Not equivalent to DEXA lean mass
  - Hydration-sensitive; interpret with capture conditions

---

## Training Terms

### B-Blocks
Internal naming convention for training modules. Logged as executed.

#### B1 (Incline Treadmill)
- Definition: Incline treadmill session
- Logged fields:
  - Duration (min)
  - Incline (%)
  - Speed (mph)
- Example:
  - `B1: 52m | 10% | 3.3`

#### B3 / B4 (Locomotion / Structural Circuits)
- Definition: Turf or floor circuits emphasizing locomotion and structural integrity
- Logged as:
  - Circuit count
  - Movements + counts (or distance/time if applicable)
- Examples:
  - `B3: Rope 50 | Goblet x3 (deep pause)`
  - `B4: Bear F/B/L/R | Crab F/B`

### Circuits
- Definition: One complete pass through the defined movement sequence
- Unit: count (#)

---

## Recovery / Physiology Terms

### HR (Heart Rate)
- Definition: Heart rate measured by wearable or validated device
- Unit: bpm
- If multiple readings exist, specify:
  - resting (upon waking) vs active

### HRV
- Definition: Heart rate variability metric as reported by wearable/device
- Unit: device-defined (often ms)
- Notes:
  - Record device/source when possible
  - Compare within the same device ecosystem

### Steps
- Definition: Total daily step count
- Unit: count (#)
- Source: wearable/app reported value

### Active Calories
- Definition: Estimated active energy expenditure from wearable/app
- Unit: kcal
- Note: Device estimates vary; use trend only within same system

---

## Files and Naming

### Snapshots
- Location: `/snapshots/YYYY-MM/`
- Naming: `YYYY-MM-DD_<capture>_<source>.md` (or `.pdf/.jpg` as applicable)
- Examples:
  - `2026-02-12_dexa_summary.pdf`
  - `2026-02-12_bodpod_results.jpg`

### Reports
- Location: `/reports/`
- Naming: `YYYY-MM_<capture>-report.md`
- Example:
  - `2026-02_dexa-report.md`

### Current State
- File: `LATEST.md`
- Updated weekly or upon material capture

---

## Change Control

If any definition changes:
- Update this file
- Log the change in `CHANGELOG.md`
- Increment version according to `VERSIONING.md`
