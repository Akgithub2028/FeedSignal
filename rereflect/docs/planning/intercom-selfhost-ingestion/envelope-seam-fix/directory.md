# Directory guide: `docs/planning/intercom-selfhost-ingestion/envelope-seam-fix`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for intercom selfhost ingestion, aspect envelope seam fix. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — `envelope-seam-fix`: Intercom webhook deliveries are received and authenticated, but produce **no feedback item, in any release**. The backend route hands the worker adapter a payload shape the
- [plan_20260731.md](<plan_20260731.md>) — Implementation Plan — `envelope-seam-fix`: 3. Confirm `IntercomConnector.fetch_new_items` returns `[]` and creates nothing (`worker-service/src/tasks/integrations.py:170-177`) — it is deleted in a later aspect.

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice; Which side is the bug — settled by the tests, not by preference; 1. Project Setup Checklist; 2. Implementation Phases.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
