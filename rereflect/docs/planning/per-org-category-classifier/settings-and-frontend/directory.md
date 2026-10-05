# Directory guide: `docs/planning/per-org-category-classifier/settings-and-frontend`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for per org category classifier, aspect settings and frontend. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect: settings-and-frontend: already-type-parameterized backend accuracy/rollback API. The backend `GET/POST .../classifier/accuracy/rollback` already accept `classifier_type` (default
- [plan_20260711.md](<plan_20260711.md>) — Implementation Plan — settings-and-frontend (2026-07-11): (`GET/PATCH /api/v1/settings/ai`). **No backend change in this aspect.** The accuracy/rollback route query param on both `GET .../classifier/accuracy` and `POST…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope (`services/frontend-web/`); Contract already provided (verified by reading, not assumed); Patterns to mirror (verified cites).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
