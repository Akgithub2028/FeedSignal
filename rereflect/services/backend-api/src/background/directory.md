# Directory guide: `services/backend-api/src/background`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Background dispatch and maintenance support. The production worker owns Celery/Beat; do not infer a separate scheduler from historical architecture diagrams.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .py: 3.

## Read first

- [__init__.py](<__init__.py>) — Background jobs via Celery + Redis.
- [celery_client.py](<celery_client.py>) — Celery client for queueing tasks to worker-service. This module provides a way to queue analysis tasks from the backend-api to the separate worker-service for distributed processing. Redis…
- [gdpr_purge.py](<gdpr_purge.py>) — GDPR Purge Task — deletes user data after the 30-day grace period. This module exposes `check_deletion_requests(db)` which is called: - By the Celery Beat scheduler (daily) - Directly in…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): celery_client.py: get_redis_url, get_celery_app, queue_analyze_feedback, queue_analyze_batch, get_task_status; gdpr_purge.py: _purge_user, check_deletion_requests.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
