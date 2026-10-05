# Directory guide: `docs/planning/automation-send-customer-email/action-core`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for automation send customer email, aspect action core. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Spec — action-core (backend action type + delivery model): The automations engine has no way to email the customer. This aspect adds the backend half: the `send_customer_email` action type, its config validation, the
- [plan_20260819.md](<plan_20260819.md>) — Plan — action-core (backend action type + delivery model): Scope: **backend-api only.** The worker task (`tasks.outreach.send_automation_email`), the three worker mirrors, the frontend editor, the seeded template and…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice; In-scope (backend-api only); 1. Project Setup Checklist; 2. Implementation Phases (strict TDD — failing tests first, each phase green before the next).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
