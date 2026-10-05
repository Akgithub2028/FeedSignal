# Directory guide: `docs/planning/scheduled-ai-reports`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for scheduled ai reports. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 4 child directories, and 11 files in its subtree before generated guides/index inventories. Common formats: .md: 11.

## Read first

- [prd.md](<prd.md>) — PRD — Scheduled & Emailed AI Reports: Rereflect's On-Demand AI Reports (M2.4, `COMPLETE`) require a user to open the Copilot (Cmd+K) and ask for a report each time. The only recurring communication today is the
- [understanding.md](<understanding.md>) — Understanding note — scheduled & emailed AI reports (Phase 2 dig): A follow-on slice of shipped M2.4 On-Demand AI Reports (`AI-TRACKING.md:51`; non-goals at `PRD-ON-DEMAND-AI-REPORTS.md:37-38`): let an org configure a…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [backend-schedule-crud](<backend-schedule-crud/directory.md>), [frontend-scheduled-reports-ui](<frontend-scheduled-reports-ui/directory.md>), [worker-email-delivery](<worker-email-delivery/directory.md>), [worker-scheduled-generation](<worker-scheduled-generation/directory.md>).

Document sections to inspect: 1. Problem Statement; 2. Goals & Success Metrics; What this feature really is; Shipped pieces we reuse (verified).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
