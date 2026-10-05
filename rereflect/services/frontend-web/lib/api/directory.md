# Directory guide: `services/frontend-web/lib/api`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Typed frontend clients for backend endpoints. Keep response types, error handling, and organization-scoped server contracts synchronized.

This directory has 56 immediate baseline/preparation files, 1 child directories, and 84 files in its subtree before generated guides/index inventories. Common formats: .ts: 84.

## Read first

- [account.ts](<account.ts>) — Download all personal data as a ZIP archive. Triggers a browser download automatically.
- [admin-orgs.ts](<admin-orgs.ts>) — Exports/declarations: AdminOrg, AdminOrgUser, AdminOrgDetail, AdminOrgListResponse, adminOrgsAPI
- [admin-query-templates.ts](<admin-query-templates.ts>) — Exports/declarations: QueryTemplate, QueryTemplateListResponse, QueryTemplateListParams, QueryTemplateUpdate, CopilotStats
- [admin-users.ts](<admin-users.ts>) — Exports/declarations: AdminUser, AdminUserListResponse, AdminUserUpdate, adminUsersAPI
- [ai-corrections.ts](<ai-corrections.ts>) — Submit a correction or rating signal for an AI output. Available to all authenticated users.
- [ai-readiness.ts](<ai-readiness.ts>) — Exports/declarations: AIReadiness, aiReadinessAPI
- [ai-settings.ts](<ai-settings.ts>) — Exports/declarations: AIModels, AISettings, AISettingsUpdate, EmbeddingStatus, SentimentStatus

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>).

Direct declarations (navigation cues, not execution results): account.ts: accountAPI; admin-orgs.ts: AdminOrg, AdminOrgUser, AdminOrgDetail, AdminOrgListResponse, adminOrgsAPI; admin-query-templates.ts: QueryTemplate, QueryTemplateListResponse, QueryTemplateListParams, QueryTemplateUpdate, CopilotStats; admin-users.ts: AdminUser, AdminUserListResponse, AdminUserUpdate, adminUsersAPI; ai-corrections.ts: AICorrection, MostCorrectedItem, CorrectionStats, SubmitCorrectionPayload, PaginatedCorrections; ai-readiness.ts: AIReadiness, aiReadinessAPI; ai-settings.ts: AIModels, AISettings, AISettingsUpdate, EmbeddingStatus, SentimentStatus.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
