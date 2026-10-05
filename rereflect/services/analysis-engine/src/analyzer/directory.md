# Directory guide: `services/analysis-engine/src/analyzer`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Core analysis modules consumed by backend/worker packaging. Preserve normalized outputs, model-version semantics, and optional local/cloud behavior.

This directory has 7 immediate baseline/preparation files, 3 child directories, and 28 files in its subtree before generated guides/index inventories. Common formats: .py: 28.

## Read first

- [__init__.py](<__init__.py>) — Feedback analyzer package.
- [categorizer.py](<categorizer.py>) — Categorizers for pain points, feature requests, and urgent feedback.
- [core.py](<core.py>) — Core feedback analyzer implementation.
- [extractors.py](<extractors.py>) — Extractors for pain points, feature requests, and patterns.
- [models.py](<models.py>) — Data models for feedback analysis.
- [sentiment.py](<sentiment.py>) — Sentiment analysis — composes a pluggable SentimentProvider with provider-independent label / is_extreme / churn_risk logic. Default provider ('vader') is byte-identical to the…
- [tag_extractor.py](<tag_extractor.py>) — Tag extraction module for categorizing feedback.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [churn_classifier](<churn_classifier/directory.md>), [corrections_classifier](<corrections_classifier/directory.md>), [sentiment_providers](<sentiment_providers/directory.md>).

Direct declarations (navigation cues, not execution results): categorizer.py: CategorizationResult, PainPointCategorizer, FeatureRequestCategorizer, UrgentCategorizer; core.py: FeedbackAnalyzer; extractors.py: PainPointExtractor, FeatureRequestExtractor; models.py: FeedbackItem, FeedbackInput, PainPoint, FeatureRequest, SentimentByPeriod; sentiment.py: SentimentAnalyzer; tag_extractor.py: TagExtractor.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run focused analysis-engine tests for changed outputs/model gates. Verify optional dependencies and dataset provenance; model claims require held-out evidence.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
