# Directory guide: `services/worker-service/src/services`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Worker business logic, including deliberate automation/health/segment/classifier mirrors. Keep action-support fixtures, cooldown conventions, and mirrored semantics aligned.

This directory has 32 immediate baseline/preparation files, 0 child directories, and 32 files in its subtree before generated guides/index inventories. Common formats: .py: 32.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [asana_adapter.py](<asana_adapter.py>) — Pure Asana task-state -> status_sync_core category adapter (no I/O). Slice 1 maps only the boolean `completed` field: completed True -> "done" (status_sync_core resolves -> resolved by…
- [automation_churn_trigger.py](<automation_churn_trigger.py>) — automation_churn_trigger — focused `churn_probability_threshold` evaluator for the worker's probability-update seam (Task 4, churn-triggered-playbooks). Why this exists (read before…
- [automation_email_delivery.py](<automation_email_delivery.py>) — Shared worker-side plumbing for the automation `send_customer_email` action (automation-send-customer-email, worker-mirrors aspect). Two things live here: 1. **Delivery-row helpers** —…
- [automation_feedback_trigger.py](<automation_feedback_trigger.py>) — automation_feedback_trigger — worker-side mirror of the `feedback_category_match`, `sentiment_pattern`, and (added for batch-sentiment-trigger, Track B) `batch_sentiment_threshold` triggers…
- [automation_usage_trend_trigger.py](<automation_usage_trend_trigger.py>) — automation_usage_trend_trigger — focused `usage_trend` evaluator for the worker's daily usage-recompute seam (worker-trend-evaluator aspect, usage-trend-automation-trigger PRD, M1/M5). Why…
- [calibration_refit.py](<calibration_refit.py>) — Calibration refit logic — Phase 6.1 (M4.1). Entry point ----------- refit_org(org_id, db) -> dict Pure logic: no Celery, no FastAPI. All DB I/O is synchronous SQLAlchemy. The caller…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): asana_adapter.py: asana_category; automation_churn_trigger.py: _get_redis, _check_cooldown, _set_cooldown, evaluate_churn_probability_triggers, _evaluate_rule; automation_email_delivery.py: create_delivery_row, get_delivery_row, set_delivery_outcome, _err, execute_send_customer_email; automation_feedback_trigger.py: _get_redis, _check_cooldown, _set_cooldown, evaluate_feedback_triggers, _evaluate_rule; automation_usage_trend_trigger.py: _get_redis, _check_cooldown, _set_cooldown, evaluate_usage_trend_triggers, _evaluate_rule; calibration_refit.py: refit_org, _collect_labels, _get_score_for_customer, _fit_isotonic, _serialize_model.

Cross-service filename matches: `asana_adapter.py`, `automation_email_delivery.py`, `classifier_predict.py`, `classifier_resolver.py`, `report_generator.py`, `segment_service.py`, `sentiment_resolver.py`, `status_sync_core.py`. Compare backend/worker semantics and model columns before changing these; filename matches do not prove equivalent implementations.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
