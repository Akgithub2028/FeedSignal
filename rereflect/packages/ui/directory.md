# Directory guide: `packages/ui`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

The shared @rereflect/ui workspace. Owns its exported components, styles, utilities, and configuration; it is not a shared Python package.

This directory has 3 immediate baseline/preparation files, 1 child directories, and 8 files in its subtree before generated guides/index inventories. Common formats: .ts: 3, .json: 2, .tsx: 2, .css: 1.

## Read first

- [package.json](<package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [tailwind.config.ts](<tailwind.config.ts>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [tsconfig.json](<tsconfig.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## Files, children, and contracts

[Complete file inventory](<../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [src](<src/directory.md>).

## Inputs, outputs, and change safety

Inputs are composition props, public content/assets, and workspace consumers; outputs are rendered UI or static exports. Keep shared exports and package identifiers aligned. Public copy must not claim credentials, hosted availability, or validated predictive outcomes that do not exist. Unknown domains remain in the unresolved ledger until owner-controlled destinations are confirmed.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../UNANSWERED_SECRETS.md>).
