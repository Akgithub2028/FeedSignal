# Directory guide: `services/backend-api/src`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Backend application modules. Routes consume schemas/services/models; authentication derives tenant identity; transaction behavior and background dispatch must be inspected together.

This directory has 4 immediate baseline/preparation files, 10 child directories, and 270 files in its subtree before generated guides/index inventories. Common formats: .py: 270.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [notification_dispatch_helpers.py](<notification_dispatch_helpers.py>) — Helpers for dispatching targeted workflow notifications directly from the backend-api. Creates Notification records in the database for specific users, respecting their alert preferences.
- [seed.py](<seed.py>) — Seed script to create initial owner user. Runs on application startup if owner user doesn't exist.
- [seed_byok.py](<seed_byok.py>) — Env-seed BYOK keys for single-tenant self-hosted convenience (OSS Pivot Q1). On application startup, for each of the three provider env vars that is present, ensure an OrgApiKey row exists…

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [api](<api/directory.md>), [background](<background/directory.md>), [config](<config/directory.md>), [database](<database/directory.md>), [models](<models/directory.md>), [schemas](<schemas/directory.md>), [scripts](<scripts/directory.md>), [services](<services/directory.md>), [templates](<templates/directory.md>), [utils](<utils/directory.md>).

Direct declarations (navigation cues, not execution results): notification_dispatch_helpers.py: _create_targeted_notifications, dispatch_status_changed, dispatch_feedback_assigned, dispatch_health_drop_alert_impl, dispatch_note_added; seed.py: seed_admin_user, seed_system_templates; seed_byok.py: seed_byok_keys_from_env.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
