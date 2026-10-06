# FeedSignal

**Customer feedback intelligence for tiny SaaS teams.** Turn customer conversations into evidence for what to build next.

Maintained by [Akgithub2028](https://github.com/Akgithub2028). Support and administrator contact: [aayaannkausar@gmail.com](mailto:aayaannkausar@gmail.com).

Repository: **[Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal)**. FeedSignal is an independent fork of [Rereflect](https://github.com/haqaliz/rereflect), distributed under the retained [MIT License](LICENSE) and [NOTICE](NOTICE).

## Current status

**Ownership conversion and complete deployment are unfinished.** Both Vercel frontends now serve FeedSignal with owner branding. The owner API runs reviewed integration revision `5ad1548`. Google owner login, Slack test posting, Linear/Jira issue creation and signed return-status synchronization, Asana task completion/status synchronization, and HubSpot connection/read permissions have passed live checks. Background processing, remaining connectors, remaining live email triggers and remaining frontend source publication remain unfinished.

Read **[ownership and deployment status](docs/OWNERSHIP_DEPLOYMENT_STATUS.md)** for the exact completed work, live resource inventory and ordered remaining steps. A successful local build, provider login or health response is not a complete release.

| Component | Owner origin | Observed state |
|---|---|---|
| Landing | https://feed-signal-ochre.vercel.app | FeedSignal production deployment READY; owner GitHub/support links verified |
| Dashboard | https://feedsignal-xi.vercel.app | FeedSignal production deployment READY; Google owner login verified |
| API | https://feedsignal-api.onrender.com | Reviewed integration revision `5ad1548` live; owner runtime/security/email changes deployed; provider retirement still open |
| Database / queue | Owner Render PostgreSQL 16 and Key Value | Provisioned; private connection details |
| Celery / Beat | Not deployed | Required for ingestion, analysis and scheduled work |

The current hosting budget is $0. Free Render PostgreSQL has an expiry, free Key Value is volatile, and the existing continuous worker has no free Render tier. Resolve full hosting before calling this a durable production SaaS. No full application stack is being started on the owner's computer.

## Baseline capabilities

The inherited code includes feedback import and classification, sentiment/pain-point/feature-request analysis, customer profiles and churn heuristics, workflow/assignment, analytics/export, organization roles, optional AI Copilot and optional external providers. These are source capabilities; their live operation depends on configured services and credentials.

- Analysis can use the baseline keyless VADER/keyword pipeline on a running worker. An external LLM is optional; BYOK or an appropriate local model is needed for selected advanced AI functions.
- Slack, Linear, Jira, Asana and HubSpot implementations are retained for owner setup. Google owner login uses FeedSignal's own OAuth client; public audience is In production; branding ownership verification remains pending. Workspace signup alone does not create an application integration.
- Resend uses the owner's key, with a restricted test sender for now. Eight owner email templates are published/configured and one baseline welcome email delivered to the owner. General customer sending and inbound email still need a verified owned domain.
- The owner requested **Salesforce removal and Intercom/Zendesk replacement with tawk.to**. Those removals and the new adapter are **pending**, not advertised as completed integrations.
- Multi-tenant authorization and external-event handling require release verification before customer use.

Local wordmarks, metadata, contact links and active frontend product copy use FeedSignal and the owner GitHub identity. Some inherited abstract artwork, screenshots and legacy blog slugs remain; they are historical/prototype material, not verified FeedSignal customer evidence. Package/schema names and wire headers are retained where compatibility requires them.

## Source layout

The Git repository contains the pnpm workspace in `rereflect/`. Paths below are relative to that workspace:

| Path | Responsibility |
|---|---|
| `services/frontend-web` | Next.js dashboard, authentication and integration settings |
| `services/landing-web` | Static Next.js marketing/documentation site |
| `services/backend-api` | FastAPI, authorization, PostgreSQL/Alembic, OAuth and webhook routes |
| `services/worker-service` | Celery ingestion, analysis, polling, notifications and Beat schedules |
| `services/analysis-engine` | Sentiment/classification and optional model components |
| `packages/ui` | Shared components, styling and FeedSignal wordmark; internal name `@rereflect/ui` retained |
| `docs/m0` | Public demand/pricing research and dataset records |
| `secrets` | Ignored private owner setup files; never commit or publish |

Next.js frontends talk to FastAPI; FastAPI and the worker share PostgreSQL and the encryption key. Redis brokers background jobs. Hosting the frontend does not run the worker.

## Setup and verification

```bash
git clone https://github.com/Akgithub2028/FeedSignal.git
cd FeedSignal/rereflect
pnpm install --frozen-lockfile
```

Use [launch setup](docs/LAUNCH_SETUP.md) for the selected Vercel/Render configuration, [self-hosting](docs/SELF_HOSTING.md) for the inherited optional Compose recipe, and [development](docs/DEVELOPMENT.md) for local development tooling. Keep credentials out of command output, Git and public documentation.

A fresh installation requires explicitly supplied `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `JWT_SECRET` and `LLM_ENCRYPTION_KEY`. The current owner values are already generated privately; do not regenerate them or overwrite existing users to change the brand. Configure backend/worker origins and shared datastore settings consistently. Populate public frontend variables before rebuilding.

For this monorepo, the dashboard build uses Webpack; extracted helper components avoid invalid Next.js Page exports. The local verification baseline uses Node 20; Vercel projects currently use Node 24, so provider builds remain a separate release check.

## Documentation

| Document | Purpose |
|---|---|
| [Ownership/deployment status](docs/OWNERSHIP_DEPLOYMENT_STATUS.md) | What is done, what is live and what remains |
| [Owner configuration](OWNER_CONFIG.md) | Confirmed identity, account, integration and hosting choices |
| [Unanswered settings](UNANSWERED_SECRETS.md) | Searchable public resolution markers; never actual secrets |
| [Launch setup](docs/LAUNCH_SETUP.md) | Exact origins, provider setup and deployment constraints |
| [Baseline launch plan](docs/BASELINE_LAUNCH_PLAN.md) | Ordered implementation and release tasks |
| [Milestone plan](docs/IMPLEMENTATION_PLAN.md) | Tiny SaaS direction and path toward the $1,000 MRR goal |
| [M0 status](docs/m0/STATUS.md) | Completed public research; real commitments/payment still unverified |
| [Architecture](docs/ARCHITECTURE.md) / [API](docs/API.md) | Baseline structure and API contracts |
| [Directory guide index](docs/DIRECTORY_GUIDE_INDEX.md) | Agent navigation and directory summaries |
| [Contributing](CONTRIBUTING.md) | Development contributions to this fork |

Original copyright, license notices, third-party attribution and technical compatibility identifiers remain intact. Historical planning documents describe their original snapshot; current owner status takes precedence.
