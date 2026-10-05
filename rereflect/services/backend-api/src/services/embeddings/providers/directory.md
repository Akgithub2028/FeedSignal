# Directory guide: `services/backend-api/src/services/embeddings/providers`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Embedding provider or vector-search support. Preserve model/provider/version consistency and organization-scoped storage; optional providers need owner credentials before use.

This directory has 5 immediate baseline/preparation files, 0 child directories, and 5 files in its subtree before generated guides/index inventories. Common formats: .py: 5.

## Read first

- [__init__.py](<__init__.py>) — Embedding provider implementations.
- [google.py](<google.py>) — Google (Gemini) embedding provider. Uses google-generativeai SDK (google-generativeai>=0.8.0, already in requirements.txt for both backend-api and worker-service). Note: the…
- [local.py](<local.py>) — LocalEmbeddingProvider — in-process, CPU, air-gappable embedding provider. Uses sentence-transformers to run embedding models locally (no network call per embed(), no API key). Mirrors the…
- [openai.py](<openai.py>) — OpenAI embedding provider. Mirrors the embedding call already in template_matcher._call_embedding_api (L120-134), but wraps it in the EmbeddingProvider interface so it is injectable and…
- [openai_compatible.py](<openai_compatible.py>) — OpenAI-compatible embedding provider (keyless / local). Targets any server that exposes the OpenAI Embeddings API format: - Ollama (http://localhost:11434/v1) - LM Studio, vLLM, llama.cpp,…

## Files, children, and contracts

[Complete file inventory](<../../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): google.py: GoogleEmbeddingProvider; local.py: _is_offline, _get_model, LocalEmbeddingProvider; openai.py: OpenAIEmbeddingProvider; openai_compatible.py: OpenAICompatibleEmbeddingProvider.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../../UNANSWERED_SECRETS.md>).
