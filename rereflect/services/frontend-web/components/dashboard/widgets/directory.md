# Directory guide: `services/frontend-web/components/dashboard/widgets`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for widgets within services/frontend-web/components/dashboard. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 16 immediate baseline/preparation files, 0 child directories, and 16 files in its subtree before generated guides/index inventories. Common formats: .tsx: 16.

## Read first

- [ActivityFeedWidget.tsx](<ActivityFeedWidget.tsx>) — Exports/declarations: ActivityFeedWidget
- [AiInsightsWidget.tsx](<AiInsightsWidget.tsx>) — Exports/declarations: AiInsightsWidget
- [AnomalyAlertsWidget.tsx](<AnomalyAlertsWidget.tsx>) — Exports/declarations: AnomalyAlertsWidget
- [AtRiskCustomersWidget.tsx](<AtRiskCustomersWidget.tsx>) — Exports/declarations: AtRiskCustomersWidget
- [ChurnRiskWidget.tsx](<ChurnRiskWidget.tsx>) — Exports/declarations: ChurnRiskWidget
- [FeatureRequestsWidget.tsx](<FeatureRequestsWidget.tsx>) — Exports/declarations: FeatureRequestsWidget
- [ModelAccuracyCard.tsx](<ModelAccuracyCard.tsx>) — Exports/declarations: ModelAccuracyCard

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): ActivityFeedWidget.tsx: ActivityFeedWidget; AiInsightsWidget.tsx: AiInsightsWidget; AnomalyAlertsWidget.tsx: AnomalyAlertsWidget; AtRiskCustomersWidget.tsx: AtRiskCustomersWidget; ChurnRiskWidget.tsx: ChurnRiskWidget; FeatureRequestsWidget.tsx: FeatureRequestsWidget; ModelAccuracyCard.tsx: ModelAccuracyCard.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
