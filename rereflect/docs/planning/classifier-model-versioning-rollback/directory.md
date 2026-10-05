# Directory guide: `docs/planning/classifier-model-versioning-rollback`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for classifier model versioning rollback. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 5 child directories, and 8 files in its subtree before generated guides/index inventories. Common formats: .md: 8.

## Read first

- [prd.md](<prd.md>) — PRD — Durable Classifier Model Rollback + Versioning: Rereflect's flagship moat is the **per-org self-improving classifier flywheel** (M5.2 — sentiment/category/urgency heads trained on the org's own corrections,
- [plan_20260724.md](<plan_20260724.md>) — Implementation Plan — Durable Classifier Model Rollback + Versioning (2026-07-24): (`sentiment_autopromote_hold` / `category_autopromote_hold` / `urgency_autopromote_hold`, Boolean, default false). NOT a row-pin. The
- [understanding.md](<understanding.md>) — Understanding — durable classifier model rollback + versioning: originally-recommended feature already shipped. See `_card/card.md` for the Commits `a630c9c` + `cea261b` (M5.2 settings), documented…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [backend-routes](<backend-routes/directory.md>), [data-model-and-migration](<data-model-and-migration/directory.md>), [docs-and-tracking](<docs-and-tracking/directory.md>), [frontend-versioning-ui](<frontend-versioning-ui/directory.md>), [worker-hold-guard](<worker-hold-guard/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics; Architecture decisions (locked, from PRD + interview); Project setup / impact; What is ALREADY shipped (do not rebuild); The real, unbuilt problem (this feature).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
