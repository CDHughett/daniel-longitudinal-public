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
- Energy expenditure: kilocalories per day (kcal/day)
- Biological age outputs: years
- Percentile-based scores: percentile (0-100)
- Pace-of-aging outputs: ratio

---

## biomarker_snapshot.csv fields

### date
- Snapshot month in `YYYY-MM` format.
- Example: `2026-02`

### source
- Indicates the row is a fused snapshot compiled from multiple artifacts.
- Expected value: `integrated`

### dexa_date
- Date of the DEXA artifact used for this snapshot.
- Format: `YYYY-MM-DD`

### bodpod_date
- Date of the BodPod artifact used for this snapshot.
- Format: `YYYY-MM-DD`

### chronological_age
- Calendar age at time of testing.
- Unit: years

### omicm_age
- TruAge OMICm biological age output.
- Unit: years

### omicm_age_delta_years
- Difference between `omicm_age` and `chronological_age`.
- Unit: years
- Negative values indicate OMICm age below chronological age.

### dunedin_pace
- DunedinPACE rate-of-aging output.
- Unit: ratio
- Interpretation: `1.0` = aging one biological year per chronological year; values below `1.0` indicate slower aging pace.

### symphony_age
- Composite SYMPHONY organ-system age output.
- Unit: years

### blood_age
- SYMPHONY blood system age.
- Unit: years

### brain_age
- SYMPHONY brain system age.
- Unit: years

### inflammation_age
- SYMPHONY inflammation system age.
- Unit: years

### heart_age
- SYMPHONY heart system age.
- Unit: years

### hormone_age
- SYMPHONY hormone system age.
- Unit: years

### immune_age
- SYMPHONY immune system age.
- Unit: years

### kidney_age
- SYMPHONY kidney system age.
- Unit: years

### liver_age
- SYMPHONY liver system age.
- Unit: years

### metabolic_age
- SYMPHONY metabolic system age.
- Unit: years

### lung_age
- SYMPHONY lung system age.
- Unit: years

### musculoskeletal_age
- SYMPHONY musculoskeletal system age.
- Unit: years

### body_score
- DEXA summary body score grade.
- Unit: categorical
- Example: `A`

### total_mass_lbs
- Total body mass from DEXA.
- Unit: pounds

### body_fat_pct_dexa
- Body fat percentage from DEXA.
- Unit: percent

### fat_mass_lbs_dexa
- Fat mass from DEXA.
- Unit: pounds

### lean_mass_lbs_dexa
- Lean mass from DEXA.
- Unit: pounds

### visceral_fat_lbs
- Visceral fat estimate from DEXA.
- Unit: pounds

### t_score
- Bone density T-score from DEXA.
- Unit: score

### bodpod_body_fat_pct
- Body fat percentage from BodPod.
- Unit: percent

### bodpod_fat_mass_lbs
- Fat mass from BodPod.
- Unit: pounds

### bodpod_ffm_lbs
- Fat-free mass from BodPod.
- Unit: pounds

### bodpod_body_mass_lbs
- Body mass from BodPod.
- Unit: pounds

### bodpod_ree_kcal_day
- Resting energy expenditure from BodPod/COSMED output.
- Unit: kcal/day

### bodpod_tee_kcal_day
- Total energy expenditure from BodPod/COSMED output.
- Unit: kcal/day

### truhealth_vitamins_score
- TruHealth nutrition domain percentile for vitamins.
- Unit: percentile (0-100)

### truhealth_amino_acids_score
- TruHealth nutrition domain percentile for amino acids.
- Unit: percentile (0-100)

### truhealth_antioxidants_score
- TruHealth nutrition domain percentile for antioxidants.
- Unit: percentile (0-100)

### truhealth_fats_membranes_score
- TruHealth nutrition domain percentile for fats and cellular membranes.
- Unit: percentile (0-100)

### truhealth_lipid_peroxidation_score
- TruHealth general health domain percentile for lipid peroxidation.
- Unit: percentile (0-100)

### truhealth_serum_lipids_score
- TruHealth general health domain percentile for serum lipids.
- Unit: percentile (0-100)

