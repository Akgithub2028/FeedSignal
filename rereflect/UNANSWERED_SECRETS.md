# FeedSignal — unanswered configuration and credentials

Updated: 2026-10-07. This is a **public checklist**, not a secrets vault. Never insert passwords, API keys, OAuth secrets, tokens, database URLs containing passwords, or secret webhook URLs into this file. Record only resolution status and the secure location of a value. Supply actual secrets through ignored local files or provider secret settings.

## Confirmed decisions

| Setting | Value / decision |
|---|---|
| Product name | **FeedSignal** |
| Lowercase project slug | `feedsignal` |
| Positioning | Customer feedback intelligence for tiny SaaS teams; turn conversations into evidence for what to build next. |
| Support contact | `aayaannkausar@gmail.com` |
| Administrative email | `aayaannkausar@gmail.com` |
| GitHub identity / only current social profile | [Akgithub2028](https://github.com/Akgithub2028) |
| Current integration scope | Remove Salesforce and replace Intercom/Zendesk with free support ingestion. tawk.to selected; adapter/removal pending. Other connectors retained. |
| Hosting | Existing Vercel feed-signal landing and created feedsignal dashboard; Render owner API/PostgreSQL/Redis provisioned, no worker. Railway/Compose remain inherited fallback recipes. Full local startup withdrawn. Budget $0; continuous-worker/durable-database topology unresolved. |
| Database engine | Retain PostgreSQL; production Compose specifies `postgres:16-alpine`. Redis is the job broker/cache, not the customer-feedback database. |

The working name is selected for this repository. Domain, trademark, and account-name availability are not established. Owned repository is [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal); no owned domain is claimed.

## Placeholder convention and resolution procedure

Every missing item has the exact marker `UNANSWERED_<ID>`. Find references with `rg -n 'UNANSWERED_[A-Z0-9_]+' . ../Implementation_Plan.md`.

- In documentation, markers identify questions and missing evidence.
- In environment templates, secrets stay **empty** and markers appear in comments. Optional services remain unconfigured. A nonempty fake OAuth secret or signing key can enable broken behavior, so do not use marker text as a real secret.
- Local URLs such as `http://localhost:3000` are development defaults, not answers about production domains.
- No real secrets belong in `NEXT_PUBLIC_*`, Markdown, committed examples, logs, or Git history.
- When an item is resolved, replace its nonsecret configuration where appropriate; change this checklist row to `RESOLVED`, with the provider/environment/key name holding its secret. Keep historical evidence accurate.
- Do not bulk-replace identical marker strings with a secret throughout the repository. Populate the secure runtime setting only.
- `.env` and `.env.local` are ignored. Check `git check-ignore` before writing other secret filenames; the existing rules do not ignore every possible `.env.*` name.

## Identity, deployment, and data decisions

| Marker | Missing answer | Current disposition |
|---|---|---|
| `UNANSWERED_OWNER_LEGAL_NAME` | Owner/company legal identity for terms and privacy | GitHub username is known; legal name was not supplied. |
| `UNANSWERED_GITHUB_REPOSITORY_URL` | Owned repository | RESOLVED: https://github.com/Akgithub2028/FeedSignal; local origin matches and remote main/rereflect/package.json fetched. |
| `UNANSWERED_MARKETING_ORIGIN` | Marketing HTTPS origin | RESOLVED: https://feed-signal-ochre.vercel.app, verified assigned Vercel production domain. Custom domain not required initially. |
| `UNANSWERED_APP_ORIGIN` | App HTTPS origin | RESOLVED: https://feedsignal-xi.vercel.app assigned; production/preview frontend variables installed, dashboard production READY. |
| `UNANSWERED_API_ORIGIN` | Public backend HTTPS origin | RESOLVED: https://feedsignal-api.onrender.com; initial owner service deployment live, local owner code still to publish. |
| `UNANSWERED_INBOUND_EMAIL_DOMAIN` | Receiving domain and DNS control | Needed before replacing generated inbound addresses and provisioning Resend receiving. |
| `UNANSWERED_VERCEL_TEAM` | Vercel team/access | RESOLVED: CLI confirms akgithub2028; team akgithub2028s-projects, ID team_Z1Wh41hc04xfBLPGrxCMAV0J. |
| `UNANSWERED_VERCEL_APP_PROJECT` | Dashboard app project | RESOLVED: feedsignal, prj_CLpIHzfOs7tjzWwUUqDEaKVHAO8T; root rereflect/services/frontend-web; linked/configured; production READY. |
| `UNANSWERED_VERCEL_LANDING_PROJECT` | Landing project ID/URL | RESOLVED: feed-signal, ID prj_oVq53qCrAcsYhbmwNqmynoIFCrHf; root rereflect/services/landing-web; https://feed-signal-ochre.vercel.app. Local folder linked. |
| `UNANSWERED_BACKEND_HOSTING_ACCOUNT` | Backend hosting | RESOLVED: CLI confirms aayaannkausar@gmail.com; workspace tea-danhmfv40ujc73c05hqg; project prj-db1vl0p7lnhs73d2h55g, environment evm-db1vl0p7lnhs73d2h560. |
| `UNANSWERED_BACKEND_PROJECT_URL` | Backend project/API origin | RESOLVED: API https://feedsignal-api.onrender.com, service srv-db210qh7lnhs73d79kq0 in the owner Render project. |
| `UNANSWERED_DATABASE_REUSE_AUTHORIZATION` | Original database reuse | CLOSED / NOT REQUIRED: fresh owner-controlled PostgreSQL; no original database access requested. |
| `UNANSWERED_DATABASE_RETENTION_CHOICE` | Data retention | RESOLVED: fresh PostgreSQL; no original users/tokens imported, no original database deleted. |
| `UNANSWERED_DATABASE_HOST` | Fresh PostgreSQL hosting | PROVISIONED: Render PostgreSQL16 dpg-db20qap7lnhs73d6ki20-a, available; expires 2026-11-04 20:48:43 UTC. Durable production choice remains OPEN. |
| `UNANSWERED_DATABASE_URL` | Backend/worker DATABASE_URL | INSTALLED IN API SETTINGS: private owner connection details in ignored secrets/render-postgres-private.json and render-api.env. Worker installation pending. |
| `UNANSWERED_DOCKER_ACCESS` | Local Docker access | DEFERRED / NOT REQUIRED for selected cloud operation. Agent Docker socket access denied; no full local startup requested. |
| `UNANSWERED_EXISTING_CONNECTION_INVENTORY` | Owner hosting environment inventory | VERIFIED: API/fresh PostgreSQL/Redis now exist; dashboard project/config exists. API owner values installed; no original account data imported. Full connected-workspace DB inventory/end-to-end checks remain pending. |
| `UNANSWERED_LOGO_ASSETS` | Whether to replace inherited logo/images/screenshots | Existing assets remain upstream artifacts; text identity is recorded separately. |
| `UNANSWERED_NAME_AVAILABILITY` | Domain/account/legal clearance for FeedSignal | Pending before public launch; name is a working product choice. |

## Current cloud launch blockers

See [current ownership/deployment status](docs/OWNERSHIP_DEPLOYMENT_STATUS.md), [launch setup](docs/LAUNCH_SETUP.md) and [baseline launch plan](docs/BASELINE_LAUNCH_PLAN.md). Current instructions authorize cloud setup, not paid resources or full local application startup.

| Marker | Missing answer / evidence | State |
|---|---|---|
| `UNANSWERED_CLOUD_TOPOLOGY` | Continuous worker and durable database within $0 cloud constraint | OPEN: no free Render worker; Vercel functions cannot run the existing continuous Celery process. |
| `UNANSWERED_VERCEL_PLAN_ELIGIBILITY` | Actual commercial-use-eligible Vercel plan | VERIFIED HOBBY; commercial eligibility remains OPEN. Hobby is personal/non-commercial only; no upgrade authorized. |
| `UNANSWERED_TAWK_ACCOUNT` | Owner account/property authorization | OPEN: signup filled in Firefox; human verification failed again after a refreshed retry; owner must complete signup in a supported normal browser. Account creation not confirmed. |
| `UNANSWERED_TAWK_PROPERTY_ID` | Per-organization registered property ID | OPEN; do not guess/share across tenants. |
| `UNANSWERED_TAWK_WIDGET_ID` | Optional website widget ID | OPEN; only needed when installing chat. |
| `UNANSWERED_TAWK_WEBHOOK_SECRET` | Encrypted per-source signing secret | OPEN; obtain/register after adapter implementation. |
| `UNANSWERED_TAWK_WEBHOOK_SETUP` | Transcript/ticket-create subscriptions | OPEN; proposed /api/v1/webhooks/tawk/events is not implemented. |

## Core deployment credentials

| Marker | Runtime setting / secure destination | Requirement |
|---|---|---|
| `UNANSWERED_POSTGRES_PASSWORD` | Managed PostgreSQL credential | RESOLVED privately from owner Render database; ignored secrets/render-postgres-private.json. No password belongs in this file. |
| `UNANSWERED_JWT_SECRET` | Backend JWT_SECRET | GENERATED AND INSTALLED: ignored secrets/core.env (0600) and owner API cloud setting. Do not regenerate casually; session invalidation must be coordinated. |
| `UNANSWERED_ADMIN_PASSWORD` | Backend ADMIN_PASSWORD | GENERATED AND INSTALLED: ignored secrets/core.env (0600) and API settings; live owner login/system-admin role verified. |
| `UNANSWERED_LLM_ENCRYPTION_KEY` | Backend/worker LLM_ENCRYPTION_KEY | GENERATED AND INSTALLED IN API: ignored secrets/core.env (0600). Same key must be installed in the future worker; never rotate without encrypted-record migration. |
| `UNANSWERED_REDIS_HOST` | Backend/worker REDIS_HOST | PROVISIONED / API CONFIGURED: owner Key Value red-db20qb6i0phs73cs1s4g; endpoint private in ignored files/cloud settings. Worker not deployed. |
| `UNANSWERED_REDIS_PASSWORD` | Backend/worker REDIS_PASSWORD | OWNER CONNECTION INFO STORED PRIVATELY: API uses the provider internal connection settings. Authentication/durability for the final worker must be verified; do not expose the queue publicly. |
| `UNANSWERED_DEPLOYMENT_ACCESS` | Local provider CLI/browser authorization | RESOLVED: live Vercel, GitHub and Render identities verified on 2026-10-06. Earlier DNS issue resolved. Render token generated/saved; no repeated device authorization needed. Secrets stay in provider CLI credential storage. |
| `UNANSWERED_BACKUP_AND_RESTORE` | Backup retention and restore drill record | Decide before production cutover. |

## Slack, Jira, Linear, Google login, and Resend

| Marker | Value / destination | How it is obtained |
|---|---|---|
| `UNANSWERED_SLACK_CLIENT_ID` | Backend SLACK_CLIENT_ID | CONFIGURED: active owner FeedSignal app A0C6U45DBEZ; private providers.env and Render API. |
| `UNANSWERED_SLACK_CLIENT_SECRET` | Backend SLACK_CLIENT_SECRET | CONFIGURED: private providers.env and Render API; never publish the value. |
| `UNANSWERED_SLACK_SIGNING_SECRET` | Backend SLACK_SIGNING_SECRET | CONFIGURED: private providers.env and Render API; provider challenge verified. |
| `UNANSWERED_SLACK_REDIRECT_URI` | Backend SLACK_REDIRECT_URI | CONFIGURED: https://feedsignal-api.onrender.com/api/v1/integrations/slack/oauth/callback, persisted in owner app. |
| `UNANSWERED_SLACK_WORKSPACE_CHANNELS` | Source/integration settings | RESOLVED: owner team T0C7136FUE8; integration 1, public #feedsignal-test / C0C738CFN3E; bot added and actual test posting PASS. Ingestion/analysis/reply still unverified. |
| `UNANSWERED_SLACK_EVENTS_SETUP` | Slack events/scopes | CONFIGURED: signed event endpoint and public/private message subscriptions verified; six grants deployed. Real queued ingestion still needs worker verification. |
| `UNANSWERED_SLACK_WEBHOOK_URL` | Integration UI, if using webhook alerts | RESOLVED PRIVATELY through owner OAuth incoming-webhook grant; never publish the URL. |
| `UNANSWERED_JIRA_SITE_URL` | Jira integration UI | RESOLVED: https://aayaannkausar.atlassian.net; live connection/test PASS. |
| `UNANSWERED_JIRA_ACCOUNT_EMAIL` | Jira integration UI | RESOLVED: owner account aayaannkausar@gmail.com verified by actual Jira connection. |
| `UNANSWERED_JIRA_API_TOKEN` | Jira integration UI → encrypted DB | RESOLVED PRIVATELY: generated FeedSignal API connection token, private providers.env and encrypted owner DB. Separately supplied FeedSignal token deliberately unused. |
| `UNANSWERED_JIRA_PROJECT_KEYS` | Issue creation defaults | RESOLVED: feedsignal project, SCRUM / 10000; controlled issue SCRUM-1 created. |
| `UNANSWERED_JIRA_WEBHOOK_SETUP` | Jira admin and app-generated signing settings | RESOLVED: signed /api/v1/webhooks/jira/inbound; issue_updated, project = SCRUM; real status transitions returned controlled feedback2 in_review then resolved. |
| `UNANSWERED_LINEAR_CLIENT_ID` | Backend `LINEAR_CLIENT_ID` | CONFIGURED: public FeedSignal OAuth app 510e90b8-0763-477d-a359-6b80f1b9f2d0; private providers.env and Render API. |
| `UNANSWERED_LINEAR_CLIENT_SECRET` | Backend `LINEAR_CLIENT_SECRET` | CONFIGURED PRIVATELY: installed in Render; renewable encrypted token lifecycle deployed and owner reauthorization PASS. |
| `UNANSWERED_LINEAR_REDIRECT_URI` | Backend LINEAR_REDIRECT_URI | CONFIGURED: https://feedsignal-api.onrender.com/api/v1/integrations/linear/callback, registered in owner app. |
| `UNANSWERED_LINEAR_WORKSPACE_TEAM` | Authorized integration/team settings | RESOLVED: owner EU workspace https://linear.app/feedsignal, FEE; General team mapping, five status mappings, one dynamic webhook. Controlled FEE-5 creation and signed Done→feedback1 resolved PASS. |
| `UNANSWERED_GOOGLE_CLIENT_ID` | Frontend `NEXT_PUBLIC_GOOGLE_CLIENT_ID`, backend `GOOGLE_CLIENT_ID` | RESOLVED: owner approved My Project 41450 / generated-wharf-500012-q3, matching Vercel/Render IDs. Actual dashboard popup owner login PASS. |
| `UNANSWERED_GOOGLE_CONSENT_SETUP` | Google Cloud account / app registration | PUBLIC AUDIENCE CONFIGURED: In production; owner login PASS; owner homepage/privacy/terms saved. Search Console homepage ownership verified; OAuth branding recheck pending after the stated 24-hour window (2026-10-07 19:15 UTC); old unused secret disabled. |
| `UNANSWERED_RESEND_API_KEY` | Backend/worker RESEND_API_KEY | OWNER FULL-ACCESS KEY INSTALLED: supplied send-only key could not read templates; replacement named FeedSignal templates and transactional email stored privately and in Render. Owner welcome delivered. Worker not installed; never paste values here. |
| `UNANSWERED_RESEND_FROM_EMAIL` | Backend/worker FROM_EMAIL | TEST SENDER CONFIGURED: onboarding@resend.dev in API; owner-recipient-only. General customer sender/domain verification still OPEN. |
| `UNANSWERED_RESEND_INBOUND_WEBHOOK_SECRET` | Backend `RESEND_INBOUND_WEBHOOK_SECRET` | Resend receiving webhook configuration. |
| `UNANSWERED_RESEND_TEMPLATE_IDS` | Owner `RESEND_TEMPLATE_*` settings | INSTALLED: eight owner templates created/published, IDs in ignored providers.env and Render. Welcome baseline function delivery PASS. No missing-template fallback in transactional paths; remaining live triggers/worker digests unverified. |
| `UNANSWERED_RESEND_DOMAIN_DNS` | Resend / DNS provider | Verify sending/receiving domains and record webhook `/api/v1/webhooks/email/inbound`. |

## Additional capabilities and retired requirements

| Marker | Missing answer / secure destination |
|---|---|
| `UNANSWERED_INTERCOM_ACCESS_TOKEN` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_INTERCOM_CLIENT_SECRET` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_INTERCOM_CLIENT_ID` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_INTERCOM_REDIRECT_URI` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_INTERCOM_WORKSPACE` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_ZENDESK_SUBDOMAIN` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_ZENDESK_ACCOUNT_EMAIL` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_ZENDESK_API_TOKEN` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_ZENDESK_WEBHOOK_SETUP` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_ASANA_ACCESS_TOKEN` | RESOLVED PRIVATELY: owner FeedSignal API connection PAT saved in ignored providers.env and encrypted DB; live connect/test PASS. |
| `UNANSWERED_ASANA_WORKSPACE_PROJECT` | RESOLVED: owner workspace/project mappings; reviewed webhook fix deployed, 56 focused checks passed. Real handshake and controlled task completion -> feedback3 resolved PASS. |
| `UNANSWERED_HUBSPOT_ACCESS_TOKEN` | RESOLVED PRIVATELY: portal247619521, service key FeedSignal API connection /56032402; five required scopes. Encrypted DB connection and live test PASS. |
| `UNANSWERED_HUBSPOT_PORTAL_PROPERTIES` | PARTIAL: free owner HubSpot portal247619521 created; product FeedSignal, software industry, owner confirmed6–10people. ARR mapping annualrevenue configured; account/contact/company/deal/property/pipeline reads PASS. Worker sync and enrichment pending; writeback off. |
| `UNANSWERED_SALESFORCE_CLIENT_ID` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_SALESFORCE_CLIENT_SECRET` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_SALESFORCE_REDIRECT_URI` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_SALESFORCE_ORG` | RETIRED REQUIREMENT: do not request credentials. Runtime removal/replacement is pending, not completed by this ledger. |
| `UNANSWERED_DISCORD_WEBHOOK_URL` | DEFERRED: owner confirmed no destination exists; optional connector remains unconfigured. |
| `UNANSWERED_TEAMS_WEBHOOK_URL` | DEFERRED: owner confirmed no destination exists; optional connector remains unconfigured. |
| `UNANSWERED_GENERIC_WEBHOOK_SOURCES` | Your source names and app-generated per-source secrets. |
| `UNANSWERED_OIDC_CONFIGURATION` | Optional IdP issuer/client/secret/allowed domains, encrypted app settings. |
| `UNANSWERED_SAML_CONFIGURATION` | Optional IdP metadata/signing certificate/allowed domains, app settings. |
| `UNANSWERED_SENTRY_CONFIGURATION` | Optional owner org/project/DSNs/source-map upload credential; leave telemetry disabled until chosen. |
| `UNANSWERED_AI_PROVIDER_CONFIGURATION` | Optional local endpoint or BYOK provider/model/key; keyless local analysis remains available. |

## Research completion and future customer evidence

M0 public research is COMPLETE under the owner's revised scope; [status](docs/m0/STATUS.md), [research report](docs/m0/RESEARCH_REPORT.md) and [public datasets](docs/m0/PUBLIC_DATASETS.md) record the evidence. No interview is required for M0. These entries are retained to avoid losing earlier questions, with their actual disposition; they are not infrastructure secrets.

| Marker | Disposition / evidence still needed |
|---|---|
| `UNANSWERED_FOUNDER_INTERVIEWS` | WAIVED for M0 by owner; optional worksheet only, no interviews conducted. |
| `UNANSWERED_FEEDBACK_REVIEW_TEAMS` | DEFERRED / OPTIONAL: future permissioned real-team feedback review; public data is not five-team review. |
| `UNANSWERED_PERMISSIONED_EVALUATION_DATA` | PUBLIC DEVELOPMENT DATA ACQUIRED: Banking77 local package. Representative SaaS/account evaluation data remains DEFERRED, with consent/provenance/retention needed if collected. |
| `UNANSWERED_PILOT_BRIEFS` | DEFERRED to M2: three manually verified real-team briefs. No actual brief recipient or delivered brief is recorded. |
| `UNANSWERED_PILOT_COMMITMENTS` | DEFERRED to M2 gate: three qualified teams agreeing to continued use; zero obtained. |
| `UNANSWERED_WILLINGNESS_TO_PAY` | DEFERRED to M2 gate: two explicit price-specific acceptances, with payments tracked separately; zero obtained. Competitor prices do not close this entry. |
| `UNANSWERED_PRIORITIZED_INTERVIEW_FINDINGS` | SUPERSEDED by public-source pain ranking in RESEARCH_REPORT.md; no interview findings are claimed. |
| `UNANSWERED_EXTERNAL_TEST_AUTHORIZATION` | RESOLVED for controlled owner-workspace setup messages/issues and owner-recipient-only email under explicit user authorization; no customer-workspace tests authorized. |

M0 completion denotes research and preparation, not demonstrated demand, active connections, paid subscriptions or deployable credentials. Never populate this ledger with invented commitments or actual secret values.
