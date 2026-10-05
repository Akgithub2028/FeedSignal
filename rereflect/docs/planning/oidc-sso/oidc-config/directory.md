# Directory guide: `docs/planning/oidc-sso/oidc-config`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for oidc sso, aspect oidc config. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .md: 2.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — `oidc-config`: Give an operator a place to store their IdP connection — issuer, client id, client secret, the domain allowlist, and an on/off switch — and give the rest of the system two read paths: an…
- [plan_20260717.md](<plan_20260717.md>) — Implementation Plan — `oidc-config`: (`src/api/routes/zendesk_integration.py`) — same Fernet pattern, same `token_hint`/`secret_hint` - `services/backend-api/src/models/oidc_config.py` **(new)** — the model per spec §1.…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & user outcome; In-scope (PRD M2/M3/M4/M12); Global constraints (hand to every implementer + reviewer, verbatim); Setup.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
