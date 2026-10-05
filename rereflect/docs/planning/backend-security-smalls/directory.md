# Directory guide: `docs/planning/backend-security-smalls`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for backend security smalls. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [prd.md](<prd.md>) — PRD — Backend security smalls (oauth state, generic webhook secret, events-emit): TTL: OAuth callbacks (Slack :841-871, Intercom :1032-1062) fail intermittently on any multi-replica backend, and entries never expire…
- [plan_20260818.md](<plan_20260818.md>) — Implementation plan — backend-security-smalls (2026-08-18): Source: `docs/planning/backend-security-smalls/prd.md`. House commit style. - `services/backend-api/src/api/routes/integrations.py` — delete `oauth_states`

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Item 1 — P3: OAuth state out of the process dict; Item 2 — S1: generic inbound webhook secret posture; Phase 1 — Stateless OAuth state (Slack + Intercom + Linear); Phase 2 — Generic webhook: mint-and-require on new sources.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
