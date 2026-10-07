# Deployment, ownership, and integration migration audit

Audit date: 2026-10-05. Local checkout inspected: `93359c4a2bf20310f98e42d570de50a1586812d8`.
Original repository: [haqaliz/rereflect](https://github.com/haqaliz/rereflect).

**Historical source audit.** The observations below describe the 5 October checkout, before owner setup. They are not the current deployment state. Read [ownership/deployment status](OWNERSHIP_DEPLOYMENT_STATUS.md), [owner configuration](../OWNER_CONFIG.md) and [UNANSWERED_SECRETS.md](../UNANSWERED_SECRETS.md) for current evidence. Owner infrastructure now exists; local branding/security changes are underway. The former keep-all connector policy was superseded by requested Salesforce removal and Intercom/Zendesk replacement, still pending. No secrets are recorded here.

## 1. What is actually connected?

- The local `origin` fetch/push remote points to the original repository. We need your fork/repository URL before changing it; keep the original as `upstream` for provenance if desired.
- Only example environment files were found in the checkout. No populated deployment `.env` files, `.vercel` project metadata, or `vercel.json` were found. Example credentials are configuration instructions, not evidence of live connections.
- The repo contains Railway configurations for backend, worker, frontend, and landing services, plus Docker Compose. These files describe builds and do not establish account ownership.
- OAuth app credentials are read from environment variables. Authorized workspace tokens, webhook URLs, and several integration credentials live in PostgreSQL, scoped to organizations. Copying source does not copy these connections.
- Vercel project ownership, dashboard environment variables, domains, Git integrations, and a hosted database were not accessible in this audit. They must be inventoried separately before declaring the original creator disconnected.
- Attempts to inspect `https://rereflect.ca` and `https://rereflect-landing-web.vercel.app` through the web tool failed. This does not establish that the sites are down or that they belong to your account.

Recommended default: create deployments under your accounts with a fresh database unless you have existing data to retain. Do not delete or modify the original creator's infrastructure.

## 2. Confirmed replacements and repairs

| Area | Source evidence | Required action |
|---|---|---|
| Owner bootstrap | `services/backend-api/src/seed.py` | Replace the original support-email fallback and remove the embedded default password. Require explicit bootstrap credentials. The seed only runs when there are no users: changing `ADMIN_EMAIL` does not transfer ownership in an existing database. |
| Owner invitation privilege | `services/backend-api/src/api/routes/team.py` | `SUPER_ADMIN_EMAIL` defaults to the original support address and affects permission to invite owners. Configure your verified administrative email and review existing roles/system-admin accounts. |
| Frontend redirects | `services/frontend-web/middleware.ts` | Privacy, terms, and changelog redirect to `https://rereflect.ca`; point these at your marketing deployment. |
| Landing identity and SEO | `services/landing-web/app/layout.tsx`, `app/page.tsx`, blog pages, `public/sitemap.xml`, `public/robots.txt` | Replace canonical URLs, metadata, social handle `@rereflectapp`, site name, and relevant branding with your confirmed details. |
| User-facing GitHub links | `services/landing-web/components/landing/` and frontend settings pages | Point product CTAs and maintained documentation at your repository. Retain original-repository attribution where it identifies upstream work. |
| Email sender defaults | Backend `src/services/email_service.py`, worker `src/email.py`, backend `src/services/response_sender.py` | Set your verified `FROM_EMAIL`, `FROM_NAME`, and `APP_URL`; replace original-domain fallback values. Response sending can also use organization-specific sender configuration, which requires a database audit. |
| Hardcoded alert sender | Backend `src/services/email_service.py`, `ALERT_FROM_EMAIL` | Alerts use an original-domain sender constant. Make this configurable; setting `FROM_EMAIL` alone does not fix it. |
| Hardcoded inbound email domain | Backend `src/api/routes/feedback_sources.py` | New inbound addresses are generated as `feedback-…@rereflect.ca`. Introduce your configured inbound domain and coordinate Resend/DNS setup. Existing source addresses require an explicit migration if retaining a database. |
| Email template links | Backend `src/templates/email_templates.py` and `templates/email/member_removed.html` | Replace original website/privacy/terms/app links and review the actual templates configured in your Resend account. |
| Sentry source-map target | `services/frontend-web/next.config.ts` | Sentry org is hardcoded to `rereflect`, project to `frontend-web`. Use your project identifiers or disable upload configuration. Runtime telemetry is conditional on DSN variables, so this is not evidence that data currently goes to the creator. |
| Deployment variable forwarding | `docker-compose.prod.yml` | Backend and worker receive an explicit variable list without many OAuth/email/public-URL variables. A root `.env` alone will not forward missing variables into these containers. Add explicit forwarding or a carefully scoped override for each service. |
| Product claims and legal pages | Landing privacy/terms/FAQ and historical blog copy | Replace operator/contact details and review self-hosted-only claims against your managed deployment. Domain substitution alone is insufficient. |
| Stale Stripe example | `services/frontend-web/.env.example`, backend `src/api/routes/billing.py` | A placeholder Stripe public key remains in the example, but Stripe billing endpoints were removed. No Stripe credentials are needed merely to transfer ownership; paid billing is a separate implementation. |

Retain the existing MIT copyright and permission notice in `LICENSE`. Add attribution for your modifications if appropriate. Avoid mechanically renaming internal `@rereflect/ui` imports or historical migration identifiers: those are code contracts, not external account connections.

## 3. Information needed from you first

Public/nonsecret details may be supplied in chat:

1. Product name; owner/company display name; support email; administrative email; social handles; optional replacement logo.
2. Your GitHub repository URL and whether to preserve an `upstream` remote.
3. Marketing domain, app domain, and backend API domain, or your intended temporary hosting URLs.
4. Vercel team and project names/URLs; backend hosting provider/project; whether infrastructure already exists.
5. Fresh database or existing database with data to keep; your organization/workspace name.
6. Integrations to activate now. Optional integrations can remain unconfigured.

Secret values must be entered into provider secret settings or ignored local environment files, not pasted into chat or committed. For local preparation use an ignored file such as `.env.local`; verify ignore rules before entering values. Do not use `.env.production` without checking it is ignored: the current ignore rules do not blanket-ignore every `.env.*` filename. Never put server secrets in `NEXT_PUBLIC_*` variables.

## 4. Credentials and configuration by service

| Service | Public details needed | Secret/configuration needed and where it belongs |
|---|---|---|
| Vercel | Your team/project names, Git repository, app/marketing URLs | Prefer your authenticated CLI session or connected deployment tool. Do not send your account password. If automation needs a token, keep it in a secure credential store with appropriate scope. |
| Backend/database/Redis | Hosting provider, project identity, API URL, database migration choice | Your `DATABASE_URL`, Redis configuration, and deployment credentials, stored in backend/worker secret settings. PostgreSQL and Redis should be services you control. |
| Core authentication | Your admin email and organization | Fresh `JWT_SECRET`, `ADMIN_PASSWORD`, and Fernet `LLM_ENCRYPTION_KEY` for a fresh installation. Backend/worker must use the same encryption key. Do not overwrite an existing key without migrating encrypted data. |
| Slack OAuth | Your Slack app/client ID, workspace, selected channels | Backend: `SLACK_CLIENT_ID`, `SLACK_CLIENT_SECRET`, `SLACK_REDIRECT_URI`, `SLACK_SIGNING_SECRET`. Install your app through the product's Connect flow to create a workspace token. Do not copy the original creator's token. |
| Slack alerts only | Destination workspace/channel | An incoming webhook URL can be entered through Settings → Integrations. This URL itself is a secret. OAuth registration is unnecessary if using only this webhook path. |
| Jira Cloud | `https://YOUR-SITE.atlassian.net`, account email, project keys | Enter your Atlassian API token in Settings → Integrations → Jira. The current code uses Basic-auth email/token, not Jira OAuth. Webhook signing configuration is provisioned separately in the app. |
| Linear | Your OAuth app/client ID and workspace/team | Backend: `LINEAR_CLIENT_ID`, `LINEAR_CLIENT_SECRET`, `LINEAR_REDIRECT_URI`. Authorize through Connect; inspect/replace existing workspace token and webhook configuration if keeping a database. |
| Google login | Your Google Cloud project, OAuth consent branding, web client ID | Frontend: `NEXT_PUBLIC_GOOGLE_CLIENT_ID`; backend: `GOOGLE_CLIENT_ID` for its ID-token verification path. Configure authorized JavaScript origins for your app. Current frontend uses an access-token popup flow; do not request a client secret solely for this flow. |
| Resend email | Verified sending domain, inbound domain if needed, sender address/name | Backend and worker: `RESEND_API_KEY`, `FROM_EMAIL`, `FROM_NAME`, `APP_URL`; inbound backend: `RESEND_INBOUND_WEBHOOK_SECRET`. Optional `RESEND_TEMPLATE_*` IDs must belong to your account. Configure domain verification and receiving DNS records. |
| Intercom, preferred token path | Your Intercom workspace/app | Enter access token and app client secret in the integration UI; the secret is needed for authenticated webhooks. Stored encrypted per organization. A reconnect without a new secret can preserve the old secret, so inspect/migrate explicitly. |
| Intercom legacy OAuth | Your app/client ID | Backend: `INTERCOM_CLIENT_ID`, `INTERCOM_CLIENT_SECRET`, `INTERCOM_REDIRECT_URI`. Use only if choosing that flow; token-based connections also support periodic ingestion. |
| Zendesk | Your subdomain and account email | API token entered in Settings → Integrations. Rotate/recreate webhook signing configuration and source mapping if transferring an existing database. |
| Asana | Your workspace/project | Personal access token entered in Settings → Integrations. Webhook setup includes a server-side handshake; no Asana OAuth client is required by this implementation. |
| HubSpot | Your portal and desired revenue property | Your private-app access token entered through Settings → Integrations; optional writeback permissions only if enabling that behavior. |
| Salesforce | Your Salesforce organization and OAuth app | `SALESFORCE_CLIENT_ID`, `SALESFORCE_CLIENT_SECRET`, `SALESFORCE_REDIRECT_URI` on backend; client credentials also needed by worker tasks that refresh access tokens. Authorize your organization through the product. |
| Discord / Teams | Your destination channel | Your webhook URL entered in Settings → Integrations. Treat the complete URL as a credential. |
| Sentry, optional | Your organization/project names | Your `SENTRY_DSN`, `NEXT_PUBLIC_SENTRY_DSN`, and optional `SENTRY_AUTH_TOKEN` for uploads. Leave telemetry unconfigured if you do not want Sentry. |
| AI providers, optional | Provider/model choice | Your provider key through the organization's AI settings; operator environment-key support also exists. Leave cloud AI unconfigured to use the local pipeline. |

Do not configure every service just because an integration exists. A tiny-team launch can begin with Slack and one issue tracker.

## 5. Callback and public URL contract

Let `API` be your externally reachable HTTPS backend origin and `APP` your app origin. Register exact callback URLs with your own provider applications:

| Provider | Callback / event URL |
|---|---|
| Slack OAuth | `API/api/v1/integrations/slack/oauth/callback` |
| Slack Events API | `API/api/v1/webhooks/slack/events` |
| Linear OAuth | `API/api/v1/integrations/linear/callback` |
| Linear webhook | `API/api/v1/webhooks/linear/inbound` |
| Intercom OAuth | `API/api/v1/integrations/intercom/oauth/callback` |
| Salesforce OAuth | `API/api/v1/integrations/salesforce/callback` |
| Jira status webhook | `API/api/v1/webhooks/jira/inbound`, with signing configuration generated through the app |

Set backend `FRONTEND_URL=APP`, `APP_URL=APP`, `BACKEND_URL=API`, and `CORS_ORIGINS` to the specific allowed app origins. Set frontend `NEXT_PUBLIC_API_URL=API`; set `NEXT_PUBLIC_APP_URL` where app links use it. Public frontend variables are baked into builds, so rebuild after changing them.

The existing Slack OAuth request asks for `chat:write,channels:read,groups:read`. Feedback ingestion additionally needs appropriate Events API subscriptions, channel access, and corresponding scopes. Audit the actual selected source flow before publishing the Slack app; posting permissions alone do not establish inbound message capture. [Slack OAuth documentation](https://docs.slack.dev/authentication/installing-with-oauth/).

## 6. Deployment ownership plan

1. Confirm identity, domains, database choice, and your repository. Keep old production untouched while preparing your deployment.
2. Create or identify two Vercel projects under your team: landing root `services/landing-web` and app root `services/frontend-web`. Both consume `packages/ui`, so configure monorepo dependency access and pnpm workspace installation. Check build output against landing's static `output: export` and the app's Next.js build. These are proposed settings, not verified dashboard values. [Vercel monorepo setup](https://vercel.com/docs/monorepos).
3. Run the existing FastAPI/Celery/PostgreSQL/Redis stack on your backend host. Keep the Celery worker running as a worker process; deploying the two web frontends alone does not run ingestion or scheduled jobs.
4. Add your public URL settings, required generated secrets, and only the credentials for selected integrations. For Compose, fix variable forwarding; for Railway, follow the service configuration's root/build paths.
5. Replace the confirmed code-level original-domain paths and user-facing identity. Publish operator-appropriate privacy/terms content.
6. Initialize your owner on a fresh database, or perform an explicit account/role migration on retained data. `ADMIN_EMAIL` is a bootstrap setting, not an ownership-transfer command.
7. Register your OAuth apps, exact callbacks, and webhooks; authorize your own workspaces. Keep staging and production connections separate, and avoid connecting production providers to arbitrary preview deployment URLs.
8. Verify builds, login, redirects, verified email sending/receiving, source ingestion, and issue synchronization before switching production domains.

If retaining a database: back it up; inventory connection metadata without exporting tokens; pause jobs/outreach/writeback; deactivate inherited connections; reconnect your accounts; rotate webhook secrets; verify provider-side revocation where you have authority; remove obsolete credentials once rollback requirements are resolved. Some disconnect routes merely set `is_active=False`, and Slack deletion removes a database row without provider-side revocation. Neither operation alone proves an external token was revoked. Salesforce/HubSpot disconnect behavior may purge CRM enrichment, so assess data effects first.

Do not blindly regenerate `LLM_ENCRYPTION_KEY` on an existing database: it would make stored credentials unreadable. Changing the JWT signing key invalidates existing sessions and signed state. Historical feedback and issue links need separate provenance decisions; they should not silently be attributed to your new workspaces.

## 7. Completion criteria

- Your repository is the push target; cloud projects and domains belong to your accounts.
- No original app/marketing/email destinations remain in active user flows, generated sources, or configured templates, except intentional upstream attribution.
- Your administrative account holds the intended role; bootstrap defaults cannot create an account using a built-in password.
- OAuth consent shows your app; callbacks return to your deployment; integration status identifies your workspaces/sites.
- Test Slack ingress and alert delivery using your selected channel; test Jira or Linear with a clearly marked test item and status transition. Obtain explicit test-message/issue authorization before sending to external systems.
- Valid webhooks are accepted and invalid signatures rejected; backend/worker secrets and URL configuration are consistent.
- Existing database connections are inspected and migrated where applicable; third-party tokens/webhooks are revoked or removed through authorized provider controls.
- Secrets remain outside Git and chat, production builds are validated, and retained data is backed up before cutover.

Outstanding inputs: actual owned repository URL, domains, hosting account/project IDs, database access/retention choice, and credentials for all retained integrations. Confirmed identity and contact details are in [OWNER_CONFIG.md](../OWNER_CONFIG.md). PostgreSQL 16 is the baseline database; original hosted-instance access is unverified. Runtime replacement and credential provisioning are M1 tasks; see [M0 status](m0/STATUS.md).
