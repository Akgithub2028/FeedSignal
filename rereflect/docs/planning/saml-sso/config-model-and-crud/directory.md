# Directory guide: `docs/planning/saml-sso/config-model-and-crud`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for saml sso, aspect config model and crud. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — config-model-and-crud: An admin/owner can store and manage the deployment's single SAML IdP connection, and the deployment enforces **one SSO protocol total** (OIDC xor SAML). Mirrors `oidc_config` exactly…
- [impl-report.md](<impl-report.md>) — Implementation Report — config-model-and-crud (SAML SSO, aspect 2/6): Implemented the SAML config model + CRUD + cross-provider single-enabled guard exactly per `plan_20260717.md`, mirroring the shipped OIDC aspect.…
- [plan_20260717.md](<plan_20260717.md>) — Tech Plan — SAML SSO · config-model-and-crud: This plan mirrors the shipped OIDC aspect (`oidc_config.py` model + `routes/oidc_config.py` + `c9d0e1f2a3b4` / `n8o9p0q1r2s3` migrations + `test_oidc_config.py`) exactly in…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; Summary; Files changed; 0. Key decisions locked for this aspect; 1. Files touched (build order is §4).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
