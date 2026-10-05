# Directory guide: `services/backend-api/scripts`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for scripts within services/backend-api. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 12 immediate baseline/preparation files, 0 child directories, and 12 files in its subtree before generated guides/index inventories. Common formats: .py: 12.

## Read first

- [backfill_churn_factors.py](<backfill_churn_factors.py>) — Backfill churn_risk_factors for existing feedback items that have a churn_risk_score but no factor breakdown. Also recomputes confidence_score on all CustomerHealth records. Usage: python…
- [backfill_customer_email.py](<backfill_customer_email.py>) — Backfill customer_email on existing feedback items from source_metadata. Run: cd services/backend-api && source venv/bin/activate && python scripts/backfill_customer_email.py
- [backfill_health_history.py](<backfill_health_history.py>) — Backfill initial health score history for existing customers who have no history records. This seeds the first data point so the Health Score History chart has something to show. Run: cd…
- [backfill_health_scores.py](<backfill_health_scores.py>) — Backfill customer health scores for all customers with customer_email set. Run AFTER backfill_customer_email.py. Run: cd services/backend-api && source venv/bin/activate && python…
- [backtest_churn.py](<backtest_churn.py>) — Backtest churn prediction accuracy against historical data. Usage: python scripts/backtest_churn.py --days 30 --output results.csv --db-url postgresql://... The script evaluates churn…
- [eval_churn_label_gate.py](<eval_churn_label_gate.py>) — Offline churn label-gate study harness (M5.3, aspect 2 — churn-label-gate-study). Re-derives the per-org churn-label activation gate (CHURN_LABEL_TARGET, currently 500 in…
- [eval_embeddings.py](<eval_embeddings.py>) — Offline retrieval eval harness — runs one or more embedding providers over the held-out template-matching fixtures and computes recall@1, MRR, and false-match rate at the production…

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): backfill_churn_factors.py: get_items_to_backfill, run_backfill, _recompute_confidence_scores, main; backfill_customer_email.py: extract_email, main; backfill_health_history.py: main; backfill_health_scores.py: main; backtest_churn.py: is_churned, compute_metrics, find_optimal_threshold, build_csv_rows, check_data_sufficiency; eval_churn_label_gate.py: FamilySpec, CurvePoint, _seed_for, _segment_of, _tune_intercept; eval_embeddings.py: load_fixtures, build_resolved_embedder, _best_similarity_per_template, _reciprocal_rank, ProviderRetrievalResult.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
