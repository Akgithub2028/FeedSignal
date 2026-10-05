# Directory guide: `services/worker-service/src/clients`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Outbound provider HTTP clients. Credentials belong to the relevant authorized organization; retries and logging must not expose tokens or trigger duplicate writes.

This directory has 7 immediate baseline/preparation files, 0 child directories, and 7 files in its subtree before generated guides/index inventories. Common formats: .py: 7.

## Read first

- [__init__.py](<__init__.py>) — Inspect file contents and its consumers; no executable behavior is asserted from the filename.
- [asana.py](<asana.py>) — Asana REST API client for the inbound status-sync worker task (asana-status-sync/asana-client-get-task). The worker cannot import backend-api, so this is a standalone mirror of…
- [hubspot.py](<hubspot.py>) — HubSpot CRM HTTP client for the hubspot-sync worker task. Pulls Contacts, Companies, and Deals from HubSpot CRM v3 API. Handles pagination (cursor-based), 429 rate limits (Retry-After…
- [intercom.py](<intercom.py>) — Intercom REST client for the conversation-pull and write-back paths. Mirrors src/clients/zendesk.py in error taxonomy and lifecycle. Lives in worker-service because worker-service cannot…
- [jira.py](<jira.py>) — Jira Cloud REST API client for the inbound status-sync worker task (jira-status-sync/inbound-status-sync, Phase 4). The worker cannot import backend-api, so this is a standalone mirror of…
- [salesforce.py](<salesforce.py>) — Salesforce REST/SOQL HTTP client for the salesforce-sync worker task. Mints a short-lived access_token from a stored OAuth refresh_token before each run (web-server OAuth 2.0 — mirrors…
- [zendesk.py](<zendesk.py>) — Zendesk REST/incremental-export HTTP client for the zendesk-sync worker task (ingestion-pull aspect). Thin httpx wrapper, HTTP Basic auth using the token-access convention (`{email}/token`,…

## Files, children, and contracts

[Complete file inventory](<../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): asana.py: AsanaError, AsanaAuthError, AsanaTransientError, AsanaNotFoundError, AsanaClient; hubspot.py: HubSpotTransientError, HubSpotScopeError, HubSpotNotFoundError, _format_number, HubSpotClient; intercom.py: IntercomError, IntercomAuthError, IntercomTransientError, IntercomNotFoundError, IntercomClient; jira.py: JiraError, JiraAuthError, JiraTransientError, JiraNotFoundError, JiraClient; salesforce.py: SalesforceTransientError, SalesforceAuthError, SalesforceQueryError, SalesforceScopeError, SalesforceNotFoundError; zendesk.py: ZendeskError, ZendeskAuthError, ZendeskTransientError, ZendeskNotFoundError, ZendeskClient.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused worker pytest checks and real Redis/PostgreSQL where dispatch, retries, and committed-state visibility matter. Verify Beat scheduling topology before deployment.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../UNANSWERED_SECRETS.md>).
