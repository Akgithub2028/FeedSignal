# FeedSignal baseline launch implementation plan

> For agentic workers: execute tasks sequentially using superpowers:executing-plans; no parallel delegation is requested. Track completed checks and blocked access explicitly.

**Goal:** Run an owner-controlled FeedSignal baseline with landing and dashboard on Vercel and its backend on an explicitly viable hosting arrangement. Verified existing `feed-signal` project hosts the landing; prepare the dashboard separately as `feedsignal`.

**Architecture:** Keep Next.js on Vercel and FastAPI/PostgreSQL/Redis/Celery separate. Replace Intercom/Zendesk ingestion with tawk.to; retire Salesforce. Do not create paid services or start the full baseline locally under current instructions.

**Tech stack:** Existing pnpm/Next.js, Python/FastAPI, SQLAlchemy/Alembic, PostgreSQL, Redis/Celery, Docker.

**Spec:** [Current launch decisions and provider research](LAUNCH_SETUP.md).

## Global constraints

- Owned repo is [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal); app workspace is its `rereflect/` subdirectory.
- Product FeedSignal; support/admin `aayaannkausar@gmail.com`; GitHub-only social identity.
- Budget $0. Vercel app stays cloud hosted. No billable resources, full local startup or original account access.
- Fresh PostgreSQL; do not import original creator users/tokens. Preserve migration history, MIT license, NOTICE and internal `rereflect_category`/package contracts.
- Secrets remain in ignored files/provider settings; `UNANSWERED_*` must never become fake runtime credentials.

## Review focus

1. Old domain redirects, sender fallbacks and privileged-email defaults can survive superficial text rebranding.
2. A green frontend deploy or `/health` response can conceal an absent worker/database.
3. Retired providers can still run through generic integration routes, notifications, writeback and scheduled tasks.
4. Webhook retries or property mismatches can duplicate feedback or route it into the wrong tenant.
5. Free-host expiration, cold starts and Redis restarts can erase data or delay short-timeout OAuth/webhook requests.

## Task 1: Owner access and deployable topology

Files: `OWNER_CONFIG.md`, `UNANSWERED_SECRETS.md`, `services/*-web/vercel.json`, `render.api-preview.yaml`, this plan and `LAUNCH_SETUP.md`.

- [x] Verify remote repo layout; prepare monorepo build configuration and update owner decisions.
- [x] Complete CLI authorization and verify identity/workspace without printing tokens (Vercel, Render and GitHub verified 2026-10-06).
- [x] Inspect existing `feed-signal` deployment, root and environment **names**; link the existing landing folder. Production domain `feed-signal-ochre.vercel.app`; no production variables. Owner API/PostgreSQL/Redis are now provisioned; full topology remains partial.
- [ ] Resolve the absence of a continuous worker and durable database within the owner's budget. Do not claim this is solved by the prepared API-only preview.
- [x] Register assigned app/API origins and owner free setup resources in the ledger; database expiry and sleeping-worker limits remain explicit. These preview resources do not complete the topology.

Deliverable: authenticated owner access and a topology capable of all required background jobs, not merely a frontend URL. Validate manifests with the installed provider CLI before applying.

## Task 2: Runtime ownership and security

Files: backend `src/seed.py`, `src/api/routes/team.py`, email services/templates and `feedback_sources.py`; frontend `middleware.ts`, `next.config.ts`, active app copy; landing metadata, pages, navigation/footer and shared links.

- [x] Test fresh bootstrap without configured admin credentials creates no inherited owner; with explicit credentials it creates only the intended owner (9 tests, real isolated SQLite DB).
- [x] Test an existing-user database is never promoted or overwritten by changing admin environment variables. Failed bootstrap rolls back organization creation too.
- [x] Remove embedded password and original privileged-email defaults locally; require explicit bootstrap credentials and persisted system-admin authorization. Verify the published revision separately.
- [x] Rebrand active product text and make legal/marketing/app origins explicit. Remove upstream website destinations from active signup, redirect and email flows; preserve attribution separately.
- [x] Make Sentry source-map organization/project operator-supplied locally and disable unconfigured upload/runtime telemetry; focused source tests passed.
- [x] API and worker share owner encryption key/database/Redis; public origins configured and frontend rebuilt.

Verification: focused bootstrap/authorization tests; missing/incorrect origin tests; production frontend/landing builds; authenticated fresh-install smoke check. Historical docs and internal identifiers are not blind-renamed.

## Task 3: Retire Salesforce, Intercom and Zendesk

