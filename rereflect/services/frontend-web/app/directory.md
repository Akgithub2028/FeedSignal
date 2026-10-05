# Directory guide: `services/frontend-web/app`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

App Router layouts and pages. providers.tsx configures shared client providers; layout.tsx owns metadata/fonts; protected/public paths must retain their actual auth boundaries.

This directory has 6 immediate baseline/preparation files, 6 child directories, and 110 files in its subtree before generated guides/index inventories. Common formats: .tsx: 108, .css: 1, .svg: 1.

## Read first

- [layout.tsx](<layout.tsx>) — Exports/declarations: metadata, RootLayout
- [page.tsx](<page.tsx>) — Exports/declarations: Home
- [global-error.tsx](<global-error.tsx>) — Exports/declarations: GlobalError
- [globals.css](<globals.css>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [icon.svg](<icon.svg>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [providers.tsx](<providers.tsx>) — Exports/declarations: Providers

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [(dashboard)](<(dashboard)/directory.md>), [invite](<invite/directory.md>), [login](<login/directory.md>), [outreach](<outreach/directory.md>), [shared](<shared/directory.md>), [signup](<signup/directory.md>).

Direct declarations (navigation cues, not execution results): layout.tsx: metadata, RootLayout; page.tsx: Home; global-error.tsx: GlobalError; providers.tsx: Providers.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
