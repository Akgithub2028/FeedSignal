# Directory guide: `docs/planning/oidc-sso/auth-test-harness`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for oidc sso, aspect auth test harness. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — `auth-test-harness`: must not change behaviour** (PRD S4). Before any OIDC production code is written, we need a green, trustworthy characterization net around the **current** auth behaviour, so that any…
- [plan_20260716.md](<plan_20260716.md>) — Implementation Plan — `auth-test-harness`: Verified live in the worktree on 2026-07-16 — the PRD's R3 ("zero auth tests") is **frontend-only**: the substance, but small and infra-ready. The PRD's "M1 may dwarf the…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & user outcome; ⚠️ Reality correction (verified 2026-07-16, supersedes PRD R3); 0. Reality check baked into this plan (read first); 1. Project Setup Checklist.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
