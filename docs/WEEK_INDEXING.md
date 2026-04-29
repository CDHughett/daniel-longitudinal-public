# Week Indexing Convention

This repository uses an internal week indexing system for reports and active dashboard updates.

## Key Rule

Report labels such as `2026-W17` represent internal reporting weeks, not strict ISO calendar weeks.

## Offset

The internal reporting week may be offset from the calendar week depending on reporting cadence.

Example:

- Internal reporting label: `2026-W17`
- Calendar week: `2026-W18`

## Why This Exists

The reporting system is structured around:

- Complete data windows
- Retrospective weekly closeouts
- Consistent reporting cadence
- Snapshot and artifact alignment

This makes the archive easier to interpret longitudinally than strict calendar-week labeling alone.

## Interpretation Guidance

Week references in:

- `LATEST.md`
- `/reports`
- `CHANGELOG.md`

should be interpreted as internal reporting windows unless otherwise stated.

## Integrity Note

This is a naming convention only.

No data is shifted, omitted, or misaligned due to this offset.
