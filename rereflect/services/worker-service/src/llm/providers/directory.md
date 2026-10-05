# Directory guide: `services/worker-service/src/llm/providers`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

LLM provider interfaces or implementation modules. Keep local and BYOK modes intact; credentials and model configuration are organization/operator settings, not bundled vendor keys.

This directory has 5 immediate baseline/preparation files, 0 child directories, and 5 files in its subtree before generated guides/index inventories. Common formats: .py: 5.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [anthropic.py](<anthropic.py>) — Anthropic LLM provider implementation. Uses messages.create API. System messages are extracted into the separate 'system' parameter. JSON mode is handled via prompt instruction + stripping…
- [google.py](<google.py>) — Google Generative AI (Gemini) LLM provider implementation. Uses google-generativeai SDK. JSON mode is handled via response_mime_type="application/json". System messages are passed as…
- [openai.py](<openai.py>) — OpenAI LLM provider implementation. Uses chat.completions.create with json_object response format for JSON mode. System messages are kept in the messages array (OpenAI's native format).
- [openai_compatible.py](<openai_compatible.py>) — OpenAI-compatible LLM provider. Wraps the OpenAI client against a custom base_url, enabling local / offline models (Ollama, LM Studio, vLLM, etc.) as drop-in replacements. The api_key is…

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): anthropic.py: _strip_json_fences, AnthropicProvider; google.py: GoogleProvider; openai.py: OpenAIProvider; openai_compatible.py: OpenAICompatibleProvider.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
