# Record 043 — August 2026 Biological Translation Closure

**Record:** 043  
**Domain:** `biological_translation`  
**Prediction type:** trajectory  
**Registration date:** 2026-06-25  
**Primary biological endpoint:** 2026-08-17  
**Snapshot-cycle completion date:** 2026-08-18  
**Closure date:** 2026-09-10  
**Final status:** closed / not supported  
**Error direction:** over

---

## Original Prediction

> Prediction: The August 2026 biological snapshot will demonstrate measurable improvement relative to May 2026 across the overall physiological profile, but the magnitude of improvement will be smaller than the February-to-May interval. This tests whether prolonged protocol stability continues translating into measurable biological adaptation while probing calibration after prior conservative underestimation.

The registered prediction text remains unchanged in `model_error_gap_v1.csv`.

---

## Governing Evaluation Plan

Record 043 is evaluated under:

[`../../methodology/open_prediction_evaluation_plan_041_044.md`](../../methodology/open_prediction_evaluation_plan_041_044.md)

The preregistered overall-improvement rule requires all of the following:

1. at least two of the three core biological anchors improve beyond their operational thresholds
2. any remaining core anchor is stable or improved
3. at least 60% of directly comparable supporting metrics are stable or improved
4. neither the system-age group nor the TruHealth group shows a majority of materially adverse changes
5. no source-quality or comparability issue invalidates the primary comparison

The prediction is supported only when that overall-improvement rule is met and the median core-anchor improvement ratio is greater than 0 but less than 1.0.

Failure through model overestimation applies when the overall-improvement rule is not met, including when improvement is too narrow to qualify as overall physiological improvement or the profile materially worsens.

---

## Source and Date Boundary

The August TruDiagnostic biological result set is assigned to the governed primary sample date:

```text
2026-08-17
```

The contemporaneous repository collection record controls the actual sample date/time and preparation conditions. Provider-report headers remain preserved as provider-displayed administrative metadata.

The source-role reconciliation is documented in:

[`../source_provenance/2026-08-trudiagnostic-reconciliation.md`](../source_provenance/2026-08-trudiagnostic-reconciliation.md)

That metadata difference does not alter the biological values used here and does not invalidate the comparison.

Primary structured comparison rows:

- February: `data/biomarker_snapshot.csv` — `2026-02`
- May: `data/biomarker_snapshot.csv` — `2026-05`
- August: `data/biomarker_snapshot.csv` — `2026-08`

Detailed provider-specific rows are preserved in:

- `data/epigenetic_longitudinal.csv`

---

## Core Biological Anchors

| Anchor | Feb | May | Aug | May→Aug change | Registered threshold | Classification |
|---|---:|---:|---:|---:|---:|---|
| OMICm age delta | -1.1 y | -3.7 y | -3.9 y | 0.2 y more favorable | ≥0.5 y more favorable | stable |
| DunedinPACE | 0.88 | 0.79 | 0.77 | 0.02 lower | ≥0.01 lower | improved |
| SymphonyAge | 51.2 y | 37.8 y | 46.1 y | 8.3 y higher | ≥1.0 y lower for improvement | adverse |

Core-anchor result:

```text
improved: 1
stable:   1
adverse:  1
```

Therefore:

- the required minimum of two improving core anchors is not met
- the remaining-anchor condition is also not met because SymphonyAge is materially adverse

The overall-improvement rule already fails at the core-anchor layer.

---

## Supporting System and Organ Ages

Registered material-change threshold:

```text
improvement: decrease of at least 1.0 year
stable:      change smaller than 1.0 year in either direction
adverse:     increase of at least 1.0 year
```

| System age | May | Aug | Change | Classification |
|---|---:|---:|---:|---|
| Blood | 40.2 | 44.3 | +4.1 | adverse |
| Brain | 38.2 | 44.0 | +5.8 | adverse |
| Inflammation | 39.9 | 41.3 | +1.4 | adverse |
| Heart | 37.6 | 46.2 | +8.6 | adverse |
| Hormone | 33.1 | 36.0 | +2.9 | adverse |
| Immune | 43.4 | 44.7 | +1.3 | adverse |
| Kidney | 40.5 | 46.4 | +5.9 | adverse |
| Liver | 37.0 | 43.8 | +6.8 | adverse |
| Metabolic | 35.0 | 43.1 | +8.1 | adverse |
| Lung | 39.5 | 47.1 | +7.6 | adverse |
| Musculoskeletal | 35.5 | 40.1 | +4.6 | adverse |

System-age result:

```text
improved: 0
stable:   0
adverse: 11
```

