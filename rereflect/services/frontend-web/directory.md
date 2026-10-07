# Directory guide: `services/frontend-web`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Next.js application frontend. Owns dashboard/auth/settings pages, components, API clients, context/hooks, and frontend tests. Public environment variables are baked into builds.

This directory has 20 immediate baseline/preparation files, 7 child directories, and 565 files in its subtree before generated guides/index inventories. Common formats: .tsx: 419, .ts: 131, .json: 3, .svg: 2.

## Read first

- [Dockerfile](<Dockerfile>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [package.json](<package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [.env.example](<.env.example>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [components.json](<components.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [eslint.config.mjs](<eslint.config.mjs>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [instrumentation-client.ts](<instrumentation-client.ts>) — Sentry client-side configuration. Runs in the browser. Initializes only when NEXT_PUBLIC_SENTRY_DSN is set, so a self-hosted install sends nothing anywhere unless the operator…
- [instrumentation.ts](<instrumentation.ts>) — Exports/declarations: register, onRequestError

## Files, children, and contracts

[Complete file inventory](<../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>), [app](<app/directory.md>), [components](<components/directory.md>), [contexts](<contexts/directory.md>), [hooks](<hooks/directory.md>), [lib](<lib/directory.md>), [public](<public/directory.md>).

Direct declarations (navigation cues, not execution results): instrumentation-client.ts: onRouterTransitionStart; instrumentation.ts: register, onRequestError.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../UNANSWERED_SECRETS.md>).

## Owner launch update — 6 October

[Cloud setup](../../docs/LAUNCH_SETUP.md) records confirmed repository/project roots, CLI authentication and unresolved $0 worker/database constraints. Service-level Vercel settings are prepared; runtime ownership and provider replacement remain pending. No full local startup.

## Current owner preparation

Local product copy/metadata/contact links use FeedSignal and Akgithub2028. Vercel feedsignal project and public API/app/marketing variables exist, but no deployment. Build uses Webpack. Page helpers now live in components/customers/ChurnSuggestionEvidenceCell.tsx, components/settings/ApiKeyScopes.tsx and lib/ssoErrorMessage.ts. See [current ownership status](../../docs/OWNERSHIP_DEPLOYMENT_STATUS.md) before reporting live readiness.
