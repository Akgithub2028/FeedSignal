# Directory guide: `services/frontend-web/contexts`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for contexts within services/frontend-web. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 7 immediate baseline/preparation files, 1 child directories, and 9 files in its subtree before generated guides/index inventories. Common formats: .tsx: 9.

## Read first

- [AuthContext.tsx](<AuthContext.tsx>) — Exports/declarations: AuthProvider, useAuth
- [FeatureRequestsPageContext.tsx](<FeatureRequestsPageContext.tsx>) — Exports/declarations: FeatureRequestsPageProvider, useFeatureRequestsPage
- [FeedbackPageContext.tsx](<FeedbackPageContext.tsx>) — Exports/declarations: FeedbackPageProvider, useFeedbackPage
- [PainPointsPageContext.tsx](<PainPointsPageContext.tsx>) — Exports/declarations: PainPointsPageProvider, usePainPointsPage
- [RealtimeContext.tsx](<RealtimeContext.tsx>) — Exports/declarations: EventHandler, RealtimeContextType, RealtimeProvider, useRealtime
- [ThemeContext.tsx](<ThemeContext.tsx>) — Exports/declarations: ThemeProvider, useTheme
- [UrgentFeedbackPageContext.tsx](<UrgentFeedbackPageContext.tsx>) — Exports/declarations: UrgentFeedbackPageProvider, useUrgentFeedbackPage

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>).

Direct declarations (navigation cues, not execution results): AuthContext.tsx: AuthProvider, useAuth; FeatureRequestsPageContext.tsx: FeatureRequestsPageProvider, useFeatureRequestsPage; FeedbackPageContext.tsx: FeedbackPageProvider, useFeedbackPage; PainPointsPageContext.tsx: PainPointsPageProvider, usePainPointsPage; RealtimeContext.tsx: EventHandler, RealtimeContextType, RealtimeProvider, useRealtime; ThemeContext.tsx: ThemeProvider, useTheme; UrgentFeedbackPageContext.tsx: UrgentFeedbackPageProvider, useUrgentFeedbackPage.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
