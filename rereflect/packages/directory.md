# Directory guide: `packages`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Shared pnpm workspace packages consumed by app and landing frontends. Do not rename identifiers simply to change user-facing branding.

This directory has 0 immediate baseline/preparation files, 1 child directories, and 8 files in its subtree before generated guides/index inventories. Common formats: .ts: 3, .json: 2, .tsx: 2, .css: 1.

## Read first

No direct implementation entry files. Follow the child guides below for the actual documents or runtime modules.

## Files, children, and contracts

[Complete file inventory](<../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [ui](<ui/directory.md>).

## Inputs, outputs, and change safety

Read callers, environment requirements, and side effects before execution. Keep known owner settings separate from unresolved credentials. Preserve tenant/source provenance and internal import/data contracts; renaming a product is not authorization to alter the original maintainer's infrastructure.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../UNANSWERED_SECRETS.md>).
