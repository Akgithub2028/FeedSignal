# Directory guide: `docs/planning/usage-decline-churn-labels/frontend-settings-and-evidence`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for usage decline churn labels, aspect frontend settings and evidence. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect — frontend-settings-and-evidence: The operator needs somewhere to turn this on, a way to judge whether it is working, and an evidence display that isn't CRM-shaped. Today the review queue's `EvidenceCell` reads…
- [plan_20260723.md](<plan_20260723.md>) — Implementation Plan — frontend-settings-and-evidence: `node_modules` is per-worktree — run `npm install` first if it is missing. against the fixed `evidence` key names (below) and the settings API already shipped.

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice; User outcome; 0. Context the executing agent must not re-derive; 1. The contracts this aspect consumes (already fixed).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
