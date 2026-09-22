# Supplementation Architecture — Effective 2026-09-18

## Status

**Active protocol-context record**

**Effective exposure date:** 2026-09-18  
**Repository disclosure date:** 2026-09-22  
**Evidence class:** retrospective operator report of a date-bounded protocol change

This document preserves a material change in the subject's background supplementation architecture.

The exposure change began on 2026-09-18. It was not represented in the completed `Daniel_Dataset_v1.31` source used for the Week 37 closeout and was disclosed to the archive on 2026-09-22. The distinction between **effective date** and **documentation date** is therefore preserved explicitly.

This is not a clinical recommendation or generalized supplementation protocol.

---

## Prior Architecture

Before 2026-09-18, the operator had maintained a broad multi-compound supplementation architecture for more than nine months, with products taken daily or on recurring 5-on / 2-off schedules as applicable.

The previously disclosed routine/cycled layer included compounds or products used for overlapping longevity, antioxidant, inflammatory, methylation, cognition, vascular, nutrient, and hormone-support rationales, including:

- NMN
- pterostilbene
- CoQ10 / PQQ
- Pycnogenol
- lion's mane
- astaxanthin
- sulforaphane
- NAC
- alpha-GPC
- CDP-choline
- TMG
- methylfolate
- vitamin B12
- DHEA
- high-dose zinc with copper
- boron
- Nigella sativa
- lutein / zeaxanthin
- beef-organ capsules
- beef-tallow capsules
- other optional recovery/performance compounds used as part of the larger shelf

Creatine, protein supplementation, magnesium, omega-3 intake, and selected goal-specific tools were also part of the broader prior environment.

The archive does not claim uniform day-level adherence for every compound. Public supplementation coverage remains contextual rather than a canonical daily adherence dataset.

---

## Architecture Beginning 2026-09-18

The prior broad shelf was discontinued as a routine baseline and replaced with a smaller evidence-weighted architecture.

### Core retained layer

- **Creatine monohydrate:** approximately 5 g/day.
- **Whey isolate:** retained as a food/protein tool; quantity is determined by total dietary protein needs rather than treated as a mandatory fixed supplement dose.
- **Magnesium glycinate:** retained at the established modest supplemental dose, approximately 210 mg/day when used.
- **Omega-3 EPA/DHA:** retained when dietary fatty-fish intake is insufficient.
- **Vitamin D3 / K2:** no longer treated as an automatic high-dose daily baseline; vitamin-D use is intended to be laboratory/status guided.

### Goal- or context-specific tools

The following may remain available without constituting mandatory daily baseline exposure:

- collagen for connective-tissue / loading support
- glycine as an optional sleep/recovery tool
- L-citrulline as an optional performance tool
- tart cherry as a selective recovery tool rather than a standing daily intervention

### Ordinary food exposure

Culinary turmeric, ginger, Ceylon cinnamon, and small amounts of black pepper remain part of ordinary food/shake intake. They are classified as food context rather than a concentrated antioxidant-supplement layer.

---

## Rationale

The transition was made to:

- weight human outcome evidence more heavily than mechanistic plausibility alone
- reduce redundant pathway targeting across many simultaneous compounds
- improve interpretability of the longitudinal system
- reduce unnecessary recurring cost
- preserve high-signal nutritional and performance support
- avoid maintaining concentrated antioxidant or hormone-support exposure without a defined indication

The change was **not** introduced to improve an upcoming snapshot, force a biomarker result, create a favorable recovery narrative, or rescue any existing Model Error record.

---

## Causal Boundary

This is a multi-variable exposure change.

Because numerous compounds were stopped or reclassified at the same time, subsequent changes in:

- sleep
- resting or sleeping heart rate
- HRV
- dream phenomenology
- subjective recovery
- training performance
- body composition
- blood biomarkers
- molecular or epigenetic outputs

cannot be attributed to any individual removed compound or to the supplementation change as a whole.

Any post-2026-09-18 pattern is initially descriptive and hypothesis-generating.

As of the 2026-09-22 disclosure, the operator had subjectively noticed possible improvement in some sleep characteristics and possibly lower resting-heart-rate behavior. Those observations occurred after the exposure change and are **not** treated as causal evidence, a registered prediction, or a scored outcome.

---

## Longitudinal Interpretation Boundary

For future analysis, 2026-09-18 may be used as a documented protocol-context boundary:

```text
pre-2026-09-18:
broad multi-compound supplementation architecture

2026-09-18 onward:
reduced evidence-weighted supplementation architecture
```

A future exploratory pre/post analysis may compare windows around this boundary, but it must preserve concurrent influences such as training exposure, sleep, stress, intake, bodyweight, travel, ordinary-life load, and measurement variability.

No retrospective Model Error record is created from this transition.

No prospective prediction may be backdated to the transition after post-change observations are already known.

---

## Structured-Data Provenance Boundary

No new `data/context_events_v1.csv` row is created by this disclosure batch.

The current v1 machine-readable schema requires a canonical `private_workbook:` or `private_pdf:` `source_ref`. The 2026-09-18 supplementation transition was not preserved in the completed v1.31 private source used for Week 37.

Creating a structured row that falsely points to v1.31 would overstate provenance.

If a later governed private source preserves this retrospective disclosure with an acceptable canonical locator, a bounded context-event row may be added prospectively as an archive-maintenance step while retaining the original 2026-09-18 effective date and 2026-09-22 disclosure date.

---

## Invariants

This transition does not by itself change:

- Phase 2 declaration
- Phase 2D status
- B1 prescription
- Load Integration prescription
- Week 38 reserve-replication posture
- Model Error records 041–046
- DQ-011
- August snapshot interpretation
- v1.1.0 release identity
- Git tag or DOI lineage
