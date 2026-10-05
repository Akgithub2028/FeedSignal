# Directory guide: `services/analysis-engine/src/analyzer/sentiment_providers/providers`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Analysis/classifier support modules or examples. Inspect inputs, label definitions, model promotion gates, and corresponding tests before changing model behavior.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .py: 3.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [transformer.py](<transformer.py>) — Exports/declarations: _get_model_and_tokenizer, TransformerSentimentProvider
- [vader.py](<vader.py>) — Exports/declarations: VaderSentimentProvider

## Files, children, and contracts

[Complete file inventory](<../../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): transformer.py: _get_model_and_tokenizer, TransformerSentimentProvider; vader.py: VaderSentimentProvider.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run focused analysis-engine tests for changed outputs/model gates. Verify optional dependencies and dataset provenance; model claims require held-out evidence.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../../UNANSWERED_SECRETS.md>).
