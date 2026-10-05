# Directory guide: `services/backend-api/src/api/routes`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Product and integration HTTP endpoints. OAuth callbacks/webhooks have distinct authentication rules; routes normally derive organization identity from the authenticated principal.

This directory has 77 immediate baseline/preparation files, 0 child directories, and 77 files in its subtree before generated guides/index inventories. Common formats: .py: 77.

## Read first

- [auth.py](<auth.py>) — Exports/declarations: signup, login, get_current_user_info, get_preferences, update_preferences
- [feedback.py](<feedback.py>) — Exports/declarations: get_sentiment_analyzer, get_categorizers, analyze_single_feedback, FeedbackCreateRequest, UrgentUpdateRequest
- [integrations.py](<integrations.py>) — Integrations API routes for managing Slack, Intercom, and other third-party integrations.
- [source_webhooks.py](<source_webhooks.py>) — Webhook endpoints for receiving events from external sources (Slack, Intercom, generic webhooks). These endpoints handle signature verification and queue events for async processing.
- [usage_webhooks.py](<usage_webhooks.py>) — Inbound product-usage event receiver. POST /api/v1/webhooks/usage Accepts a Segment-compatible normalized batch of usage events from self-hosted operators. Authentication uses the existing…
- [jira_integration.py](<jira_integration.py>) — Jira Cloud integration routes (backend-connection aspect, Phase 3). Routes: POST /api/v1/integrations/jira/connect — validate + encrypt + store GET /api/v1/integrations/jira/status —…
- [linear_integration.py](<linear_integration.py>) — Linear integration API routes. Covers: OAuth flow, issue creation, configuration endpoints (team/status mappings), and proxy endpoints to the Linear API (teams, projects, labels).

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): auth.py: POST /signup, POST /login, GET /me, GET /me/preferences (additional routes in source); feedback.py: POST /, GET /, GET /{feedback_id}, DELETE /{feedback_id} (additional routes in source); integrations.py: GET /, POST /slack/webhook, POST /discord/webhook, POST /teams/webhook (additional routes in source); source_webhooks.py: POST /slack/events, POST /inbound/{webhook_id}, POST /intercom/events, POST /zendesk/events; usage_webhooks.py: POST ; jira_integration.py: POST /connect, GET /status, DELETE /disconnect, POST /test (additional routes in source); linear_integration.py: GET /connect, GET /callback, DELETE /disconnect, GET /status….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

Ownership queue includes original-domain inbound addresses, admin-email defaults, OAuth/webhook configuration, and public URL settings. Usage webhook commit/dispatch ordering requires M1 reproduction.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
