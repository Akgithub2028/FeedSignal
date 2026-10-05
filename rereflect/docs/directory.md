# Directory guide: `docs`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Operational documentation, historical planning, assets, ownership audit, canonical implementation plan, and M0 handoff. Current source and maintained operational docs take precedence over old PRD status/pricing.

This directory has 8 immediate baseline/preparation files, 4 child directories, and 600 files in its subtree before generated guides/index inventories. Common formats: .md: 576, .png: 17, .json: 3, .csv: 3.

## Read first

- [IMPLEMENTATION_PLAN.md](<IMPLEMENTATION_PLAN.md>) — FeedSignal: implementation plan toward $1,000 MRR: FeedSignal uses the known support/admin email and GitHub identity above. Domains are undecided (`UNANSWERED_MARKETING_ORIGIN`, `UNANSWERED_APP_ORIGIN`,…
- [OWNERSHIP_AND_INTEGRATION_AUDIT.md](<OWNERSHIP_AND_INTEGRATION_AUDIT.md>) — Deployment, ownership, and integration migration audit: Audit date: 2026-10-05. Local checkout inspected: `93359c4a2bf20310f98e42d570de50a1586812d8`. Original repository: haqaliz/rereflect.
- [ARCHITECTURE.md](<ARCHITECTURE.md>) — Architecture: A Next.js frontend talks to a FastAPI backend over REST. Long-running analysis is offloaded to a Celery worker (Redis broker), which uses the analysis engine — VADER /
- [SELF_HOSTING.md](<SELF_HOSTING.md>) — Self-Hosting Rereflect: Rereflect is open source (MIT) and designed to run entirely on your own infrastructure. **All features are unlocked** on a self-hosted instance — there are
- [API.md](<API.md>) — API Reference: Rereflect exposes a REST API under `/api/v1`. When the backend is running, the full interactive OpenAPI/Swagger docs are at **http://localhost:8000/docs** — this page is a
- [DEVELOPMENT.md](<DEVELOPMENT.md>) — Development: How to run Rereflect from source for local development. For containerized deployment instead, see SELF_HOSTING.md.
- [DIRECTORY_FILE_INDEX.md](<DIRECTORY_FILE_INDEX.md>) — FeedSignal complete directory file inventory: Baseline `93359c4a2bf20310f98e42d570de50a1586812d8` plus M0 preparation files; updated 2026-10-06. Generated `directory.md` files are indexed separately. This preserves…

## Files, children, and contracts

[Complete file inventory](<DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [archive](<archive/directory.md>), [assets](<assets/directory.md>), [m0](<m0/directory.md>), [planning](<planning/directory.md>).

Document sections to inspect: Owner configuration and unresolved launch settings; 1\. Recommended product direction; 1. What is actually connected?; 2. Confirmed replacements and repairs; Services; Tech stack; Prerequisites; Quick start (Docker Compose); Authentication; Multi-tenancy; The toolchain & package management; `.`;….

## Inputs, outputs, and change safety

Read callers, environment requirements, and side effects before execution. Keep known owner settings separate from unresolved credentials. Preserve tenant/source provenance and internal import/data contracts; renaming a product is not authorization to alter the original maintainer's infrastructure.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../UNANSWERED_SECRETS.md>).
