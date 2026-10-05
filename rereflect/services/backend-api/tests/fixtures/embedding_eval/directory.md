# Directory guide: `services/backend-api/tests/fixtures/embedding_eval`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .jsonl: 2, .py: 1.

## Read first

- [test_fixtures_valid.py](<test_fixtures_valid.py>) — Validation tests for the held-out retrieval-eval fixtures (local-embedding-quality, aspect retrieval-eval-card, Task 1). These fixtures back an eval of embedding retrieval quality: given a…
- [queries.jsonl](<queries.jsonl>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [queries_tiny.jsonl](<queries_tiny.jsonl>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): test_fixtures_valid.py: _load_jsonl, all_descriptions, all_question_patterns, queries_rows, queries_tiny_rows.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
