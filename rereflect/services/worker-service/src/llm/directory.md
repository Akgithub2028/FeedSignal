# Directory guide: `services/worker-service/src/llm`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

LLM provider interfaces or implementation modules. Keep local and BYOK modes intact; credentials and model configuration are organization/operator settings, not bundled vendor keys.

This directory has 8 immediate baseline/preparation files, 1 child directories, and 13 files in its subtree before generated guides/index inventories. Common formats: .py: 13.

## Read first

- [__init__.py](<__init__.py>) — LLM abstraction layer for the worker service. Provides a provider-agnostic interface for calling OpenAI, Anthropic, and Google models, with automatic retry and fallback chain support.…
- [base.py](<base.py>) — Abstract base class for LLM providers.
- [factory.py](<factory.py>) — LLM Provider Factory — creates provider instances by name.
- [fallback.py](<fallback.py>) — FallbackChain — orchestrates retry logic for LLM calls. Strategy: 1. Try primary provider (org's BYOK key) 2. On transient failure (429, 5xx, timeout): retry once with 2s backoff 3. If…
- [org_resolver.py](<org_resolver.py>) — Resolves per-org LLM configuration: provider, model, API key. Strictly BYOK (bring-your-own-key): reads OrgApiKey from the database. If no valid BYOK key exists for an org, AI is disabled…
- [pricing.py](<pricing.py>) — LLM pricing table and cost estimation utilities. Prices are in USD per 1M tokens (input/output). Cost is returned in cents.
- [prompts.py](<prompts.py>) — All LLM prompts used by the worker service. Moved from openai_client.py — kept identical to preserve existing behavior.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [providers](<providers/directory.md>).

Direct declarations (navigation cues, not execution results): base.py: LLMProvider; factory.py: LLMProviderFactory; fallback.py: _is_auth_error, _get_fallback_reason, FallbackChain; org_resolver.py: _decrypt_api_key, log_usage, build_fallback_chain, call_llm_for_org; pricing.py: estimate_cost_cents.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
