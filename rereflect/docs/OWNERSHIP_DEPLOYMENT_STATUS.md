# FeedSignal ownership and deployment status

Updated **7 October 2026**. Owner repository: [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal). Derived from [Rereflect](https://github.com/haqaliz/rereflect); MIT license and NOTICE retained.

**Both frontends are live with FeedSignal branding. Complete baseline launch remains unfinished:** no Celery worker/Beat exists, only owner-recipient email delivery has been verified, and some prepared ownership changes remain local. A connected provider or working webhook does not prove AI processing.

## Identity and live resources

| Component | Owner resource | Verified state |
|---|---|---|
| Product | FeedSignal / `feedsignal` | Support/admin `aayaannkausar@gmail.com`; maintainer [Akgithub2028](https://github.com/Akgithub2028) |
| Landing | https://feed-signal-ochre.vercel.app; Vercel `feed-signal`, `prj_oVq53qCrAcsYhbmwNqmynoIFCrHf` | READY; HTTP 200, FeedSignal title and owner support/GitHub links |
| Dashboard | https://feedsignal-xi.vercel.app; Vercel `feedsignal`, `prj_CLpIHzfOs7tjzWwUUqDEaKVHAO8T` | READY; HTTP 200 login, actual owner Google login and authenticated dashboard verified |
| API | https://feedsignal-api.onrender.com; Render `srv-db210qh7lnhs73d79kq0` | LIVE on owner tawk.to/runtime commit `9a76919`, branch `feedsignal/owner-launch`, auto-deploy off; owner login verified |
| Database | Render `dpg-db20qap7lnhs73d6ki20-a` | Fresh owner PostgreSQL 16; migrations through `fe20261007a1`; expires **2026-11-04 20:48:43 UTC** |
| Queue | Render `red-db20qb6i0phs73cs1s4g` | Free Key Value; `noeviction`, persistence off |
| Worker / Beat | None | Not deployed; scheduled ingestion and analysis are incomplete |
| Render project | `prj-db1vl0p7lnhs73d2h55g` | Owner API/database/queue; no original account data imported |

Vercel deployment artifacts include prepared frontend ownership changes uploaded by CLI. Much of that source is still uncommitted. The live API contains the reviewed OAuth/Asana fixes. Owner runtime/security/email changes and tawk.to ingestion are LIVE as `9a76919`; HubSpot connection and the three tracker statuses persisted after deployment. No original maintainer account was accessed or revoked.

## Integration evidence

| Provider | Owner configuration | Actual verification / remaining work |
|---|---|---|
| Google | Approved existing My Project 41450 (`generated-wharf-500012-q3`); FeedSignal web client, matching Render/Vercel client IDs | Actual owner popup login PASS. Consent audience is **In production**; homepage/privacy/terms links persisted. Search Console homepage ownership verified with the HTML tag. Google OAuth branding re-verification waits for its stated 24-hour propagation window; retry after 2026-10-07 19:15 UTC. Login publication and branding verification are separate checks. Client secret is not exposed in frontend. |
| Slack | https://feedsignal.slack.com, team `T0C7136FUE8`; active app `A0C6U45DBEZ`; six grants including history and incoming webhook | OAuth integration **1** retained through reauthorization; bot added to **public** `#feedsignal-test` (`C0C738CFN3E`); actual test post PASS. Callback/events verification and message subscriptions configured. Live ingestion, AI analysis and reply round trip remain unverified. Unused Demo App remains untouched. |
| Linear | https://linear.app/feedsignal, EU; public app `510e90b8-0763-477d-a359-6b80f1b9f2d0`, team **FEE** | Connection and teams PASS; encrypted renewable tokens deployed; exactly one dynamic webhook confirmed. General-to-FEE mapping and five status mappings configured. FeedSignal created controlled issue **FEE-5**; browser Done transition returned feedback **1** as **resolved** through the signed webhook. Duplicate creation guard verified. |
| Jira | https://aayaannkausar.atlassian.net; project **feedsignal**, key **SCRUM**, id `10000` | Owner `FeedSignal API connection` token encrypted in DB; connect/test PASS. Separate user-supplied token deliberately unused. Signed webhook enabled, `jira:issue_updated`, JQL `project = SCRUM`. FeedSignal created controlled issue **SCRUM-1**; real transitions returned feedback **2** as **in_review**, then **resolved**. First delivery seeds stored state by design. |
| Asana | Owner workspace **FeedSignal** (`1219228511860712`), project **FeedSignal connection tests** (`1219243331704482`) | Encrypted owner PAT; connect/test/project PASS. Reviewed webhook ordering/race/error fix deployed (`3c95946`), 56 focused checks passed. Real handshake enabled; controlled task `1219243143676079` completion returned feedback **3** as **resolved**. No-card trial transitions to Personal; no billing/invitations. |
| HubSpot | Owner portal **247619521**, service key **FeedSignal API connection** (`56032402`) | Key privately saved and encrypted in DB; live connect/test PASS. Required account-info, contacts, companies, deals, contact-property and pipeline reads all returned HTTP 200. Scopes: contacts.read/write, companies.read, deals.read, schemas.contacts.read. ARR field `annualrevenue`; writeback remains off. Worker-based enrichment and sync remain unverified. [Service keys](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/account-service-keys). |
| Discord / Teams | Retained optional connectors | Owner confirmed neither destination exists; deferred, unconfigured. |
| Salesforce / Intercom / Zendesk | User retired these requirements | Runtime/UI/schedule removal remains pending; do not request their credentials. |
| tawk.to | Activated owner account; FeedSignal property `6ac54b01cc4acf34c881125c`, active widget `1k49aq1cq`; source **2** | Signed API and owner/admin UI deployed. Provider webhook registered for completed transcripts/new tickets. Controlled signed fixture produced feedback **4**, organization **1**; wrong signature **401**, accepted **200**, replay duplicate, one receipt/feedback, visitor-only text and anonymous contact verified. UI count PASS. Actual provider-originated delivery is **unverified**: public chat blank/HTTP 403 and embed connection reset. AI analysis awaits worker. |

The three tracker tests use explicitly labeled owner setup data, not customer evidence. Their successful webhooks require no Celery worker. AI processing is not claimed.

## Email

Owner Resend key is stored privately and installed in API settings. Current sender is `FeedSignal <onboarding@resend.dev>`; owner explicitly approved **owner-recipient-only** verification. No sending domain is owned. Actual baseline `send_welcome_email` owner send PASS; Resend reports **delivered**, sender FeedSignal, recipient owner only. This isolated function check does not prove every deployed API email trigger.

Prepared local backend/worker copy and HTML templates use FeedSignal and owner origins. Publish reviewed backend changes before claiming the live email paths have been rebranded. All eight owner templates are created/published and their IDs installed in Render: team invite, welcome, password reset, weekly digest, role change, member removed, daily alert digest, alert notification. The supplied send-only key could not retrieve templates (HTTP 401); a separately named owner full-access key was created and privately installed. Transactional template paths have **no missing-template HTML fallback**. Verify remaining trigger flows; the reset email function alone does not establish an implemented reset endpoint. Worker digests additionally require the missing worker.

General customer sending and inbound email stay deferred until an owned domain, DNS, sender verification and signed receiving webhook exist. Gmail support identity alone does not satisfy those requirements.

## Prepared changes still to publish or complete

1. Review, test and commit remaining branding/security changes. Local bootstrap requires explicit admin credentials, preserves existing users, and removes inherited privileged-email fallback using persisted system-admin authorization. Inbound sources guard against an absent receiving domain. These backend changes are LIVE in `5ad1548`; remaining frontend source publication is pending.
2. Retry Google OAuth branding verification after 2026-10-07 19:15 UTC; Search Console ownership now verified. Asana status round trip and HubSpot connection checks now pass. tawk.to owner setup, signed ingestion and UI now pass controlled checks; retry a real provider delivery when public chat is accessible.
3. Verify remaining live email triggers after the owner runtime deployment. Owner welcome delivery and eight templates now pass; general sender and inbound DNS remain deferred.
4. Retire the three unwanted connectors across direct/generic API routes, UI and scheduled dispatch. tawk.to ingestion is implemented; actual provider-originated delivery remains unverified.
5. Resolve continuous worker/Beat, AI configuration, expiring PostgreSQL, queue durability and backup/restore within an authorized hosting arrangement. The strict $0 Render setup currently does not provide these. No paid resource or full local baseline startup is authorized.
6. Run tenant isolation, migration/restart and full ingestion → analysis → response checks. Vercel Hobby commercial eligibility also remains unresolved; no plan upgrade authorized.

## Verification record

- tawk.to API **26 passed / 1 PostgreSQL-only skip**; isolated PostgreSQL **27 passed**, including simultaneous delivery deduplication. Temporary test IP allowlist restored exactly; isolated schema removed. UI/adjacent Linear **15 passed**, final Next.js build passed. Render deployment `dep-db2sa72jnfac73frngdg` LIVE and migration `fe20261007a1` applied; Vercel dashboard `dpl_3AaXdhKjEa6qxHTVkhPtpvX6yTUe` READY. Live controlled fixture and status screen verified; provider-originated delivery and AI processing are separate pending checks.

- Reviewed deployed owner/provider checks: **61 passed**; provider review independently **31 passed**.
- Linear real PostgreSQL concurrency/lifecycle checks: **16 passed** (one provider renewal for two simultaneous callers).
- Dashboard: **211 files / 1,847 tests passed** before the additional deployment-root regression; configuration checks now **4 passed**. Both actual Vercel builds are READY.
- Asana ordering/error regressions **3 passed** after observed failures; combined Asana client/regression checks **56 passed**, reviewed and deployed; real task status synchronization passed.
- Earlier landing **27 tests** and production build passed; actual provider build now READY.
- Full backend test collection is blocked by missing `onelogin`/native SAML dependencies in the local environment; no full-suite pass claimed. Deprecation warnings remain.

See [launch plan](BASELINE_LAUNCH_PLAN.md), [setup](LAUNCH_SETUP.md), and [unanswered requirements](../UNANSWERED_SECRETS.md). Actual secrets remain only in ignored private files/provider settings. Do not regenerate the established JWT/encryption keys casually.

2026-10-07 checks: **19 owner backend tests**, **6 alert-email tests**, and **80 worker email/outreach/playbook tests** passed. No full worker or AI processing is running.
