# FeedSignal — unanswered configuration and credentials

Updated: 2026-10-05. This is a **public checklist**, not a secrets vault. Never insert passwords, API keys, OAuth secrets, tokens, database URLs containing passwords, or secret webhook URLs into this file. Record only resolution status and the secure location of a value. Supply actual secrets through ignored local files or provider secret settings.

## Confirmed decisions

| Setting | Value / decision |
|---|---|
| Product name | **FeedSignal** |
| Lowercase project slug | `feedsignal` |
| Positioning | Customer feedback intelligence for tiny SaaS teams; turn conversations into evidence for what to build next. |
| Support contact | `aayaannkausar@gmail.com` |
| Administrative email | `aayaannkausar@gmail.com` |
| GitHub identity / only current social profile | [Akgithub2028](https://github.com/Akgithub2028) |
| Existing integrations | Retain all implementations; reconnect using owner-controlled accounts when credentials arrive. Retained capability does not mean a live connection has been verified. |
| Existing backend deployment recipe | Retain Railway configuration and Docker Compose. Actual original hosting account/provider is unverified; no migration away from those recipes is requested. |
| Database engine | Retain PostgreSQL; production Compose specifies `postgres:16-alpine`. Redis is the job broker/cache, not the customer-feedback database. |

The working name is selected for this repository. Domain, trademark, and account-name availability are not established. Do not invent an owned domain or a created repository.

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
| `UNANSWERED_GITHUB_REPOSITORY_URL` | Actual repository URL under Akgithub2028 | Suggested repository slug is `feedsignal`, but existence/ownership are unverified. Original `origin` remains unchanged until the target is confirmed. |
| `UNANSWERED_MARKETING_ORIGIN` | Marketing HTTPS origin | No domain invented. |
| `UNANSWERED_APP_ORIGIN` | App HTTPS origin | Local frontend default remains `http://localhost:3000`. |
| `UNANSWERED_API_ORIGIN` | Public backend HTTPS origin | Local API default remains `http://localhost:8000`. |
| `UNANSWERED_INBOUND_EMAIL_DOMAIN` | Receiving domain and DNS control | Needed before replacing generated inbound addresses and provisioning Resend receiving. |
| `UNANSWERED_VERCEL_TEAM` | Your Vercel team/account slug or ID | No connected Vercel account or project link found locally. |
| `UNANSWERED_VERCEL_APP_PROJECT` | Created app project ID/URL | Requested naming basis is `feedsignal`; proposed app project name `feedsignal`. Not created. |
| `UNANSWERED_VERCEL_LANDING_PROJECT` | Created landing project ID/URL | Requested naming basis is `feedsignal`; if both projects share one team, use `feedsignal-landing` to distinguish them. This suffix is a proposal, not a supplied answer. |
| `UNANSWERED_BACKEND_HOSTING_ACCOUNT` | Owner-controlled backend account/project | Keep Railway config and Compose fallback; actual original account unverified. |
| `UNANSWERED_BACKEND_PROJECT_URL` | Created backend service/project URL | Proposed project slug `feedsignal`; no deployment created. |
| `UNANSWERED_DATABASE_REUSE_AUTHORIZATION` | Is an existing database yours to access and reuse? | No original database credentials supplied. A public code clone does not grant database access. |
| `UNANSWERED_DATABASE_RETENTION_CHOICE` | Fresh database or existing data to preserve? | Pending. Never wipe a database to resolve this. |
| `UNANSWERED_DATABASE_HOST` | Owner-controlled PostgreSQL host/provider/project | Existing engine is easily provisionable locally; existing hosted instance is not verified accessible. |
| `UNANSWERED_DATABASE_URL` | PostgreSQL connection string | Backend and worker secret settings. Do not paste a password-bearing URL here. |
| `UNANSWERED_DOCKER_ACCESS` | Permission to access the Docker daemon / usable local Docker environment | `docker ps` returned permission denied for `/var/run/docker.sock`; no container created or inspected. |
| `UNANSWERED_EXISTING_CONNECTION_INVENTORY` | Connection metadata in a retained DB and host environments | Requires authorized database/hosting access; do not export token values. |
| `UNANSWERED_LOGO_ASSETS` | Whether to replace inherited logo/images/screenshots | Existing assets remain upstream artifacts; text identity is recorded separately. |
| `UNANSWERED_NAME_AVAILABILITY` | Domain/account/legal clearance for FeedSignal | Pending before public launch; name is a working product choice. |

## Core deployment credentials

| Marker | Runtime setting / secure destination | Requirement |
|---|---|---|
| `UNANSWERED_POSTGRES_PASSWORD` | `POSTGRES_PASSWORD`, database secret manager | Fresh install: generate; existing install: obtain authorized access. |
| `UNANSWERED_JWT_SECRET` | Backend `JWT_SECRET` | Generate strong random value for fresh install; rotation invalidates sessions and signed states. |
| `UNANSWERED_ADMIN_PASSWORD` | Backend `ADMIN_PASSWORD` | Unique private bootstrap password; existing DB requires explicit account ownership procedure. |
| `UNANSWERED_LLM_ENCRYPTION_KEY` | Backend and worker `LLM_ENCRYPTION_KEY` | Same Fernet key across services; preserve or migrate an existing key before rotating. |
| `UNANSWERED_REDIS_HOST` | Backend/worker `REDIS_HOST` | Compose development default is service `redis`; managed endpoint pending. |
| `UNANSWERED_REDIS_PASSWORD` | Backend/worker `REDIS_PASSWORD` | Provider-required authentication; never expose Redis publicly without protection. |
| `UNANSWERED_DEPLOYMENT_ACCESS` | Authenticated provider CLI/session or secure token store | Account passwords must not be sent in chat. |
| `UNANSWERED_BACKUP_AND_RESTORE` | Backup retention and restore drill record | Decide before production cutover. |

## Slack, Jira, Linear, Google login, and Resend

| Marker | Value / destination | How it is obtained |
|---|---|---|
| `UNANSWERED_SLACK_CLIENT_ID` | Backend `SLACK_CLIENT_ID` | Your Slack app registration. |
| `UNANSWERED_SLACK_CLIENT_SECRET` | Backend `SLACK_CLIENT_SECRET` | Your Slack app's client secret. |
| `UNANSWERED_SLACK_SIGNING_SECRET` | Backend `SLACK_SIGNING_SECRET` | Slack app Basic Information. |
| `UNANSWERED_SLACK_REDIRECT_URI` | Backend `SLACK_REDIRECT_URI` | Your API origin + `/api/v1/integrations/slack/oauth/callback`; register exact URL. |
| `UNANSWERED_SLACK_WORKSPACE_CHANNELS` | Source/integration settings | Your workspace and selected channels; then authorize your app. |
| `UNANSWERED_SLACK_EVENTS_SETUP` | Slack Events API subscriptions/scopes | Target `/api/v1/webhooks/slack/events`; inbound permissions must match selected sources. |
| `UNANSWERED_SLACK_WEBHOOK_URL` | Integration UI, if using webhook alerts | Your incoming webhook URL; the whole URL is secret. |
| `UNANSWERED_JIRA_SITE_URL` | Jira integration UI | Your `https://<site>.atlassian.net`. |
| `UNANSWERED_JIRA_ACCOUNT_EMAIL` | Jira integration UI | Atlassian account email; do not assume it equals support email. |
| `UNANSWERED_JIRA_API_TOKEN` | Jira integration UI → encrypted DB | Generate in your Atlassian account. Current connector uses email/API token, not OAuth. |
| `UNANSWERED_JIRA_PROJECT_KEYS` | Issue creation defaults | Select your projects after connecting. |
| `UNANSWERED_JIRA_WEBHOOK_SETUP` | Jira admin and app-generated signing settings | `/api/v1/webhooks/jira/inbound`; generated secret shown once, never paste it here. |
| `UNANSWERED_LINEAR_CLIENT_ID` | Backend `LINEAR_CLIENT_ID` | Your Linear OAuth app. |
| `UNANSWERED_LINEAR_CLIENT_SECRET` | Backend `LINEAR_CLIENT_SECRET` | Your Linear OAuth app. |
| `UNANSWERED_LINEAR_REDIRECT_URI` | Backend `LINEAR_REDIRECT_URI` | API origin + `/api/v1/integrations/linear/callback`. |
| `UNANSWERED_LINEAR_WORKSPACE_TEAM` | Authorized integration + team settings | Connect your workspace; new token is encrypted in DB. |
| `UNANSWERED_GOOGLE_CLIENT_ID` | Frontend `NEXT_PUBLIC_GOOGLE_CLIENT_ID`, backend `GOOGLE_CLIENT_ID` | Google Cloud web OAuth client; configure allowed JavaScript origins and consent branding. |
| `UNANSWERED_GOOGLE_CONSENT_SETUP` | Google Cloud account / app registration | Current popup/access-token flow does not need a client secret supplied to the frontend. |
| `UNANSWERED_RESEND_API_KEY` | Backend and worker `RESEND_API_KEY` | Your Resend account. |
| `UNANSWERED_RESEND_FROM_EMAIL` | Backend/worker `FROM_EMAIL`; organization sender config | Must be authorized by Resend. Support Gmail is a contact address, not an automatically usable sender domain. |
| `UNANSWERED_RESEND_INBOUND_WEBHOOK_SECRET` | Backend `RESEND_INBOUND_WEBHOOK_SECRET` | Resend receiving webhook configuration. |
| `UNANSWERED_RESEND_TEMPLATE_IDS` | Optional `RESEND_TEMPLATE_*` settings | Templates created in your account; built-in HTML fallback exists on relevant paths. |
| `UNANSWERED_RESEND_DOMAIN_DNS` | Resend / DNS provider | Verify sending/receiving domains and record webhook `/api/v1/webhooks/email/inbound`. |

## Other retained integration capabilities

| Marker | Missing answer / secure destination |
|---|---|
| `UNANSWERED_INTERCOM_ACCESS_TOKEN` | Your workspace access token, entered in integration UI and encrypted in DB. |
| `UNANSWERED_INTERCOM_CLIENT_SECRET` | Your app client secret for token-path webhooks or backend `INTERCOM_CLIENT_SECRET` for legacy OAuth. |
| `UNANSWERED_INTERCOM_CLIENT_ID` | Backend `INTERCOM_CLIENT_ID` if selecting legacy OAuth. |
| `UNANSWERED_INTERCOM_REDIRECT_URI` | API origin + `/api/v1/integrations/intercom/oauth/callback` for legacy OAuth. |
| `UNANSWERED_INTERCOM_WORKSPACE` | Your workspace metadata and choice of token/OAuth connection. |
| `UNANSWERED_ZENDESK_SUBDOMAIN` | Your Zendesk account subdomain, integration UI. |
| `UNANSWERED_ZENDESK_ACCOUNT_EMAIL` | Zendesk account email, integration UI. |
| `UNANSWERED_ZENDESK_API_TOKEN` | Integration UI → encrypted DB. |
| `UNANSWERED_ZENDESK_WEBHOOK_SETUP` | Your webhook endpoint and generated signing configuration. |
| `UNANSWERED_ASANA_ACCESS_TOKEN` | Your personal access token, integration UI → encrypted DB. |
| `UNANSWERED_ASANA_WORKSPACE_PROJECT` | Selected workspace/project and optional webhook handshake. |
| `UNANSWERED_HUBSPOT_ACCESS_TOKEN` | Your private-app token, integration UI → encrypted DB. |
| `UNANSWERED_HUBSPOT_PORTAL_PROPERTIES` | Portal and revenue/writeback property mapping. |
| `UNANSWERED_SALESFORCE_CLIENT_ID` | Backend and worker `SALESFORCE_CLIENT_ID`. |
| `UNANSWERED_SALESFORCE_CLIENT_SECRET` | Backend and worker `SALESFORCE_CLIENT_SECRET`. |
| `UNANSWERED_SALESFORCE_REDIRECT_URI` | Backend `SALESFORCE_REDIRECT_URI`, API origin + `/api/v1/integrations/salesforce/callback`. |
| `UNANSWERED_SALESFORCE_ORG` | Your organization and optional sandbox login origin; authorize in app. |
| `UNANSWERED_DISCORD_WEBHOOK_URL` | Your destination secret webhook URL, integration UI. |
| `UNANSWERED_TEAMS_WEBHOOK_URL` | Your destination secret webhook URL, integration UI. |
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
| `UNANSWERED_EXTERNAL_TEST_AUTHORIZATION` | OPEN: permission for live third-party test messages, emails or provider-side issues, independent of M0 research completion. |

M0 completion denotes research and preparation, not demonstrated demand, active connections, paid subscriptions or deployable credentials. Never populate this ledger with invented commitments or actual secret values.
