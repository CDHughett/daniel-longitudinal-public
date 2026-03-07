# Measurement Sources

This document defines the devices, facilities, and software systems used for data capture within this repository.

The purpose of this file is to:

• preserve longitudinal comparability  
• identify potential sources of systematic bias  
• document capture conditions for future interpretation  

Where public disclosure of facilities is not desired, stable aliases are used.

Example:

DEXA_SITE_A  
BODPOD_SITE_A  
LAB_SITE_A  

The true mapping between aliases and real facilities is maintained privately.

---

# Measurement Governance

All measurements included in this archive must satisfy the following conditions:

1. Captured during normal operating conditions
2. No artificial dehydration or manipulation protocols
3. No acute glycogen depletion or loading strategies
4. No short-term behavioral manipulation intended to influence measurements

The objective is **representative physiological state**, not peak display.

---

# Body Composition

## DEXA

Provider (public alias)  
`DEXA_SITE_A`

Machine model  
`TODO` (if available)

Software version  
`TODO`

Reporting format

• Official PDF archived in `/snapshots`
• Key numerical values transcribed into reports

Capture conditions

• Fasted (≥10 hours)  
• Normal hydration state  
• No dehydration or sodium manipulation  
• No glycogen depletion protocols  
• Normal training schedule maintained  

Known considerations

• Lean mass is sensitive to glycogen and hydration status  
• Cross-machine comparisons may introduce measurement variance  
• Longitudinal comparisons should prioritize identical hardware and software versions when possible  

---

## BodPod

Provider (public alias)  
`BODPOD_SITE_A`

Machine model  
COSMED Bod Pod (if confirmed)

Capture conditions

• Fasted (≥10 hours)  
• Minimal clothing per facility protocol  
• No dehydration manipulation  
• No sauna exposure prior to measurement  

Known considerations

• Sensitive to hydration state  
• Sensitive to gastrointestinal contents  
• Comparisons should prioritize the same facility and calibration standard  

---

# Wearables

## Primary wearable

Device  
`TODO` (example: WHOOP / Garmin / Oura)

Software ecosystem  
`TODO`

Metrics utilized

• Heart Rate (HR)  
• Heart Rate Variability (HRV)  
• Sleep duration (if applicable)  
• Activity metrics (steps or equivalent, if used)

Data handling

• Raw device values recorded  
• No post-processing adjustments  
• No algorithmic modification beyond device reporting  

Considerations

• HRV values are device-specific  
• Cross-platform HRV comparisons are not considered valid  

---

# Laboratory Testing

Provider (public alias)  
`LAB_SITE_A`

Reporting method

• Official laboratory report archived in `/snapshots`  
• Key biomarkers transcribed into report files  

Considerations

• Reference ranges may change over time  
• Cross-laboratory comparisons should be interpreted cautiously  
• Biomarker interpretation remains context-bound to capture conditions  

---

# Data Handling Policy

All measurement artifacts follow these rules:

• Original source artifacts are preserved unmodified  
• Numerical values may be transcribed for reporting clarity  
• Transcription errors must be corrected via new commits  
• Historical artifacts are never overwritten  

This preserves the integrity of the longitudinal archive.

---

# Longitudinal Comparability

If any of the following change:

• measurement facility  
• hardware platform  
• device ecosystem  
• laboratory provider  
• capture protocol  

Then the following actions must occur:

1. Update this document  
2. Record the change in `CHANGELOG.md`  
3. Note potential comparability impact in the next report  

---

# Interpretation Boundary

Measurement artifacts represent **observation points**, not claims.

Interpretation of measurements is governed by:

→ `ASSUMPTIONS_AND_BOUNDARIES.md`  
→ `METHODOLOGY_AND_CONTROLS.md`

These files define the limits of causal inference within the archive.
