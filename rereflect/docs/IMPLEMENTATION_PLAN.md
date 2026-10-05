
# FeedSignal: implementation plan toward $1,000 MRR

**Planning date:** 5 October 2026; public-research M0 completed 6 October 2026  
**Upstream repository:** [github.com/haqaliz/rereflect](https://github.com/haqaliz/rereflect), cloned locally in `rereflect/`.
**Owner:** [Akgithub2028](https://github.com/Akgithub2028); support/admin: `aayaannkausar@gmail.com`.
**Project slug:** `feedsignal`; actual owned repository URL: `UNANSWERED_GITHUB_REPOSITORY_URL`.
**Configuration ledger:** `rereflect/UNANSWERED_SECRETS.md` in this workspace, or `UNANSWERED_SECRETS.md` from the repository root. Never store actual secrets in the plan or ledger.
**Audited revision:** `93359c4a2bf20310f98e42d570de50a1586812d8`  
**Target:** B2B SaaS teams with approximately 2–10 employees, including suitable early YC startups.  
**Commercial objective:** At least $1,000 in recurring monthly subscription revenue.


## Owner configuration and unresolved launch settings

FeedSignal uses the known support/admin email and GitHub identity above. Domains are undecided (`UNANSWERED_MARKETING_ORIGIN`, `UNANSWERED_APP_ORIGIN`, `UNANSWERED_API_ORIGIN`). The original hosted backend/database account is not known; preserve Railway and Compose recipes until owner-controlled hosting is selected. Retain PostgreSQL as the engine; database access and retention are separate unanswered decisions.

All current Slack, Jira, Linear, Intercom, Zendesk, Asana, HubSpot, Salesforce, Discord, Teams, generic webhook, email, Google login, and SSO implementations stay available. Simplifying onboarding means guiding users through their selected sources, not deleting other connectors. Live integrations remain unverified until credentials and provider authorization are supplied. Credentials are indexed in `UNANSWERED_SECRETS.md`; do not put secret values in this document.

The canonical repository copy is `docs/IMPLEMENTATION_PLAN.md`; the workspace copy `../Implementation_Plan.md` is synchronized at M0. Future changes should update the canonical copy and any maintained workspace copy together.

## 1\. Recommended product direction

Build a **managed customer intelligence service that helps founders decide what to build next and follow up with affected customers**.

The core promise should be:

> Connect your customer conversations. Get a short weekly brief showing the problems affecting your target customers, the evidence behind them, and the next action to take.

Rereflect already has substantial functionality. Its strongest opportunity is improving reliability, onboarding, evidence quality, account context, and everyday usefulness.

The paid product should deliver this workflow:

1. Capture feedback from the channels customers already use.
2. Extract individual problems and requests.
3. Group related evidence into persistent product opportunities.
4. Show which customer accounts are affected.
5. Help a founder choose an action.
6. Link accepted work to Linear.
7. Notify the right customers after the change is available.
8. Measure whether the team continues using the workflow.

A generic “AI feedback dashboard” will be difficult to sell. The product must save recurring work and improve a specific product decision.

## 2\. Audit scope and limitations

The repository inventory contains **2,321 files, 542 directories, and 595 Markdown files**. All Markdown files were retrieved remotely. Current documentation, tracking records, planning documents, and selected implementation paths were examined.

This was a source-based audit. Local repository access was restored and M0 preparation was performed on 5 October 2026. Directory guide coverage and documentation/configuration consistency are checked in `docs/m0/VERIFICATION.md`. The application, production database migrations, provider connections, and product test suites were not executed for this documentation milestone.

The published URLs, [rereflect.ca](<https://rereflect.ca>) and [the Vercel landing site](<https://rereflect-landing-web.vercel.app>), were inaccessible through the browsing tool. Their live appearance, signup flow, and runtime behavior therefore remain unverified. Landing-page observations below refer to repository source.

Community research is qualitative. Reddit discussions contain self-promotion and unverified experiences; they suggest interview questions rather than establish demand. X searches did not produce sufficiently verifiable posts to support conclusions.

## 3\. What the baseline already provides

The current project is **free, MIT-licensed, self-hosted software**, with optional customer-provided LLM keys and a local analysis fallback.

It already includes:

- Feedback ingestion through CSV, email, webhooks, Slack, Intercom, and Zendesk.
- Sentiment, categorization, urgency, and churn-related analysis.
- Customer profiles, health scores, timelines, and segments.
- Workflow assignment, automations, playbooks, and customer outreach.
- Linear, Jira, Asana, HubSpot, and Salesforce integrations.
- Reports, scheduled reports, analytics, exports, and sharing.
- Organization isolation, roles, public API keys, and SSO capabilities.

These should generally be extended and simplified. They should not be scheduled as entirely new features. [Current README](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/README.md>)

The historical hosted service was intentionally retired, and Stripe payment routes were removed. Monetization requires a new managed-service operating model and payment lifecycle. Changing a plan flag will not restore a complete SaaS business. [Pivot record](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/docs/archive/prd/PRD-OSS-SELF-HOSTED-PIVOT.md>), [current billing routes](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/api/routes/billing.py>)

Archived PRDs explicitly warn that their status headers and commercial assumptions are stale. Current source, changelog, and maintained operational documentation must take precedence. [Archive guidance](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/docs/archive/prd/README.md>)

## 4\. Market evidence and implications

| Evidence | Implication for this product |
|---|---|
| SaaS founders describe feedback scattered across support tickets, email, Slack, and calls. | Reduce collection work through existing channels. |
| Some founders prioritize customer segment over vote totals. | Count distinct accounts and distinguish target customers from total mentions. |
| A small-team discussion describes replacing Canny internally, then encountering maintenance and notification work. | Hosting reliability and follow-through can be more valuable than a feedback board alone. |
| Hacker News discussions warn against turning every request directly into an engineering ticket. | Introduce an opportunity and decision stage before creating work. |

Sources: [fragmented feedback discussion](<https://www.reddit.com/r/SaaS/comments/1oczmyl/how_do_you_actually_manage_customer_feedback/>), [prioritization discussion](<https://www.reddit.com/r/SaaS/comments/1s7pb9b/how_do_you_guys_handle_feature_requests_from_users/>), [build-versus-buy discussion](<https://www.reddit.com/r/SaaS/comments/1rgpfy7/the_build_versus_buy_math_for_saas_has_changed/>), [feedback and backlog discussion](<https://news.ycombinator.com/item?id=39081876>).

### Competitive reality

| Product or alternative | Observed offer | Implication |
|---|---|---|
| Canny | Automatic capture and deduplication; displayed Pro entry price of $79/month billed annually, with tracked-user pricing. | AI capture and deduplication are already established features. |
| Savio | Feedback centralization, segmentation, prioritization, and closing the loop; displayed Essential entry price of $39/month paid annually, including one paid user. | Evidence-based prioritization alone is insufficient differentiation. |
| Featurebase | Support and feedback together; displayed Growth price of $29/seat/month billed yearly, plus a startup program advertising substantial discounts. | Tiny startups already have inexpensive alternatives. |
| Linear Customer Requests | Account pages, revenue/tier attributes, and requests linked to issues. | Teams already using Linear may need little additional software. |
| Dovetail | Free analysis entry point and a broader enterprise offering. | Generic summaries and research chat face strong competition. |
| Existing spreadsheet plus AI assistant | Cheap and flexible, but depends on manual collection and maintenance. | The managed workflow must clearly outperform this practical substitute. |

Sources: [Canny pricing](<https://canny.io/pricing>), [Savio pricing](<https://www.savio.io/pricing/>), [Featurebase pricing](<https://www.featurebase.app/pricing>), [Linear Customer Requests](<https://linear.app/docs/customer-requests>), [Dovetail pricing](<https://dovetail.com/pricing/>).

**Positioning hypothesis:** win through fast setup, credible evidence, account context, and dependable follow-through for a founder without a dedicated product manager.

The completed public-research report (`docs/m0/RESEARCH_REPORT.md`) compares these substitutes and prices. Test the offer through actual M2 usage and price-specific responses before expanding feature investment.

## 5\. Initial ideal customer profile

Start with a founder-led B2B SaaS team that:

- Has 2–10 employees.
- Has paying customers and recurring customer conversations.
- Receives feedback through at least two channels.
- Uses Linear or is willing to export decisions there.
- Spends at least an hour weekly consolidating or reviewing feedback.
- Has recently missed a request, duplicated work, or struggled to justify a priority.

A useful initial qualification hypothesis is **50–1,000 relevant conversations per month**. Validate this range during permissioned onboarding and usage observation; interviews are optional.

YC membership should be a prospecting filter, not the defining customer need. A bootstrapped company with repeated feedback problems may be a better customer than a YC company without sufficient feedback volume.

Initially deprioritize:

- Prelaunch products with almost no customer evidence.
- Teams satisfied with Linear’s existing customer-request workflow.
- Enterprise procurement requiring extensive certifications.
- Companies expecting a full customer support platform.
- Customers purchasing primarily for advanced churn prediction.

## 6\. Current bottlenecks

### P0: correctness and tenant protection

**1\. Default churn probability appears to reverse risk direction.**

The health service computes its churn component as `100 − average churn risk`, so higher values mean healthier customers. The probability updater passes this component into an identity fallback that interprets higher values as greater churn probability.

Consequently, the inspected fallback arithmetic turns raw risk 10 into component 90, then probability 90%. This is a high-confidence source finding requiring runtime reproduction.

**Required work:** establish consistent score semantics, correct the mapping, version affected calibration artifacts, and recompute affected outputs. Disable probability-driven customer outreach until validated.

Sources: [health scoring](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/services/health_score_service.py>), [probability updater](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/worker-service/src/services/probability_updater.py>).

**2\. Copilot SQL needs stronger isolation and cancellation.**

Organization scoping is inserted through text manipulation. This warrants adversarial checks covering Boolean expressions and joins. The executor also returns a timeout while its query thread can continue executing.

**Required work:** initially restrict the managed product to curated query functions. Before enabling arbitrary generated SQL, require a read-only database role, database-enforced timeout, robust query validation, and independently enforced tenant restrictions.

Sources: [SQL validator](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/services/copilot/sql_validator.py>), [SQL executor](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/services/copilot/sql_executor.py>). PostgreSQL supports database-side statement cancellation through [`statement_timeout`](<https://www.postgresql.org/docs/current/runtime-config-client.html>).

**3\. Usage tasks can be published before their database transaction commits.**

The usage receiver queues processing inside its insertion loop and commits the outer transaction afterward. A fast worker can see no event; the worker’s missing-event path returns a skipped result.

**Required work:** persist processing intent transactionally and dispatch committed jobs. Add recovery for committed events whose queue publication fails.

Sources: [usage receiver](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/api/routes/usage_webhooks.py>), [usage worker](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/worker-service/src/tasks/usage_metrics.py>).

### P1: value and operating cost

| Bottleneck | Required improvement |
|---|---|
| Customer identity largely uses email. | Introduce stable contacts and customer accounts, with reviewed identity mappings. |
| Feedback records have singular extracted pain-point and feature-request fields. | Support multiple evidence-backed observations within one conversation. |
| Categories and reports do not establish a complete persistent opportunity lifecycle. | Add opportunities linking evidence, accounts, decisions, delivery, and follow-up. |
| The sidebar exposes many destinations and settings. | Make the default experience a brief, opportunities, evidence, and sources. |
| Usage processing scans all historical events per customer; daily recomputation loads all rollup rows. | Use bounded rollups and paginated recomputation; avoid importing unnecessary raw telemetry. |
| Backend and worker duplicate models and business logic. | Add parity checks, then consolidate pure logic when touched by relevant work. |
| Combined public feedback updates are documented as non-atomic. | Make single-item mutations atomic and preserve explicit per-item outcomes for bulk operations. |

Sources: [customer model](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/models/customer_health.py>), [feedback model](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/backend-api/src/models/feedback.py>), [navigation](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/frontend-web/components/AppSidebar.tsx>), [technical follow-ups](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/TRACKING.md>), [API limitations](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/docs/API.md>).

### Predictive analysis should remain secondary

The churn training path uses usage and feedback features that the inspected inference path substitutes with defaults. Historical reconstruction also retains current values when historical fields are unavailable, creating potential leakage.

Existing evaluation uses held-out training splits, which is useful, but does not establish prospective account-level prediction quality. The tracking documentation explicitly states that the real-organization exit remains unvalidated.

**Required work:** establish training/serving feature parity, historical feature availability, fixed prediction horizons, eligible negative examples, and chronological account-grouped evaluation before selling predictive accuracy.

Sources: [training path](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/worker-service/src/tasks/churn_classifier_training.py>), [inference path](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/worker-service/src/services/probability_updater.py>), [evaluation](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/services/analysis-engine/src/analyzer/churn_classifier/evaluate.py>), [AI tracking](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/AI-TRACKING.md>).

## 7\. Target product and technical contracts

### A. Fast capture

Launch with CSV, forwarded email, and selected Slack channels. Reuse existing ingestion. Prioritize improvements to existing Intercom support when pilots require it.

Every ingested record should preserve:

- Tenant and source identity.
- Provider object ID and revision.
- Original timestamp, source URL, and author role.
- Processing status and failure reason.
- Import batch and replay history.

Deduplicate transport events using tenant, source instance, and provider ID. Treat an updated conversation as a revision rather than another independent customer request.

Exclude internal replies, quoted email chains, bot messages, and demo records from customer-demand counts.

### B. Stable customer accounts

Add stable account and contact entities alongside existing email fields.

Recommended relationships:

- **Customer account:** name, external ID, segment, plan, status.
- **Contact:** stable ID and email aliases.
- **External identity:** source-specific customer/contact identifiers.
- **Membership:** contact-to-account relationship.
- **Revenue snapshot:** amount, currency, recurring interval, source, effective date.
- **Feedback association:** feedback-to-contact/account mapping and confidence.

Match through explicit product/customer IDs first. Use email and domain matching as suggestions requiring appropriate review. Do not automatically combine users sharing a public email domain.

Preserve unknown identities explicitly. Backfill in batches and retain compatibility with existing APIs.

### C. Evidence-backed opportunities

Create persistent opportunities representing underlying customer problems.

Each opportunity should contain:

- Problem statement and affected workflow.
- Exact supporting excerpts and source links.
- Distinct account count and conversation count.
- Target-customer relevance.
- Associated recurring revenue, with coverage and freshness.
- Supporting and contradictory evidence.
- Proposed next action.
- Human owner, effort estimate, status, and decision rationale.
- Linked delivery work and follow-up state.

A single conversation can support several opportunities.

Store evidence spans separately from generated descriptions. Record source revision, character offsets or message identifiers, extraction version, and model provenance.

Use AI to propose matches. Begin with human-confirmed merges and support splitting incorrectly grouped opportunities.

### D. Transparent prioritization

Show distinct account demand, target-segment relevance, urgency evidence, associated revenue, and estimated effort.

Start with clear filters and sort orders. Introduce configurable scoring only when customers ask for it.

Label financial figures **associated MRR**. This is the revenue of accounts discussing a problem; it does not establish how much revenue a feature will generate or save.

Avoid counting:

- Multiple contacts from one account as independent accounts.
- Repeated conversation imports as additional demand.
- Trial users as paying customers.
- Unknown revenue as zero revenue.
- Different currencies as directly additive without a stated conversion policy.

### E. Weekly decision brief

Deliver a short brief containing:

1. Three opportunities worth reviewing.
2. Changes since the previous brief.
3. Significant customer blockers.
4. Decisions awaiting an owner.
5. Fixes awaiting customer follow-up.
6. Data freshness and coverage.

Every material claim should link to supporting evidence.

Allow “insufficient evidence” and “no significant change.” Do not manufacture a full report for a quiet week.

Reuse existing scheduled-report infrastructure. Add deterministic counts and comparisons before generating narrative.

### F. Closing the loop

Extend existing issue links and outreach into an explicit lifecycle:

**Observed → reviewed → selected → in progress → available → notified → outcome reviewed.**

An issue marked done does not prove a feature is deployed or available to every customer. Require a release confirmation or an approved release signal before notifying customers.

Follow-up delivery must include approval, recipient preview, unsubscribe handling, deduplication, delivery status, and recovery after failures.

## 8\. Implementation milestones

**Working assumption:** one experienced implementation engineer, with founder-led research and sales running alongside development. Dates are targets; release gates take priority.

### M0 — Complete public research and prepare repository guides

**Target:** 5–11 October.  
**Dependency:** none.  
**Status on 6 October:** COMPLETE under the owner-revised public-research scope. Interviews are waived; product-specific commitments and willingness to pay are unverified and deferred to M2. The former real-customer validation gate was replaced explicitly, not achieved through public or synthetic evidence.

**Completed repository deliverables**

- [x] Verify local clone at the audited baseline revision.
- [x] Select **FeedSignal**, project slug `feedsignal`, owner GitHub `Akgithub2028`, support/admin `aayaannkausar@gmail.com`.
- [x] Retain all existing integration implementations. Missing credentials do not justify removing a connector.
- [x] Audit original-owner references and configuration; create `docs/OWNERSHIP_AND_INTEGRATION_AUDIT.md` and `OWNER_CONFIG.md`.
- [x] Record every unknown account/domain/credential/data-retention choice in `UNANSWERED_SECRETS.md`, with `UNANSWERED_<ID>` markers and secure destinations.
- [x] Update example environments with confirmed identity, development-only URLs, and empty secrets. These examples are not deployable production settings.
- [x] Identify PostgreSQL 16 and Redis in Compose, and retain Railway recipes. Original hosted database access is unverified; local Docker inspection is blocked by socket permissions. Track the decision instead of assuming reuse or wiping data.
- [x] Create a `directory.md` for the repository root and every baseline tracked directory, plus directories introduced by M0; index them in `docs/DIRECTORY_GUIDE_INDEX.md` with a complete file inventory in `docs/DIRECTORY_FILE_INDEX.md`.
- [x] Prepare the founder-interview runbook, pilot/evaluation worksheets, database/hosting handoff, and verification record under `docs/m0/`.

**Completed research deliverables**

- [x] Review public pain and counterexamples, existing substitutes, and six official pricing/product pages; write `docs/m0/RESEARCH_REPORT.md` and dated `pricing_signals.csv`.
- [x] Find Banking77, Bitext and ABCD; document provenance, licenses, limitations and acquisition instructions in `docs/m0/PUBLIC_DATASETS.md`.
- [x] Acquire Banking77 locally: 13,083 labeled examples / 77 intents, unchanged upstream bytes, original license, source hashes, schema and duplicate/overlap checks. Other candidates are sourced, not downloaded.
- [x] Rank observed pain qualitatively; specify the $59/$99 workspace hypothesis, billable-conversation contract, $1,000 MRR arithmetic and conversion sensitivity. Competitor offers are pricing signals, not proven FeedSignal willingness to pay.
- [x] Replace interview-led M0 prerequisites with public research, as the owner requested. Preserve optional interview worksheets and move real usage, pilot briefs, commitments and payment evidence to later milestones.
- [x] Synchronize status, ledger, evaluation protocol and both plan copies; refresh directory guides and verify local links, provenance and placeholders.

**Revised gate and remaining evidence**

M0 permits M1 reliability/ownership work and a bounded M2 prototype/pilot. It does not validate product-market fit. No real team commitment, FeedSignal price acceptance or payment was obtained. During M2, use permissioned onboarding artifacts and asynchronous/in-product responses; scheduled interviews are optional. Require three qualified continued-use commitments and two explicit price-specific acceptances before expanding M3–M6, retaining the three-recurring-paid-pilot target. If evidence is weak, revise the segment/offer rather than building the full roadmap.

`docs/m0/STATUS.md` is the completion and scope-change ledger. Runtime rebranding, secure bootstrap changes, hosted provisioning and live reconnection remain M1 tasks; preserve every existing integration capability. Missing provider credentials still block their deployment, independently of completed research.

### M1 — Establish a trustworthy managed baseline

**Target:** 12–25 October.  
**Dependency:** M0.

**Actions**

- Reproduce and correct the churn-direction problem; disable affected automation meanwhile.
- Restrict hosted copilot queries to curated functions.
- Add database-enforced query timeouts and tenant-isolation regression checks.
- Repair commit-before-dispatch behavior and add durable recovery.
- Audit inherited integrations for managed multi-tenant use.
- Apply the confirmed FeedSignal identity to runtime UI/templates and GitHub-only social presence. Preserve upstream MIT/NOTICE attribution and internal package/data contracts.
- Replace original-owner bootstrap defaults and embedded password; test new versus existing-database behavior. Make original-domain redirects, senders, inbound addresses, and Sentry targets configurable using confirmed owner settings.
- Preserve all connector implementations. Wire missing OAuth/email/public-URL variables into Compose; authorize owner-controlled workspaces only after credentials are securely provisioned.
- Resolve only required entries from `UNANSWERED_SECRETS.md` before enabling a provider. Never use placeholder strings as credentials or overwrite an existing encryption key without migrating data.
- Deploy API, worker, scheduler, frontend, PostgreSQL, and Redis.
- Keep databases private; configure backups and test restoration.
- Introduce explicit managed-service configuration and subscription entitlements.
- Add subscription checkout, cancellation, payment-state synchronization, and reconciliation.
- Keep customer-data revenue imports separate from the product’s own subscription billing.
- Add bounded model budgets before providing a platform-funded LLM key.

Stripe webhook processing must verify signatures, tolerate duplicate deliveries, and reconcile subscription state. [Stripe webhook guidance](<https://docs.stripe.com/webhooks>)

**Acceptance**

- Cross-tenant API, background-job, cache, export, and shared-link checks pass.
- A timed-out query stops in PostgreSQL.
- Worker execution sees committed records.
- Queue failures recover without duplicate effects.
- A paid subscription creates the expected entitlement; cancellation updates it.
- A backup restores into an isolated environment.
- Self-hosted operation retains its existing unrestricted behavior.

**Gate**

Accept a small number of paid pilots after these checks pass. Reliability defects block onboarding expansion.

### M2 — Make the first useful result fast

**Target:** 26 October–1 November.  
**Dependency:** M1.

**Actions**

- Add a setup flow covering product context, target customer, and first source.
- Offer clearly labeled sample data.
- Improve CSV mapping and import previews.
- Simplify selected-channel Slack and forwarded-email setup.
- Show accepted, duplicate, rejected, pending, and failed records.
- Provide a recovery action for stalled imports.
- Simplify primary navigation to Brief, Opportunities, Evidence, and Sources.

Slack ingestion must verify request signatures and replay freshness. [Slack verification guidance](<https://docs.slack.dev/authentication/verifying-requests-from-slack/>)

**Acceptance**

- At least four of five pilot teams reach a useful result within 15 minutes using prepared data.
- Repeating an import does not inflate counts.
- Failed records have actionable explanations.
- Disconnecting a source prevents subsequent ingestion.

**Commercial validation gate:** during M2 record three dated continued-use commitments and two explicit acceptances of a concrete $59/$99 offer from qualified decision makers. A waitlist, public post, demo or competitor price does not qualify. Use asynchronous responses and observed use; interviews are optional. Do not expand M3–M6 until this evidence exists.

**Commercial target:** three recurring paid pilots; successful recurring payment is stronger evidence than price acceptance. See `docs/m0/PILOT_AND_EVALUATION.md`.

### M3 — Introduce account-level identity and revenue context

**Target:** 2–8 November.  
**Dependency:** M2.

**Actions**

- Add stable account, contact, identity, and membership records.
- Backfill existing customer emails without destructive replacement.
- Build reviewable account matching and merge handling.
- Start revenue enrichment with CSV.
- Preserve currency, interval, freshness, and unknown values.
- Add a billing-data connector only if repeated pilot demand justifies it.

**Acceptance**

- Two contacts belonging to one account contribute one account to opportunity demand.
- Email changes preserve history.
- Reviewed merges retain provenance.
- Unknown mappings and missing revenue remain visible.
- Existing customer APIs continue working during migration.

**Commercial target:** five paying teams.

### M4 — Build persistent, cited opportunities

**Target:** 9–22 November.  
**Dependency:** M3.

**Actions**

- Add opportunities, evidence spans, associations, and decision records.
- Extract multiple observations from conversations.
- Suggest semantic matches to existing opportunities.
- Provide merge, split, dismiss, and watch controls.
- Add account/segment filters and transparent ranking.
- Preserve human corrections during reprocessing.
- Add model versioning, cached extraction, bounded retries, and abstention.

**Acceptance**

Use held-out pilot examples, including negation, vague requests, multiple problems, internal replies, and repeated conversations.

Initial release targets:

- Every displayed quotation matches its underlying source.
- Every numeric claim comes from deterministic aggregation.
- At least 90% of sampled proposed evidence links are judged relevant.
- No cross-tenant evidence appears.
- Model outage leaves a usable import/review workflow.
- Corrections survive reanalysis.

Treat these as product quality gates, not guarantees of universal accuracy.

### M5 — Deliver a recurring weekly brief

**Target:** 23–29 November.  
**Dependency:** M4.

**Actions**

- Extend scheduled reports with opportunity changes and pending decisions.
- Deliver through email and optionally Slack.
- Add source freshness and identity/revenue coverage.
- Let recipients acknowledge, dismiss, assign, or inspect evidence.
- Suppress repetitive alerts and unchanged reports.
- Measure meaningful review activity.

**Acceptance**

- Three of five pilots use the brief for a real product decision over two consecutive weeks.
- Retry delivery does not send duplicate briefs.
- Quiet weeks produce appropriately short reports.
- Evidence access respects tenant permissions.

**Commercial target:** eight paying teams and two permissioned case studies.

### M6 — Link decisions to delivery and follow-up

**Target:** 30 November–6 December.  
**Dependency:** M4–M5.

**Actions**

- Extend Linear integration to opportunity-level work.
- Draft an issue with the problem, evidence, acceptance criteria, and unresolved questions.
- Require human approval before creating work.
- Track delivery separately from release availability.
- Draft updates for the affected customers.
- Reuse existing outreach suppression and unsubscribe controls.
- Record follow-up outcomes without claiming causal revenue impact.

**Acceptance**

- Repeated creation attempts do not duplicate issues.
- Closing an issue does not automatically notify customers.
- Replayed release events do not duplicate outreach.
- Opted-out customers remain excluded.
- One pilot completes the capture-to-release-to-follow-up workflow.

**Commercial target:** ten paying teams.

### M7 — Reach and retain $1,000 MRR

**Target:** 7–27 December.  
**Dependency:** successful paid pilots.

**Actions**

- Continue narrowly targeted founder outreach.
- Publish permissioned examples demonstrating a useful decision or reduced review work.
- Offer migration through CSV rather than building many bespoke connectors.
- Add an integration when at least three paying teams request it or it unlocks qualified sales.
- Optimize measured slow queries and costly processing paths.
- Add incremental usage rollups, bounded retention, and paginated recomputation where required.
- Reduce recurring support burden.
- Review retention and acquisition conversion weekly.

**Acceptance**

- At least $1,000 normalized recurring subscription revenue.
- Exclude setup fees, trials, and unpaid commitments.
- Target at least 80% second-month retention among eligible customers.
- Target at least 60% weekly meaningful use.
- Target variable infrastructure/model/delivery gross margin above 75%.
- Track founder support time separately.

**Fallback**

If usage is weak despite successful onboarding, inspect behavior and request asynchronous feedback from inactive customers before adding features. Interviews are optional. Revise the brief, segment, or job being solved.

## 9\. Architecture and implementation rules

Retain the existing Next.js, FastAPI, SQLAlchemy, PostgreSQL, Celery, and Redis architecture.

### Data and jobs

- Apply additive migrations and maintain one Alembic head.
- Backfill in bounded batches.
- Require tenant identifiers in new entities, jobs, cache keys, and vector queries.
- Persist job intent in the same transaction as relevant data changes.
- Use retries with backoff and jitter.
- Make external writes idempotent.
- Record terminal failures and expose replay controls.
- Keep an auditable distinction between received, processed, analyzed, and delivered.

For semantic matching, begin with existing infrastructure or PostgreSQL-based storage. A separate vector platform should follow measured need.

### AI processing

Use this sequence:

**Normalize → separate customer/internal content → extract observations → verify evidence → suggest opportunity links → calculate counts → generate narrative.**

Treat source text as untrusted data. It must not authorize actions.

Cache extraction by content revision, prompt version, and model version. Keep manual overrides separately. Do not silently reassign opportunities when models change.

Platform-funded AI requires a new bounded resolver path: the baseline intentionally removed its system-key fallback. Maintain a clear customer-BYOK option.

### Hosted privacy and access

- Encrypt integration credentials and plan key rotation.
- Keep tokens and customer content out of operational logs.
- Audit browser session storage before launch.
- If moving to HttpOnly cookies, add appropriate CSRF protection and WebSocket authentication.
- Inventory export/delete behavior across derived evidence, embeddings, reports, and jobs.
- Explain backup retention and deletion timing.
- Separate hosted operational metrics from customer feedback content.

Keep self-hosted telemetry behavior consistent with the existing product promise. The managed service can collect disclosed operational metrics without silently changing self-hosted behavior.

### Verification

The inspected CI covers backend, worker, and frontend tests/linting. Extend it to relevant analysis-engine tests and production builds.

Add real PostgreSQL/Redis integration checks where transaction visibility and queue behavior matter. Do not rely exclusively on mocks for these paths. [Current CI](<https://github.com/haqaliz/rereflect/blob/93359c4a2bf20310f98e42d570de50a1586812d8/.github/workflows/ci.yml>)

## 10\. Pricing, economics, and acquisition

### Proposed pricing hypotheses

| Offer | Proposed price | Initial boundaries |
|---|---:|---|
| Self-hosted edition | Free | Existing portable software; customer operates it. |
| Managed Starter | $59/workspace/month | Team up to 10 people, three sources, 1,000 analyzed conversations/month, weekly brief and Linear workflow. |
| Managed Growth | $99/workspace/month | Five sources, 3,000 analyzed conversations/month, more frequent briefs and higher usage allowance. |

These remain hypotheses after M0 public pricing research; validate them through concrete M2 offers and successful recurring payments before making them permanent. See the pricing research and usage contract in `docs/m0/RESEARCH_REPORT.md`.

Define an analyzed conversation clearly. Retries, duplicate deliveries, and provider revisions must not unexpectedly consume additional allowance. Display usage and warn before limits. Start with explicit upgrades rather than surprise overage charges.

A 30-day activation allowance of up to 1,000 historical conversations per workspace can support migration. Further imports should be quoted or approved explicitly.

### $1,000 MRR scenarios

| Customer mix | MRR |
|---|---:|
| 17 Starter customers | $1,003 |
| 11 Growth customers | $1,089 |
| 10 Starter + 5 Growth | $1,085 |

These are arithmetic scenarios, not acquisition forecasts.

### Illustrative Starter economics

At 17 Starter customers:

- Revenue: **$1,003/month**.
- Shared hosting target: **$100/month**.
- AI budget ceiling: **$85/month**.
- Delivery/monitoring allowance: **$25/month**.
- Payment-processing allowance: **$35/month**.
- Remaining contribution: approximately **$758/month**, before founder labor and other expenses.

These are planning allowances, not verified vendor quotations. Instrument actual costs from the first pilot. The Growth plan requires its own cost model at the larger allowance.

At $59, buyers must receive useful automation without recurring concierge work. Human-reviewed briefs are appropriate during validation, but should not become an unpriced permanent service.

### Founder-led acquisition

A first working funnel hypothesis:

**200 qualified companies → 40 conversations → 25 pilots → 17 subscribers.**

This implies approximately 68% pilot conversion, which is demanding. Measure the actual funnel; if conversion is lower, revise the acquisition target or offer.

Weekly actions:

1. Research approximately 20 relevant companies.
2. Approach founders through appropriate existing relationships and public channels.
3. Offer to review a recent feedback batch with their permission.
4. Show one useful finding and its original evidence.
5. Invite the team to a paid recurring pilot.
6. Record the objection and next step.

Do not claim YC affiliation. Discuss the buyer’s actual workflow and pain.

Useful acquisition assets:

- A sample weekly brief.
- A short capture-to-decision demonstration.
- A comparison with the buyer’s spreadsheet or Linear workflow.
- A transparent pricing page.
- Permissioned case studies.

### Metrics

Track:

- First useful result time.
- Import completion and failure rate.
- Account-mapping coverage.
- Proposed evidence-link acceptance.
- Weekly meaningful review.
- Opportunities selected or deliberately dismissed.
- Follow-ups completed.
- Paid conversion and second-month retention.
- Recurring revenue, cost per workspace, and support time.

A useful primary product metric is:

> Workspaces making at least one evidence-backed product decision per week.

Define a decision as a recorded review with an action or rationale; an email open alone does not qualify.

## 11\. Repository map and `directory.md` requirements

**Status on 5 October 2026:** directory guides and their indexes have been created from the local clone. See `docs/m0/VERIFICATION.md` for coverage checks and limits; summaries describe declarations/docs, not executed runtime behavior.

Maintain `directory.md` in the repository root and each source/documentation directory. The baseline has **542 tracked directories**, requiring 543 baseline guides including the root. M0 also introduces `docs/m0/`, `docs/m0/datasets/` and `docs/m0/datasets/banking77/`, requiring three additional guides (546 guides total). Exclude `.git`, installed dependencies, virtual environments, and generated build output. The complete tracked-file inventory is in `docs/DIRECTORY_FILE_INDEX.md`; guide links are in `docs/DIRECTORY_GUIDE_INDEX.md`.

### Required contents of each guide

Keep each guide concise, normally 150–400 words:

- Directory purpose and runtime relevance.
- Immediate files and child directories.
- Key entry points and files to read first.
- Inputs, outputs, and dependencies.
- Relevant models, routes, events, or contracts.
- Tenant/authentication requirements.
- Cross-service mirrors that must stay aligned.
- Appropriate verification.
- Known limitations and historical material.
- Audited revision and last update.

Do not describe README-only scaffolding as implemented behavior. For planning directories, distinguish PRD intent from current implementation. For assets, summarize their purpose and usage.

Add a root index linking every guide. Update affected guides with implementation changes. Guides accelerate navigation; agents should still read the files they edit.

### Implementation navigation map

| Directory | Responsibility and implementation guidance |
|---|---|
| Repository root | Workspace configuration, Compose deployment, environment examples, source license, and tracking records. Start here for deployment assumptions. |
| `.claude/skills/` | Existing development workflows. Separate agent instructions from product implementation evidence. |
| `.github/workflows/` | CI. Extend verification for production builds, analysis, and managed-service integration paths. |
| `.github/ISSUE_TEMPLATE/` | Contributor reporting templates. |
| `docs/` | Maintained architecture, API, development, and self-hosting references. |
| `docs/archive/prd/` | Historical requirements; stale plan and status assumptions must be labeled. |
| `docs/planning/` | Feature-specific PRDs, specs, plans, and implementation records. Summarize each feature and nested aspect separately. |
| `docs/assets/` | Logos and screenshots; refresh when the managed experience changes. |
| `packages/ui/src/components/` | Shared UI elements. Current contents are limited; avoid assuming it owns every frontend component. |
| `packages/ui/src/styles/` | Shared styling. |
| `scripts/` | Documentation checks and prospecting utilities. |
| `services/backend-api/src/api/` | App registration, authentication, and dependencies. |
| `services/backend-api/src/api/routes/` | Product endpoints. Add account/opportunity contracts and hosted billing here. |
| `services/backend-api/src/api/public/` | Scoped public API authentication. Preserve API-key behavior during browser-auth changes. |
| `services/backend-api/src/models/` | Canonical ORM models. Add stable identity, evidence, opportunity, and job records. |
| `services/backend-api/src/schemas/` and `src/api/schemas/` | API contracts and validation. Document the existing split. |
| `services/backend-api/src/services/` | Health, workflow, outreach, integration, and domain logic. |
| `services/backend-api/src/services/copilot/` | Intent, SQL, formatting, templates, and action proposals. Preserve human-confirmed action boundaries. |
| `services/backend-api/src/services/embeddings/` | Embedding abstractions and providers. Tenant-scope new retrieval. |
| `services/backend-api/src/background/` | Queue client and background deletion behavior. |
| `services/backend-api/src/config/` | Plan, automation, template, and readiness configuration. Legacy prices are not the new pricing specification. |
| `services/backend-api/src/database/` | Engine and session configuration. Review connection lifecycle and timeout enforcement. |
| `services/backend-api/src/utils/` | Credential encryption, BYOK, and SSRF utilities. |
| `services/backend-api/alembic/versions/` | Schema history. Preserve a single head and additive migration sequencing. |
| `services/backend-api/scripts/` | Backfills and evaluation tools. Separate synthetic evaluation from real validation. |
| `services/backend-api/eval_results/` | Committed evaluation artifacts and their limitations. |
| Backend template directories | Transactional email definitions and HTML. Preserve render and recipient contracts. |
| `services/backend-api/tests/` | API/domain verification and fixtures. Add tenant, transaction, billing, and evidence tests. |
| `services/worker-service/src/` | Worker configuration, database access, Celery registration, and shared helpers. |
| `services/worker-service/src/adapters/` | Provider event normalization. |
| `services/worker-service/src/clients/` | External API clients. Keep rate limits and retries observable. |
| `services/worker-service/src/llm/` | Provider resolution, fallbacks, and usage logging. Add bounded managed-key behavior deliberately. |
| `services/worker-service/src/models/` | Worker ORM mirrors. Maintain schema parity. |
| `services/worker-service/src/services/` | Automation, calibration, prediction, reports, outreach, and scoring. |
| `services/worker-service/src/tasks/` | Analysis, synchronization, reports, and scheduled jobs. Add durable dispatch and recovery. |
| `services/worker-service/tests/` | Job, client, mirror, and queue-path verification. |
| `services/analysis-engine/src/analyzer/` | Core sentiment, categorization, and extraction. |
| Analyzer classifier subdirectories | Training, features, evaluation, and prediction. Preserve train/serve parity and historical feature semantics. |
| Analyzer sentiment-provider subdirectories | Local-provider selection and optional model loading. |
| `services/analysis-engine/src/api/` | Standalone analysis API. Verify its actual deployment relevance before modifying it. |
| Analysis examples/tests | Example data and model behavior checks. |
| `services/frontend-web/app/` | Authentication, public sharing, unsubscribe, and application routes. |
| `app/(dashboard)/` and nested routes | Protected pages. Introduce the simplified founder experience here. |
| `services/frontend-web/components/` | Navigation and feature components. Summarize nested feature directories individually. |
| `services/frontend-web/contexts/` | Auth, theme, realtime, and page state. |
| `services/frontend-web/hooks/` | Roles, realtime, and copilot connections. |
| `services/frontend-web/lib/api/` | Typed API clients. Extend account, opportunity, brief, and billing contracts. |
| Frontend constants/utilities | Shared status and display semantics; keep backend meanings aligned. |
| Frontend tests/public assets | UI verification, images, and theme initialization. |
| `services/landing-web/` | Separate marketing application. Update positioning, offer, and conversion flow. |
| Landing app/components/lib | Marketing pages, integrations, blog data, and motion. Source content does not prove live deployment. |
| Landing tests/public assets | Marketing verification and discoverability assets. |
| `services/integration-service/` | README-only material in the audited tree. Actual connector implementation is elsewhere. |

### Initial agent work packages

After M0, split implementation into reviewable packages:

1. Churn semantics and disabled unsafe automation.
2. Copilot query isolation and cancellation.
3. Durable job dispatch and recovery.
4. Managed subscription lifecycle.
5. First-source onboarding.
6. Stable account identity.
7. Opportunity/evidence model.
8. Weekly brief.
9. Linear delivery and release follow-up.

Each package should specify affected directories, migration impact, backward compatibility, acceptance checks, and updated guides.

## 12\. Scope boundaries before $1,000 MRR

Defer these unless paid demand changes the priority:

- Additional enterprise CRM integrations.
- A full public voting and roadmap platform.
- Custom model fine-tuning.
- Autonomous roadmap decisions.
- Automatic customer outreach without approval.
- Native call recording and transcription infrastructure.
- Broad Reddit/X ingestion.
- Mobile apps.
- Industry benchmarks without suitable consented data.
- A new microservice or infrastructure rewrite.
- Advanced predictive churn claims.
- A new MCP server solely for marketing differentiation.

After retention is established, evaluate PostHog survey/usage ingestion, transcript uploads, account-specific blockers, and agent-readable evidence exports. PostHog already provides survey collection infrastructure that may be useful to integrate. [PostHog survey documentation](<https://posthog.com/docs/surveys>)

## 13\. Definition of the first successful product

The first successful version lets a founder:

- Connect a real feedback source quickly.
- Inspect trustworthy evidence.
- See which customer accounts share a problem.
- Make and record a product decision.
- Link selected work to delivery.
- Notify customers after release.
- Receive a useful brief the following week.

The commercial milestone is **$1,000 MRR with retained, regularly active customers**. Feature count, AI demonstrations, and repository activity do not establish that outcome.

