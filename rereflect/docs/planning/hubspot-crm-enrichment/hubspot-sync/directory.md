# Directory guide: `docs/planning/hubspot-crm-enrichment/hubspot-sync`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for hubspot crm enrichment, aspect hubspot sync. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — hubspot-sync: After connecting, the operator's HubSpot Contacts/Companies/Deals are pulled, matched to Rereflect customers by email, and written to a per-customer enrichment
- [_impl-report.md](<_impl-report.md>) — HubSpot Sync — Implementation Report: Result: **4 passed**, 0 failed. (Confirmed during Phase 5 GREEN run; full backend suite not re-run due to ~83s Sentry initialization overhead per isolated run.) The existing…
- [plan_20260630.md](<plan_20260630.md>) — Tech Plan — hubspot-sync: This aspect delivers the data-movement layer of HubSpot CRM enrichment. After the `hubspot-connection` aspect establishes the `hubspot_integrations` table and token encryption, this aspect: Out…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & user outcome; In scope; Status; Commits; 1. Context and Scope; Closest analogues in codebase.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
