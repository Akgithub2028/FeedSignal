# Directory guide: `docs/m0/datasets/banking77`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Banking77: 13,083 labeled banking utterances across 77 intents, unchanged upstream train/test files under CC BY 4.0. Attribution, blob/SHA-256 hashes and normalized duplicate checks accompany the files. Seven normalized texts overlap across train and test; these are development data, not SaaS buyers.

This directory has 7 immediate baseline/preparation files, 0 child directories, and 7 files in its subtree before generated guides/index inventories. Common formats: .json: 3, .csv: 2, .md: 1, (no extension): 1.

## Read first

- [ATTRIBUTION.md](<ATTRIBUTION.md>) — Banking77 attribution: Publisher: PolyAI. Authors: Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson and Ivan Vulić. Paper: Efficient Intent Detection with Dual Sentence Encoders, 2020.
- [source_manifest.json](<source_manifest.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [quality_report.json](<quality_report.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [LICENSE](<LICENSE>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [train.csv](<train.csv>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [test.csv](<test.csv>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [categories.json](<categories.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## Files, children, and contracts

[Complete file inventory](<../../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
