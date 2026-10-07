# FeedSignal owner configuration

Confirmed identity and choices, updated **6 October 2026**. For live evidence and remaining work, read [ownership/deployment status](docs/OWNERSHIP_DEPLOYMENT_STATUS.md).

| Setting | Confirmed value |
|---|---|
| Product / project slug | **FeedSignal** / `feedsignal` |
| Positioning | Customer feedback intelligence for tiny SaaS teams |
| Support / administrative email | `aayaannkausar@gmail.com` |
| Maintainer / only social identity | [Akgithub2028](https://github.com/Akgithub2028) |
| Owned repository | [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal) |
| Frontend hosting | Vercel; existing `feed-signal` landing and separate `feedsignal` dashboard |
| Backend hosting | Render owner project `prj-db1vl0p7lnhs73d2h55g` |
| Database | Fresh owner PostgreSQL 16; no creator data/tokens reused |
| Integration changes | Remove Salesforce; replace Intercom/Zendesk with tawk.to. Removal/adapter still pending; retain other connector implementations. |
| Budget / local runtime | $0; no paid resources authorized; no full application startup on the owner's computer |

## Owner resources

- Landing: https://feed-signal-ochre.vercel.app; Vercel project `prj_oVq53qCrAcsYhbmwNqmynoIFCrHf`, root `rereflect/services/landing-web`. Existing live version still has upstream branding.
- Dashboard: https://feedsignal-xi.vercel.app; Vercel project `prj_CLpIHzfOs7tjzWwUUqDEaKVHAO8T`, root `rereflect/services/frontend-web`. Created/configured, no deployment yet.
- API: https://feedsignal-api.onrender.com; service `srv-db210qh7lnhs73d79kq0`, Singapore, free; initial remote-main revision live. Local owner changes still to publish. Owner login and system-admin role verified against the live API.
- PostgreSQL: `dpg-db20qap7lnhs73d6ki20-a`; available, migrations observed on initial deploy; expires 2026-11-04 20:48:43 UTC.
- Redis: `red-db20qb6i0phs73cs1s4g`; free, `noeviction`, no persistence. Worker/Beat not deployed.
- Render workspace: `tea-danhmfv40ujc73c05hqg`; production environment `evm-db1vl0p7lnhs73d2h560`. Do not modify unrelated projects.
- Slack: https://feedsignal.slack.com, team `T0C7136FUE8`; authenticated owner workspace verified in Firefox. App `A0C7RSCJ7NU` exists, credentials/configuration/installation incomplete.
- Linear: owner-confirmed workspace FeedSignal, EU region; app credentials and connection pending.

Owner CLI access is verified for GitHub, Vercel and Render. Their authorization does not grant Slack/Linear/Jira/Google account access. Provider workspace login does not register the application's OAuth client.

## Branding and private configuration

Local frontends and maintained operational docs use FeedSignal, owner GitHub links and the supplied support/admin address. Shared wordmark, metadata creator fields and footer maintainer link identify the owner. Inherited artwork/screenshots and legacy technical identifiers remain explicitly recorded. See [launch plan](docs/BASELINE_LAUNCH_PLAN.md) for incomplete API/worker text and release work.

Core JWT/admin/encryption values are retained privately in ignored `secrets/core.env` (0600) and installed in API cloud settings. Resend key is in ignored `secrets/providers.env` (0600) and API settings. No Slack or Linear credential has been successfully captured. There is no deployed worker to receive the shared keys yet.

Support Gmail is a contact address. Resend test sender is `onboarding@resend.dev`, restricted to the account owner; general sending requires `UNANSWERED_RESEND_FROM_EMAIL` / owner-domain verification. Receiving requires `UNANSWERED_INBOUND_EMAIL_DOMAIN` and DNS setup. Custom domains remain undecided.

## Compatibility and remaining decisions

Keep `LICENSE`, `NOTICE`, upstream attribution, migration history, internal `@rereflect/ui`/schema identifiers and public protocol headers intact. FeedSignal is independently maintained and no original maintainer account was revoked. Railway/Compose recipes remain optional inherited deployment documentation, not evidence of the selected cloud deployment.

Owner/company legal identity: `UNANSWERED_OWNER_LEGAL_NAME`. Logo/screenshot replacement: `UNANSWERED_LOGO_ASSETS`. Continuous worker/durable production hosting: `UNANSWERED_CLOUD_TOPOLOGY`. Name/domain/legal availability and commercial Vercel plan eligibility remain unanswered. The working name is not a claim of trademark ownership.

All public resolution markers are in [UNANSWERED_SECRETS.md](UNANSWERED_SECRETS.md). Never put real secrets into Markdown or marker substitutions across the repository.
