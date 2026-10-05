# Directory guide: `docs/planning/saml-sso/deps-and-docker`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Feature planning records for saml sso, aspect deps and docker. Requirements, dated plans, task notes, and closure records describe intent/history; confirm current implementation and tests before using them as a new work order.

This directory has 3 immediate baseline/preparation files, 0 child directories, and 3 files in its subtree before generated guides/index inventories. Common formats: .md: 3.

## Read first

- [spec.md](<spec.md>) — Aspect Spec — deps-and-docker: `python3-saml` depends on `xmlsec`, which needs native `libxmlsec1` / `libxml2` (+ `pkg-config`) system libraries. If the backend image / CI environment lacks them, **the entire test suite…
- [impl-report.md](<impl-report.md>) — Implementation Report — `deps-and-docker` (SAML SSO, aspect 1 of 6): The RED→GREEN cycle for `test_saml_deps.py` could **not** be fully closed in this macOS venv — well-understood, host-specific reason documented in…
- [plan_20260717.md](<plan_20260717.md>) — Tech Plan — `deps-and-docker` (SAML SSO, slice 1, aspect 1 of N): Land the SAML native dependency + Docker build changes and **prove they import** — nothing else. When this aspect is green, `from onelogin.saml2.auth…

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: Problem slice & outcome; In scope; Status: DONE_WITH_CONCERNS; What was done (phases 1–4, per plan); 0. Goal of this aspect (one paragraph); 1. Confirmed facts (do not re-derive).

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
