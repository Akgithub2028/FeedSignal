# Directory guide: `services/analysis-engine/src/analyzer/churn_classifier`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Churn classifier training/evaluation artifacts and feature definitions. Check label windows, account/time splits, readiness thresholds, and training/serving parity before claiming predictive accuracy.

This directory has 8 immediate baseline/preparation files, 0 child directories, and 8 files in its subtree before generated guides/index inventories. Common formats: .py: 8.

## Read first

- [__init__.py](<__init__.py>) — Per-org churn classifier core — pure-compute head for the M5.3 ML challenger. CPU-only, offline, per-org logistic-regression churn classifier built on the leakage-free A/B spine of…
- [dataset.py](<dataset.py>) — Churn dataset builder (M5.3 churn-classifier-core). Split into a pure transform (`rows_to_dataset`) and a lazy-SQL fetch seam (`fetch_churn_rows`), mirroring…
- [evaluate.py](<evaluate.py>) — Shadow-A/B evaluate for the churn head (M5.3 churn-classifier-core). Runs the incumbent-vs-challenger shootout on a held-out split (stratified; k-fold when tiny) and returns the…
- [features.py](<features.py>) — Frozen churn feature vector builder (M5.3 churn-classifier-core). The FROZEN field set (fixed by the gate study, aspect 2, and locked here — see tests/churn_classifier/test_features.py):…
- [labels.py](<labels.py>) — Locked knobs for the per-org churn classifier core (M5.3, aspect 3). Every constant here is parity-pinned to its source-of-truth definition in the pre-existing churn calibration path — see…
- [metrics.py](<metrics.py>) — Binary churn metrics — pure stdlib (M5.3 churn-classifier-core). `compute_binary_metrics` mirrors the corrections_classifier/metrics.py style (threshold-derived counts, every division…
- [predict.py](<predict.py>) — Pure-stdlib churn predict from JSON artifact (M5.3 churn-classifier-core). Reconstructs the binary logistic decision from a trainer.py JSON artifact WITHOUT sklearn/numpy — stdlib only…

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): dataset.py: rows_to_dataset, fetch_churn_rows; evaluate.py: EvalResult, _to_dataset, _simple_holdout_scores, _kfold_scores, evaluate_churn; features.py: _value, build_feature_vector; metrics.py: _count_confusion, _precision_recall_f1, _auc, compute_binary_metrics, binary_macro_f1; predict.py: _sigmoid, predict.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run focused analysis-engine tests for changed outputs/model gates. Verify optional dependencies and dataset provenance; model claims require held-out evidence.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
