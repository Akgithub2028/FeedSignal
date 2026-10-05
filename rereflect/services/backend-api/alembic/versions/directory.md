# Directory guide: `services/backend-api/alembic/versions`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Versioned database changes. Migration identifiers and dependency links are persistent upgrade contracts; do not rewrite applied migrations to rebrand the product.

This directory has 103 immediate baseline/preparation files, 0 child directories, and 103 files in its subtree before generated guides/index inventories. Common formats: .py: 103.

## Read first

- [093c65b07d95_fix_slack_alert_logs_feedback_id_.py](<093c65b07d95_fix_slack_alert_logs_feedback_id_.py>) — fix slack_alert_logs feedback_id ondelete set null Revision ID: 093c65b07d95 Revises: d3e4f5g6h7i8 Create Date: 2026-02-13 03:11:17.940274
- [0a3382154c27_add_usage_churn_label_config.py](<0a3382154c27_add_usage_churn_label_config.py>) — add_usage_churn_label_config Revision ID: 0a3382154c27 Revises: a1c2d3e4f5a6 Create Date: 2026-07-23 00:00:00.000000 usage-decline-churn-labels — config-and-migration aspect. Adds…
- [0bf182dad44d_playbook_tasks_table.py](<0bf182dad44d_playbook_tasks_table.py>) — playbook tasks table Revision ID: 0bf182dad44d Revises: fb57e62a2820 Create Date: 2026-08-27 02:57:08.281148 playbook-action-types M3 — durable follow-up tasks created by create_task /…
- [12a1003fbfe0_shadow_repaired_automation_triggers.py](<12a1003fbfe0_shadow_repaired_automation_triggers.py>) — shadow_repaired_automation_triggers Revision ID: 12a1003fbfe0 Revises: b2262e51eeb5 Create Date: 2026-07-29 02:01:49.626081 Phase 4 of the worker-trigger-mirror aspect…
- [16905e989875_add_usage_event.py](<16905e989875_add_usage_event.py>) — add_usage_event Revision ID: 16905e989875 Revises: z5a6b7c8d9e0 Create Date: 2026-06-28 21:29:20.783877 Creates the ``usage_events`` raw-log table for the product-usage ingestion receiver…
- [241f650d7068_add_active_days_14d_to_customer_usage.py](<241f650d7068_add_active_days_14d_to_customer_usage.py>) — add active_days_14d to customer_usage Revision ID: 241f650d7068 Revises: u4v5w6x7y8z9 Create Date: 2026-07-21 21:19:14.137905 Adds the 14-day active-days window field used by the…
- [3cb9a0d1456b_add_churn_classifier_mode.py](<3cb9a0d1456b_add_churn_classifier_mode.py>) — add_churn_classifier_mode Revision ID: 3cb9a0d1456b Revises: f6a7b8c9d0e1 Create Date: 2026-08-14 03:55:59.883435 per-org-churn-model (churn-predict-seam-resolver, data layer): -…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): 093c65b07d95_fix_slack_alert_logs_feedback_id_.py: upgrade, downgrade; 0a3382154c27_add_usage_churn_label_config.py: upgrade, downgrade; 0bf182dad44d_playbook_tasks_table.py: upgrade, downgrade; 12a1003fbfe0_shadow_repaired_automation_triggers.py: upgrade, downgrade; 16905e989875_add_usage_event.py: upgrade, downgrade; 241f650d7068_add_active_days_14d_to_customer_usage.py: upgrade, downgrade; 3cb9a0d1456b_add_churn_classifier_mode.py: upgrade, downgrade.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
