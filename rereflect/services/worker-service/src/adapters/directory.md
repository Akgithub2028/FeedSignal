# Directory guide: `services/worker-service/src/adapters`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Normalization of provider payloads into feedback/source events. Preserve provenance, source identity, deduplication, and organization attribution.

This directory has 8 immediate baseline/preparation files, 0 child directories, and 8 files in its subtree before generated guides/index inventories. Common formats: .py: 8.

## Read first

- [__init__.py](<__init__.py>) — Source adapters for handling provider-specific event processing.
- [base.py](<base.py>) — Base adapter class for source-specific event handling.
- [email.py](<email.py>) — Email adapter for handling inbound email webhook events.
- [intercom.py](<intercom.py>) — Intercom adapter for handling Intercom webhook events.
- [intercom_parts.py](<intercom_parts.py>) — Reply/rating extraction from Intercom *conversation* objects (pull path). The webhook adapter (adapters/intercom.py) parses event-shaped payloads; this module parses the conversation object…
- [slack.py](<slack.py>) — Slack adapter for handling Slack Events API events.
- [webhook.py](<webhook.py>) — Generic webhook adapter for handling custom webhook events.

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): __init__.py: get_adapter; base.py: BaseSourceAdapter; email.py: EmailAdapter; intercom.py: strip_html, _contact_email, IntercomAdapter; intercom_parts.py: _parts_of, extract_reply_parts, extract_rating, format_reply_merge, new_reply_parts; slack.py: SlackAdapter; webhook.py: _get_nested_value, WebhookAdapter.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
