# Directory guide: `services/backend-api/src/api`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

FastAPI app registration, auth/dependencies, and API route modules. Start at main.py, auth.py, and dependencies.py for mounting, session, and organization boundaries.

This directory has 4 immediate baseline/preparation files, 3 child directories, and 85 files in its subtree before generated guides/index inventories. Common formats: .py: 85.

## Read first

- [main.py](<main.py>) — Exports/declarations: seed_copilot_system_templates, warn_unconfigured_webhook_secrets, run_migrations, lifespan, CacheControlMiddleware
- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [auth.py](<auth.py>) — Exports/declarations: hash_password, verify_password, create_access_token, decode_access_token
- [dependencies.py](<dependencies.py>) — Exports/declarations: get_current_user, get_current_user_allow_deactivated, get_current_org, get_current_usage, check_feedback_limit

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [public](<public/directory.md>), [routes](<routes/directory.md>), [schemas](<schemas/directory.md>).

Direct declarations (navigation cues, not execution results): main.py: GET /, GET /health, GET /worker/status, GET /tasks/{task_id}; auth.py: hash_password, verify_password, create_access_token, decode_access_token; dependencies.py: get_current_user, get_current_user_allow_deactivated, get_current_org, get_current_usage, check_feedback_limit.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
