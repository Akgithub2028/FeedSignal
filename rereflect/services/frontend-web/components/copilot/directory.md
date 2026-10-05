# Directory guide: `services/frontend-web/components/copilot`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Implementation support for copilot within services/frontend-web/components. Read the entry files and direct declarations below, then follow parent consumers and tests; runtime behavior is not inferred solely from a directory name.

This directory has 13 immediate baseline/preparation files, 0 child directories, and 13 files in its subtree before generated guides/index inventories. Common formats: .tsx: 13.

## Read first

- [ChatArea.tsx](<ChatArea.tsx>) — If set, auto-send this query as the first message after loading
- [CommandBar.tsx](<CommandBar.tsx>) — Exports/declarations: CommandBar
- [CommandBarContext.tsx](<CommandBarContext.tsx>) — Exports/declarations: useCommandBar
- [CommandBarProvider.tsx](<CommandBarProvider.tsx>) — Exports/declarations: CommandBarProvider
- [ContextScopeSelector.tsx](<ContextScopeSelector.tsx>) — Where the dropdown opens relative to the trigger. Default: 'below'
- [ConversationList.tsx](<ConversationList.tsx>) — Change this value to trigger a re-fetch of the conversation list
- [CopilotActionButton.tsx](<CopilotActionButton.tsx>) — Persisted conversation id the proposal lives in — the execute route resolves the proposal by conversation_id + proposal_id. Never the WS turn message id. Absent (e.g.…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): ChatArea.tsx: ChatMessage, ChatArea; CommandBar.tsx: CommandBar; CommandBarContext.tsx: useCommandBar; CommandBarProvider.tsx: CommandBarProvider; ContextScopeSelector.tsx: ContextScope, ScopeOption, SCOPE_OPTIONS, ContextScopeSelector; ConversationList.tsx: ConversationList; CopilotActionButton.tsx: CopilotActionButton.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
