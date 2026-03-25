# Valid Prediction Criteria (v1.0)

Daniel Longitudinal Study  
Model Error Tracking Layer

---

## Purpose

This document defines the minimum criteria required for a prediction to be:

- recorded  
- evaluated  
- closed  

within the UDI (Unobstructed Delta Index) dataset.

The goal is to preserve:

- dataset integrity  
- decision consistency  
- auditability  

This document is intentionally minimal.

It is not a comprehensive framework.  
It is an enforcement layer.

---

## Core Principle

Predictions are only closed when **observable reality resolves the prediction without ambiguity**.

If resolution requires interpretation, projection, or additional time → the prediction remains **open**.

---

## Valid Prediction Requirements

A prediction is considered valid if it meets all of the following:

### 1. Observable Domain
The prediction must refer to a domain that can be directly observed or measured:

- physiological (HRV, sleep, performance, GI, etc.)
- behavioral (execution, task initiation, routine awareness)
- system state (stability, compatibility, disruption)

Predictions about abstract or non-observable outcomes are not valid.

---

### 2. Time-Bound or State-Resolvable
The prediction must resolve via:

- a defined time window  
**or**
- a clearly observable state transition  

Examples:
- “within 3–5 days”  
- “during early THC removal window”  
- “no training disruption under current structure”  

---

### 3. Falsifiability
The prediction must be capable of being proven wrong.

If no realistic observation could invalidate it → it should not be recorded.

---

### 4. Single-Event or Cohesive State
Each prediction should map to:

- a single observable outcome  
**or**
- a tightly coupled state cluster  

Avoid combining unrelated outcomes into a single prediction.

---

## Closure Criteria

A prediction may be marked **closed** only when:

### 1. Direct Observation Exists
There is a clear observed outcome corresponding to the prediction.

---

### 2. Outcome Matches or Deviates Clearly

Closure types:

- **closed (success)** → observed outcome aligns with prediction  
- **closed (failure)** → observed outcome contradicts prediction  

Ambiguous or partial matches should remain **open**.

---

### 3. No Additional Time Dependency

If the prediction depends on:

- future stabilization  
- multi-day trends  
- unresolved transitions  

→ it must remain **open**

---

## Non-Closure Rules

A prediction must remain **open** if any of the following are true:

- the defined time window has not elapsed  
- the system is still in transition  
- the observed outcome is incomplete  
- resolution requires interpretation rather than observation  

---

## Attribution Rules

Real-world events may include confounding factors.

When an outcome is influenced by a **known external or input-driven variable**:

- the event may still be used for closure  
- attribution must be explicitly noted  

Example:
- GI instability caused by food timing mismatch  
→ does not invalidate system stability prediction  
→ must be annotated as input-related, not systemic  

---

## Prediction Types

Predictions are categorized as:

### Point
A specific value or discrete outcome  
(e.g., HRV = 75)

---

### Range
An expected band of values  
(e.g., sleep 400–450 minutes)

---

### State
A system condition or behavior  
(e.g., “no training disruption”)

---

### Trajectory
A directional shift over time  
(e.g., “movement toward lock-in”)

Trajectory predictions require extended observation and should remain open longer.

---

## Closure Discipline

When in doubt:

> **do not close**

Premature closure is more damaging than delayed closure.

Dataset integrity is prioritized over completeness.

---

## Version Notes

v1.0 establishes baseline closure discipline using observed events from early UDI dataset integration.

Future versions may expand scope only if justified by repeated edge cases.

This document should remain minimal and enforceable.
