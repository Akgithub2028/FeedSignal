# Directory guide: `services/frontend-web/components`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Reusable application components and feature UI. Read exports and their page consumers; much of the UI lives here rather than packages/ui.

This directory has 16 immediate baseline/preparation files, 15 child directories, and 178 files in its subtree before generated guides/index inventories. Common formats: .tsx: 173, .ts: 5.

## Read first

- [AppSidebar.tsx](<AppSidebar.tsx>) — Exports/declarations: AppSidebar
- [Button.tsx](<Button.tsx>) — Exports/declarations: Button
- [Card.tsx](<Card.tsx>) — Exports/declarations: Card, CardHeader, CardContent, CardTitle
- [Checkbox.tsx](<Checkbox.tsx>) — Exports/declarations: CheckboxProps
- [GoogleSignInButton.tsx](<GoogleSignInButton.tsx>) — Exports/declarations: GoogleSignInButton
- [Header.tsx](<Header.tsx>) — Exports/declarations: Header
- [InviteMemberModal.tsx](<InviteMemberModal.tsx>) — Exports/declarations: InviteMemberModal

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [__tests__](<__tests__/directory.md>), [analytics](<analytics/directory.md>), [copilot](<copilot/directory.md>), [customers](<customers/directory.md>), [dashboard](<dashboard/directory.md>), [feedback](<feedback/directory.md>), [feedbacks](<feedbacks/directory.md>), [icons](<icons/directory.md>), [integrations](<integrations/directory.md>), [playbooks](<playbooks/directory.md>), [providers](<providers/directory.md>), [settings](<settings/directory.md>); 3 more in the index.

Direct declarations (navigation cues, not execution results): AppSidebar.tsx: AppSidebar; Button.tsx: Button; Card.tsx: Card, CardHeader, CardContent, CardTitle; Checkbox.tsx: CheckboxProps; GoogleSignInButton.tsx: GoogleSignInButton; Header.tsx: Header; InviteMemberModal.tsx: InviteMemberModal.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Use the service's current package.json scripts, pnpm workspace installation, relevant Vitest checks, and a production build for UI/config changes. Do not infer tool availability or build success from package metadata.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
