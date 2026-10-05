# Directory guide: `docs/planning/automation-playbook-dispatch-commit/dispatch-ordering`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for automation playbook dispatch commit, aspect dispatch ordering. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Spec — dispatch-ordering: publishing its id, so the worker can always find it (PRD M1–M3). Deferred dispatch; retry on `not found`; publish-failure handling; trigger/action restriction.
- [plan_20260925.md](<plan_20260925.md>) — Plan — dispatch-ordering (2026-09-25): mirroring `tests/test_automation_engine_send_customer_email.py:445-484` (spy `db.commit`, Run → FAIL (commit only at `_evaluate_rule:203`, after send_task).

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: In scope; Out of scope; Phase 1 — Backend engine (`services/backend-api`); Phase 2 — Worker mirrors (`services/worker-service`, `SENTRY_DSN=""`).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
