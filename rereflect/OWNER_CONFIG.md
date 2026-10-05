# FeedSignal owner configuration

Confirmed by the owner on 2026-10-05:

- Product: **FeedSignal**; project slug: **`feedsignal`**.
- Product description: customer feedback intelligence for tiny SaaS teams.
- Support and administrative email: **`aayaannkausar@gmail.com`**.
- Current social link: **[Akgithub2028 on GitHub](https://github.com/Akgithub2028)**. No other social identity was provided.
- Keep every existing integration implementation. New owner-controlled connections require credentials and authorization; none are claimed connected yet.
- Keep the baseline PostgreSQL engine, Railway deployment recipes, and Docker Compose fallback. Actual original hosting and database access are unknown.

Product name is a working choice, not proof of domain or legal availability. Owner legal name: `UNANSWERED_OWNER_LEGAL_NAME`. Owned repository URL: `UNANSWERED_GITHUB_REPOSITORY_URL`; do not assume a `feedsignal` repository already exists.

Vercel app project naming basis is `feedsignal`. A separate landing project in the same team may need a distinct name; `feedsignal-landing` is proposed pending account setup. No cloud project has been created. Marketing/API/app domains remain unanswered.

## Applying these decisions

M0 applies the known identity to this preparation documentation and environment templates. [M0 status](docs/m0/STATUS.md) tracks completion. Runtime UI, email-template, default-admin, hardcoded URL, Sentry, and inbound-domain changes belong to the ownership tasks in M1; see the [audit](docs/OWNERSHIP_AND_INTEGRATION_AUDIT.md). They are not implemented merely by selecting a name.

Keep internal package identifiers such as `@rereflect/ui`, Docker service names, migrations, and historical attribution intact until a specific technical change requires otherwise. Changing those blindly breaks code and data contracts. Retain `LICENSE` and `NOTICE` and identify this work as derived from [Rereflect](https://github.com/haqaliz/rereflect).

Searchable settings and every unresolved credential are in [UNANSWERED_SECRETS.md](UNANSWERED_SECRETS.md). Do not store real secrets there. Unknown optional providers remain unconfigured, while their code stays available.

The supplied Gmail address is suitable as a support contact and configured admin identity. It is not proof that Resend can send using `gmail.com`. Automated sender: `UNANSWERED_RESEND_FROM_EMAIL`; receiving domain: `UNANSWERED_INBOUND_EMAIL_DOMAIN`.
