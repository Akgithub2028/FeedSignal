# Directory guide: `.`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

FeedSignal preparation workspace, derived from Rereflect. Owns pnpm workspace configuration, deployment recipes, environment templates, license/provenance, operational documentation, and the owner handoff.

This directory has 31 immediate baseline/preparation files, 6 child directories, and 2342 files in its subtree before generated guides/index inventories. Common formats: .py: 997, .md: 609, .tsx: 467, .ts: 148.

## Read first

- [OWNER_CONFIG.md](<OWNER_CONFIG.md>) — FeedSignal owner configuration: Product name is a working choice, not proof of domain or legal availability. Owner legal name: `UNANSWERED_OWNER_LEGAL_NAME`. Owned repository URL: `UNANSWERED_GITHUB_REPOSITORY_URL`; do…
- [UNANSWERED_SECRETS.md](<UNANSWERED_SECRETS.md>) — FeedSignal — unanswered configuration and credentials: The working name is selected for this repository. Domain, trademark, and account-name availability are not established. Do not invent an owned domain or a created…
- [README.md](<README.md>) — FeedSignal: Owner/support/admin: `aayaannkausar@gmail.com` · Akgithub2028 on GitHub. Independent FeedSignal fork; owner API/DB/Redis now exist, frontends/worker/connectors remain partial. All existing…
- [docker-compose.prod.yml](<docker-compose.prod.yml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [.env.prod.example](<.env.prod.example>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [package.json](<package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [CLAUDE.md](<CLAUDE.md>) — Rereflect - Customer Feedback Analyzer: AI-powered customer feedback analysis platform for SaaS businesses. The automations engine exists **twice**, on purpose, and the two must stay in agreement:

## Files, children, and contracts

[Complete file inventory](<docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [.claude](<.claude/directory.md>), [.github](<.github/directory.md>), [docs](<docs/directory.md>), [packages](<packages/directory.md>), [scripts](<scripts/directory.md>), [services](<services/directory.md>).

Document sections to inspect: Applying these decisions; Confirmed decisions; Placeholder convention and resolution procedure; Current status; Baseline capabilities; Highlights; Project Overview; Key Features.

## Inputs, outputs, and change safety

Read callers, environment requirements, and side effects before execution. Keep known owner settings separate from unresolved credentials. Preserve tenant/source provenance and internal import/data contracts; renaming a product is not authorization to alter the original maintainer's infrastructure.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<UNANSWERED_SECRETS.md>).

## Owner launch update — 6 October

[Cloud setup](docs/LAUNCH_SETUP.md) records confirmed repository/project roots, CLI authentication and unresolved $0 worker/database constraints. Service-level Vercel settings are prepared; runtime ownership and provider replacement remain pending. No full local startup.

## Owner status update — 6 October

Read [README.md](README.md), [current ownership/deployment status](docs/OWNERSHIP_DEPLOYMENT_STATUS.md), [owner configuration](OWNER_CONFIG.md) and [unanswered settings](UNANSWERED_SECRETS.md) first. Owner API/DB/Redis and dashboard project now exist; local branding/security changes are not published. Worker and OAuth installation remain unfinished. Preserve inherited identifiers and license attribution.
