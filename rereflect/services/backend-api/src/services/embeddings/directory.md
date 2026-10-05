# Directory guide: `services/backend-api/src/services/embeddings`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Embedding provider or vector-search support. Preserve model/provider/version consistency and organization-scoped storage; optional providers need owner credentials before use.

This directory has 5 immediate baseline/preparation files, 1 child directories, and 10 files in its subtree before generated guides/index inventories. Common formats: .py: 10.

## Read first

- [__init__.py](<__init__.py>) — Embeddings package — provider-agnostic embedding abstraction for backend-api. Public surface: EmbeddingProvider — ABC (for type hints in consumers) EmbeddingProviderFactory — name →…
- [base.py](<base.py>) — EmbeddingProvider — abstract base class for all embedding providers. Every provider must: - Implement embed(text: str) -> list[float] Normalise the provider SDK's response to a flat Python…
- [defaults.py](<defaults.py>) — Provider → default embedding model lookup. Pure helper, no route/DB imports. Mirrors src/api/routes/ai_settings.py::_default_embedding_model exactly (see that function's docstring) — this…
- [factory.py](<factory.py>) — EmbeddingProviderFactory — creates embedding provider instances by name. Mirrors the shape of services/worker-service/src/llm/factory.py (LLMProviderFactory) for consistency. Cross-service…
- [resolver.py](<resolver.py>) — Org-scoped embedding provider resolver. Single entry point for all consumers (template-matching-local, copilot-llm-local): embedder = resolve_embedding_provider(org_id, db) if embedder is…

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [providers](<providers/directory.md>).

Direct declarations (navigation cues, not execution results): base.py: EmbeddingProvider; defaults.py: default_model_for_provider; factory.py: EmbeddingProviderFactory; resolver.py: ResolvedEmbedder, resolve_embedding_provider.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
