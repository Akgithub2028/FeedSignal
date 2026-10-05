# Directory guide: `services/frontend-web/lib/constants`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for constants within services/frontend-web/lib. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 4 immediate baseline/preparation files, 1 child directories, and 5 files in its subtree before generated guides/index inventories. Common formats: .ts: 5.

## Read first

- [churn.ts](<churn.ts>) — Returns a risk band string based on churn probability (0.0–1.0). Bands: <0.30 low, <0.50 medium, <0.70 high, >=0.70 critical.
- [segments.ts](<segments.ts>) — Rule-based customer segment slugs (segment-engine contract). `unsegmented` (or `null` from the API) means the engine hasn't computed a segment for this customer yet — not an error…
- [status-sync-keys.ts](<status-sync-keys.ts>) — Hardcoded canonical foreign-key lists for each inbound status-sync provider's `StatusMappingEditor` (mapping-editor aspect). No discovery endpoint — these mirror the backend's…
- [workflow-status.ts](<workflow-status.ts>) — Rereflect's canonical feedback workflow statuses — the mapping *target* shared by every inbound status-sync integration (Linear, Jira, Asana, Zendesk). Relocated out of…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>).

Direct declarations (navigation cues, not execution results): churn.ts: RiskBand, getRiskBandColor, RISK_BAND_COLOR, CHURN_REASON_LABELS, CHURN_REASON_CODES; segments.ts: SegmentSlug, SEGMENT_SLUGS, SEGMENT_LABELS, SEGMENT_COLOR, normalizeSegment; status-sync-keys.ts: JIRA_STATUS_MAPPING_KEYS, ASANA_STATUS_MAPPING_KEYS, ZENDESK_STATUS_MAPPING_KEYS; workflow-status.ts: REREFLECT_STATUSES.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
