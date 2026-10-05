# Directory guide: `services`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Runtime service boundaries: backend-api, worker-service, analysis-engine, frontend-web, and landing-web. integration-service is documentation-only scaffolding.

This directory has 1 immediate baseline/preparation files, 6 child directories, and 1682 files in its subtree before generated guides/index inventories. Common formats: .py: 996, .tsx: 465, .ts: 145, .json: 15.

## Read first

- [.dockerignore](<.dockerignore>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [analysis-engine](<analysis-engine/directory.md>), [backend-api](<backend-api/directory.md>), [frontend-web](<frontend-web/directory.md>), [integration-service](<integration-service/directory.md>), [landing-web](<landing-web/directory.md>), [worker-service](<worker-service/directory.md>).

## Inputs, outputs, and change safety

Read callers, environment requirements, and side effects before execution. Keep known owner settings separate from unresolved credentials. Preserve tenant/source provenance and internal import/data contracts; renaming a product is not authorization to alter the original maintainer's infrastructure.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../UNANSWERED_SECRETS.md>).
