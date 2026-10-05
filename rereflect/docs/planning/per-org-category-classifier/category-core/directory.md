# Directory guide: `docs/planning/per-org-category-classifier/category-core`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for per org category classifier, aspect category core. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect: category-core (analysis-engine spine): The spine is ~90% generic; only four sentiment touch-points block a category head. Parameterize them (sentiment default preserved, byte-stable) and add a category dataset…
- [plan_20260711.md](<plan_20260711.md>) — Implementation Plan — category-core (analysis-engine spine): This plan is written for an autonomous coding agent to execute unattended, strict TDD, small commits per phase. Every phase: write/extend the failing test(s)…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope (all under `services/analysis-engine/src/analyzer/corrections_classifier/`); 0. Ground truth (verified by reading, 2026-07-11); Phase 1 — `dataset.py`: parameterize label filter + correction_type, add category builder.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