### truhealth_blood_pressure_score
- TruHealth general health domain percentile for blood pressure-related markers.
- Unit: percentile (0-100)

### truhealth_metabolic_score
- TruHealth general health domain percentile for metabolic markers.
- Unit: percentile (0-100)

### truhealth_immune_score
- TruHealth general health domain percentile for immune markers.
- Unit: percentile (0-100)

### truhealth_neurocognitive_score
- TruHealth general health domain percentile for neurocognitive markers.
- Unit: percentile (0-100)

### truhealth_inflammation_score
- TruHealth general health domain percentile for inflammation markers.
- Unit: percentile (0-100)

### truhealth_stress_score
- TruHealth general health domain percentile for stress markers.
- Unit: percentile (0-100)

### truhealth_toxins_score
- TruHealth general health domain percentile for toxins-related markers.
- Unit: percentile (0-100)

### truhealth_uric_acid_pathway_score
- TruHealth general health domain percentile for uric acid pathway markers.
- Unit: percentile (0-100)

### truhealth_mitochondrial_function_score
- TruHealth general health domain percentile for mitochondrial function.
- Unit: percentile (0-100)

### truhealth_oxidative_defense_score
- TruHealth general health domain percentile for oxidative defense.
- Unit: percentile (0-100)

### truhealth_nad_metabolism_score
- TruHealth general health domain percentile for NAD+ metabolism.
- Unit: percentile (0-100)

### truhealth_ketones_score
- TruHealth general health domain percentile for ketone-related markers.
- Unit: percentile (0-100)

### truhealth_supplements_score
- TruHealth general health domain percentile for supplement-related biomarker patterning.
- Unit: percentile (0-100)

### notes
- Free-text context for the snapshot row.
- Used to identify source scope, caveats, or integration notes.

---

## epigenetic_longitudinal.csv fields

### date
- Capture date of the epigenetic test result.
- Format: `YYYY-MM-DD`

### domain
- Broad grouping of the result.
- Examples:
  - `aging`
  - `organ_age`
  - `truhealth_domain`
  - `truhealth_marker`

### biomarker
- Machine-readable biomarker or output name.
- Examples:
  - `omicm_age`
  - `dunedin_pace`
  - `blood_age`
  - `ldl_c`
  - `pfos`

### value
- Numeric result value as reported or derived from source artifact.
- Unit depends on field context.

### unit
- Measurement unit for the value.
- Examples:
  - `years`
  - `ratio`
  - `percentile`

### status
- Interpretation category associated with the value.
- Examples:
  - `normal`
  - `suboptimal`
  - `high`
  - `high_warning`
  - `low`
  - `reference`

### source
- Report source used for the row.
- Expected values:
  - `TruAge`
  - `Advanced_TruAge`
  - `TruHealth`

### notes
- Free-text context, caveats, or interpretation notes for the row.

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
- Location: `/snapshots/`
- Structure:
  - May include both flat files and subdirectories
  - Legacy formats are preserved for historical continuity

- Preferred Naming:
  `YYYY-MM-DD_<capture>_<source>.<ext>`

- Examples:
  - `2026-02-12_dexa_summary.pdf`
  - `2026-02-12_bodpod_results.jpg`

Note:
Snapshot structure has evolved over time.  
The repository preserves historical formats rather than enforcing retroactive restructuring.

### Reports

The repository supports two report classes:

#### 1. Weekly Reports (Primary)
- Location: `/reports/`
- Naming: `YYYY-W##.md`
- Example:
  - `2026-W11.md`

#### 2. Capture Reports (Event-Specific)
- Location: `/reports/`
- Naming: `YYYY-MM_<capture>-report.md`
- Example:
  - `2025-11_dexa-report.md`

Weekly reports are the dominant and expected format.  
Capture reports are used selectively for discrete measurement events.

### Current State
- File: `LATEST.md`
- Updated weekly or upon material capture

---

## Change Control

If any definition changes:
- Update this file
- Log the change in `CHANGELOG.md`
- Increment version according to `VERSIONING.md`
