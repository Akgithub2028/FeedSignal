# Directory guide: `docs/planning/local-embedding-quality`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for local embedding quality. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 5 child directories, and 12 files in its subtree before generated guides/index inventories. Common formats: .md: 12.

## Read first

- [prd.md](<prd.md>) — PRD — Local Embedding Quality (M5.4): Rereflect's AI Copilot matches a user's natural-language question against stored **query templates** (canned SQL) using embeddings, and only falls through to LLM NL→SQL when no…
- [understanding.md](<understanding.md>) — Phase 2 Understanding — local-embedding-quality (M5.4): AI Copilot's template matching — the quality dimension that `local-embeddings-offline-copilot` deliberately deferred (that initiative shipped the plumbing and…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [in-process-provider](<in-process-provider/directory.md>), [offline-packaging](<offline-packaging/directory.md>), [ollama-default-bump](<ollama-default-bump/directory.md>), [retrieval-eval-card](<retrieval-eval-card/directory.md>), [staleness-model-key](<staleness-model-key/directory.md>).

Document sections to inspect: Problem Statement; Goals & Success Metrics; Affected area — entirely `services/backend-api/src` (worker has zero embedding consumers); Finding 1 — there is NO in-process local embedding provider (scope-defining).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
