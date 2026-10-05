# Directory guide: `services/backend-api/src/models`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

SQLAlchemy persistence contracts. Backend and worker carry mirrored models; schema changes require aligned mirrors and an Alembic migration.

This directory has 71 immediate baseline/preparation files, 0 child directories, and 71 files in its subtree before generated guides/index inventories. Common formats: .py: 71.

## Read first

- [organization.py](<organization.py>) — Exports/declarations: Organization
- [user.py](<user.py>) — Exports/declarations: User
- [feedback.py](<feedback.py>) — Exports/declarations: FeedbackItem
- [customer_health.py](<customer_health.py>) — Exports/declarations: CustomerHealth
- [integration.py](<integration.py>) — Exports/declarations: Integration, SlackAlertLog
- [linear_integration.py](<linear_integration.py>) — Exports/declarations: LinearIntegration, LinearTeamMapping, LinearStatusMapping, FeedbackLinearIssue
- [jira_integration.py](<jira_integration.py>) — Jira Cloud integration model. One row per organization. api_token is Fernet-encrypted via encrypt_api_key (never stored plaintext). Encryption happens in the route layer, not here. See…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): organization.py: Organization; user.py: User; feedback.py: FeedbackItem; customer_health.py: CustomerHealth; integration.py: Integration, SlackAlertLog; linear_integration.py: LinearIntegration, LinearTeamMapping, LinearStatusMapping, FeedbackLinearIssue; jira_integration.py: JiraIntegration, FeedbackJiraIssue.

Cross-service filename matches: `automation_email_delivery.py`, `automation_execution.py`, `automation_rule.py`. Compare backend/worker semantics and model columns before changing these; filename matches do not prove equivalent implementations.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

Customer identity currently includes email-based health uniqueness; stable account identities and multi-issue opportunity evidence are later implementation milestones.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
