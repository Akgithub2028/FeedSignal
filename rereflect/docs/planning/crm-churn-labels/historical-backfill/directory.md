# Directory guide: `docs/planning/crm-churn-labels/historical-backfill`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for crm churn labels, aspect historical backfill. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect spec — historical-backfill: (`ai_readiness.py:74-79`) and the calibrator gate (`churn_calibration.py:50`) count `CustomerChurnEvent` rows — *actual churns*. An org with 1,000 customers at 5% annual churn
- [plan_20260715.md](<plan_20260715.md>) — Implementation Plan — historical-backfill: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. rows. ~50 real churns/year for a 1,000-customer org ⇒ forward-only reaches the 500 gate in ~10…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; 0. Impact analysis (from the dig — verified against source); Reuse verbatim (do NOT fork).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
