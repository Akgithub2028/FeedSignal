# Directory guide: `docs/planning/mutation-route-rbac`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for mutation route rbac. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 4 child directories, and 10 files in its subtree before generated guides/index inventories. Common formats: .md: 10.

## Read first

- [prd.md](<prd.md>) — PRD: Mutation-route RBAC: Of 190 in-scope mutation routes in `services/backend-api/src/api/routes/`, 64 carry no role check. Where a `require_feature(...)` gate exists it is not a role gate and always passes under…
- [plan_index_20261002.md](<plan_index_20261002.md>) — Execution order: Tasks 2 and 3 are independent and can be dispatched as parallel agents after 1 is merged on the branch; each agent works strict TDD (RED test first, commit RED, then GREEN). Shared-file caution:…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [backend-gating](<backend-gating/directory.md>), [docs-tracking](<docs-tracking/directory.md>), [frontend-gating](<frontend-gating/directory.md>), [sweep-guard](<sweep-guard/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
