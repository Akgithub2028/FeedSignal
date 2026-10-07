# FeedSignal pending launch work

Updated 7 October 2026. Owner confirms strict **$0 hosting budget** and **no owned domain**. This checklist records evidence; unchecked items are not production-ready.

- [x] tawk.to ingestion, encrypted configuration, signed webhook and controlled signed fixture: deployed `9a76919`, owner feedback 4 persisted once; replay deduplicated.
- [ ] Real tawk.to delivery: public visitor chat blocked in the owner's browser too; no provider-originated event verified.
- [x] Retire Salesforce/Intercom/Zendesk from active API, frontend and background dispatch: release `7b41bb7` deployed on API/dashboard; no retired OpenAPI routes, all three create attempts rejected, authenticated Zendesk settings shows 404. Worker schedule/queued-event guards verified locally. Migration/history records preserved.
- [ ] Worker and scheduler: no cloud worker/Beat exists. Render worker has no free tier; no paid resource or full local baseline authorized. AI processing, CRM sync and digests remain unverified.
- [ ] Durable PostgreSQL: current free database expires **4 November 2026**. Select a non-expiring host or authorize an upgrade before then; no migration destination chosen.
- [ ] Redis durability: free queue has no persistence; durable broker hosting remains unresolved.
- [x] PostgreSQL backup/restore rehearsal: private custom-format backup restored into an isolated temporary database; all 81 table counts and content hashes matched. Temporary database removed and original IP allowlist restored exactly. This is a manual rehearsal, not an automated backup service.
- [ ] Customer email/inbound: no owned domain or DNS; Resend test sender restricted to owner. Obtain domain/DNS, verify sender/receiving records and signed webhook before customer use.
- [ ] Remaining owner email triggers: welcome delivered; other trigger paths need controlled verification. Customer-recipient sends cannot be verified without an authorized domain.
- [ ] Google branding verification: owner login works; provider instructed homepage propagation wait until **7 October 2026 19:15 UTC**; verification not yet approved.
- [x] Dashboard Git repository linked to Akgithub2028/FeedSignal; production branch `feedsignal/owner-launch` verified by API.
- [x] Commit/push remaining prepared frontend/docs: `7b41bb7`; dashboard Git-triggered production deployment READY. Landing production branch also tracks `feedsignal/owner-launch`; production promotion READY; live homepage has owner branding/tawk and no retired-provider claims.
- [x] Reconcile launch/status/setup docs and directory summaries; preserve pending external prerequisites explicitly.
- [ ] Complete deployed workflow: tenant isolation, retries, AI output, CRM sync/digests and persistence after restarts. This depends on the missing worker/durable storage.
- [ ] Commercial hosting eligibility: current Vercel Hobby is limited to personal/non-commercial use; commercial launch needs an eligible plan/provider.

Current deployment details: [ownership status](OWNERSHIP_DEPLOYMENT_STATUS.md). Credential/status ledger: [UNANSWERED_SECRETS](../UNANSWERED_SECRETS.md). Implementation instructions: [baseline launch plan](BASELINE_LAUNCH_PLAN.md).
