# Directory guide: `docs/planning/customer-segments`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for customer segments. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 3 child directories, and 8 files in its subtree before generated guides/index inventories. Common formats: .md: 8.

## Read first

- [prd.md](<prd.md>) — PRD — Customer Segments (rule-based): Rereflect surfaces every customer as an individual row on the Customers page with a health score and churn risk, but gives operators **no way to group customers by behavior**. A CS…
- [understanding.md](<understanding.md>) — Understanding — Customer Segments (Phase 2 dig): Group customers into **rule-based behavioral cohorts** (power users, silent churners, happy advocates, at-risk, dormant, …) computed **only from signals that already…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [segment-api](<segment-api/directory.md>), [segment-engine](<segment-engine/directory.md>), [segment-ui](<segment-ui/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics; What this is really asking; Affected areas (which services).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
