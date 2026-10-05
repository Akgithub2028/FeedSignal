# Directory guide: `services/landing-web/app`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Static marketing routes, metadata, legal pages, blog, and integration descriptions. Source copy is not proof that a feature exists or that FeedSignal is deployed.

This directory has 5 immediate baseline/preparation files, 4 child directories, and 20 files in its subtree before generated guides/index inventories. Common formats: .tsx: 17, .css: 2, .svg: 1.

## Read first

- [layout.tsx](<layout.tsx>) — Exports/declarations: metadata, RootLayout
- [page.tsx](<page.tsx>) — Exports/declarations: metadata, Home
- [globals.css](<globals.css>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [icon.svg](<icon.svg>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [landing.css](<landing.css>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [blog](<blog/directory.md>), [integrations](<integrations/directory.md>), [privacy](<privacy/directory.md>), [terms](<terms/directory.md>).

Direct declarations (navigation cues, not execution results): layout.tsx: metadata, RootLayout; page.tsx: metadata, Home.

## Inputs, outputs, and change safety

Inputs are composition props, public content/assets, and workspace consumers; outputs are rendered UI or static exports. Keep shared exports and package identifiers aligned. Public copy must not claim credentials, hosted availability, or validated predictive outcomes that do not exist. Unknown domains remain in the unresolved ledger until owner-controlled destinations are confirmed.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
