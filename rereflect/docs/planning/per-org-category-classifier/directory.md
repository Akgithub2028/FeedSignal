# Directory guide: `docs/planning/per-org-category-classifier`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for per org category classifier. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 5 child directories, and 12 files in its subtree before generated guides/index inventories. Common formats: .md: 12.

## Read first

- [prd.md](<prd.md>) — PRD — Per-Org Category Classifier (M5.2 v2): `docs/planning/per-org-corrections-classifier/prd.md:145`) time an operator overrides the AI-assigned pain-point or feature-request category on a feedback item —
- [understanding.md](<understanding.md>) — Phase 2 — Understanding note: per-org category classifier (M5.2 v2): Synthesis of four read-only service maps (analysis-engine, worker, backend, frontend), 2026-07-11. Extend the shipped M5.2 per-org self-improving…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [category-core](<category-core/directory.md>), [data-and-config](<data-and-config/directory.md>), [predict-seam](<predict-seam/directory.md>), [settings-and-frontend](<settings-and-frontend/directory.md>), [worker-trainer](<worker-trainer/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics; What the issue is really asking; Headline finding: the spine is already ~90% task-generic.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
