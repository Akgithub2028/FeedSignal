# Directory guide: `packages/ui/src/components`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for components within packages/ui/src. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .tsx: 2.

## Read first

- [Logo.tsx](<Logo.tsx>) — Exports/declarations: Logo, LogoWithText
- [select.tsx](<select.tsx>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): Logo.tsx: Logo, LogoWithText.

## Inputs, outputs, and change safety

Inputs are composition props, public content/assets, and workspace consumers; outputs are rendered UI or static exports. Keep shared exports and package identifiers aligned. Public copy must not claim credentials, hosted availability, or validated predictive outcomes that do not exist. Unknown domains remain in the unresolved ledger until owner-controlled destinations are confirmed.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).

## FeedSignal identity update

[Logo.tsx](Logo.tsx) retains the inherited abstract glyph and size contract; `LogoWithText` now renders FeedSignal. Package/import names remain `@rereflect/ui`. Artwork replacement is an open owner decision; do not restore the upstream wordmark.
