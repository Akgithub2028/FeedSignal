# Directory guide: `services/analysis-engine/src/analyzer/corrections_classifier`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for corrections_classifier within services/analysis-engine/src/analyzer. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 7 immediate baseline/preparation files, 0 child directories, and 7 files in its subtree before generated guides/index inventories. Common formats: .py: 7.

## Read first

- [__init__.py](<__init__.py>) — Per-org sentiment and category corrections classifier — pure-compute core (M5.2). CPU-only, offline, per-org TF-IDF + logistic-regression classifier, mirroring the churn split…
- [dataset.py](<dataset.py>) — Corrections dataset builder — task-generic (sentiment + category), Phase 1 (M5.2 training-and-eval-core). Split into a pure transform (`rows_to_dataset`) and a lazy-SQL fetch seam…
- [evaluate.py](<evaluate.py>) — Shadow-A/B evaluate — Phase 4b (M5.2 training-and-eval-core). Runs the incumbent-vs-challenger shootout on a held-out split (stratified; k-fold when tiny) and returns the…
- [labels.py](<labels.py>) — Fixed sentiment label vocabulary + locked knobs for the corrections classifier (M5.2). `SENTIMENT_LABELS` is sorted so it matches sklearn's `classes_` ordering when the trainer fits on…
- [metrics.py](<metrics.py>) — Multiclass confusion-matrix metrics — Phase 4a (M5.2 training-and-eval-core). VERBATIM port of `_safe_precision_recall_f1_accuracy` / `confusion_to_binary_counts` /…
- [predict.py](<predict.py>) — Pure-Python predict-from-JSON — Phase 3 (M5.2 training-and-eval-core). Reconstructs the TF-IDF + logistic-regression decision from a JSON artifact (see trainer.py's schema) WITHOUT…
- [trainer.py](<trainer.py>) — TF-IDF + logistic-regression trainer — Phase 2 (M5.2 training-and-eval-core). Serializes ONLY to JSON-native types (never pickle) — vocabulary/idf weights + logreg coef_/intercept_/classes_…

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): dataset.py: _normalize_label, _resolve_text, rows_to_dataset, fetch_correction_rows, fetch_sentiment_correction_rows; evaluate.py: EvalResult, _empty_confusion, _confusion_for, _classes_present, _stratified_indices_by_class; metrics.py: _safe_precision_recall_f1_accuracy, confusion_to_binary_counts, compute_multiclass_metrics; predict.py: _tokenize, _tfidf_vector, _decision, _softmax, _sigmoid; trainer.py: train_classifier, _serialize.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run focused analysis-engine tests for changed outputs/model gates. Verify optional dependencies and dataset provenance; model claims require held-out evidence.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
