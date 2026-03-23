# Valid Prediction Criteria

Defines the requirements for a prediction to be included in the model error dataset.

---

## Definition

A valid prediction is a forward-stated, testable claim with a defined outcome condition, logged before the outcome exists.

---

## Core Requirements

### 1. Temporal Integrity
Prediction must be logged before outcome is known.

- Primary → logged in real time  
- Inferred / reconstructed → explicitly labeled  

---

### 2. Testability
Prediction must be provably correct or incorrect.

Invalid if it cannot be resolved objectively.

---

### 3. Defined Domain
Each prediction must belong to a domain:

- HRV  
- sleep  
- performance  
- recovery_rate  

---

### 4. Resolution Condition
Prediction must include a clear resolution condition:

- time-bound (e.g., next 7 days)  
- event-bound (e.g., no destabilization event)  

---

### 5. Directional Clarity
Prediction must define a direction or state:

- increase / decrease  
- stable  
- event / no event  

---

### 6. Measurability
Prediction must map to an observable variable.

---

### 7. Non-Retroactivity
Predictions cannot be edited after outcome is known.

Only outcome and error fields may be filled.

---

### 8. Atomic Structure
Each prediction must represent a single claim.

Compound predictions must be split into separate rows.

---

## Classification Tiers

### Tier 1 — Strong
- time-bound  
- measurable  
- binary or numeric  

### Tier 2 — Acceptable
- directional  
- resolvable  

### Tier 3 — Weak
- vague  
- interpretive  
- difficult to resolve  

---

## Enforcement Rule

If a prediction fails any core requirement, it should not be logged as a primary entry.

It may be stored separately or discarded.
