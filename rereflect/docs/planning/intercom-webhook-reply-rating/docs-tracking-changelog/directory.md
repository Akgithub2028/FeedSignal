# Directory guide: `docs/planning/intercom-webhook-reply-rating/docs-tracking-changelog`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for intercom webhook reply rating, aspect docs tracking changelog. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect spec — Docs, changelog & tracking markers: The feature flips the honest-limits claims from #16 ("the webhook's replied/rating events are still dedup-inert — flagged follow-up, not fixed") and closes the
- [plan_20260816.md](<plan_20260816.md>) — Implementation Plan — docs-tracking-changelog (aspect 4 of 4, close-out, runs last): `webhook-enrich-module`, `golden-fixtures-route-pins`) have merged into the branch. This plan's placeholders (merge sha, PR number,…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice; In-scope; 0. Facts gathered (verified 2026-08-16, before writing); 1. Project setup checklist.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
