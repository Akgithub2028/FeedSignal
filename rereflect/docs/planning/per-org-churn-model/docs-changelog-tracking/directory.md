# Directory guide: `docs/planning/per-org-churn-model/docs-changelog-tracking`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for per org churn model, aspect docs changelog tracking. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Spec — docs-changelog-tracking (close-out): Repo convention (visible across every shipped feature's commit history) is that a feature lands with its docs: CHANGELOG entries, SELF_HOSTING upgrade callouts, AI-TRACKING
- [plan_20260814.md](<plan_20260814.md>) — Implementation Plan — docs-changelog-tracking (aspect 7, close-out): - `AI-TRACKING.md` (M5.3 markers + gate caveat 542-553 + M5.2/M5.4 rows if needed) - `DEV-TRACKING.md` (FIXED markers for both registration bugs; the…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice; In scope; 1. Project setup checklist; 2. Implementation phases.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
