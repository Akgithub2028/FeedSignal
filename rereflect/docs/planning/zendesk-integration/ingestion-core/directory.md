# Directory guide: `docs/planning/zendesk-integration/ingestion-core`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for zendesk integration, aspect ingestion core. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect: ingestion-core: `FeedbackItem`. Both entry points (pull, webhook) funnel through this. - `check_triggers(event_type, event_data, triggers)` — match configured triggers (new-ticket;
- [_impl-report.md](<_impl-report.md>) — Implementation Report — ingestion-core (Zendesk): Each `feat(zendesk)` commit corresponds 1:1 to a plan phase (1–6), built strict RED→GREEN (test written and confirmed failing before the production code was
- [plan_20260705.md](<plan_20260705.md>) — Implementation Plan — ingestion-core: backend). **Blocks:** `ingestion-pull`, `ingestion-webhook`. `services/worker-service` only: `src/adapters/zendesk.py` (new), `src/adapters/__init__.py`

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: In scope; Out of scope; Status: DONE; Commits (in order); Services touched; Contracts locked in this aspect.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
