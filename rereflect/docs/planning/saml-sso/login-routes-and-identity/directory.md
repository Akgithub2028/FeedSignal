# Directory guide: `docs/planning/saml-sso/login-routes-and-identity`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for saml sso, aspect login routes and identity. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — login-routes-and-identity: The end-to-end SP-initiated login: start → IdP → ACS → validated assertion → resolved user → JWT → persist the returned `request_id` (pending) via the replay store; 302 to the…
- [impl-report.md](<impl-report.md>) — Impl Report — `login-routes-and-identity` (SAML 2.0 SSO, aspect 4): Two routes wired into `src/api/routes/auth.py` (riding the existing `auth.router`, prefix `/api/v1/auth`), plus the reused OIDC-shaped…
- [plan_20260717.md](<plan_20260717.md>) — Tech Plan — `login-routes-and-identity` (SAML 2.0 SSO): This aspect wires the **SP-initiated SAML login flow** into the reused OIDC identity-resolution block: `sso_error` constants + `SAML_ACS_PATH`, the…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope (in `src/api/routes/auth.py`, mirroring the OIDC routes); Status: DONE — green; Commits (phase-sized, TDD RED→GREEN); 1. Scope & boundary; 2. Interfaces consumed (contracts to hold this aspect to).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
