# FeedSignal ownership and deployment status

Updated **7 October 2026**. Owner repository: [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal). Derived from [Rereflect](https://github.com/haqaliz/rereflect); MIT license and NOTICE retained.

**Owner-controlled free development deployment is live:** both frontends, API, sleeping worker/Beat, real tawk/Slack ingestion, Gemini categorization and HubSpot sync are verified. Remaining development gaps and real-shipping prerequisites are tracked in [PENDING_LAUNCH.md](PENDING_LAUNCH.md).

## Identity and live resources

| Component | Owner resource | Verified state |
|---|---|---|
| Product | FeedSignal / `feedsignal` | Support/admin `aayaannkausar@gmail.com`; maintainer [Akgithub2028](https://github.com/Akgithub2028) |
| Landing | https://feed-signal-ochre.vercel.app; Vercel `feed-signal`, `prj_oVq53qCrAcsYhbmwNqmynoIFCrHf` | READY; HTTP 200, FeedSignal title and owner support/GitHub links |
| Dashboard | https://feedsignal-xi.vercel.app; Vercel `feedsignal`, `prj_CLpIHzfOs7tjzWwUUqDEaKVHAO8T` | READY; HTTP 200 login, actual owner Google login and authenticated dashboard verified |
| API | https://feedsignal-api.onrender.com; Render `srv-db210qh7lnhs73d79kq0` | LIVE on reviewed Jira compatibility commit `a88ad40`, branch `feedsignal/owner-launch`, auto-deploy off; owner login verified |
| Database | Render `dpg-db20qap7lnhs73d6ki20-a` | Fresh owner PostgreSQL 16; migrations through `fe20261007a1`; expires **2026-11-04 20:48:43 UTC** |
| Queue | Render `red-db20qb6i0phs73cs1s4g` | Free Key Value; `noeviction`, persistence off |
| Worker / Beat | https://feedsignal-worker-preview.onrender.com; `srv-db37cjqjnfac738urbbg` | Free sleeping web preview, live `a88ad40`; one supervised worker/Beat; actual processing verified; no continuous scheduling guarantee |
| Render project | `prj-db1vl0p7lnhs73d2h55g` | Owner API/database/queue; no original account data imported |

Prepared frontend ownership changes are committed and pushed as `7b41bb7`. Dashboard Git-triggered production deployment `dpl_B2PA5q2xUS3JVrjMGjJeniPrkcqz` is READY; final landing `dpl_ETyJD64nAfmU53yrKvqrE1sZFBLY` and dashboard `dpl_AjnXBbgkXEeQn8PE5nnBBqpqMNd2` Git-triggered production deployments are READY on `3dbd3ae`. The live API contains the reviewed OAuth/Asana fixes. Owner runtime/security/email changes and tawk.to ingestion are LIVE as `9a76919`; HubSpot connection and the three tracker statuses persisted after deployment. No original maintainer account was accessed or revoked.

## Integration evidence

| Provider | Owner configuration | Actual verification / remaining work |
|---|---|---|
| Google | Approved existing My Project 41450 (`generated-wharf-500012-q3`); FeedSignal web client, matching Render/Vercel client IDs | Actual owner popup login PASS. Consent audience is **In production**; homepage/privacy/terms links persisted. Search Console homepage ownership verified with the HTML tag. Google OAuth branding re-verification waits for its stated 24-hour propagation window; retry after 2026-10-07 19:15 UTC. Login publication and branding verification are separate checks. Client secret is not exposed in frontend. |
| Slack | https://feedsignal.slack.com, team `T0C7136FUE8`; active app `A0C6U45DBEZ`; six grants including history and incoming webhook | OAuth integration **1** retained through reauthorization; bot added to **public** `#feedsignal-test` (`C0C738CFN3E`); actual test post PASS. Callback/events verification and message subscriptions configured. Worker processed signed source events into analyzed feedback 8/9. Reply round trip remains unverified. Unused Demo App remains untouched. |
| Linear | https://linear.app/feedsignal, EU; public app `510e90b8-0763-477d-a359-6b80f1b9f2d0`, team **FEE** | Connection and teams PASS; encrypted renewable tokens deployed; exactly one dynamic webhook confirmed. General-to-FEE mapping and five status mappings configured. FeedSignal created controlled issue **FEE-5**; browser Done transition returned feedback **1** as **resolved** through the signed webhook. Duplicate creation guard verified. |
| Jira | https://aayaannkausar.atlassian.net; project **feedsignal**, key **SCRUM**, id `10000` | Owner `FeedSignal API connection` token encrypted in DB; connect/test PASS. Separate user-supplied token deliberately unused. Signed webhook enabled, `jira:issue_updated`, JQL `project = SCRUM`. FeedSignal created controlled issue **SCRUM-1**; real transitions returned feedback **2** as **in_review**, then **resolved**. First delivery seeds stored state by design. |
| Asana | Owner workspace **FeedSignal** (`1219228511860712`), project **FeedSignal connection tests** (`1219243331704482`) | Encrypted owner PAT; connect/test/project PASS. Reviewed webhook ordering/race/error fix deployed (`3c95946`), 56 focused checks passed. Real handshake enabled; controlled task `1219243143676079` completion returned feedback **3** as **resolved**. No-card trial transitions to Personal; no billing/invitations. |
| HubSpot | Owner portal **247619521**, service key **FeedSignal API connection** (`56032402`) | Key privately saved and encrypted in DB; live connect/test PASS. Required account-info, contacts, companies, deals, contact-property and pipeline reads all returned HTTP 200. Scopes: contacts.read/write, companies.read, deals.read, schemas.contacts.read. ARR field `annualrevenue`; writeback remains off. Actual worker sync succeeded with 221 contacts; customer-health recompute remains unavailable (issue #3). [Service keys](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/account-service-keys). |
| Discord / Teams | Retained optional connectors | Owner confirmed neither destination exists; deferred, unconfigured. |
| Salesforce / Intercom / Zendesk | User retired these requirements | Retirement deployed and verified (`7b41bb7`): dedicated routes removed, generic enable paths blocked, settings pages return 404, notification/writeback/Beat disabled. Live OpenAPI contains no retired routes; all three generic creation attempts reject, authenticated Zendesk settings shows 404. Historical records retained. |
| tawk.to | Activated owner account; FeedSignal property `6ac54b01cc4acf34c881125c`, active widget `1k49aq1cq`; source **2** | Signed API and owner/admin UI deployed. Provider webhook registered for completed transcripts/new tickets. Controlled signed fixture produced feedback **4**, organization **1**; wrong signature **401**, accepted **200**, replay duplicate, one receipt/feedback, visitor-only text and anonymous contact verified. UI count PASS. Actual provider ticket delivery produced feedback 7; Inbox transcript correlated with feedback 6. Worker Gemini categorized feedback 7 with confidence 0.95. Public visitor chat is still blocked by HTTP 403/1010. |

The three tracker tests use explicitly labeled owner setup data, not customer evidence. Their successful webhooks require no Celery worker. Worker processing is now verified separately; these setup fixtures are not customer evidence.

## Email

Owner Resend key is stored privately and installed in API settings. Current sender is `FeedSignal <onboarding@resend.dev>`; owner explicitly approved **owner-recipient-only** verification. No sending domain is owned. Actual baseline `send_welcome_email` owner send PASS; Resend reports **delivered**, sender FeedSignal, recipient owner only. This isolated function check does not prove every deployed API email trigger.

Deployed backend copy and HTML templates use FeedSignal and owner origins; worker copies and configuration are deployed in the sleeping preview. All eight owner templates are created/published and their IDs installed in Render: team invite, welcome, password reset, weekly digest, role change, member removed, daily alert digest, alert notification. The supplied send-only key could not retrieve templates (HTTP 401); a separately named owner full-access key was created and privately installed. Transactional template paths have **no missing-template HTML fallback**. Verify remaining trigger flows; the reset email function alone does not establish an implemented reset endpoint. Seven additional owner-only helper/template deliveries passed; actual worker scheduled report generated and delivered, then test schedule disabled. Digest task execution with zero eligible users is not delivery verification.

General customer sending and inbound email stay deferred until an owned domain, DNS, sender verification and signed receiving webhook exist. Gmail support identity alone does not satisfy those requirements.

## Remaining launch work

1. Owner branding/security and remaining prepared frontend source are committed/pushed as `7b41bb7`. Backend bootstrap preserves existing users and requires explicit credentials; inbound sources guard against an absent receiving domain. Dashboard and landing production artifacts are READY. Retired public landing route definitions are removed in `3dbd3ae`; production URLs for all three return HTTP 404. Homepage returns 200, shows FeedSignal/tawk.to and has no retired-provider claims.
2. Retry Google OAuth branding verification after 2026-10-07 19:15 UTC; Search Console ownership now verified. Asana status round trip and HubSpot connection checks now pass. tawk.to owner setup, signed ingestion and UI now pass controlled checks; provider-originated ticket delivery is now verified; visitor widget accessibility remains separate.
3. Verify remaining live email triggers after the owner runtime deployment. Owner welcome delivery and eight templates now pass; general sender and inbound DNS remain deferred.
4. Maintain the deployed retirement across direct/generic API routes, UI and scheduled dispatch. tawk.to ingestion is implemented; provider-originated ticket delivery and Gemini processing are now verified.
5. Sleeping worker/Beat and owner Gemini configuration now work for development. Continuous scheduling, expiring PostgreSQL, queue durability and scheduled backups remain real-shipping requirements; isolated backup/restore rehearsal passed. No paid resource or full local baseline startup is authorized.
6. Run tenant isolation, migration/restart and full ingestion → analysis → response checks. Vercel Hobby commercial eligibility also remains unresolved; no plan upgrade authorized.

## Verification record

- tawk.to API **26 passed / 1 PostgreSQL-only skip**; isolated PostgreSQL **27 passed**, including simultaneous delivery deduplication. Temporary test IP allowlist restored exactly; isolated schema removed. UI/adjacent Linear **15 passed**, final Next.js build passed. Render deployment `dep-db2sa72jnfac73frngdg` LIVE and migration `fe20261007a1` applied; Vercel dashboard `dpl_3AaXdhKjEa6qxHTVkhPtpvX6yTUe` READY. Live controlled fixture and status screen verified; provider-originated delivery and AI processing were subsequently verified; see current checklist.

- Reviewed deployed owner/provider checks: **61 passed**; provider review independently **31 passed**.
- Linear real PostgreSQL concurrency/lifecycle checks: **16 passed** (one provider renewal for two simultaneous callers).
- Dashboard: **211 files / 1,847 tests passed** before the additional deployment-root regression; configuration checks now **4 passed**. Both actual Vercel builds are READY.
- Asana ordering/error regressions **3 passed** after observed failures; combined Asana client/regression checks **56 passed**, reviewed and deployed; real task status synchronization passed.
- Earlier landing **27 tests** and production build passed; actual provider build now READY.
- Full backend test collection is blocked by missing `onelogin`/native SAML dependencies in the local environment; no full-suite pass claimed. Deprecation warnings remain.

See [launch plan](BASELINE_LAUNCH_PLAN.md), [setup](LAUNCH_SETUP.md), and [unanswered requirements](../UNANSWERED_SECRETS.md). Actual secrets remain only in ignored private files/provider settings. Do not regenerate the established JWT/encryption keys casually.

2026-10-07 checks: **19 owner backend tests**, **6 alert-email tests**, and **80 worker email/outreach/playbook tests** passed. This was an earlier pre-worker check; the free preview and Gemini processing were subsequently verified.

## Launch completion checks, 7 October

Dashboard Git linkage now points to `Akgithub2028/FeedSignal`, production branch `feedsignal/owner-launch` (verified through Vercel API). Google branding still awaits the stated propagation window. PostgreSQL custom-format backup was restored to a temporary database: all **81 public tables** matched in counts and content hashes; temporary database removed and original IP allowlist restored exactly. Archive and evidence remain ignored/private. Automated backup scheduling and non-expiring storage are still unresolved.

Retirement checks: backend **41 passed / 1 PostgreSQL-only skip**, worker **68 passed** including schedule integrity. Final review found obsolete marketing and Zendesk onboarding; both corrected. Dashboard **1,818 tests passed**, landing **27 passed**; both production builds passed. All 148 staged files were checked against known private credential values with zero matches. API deployment `dep-db2sugss728c73ai34d0` is LIVE on `7b41bb7`. Owner login, controlled tawk feedback 4, and tracker feedback 1–3 persisted after restart. Subsequent owner Inbox correlation verified feedback 6; a controlled real provider ticket created feedback 7, then Gemini analysis persisted. Current actionable blockers and next steps are maintained in [PENDING_LAUNCH.md](PENDING_LAUNCH.md).

Final live checks: owner Slack integration remains active with signature verification configured; HubSpot test passes after restart. Public tawk retry still returns Cloudflare HTTP 403/error 1010; embed connection resets. No paid service, full local application stack or domain was provisioned.

Current controlled evidence: owner Gemini-only service-account-bound key is encrypted in org settings; model `gemini-3.5-flash-lite` passed API test and worker categorization. Usage records show 674 tokens and zero fallback for the feedback test. Scheduled executive report persisted and Resend confirmed owner delivery. Test schedule 1 is disabled. Jira legacy endpoint HTTP 410 fixed and deployed in both API/worker; focused backend 38 and worker 37 Jira checks pass. Wake-on-dispatch implementation is approved/reviewed; live verification is tracked in the pending checklist.
