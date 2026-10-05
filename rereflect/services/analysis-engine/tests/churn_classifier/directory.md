# Directory guide: `services/analysis-engine/tests/churn_classifier`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 10 immediate baseline/preparation files, 0 child directories, and 10 files in its subtree before generated guides/index inventories. Common formats: .py: 10.

## Read first

- [test_dataset.py](<test_dataset.py>) — Tests for churn_classifier.dataset (M5.3 churn-classifier-core). `rows_to_dataset` is pure (plain dicts in, no DB). `fetch_churn_rows` needs sqlalchemy — guarded with `pytest.importorskip`…
- [test_evaluate.py](<test_evaluate.py>) — Tests for churn_classifier.evaluate (M5.3 churn-classifier-core). `evaluate_churn` runs the incumbent-vs-challenger A/B on a leakage-free stratified holdout (k-fold when tiny), scoring BOTH…
- [test_features.py](<test_features.py>) — Tests for churn_classifier.features (M5.3 churn-classifier-core). Pins the FROZEN feature vector — the field set fixed by the gate study (aspect 2) and locked here: 6 health components +…
- [test_labels.py](<test_labels.py>) — Tests for churn_classifier.labels (M5.3 churn-classifier-core). Every constant here is parity-pinned to its source-of-truth definition elsewhere in the repo (the churn calibration path that…
- [test_lazy_import.py](<test_lazy_import.py>) — Proves sklearn/numpy are truly optional at import time for churn_classifier (mirror of tests/corrections_classifier/test_lazy_import.py). Only train_churn_classifier needs them, and it…
- [test_metrics.py](<test_metrics.py>) — Tests for churn_classifier.metrics (M5.3 churn-classifier-core). Hand-computed golden tests for `compute_binary_metrics` (positive-class precision/recall/F1 at the 0.5 threshold, rank-based…
- [test_predict.py](<test_predict.py>) — Tests for churn_classifier.predict (M5.3 churn-classifier-core). predict() is pure stdlib (math.sigmoid of the linear score) — no sklearn/numpy at runtime, even though the sklearn-parity…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): test_dataset.py: test_rows_to_dataset_builds_feature_vectors_and_positive_default_labels, test_rows_to_dataset_respects_explicit_label, test_rows_to_dataset_preserves_row_order, test_rows_to_dataset_all_missing_fields_uses_defaults_no_raise, test_rows_to_dataset_empty_input; test_evaluate.py: _row_vec, _dataset, _incumbent_identity, _incumbent_wrong, _never_call; test_features.py: test_feature_names_are_frozen_and_fixed_order, _full_row, test_full_row_produces_expected_vector, test_vector_length_matches_feature_names, test_all_missing_row_returns_documented_defaults_without_raising; test_labels.py: _parse_int_const, test_min_labels_value,….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
