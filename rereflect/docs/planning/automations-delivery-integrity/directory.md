# Directory guide: `docs/planning/automations-delivery-integrity`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for automations delivery integrity. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 1 immediate baseline/preparation files, 2 child directories, and 5 files in its subtree before generated guides/index inventories. Common formats: .md: 5.

## Read first

- [prd.md](<prd.md>) — PRD — Automations Delivery Integrity: Rereflect's automations surface tells users it is doing things it is not doing. Two independent, **verified** defects compound on the same code path.

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [slack-channel-and-loudness](<slack-channel-and-loudness/directory.md>), [worker-trigger-mirror](<worker-trigger-mirror/directory.md>).

Document sections to inspect: Problem Statement; Defect A — two trigger types have never fired, in any deployment.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
