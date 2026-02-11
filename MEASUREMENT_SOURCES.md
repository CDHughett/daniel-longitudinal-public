# Measurement Sources

This document defines the devices, facilities, and software systems used for data capture within this repository.

The purpose is to preserve longitudinal comparability and identify potential systematic biases.

---

## Body Composition

### DEXA

- Provider: [Insert Facility Name]
- Location: [City, State]
- Machine Model: [Insert manufacturer + model if known]
- Software Version: [If available]
- Reporting Format: PDF summary + numeric values transcribed into snapshot report
- Capture Conditions:
  - Fasted (≥10 hours)
  - Normal hydration
  - No dehydration or sodium manipulation
  - No acute glycogen depletion protocol
- Known Considerations:
  - Lean mass is sensitive to glycogen and hydration state
  - Cross-machine comparisons may not be directly equivalent
  - Future scans should be conducted on the same machine when possible

---

### Bod Pod

- Provider: [Insert Facility Name]
- Location: [City, State]
- Machine Model: COSMED Bod Pod (if confirmed)
- Calibration: Performed by facility prior to test (per provider protocol)
- Capture Conditions:
  - Fasted (≥10 hours)
  - Minimal clothing
  - No sauna or dehydration manipulation
- Known Considerations:
  - Sensitive to hydration and gastrointestinal contents
  - Not equivalent to DEXA lean mass metrics
  - Should be compared longitudinally within same facility

---

## Wearables

### Primary Wearable

- Device: [Device Name + Model]
- Firmware / App Ecosystem: [App Name + Version if known]
- Metrics Used:
  - Heart Rate (HR)
  - Heart Rate Variability (HRV)
  - Steps
  - Active Calories
  - Activity Intensity
- Data Handling:
  - Raw values used as reported
  - No post-processing modifications
- Known Considerations:
  - HRV values are device-specific and not cross-platform comparable
  - Active calorie estimates are algorithm-derived

---

## Laboratory Testing (If Applicable)

- Provider: [Lab Name]
- Location: [City, State or Mail-in]
- Testing Type:
  - Blood panels
  - Biomarker panels
  - Epigenetic testing (if applicable)
- Reporting Method:
  - Official lab report PDF archived
  - Key values transcribed into report files
- Known Considerations:
  - Reference ranges may change over time
  - Cross-lab comparisons should be interpreted cautiously

---

## Software / Tracking Systems

- Activity Tracking App: [App Name]
- Data Storage:
  - Manual transcription into Markdown reports
  - Version-controlled via Git
- No automated transformation pipelines currently in use.

---

## Change Control

If:
- Facility changes
- Machine changes
- Wearable ecosystem changes
- Lab provider changes

Then:
1. Update this file
2. Log the change in CHANGELOG.md
3. Note impact on longitudinal comparability in the next report
