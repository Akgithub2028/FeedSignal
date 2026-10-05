# Directory guide: `services/backend-api`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

FastAPI API, organization-scoped authorization, persistence, integrations, Alembic migrations, and service tests. Entry point is src/api/main.py; PostgreSQL is the production store.

This directory has 12 immediate baseline/preparation files, 6 child directories, and 727 files in its subtree before generated guides/index inventories. Common formats: .py: 702, .json: 4, .html: 4, .sh: 3.

## Read first

- [Dockerfile](<Dockerfile>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [README.md](<README.md>) — Backend API
- [test_api.sh](<test_api.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [test_week2.sh](<test_week2.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [.env.example](<.env.example>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [alembic.ini](<alembic.ini>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [pytest.ini](<pytest.ini>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [alembic](<alembic/directory.md>), [eval_results](<eval_results/directory.md>), [scripts](<scripts/directory.md>), [src](<src/directory.md>), [templates](<templates/directory.md>), [tests](<tests/directory.md>).

Document sections to inspect: Purpose; Tech Stack.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../UNANSWERED_SECRETS.md>).
