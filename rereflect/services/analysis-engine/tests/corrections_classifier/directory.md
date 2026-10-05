# Directory guide: `services/analysis-engine/tests/corrections_classifier`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 10 immediate baseline/preparation files, 0 child directories, and 10 files in its subtree before generated guides/index inventories. Common formats: .py: 10.

## Read first

- [test_dataset.py](<test_dataset.py>) — Tests for corrections_classifier.dataset — Phase 1 (M5.2 training-and-eval-core). `rows_to_dataset` is pure (plain dicts in, no DB). `fetch_sentiment_correction_rows` /…
- [test_evaluate.py](<test_evaluate.py>) — Tests for corrections_classifier.evaluate — Phase 4b (M5.2 training-and-eval-core). `evaluate` itself is pure (predict/metrics are pure stdlib), but it now TRAINS the challenger itself via…
- [test_labels.py](<test_labels.py>) — Tests for corrections_classifier.labels — urgency-core (M urgency-classifier-head). `URGENCY_LABELS` is a fixed, lexicographically-sorted binary vocab — mirrors `SENTIMENT_LABELS`'s…
- [test_lazy_import.py](<test_lazy_import.py>) — Proves sklearn/numpy are truly optional at import time for corrections_classifier (mirror of tests/sentiment_providers/test_lazy_import.py). Only train_classifier needs them, and it imports…
- [test_metrics_parity.py](<test_metrics_parity.py>) — Parity anchor for corrections_classifier.metrics — Phase 4a (M5.2 training-and-eval-core). metrics.py is a VERBATIM port of `_safe_precision_recall_f1_accuracy` /…
- [test_predict.py](<test_predict.py>) — Tests for corrections_classifier.predict — Phase 3 (M5.2 training-and-eval-core). predict() and score_from_proba() are pure stdlib (re, math) — no sklearn/numpy needed at runtime, even…
- [test_trainer.py](<test_trainer.py>) — Tests for corrections_classifier.trainer — Phase 2 (M5.2 training-and-eval-core). Guards the whole file with pytest.importorskip("sklearn") so the wheels-less CI venv (worker-service…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): test_dataset.py: test_uses_feedback_text_when_present, test_falls_back_to_joined_feedback_item_text_when_feedback_text_blank, test_drops_row_when_no_resolvable_text, test_drops_out_of_vocab_label, test_label_vocabulary_is_exactly_three; test_evaluate.py: test_sentiment_default_labels_produces_identical_evalresult_to_before, _row, _balanced_dataset, _imbalanced_dataset, _gold_label; test_labels.py: test_urgency_labels_value, test_urgency_labels_sorted_positive_is_index_1; test_lazy_import.py: _run, test_package_importable_without_sklearn_or_numpy, test_trainer_module_importable_without_sklearn_or_numpy,….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
