# FeedSignal owner launch setup

Updated **7 October 2026**. [Ownership/deployment status](OWNERSHIP_DEPLOYMENT_STATUS.md) is the current evidence record. This document specifies the selected setup; it does not claim all integrations or background processing work.

## Identity and assigned origins

Repository: [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal). Product FeedSignal, slug `feedsignal`, support/admin `aayaannkausar@gmail.com`; only social identity [Akgithub2028](https://github.com/Akgithub2028).

| Origin | Assigned URL | Current state |
|---|---|---|
| Marketing | https://feed-signal-ochre.vercel.app | READY; live FeedSignal branding verified |
| Dashboard | https://feedsignal-xi.vercel.app | READY; actual owner Google login verified |
| API | https://feedsignal-api.onrender.com | Reviewed OAuth commit 5ad1548 LIVE; owner runtime/security/email changes deployed; remaining provider retirement open |
| Slack workspace | https://feedsignal.slack.com | Owner app authorized; #feedsignal-test posting PASS |

No custom domain/DNS purchase is assumed. Provider dashboard URLs are administrative pages, not callback origins.

## Verified provider access

GitHub CLI identity `Akgithub2028`, Vercel `akgithub2028` in team `akgithub2028s-projects`, and Render `aayaannkausar@gmail.com` are authenticated. The previous DNS/device-authorization blocker is resolved. Reuse saved CLI authorization; only repeat login when a provider reports expiration/revocation. Never print token files.

Render workspace `tea-danhmfv40ujc73c05hqg`, project `prj-db1vl0p7lnhs73d2h55g`, production environment `evm-db1vl0p7lnhs73d2h560`. Owner resources now include API, fresh PostgreSQL and Key Value. Other projects are outside this setup.

## Vercel

Git root contains `rereflect/`; the pnpm workspace root is inside that directory. Both apps depend on `rereflect/packages/ui`, so include workspace source outside the selected app root.

| Project | ID | Git-root-relative directory | Build/output |
|---|---|---|---|
| `feed-signal` landing | `prj_oVq53qCrAcsYhbmwNqmynoIFCrHf` | `rereflect/services/landing-web` | `pnpm --filter landing-web build`; Next.js adapter auto-detects static export (no explicit outputDirectory override) |
| `feedsignal` dashboard | `prj_CLpIHzfOs7tjzWwUUqDEaKVHAO8T` | `rereflect/services/frontend-web` | `pnpm --filter customer-feedback-frontend build`; Next.js default |

Both local app folders are linked. Dashboard production/preview variables `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_APP_URL` and `MARKETING_URL` are installed with the assigned origins above. The owner Google public client ID is installed; leave Sentry unset unless owner telemetry is configured. Public variables are baked into builds and must be followed by a rebuild.

Prepared service `vercel.json` files use frozen-lockfile installation and pnpm 10.32.1. Dashboard uses `next build --webpack`, because the installed pnpm packages resolved under Webpack while Turbopack failed resolution. Local builds use Node 20; provider projects currently use Node 24, so verify provider builds separately. [Vercel monorepos](https://vercel.com/docs/monorepos).

The team is Hobby. Commercial-use eligibility remains unresolved and no upgrade is authorized. [Vercel Hobby](https://vercel.com/docs/plans/hobby).

## Render API and datastores

| Resource | Owner ID / setup |
|---|---|
| API | `srv-db210qh7lnhs73d79kq0`, free, Singapore, auto-deploy off, branch `feedsignal/owner-launch` |
| PostgreSQL 16 | `dpg-db20qap7lnhs73d6ki20-a`, available; expires 2026-11-04 20:48:43 UTC |
| Key Value | `red-db20qb6i0phs73cs1s4g`, free, `noeviction`, persistence off |
| Worker / scheduler | Not created; full hosting decision still required |

API Docker context is `rereflect/services`; Dockerfile is `rereflect/services/backend-api/Dockerfile`. Reviewed OAuth deployment is live on commit `5ad1548`; owner security/email runtime changes are included; remaining frontend source publication and provider retirement are separate tasks. `/health` and owner login have succeeded. Migration logs showed upgrade through the existing head. Verify migration head again after the final owner revision is deployed.

Private datastore credentials live only in ignored `secrets/render-*-private.json` and API settings. Core JWT, admin password, encryption key, public origins/CORS and Resend settings are installed in API cloud configuration. API settings inspection is not proof that every update reached the running process; redeploy and verify before connector registration tests.

The prepared `render.api-preview.yaml` was not applied as a Blueprint; current resources were provisioned through owner-authenticated APIs/CLI. It remains an API-only recipe and creates no worker/datastore. Do not apply it blindly on top of existing resources.

## Worker and durability still required

Run a real continuous Celery worker and one Beat scheduler initially; both share `DATABASE_URL`, Redis settings and `LLM_ENCRYPTION_KEY` with the API. Worker Dockerfile: `rereflect/services/worker-service/Dockerfile`, same build context as API. Measure memory needs for CPU PyTorch/local models before selecting compute. Verify tasks, retries and restarts rather than relying on a frontend URL.

The chosen $0 budget does not cover this complete Render topology: background workers have no free tier; free web services sleep, PostgreSQL expires after 30 days and Key Value loses queued data on restart. No paid resource or full local application startup is authorized. Resolve an actual allowed hosting arrangement before accepting customer jobs. [Render free services](https://render.com/docs/free).

## Exact provider setup and remaining verification

Owner setup is installed for Google, Slack, Linear, Jira, Asana and HubSpot. Background synchronization requires the missing worker; account registration alone is not ingestion evidence.

| Provider | Verified owner setup | Callback / remaining work |
|---|---|---|
| Slack | Active FeedSignal app A0C6U45DBEZ; team T0C7136FUE8; keys installed; integration1; bot in #feedsignal-test; posting PASS | `/api/v1/integrations/slack/oauth/callback`; signed `/api/v1/webhooks/slack/events`; ingestion/analysis/reply unverified |
| Linear | Owner app510e90b8-0763-477d-a359-6b80f1b9f2d0; encrypted renewable token; FEE mappings; real FEE-5 status roundtrip PASS | `/api/v1/integrations/linear/callback`; exactly1dynamic `/api/v1/webhooks/linear/inbound`; live24hrenewal still to observe |
| Google | Matching owner client IDs; popup login PASS; In production; homepage/privacy/terms saved | Origin https://feedsignal-xi.vercel.app; Search Console ownership verified; OAuth branding recheck pending after 2026-10-07 19:15 UTC |
| Jira | Owner site aayaannkausar.atlassian.net, FeedSignal API connection token, feedsignal/SCRUM; status roundtrip PASS | `/api/v1/webhooks/jira/inbound`, signed issue_updated, project=SCRUM |
| Asana | Owner PAT/workspace/project; real handshake and controlled task completion synchronization PASS | Signed callback uses private secret-bearing URL; never publish it |
| HubSpot | Portal247619521, service key56032402; encrypted connection/test and required reads PASS; annualrevenue mapping | contacts.read/write, companies.read, deals.read, schemas.contacts.read; writeback off; worker sync unverified |
| Resend | Full-access owner key and8published templates installed; owner welcome delivered | onboarding@resend.dev owner-only; customer sending/receiving needs owned domain/DNS |
| Discord / Teams | Optional; owner confirmed neither destination exists | Deferred/unconfigured |

Slack requires `chat:write`, `channels:read`, `groups:read`, `channels:history` and `groups:history` for the baseline selected-channel posting/polling/events paths. The public [Slack manifest](provider-setup/slack-manifest.json) is a target configuration, not proof it was applied. Do not enable events before signed challenge verification succeeds. [Slack OAuth](https://docs.slack.dev/authentication/installing-with-oauth/).

Linear workspace signup does not create an OAuth app. Its dynamic webhook creation requires the `admin` grant; app-level and dynamic webhook registrations must not double-deliver events. [Linear webhooks](https://linear.app/developers/webhooks). Normal Firefox signup succeeded after automated Google/email signup was rejected; do not change browser security signals to hide automation.

Gmail is a support contact, not a sender domain the owner can authenticate with Resend. [Resend test sender restriction](https://resend.com/docs/knowledge-base/403-error-resend-dev-domain). General inbound email waits for domain/DNS control. Transactional template paths have no fallback when template IDs are absent. All8owner template IDs are installed. Actual owner welcome function delivery passed; remaining live triggers, worker digests and domain-dependent email require separate verification.

## Retired providers and replacement

Salesforce removal and Intercom/Zendesk replacement are authorized but not implemented. Do not request their credentials. Remove active routes, UI choices, schedules and writeback while retaining migration history/provenance. Their code/UI remains visible until that task is complete.

Selected free support replacement is tawk.to. The adapter is not implemented or registered. Build signed raw-body HMAC-SHA1 verification with `X-Tawk-Signature`, per-property tenant routing, durable event receipts and deduplication of `X-Hook-Event-Id`. Normalize finished transcripts/new tickets; do not advertise historical backfill, ticket-update sync or reply writeback without implementation. [tawk.to webhooks](https://developer.tawk.to/webhooks/).

## Release gate

Follow [baseline launch plan](BASELINE_LAUNCH_PLAN.md), publish reviewed source, deploy both frontends/API, finish worker/provider setup and verify owner-only login, tenant isolation, persisted ingestion, analysis completion, tracker round trip, signed webhooks, owner email delivery and restart/retry behavior. Use [UNANSWERED_SECRETS.md](../UNANSWERED_SECRETS.md) for public status markers; secrets stay in ignored files/provider settings.

Current checks and their limits are recorded in [ownership/deployment status](OWNERSHIP_DEPLOYMENT_STATUS.md). Controlled Slack posting, Linear/Jira/Asana tracker round trips and owner welcome delivery have been verified. No fully processed live AI feedback or worker CRM sync has been verified. Complete deployment remains open.
