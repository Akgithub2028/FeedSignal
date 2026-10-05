# Directory guide: `docs/planning/product-usage-enrichment/usage-rollup-and-score`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for product usage enrichment, aspect usage rollup and score. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — usage-rollup-and-score: Raw usage events become a per-customer rollup with a 0-100 `usage_score` (recency + frequency + breadth), recomputed as events arrive and on a schedule, so a customer going quiet…
- [plan_20260628.md](<plan_20260628.md>) — Implementation Plan — usage-rollup-and-score (2026-06-28): - **Recency** from `last_active_at`: ≤2d→100, ≤7d→80, ≤14d→60, ≤30d→40, ≤60d→20, else 5; `None`→neutral. - **Frequency** from `active_days_30d`: ≥20→100 … 0→low…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; 0. Project setup; Phase 1 — `customer_usage` model + migration.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
