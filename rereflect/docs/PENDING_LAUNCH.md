# FeedSignal pending launch work

Updated 7 October 2026. The owner requests a **$0, fully working development deployment on the current Vercel/Render topology**, not commercial shipping. No domain is owned. This record separates observed behavior from remaining work.

## Completed and observed

- [x] Owner branding, bootstrap security, Google/Slack/Linear/Jira/Asana/HubSpot configuration and both Vercel Git links on `feedsignal/owner-launch`.
- [x] Salesforce/Intercom/Zendesk removed from active API, frontend and scheduled dispatch; historical migrations preserved.
- [x] tawk signed webhook, encrypted configuration/UI, tenant routing, durable receipt and replay deduplication. Real provider ticket delivery produced feedback **7**; provider Inbox transcript correlated with feedback **6**. Public visitor widget remains blocked separately.
- [x] Free Render worker preview **srv-db37cjqjnfac738urbbg** deployed with one supervised Celery worker and one Beat. Actual Slack feedback **8/9**, tawk feedback and HubSpot **221-contact sync** processed successfully. Health is process liveness, not broker readiness.
- [x] Owner Gemini-only bound key installed privately/encrypted; `gemini-3.5-flash-lite` model test succeeded. Real tawk feedback **7** categorized (`functionality_broken`, `export_import`, confidence **0.95**); stored Google usage **674 tokens**, **one request**, **zero fallback**. No paid billing enabled. Older 2.5 Flash-Lite rejected new users; it was not left selected.
- [x] Controlled executive-summary schedule generated a persisted report and owner-only Resend email delivered. Test schedule **1** disabled afterward. Beat daily digest ran with no eligible users; that is execution evidence, not digest-delivery evidence.
- [x] All eight owner email templates have delivered in isolated owner-only helper checks. These do not prove every application trigger.
- [x] Jira removed `/search` endpoint fixed in both clients using `/search/jql` and continuation tokens (`a88ad40`); API and worker deployed live.
- [x] API/worker redeploy persistence checked: owner login, analyzed feedback, report, CRM connection and resolved tracker statuses retained. Tawk invalid signature **401**, accepted duplicate **200**, exactly one matching receipt after restart.
- [x] Manual PostgreSQL backup/restore: all **81 tables** matched counts/content hashes; original network allowlist restored.

## Remaining development functionality

- [ ] Deploy/configure approved asynchronous wake-on-dispatch hook and verify a queued job wakes a sleeping worker. No periodic uptime pings. Cold starts delay jobs; Redis must retain them until processing.
- [ ] Customer health recomputation is unavailable in the worker image (existing GitHub issue **#3**). Primary ingestion/analysis/CRM succeeds, but derived health scores do not refresh from worker events. Resolve using one shared scoring implementation and preserve automation/notification side effects; do not silently copy a degraded scorer.
- [ ] Verify actual weekly/daily digest recipient selection and delivery. Current owner-only sender cannot deliver to other members. Continuous scheduled timing cannot be guaranteed by a sleeping free web service.
- [ ] Welcome helper has no signup call site; password-reset helper has no implemented reset endpoint/page. Team membership email triggers have local tests and template delivery evidence; do not claim an end-to-end reset flow exists. Implement/verify these flows before advertising them.
- [ ] Finish Google OAuth branding approval after provider propagation window **7 October 2026 19:15 UTC**; owner Google login already works.
- [ ] Public tawk visitor widget still returns Cloudflare **403/1010** or a blank page. Provider-originated ticket/transcript ingestion works; fix visitor accessibility separately with tawk support/provider settings.
- [ ] Complete live second-tenant authorization, broker outage/retry and sleep/wake recovery checks. Existing webhook tenant/concurrency regression checks pass; avoid asserting all live isolation paths were exercised.

## Deferred real-shipping requirements

- [ ] Free PostgreSQL expires **4 November 2026**. No non-expiring replacement/upgrade authorized. Keep an independent backup and restore before expiration.
- [ ] Free Redis lacks persistence; queue loss on restart is possible. Durable broker and automatic independent backups remain unresolved.
- [ ] Domain/DNS for customer-wide Resend sending and inbound receiving. Current `onboarding@resend.dev` sends only to the owner.
- [ ] Always-on worker/Beat and commercially eligible hosting before customer launch. The owner keeps the current free topology; this preview is not an always-on production deployment.

Verification this run: **73 worker preview/retirement/schedule tests**, **37 Jira worker/client tests**, **38 backend Jira client tests**, and **6 wake-hook tests** passed. Backend client/hook checks used `--noconftest`; full backend collection remains blocked locally by missing `onelogin`/SAML dependencies. Existing SQLAlchemy/datetime warnings remain. Earlier dashboard **1,818**, landing **27**, focused API **41** and both builds passed. Do not add overlapping test counts.

Resources and setup: [ownership status](OWNERSHIP_DEPLOYMENT_STATUS.md), [launch plan](BASELINE_LAUNCH_PLAN.md), [credential ledger](../UNANSWERED_SECRETS.md). Provider constraints: [Render free services](https://render.com/docs/free), [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [Jira supported search](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/).
