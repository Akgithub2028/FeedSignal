# Directory guide: `docs/planning/zendesk-status-sync/webhook-realtime`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for zendesk status sync, aspect webhook realtime. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect: webhook-realtime: Near-real-time status-sync: when Zendesk sends a ticket-update webhook, reconcile that single ticket's status immediately (subject to the same opt-in + change-gate), instead of waiting for the…
- [dig.md](<dig.md>) — Phase 0 dig — webhook-realtime event shape (GO)
- [plan_20260712.md](<plan_20260712.md>) — Plan — webhook-realtime (2026-07-12)

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; Receiver (existing); Payload is OPERATOR-AUTHORED (Liquid template), not Zendesk-native; Service touched; Phase 0 — Spike: map the current receiver + confirm event shape (READ-ONLY, no code).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
