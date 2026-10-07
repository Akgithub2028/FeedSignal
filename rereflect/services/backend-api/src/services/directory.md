# Directory guide: `services/backend-api/src/services`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Backend business logic for analysis, health/churn, copilot, integrations, identity, email, and automation. Some pure services are mirrored in worker-service and must stay consistent.

This directory has 56 immediate baseline/preparation files, 2 child directories, and 80 files in its subtree before generated guides/index inventories. Common formats: .py: 80.

## Read first

- [health_score_service.py](<health_score_service.py>) — Customer health score computation service. Computes a 0-100 health score per customer using churn-heavy weights. Higher score = healthier customer.
- [email_service.py](<email_service.py>) — Email service using Resend for sending transactional emails. Fetches templates from Resend, renders variables locally, then sends.
- [response_sender.py](<response_sender.py>) — Response Sender Service. Handles sending a response through various integration channels: - Slack: thread reply via chat.postMessage - Intercom: admin reply to conversation - Linear:…
- [automation_engine.py](<automation_engine.py>) — AutomationEngine — Phase 2 execution engine for AI Workflow Automation (M4.4). Evaluates active automation rules against events and fires their actions. Dispatch points (callers): -…
- [google_auth.py](<google_auth.py>) — Google OAuth token verification service.
- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [ai_correction_service.py](<ai_correction_service.py>) — AI correction service — shared helper for persisting human-in-the-loop correction/rating signals. Extracted from the internal ``POST /api/v1/ai-corrections`` route so that both the internal…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [copilot](<copilot/directory.md>), [embeddings](<embeddings/directory.md>).

Direct declarations (navigation cues, not execution results): health_score_service.py: _get_org_weights, _compute_usage_component, _compute_crm_component, compute_health_score, _maybe_enqueue_writeback; email_service.py: _is_email_enabled, _get_template, _render_template, _send_email, _send_email_with_from; response_sender.py: send_via_slack, send_via_intercom, send_via_linear, send_via_email; automation_engine.py: _get_redis, AutomationEngine, seed_churn_cooldowns; google_auth.py: GoogleUserInfo, verify_google_token, verify_google_access_token; ai_correction_service.py: urgency_label, create_ai_correction.

Cross-service filename matches: `asana_adapter.py`, `classifier_predict.py`, `classifier_resolver.py`, `segment_service.py`, `sentiment_resolver.py`, `status_sync_core.py`, `usage_decline_labels_core.py`, `usage_score_service.py`. Compare backend/worker semantics and model columns before changing these; filename matches do not prove equivalent implementations.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).

## Owner Linear token lifecycle

`linear_tokens.py` is the single usable-token path for Linear routes and responses. It validates/encrypts access and rotating refresh tokens, records UTC expiry, uses PostgreSQL NOWAIT plus bounded asynchronous retry to avoid event-loop lock starvation, commits both tokens atomically and returns sanitized reconnect/retry errors. Call before other DB mutations. All expired legacy grants need reauthorization. Review the companion `fe20261006a1` migration before deploying; never rotate the existing shared encryption key to repair a connection.
