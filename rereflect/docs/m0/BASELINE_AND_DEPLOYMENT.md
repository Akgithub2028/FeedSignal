# FeedSignal baseline, database, and integration handoff

Source audited locally on 2026-10-05: `93359c4a2bf20310f98e42d570de50a1586812d8`.
Upstream: [haqaliz/rereflect](https://github.com/haqaliz/rereflect).

## Current owner decisions — 6 October

This is the original inherited-source audit, not the current deployment inventory. Owner GitHub/Vercel/Render access is verified; dashboard project, API, PostgreSQL and Redis now exist. The API is live on an older remote revision; frontends/worker/provider setup remain unfinished. No full local startup is requested. Salesforce removal and Intercom/Zendesk replacement remain pending. Read [current ownership/deployment status](../OWNERSHIP_DEPLOYMENT_STATUS.md) and [launch setup](../LAUNCH_SETUP.md). Statements below about absent resources describe the earlier audit date and must not be used as current status.

## Database answer

The original repository uses **PostgreSQL**, through SQLAlchemy and Alembic. Production Compose specifies **PostgreSQL 16** (`postgres:16-alpine`) with a persistent `postgres_data` volume. Source: `docker-compose.prod.yml`, `services/backend-api/src/database/session.py`, and `services/backend-api/alembic/`. The backend's local fallback database is `customer_feedback_saas`; Compose uses its configured PostgreSQL database. The worker connects to the same customer database. Redis handles Celery jobs/results/cache; it is not the primary customer-data store. SQLite appears in tests and is not a production database substitute.

**Reuse the engine and schema. Access to the original hosted database is not established.** The clone contains no populated database environment file, hosted connection URL, or database dump. No accessible listener was found at this session's `127.0.0.1:5432`; `127.0.0.1:6379` was also unavailable. These observations do not prove another machine's or a remote database's availability. `docker ps` could not inspect containers because this user was denied access to `/var/run/docker.sock`.

Missing answers: `UNANSWERED_DATABASE_REUSE_AUTHORIZATION`, `UNANSWERED_DATABASE_RETENTION_CHOICE`, `UNANSWERED_DATABASE_HOST`, `UNANSWERED_DATABASE_URL`, `UNANSWERED_DOCKER_ACCESS`.

The engine is straightforward to provision with the retained Compose recipe once Docker access and required secrets are available, or through owner-controlled PostgreSQL hosting. Render was subsequently selected; its free tier cannot host the entire continuous-worker topology. No database was created, queried with credentials, migrated, or wiped. Never seek access to the original maintainer's database merely because its source code is public.

If retaining existing data, first establish ownership and backup/restore; inspect users, organization roles, integration metadata, source mappings, and encryption-key availability. Preserve `LLM_ENCRYPTION_KEY` until encrypted records are migrated; changing `ADMIN_EMAIL` does not transfer an existing account. If no usable owner-controlled database exists, propose a fresh PostgreSQL instance and obtain a retention decision before provisioning.

## Deployment recipes retained

| Component | Baseline recipe | Ownership / readiness |
|---|---|---|
| Backend FastAPI | `services/backend-api/railway.toml`: Railway root `services/`, Dockerfile `backend-api/Dockerfile`; Compose backend service | Actual account and public API URL unanswered. |
| Celery worker + Beat | `services/worker-service/railway.toml`: root `services/`, Dockerfile `worker-service/Dockerfile`; worker `start.sh` starts Beat | Keep as a long-running worker. Scheduler topology must prevent duplicate Beat schedulers at scale. Not running/verified here. |
| App frontend | Next.js app `services/frontend-web`; Railway Docker recipe also exists | Proposed Vercel app name `feedsignal`; account/project URL unanswered. |
| Landing frontend | Static Next.js export `services/landing-web`; Railway Docker recipe also exists | Second Vercel project may use `feedsignal-landing`; owner account and domains unanswered. |
| PostgreSQL | Compose `postgres:16-alpine` | Engine retained, live instance unanswered. |
| Redis | Compose Redis service, worker configuration in `src/config.py` | Live instance/access unanswered. |

Do not assume Railway is the original live host solely from its config files. Preserve it as the existing deployment option. Vercel ownership is not inherited by cloning. No local `.vercel` metadata or `vercel.json` was found. Follow [Vercel's monorepo setup](https://vercel.com/docs/monorepos) and the owner's account before linking projects; app and landing both depend on `packages/ui`.

## Inherited capabilities (current launch scope differs)

| Capability | Actual implementation entry points | Missing owner-controlled setup |
|---|---|---|
| Slack OAuth / alerts | Backend `src/api/routes/integrations.py`; Slack adapter and source webhooks | `UNANSWERED_SLACK_CLIENT_ID`, `UNANSWERED_SLACK_CLIENT_SECRET`, `UNANSWERED_SLACK_SIGNING_SECRET`, workspace/channels/Events API setup. |
| Jira Cloud | Backend `jira_integration.py`, `jira_webhook.py`; worker `src/tasks/jira_sync.py` | `UNANSWERED_JIRA_SITE_URL`, account email, token, projects/webhook settings. Email + API token, not Jira OAuth. |
| Linear | Backend `linear_integration.py`, `linear_webhook.py` | OAuth registration and workspace/team authorization; `UNANSWERED_LINEAR_CLIENT_ID` and secret. |
| Google login | Frontend `components/GoogleSignInButton.tsx`; backend `google_auth.py` and auth routes | `UNANSWERED_GOOGLE_CLIENT_ID` and consent/origin configuration. |
| Email / Resend | Backend `email_webhooks.py`, `email_service.py`; worker `src/email.py` | API key, verified sending/receiving domains, webhook secret/templates. |
| Intercom | Token connection routes, legacy OAuth routes, worker sync/writeback | Owner workspace token/client secret or chosen OAuth registration; both existing paths retained. |
| Zendesk | Backend connection/webhook routes; worker sync/status tasks | Subdomain/account email/API token and signing setup. |
| Asana | Backend connection/issue/webhook routes | Personal access token, workspace/project, optional webhook handshake. |
| HubSpot | Backend private-token routes; worker sync/writeback | Private-app token and portal/property mapping. |
| Salesforce | Backend OAuth routes; worker token refresh/sync/writeback | Client credentials, callback, authorized organization. |
| Discord / Teams | Backend webhook integrations; worker notification dispatch | Owner destination webhook URLs. |
| Generic webhooks / CSV / usage API | Feedback source routes, import paths, worker source/usage tasks | CSV can be demonstrated without provider credentials; signed external sources and usage events require configured source/API credentials. |
| OIDC / SAML | Backend auth and IdP-config routes; frontend login/settings | Optional owner IdP configuration; retained, not activated. |
| AI providers / local mode | Backend/worker provider resolvers and analysis engine | BYOK/local endpoint optional; keyless VADER pipeline remains available. |
| Sentry | Conditional runtime DSN initialization, frontend source-map configuration | Owner configuration optional; old build org/project identifiers require M1 replacement or upload disablement. |

Retained source does not prove successful installation or tenant-safe deployment. No external tokens were tested. `services/integration-service/` contains a README only; it is not a separately implemented integration runtime. Use the backend/worker implementations above as source evidence.

## M1 ownership implementation queue

1. Apply FeedSignal to active UI text and supported email templates; GitHub-only social presence; preserve upstream license/notice and internal identifiers.
2. Remove the embedded bootstrap password and original-owner email privilege defaults; use explicitly configured administrative identity. Test empty/fresh/existing database behavior without promoting an existing user merely from an environment change.
3. Make original-domain destinations configurable: frontend privacy/terms redirects, public share CTAs, metadata/SEO, email links/senders, and generated inbound-email domains. Unanswered domains must result in safe local/unconfigured behavior, not links to the original creator.
4. Audit per-organization sender/integration settings if a database is retained. Reconnection must not accidentally retain an old webhook secret when a connector supports keeping omitted settings.
5. Wire needed OAuth, email, public-URL, and worker refresh variables into Compose. A root `.env` does not automatically enter a container with an explicit environment list.
6. Reproduce the plan's churn direction, SQL timeout/isolation, and usage commit-before-dispatch defects. Source observations are not executed reproductions; fixes require meaningful tests.
7. Validate runtime credentials before deployment; never treat `UNANSWERED_*`, empty values, or example defaults as valid production credentials. Configure production public variables before rebuilding the frontend.

All unresolved fields and credential destinations are indexed in [UNANSWERED_SECRETS.md](../../UNANSWERED_SECRETS.md). The revised public-research M0 is complete; real usage and payment checks remain M2 commercial gates. Research completion does not resolve missing deployment credentials.
