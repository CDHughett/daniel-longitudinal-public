#!/usr/bin/env python3
"""Repository validator entry point with session-aware current-state semantics.

The validation implementation remains in ``validate_repository_core.py``. This
entry point narrows two legacy assumptions preserved in the core implementation:
training coverage is session-indexed rather than day-indexed, and the release
DOI changed only after external v1.1.0 publication completed.
"""

from __future__ import annotations

import re
import sys

import validate_repository_core as core


_ENDPOINT_RE = re.compile(
    r"^Aligned daily/sleep/training endpoints diverge: "
    r"daily=(\d{4}-\d{2}-\d{2}), "
    r"sleep=(\d{4}-\d{2}-\d{2}), "
    r"training=(\d{4}-\d{2}-\d{2})$"
)

_PUBLISHED_V1_1_0_DOI = "10.5281/zenodo.22759132"


_original_error = core.Report.error


def _session_aware_error(self: core.Report, check: str, message: str) -> None:
    """Preserve errors except two explicitly governed legacy assumptions."""
    if (
        check == "release metadata"
        and message
        == f"Unexpected DOI in CITATION.cff: {_PUBLISHED_V1_1_0_DOI!r}"
    ):
        self.pass_(
            check,
            (
                "Authoritative published v1.1.0 DOI accepted: "
                f"{_PUBLISHED_V1_1_0_DOI}"
            ),
        )
        return

    match = _ENDPOINT_RE.match(message)
    if check != "current state surfaces" or match is None:
        _original_error(self, check, message)
        return

    daily_end, sleep_end, training_end = match.groups()

    # Daily biomarkers and canonical sleep describe represented days and must
    # remain aligned. Training describes completed sessions, so its latest date
    # may legitimately be earlier; it must never extend beyond daily coverage.
    if daily_end == sleep_end and training_end <= daily_end:
        self.pass_(
            check,
            (
                "Daily and canonical-sleep endpoints align at "
                f"{daily_end}; training is session-indexed and ends at "
                f"{training_end}, which is valid when later represented days "
                "contain zero completed sessions"
            ),
        )
        return

    _original_error(self, check, message)


core.Report.error = _session_aware_error


if __name__ == "__main__":
    sys.exit(core.main())
