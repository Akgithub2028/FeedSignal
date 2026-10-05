# Directory guide: `services/frontend-web/app/(dashboard)/settings/automations/__tests__`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 15 immediate baseline/preparation files, 0 child directories, and 15 files in its subtree before generated guides/index inventories. Common formats: .tsx: 15.

## Read first

- [CategoryMatchConfigKeys.test.tsx](<CategoryMatchConfigKeys.test.tsx>) — The category-match editor must write the keys the backend actually reads. DEV-TRACKING P4: `[id]/page.tsx`'s CategoryMatchTriggerFields read and wrote `config.tags` /…
- [SendCustomerEmailConfigKeys.test.tsx](<SendCustomerEmailConfigKeys.test.tsx>) — The send_customer_email editor must write EXACTLY the two keys the backend accepts. `SendCustomerEmailConfig` (backend `automations.py`) is `extra="forbid"`, so a config carrying…
- [id-action-support.test.tsx](<id-action-support.test.tsx>) — R6 (automation-action-support) on the rule detail/edit page: the action select is filtered by the trigger's supported actions, a rule saved before the matrix existed shows an…
- [id-batch-sentiment-trigger.test.tsx](<id-batch-sentiment-trigger.test.tsx>) — Tests for the `batch_sentiment_threshold` trigger additions to the automation rule detail/edit page: the trigger type option, config field pre-population from trigger_config,…
- [id-churn-playbook.test.tsx](<id-churn-playbook.test.tsx>) — Tests for the churn-triggered-playbooks additions to the automation rule detail/edit page: the `churn_probability_threshold` trigger config, the `run_playbook` action config…
- [id-email-deliveries.test.tsx](<id-email-deliveries.test.tsx>) — Tests for the Email Deliveries surface on the automation rule detail page (automation-send-customer-email, frontend-editor Phase 4). A `skipped` row is the honest record of a send…
- [id-send-customer-email.test.tsx](<id-send-customer-email.test.tsx>) — Tests for the `send_customer_email` action editor on the automation rule detail/edit page (automation-send-customer-email, frontend-editor Phase 2). The contract this pins:…

## Files, children, and contracts

[Complete file inventory](<../../../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

## Inputs, outputs, and change safety

Inputs are page props, URL state, authenticated API responses, and public build settings; outputs are UI state/actions or typed requests. Server authorization must enforce tenant boundaries regardless of client filters. Never place private provider keys in browser bundles or NEXT_PUBLIC variables. Check parent layouts and API types before changing flows.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../../../UNANSWERED_SECRETS.md>).
