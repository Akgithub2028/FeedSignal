# Directory guide: `docs/planning/saml-sso/frontend-saml-ui`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for saml sso, aspect frontend saml ui. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — frontend-saml-ui: An admin configures SAML at `/settings/sso`, and end users get one "Sign in with SSO" button that starts the SAML flow. Mirrors the OIDC frontend surface; exactly one SSO button ever…
- [impl-report.md](<impl-report.md>) — Implementation Report — frontend-saml-ui: `npm run test` / `npx vitest` are intercepted by the user's `rtk` shell hook and silently return 0 suites (a proxy artifact, not a project issue). All commands below were run…
- [plan_20260717.md](<plan_20260717.md>) — Implementation Plan — frontend-saml-ui: Mirror the shipped **OIDC frontend surface** for SAML. Every file below has an OIDC counterpart already in the tree — we clone the pattern, swap OIDC → SAML nouns/endpoints, and…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope (`services/frontend-web`); Environment note; Pre-flight baseline (before any change); 0. Scope & intent; 1. Dependencies & pre-flight.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
