# Directory guide: `services/worker-service/src/models`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Worker persistence mirrors. Align columns and semantic contracts with backend models and migrations; identical filenames are a navigation cue, not proof of equal contents.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .py: 3.

## Read first

- [__init__.py](<__init__.py>) — Database models for worker service. Imports models from backend-api to ensure consistency. Note: In production, these should be in a shared package. For now, we duplicate the essential…
- [automation_execution.py](<automation_execution.py>) — AutomationExecution — lightweight SQLAlchemy mirror for worker-service. The full model lives in backend-api. This mirror is used by src/tasks/automation.py for the weekly purge task. No…
- [automation_rule.py](<automation_rule.py>) — AutomationRule — lightweight SQLAlchemy mirror for worker-service. The full model + engine live in backend-api (`services/backend-api/src/models/automation_rule.py`). This mirror is used…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): __init__.py: User, Organization, Subscription, UsageRecord, FeedbackItem; automation_execution.py: AutomationExecution; automation_rule.py: AutomationRule.

Cross-service filename matches: `automation_execution.py`, `automation_rule.py`. Compare backend/worker semantics and model columns before changing these; filename matches do not prove equivalent implementations.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
