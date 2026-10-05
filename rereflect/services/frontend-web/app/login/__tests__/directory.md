# Directory guide: `services/frontend-web/app/login/__tests__`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 1 immediate baseline/preparation files, 0 child directories, and 1 files in its subtree before generated guides/index inventories. Common formats: .tsx: 1.

## Read first

- [page.test.tsx](<page.test.tsx>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
