# Directory guide: `docs/planning/churn-triggered-playbooks`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for churn triggered playbooks. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [prd.md](<prd.md>) — PRD — Churn-Triggered Playbook Auto-Execution: Rereflect closes most of the churn loop: it computes a calibrated **churn probability** and a **customer health score** (M4.1), and it ships **churn playbooks** — reusable
- [plan_20260718.md](<plan_20260718.md>) — Implementation Plan — Churn-Triggered Playbook Auto-Execution: trigger + a `run_playbook` action + `off/shadow/active` `mode`. Health/`risk_level` auto-runs flow through the backend engine (already dispatched from

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem Statement; Goals & Success Metrics; Architecture decisions (locked); Project Setup / Impact.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
