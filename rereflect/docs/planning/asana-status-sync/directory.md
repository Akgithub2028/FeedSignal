# Directory guide: `docs/planning/asana-status-sync`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for asana status sync. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 1 immediate baseline/preparation files, 6 child directories, and 13 files in its subtree before generated guides/index inventories. Common formats: .md: 13.

## Read first

- [prd.md](<prd.md>) — PRD — Asana Inbound Status-Sync: The Asana integration (slice 1, shipped 2026-07-06) is **outbound-only**: an operator can create an Asana task from a feedback item, but when the engineer later completes that task in…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [asana-client-get-task](<asana-client-get-task/directory.md>), [backend-routes](<backend-routes/directory.md>), [docs-and-tracking](<docs-and-tracking/directory.md>), [frontend](<frontend/directory.md>), [model-migrations](<model-migrations/directory.md>), [worker-sync-task](<worker-sync-task/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
