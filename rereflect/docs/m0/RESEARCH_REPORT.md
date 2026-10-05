# FeedSignal M0: public evidence and pricing decision

Research date: **6 October 2026**. Upstream: [haqaliz/rereflect](https://github.com/haqaliz/rereflect). Owner: [Akgithub2028](https://github.com/Akgithub2028).

**Decision:** proceed to M1 reliability and ownership work, then a bounded M2 pilot. Test **$59 and $99 per workspace per month** for a managed weekly decision workflow. Public evidence supports a problem hypothesis and competitive price range; it does not establish demand for FeedSignal.

The owner has replaced interview-led M0 with public dataset and pricing research. M0 is complete within that revised scope. Real usage, commitments, and purchases remain future commercial checks. [Status and scope change](STATUS.md), [datasets](PUBLIC_DATASETS.md), [implementation plan](../IMPLEMENTATION_PLAN.md).

## Evidence quality and research method

Reviewed official pricing/product pages, original dataset repositories/cards, and directly accessible Reddit discussions. Searches covered fragmented SaaS feedback, manual spreadsheets, Canny costs, build-versus-buy, and Linear customer requests. Selected both supporting and opposing evidence; this is a purposive qualitative sample, not a representative survey or a conversion forecast.

Official prices describe offers, not transaction volume. Vendor testimonials are curated. Forum authors' employment, spending, and team size are self-reported and unverified; comments may promote competing products. Repeated claims from the same thread are one source. No X claim is used because sufficiently verifiable evidence was unavailable. No individuals were contacted.

## Public pain signals and implementation consequences

| Evidence | What it supports | Consequence for FeedSignal |
|---|---|---|
| An author describing an eight-person B2B SaaS reports weekly consolidation across support, CRM, notes, email, and Slack, losing customer and urgency context. [Discussion](https://www.reddit.com/r/SaaSSales/comments/1nfg3cs/were_drowning_in_customer_feedback_across_12/) | A close-to-target account of collection overhead; identity is unverified. | Preserve source links, timestamps, account mapping and exact excerpts through ingestion and briefs; offer a useful first import rather than another manual board. |
| A small-team author reports avoiding a steep feedback-tool bill by building a replacement, then experiencing notification and maintenance gaps. [Discussion](https://www.reddit.com/r/SaaS/comments/1rgpfy7/the_build_versus_buy_math_for_saas_has_changed/) | Cost sensitivity and a credible DIY substitute; not an invoice or a FeedSignal purchase intent. | Predictable workspace pricing, transparent limits, exportability, recovery and dependable customer follow-through must justify the subscription. |
| A Linear user describes requests ranging from small changes to whole projects and wants discovery before delivery. [Discussion](https://www.reddit.com/r/Linear/comments/1m31wxj/how_do_you_work_with_customer_requests/) | Request grouping and decision stages matter independently of issue creation. | Persist opportunities, split multi-issue messages, allow merge/split review, and create issues only after human approval. |
| A founder describes multi-product consolidation and cost concerns while recruiting testers for their own feedback tool. [Discussion](https://www.reddit.com/r/Solopreneur/comments/1r38dag/launched_2_saas_in_2026_feedback_management/) | Weak supporting evidence: also a competitor advertisement. | Retain multi-tenant foundations, but defer a special multi-product offer until usage demands it. Do not count this as a buyer commitment. |
| Feedback-tool discussion describes friction from requiring an account to submit feedback. [Hacker News](https://news.ycombinator.com/item?id=43379395) | A qualitative acquisition obstacle, not a market prevalence estimate. | Start with existing conversations and email/CSV/Slack capture; avoid making customers adopt a new portal to create value. |

**Our inferred priority:** (1) reduce weekly collection and triage work, (2) retain evidence and account context when choosing priorities, (3) reliably link decisions to delivery and follow-up. Confidence is higher that these problems exist than that enough 2–10-person teams will pay for this particular solution. Advanced predictive churn and a broad autonomous agent remain lower priority.

## Verified published pricing signals

Prices below are USD, as displayed on 6 October 2026. Annual effective monthly prices are labeled explicitly; taxes, add-ons, promotions, and actual checkout totals are not included.

| Alternative | Published offer / charging unit | Interpretation |
|---|---|---|
| [Canny](https://canny.io/pricing) | Free: 25 tracked users. Pro starts at $79/month **billed yearly**, 100+ tracked users. | Direct competitor; customer participation can affect cost. |
| [Savio](https://www.savio.io/pricing/) | Essential $39, Professional $79, Business $249/month **paid annually**; one paid user included, extra paid users $23/$39/$49. | A close feedback-workflow benchmark with seat costs. |
| [Featurebase](https://www.featurebase.app/pricing) | Growth $29 and Professional $59/**seat**/month, billed yearly; $0.49/AI resolution. Startup offer advertises 86% off for companies under two years and under six employees. | Bundled support and feedback; startup discounts weaken a simple cheaper-tool pitch. |
| [UserJot](https://userjot.com/pricing) | Free boards; Starter $29/month, Professional $59/month, unlimited users/posts. Page does not label these as annual commitments. | Flat pricing already exists; a board is not enough to distinguish FeedSignal. |
| [Linear Customer Requests](https://linear.app/docs/customer-requests) | Available on all current plans; integration availability varies by plan. | Already-purchased workflow substitute; avoid duplicating its account/request views. |
| [PostHog](https://posthog.com/pricing) | Surveys include 1,500 responses free per month. | Feedback collection alone competes with a generous free allowance. |

Machine-readable observations: [pricing signals CSV](pricing_signals.csv). They are observations of public offers, not an estimated willingness-to-pay distribution.

## Price hypothesis and delivery contract

Retain the plan's proposed $59 Starter and $99 Growth workspace offers. Include up to ten teammates, no charge per feedback submitter, and published source/conversation limits. Annual discounts can wait until monthly retention is known. A 14-day trial is an implementation proposal, not an available service.

Starter: three connected source instances, 1,000 analyzed conversations per month, one weekly cited brief, opportunity review, Linear handoff, approved release follow-up, and export/delete. Growth: five source instances, 3,000 conversations and more frequent briefs. All existing connector implementations remain available within the chosen source limit; no connector is removed or claimed operational before reconnection.

Define a billable conversation as a stable `(tenant, source_instance, provider_conversation_id)` thread, not an individual message, observation, retry or webhook event. Count it once in a billing period; charge no extra unit for corrections/revisions that period. Bound attachment/text processing separately and show usage before processing expensive backfills. Count CSV rows as distinct conversations only when no stable thread ID is supplied; preview that consequence. Same-ID transport replays never add demand or billing counts. Unknown cross-channel duplicates stay reviewable rather than automatically charging or merging on an email guess.

Implement entitlements server-side; persist billing-period boundaries, import batch/source IDs, revision history and a durable usage ledger. Cache analysis by content/model/prompt version. Keep historical imports under the explicit allowance in the main plan. Notify before limits; allow an explicit upgrade or pause further paid analysis, with export access preserved. Do not create surprise usage invoices.

**Illustrative value threshold, not measured ROI:** at an assumed founder-hour value of $50, $59 requires about 71 minutes saved monthly; $99 about 119 minutes. If it saves only 15 minutes per month, these prices are hard to defend. Show original evidence and decisions affected, not an unsupported claim of revenue saved or churn prevented.

## Path to $1,000 MRR and constraints

| Retained paying mix | Monthly subscription revenue |
|---|---:|
| 17 Starter | $1,003 |
| 11 Growth | $1,089 |
| 10 Starter + 5 Growth | $1,085 |

These are arithmetic scenarios, with no asserted conversion probability. For 17 retained buyers, illustrative qualified-pilot conversion of 20%, 40% or 60% requires 85, 43 or 29 pilots respectively, before churn. This sensitivity replaces treating a single optimistic funnel as evidence.

At a hypothetical 5% monthly logo churn, 17 accounts lose 0.85 accounts/month on average; roughly one replacement per month merely sustains the level. At $59, permanent manual curation can erase margin. Track provider tokens, queue work, storage, delivery, processing fees, refunds and founder support minutes. The main plan's cost allowances remain unverified targets, not vendor quotes. Price only scales if brief generation and ingestion become dependable without weekly concierge labor.

## Commercial validation after M0, without interviews

Do not require a scheduled interview. During M2, give qualified teams a real import and reviewed brief through owner-authorized onboarding. Record permissioned artifact access and in-product behavior instead of claiming that public commenters are our customers.

1. Recruit five qualified teams through channels the owner authorizes. No outreach is sent by this research task.
2. Record actual time to the first useful result, imported accepted/failed counts, and an explicit useful/not-useful response or a saved decision. A page view alone is insufficient.
3. Obtain three dated agreements to continue for another weekly cycle; verify whether they return or request the next brief.
4. Present a concrete $59 or $99 offer, with exact scope. Record at least two explicit price-specific acceptances by decision makers. Separate acceptance, checkout start, recurring subscription and successful settled payment.
5. Keep M2's three-paid-pilot target; do not expand M3–M6 scope if teams do not return or will not accept the price. Diagnose the offer from asynchronous responses/behavior; interviews are optional.

With such a small sample, sequential offers reveal objections but are not a statistically powered A/B test. Failed payments, refundable deposits, waitlist signups, likes and compliments are not retained MRR. Existing research has **zero FeedSignal commitments and zero product-specific payment evidence**; both remain in [the ledger](../../UNANSWERED_SECRETS.md).

## Handoff to implementation

M1 addresses the audited correctness, tenant-isolation, dispatch, owner-default and deployment risks first. M2 uses the public dataset for development only, with conspicuously labeled demos, and tests actual onboarding when permitted. M3–M6 implement account context, opportunities, brief quality and follow-up only within the commercial gates above. Recheck competitor pricing immediately before publishing an offer; this report preserves a dated research snapshot.
