# Directory guide: `docs/planning/intercom-selfhost-ingestion`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for intercom selfhost ingestion. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 1 immediate baseline/preparation files, 6 child directories, and 9 files in its subtree before generated guides/index inventories. Common formats: .md: 9.

## Read first

- [prd.md](<prd.md>) — PRD — Intercom ingestion, operable on a self-host: the landing page, and documented in `docs/SELF_HOSTING.md:1571`. A self-hoster can click Connect, complete an OAuth flow, see webhook events arrive — and never get a…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [cleanup-and-docs](<cleanup-and-docs/directory.md>), [envelope-seam-fix](<envelope-seam-fix/directory.md>), [pull-sync](<pull-sync/directory.md>), [tenancy-discriminator](<tenancy-discriminator/directory.md>), [token-paste-connect](<token-paste-connect/directory.md>), [webhook-per-org-secret](<webhook-per-org-secret/directory.md>).

Document sections to inspect: Problem Statement; Why the credibility cost is the real cost.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
