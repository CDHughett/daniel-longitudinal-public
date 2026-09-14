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

## Preservation note

This is the current canonical closure record. The complete closure text as committed at adjudication is preserved byte-for-byte at [`archive/record_043_closure_2026-09-10.txt`](./archive/record_043_closure_2026-09-10.txt).

A later source-backed cleanup completed the supplemental August Bod Pod structured fields. That post-closure completion does **not** reopen, rescore, or alter Record 043 because Bod Pod was supplemental under the registered biological-translation plan.

---

## Original prediction

> Prediction: The August 2026 biological snapshot will demonstrate measurable improvement relative to May 2026 across the overall physiological profile, but the magnitude of improvement will be smaller than the February-to-May interval. This tests whether prolonged protocol stability continues translating into measurable biological adaptation while probing calibration after prior conservative underestimation.

The registered prediction text remains unchanged in `model_error_gap_v1.csv`.

---

## Governing evaluation plan

Record 043 is evaluated under [`../../methodology/open_prediction_evaluation_plan_041_044.md`](../../methodology/open_prediction_evaluation_plan_041_044.md).

The preregistered overall-improvement rule required all of the following:

1. at least two of the three core biological anchors improve beyond their operational thresholds
2. any remaining core anchor is stable or improved
3. at least 60% of directly comparable supporting metrics are stable or improved
4. neither the system-age group nor the TruHealth group shows a majority of materially adverse changes
5. no source-quality or comparability issue invalidates the primary comparison

The prediction was supported only if that rule was met and the median core-anchor improvement ratio was greater than 0 but less than 1.0.

---

## Source and date boundary

The August TruDiagnostic biological result set is assigned to the governed primary sample date `2026-08-17`. The contemporaneous repository collection record controls the actual sample date/time and preparation conditions. Provider-report headers remain preserved as provider-displayed administrative metadata.

Source-role reconciliation: [`../source_provenance/2026-08-trudiagnostic-reconciliation.md`](../source_provenance/2026-08-trudiagnostic-reconciliation.md)

Primary structured comparison rows:

- February: `data/biomarker_snapshot.csv` — `2026-02`
- May: `data/biomarker_snapshot.csv` — `2026-05`
- August: `data/biomarker_snapshot.csv` — `2026-08`

---

## Core biological anchors

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

The required minimum of two improving core anchors was not met, and the remaining-anchor condition also failed because SymphonyAge was materially adverse.

---

## Supporting system and organ ages

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

This group therefore contained a material adverse majority.

---

## Supporting TruHealth domains

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

The group did not show a majority of adverse changes, but only 11 of 19 domains were stable or improved.

---

## Combined supporting-metric rule

The directly comparable supporting profile contained 11 system/organ ages and 19 TruHealth domains.

```text
system/organ ages: 0 of 11 stable or improved
TruHealth domains: 11 of 19 stable or improved
combined:          11 of 30 = 36.7%
registered rule:   at least 60% stable or improved
```

The supporting-profile percentage rule therefore failed.

---

## Supplemental measurement boundary and later completion

DEXA, Bod Pod, VO₂, bodyweight, and recovery telemetry were supplemental under the registered plan and could not rescue failure of the core biological-aging comparison.

At the moment Record 043 was adjudicated, the August DEXA row was structured and the Bod Pod collection date was preserved, while the Bod Pod numeric structured fields had not yet been required or used for scoring. On 2026-09-10, a later governed post-snapshot cleanup directly transcribed the retained COSMED source values into `data/biomarker_snapshot.csv`:

```text
body fat:      11.3%
fat mass:      26.630 lb
fat-free mass: 208.693 lb
body mass:     235.323 lb
REE:           2491 kcal/day
TEE:           4334 kcal/day
TGV model:     Predicted
```

This supplemental completion changes the current archive completeness state only. It does not alter the registered scoring domain, closure date, thresholds, supporting-profile calculation, actual outcome, support status, or error direction for Record 043.

---

## Formal adjudication

The August profile did **not** satisfy the preregistered definition of measurable overall improvement relative to May.

The failure was driven by multiple independent registered conditions:

- only 1 of 3 core anchors materially improved
- SymphonyAge materially worsened
- 11 of 11 system/organ ages materially worsened under the registered threshold
- only 36.7% of the full supporting profile was stable or improved, below the required 60%
- the system-age group contained a material adverse majority

Favorable evidence remains preserved: DunedinPACE improved from 0.79 to 0.77; OMICm age delta moved slightly more favorable but remained inside the registered stable band; 8 of 19 TruHealth domains materially improved; and 3 additional TruHealth domains remained stable.

Final disposition:

```text
prediction:      moderate_improvement
actual:          overall_improvement_not_met
status:          closed
support:         not supported
error_direction: over
```

`over` means the model overestimated the breadth of August biological improvement relative to the preregistered overall-profile requirement.

This closure does not establish generalized biological deterioration, infer why provider metrics moved, change Phase 2 status, or declare Phase 2D.
