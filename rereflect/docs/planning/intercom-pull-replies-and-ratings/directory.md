# Directory guide: `docs/planning/intercom-pull-replies-and-ratings`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for intercom pull replies and ratings. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 1 immediate baseline/preparation files, 5 child directories, and 11 files in its subtree before generated guides/index inventories. Common formats: .md: 11.

## Read first

- [prd.md](<prd.md>) — PRD — Intercom pull: replies & ratings enrichment: The Intercom **15-minute pull ingests the first message of a conversation only** (intercom_sync.py D3; pull-sync/spec.md:65-66). Replies and ratings were assumed to

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [adapter-reply-rating-extraction](<adapter-reply-rating-extraction/directory.md>), [client-conversation-parts](<client-conversation-parts/directory.md>), [docs-tracking-changelog](<docs-tracking-changelog/directory.md>), [pull-enrichment](<pull-enrichment/directory.md>), [reanalysis-seam](<reanalysis-seam/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
