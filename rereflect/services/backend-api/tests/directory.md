# Directory guide: `services/backend-api/tests`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 304 immediate baseline/preparation files, 2 child directories, and 320 files in its subtree before generated guides/index inventories. Common formats: .py: 314, .csv: 3, .jsonl: 2, .json: 1.

## Read first

- [test_action_proposer.py](<test_action_proposer.py>) — Phase D TDD — deterministic action proposer (copilot-suggested-actions). Unit tests for the pure, synchronous proposer module (`src/services/copilot/action_proposer.py`): -…
- [test_action_registry.py](<test_action_registry.py>) — TDD tests — action registry (`src/services/copilot/action_registry.py`). The registry is the ONLY dispatch path for copilot-suggested actions (PRD M1): it maps a stable `action` id to an…
- [test_active_days_14d_migration.py](<test_active_days_14d_migration.py>) — TDD migration test for Phase B of the usage-trend-churn-signal aspect (rollup-rewindow-fix): `customer_usage.active_days_14d` (Integer, nullable, no server_default, no backfill). Strategy…
- [test_ai_correction_service.py](<test_ai_correction_service.py>) — Characterization + behavior tests for `create_ai_correction` (src/services/ai_correction_service.py). Locks the current (pre-bulk) default behavior — commits internally — before adding an…
- [test_ai_correction_service_urgency.py](<test_ai_correction_service_urgency.py>) — TDD tests for the shared urgency corrected-value constant/helper (capture-seam Phase 1) — `services/ai_correction_service.py`. Goal: a single backend source of truth for…
- [test_ai_corrections.py](<test_ai_corrections.py>) — TDD tests for AI Human-in-the-Loop corrections (Track B). Covers: 1. test_submit_thumbs_up 2. test_submit_thumbs_down_with_text 3. test_submit_category_correction 4.…
- [test_ai_readiness.py](<test_ai_readiness.py>) — Tests for the AI training-readiness report (M5.0) — strict TDD. Endpoint under test: GET /api/v1/analytics/ai-readiness — per-org, no-ML, read-only aggregation over FeedbackItem /…

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [embeddings](<embeddings/directory.md>), [fixtures](<fixtures/directory.md>).

Direct declarations (navigation cues, not execution results): test_action_proposer.py: TestExtractCustomerEmails, TestProposeActions, TestActionEmailCap; test_action_registry.py: _User, TestRegistryShape, TestGetEntry, TestRequireRole, TestRegistryDriftGuard; test_active_days_14d_migration.py: _make_engine, _dispose, _apply_upgrade, _apply_downgrade, pre_migration_engine; test_ai_correction_service.py: db, org, TestCreateAiCorrectionDefaultCommits, TestCreateAiCorrectionCommitFalse; test_ai_correction_service_urgency.py: TestUrgencyCorrectedValuesVocab, TestUrgencyLabelHelper, TestUrgencyVocabMatchesAnalysisEngine; test_ai_corrections.py: _member_token, TestSubmitCorrection,….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
