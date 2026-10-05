# Directory guide: `docs/planning/customer-360-unified-timeline/timeline-service-v1`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for customer 360 unified timeline, aspect timeline service v1. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — `timeline-service-v1`: Today `GET /api/v1/customers/{email}/activity` merges 5 sources inline and truncates to 10 (`routes/customers.py:512-611`). Usage (M3.2) and churn (M4.1) are absent and there is no
- [plan_20260629.md](<plan_20260629.md>) — Implementation Plan — `timeline-service-v1`: - Existing `/activity` logic to port: `src/api/routes/customers.py:512-611` (`get_customer_activity`). - `ActivityEvent` / `CustomerActivityResponse` schemas:…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; 0. Impact analysis (existing codebase — no scaffolding); Source-of-truth table (org-scoped, `organization_id` on every query).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
