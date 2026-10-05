# Directory guide: `docs/planning/hubspot-crm-enrichment/crm-profile-and-timeline`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for hubspot crm enrichment, aspect crm profile and timeline. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — crm-profile-and-timeline: A CS lead viewing `/customers/{email}` sees a **CRM / Company** card (company, lifecycle stage, ARR, renewal date, primary deal + stage + amount) and CRM events
- [_impl-report.md](<_impl-report.md>) — Implementation Report — `crm-profile-and-timeline`: A single enrichment snapshot cannot detect a deal stage *change* — there is no per-sync history table in v1. `crm_contact_synced` and `crm_renewal_upcoming` are the…
- [plan_20260630.md](<plan_20260630.md>) — Implementation Plan — `crm-profile-and-timeline`: row and emit these EXACT `Optional` fields (`None` when the row/value is absent): `CustomerProfileResponse` (customers.py) and `PublicCustomerProfile360` (public_api.py)

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & user outcome; In scope; Commits; Test Commands + Results; Pinned shared contract (do not deviate); 1. Project Setup Checklist.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
