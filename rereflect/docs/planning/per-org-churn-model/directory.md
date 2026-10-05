# Directory guide: `docs/planning/per-org-churn-model`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for per org churn model. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 1 immediate baseline/preparation files, 7 child directories, and 15 files in its subtree before generated guides/index inventories. Common formats: .md: 15.

## Read first

- [prd.md](<prd.md>) — PRD — Per-Org Churn ML Model (M5.3): isotonic-calibrated heuristic — with the heuristic preserved as the automatic fallback. For whom: the self-hosting operator of Rereflect who labels churn events (manually, via

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [calibration-beat-fix](<calibration-beat-fix/directory.md>), [churn-classifier-core](<churn-classifier-core/directory.md>), [churn-label-gate-study](<churn-label-gate-study/directory.md>), [churn-predict-seam-resolver](<churn-predict-seam-resolver/directory.md>), [docs-changelog-tracking](<docs-changelog-tracking/directory.md>), [settings-api-and-churn-accuracy-card](<settings-api-and-churn-accuracy-card/directory.md>), [worker-churn-trainer-and-schedule](<worker-churn-trainer-and-schedule/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
