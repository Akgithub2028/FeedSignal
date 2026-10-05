# Directory guide: `services/worker-service/src`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Worker application modules. Uses its own src package and copied analysis-engine modules; it cannot assume backend-api Python imports are installed.

This directory has 10 immediate baseline/preparation files, 6 child directories, and 101 files in its subtree before generated guides/index inventories. Common formats: .py: 101.

## Read first

- [celery_app.py](<celery_app.py>) — Celery application configuration. Uses Redis Streams as the message broker.
- [config.py](<config.py>) — Worker service configuration. Uses Redis logical databases for isolation: - DB 0: Celery broker (task queue) - DB 1: Session storage (reserved for backend-api) - DB 2: Application cache…
- [database.py](<database.py>) — Database session management for worker service. Shares the same database as backend-api.
- [email.py](<email.py>) — Email service for worker-service. Duplicates core Resend email logic for sending weekly digests.
- [cache.py](<cache.py>) — Cache invalidation utility for worker-service. Connects to Redis DB 2 (application cache) to invalidate stale entries when worker tasks create or modify feedback items.
- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [email_parser.py](<email_parser.py>) — Smart email body parsing for inbound email feedback. Strips forwarding headers, signatures, quoted replies, and HTML to extract clean feedback text from forwarded emails. NOTE: This is a…

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [adapters](<adapters/directory.md>), [clients](<clients/directory.md>), [llm](<llm/directory.md>), [models](<models/directory.md>), [services](<services/directory.md>), [tasks](<tasks/directory.md>).

Direct declarations (navigation cues, not execution results): config.py: Settings, get_redis_url; database.py: get_db_session; email.py: _is_email_enabled, _get_template, _render_template, _send_email, _send_with_template; cache.py: _get_redis, cache_invalidate; email_parser.py: _HTMLTextExtractor, _html_to_text, _remove_forwarding_headers, _remove_signatures, _remove_quoted_replies.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
