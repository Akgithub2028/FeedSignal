# Directory guide: `docs/planning/oidc-sso`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for oidc sso. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 5 child directories, and 12 files in its subtree before generated guides/index inventories. Common formats: .md: 12.

## Read first

- [prd.md](<prd.md>) — PRD — OIDC Single Sign-On (self-hosted): An operator running a self-hosted Rereflect instance cannot connect their identity provider to login. which an enterprise IT function will accept as the access path to an…
- [understanding.md](<understanding.md>) — Understanding — `oidc-sso` (Phase 2 dig): All paths below are in the worktree. Every claim is cited; where I could not verify something, it is Let an operator of a **self-hosted** Rereflect deployment plug their own…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [auth-test-harness](<auth-test-harness/directory.md>), [oidc-config](<oidc-config/directory.md>), [oidc-docs-and-compose](<oidc-docs-and-compose/directory.md>), [oidc-frontend](<oidc-frontend/directory.md>), [oidc-login-flow](<oidc-login-flow/directory.md>).

Document sections to inspect: 1. Problem Statement; 2. Acceptance Criteria (correctness-only — see the honesty note); 1. What the task is really asking; 2. The headline finding — the "reuse the existing seam" premise is only half right.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
