# UDI Reconciliation: Compound Records 032 and 033

## Purpose

This document resolves the compound-record eligibility issue
identified in the UDI v1.1 framework for records 032 and 033.

These records contain multiple independently measurable outcomes
within a single model-error entry and therefore cannot be included
directly within `UDI_point` calculations without prior resolution.

This reconciliation follows the preferred resolution path defined in:

`docs/methodology/udi_framework_v1.md`

> split compound records into sub-records when component outcomes are independently measurable

Original records remain unchanged and continue to serve as the
canonical historical prediction records.

---

## Record 032

### Original Record

Prediction:

- DunedinPACE = 0.87
- SYMPHONY Age = 49.6

Observed:

- DunedinPACE = 0.79
- SYMPHONY Age = 37.8

Recorded Errors:

- DunedinPACE error = 9.2%
- SYMPHONY Age error = 23.8%

### Component Resolution

032-A

- Domain: epigenetic_aging_dunedinpace
- Error Direction: over
- Error Percentage: 9.2%

032-B

- Domain: epigenetic_aging_symphony_age
- Error Direction: over
- Error Percentage: 23.8%

---

## Record 033

### Original Record

Prediction:

- Body Fat % = 14.1
- Lean Mass = 184.4 lb
- Total Mass = 224.8 lb

Observed:

- Body Fat % = 15.4
- Lean Mass = 184.9 lb
- Total Mass = 229.1 lb

Recorded Errors:

- Body Fat % error = 9.2%
- Lean Mass error = 0.3%
- Total Mass error = 1.9%

### Component Resolution

033-A

- Domain: body_comp_bodyfat_pct
- Error Direction: under
- Error Percentage: 9.2%

033-B

- Domain: body_comp_lean_mass
- Error Direction: under
- Error Percentage: 0.3%

033-C

- Domain: body_comp_total_mass
- Error Direction: under
- Error Percentage: 1.9%

---

## Governance Notes

No original model-error records were modified.

No prediction values were changed.

No observed values were changed.

This reconciliation exists solely to permit future
component-level interpretation and eligibility review
within stratified UDI reporting.

Composite UDI remains withheld under the existing
UDI v1.1 methodology.
