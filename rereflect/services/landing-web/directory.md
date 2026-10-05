# Directory guide: `services/landing-web`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Static Next.js marketing application. next.config.ts uses output: export; source retains inherited domains/branding pending M1 ownership replacement.

This directory has 13 immediate baseline/preparation files, 5 child directories, and 77 files in its subtree before generated guides/index inventories. Common formats: .tsx: 46, .ts: 14, .css: 2, .svg: 2.

## Read first

- [Dockerfile](<Dockerfile>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [package.json](<package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [.env.example](<.env.example>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [docker-entrypoint.sh](<docker-entrypoint.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [next.config.ts](<next.config.ts>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [nginx.conf](<nginx.conf>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [nginx.conf.template](<nginx.conf.template>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>), [app](<app/directory.md>), [components](<components/directory.md>), [lib](<lib/directory.md>), [public](<public/directory.md>).

## Inputs, outputs, and change safety

Inputs are composition props, public content/assets, and workspace consumers; outputs are rendered UI or static exports. Keep shared exports and package identifiers aligned. Public copy must not claim credentials, hosted availability, or validated predictive outcomes that do not exist. Unknown domains remain in the unresolved ledger until owner-controlled destinations are confirmed.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../UNANSWERED_SECRETS.md>).
