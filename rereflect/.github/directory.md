# Directory guide: `.github`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

GitHub contributor and continuous-integration configuration; no live cloud account ownership is established by these files.

This directory has 2 immediate baseline/preparation files, 2 child directories, and 5 files in its subtree before generated guides/index inventories. Common formats: .md: 3, .yml: 2.

## Read first

- [FUNDING.yml](<FUNDING.yml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [pull_request_template.md](<pull_request_template.md>) — Summary

## Files, children, and contracts

[Complete file inventory](<../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [ISSUE_TEMPLATE](<ISSUE_TEMPLATE/directory.md>), [workflows](<workflows/directory.md>).

Document sections to inspect: Related issues; Type of change.

## Inputs, outputs, and change safety

Read callers, environment requirements, and side effects before execution. Keep known owner settings separate from unresolved credentials. Preserve tenant/source provenance and internal import/data contracts; renaming a product is not authorization to alter the original maintainer's infrastructure.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../UNANSWERED_SECRETS.md>).
