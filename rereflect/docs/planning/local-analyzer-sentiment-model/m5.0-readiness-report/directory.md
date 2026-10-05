# Directory guide: `docs/planning/local-analyzer-sentiment-model/m5.0-readiness-report`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for local analyzer sentiment model, aspect m5.0 readiness report. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — m5.0-readiness-report: `per-org-resolution`, `model-packaging`, or `eval-harness-and-card`. Can be built fully in parallel; owns PRD must-have #8 and `AI-TRACKING.md:313` (M5.0 — Data & Model Readiness…
- [plan_20260710.md](<plan_20260710.md>) — Implementation Plan — m5.0-readiness-report (2026-07-10): is **independent** of the sentiment-provider-core / per-org-resolution / model-packaging / eval-harness-and-card aspects — no ML, no `analysis-engine` changes,…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; Data model grounding (read before coding — exact field names); 1. Project setup; 2. Reference implementations (read before coding).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
