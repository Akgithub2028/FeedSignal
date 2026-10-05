# Directory guide: `services/analysis-engine/src/analyzer/sentiment_providers`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Analysis/classifier support modules or examples. Inspect inputs, label definitions, model promotion gates, and corresponding tests before changing model behavior.

This directory has 3 immediate baseline/preparation files, 1 child directories, and 6 files in its subtree before generated guides/index inventories. Common formats: .py: 6.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [base.py](<base.py>) — Exports/declarations: SentimentScore, SentimentProvider
- [factory.py](<factory.py>) — Exports/declarations: SentimentProviderFactory

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [providers](<providers/directory.md>).

Direct declarations (navigation cues, not execution results): base.py: SentimentScore, SentimentProvider; factory.py: SentimentProviderFactory.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run focused analysis-engine tests for changed outputs/model gates. Verify optional dependencies and dataset provenance; model claims require held-out evidence.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
