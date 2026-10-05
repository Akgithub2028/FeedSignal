# Directory guide: `services/backend-api/src/utils`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for utils within services/backend-api/src. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 4 immediate baseline/preparation files, 0 child directories, and 4 files in its subtree before generated guides/index inventories. Common formats: .py: 4.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [byok.py](<byok.py>) — BYOK (Bring Your Own Key) resolution helper. Provides a single shared helper `resolve_org_byok_key` that retrieves a decrypted API key for a provider from the org's OrgApiKey table. This…
- [encryption.py](<encryption.py>) — Fernet symmetric encryption utilities for BYOK API key storage. The encryption key is sourced from the LLM_ENCRYPTION_KEY environment variable. Generate once: python -c "from…
- [ssrf.py](<ssrf.py>) — Shared SSRF gate for hosts derived from untrusted operator/IdP-supplied input (e.g. an OIDC issuer or jwks_uri) that this service is about to fetch. Same semantics as the per-integration…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): byok.py: resolve_org_byok_key; encryption.py: _get_fernet, encrypt_api_key, decrypt_api_key, get_key_hint; ssrf.py: SsrfError, assert_host_not_ssrf.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
