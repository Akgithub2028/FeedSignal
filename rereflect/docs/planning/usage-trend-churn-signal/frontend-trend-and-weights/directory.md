# Directory guide: `docs/planning/usage-trend-churn-signal/frontend-trend-and-weights`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for usage trend churn signal, aspect frontend trend and weights. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — frontend-trend-and-weights: Two frontend-only slices, both about making a shipped-but-invisible capability reachable. `usage_trend_state` / `usage_trend_pct` on the usage API response; without a UI they…
- [plan_20260722.md](<plan_20260722.md>) — Implementation Plan — frontend-trend-and-weights: `cd services/frontend-web`. Try `npm install` first (worked in a recent worktree per the repo gotchas note); if it fails with `EUNSUPPORTEDPROTOCOL`, run `pnpm install`…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; Evidence (observed, verified in this worktree); 0. Setup; Part B — D4 weights fix (do first, split-able).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
