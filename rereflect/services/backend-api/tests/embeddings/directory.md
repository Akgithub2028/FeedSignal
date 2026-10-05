# Directory guide: `services/backend-api/tests/embeddings`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 9 immediate baseline/preparation files, 0 child directories, and 9 files in its subtree before generated guides/index inventories. Common formats: .py: 9.

## Read first

- [test_base.py](<test_base.py>) — Phase 1 RED: Tests for the EmbeddingProvider abstract base interface. Asserts: - EmbeddingProvider is abstract (cannot be instantiated directly) - embed(text: str) -> list[float] is…
- [test_factory.py](<test_factory.py>) — Phase 4 RED: Tests for EmbeddingProviderFactory. - create("openai", api_key="k", model=None) → OpenAIEmbeddingProvider - create("openai_compatible", base_url=..., model="nomic-embed-text")…
- [test_google_provider.py](<test_google_provider.py>) — Phase 3 RED: Tests for GoogleEmbeddingProvider. AC3: google provider normalizes its response to list[float]. - Mock google.generativeai client; assert embed() returns list[float] -…
- [test_local_provider.py](<test_local_provider.py>) — Aspect 2 / Task 1 RED: Tests for LocalEmbeddingProvider. In-process, CPU, air-gappable embedding provider using sentence-transformers. Mirrors the M5.1 TransformerSentimentProvider…
- [test_openai_compatible_provider.py](<test_openai_compatible_provider.py>) — Phase 2 RED: Tests for OpenAICompatibleEmbeddingProvider. AC2: openai_compatible provider calls configured base_url with no api_key, returns the model's native dims (mock a 768-dim…
- [test_openai_provider.py](<test_openai_provider.py>) — Phase 2 RED: Tests for OpenAIEmbeddingProvider. AC1: openai provider returns a 1536-dim vector (mocked client) for given text. - Mock openai.OpenAI client - Assert embed("hi") returns a…
- [test_resolver.py](<test_resolver.py>) — Phase 5 RED: Tests for resolve_embedding_provider. Degrade matrix (the contract the whole feature leans on): 1. Org with default_provider="openai" + valid BYOK key → ResolvedEmbedder with…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): test_base.py: TestEmbeddingProviderIsAbstract; test_factory.py: TestEmbeddingProviderFactory; test_google_provider.py: TestGoogleEmbeddingProvider; test_local_provider.py: stub_sentence_transformers, _reload_local_provider_module, TestLocalEmbeddingProviderEmbed, TestLocalEmbeddingProviderLazyLoad, TestLocalEmbeddingProviderOfflineEnv; test_openai_compatible_provider.py: TestOpenAICompatibleEmbeddingProvider; test_openai_provider.py: TestOpenAIEmbeddingProvider; test_resolver.py: _make_config, _make_db_with_config, _make_db_without_config, TestResolveEmbeddingProvider.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