Files: backend API router registration and generic integration validation; worker `src/celery_app.py`, sync/writeback dispatchers; frontend settings/integration cards, notification and response settings; active landing claims/environment examples.

- [x] Test retired provider connection endpoints and generic create/update paths cannot enable a connection.
- [x] Remove active provider choices, OAuth callbacks and router registration; remove their Beat schedule and task loading/dispatch.
- [x] Remove active response/notification choices and marketing promises that depend on these connectors.
- [x] Preserve applied migrations and historical record provenance; a fresh DB contains no inherited provider records. Do not revoke another creator's account credentials.
- [x] Run router, schedule integrity and settings tests, then frontend build. Audit indirect calls before deleting implementation modules.

Deliverable: no active retired-provider authorization, polling or writeback path. Focused checks pass; `7b41bb7` is LIVE on Render and READY on dashboard. Live retired routes absent/create rejected; authenticated retired settings page returns 404.

## Task 4: tawk.to free ingestion

Files to create: backend `src/api/routes/tawk_integration.py`, `src/api/routes/tawk_webhook.py`, ingestion service and focused tests; frontend settings page/API client; database event-receipt migration if existing receipts cannot provide required uniqueness.

- [x] Test raw-body signature verification: absent/wrong signature rejects; valid request succeeds; no cross-property tenant routing.
- [x] Implement per-organization property registration and encrypted secret storage. Expose callback `/api/v1/webhooks/tawk/events` only after the implementation exists; do not point a provider at an invented working endpoint.
- [x] Normalize `chat:transcript_created` and `ticket:create`, retaining provider IDs/source evidence. Distinguish visitor from agent/system content and preserve anonymous contacts.
- [x] Commit a durable receipt before Celery dispatch; deduplicate provider retries with a database uniqueness constraint on source/event ID and recover undispatched receipts.
- [x] Test duplicate/reordered events, unknown properties, malformed/large payloads and unavailable broker. Acknowledge only after durable acceptance; retry delivery safely.
- [x] Register the owner property, webhook secret/events and optional widget after authenticated dashboard access. Do not advertise writeback or ticket updates.

**Ingestion implementation and controlled test complete (7 October):** code `9a76919` deployed on Render/Vercel; owner property/webhook registered. A labeled signed fixture persisted visitor feedback **4** in owner organization **1**, source **2**, exactly once. Bad signature 401; valid 200; replay duplicate; live UI shows one import. PostgreSQL concurrency and tenant/signature/error tests pass.

- [x] Observe actual provider delivery: controlled ticket created feedback 7; Inbox transcript correlated with feedback 6. Public visitor chat accessibility remains blocked separately.
- [x] Run actual processing with free sleeping worker/Beat: Slack/tawk analyzed, owner Gemini categorization verified, HubSpot synced 221 contacts; persisted after redeploy. Broker outage recovery and continuous scheduling remain separate unchecked requirements.

Provider delivery and worker analysis checks above now pass; full development checklist remains in PENDING_LAUNCH.md. Durable ingestion commits normalized feedback and its receipt atomically before enqueue; existing periodic unanalyzed-feedback processing provides recovery once worker/Beat run.

## Task 5: Remaining connectors and complete launch

- [x] Register owner Google/Slack/Linear apps using actual HTTPS origins; connect Jira/Asana/HubSpot and selected notification destinations using owner settings.
- [x] Verify Slack message scopes and Linear webhook privilege; adapt Jira scoped-token URLs and Microsoft Teams Workflows where necessary.
- [ ] Configure Resend only after supported sender/domain verification; inbound email waits for DNS-controlled receiving setup.
- [ ] Verify controlled ingestion and issue creation/retry behavior in owner workspaces. Do not send unsolicited messages to customer workspaces.
- [ ] Run tenant-isolation tests, migration upgrade, backup/restore, worker/Beat and end-to-end analysis checks; restart services and verify persisted data/retry recovery.
- [ ] Capture observed deployment URLs and results in the ledger. Deploy reviewed artifacts only after a viable budget/topology and authenticated access exist.

**Current scope/status (7 October 2026):** owner keeps $0 and current Vercel/Render topology for complete development, not shipping. Worker preview (`f19806b`) and Jira fix (`a88ad40`) deployed; real tawk ticket, Slack ingestion, Gemini worker categorization, HubSpot 221-contact sync and scheduled owner report delivery verified. Wake-on-dispatch approved; health recompute, full email triggers, live isolation/retry and Google branding remain pending. Database expiry/durability, domain and always-on scheduling stay deferred real-shipping requirements. See [current pending evidence](PENDING_LAUNCH.md).
