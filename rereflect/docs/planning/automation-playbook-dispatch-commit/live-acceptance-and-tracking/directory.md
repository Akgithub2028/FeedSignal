# Directory guide: `docs/planning/automation-playbook-dispatch-commit/live-acceptance-and-tracking`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for automation playbook dispatch commit, aspect live acceptance and tracking. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Spec — live-acceptance-and-tracking: real Celery worker from the worktree on an isolated Redis DB index; drive `evaluate_churn_probability_triggers` against an active `churn_probability_threshold` rule with a
- [evidence.md](<evidence.md>) — Live acceptance evidence — 2026-09-25: rule (threshold 0.5, `run_playbook` → that playbook), 40 `customer_health_scores` rows. (`ValueError: not enough values to unpack` in `fast_trace_task`) before running any task.
- [plan_20260925.md](<plan_20260925.md>) — Plan — live-acceptance-and-tracking (2026-09-25): `churn_probability_threshold` rule (threshold low, cooldown 1h) with `run_playbook`, a `CustomerHealth`

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: In scope; Acceptance criteria; Setup; Results.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
