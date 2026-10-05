# Directory guide: `docs/planning/saml-sso/docs-and-dev-idp`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for saml sso, aspect docs and dev idp. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — docs-and-dev-idp: A self-hosting operator can follow docs to register Rereflect as a SAML SP with their IdP, configure it, - Register the SP with your IdP: ACS URL `{BACKEND_URL}/api/v1/auth/saml/callback`…
- [impl-report.md](<impl-report.md>) — Implementation Report — `docs-and-dev-idp` aspect: Documented the SAML 2.0 SSO slice that shipped across the five functional aspects (`deps-and-docker`, `config-model-and-crud`, `provider-and-replay-store`,
- [plan_20260717.md](<plan_20260717.md>) — Implementation Plan — `saml-sso` / aspect `docs-and-dev-idp`: This aspect runs LAST precisely so the docs match reality. **Do this verification block first** and record the answers; every later phase consumes them. Run…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; Summary; Files changed; 0. Pre-flight: verify shipped behavior before writing a word; 0.1 Confirm the functional aspects actually landed on this branch.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