The system-age group therefore shows a material adverse majority and independently fails the registered group-level condition.

---

## Supporting TruHealth Domains

Registered material-change threshold:

```text
improvement: increase of at least 5 points
stable:      change smaller than 5 points in either direction
adverse:     decrease of at least 5 points
```

| TruHealth domain | May | Aug | Change | Classification |
|---|---:|---:|---:|---|
| Vitamins | 63 | 58 | -5 | adverse |
| Amino acids | 60 | 68 | +8 | improved |
| Antioxidants | 53 | 59 | +6 | improved |
| Fats / membranes | 54 | 56 | +2 | stable |
| Lipid peroxidation | 35 | 47 | +12 | improved |
| Serum lipids | 57 | 73 | +16 | improved |
| Blood pressure | 62 | 55 | -7 | adverse |
| Metabolic | 57 | 52 | -5 | adverse |
| Immune | 56 | 70 | +14 | improved |
| Neurocognitive | 48 | 71 | +23 | improved |
| Inflammation | 80 | 79 | -1 | stable |
| Stress | 61 | 40 | -21 | adverse |
| Toxins | 25 | 41 | +16 | improved |
| Uric-acid pathway | 68 | 51 | -17 | adverse |
| Mitochondrial function | 78 | 39 | -39 | adverse |
| Oxidative defense | 64 | 66 | +2 | stable |
| NAD metabolism | 62 | 35 | -27 | adverse |
| Ketones | 47 | 34 | -13 | adverse |
| Supplements | 51 | 67 | +16 | improved |

TruHealth-domain result:

```text
improved: 8
stable:   3
adverse:  8
```

The TruHealth group does not show a majority of adverse changes.

However, only 11 of 19 TruHealth domains are stable or improved.

---

## Combined Supporting-Metric Rule

The directly comparable supporting profile contains:

```text
11 system/organ ages
19 TruHealth domains
30 supporting metrics total
```

Stable or improved:

```text
system/organ ages: 0 of 11
TruHealth domains: 11 of 19
combined:          11 of 30 = 36.7%
```

Registered requirement:

```text
at least 60% stable or improved
```

Observed:

```text
36.7%
```

The supporting-profile percentage rule therefore fails.

---

## Magnitude Context

The February-to-May core-anchor reference changes were preregistered as:

- OMICm age delta: 2.6 years more favorable
- DunedinPACE: 0.09 lower
- SymphonyAge: 13.4 years lower

From May to August:

- OMICm moved 0.2 years in the favorable direction, below the 0.5-year improvement threshold and therefore classified as stable
- DunedinPACE improved by 0.02
- SymphonyAge moved 8.3 years in the adverse direction

Because the overall-improvement rule fails, the smaller-than-February-to-May magnitude clause cannot rescue the prediction. The formal closure therefore does not depend on selecting a favorable subset of anchor ratios.

---

## Supplemental Measurement Boundary

DEXA, Bod Pod, VO₂, bodyweight, and recovery telemetry are supplemental under the registered plan.

They cannot rescue failure of the core biological-aging comparison and are not included in the 60% supporting-profile rule.

The August DEXA row is preserved in `data/biomarker_snapshot.csv`. The August Bod Pod collection date is preserved, while its numeric structured fields remain blank pending direct source transcription. This missing supplemental transcription does not prevent record 043 closure because the registered core and supporting TruDiagnostic comparison is sufficient and directly comparable.

---

## Formal Adjudication

The August profile does **not** satisfy the preregistered definition of measurable overall improvement relative to May.

The failure is not based on one unfavorable marker. It is driven by multiple independent registered conditions:

- only 1 of 3 core anchors materially improved
- SymphonyAge materially worsened
- 11 of 11 system/organ ages materially worsened under the registered threshold
- only 36.7% of the full supporting profile was stable or improved, below the required 60%
- the system-age group contained a material adverse majority

At the same time, favorable evidence remains preserved:

- DunedinPACE improved from 0.79 to 0.77
- OMICm age delta moved slightly more favorable but remained within the registered stable band
- 8 of 19 TruHealth domains materially improved
- 3 additional TruHealth domains remained stable

Those favorable signals are real within the provider outputs but are too narrow to satisfy the locked overall-improvement rule.

Final disposition:

```text
prediction:      moderate_improvement
actual:          overall_improvement_not_met
status:          closed
support:         not supported
error_direction: over
```

`over` means the model overestimated the breadth of August biological improvement relative to the preregistered overall-profile requirement.

This closure does not establish biological deterioration as a generalized causal conclusion, does not infer why the provider metrics moved, and does not change Phase 2 status or declare Phase 2D.
