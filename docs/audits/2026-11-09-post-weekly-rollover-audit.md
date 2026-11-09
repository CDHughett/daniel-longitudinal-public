# 2026-11-09 W44/W45 Post-Weekly-Rollover Integrated Integrity Audit

**Audit date:** 2026-11-09  
**Repository:** CDHughett/daniel-longitudinal-public  
**Working branch:** w44-closeout-w45-rollover  
**Production baseline (main):** fc77e4323d2fe28b53c5bdab427afc5859f09995  
**Independently audited pre-audit HEAD:** 1f7128ddbd2d4198d90c8471c8cb70620062a868  
**Successful pre-audit workflow:** [GitHub Actions run #183, ID 42721495196](https://github.com/CDHughett/daniel-longitudinal-public/actions/runs/42721495196), on the exact pre-audit HEAD  
**Disposition:** **INTEGRITY PASS / CONDITIONAL GO** for the stated pre-audit HEAD. The audit-bearing commit is a **new HEAD** and requires its own successful exact-SHA five-validator run before PR review or merge.

---

## Scope and evidence boundary

This is a selective, credibility-relevant repository integrity checkpoint, not the operator's daily narrative or an assertion of clinical recovery. It records Batch 4's independent source-and-history comparison, two observed validation failures and their isolated repairs, passing official CI, the W44 Closed / W45 Active lifecycle, current public navigation and numerical coverage, private-file provenance, protected forecasts, privacy, and publication boundaries.

The decision establishes **internal traceability, reproducible arithmetic and valid public-document structure**. It does **not** independently validate wearable physiology, witness exercise repetitions, verify every per-set resistance load, prove a lumbar tissue diagnosis or clearance, establish causal adaptation, or imply November snapshot outcomes. The original private workbook and full private operator narrative are **not public repo artifacts**.

The repository follows its **internal week labels**, not ISO numbering: internal 2026-W44 covers **November 2–8, 2026** (ISO 2026-W45), and internal 2026-W45 covers **November 9–15, 2026**. Do not silently merge these conventions.

## 1. Exact retained source and governed append

The controlling source identity for W44 is the exact retained private **Daniel_Dataset_v1.38** file, not a reconstructed workbook or inferred checksum:

| Source field | Registered value |
|---|---|
| Private source | Daniel_Dataset_v1.38 |
| Source type | private_workbook |
| Coverage | 2026-11-02 through 2026-11-08 |
| Bytes | **371,260** |
| SHA-256 | **4a852beee7ea74895dd4c37a454e14deb32f9cb2667f927abde70d893cdfa85f** |
| Hash status | registered |
| Public registration | data/source_provenance/daniel_dataset_private_manifest.csv |
| Private-source treatment | Exact source file and long-form operator narrative remain outside public GitHub |

The private workbook contains source date cells represented as both Excel serial dates and bare day-of-month values. The governed public rows use ISO dates reconciled to source ordering and the reporting window. This is date-index normalization, **not** independent confirmation that every original source cell was a complete uniform date or permission to replace missing source values.

An independent comparison checked **91/91** source-versus-public numeric/date pairs: **35 Daily Biomarkers numeric values, 42 canonical sleep numeric values, and 14 date-key comparisons**. Separately, **14/14 training structure checks** verified two reported daily training entries on all seven dates (55-minute B1 plus 45-minute LI). These checks establish transcription correspondence for those fields; they do not externally verify actual session heart rate, exact bar weight, wearable sleep stage, or every performed repetition.

## 2. Append-only historical integrity

Five governed public data/provenance files were compared against production baseline **fc77e432…** and pre-audit HEAD **1f7128dd…**. The old file bytes remain an **exact prefix** in each case, with no rewriting of earlier rows or source history.

| Governed file | Production rows | Audited rows | Intentional change |
|---|---:|---:|---|
| data/daily_biomarkers_v1.csv | 266 | **273** | +7 W44 daily rows |
| data/sleep_longitudinal_v1.csv | 266 | **273** | +7 canonical nights |
| data/training_blocks_v1.csv | 425 | **439** | +14 reported completed B1/LI blocks |
| data/context_events_v1.csv | 56 | **56** | no new event; identical Git blob |
| data/source_provenance/daniel_dataset_private_manifest.csv | 38 | **39** | +1 exact v1.38 registration |

Daily biomarkers and canonical sleep are continuous from **February 9 through November 8, 2026**. The latest completed training date is **November 8**. The bounded context-event index intentionally still ends **November 1** because ordinary W44 reintegration did not warrant a new perturbation event. Absence of a completed session during W43 remediation is not represented as a synthetic training row.

All governed CSV column widths passed; the machine-readable validator confirmed **439 unique session IDs**, with the historically protected training prefix of **325 sessions through August 30** unchanged. New sleep-stage components for each of the seven W44 nights sum arithmetically to total sleep, but that does not establish consumer sleep-stage accuracy.

## 3. Independently reproduced W44 metrics

The unchanged weekly rollover validator independently computed all twelve required structured metrics from the committed public files and matched the closed W44 report:

| Structured metric | W44 result |
|---|---:|
| Seven-morning bodyweight average | **226.5 lb** |
| Daily Biomarkers HRV | **63.4 ms** |
| Daily resting heart rate | **46.4 bpm** |
| Daily average heart rate | **62.4 bpm** |
| Separate overnight Sleep Log HRV | **67.3 ms** |
| Separate sleeping average heart rate | **47.6 bpm** |
| Mean overnight sleep | **7h21m** |
| Mean wearable-estimated deep sleep | **1h48m** |
| Mean wearable-estimated REM | **1h04m** |
| Completed B1 sessions | **7** |
| Completed LI sessions | **7** |
| Total formal training | **700 min** |

The fourteen training rows comprise **385 B1 minutes and 315 LI minutes**, with **21.14 nominal logged B1 miles**. Prescribed distances and heart-rate targets are not necessarily independently measured on every session. LI was reported as familiar standard execution, but exact later per-set loading and complete biomechanics were not independently documented. The older differentiated resistance progressions were not comprehensively retested.

Daily and overnight HRV represent separate measurement streams and cannot be interchanged. Post-B1/post-GI weights are not interchangeable with morning weights; November 4 was **pre-GI**, and the November 5 post-B1 measurement was **missing**. Five W44 REM estimates had Low confidence and two Medium confidence. Neither favorable dream recall nor arithmetically consistent stages establish actual REM duration. W44 functional reintegration remains a bounded observational conclusion, not unrestricted lumbar clearance.

The immediately prior W43 operator correction is retained: on **November 1**, trap-bar work used the **45+25 lb per-side plate configuration for all three sets**, with trap-bar mass unverified and the normal heaviest configuration withheld. W44's comfortable reported loading does not retroactively alter that source clarification.

## 4. Validation failures detected and isolated repairs

Batch 3's head **1c7fa4c42e83ddda67da264133df4ded6f52ab08** generated failing run **42720771243**. The first two validators passed, but the third did not recognize W44's table because its heading was written as **H3** rather than the validator-required exact **H2 “Structured Weekly Metrics”**. The validator consequently reported twelve missing rows. The numerical table itself was present and correct. This was a structural parsing failure, not twelve scientific mismatches.

- **Correction bd720d76a8bbea2048daacf9346001fac187e7ac:** adjusted exactly one heading in reports/2026-W44.md, without changing the table values. Run **42721331132** then passed the first four validators.
- The latter run failed the post-release coherence validator because README.md and LATEST.md each used internal session jargon (“trait-like”) on a first-contact public page, contrary to the repository's readability boundary.
- **Correction 1f7128ddbd2d4198d90c8471c8cb70620062a868:** replaced one expression in each of README.md and LATEST.md with equivalent plain-language reporting of familiar, comfortable execution. No data, claim-strength, prediction, phase rule, validation code, or release identity changed.

Both corrections were confined to already-in-scope reporting/public-navigation files. The repository's validators were **not** rewritten, weakened, bypassed, or disabled to secure a pass.

## 5. Exact-head official validation and warnings

**Pre-audit workflow run #183, ID 42721495196, completed SUCCESS** for exact audited SHA **1f7128ddbd2d4198d90c8471c8cb70620062a868**.

| Existing official validator | GitHub Actions result |
|---|---|
| python tools/validate_repository.py | **PASS** — 0 errors, 2 known historical warnings |
| python tools/validate_machine_readable.py | **PASS** — 0 errors, 0 warnings |
| python tools/validate_weekly_rollover.py | **PASS** — W44 source, lifecycle, dates and 12 metrics match |
| python tools/validate_august_snapshot.py | **PASS** — August cross-layer evidence unchanged |
| python tools/validate_coherence.py | **PASS** — active/closed pointers, current coverage, public language, release identity |

The two **retained historical warnings**, neither new to W44, are:

1. Governed canonical sleep-stage discrepancies on **March 31, 2026 (+16 min)** and **April 2, 2026 (+14 min)**.
2. **DQ-001** awake/awakening duplication on **14 historical dates**.

The separate unresolved **DQ-011** September 8 resting-heart-rate source discrepancy is also still documented. None of these was silently corrected, erased, or used to override W44 data.

**Important CI boundary:** This run validates the **pre-audit** SHA. Creating this audit file changes the branch head and triggers a new workflow. The new audit-bearing commit must have its **own** five-validator SUCCESS before the PR/merge gate. The earlier successful run is not transferable.

## 6. Full Git tree, protected files and privacy

A recursive, non-truncated Git tree comparison and GitHub compare-commits review agreed on **exactly fifteen changed file paths** between production baseline and the pre-audit branch: four appended governed data/provenance files, W44 closed and W45 newly opened reports, and nine synchronized current-facing documents. **W45's report was the sole newly added file** before this audit. There were **238 untouched blob entries** by SHA in the tree comparison. This audit file becomes an additional changed path only after the Batch 5 commit.

The following remained unchanged: all five official validators and the workflow; August snapshot binaries, protected provider exports and checksum manifests; model-error and historical UDI/concordance data; closed predictions 041–046 (including unsupported Record 043); the registered open, locked and unscored forecasts 047–050; phase declaration and methodology; unresolved data-quality records; published **v1.1.0** release identity, Git tag, and its version/all-versions DOIs.

The public phase remains **Phase 2 — Load Integration / Consolidation / lock-in observation**, with **Phase 2D undeclared**. W44 is **Closed — Consolidated Reintegration** based on reported repeatability of the familiar standard routine; W45 is **Active — Pre-snapshot continuity / lumbar-tolerance monitoring** for November 9–15. No W45 outcomes or November 16–17 collection results were invented or prospectively scored. The objective testing rules and provider preparation requirements remain governed separately; supplemental Tanita is not equated to Bod Pod or DEXA.

No private workbook, complete operator narrative, personal medical report, unreviewed test binary, or new direct identifying information was introduced as a public changed file. Source identity is published only as governed metadata.

## 7. Decision, dependencies and next gate

**Pre-audit determination: INTEGRITY PASS / CONDITIONAL GO.** The independently audited branch had exact historical prefixes, grounded W44 dates and 91/91 source correspondence, all twelve weekly metrics reproduced, coherent public current-state documentation, protection of registered sources/governance/release boundaries, and **five official validators green on its exact SHA**.

**Batch 5 acceptance requires:** this isolated audit file committed to the existing rollover branch; a fresh successful GitHub Actions validation run whose head SHA **equals the audit commit**; and read-back of the changed-file scope and the continued separation between that branch and production main.

**Batch 6 remains separate:** human-reviewable PR, final diff and branch protection review, merge only after qualifying checks, then independent post-merge production HEAD and CI verification. This audit is not a PR approval, merger authorization, new release, Phase 2D declaration, or evidence that future November testing has already happened.

**Conclusion:** W44's governed data, the W44 Closed / W45 Active lifecycle and the public evidence surfaces were reconciled under existing scientific and technical controls. The two observed structural problems were corrected narrowly while preserving the audit trail. Remaining warnings, measurement uncertainty and all future evaluation boundaries stay explicit.
