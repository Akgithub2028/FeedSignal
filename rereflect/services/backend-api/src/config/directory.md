# Directory guide: `services/backend-api/src/config`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for config within services/backend-api/src. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 5 immediate baseline/preparation files, 0 child directories, and 5 files in its subtree before generated guides/index inventories. Common formats: .py: 5.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [automation_templates.py](<automation_templates.py>) — Pre-built automation rule templates (M4.4 — Phase 1; template 6 added by usage-trend-automation-trigger's template-and-docs aspect, M10; template 7 added by batch-sentiment-trigger, Track…
- [plans.py](<plans.py>) — Pricing plan configuration for Rereflect. Tiers: - Free: $0, 250 feedback/mo, 2 seats - Pro: $29/mo, 2,500 feedback/mo, 10 seats - Business: $99/mo, 25,000 feedback/mo, 25 seats -…
- [readiness_thresholds.py](<readiness_thresholds.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [system_templates.py](<system_templates.py>) — Default system response templates for Rereflect. These 8 templates are seeded at startup/migration and are read-only. They cannot be edited or deleted by any organization.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): plans.py: _is_self_hosted, get_plan, get_plan_for_feature, has_feature, plan_includes.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
