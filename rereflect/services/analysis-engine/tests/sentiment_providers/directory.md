# Directory guide: `services/analysis-engine/tests/sentiment_providers`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 6 immediate baseline/preparation files, 0 child directories, and 6 files in its subtree before generated guides/index inventories. Common formats: .py: 6.

## Read first

- [test_base.py](<test_base.py>) — Tests for the SentimentProvider ABC + SentimentScore contract (AC3).
- [test_factory.py](<test_factory.py>) — Tests for SentimentProviderFactory — name -> provider dispatch (AC7).
- [test_lazy_import.py](<test_lazy_import.py>) — Proves torch/transformers are truly optional at import time — the vader path never requires them; requesting/constructing the transformer provider is fine, only scoring with it needs them…
- [test_transformer_provider.py](<test_transformer_provider.py>) — Tests for TransformerSentimentProvider — mocked model/tokenizer, no real weights/download (AC4, AC10, AC11).
- [test_vader_provider.py](<test_vader_provider.py>) — Tests for VaderSentimentProvider — proves the extraction adds zero transformation vs. calling vaderSentiment directly (AC3).
- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): test_base.py: test_sentiment_provider_cannot_be_instantiated_directly, test_subclass_without_score_cannot_be_instantiated, test_minimal_concrete_subclass_can_be_instantiated_and_scores; test_factory.py: test_create_vader_returns_vader_provider, test_create_transformer_returns_transformer_provider, test_create_unknown_provider_raises_value_error; test_lazy_import.py: test_vader_path_does_not_require_torch, test_transformer_path_fails_cleanly_without_torch; test_transformer_provider.py: reset_singleton, _make_mock_tokenizer, _make_mock_model, test_score_maps_softmax_to_contract, test_model_is_per_process_singleton_across_instances;….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
