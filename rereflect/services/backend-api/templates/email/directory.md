# Directory guide: `services/backend-api/templates/email`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for email within services/backend-api/templates. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 4 immediate baseline/preparation files, 0 child directories, and 4 files in its subtree before generated guides/index inventories. Common formats: .html: 4.

## Read first

- [alert_notification.html](<alert_notification.html>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [daily_alert_digest.html](<daily_alert_digest.html>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [member_removed.html](<member_removed.html>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [role_change.html](<role_change.html>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
