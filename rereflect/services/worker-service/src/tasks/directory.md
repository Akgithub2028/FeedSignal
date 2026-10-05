# Directory guide: `services/worker-service/src/tasks`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Celery task entry points for ingestion, analysis, reports, churn/usage, notifications, CRM, and tracker sync. Inspect committed-record visibility, retries, idempotency, and tenant arguments before edits.

This directory has 28 immediate baseline/preparation files, 0 child directories, and 28 files in its subtree before generated guides/index inventories. Common formats: .py: 28.

## Read first

- [analysis.py](<analysis.py>) — Analysis tasks for processing customer feedback. Migrated from APScheduler to Celery for distributed processing. Supports LLM-powered categorization (OpenAI) with keyword fallback.
- [source_events.py](<source_events.py>) — Source event processing tasks. Handles events from all source types (Slack, webhooks, etc.) using the adapter pattern.
- [usage_metrics.py](<usage_metrics.py>) — Celery tasks for product-usage rollup and scoring (aspect 3), plus the usage-history-snapshot aspect's daily storage and pruning. Tasks: process_usage_event — triggered per event from…
- [scheduled_reports.py](<scheduled_reports.py>) — Celery tasks for scheduled AI report generation (worker-scheduled-generation). Beat schedule (registered in celery_app.py): - generate_scheduled_reports → hourly at :15 UTC; filters due…
- [jira_sync.py](<jira_sync.py>) — Inbound Jira status-sync poller (jira-status-sync/inbound-status-sync, Phase 4). See docs/planning/jira-status-sync/inbound-status-sync/plan_20260711.md. Tasks: sync_all_jira — fan-out over…
- [outreach.py](<outreach.py>) — Outreach send tasks — the only place an outreach email is actually sent. send_outreach_email(campaign_id, recipient_id) — send one outreach email via…
- [churn_classifier_training.py](<churn_classifier_training.py>) — Celery tasks for weekly per-org churn classifier retraining — worker-churn- trainer-and-schedule aspect (M5.3 per-org-churn-model). Beat schedule (registered in celery_app.py): -…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): analysis.py: _get_redis, _get_cache_redis, _invalidate_org_cache, get_sentiment_analyzer, get_tag_extractor; source_events.py: _decrypt, process_source_event, _find_matching_sources, _process_event_for_source, _log_event; usage_metrics.py: _compute_rollup_from_events, _rederive_windows, _upsert_rollup, _call_update_health, _write_usage_history_snapshots; scheduled_reports.py: _cutoff, _is_due, _claim_schedule, _report_title, _generate_for_schedule; jira_sync.py: _decrypt, _persist_terminal_status, _sync_jira_org_body, sync_all_jira, sync_jira_org; outreach.py: send_outreach_email, _process_recipient, send_automation_email,….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

M1 queue includes health-component/churn-probability direction, usage event visibility and full-history scans, and training/serving feature parity. Source findings are unexecuted.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
