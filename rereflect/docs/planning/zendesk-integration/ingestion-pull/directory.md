# Directory guide: `docs/planning/zendesk-integration/ingestion-pull`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for zendesk integration, aspect ingestion pull. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect: ingestion-pull (default entry point): tickets through the ingestion core. Works with no public ingress — the default for self-host. `tasks/integrations.py`; retire/leave-unwired that stub):
- [_impl-report.md](<_impl-report.md>) — Implementation Report — ingestion-pull (Zendesk): Each commit was built strict RED→GREEN (test file written and confirmed failing via `ModuleNotFoundError`/404 before the corresponding production
- [plan_20260705.md](<plan_20260705.md>) — Plan — Zendesk Integration: `ingestion-pull` aspect: `docs/planning/zendesk-integration/ingestion-pull/spec.md`, `docs/planning/zendesk-integration/ingestion-core/spec.md`.

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: In scope; Out of scope; Status: DONE; Commits (in order); 0. Scope recap (from spec); 1. Cross-aspect dependency check (must be true before Phase 3 can go green).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
