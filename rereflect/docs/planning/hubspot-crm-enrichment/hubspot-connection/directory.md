# Directory guide: `docs/planning/hubspot-crm-enrichment/hubspot-connection`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for hubspot crm enrichment, aspect hubspot connection. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — hubspot-connection: An org-admin connects their own HubSpot portal by pasting a private-app access token, can test it, see connection status (with last-synced time + a token hint,
- [_impl-report.md](<_impl-report.md>) — HubSpot Connection — Implementation Report: Result: **43 passed** (6 plans + 5 model + 32 routes), 0 failed, 0 errors. Backend full regression (entire test suite run separately in previous session):
- [plan_20260630.md](<plan_20260630.md>) — TDD Implementation Plan — hubspot-connection aspect: `services/backend-api/src/utils/encryption.py:14` — `_get_fernet()` raises producing an unhandled 500 on `POST /connect`. The route **must** catch

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & user outcome; In scope; Status; Commits; HubSpot CRM Enrichment · Rereflect; 1. Project Setup and Impact.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
