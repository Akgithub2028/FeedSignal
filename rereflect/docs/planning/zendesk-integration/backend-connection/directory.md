# Directory guide: `docs/planning/zendesk-integration/backend-connection`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for zendesk integration, aspect backend connection. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect: backend-connection: Fernet-encrypted `api_token` (+ encrypted nullable `webhook_secret`), `subdomain`, `email`, `token_hint`, identity (`account_user_id`, `display_name`), `is_active`, `last_synced_at`,
- [_impl-report.md](<_impl-report.md>) — Implementation report — Zendesk backend-connection aspect: Implemented the Zendesk BYOK connection slice end-to-end, mirroring the Jira Ran `alembic heads` **twice** (once before writing the migration, once again
- [plan_20260705.md](<plan_20260705.md>) — Plan — Zendesk backend-connection (aspect): This plan covers **only** the backend-connection aspect per `docs/planning/zendesk-integration/backend-connection/spec.md`: the

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: In scope; Out of scope; Summary; Alembic heads — confirmed; 0. Alembic heads — resolved; 1. Setup / Impact.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
