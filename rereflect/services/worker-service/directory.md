# Directory guide: `services/worker-service`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Celery/Redis background runtime, provider adapters/clients, mirrored models/services, ingestion, analysis, scheduled work, and tests. Entry point src/celery_app.py; start.sh launches worker with Beat.

This directory has 7 immediate baseline/preparation files, 2 child directories, and 238 files in its subtree before generated guides/index inventories. Common formats: .py: 227, .json: 4, .example: 1, (no extension): 1.

## Read first

- [Dockerfile](<Dockerfile>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [README.md](<README.md>) — Worker Service
- [.env.example](<.env.example>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [pytest.ini](<pytest.ini>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [railway.toml](<railway.toml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [requirements.txt](<requirements.txt>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [start.sh](<start.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.

## Files, children, and contracts

[Complete file inventory](<../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [src](<src/directory.md>), [tests](<tests/directory.md>).

Document sections to inspect: Purpose; Tech Stack.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../UNANSWERED_SECRETS.md>).

Owner launch: Celery no longer loads or schedules Salesforce, Intercom or Zendesk tasks. Generic retired-provider events and churn backfill cannot dispatch ingestion; historical models/task files remain for migration provenance. `src/preview_service.py` supports a sleeping Render free web-service preview with one worker and one Beat; the HTTP check reports process liveness only. See the launch checklist for actual deployment/job evidence.
