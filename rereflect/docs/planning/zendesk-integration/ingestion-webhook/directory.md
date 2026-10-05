# Directory guide: `docs/planning/zendesk-integration/ingestion-webhook`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for zendesk integration, aspect ingestion webhook. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect: ingestion-webhook (optional real-time entry point): in real time, reusing the ingestion core. Optional accelerator on top of pull. `X-Zendesk-Webhook-Signature-Timestamp` + **raw body**)); compare against the…
- [_impl-report.md](<_impl-report.md>) — Implementation Report — ingestion-webhook (Zendesk real-time entry point): `backend-connection`, `ingestion-core`, and `ingestion-pull` aspects) RED tests for all five plan phases were written up front in one file
- [plan_20260705.md](<plan_20260705.md>) — Implementation Plan — ingestion-webhook (Zendesk real-time entry point) (2026-07-05): auto-provisioned `zendesk` FeedbackSource) and **ingestion-core** (`ZendeskAdapter`, `_find_matching_sources` zendesk branch in…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: In scope; Out of scope; Status: DONE; Commits (in order); 0. Project Setup / Impact Analysis; Interface contract with ingestion-core (must match — confirm before Phase 4).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
