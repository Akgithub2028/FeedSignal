# Directory guide: `services/frontend-web/lib`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for lib within services/frontend-web. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 12 immediate baseline/preparation files, 4 child directories, and 107 files in its subtree before generated guides/index inventories. Common formats: .ts: 107.

## Read first

- [analytics.ts](<analytics.ts>) — Mixpanel Analytics Integration Tracks key user events for conversion optimization. Free tier: 20M events/month
- [api-client.ts](<api-client.ts>) — Exports/declarations: apiClient, publicApiClient
- [asanaIssueWizard.ts](<asanaIssueWizard.ts>) — True when the backend responded 200 with `{warning: "duplicate", ...}` instead of a created task (feedback already linked to an Asana task and `force` was not set).
- [category-utils.ts](<category-utils.ts>) — Exports/declarations: PAIN_POINT_CATEGORIES, FEATURE_REQUEST_CATEGORIES, URGENT_CATEGORIES, SEVERITY_STYLES, PRIORITY_STYLES
- [jiraIssueWizard.ts](<jiraIssueWizard.ts>) — True when the backend responded 200 with `{warning: "duplicate", ...}` instead of a created issue (feedback already linked to a Jira issue and `force` was not set).
- [notification-utils.ts](<notification-utils.ts>) — Exports/declarations: TYPE_ICONS, TYPE_COLORS, timeAgo
- [oauthErrors.ts](<oauthErrors.ts>) — Shared OAuth error code → friendly message mapping. Used by both the integrations index page (`/settings/integrations`, which handles the Linear OAuth return) and per-provider…

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>), [api](<api/directory.md>), [constants](<constants/directory.md>), [utils](<utils/directory.md>).

Direct declarations (navigation cues, not execution results): analytics.ts: initAnalytics, identifyUser, resetAnalytics, trackEvent, analytics; api-client.ts: apiClient, publicApiClient; asanaIssueWizard.ts: isDuplicateAsanaResponse, getAsanaCreateTaskErrorMessage, isStaleAsanaTokenStatus; category-utils.ts: PAIN_POINT_CATEGORIES, FEATURE_REQUEST_CATEGORIES, URGENT_CATEGORIES, SEVERITY_STYLES, PRIORITY_STYLES; jiraIssueWizard.ts: isDuplicateJiraResponse, getJiraCreateIssueErrorMessage, isStaleJiraTokenStatus; notification-utils.ts: TYPE_ICONS, TYPE_COLORS, timeAgo; oauthErrors.ts: OAUTH_ERROR_MESSAGES, getOauthErrorMessage.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).

## Login-helper extraction

[ssoErrorMessage.ts](ssoErrorMessage.ts) contains `resolveSsoErrorMessage`, extracted from app/login/page.tsx for Next.js Page-export validity. It uses the existing OIDC/SAML error maps; behavior is unchanged.
