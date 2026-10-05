# Directory guide: `services/analysis-engine/tests`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 8 immediate baseline/preparation files, 3 child directories, and 34 files in its subtree before generated guides/index inventories. Common formats: .py: 34.

## Read first

- [test_analyzer.py](<test_analyzer.py>) — Tests for the main analyzer.
- [test_api.py](<test_api.py>) — Tests for the API endpoints.
- [test_custom_categorizer.py](<test_custom_categorizer.py>) — TDD tests for Feature B1: custom category augmentation of keyword categorisers. Tests cover PainPointCategorizer, FeatureRequestCategorizer, and UrgentCategorizer after the…
- [test_extractors.py](<test_extractors.py>) — Tests for extractors.
- [test_sentiment.py](<test_sentiment.py>) — Tests for sentiment analyzer.
- [test_sentiment_characterization.py](<test_sentiment_characterization.py>) — Characterization test — pins SentimentAnalyzer().analyze()'s exact output for a fixed set of inputs, against the pre-refactor sentiment.py. This is the load-bearing safety net for the…
- [test_sentiment_fallback.py](<test_sentiment_fallback.py>) — Tests for SentimentAnalyzer's runtime fallback to VADER when the configured provider's score() raises (PRD #9) — analyze() must never raise.

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [churn_classifier](<churn_classifier/directory.md>), [corrections_classifier](<corrections_classifier/directory.md>), [sentiment_providers](<sentiment_providers/directory.md>).

Direct declarations (navigation cues, not execution results): test_analyzer.py: analyzer, sample_feedback, test_complete_analysis, test_sentiment_summary, test_pain_point_extraction; test_api.py: client, sample_payload, test_root_endpoint, test_health_check, test_analyze_endpoint; test_custom_categorizer.py: TestPainPointCategorizerCustom, TestFeatureRequestCategorizerCustom, TestUrgentCategorizerCustom; test_extractors.py: pain_point_extractor, feature_request_extractor, test_complaint_detection, test_pain_point_clustering, test_feature_request_detection; test_sentiment.py: analyzer, test_positive_sentiment, test_negative_sentiment, test_neutral_sentiment, test_extreme_negative_detection;….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
