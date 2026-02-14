# Measurement Sources

This document defines the devices, facilities, and software systems used for data capture within this repository.
Purpose: preserve longitudinal comparability and identify potential systematic biases.

> If you choose not to disclose facility/location publicly, use stable aliases (e.g., “DEXA_SITE_A”)
> and keep the true mapping private.

---

## Body composition

### DEXA
- Provider (public alias): `DEXA_SITE_A`
- Machine model: (if known) `TODO`
- Software version: `TODO`
- Reporting format: PDF summary + key numeric values transcribed into reports
- Capture conditions:
  - Fasted (≥10 hours)
  - Normal hydration
  - No dehydration or sodium manipulation
  - No acute glycogen depletion protocol
- Known considerations:
  - Lean mass is sensitive to glycogen/hydration
  - Cross-machine comparisons may not be equivalent
  - Prefer same machine + software where possible

### BodPod
- Provider (public alias): `BODPOD_SITE_A`
- Machine model: (if confirmed) COSMED Bod Pod
- Capture conditions:
  - Fasted (≥10 hours)
  - Minimal clothing (facility standard)
  - No sauna or dehydration manipulation
- Known considerations:
  - Sensitive to hydration and GI contents
  - Compare longitudinally within the same facility

---

## Wearables

### Primary wearable
- Device: `TODO` (e.g., Whoop / Garmin / Oura)
- App ecosystem: `TODO`
- Metrics used:
  - HR
  - HRV
  - Sleep duration (if used)
  - Steps / activity (if used)
- Handling:
  - Raw values as reported
  - No post-processing modifications
- Considerations:
  - HRV values are device-specific; avoid cross-platform comparisons

---

## Laboratory testing (if applicable)
- Provider (public alias): `LAB_SITE_A`
- Reporting method:
  - Official lab report PDF archived
  - Key values transcribed into report files
- Considerations:
  - Reference ranges can change over time
  - Cross-lab comparisons should be cautious

---

## Change control
If any of the following change:
- facility / machine / wearable ecosystem / lab provider

Then:
1) update this file  
2) log the change in `CHANGELOG.md`  
3) note comparability impact in the next report
