# Directory guide: `docs/planning/per-org-churn-model/worker-churn-trainer-and-schedule`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for per org churn model, aspect worker churn trainer and schedule. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Spec — worker-churn-trainer-and-schedule (slice 2b): A scheduled per-org training task that runs the churn core's A/B, promotes on a measurable margin, and stays reversible — following the M5.2 worker conventions…
- [plan_20260814.md](<plan_20260814.md>) — Implementation Plan — worker-churn-trainer-and-schedule (aspect 4, slice 2b): core (aspect 3) via lazy imports. Depends on aspect 1 (incumbent real) and aspect 5's migration for the OrgAIConfig columns — **read them…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice; In scope; 1. Project setup checklist; 2. Implementation phases (strict TDD).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
