# Canonical Endpoint Validation Semantics

This note documents the current endpoint rule used by repository validation for the aligned daily, sleep, and training layers.

## Daily and Sleep

`data/daily_biomarkers_v1.csv` and `data/sleep_longitudinal_v1.csv` are daily longitudinal layers. Their current represented endpoint dates must align.

A mismatch between the daily-biomarker endpoint and canonical-sleep endpoint is a validation error.

## Training

`data/training_blocks_v1.csv` is a session-level layer with zero-to-many completed sessions per represented date.

A represented daily/sleep date therefore does not require a synthetic training row when no formal session was completed on that date.

The validator applies these rules:

- training may not extend beyond the represented daily interval
- training may end before the daily/sleep endpoint when the terminal represented date or dates contain no completed training session
- no zero-duration or synthetic `no_session` training row should be created solely to force endpoint equality
- the training row count and actual training endpoint must still agree with `data/DATA_COVERAGE.md`

This distinction preserves the difference between **absence of a completed training session** and **missing daily representation**.

## Implementation Boundary

`tools/validate_repository.py` is the session-aware entry point. The pre-existing repository checks remain in `tools/validate_repository_core.py`; the entry point narrows only the legacy endpoint-equality assumption and otherwise delegates to the unchanged core validator.

The session-aware entry point suppresses the legacy endpoint-divergence error only when:

- daily biomarkers and canonical sleep end on the same represented date, and
- the latest completed training-session date is on or before that daily endpoint.

A daily/sleep endpoint mismatch remains an error. Training that extends beyond daily coverage remains an error.

## W36 Trigger

The rule was clarified during the 2026-W36 closeout after ordinary travel produced a represented zero-session terminal day on 2026-09-13. Daily biomarkers and canonical sleep legitimately extend through 2026-09-13, while the latest completed formal training session occurred on 2026-09-12.

The clarification changes validator semantics only. It does not create a training observation, alter historical training data, modify protocol state, or reinterpret the travel interruption.
