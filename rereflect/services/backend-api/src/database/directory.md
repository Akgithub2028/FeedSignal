# Directory guide: `services/backend-api/src/database`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

SQLAlchemy engine/session initialization from DATABASE_URL. Production defaults target PostgreSQL; session and transaction boundaries affect queued job visibility.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .py: 2.

## Read first

- [session.py](<session.py>) — Exports/declarations: get_db
- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): session.py: get_db.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
