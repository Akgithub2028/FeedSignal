# Directory guide: `scripts`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Repository maintenance and prospecting utilities. Inspect arguments and side effects before running; no outbound contact is authorized by the presence of a script.

This directory has 2 immediate baseline/preparation files, 0 child directories, and 2 files in its subtree before generated guides/index inventories. Common formats: .sh: 1, .py: 1.

## Read first

- [check_docs_honesty.sh](<check_docs_honesty.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [prospect.py](<prospect.py>) — Prospect research helper for Rereflect outreach. Usage: python3 scripts/prospect.py add # Add a new prospect interactively python3 scripts/prospect.py dm # Generate personalized DMs for…

## Files, children, and contracts

[Complete file inventory](<../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): prospect.py: load_prospects, save_prospects, add_prospect, generate_dm_for, generate_dms.

## Inputs, outputs, and change safety

Read callers, environment requirements, and side effects before execution. Keep known owner settings separate from unresolved credentials. Preserve tenant/source provenance and internal import/data contracts; renaming a product is not authorization to alter the original maintainer's infrastructure.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../UNANSWERED_SECRETS.md>).
