# Directory guide: `services/backend-api/src/schemas`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Request/response schema contracts. Preserve validation, serialization, optional fields, and backend/frontend agreement; schemas do not substitute for authorization in handlers.

This directory has 13 immediate baseline/preparation files, 0 child directories, and 13 files in its subtree before generated guides/index inventories. Common formats: .py: 13.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [ai_readiness.py](<ai_readiness.py>) — Pydantic schema for the AI training-readiness report (M5.0). Covers: - GET /api/v1/analytics/ai-readiness (org-level, any authenticated role)
- [churn_accuracy.py](<churn_accuracy.py>) — Pydantic schemas for churn accuracy API endpoints (M4.1 Phase 6.2a). Covers: - GET /api/v1/analytics/churn-accuracy (org-level, Business+) - GET /api/v1/system/churn-accuracy (system admin…
- [churn_calibration.py](<churn_calibration.py>) — Pydantic schemas for ChurnCalibrationModel and ChurnBacktestRun (M4.1).
- [churn_cohort.py](<churn_cohort.py>) — Pydantic response schemas for the churn cohort analytics endpoint (M4.1 Phase 4).
- [churn_event.py](<churn_event.py>) — Pydantic schemas for CustomerChurnEvent (M4.1). Separate from src/api/schemas.py to keep churn schemas self-contained.
- [churn_label_gate.py](<churn_label_gate.py>) — Pydantic schemas for GET /api/v1/settings/ai/churn/label-gate (churn-label-gate-study aspect 2, M5.3 disclosure layer). Mirrors the eval_churn_label_gate.py script's committed JSON artifact…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): ai_readiness.py: AIReadinessResponse; churn_accuracy.py: BacktestRunSummary, AccuracyCardResponse, OrgAccuracyRow, SystemAccuracyResponse, ModelVersionSummary; churn_calibration.py: ChurnCalibrationModelResponse, ChurnBacktestRunResponse; churn_cohort.py: CohortBucket, CohortGridCell, CohortAnalyticsResponse; churn_event.py: ChurnEventCreate, ChurnEventResponse, ChurnEventBulkCreate, ChurnEventCsvRow; churn_label_gate.py: GateCurvePoint, FidelitySensitivity, ChurnLabelGateResponse.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
