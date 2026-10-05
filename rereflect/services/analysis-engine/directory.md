# Directory guide: `services/analysis-engine`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Analysis library and optional API/example entry points. Supports local sentiment/classification/clustering and churn-classifier utilities. Read source and requirements for actual optional dependencies.

This directory has 4 immediate baseline/preparation files, 3 child directories, and 73 files in its subtree before generated guides/index inventories. Common formats: .py: 67, .json: 2, .example: 1, .md: 1.

## Read first

- [README.md](<README.md>) — Analysis Engine: Core analysis engine that processes customer feedback using: This service is **production-ready** and powers the entire SaaS platform.
- [.env.example](<.env.example>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [quickstart.sh](<quickstart.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [requirements.txt](<requirements.txt>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.

## Files, children, and contracts

[Complete file inventory](<../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [examples](<examples/directory.md>), [src](<src/directory.md>), [tests](<tests/directory.md>).

Document sections to inspect: Purpose; Tech Stack.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run focused analysis-engine tests for changed outputs/model gates. Verify optional dependencies and dataset provenance; model claims require held-out evidence.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../UNANSWERED_SECRETS.md>).
