# FeedSignal complete directory file inventory

Baseline `93359c4a2bf20310f98e42d570de50a1586812d8` plus M0 preparation files; updated 2026-10-06. Generated `directory.md` files are indexed separately. This preserves complete filenames while individual guides prioritize entry points.

## `.`

[Directory guide](<../directory.md>)

- [.dockerignore](<../.dockerignore>) — Static/configuration artifact; inspect its consumer.
- [.env.example](<../.env.example>) — Static/configuration artifact; inspect its consumer.
- [.env.prod.example](<../.env.prod.example>) — Static/configuration artifact; inspect its consumer.
- [.gitignore](<../.gitignore>) — Static/configuration artifact; inspect its consumer.
- [.worktreeinclude](<../.worktreeinclude>) — Static/configuration artifact; inspect its consumer.
- [AI-TRACKING.md](<../AI-TRACKING.md>) — AI Feature Tracking & 1-Year Roadmap: - [x] SQL query generation with 3-join max, 5s timeout, no subqueries, row limits by plan - [x] Result formatting: tables, charts (Recharts), deep links, markdown
- [BLOG-TRACKING.md](<../BLOG-TRACKING.md>) — Blog Content Tracking & Roadmap: Each "Rereflect vs X" comparison post should follow this structure: After publishing each post, distribute through these channels:
- [CHANGELOG.md](<../CHANGELOG.md>) — Changelog: All notable changes to Rereflect (the open-source, self-hosted edition) are documented here. Every feature is unlocked; the app runs on your own infrastructure with your own (or a local) LLM key.
- [CLAUDE.md](<../CLAUDE.md>) — Rereflect - Customer Feedback Analyzer: AI-powered customer feedback analysis platform for SaaS businesses. The automations engine exists **twice**, on purpose, and the two must stay in agreement:
- [CONTRIBUTING.md](<../CONTRIBUTING.md>) — Contributing to Rereflect: Thanks for your interest in contributing! Rereflect is open source under the MIT License, and we welcome bug reports, features, docs, and tests.
- [DEV-TRACKING.md](<../DEV-TRACKING.md>) — Development Tracking: Shipped as **v1.0.0** (2026-07-26) — free, open-source, self-hosted, MIT, BYOK. Rereflect pivoted to **free, open-source, self-hosted (MIT, BYOK)**. The SaaS/MRR framing and plan-gating below are **stale** —…
- [LICENSE](<../LICENSE>) — Static/configuration artifact; inspect its consumer.
- [NOTICE](<../NOTICE>) — Static/configuration artifact; inspect its consumer.
- [OUTREACH-TRACKING.md](<../OUTREACH-TRACKING.md>) — Outreach Tracking: With only 1 hour/week, every minute counts. Here's the optimized routine: - Search LinkedIn: "Head of Product" OR "Founder" + "SaaS" + seed/series A
- [OWNER_CONFIG.md](<../OWNER_CONFIG.md>) — FeedSignal owner configuration: Product name is a working choice, not proof of domain or legal availability. Owner legal name: `UNANSWERED_OWNER_LEGAL_NAME`. Owned repository URL: `UNANSWERED_GITHUB_REPOSITORY_URL`; do not assume…
- [PROSPECT-LIST.md](<../PROSPECT-LIST.md>) — Prospect List — Week 4 Outreach
- [QUICK_START.sh](<../QUICK_START.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [README.md](<../README.md>) — FeedSignal: Owner/support/admin: `aayaannkausar@gmail.com` · Akgithub2028 on GitHub. This is the preparation-stage fork of Rereflect. No FeedSignal cloud deployment or live provider connection is claimed. All existing integration…
- [SALES-TRACKING.md](<../SALES-TRACKING.md>) — Sales & Growth Tracking: The product is feature-rich (AI analysis, copilot, response suggestions, webhooks, integrations). The bottleneck is traffic and signups, not features. This phase focuses on converting awareness into…
- [TRACKING.md](<../TRACKING.md>) — Rereflect — Development Tracking Notes: `services/worker-service/src/tasks/churn_calibration.py` defines `refit_all_orgs`, `refit_global_calibration`, and `purge_old_calibration_models` as plain Python
- [UNANSWERED_SECRETS.md](<../UNANSWERED_SECRETS.md>) — FeedSignal — unanswered configuration and credentials: The working name is selected for this repository. Domain, trademark, and account-name availability are not established. Do not invent an owned domain or a created repository.…
- [docker-compose.prod.yml](<../docker-compose.prod.yml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [docker-compose.yml](<../docker-compose.yml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [lighthouse-report.json](<../lighthouse-report.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [package.json](<../package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [pnpm-lock.yaml](<../pnpm-lock.yaml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [pnpm-workspace.yaml](<../pnpm-workspace.yaml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [prospects.json](<../prospects.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [sample_feedback_diverse.csv](<../sample_feedback_diverse.csv>) — Static/configuration artifact; inspect its consumer.
- [start-all.sh](<../start-all.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [stop-all.sh](<../stop-all.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.

## `.claude`

[Directory guide](<../.claude/directory.md>)

- [settings.json](<../.claude/settings.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## `.claude/skills`

[Directory guide](<../.claude/skills/directory.md>)

- [feature-implementation.md](<../.claude/skills/feature-implementation.md>) — Feature Implementation Skill: Use this skill when implementing specific features from the roadmap.
- [saas-development.md](<../.claude/skills/saas-development.md>) — SaaS Development Skill: Use this skill when working on SaaS-specific features for the Customer Feedback Analyzer platform. This project is transforming from an open-source tool into a professional SaaS platform. Key documents:

## `.claude/skills/prd-generator`

[Directory guide](<../.claude/skills/prd-generator/directory.md>)

- [SKILL.md](<../.claude/skills/prd-generator/SKILL.md>) — PRD Generator: description: Generate, critique, and refine PRDs, spec files, and roadmaps for initiative-level product planning. Intended for PMs and stakeholders. Only activate when explicitly requested. Triggers on…

## `.claude/skills/prd-interview`

[Directory guide](<../.claude/skills/prd-interview/directory.md>)

- [SKILL.md](<../.claude/skills/prd-interview/SKILL.md>) — PRD Interview: description: Conduct a collaborative product requirements interview between PM and engineering. Use when turning a product brief or feature idea into a structured PRD and aspect-level specs through guided discovery…

## `.claude/skills/rereflect-begin`

[Directory guide](<../.claude/skills/rereflect-begin/directory.md>)

- [SKILL.md](<../.claude/skills/rereflect-begin/SKILL.md>) — Rereflect Begin (Full Track): description: Use when starting work on a Rereflect GitHub issue (bug/feat/task/chore) from its number, or on a freeform task, and you need stakeholder proposals (technical + non-technical PDFs with…

## `.claude/skills/rereflect-begin-fast`

[Directory guide](<../.claude/skills/rereflect-begin-fast/directory.md>)

- [SKILL.md](<../.claude/skills/rereflect-begin-fast/SKILL.md>) — Rereflect Begin (Fast Track): description: Use when starting work on a Rereflect GitHub issue (bug/feat/task/chore) from its number, or on a freeform task, and you want the fast path straight to an implementation plan. Triggers…

## `.claude/skills/rereflect-begin-fast/references`

[Directory guide](<../.claude/skills/rereflect-begin-fast/references/directory.md>)

- [gather-context.md](<../.claude/skills/rereflect-begin-fast/references/gather-context.md>) — Gathering issue context with `gh`: Goal: dump the GitHub issue, its referenced issues, and comments into A human-readable view with comments inline (handy for the dump):

## `.claude/skills/rereflect-begin/references`

[Directory guide](<../.claude/skills/rereflect-begin/references/directory.md>)

- [proposals.md](<../.claude/skills/rereflect-begin/references/proposals.md>) — Phase A — Diagrams & proposal PDFs: Runs after the PRD approval gate. Everything is written inside the worktree under Use the `excalidraw` skill. Decide how many diagrams the feature actually needs —

## `.claude/skills/rereflect-end`

[Directory guide](<../.claude/skills/rereflect-end/directory.md>)

- [SKILL.md](<../.claude/skills/rereflect-end/SKILL.md>) — Rereflect End (Full Track): description: Use when finishing local work on a Rereflect GitHub issue after the PR is merged and you also need a completion report on Desktop. Triggers on "rereflect-end", "re", "re bug 42", "re feat…

## `.claude/skills/rereflect-end-fast`

[Directory guide](<../.claude/skills/rereflect-end-fast/directory.md>)

- [SKILL.md](<../.claude/skills/rereflect-end-fast/SKILL.md>) — Rereflect End (Fast Track): description: Use when finishing local work on a Rereflect GitHub issue after the PR is merged and you want to clean up without generating a completion report. Triggers on "rereflect-end-fast", "ref",…

## `.claude/skills/rereflect-report`

[Directory guide](<../.claude/skills/rereflect-report/directory.md>)

- [SKILL.md](<../.claude/skills/rereflect-report/SKILL.md>) — Rereflect Work Item Completion Note: description: Use when a Rereflect GitHub issue (bug, task, chore, or feature) is done and you want a brief, friendly, non-technical completion note saved on Desktop to share with the team. A…

## `.claude/skills/rereflect-worktrees`

[Directory guide](<../.claude/skills/rereflect-worktrees/directory.md>)

- [SKILL.md](<../.claude/skills/rereflect-worktrees/SKILL.md>) — Rereflect Worktree Workflow: description: Isolate parallel work in the Rereflect monorepo using the Claude Code worktree layout. Use when starting work on a new bug/feature that should not collide with another running Claude…

## `.claude/skills/tech-plan`

[Directory guide](<../.claude/skills/tech-plan/directory.md>)

- [SKILL.md](<../.claude/skills/tech-plan/SKILL.md>) — Handoff Contract: description: Create a phased technical implementation plan from planning artifacts in docs/planning (PRD + aspect spec) for the Rereflect monorepo. Use after prd-interview when the user is ready to execute a…

## `.github`

[Directory guide](<../.github/directory.md>)

- [FUNDING.yml](<../.github/FUNDING.yml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [pull_request_template.md](<../.github/pull_request_template.md>) — Summary

## `.github/ISSUE_TEMPLATE`

[Directory guide](<../.github/ISSUE_TEMPLATE/directory.md>)

- [bug_report.md](<../.github/ISSUE_TEMPLATE/bug_report.md>) — Where: (e.g. Feedbacks page, backend `/api/v1/feedback`, Celery worker) If applicable, add screenshots, a short video, or relevant log output.
- [feature_request.md](<../.github/ISSUE_TEMPLATE/feature_request.md>) — Problem / motivation: What problem are you trying to solve? What's the use case? Any alternative approaches or workarounds you've thought about.

## `.github/workflows`

[Directory guide](<../.github/workflows/directory.md>)

- [ci.yml](<../.github/workflows/ci.yml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## `docs`

[Directory guide](<directory.md>)

- [API.md](<API.md>) — API Reference: Rereflect exposes a REST API under `/api/v1`. When the backend is running, the full interactive OpenAPI/Swagger docs are at **http://localhost:8000/docs** — this page is a
- [ARCHITECTURE.md](<ARCHITECTURE.md>) — Architecture: A Next.js frontend talks to a FastAPI backend over REST. Long-running analysis is offloaded to a Celery worker (Redis broker), which uses the analysis engine — VADER /
- [DEVELOPMENT.md](<DEVELOPMENT.md>) — Development: How to run Rereflect from source for local development. For containerized deployment instead, see SELF_HOSTING.md.
- [DIRECTORY_FILE_INDEX.md](<DIRECTORY_FILE_INDEX.md>) — FeedSignal complete directory file inventory: Baseline `93359c4a2bf20310f98e42d570de50a1586812d8` plus M0 preparation files; updated 2026-10-06. Generated `directory.md` files are indexed separately. This preserves complete…
- [DIRECTORY_GUIDE_INDEX.md](<DIRECTORY_GUIDE_INDEX.md>) — FeedSignal directory guide index: Baseline `93359c4a2bf20310f98e42d570de50a1586812d8`; updated 2026-10-06. **546 guides**: repository root, 542 baseline tracked directories, plus three M0 research/data directories.…
- [IMPLEMENTATION_PLAN.md](<IMPLEMENTATION_PLAN.md>) — FeedSignal: implementation plan toward $1,000 MRR: FeedSignal uses the known support/admin email and GitHub identity above. Domains are undecided (`UNANSWERED_MARKETING_ORIGIN`, `UNANSWERED_APP_ORIGIN`, `UNANSWERED_API_ORIGIN`).…
- [OWNERSHIP_AND_INTEGRATION_AUDIT.md](<OWNERSHIP_AND_INTEGRATION_AUDIT.md>) — Deployment, ownership, and integration migration audit: Audit date: 2026-10-05. Local checkout inspected: `93359c4a2bf20310f98e42d570de50a1586812d8`. Original repository: haqaliz/rereflect.
- [SELF_HOSTING.md](<SELF_HOSTING.md>) — Self-Hosting Rereflect: Rereflect is open source (MIT) and designed to run entirely on your own infrastructure. **All features are unlocked** on a self-hosted instance — there are

## `docs/archive`

[Directory guide](<archive/directory.md>)

No immediate baseline/preparation files.

## `docs/archive/prd`

[Directory guide](<archive/prd/directory.md>)

- [PRD-ADVANCED-CHURN-PREDICTION.md](<archive/prd/PRD-ADVANCED-CHURN-PREDICTION.md>) — PRD: Advanced Churn Prediction (M4.1): Turn Rereflect's existing 9-factor heuristic churn score into a **calibrated 30-day churn probability** with a confidence interval, time-to-churn timeline, cohort analytics, and reusable…
- [PRD-AI-COPILOT.md](<archive/prd/PRD-AI-COPILOT.md>) — PRD: AI Copilot — Command Bar & Conversations (M2.2): The AI Copilot gives users a natural-language interface to query, analyze, and understand their feedback data. It consists of two connected surfaces: The Cmd+K modal acts as a…
- [PRD-AI-RESPONSE-SUGGESTIONS.md](<archive/prd/PRD-AI-RESPONSE-SUGGESTIONS.md>) — PRD: AI Response Suggestions (M2.3): When a team member reviews a feedback item, they often need to respond to the customer — acknowledge a bug, thank them for a feature suggestion, or reach out proactively to an at-risk…
- [PRD-AI-WORKFLOW-AUTOMATION.md](<archive/prd/PRD-AI-WORKFLOW-AUTOMATION.md>) — PRD: AI Workflow Automation (M4.4): Teams using Rereflect identify churn risks, critical bugs, and urgent feedback — but then must manually assign, escalate, and respond to each one. A CS lead seeing a customer's health score…
- [PRD-CHURN-PREDICTION-ACCURACY.md](<archive/prd/PRD-CHURN-PREDICTION-ACCURACY.md>) — PRD: Churn Prediction Accuracy: Make churn predictions transparent, trustworthy, and measurable. Today, users see a single churn risk score (0-100) with no explanation of why it's high or low, no indication of how reliable it is,…
- [PRD-CUSTOM-WEBHOOKS-AND-TECH-DEBT.md](<archive/prd/PRD-CUSTOM-WEBHOOKS-AND-TECH-DEBT.md>) — PRD: Custom Webhooks & Technical Debt (M3.1): Rereflect users who want to automate workflows based on feedback events (e.g., post to Discord, trigger a Zapier flow, update an internal dashboard, page oncall) currently have no way…
- [PRD-CUSTOMER-360.md](<archive/prd/PRD-CUSTOMER-360.md>) — PRD: Customer 360 Page: Build a dedicated Customer 360 experience — a `/customers` list page and `/customers/[email]` profile page — that surfaces all existing customer health data in one place. Today, customer health data is…
- [PRD-CUSTOMER-SENTIMENT-ALERTS.md](<archive/prd/PRD-CUSTOMER-SENTIMENT-ALERTS.md>) — PRD: Customer Sentiment Alerts: Proactively alert users when a customer's health score deteriorates. Today, users must manually check the Customer 360 page or dashboard widget to discover at-risk customers. This feature triggers…
- [PRD-DASHBOARD-V2.md](<archive/prd/PRD-DASHBOARD-V2.md>) — PRD: Dashboard V2 — Customizable Analytics Grid: The current dashboard is a single long-scrolling page with ~10 sections that serves all user personas the same way. Key problems: Each persona will be able to configure their own…
- [PRD-GDPR-AITRUST-BLOGENGINE.md](<archive/prd/PRD-GDPR-AITRUST-BLOGENGINE.md>) — PRD: GDPR Compliance, AI Trust, & Blog Engine (M3.8): Users cannot export or delete their personal data from Rereflect. GDPR (and similar regulations) require data portability (Art. 20) and right to erasure (Art. 17). Without…
- [PRD-LOCAL-LLM-CUSTOM-AI-PUBLIC-API.md](<archive/prd/PRD-LOCAL-LLM-CUSTOM-AI-PUBLIC-API.md>) — PRD — Feature Batch: Local LLM · Custom AI · Public API: Three features, built in parallel, each chosen to fit the open-source/self-hosted/BYOK positioning: All additive; one Alembic migration off current head `w2x3y4z5a6b7`.…
- [PRD-MULTI-MODEL-SUPPORT.md](<archive/prd/PRD-MULTI-MODEL-SUPPORT.md>) — PRD: M2.1 — Multi-Model Support: Replace the hardcoded OpenAI integration with a provider-agnostic LLM abstraction layer using the factory method pattern. Support OpenAI, Anthropic, and Google as providers. Enable per-org model…
- [PRD-ON-DEMAND-AI-REPORTS.md](<archive/prd/PRD-ON-DEMAND-AI-REPORTS.md>) — PRD: On-Demand AI Reports (M2.4): Users who want to share feedback insights with stakeholders (executives, board members, investors, CS leads) must manually compile data from the dashboard, export PDFs of individual charts, and…
- [PRD-OSS-SELF-HOSTED-PIVOT.md](<archive/prd/PRD-OSS-SELF-HOSTED-PIVOT.md>) — PRD — Open-Source Self-Hosted Pivot: Rereflect pivots from a hosted multi-tenant SaaS to a **pure open-source, self-hosted product**. We stop operating the paid service, open the source under MIT, and make the codebase clean and…
- [PRD-PREDICTIVE-ANALYTICS.md](<archive/prd/PRD-PREDICTIVE-ANALYTICS.md>) — PRD: Predictive Analytics — Churn Prediction & Customer Health Score: Enhance Rereflect's AI capabilities with two interconnected features: Both features use a **hybrid approach**: algorithmic scoring for real-time updates +…
- [PRD-REALTIME-EVENTS.md](<archive/prd/PRD-REALTIME-EVENTS.md>) — PRD: Real-Time Event System — Replace Polling with WebSocket Push: The Rereflect frontend currently uses **5 independent polling loops**, all at 30-second intervals, to keep data fresh: Replace all 5 polling patterns with a…
- [PRD-TECHNICAL-DEBT.md](<archive/prd/PRD-TECHNICAL-DEBT.md>) — PRD: Technical Debt Resolution: This PRD covers the resolution of three technical debt items identified in DEV-TRACKING.md: Then update `services/backend-api/src/api/routes/feedback.py` (lines 325-337) to use `joinedload` instead…
- [PRD-admin-promo-management.md](<archive/prd/PRD-admin-promo-management.md>) — PRD: Admin Promo Code Management: Creating and managing Stripe promo codes currently requires direct access to the Stripe Dashboard. As a system admin, I need to create, view, and manage promo codes from within the Rereflect app…
- [PRD-promo-code-system.md](<archive/prd/PRD-promo-code-system.md>) — PRD: Promo Code System for Outreach: We're starting LinkedIn outreach to acquire our first 10 signups. Our key incentive is "3 months free Pro plan." Currently, there's no way to: Without this, our outreach DMs have no working…
- [README.md](<archive/prd/README.md>) — Archived PRDs: Historical product requirement documents for features that have **shipped**. They are kept here for provenance — several are cited by name and line number from the per-feature planning

## `docs/assets`

[Directory guide](<assets/directory.md>)

- [logo-white.png](<assets/logo-white.png>) — Static/configuration artifact; inspect its consumer.
- [logo.png](<assets/logo.png>) — Static/configuration artifact; inspect its consumer.

## `docs/assets/screenshots`

[Directory guide](<assets/screenshots/directory.md>)

- [analytics.png](<assets/screenshots/analytics.png>) — Static/configuration artifact; inspect its consumer.
- [churn-risks.png](<assets/screenshots/churn-risks.png>) — Static/configuration artifact; inspect its consumer.
- [dashboard.png](<assets/screenshots/dashboard.png>) — Static/configuration artifact; inspect its consumer.
- [feature-requests.png](<assets/screenshots/feature-requests.png>) — Static/configuration artifact; inspect its consumer.
- [feedback-sources.png](<assets/screenshots/feedback-sources.png>) — Static/configuration artifact; inspect its consumer.
- [feedbacks.png](<assets/screenshots/feedbacks.png>) — Static/configuration artifact; inspect its consumer.
- [pain-points.png](<assets/screenshots/pain-points.png>) — Static/configuration artifact; inspect its consumer.
- [settings-ai.png](<assets/screenshots/settings-ai.png>) — Static/configuration artifact; inspect its consumer.
- [settings-integrations.png](<assets/screenshots/settings-integrations.png>) — Static/configuration artifact; inspect its consumer.
- [settings-notifications.png](<assets/screenshots/settings-notifications.png>) — Static/configuration artifact; inspect its consumer.
- [settings-team.png](<assets/screenshots/settings-team.png>) — Static/configuration artifact; inspect its consumer.
- [settings-workflow.png](<assets/screenshots/settings-workflow.png>) — Static/configuration artifact; inspect its consumer.
- [shared-links.png](<assets/screenshots/shared-links.png>) — Static/configuration artifact; inspect its consumer.
- [urgent-feedbacks.png](<assets/screenshots/urgent-feedbacks.png>) — Static/configuration artifact; inspect its consumer.
- [workflow.png](<assets/screenshots/workflow.png>) — Static/configuration artifact; inspect its consumer.

## `docs/m0`

[Directory guide](<m0/directory.md>)

- [BASELINE_AND_DEPLOYMENT.md](<m0/BASELINE_AND_DEPLOYMENT.md>) — FeedSignal baseline, database, and integration handoff: Source audited locally on 2026-10-05: `93359c4a2bf20310f98e42d570de50a1586812d8`. Upstream: haqaliz/rereflect.
- [FOUNDER_VALIDATION.md](<m0/FOUNDER_VALIDATION.md>) — FeedSignal optional founder validation runbook: Purpose: establish whether 2–10-person B2B SaaS teams repeatedly lose useful product evidence across existing customer channels and will pay for the proposed workflow. Target at…
- [PILOT_AND_EVALUATION.md](<m0/PILOT_AND_EVALUATION.md>) — FeedSignal pilot and evaluation protocol after M0: Updated: 6 October 2026. **M0 uses public research; interviews and private-team exports are no longer completion prerequisites.** Dataset catalogue and research report are the…
- [PUBLIC_DATASETS.md](<m0/PUBLIC_DATASETS.md>) — Public datasets for FeedSignal development: Checked: **6 October 2026**. Upstream application. M0 requires a sourced dataset shortlist and a usable development corpus under the owner's revised research scope. It does not require…
- [RESEARCH_REPORT.md](<m0/RESEARCH_REPORT.md>) — FeedSignal M0: public evidence and pricing decision: Research date: **6 October 2026**. Upstream: haqaliz/rereflect. Owner: Akgithub2028. The owner has replaced interview-led M0 with public dataset and pricing research. M0 is…
- [STATUS.md](<m0/STATUS.md>) — FeedSignal M0 status and handoff: Updated: **2026-10-06**. Baseline: `93359c4a2bf20310f98e42d570de50a1586812d8`. The owner explicitly waived real interviews and requested public datasets and pricing research to complete M0.…
- [VERIFICATION.md](<m0/VERIFICATION.md>) — M0 verification record: Date: **2026-10-06**. Baseline: `93359c4a2bf20310f98e42d570de50a1586812d8`. M0 is complete under the owner's revised **public research and repository preparation** scope. The initial repository preparation…
- [pricing_signals.csv](<m0/pricing_signals.csv>) — Static/configuration artifact; inspect its consumer.

## `docs/m0/datasets`

[Directory guide](<m0/datasets/directory.md>)

No immediate baseline/preparation files.

## `docs/m0/datasets/banking77`

[Directory guide](<m0/datasets/banking77/directory.md>)

- [ATTRIBUTION.md](<m0/datasets/banking77/ATTRIBUTION.md>) — Banking77 attribution: Publisher: PolyAI. Authors: Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson and Ivan Vulić. Paper: Efficient Intent Detection with Dual Sentence Encoders, 2020.
- [LICENSE](<m0/datasets/banking77/LICENSE>) — Static/configuration artifact; inspect its consumer.
- [categories.json](<m0/datasets/banking77/categories.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [quality_report.json](<m0/datasets/banking77/quality_report.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [source_manifest.json](<m0/datasets/banking77/source_manifest.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [test.csv](<m0/datasets/banking77/test.csv>) — Static/configuration artifact; inspect its consumer.
- [train.csv](<m0/datasets/banking77/train.csv>) — Static/configuration artifact; inspect its consumer.

## `docs/planning`

[Directory guide](<planning/directory.md>)

No immediate baseline/preparation files.

## `docs/planning/_card`

[Directory guide](<planning/_card/directory.md>)

- [card.md](<planning/_card/card.md>) — Card: mutation-route-rbac (freeform, no GitHub issue): Add role enforcement to backend mutation routes that currently have none, starting with the churn/playbook loop: `playbooks.py` (5 mutations, 0 role deps), `churn_events.py`,…
- [understanding.md](<planning/_card/understanding.md>) — Understanding: mutation-route-rbac: Backend mutation routes carry no role check, so a `member` can do admin things. 190 in-scope mutation routes under `api/routes/`: 126 role-gated, **64 ungated**. Scope is wider than the

## `docs/planning/ai-drafted-issue-content`

[Directory guide](<planning/ai-drafted-issue-content/directory.md>)

- [prd.md](<planning/ai-drafted-issue-content/prd.md>) — PRD — AI-drafted issue/task content: When a user turns a feedback item into a Jira issue or Asana task via the create-work-item wizard (`feedbacks/[id]/create-issue/page.tsx`), the title/body are pre-seeded verbatim from the raw…

## `docs/planning/ai-drafted-issue-content/backend-draft-service`

[Directory guide](<planning/ai-drafted-issue-content/backend-draft-service/directory.md>)

- [plan_20260707.md](<planning/ai-drafted-issue-content/backend-draft-service/plan_20260707.md>) — Implementation Plan — backend-draft-service (2026-07-07): - `src/api/routes/feedback_issue_draft.py` — the route (mirrors `feedback_responses.py` structure). - `tests/test_issue_draft.py` — route + service tests.
- [spec.md](<planning/ai-drafted-issue-content/backend-draft-service/spec.md>) — Aspect Spec — backend-draft-service: A single shared backend service + endpoint that turns a feedback item into a `{title, body}` draft for a target work tracker (Jira/Asana), reusing the existing LLM resolution/call path.…

## `docs/planning/ai-drafted-issue-content/docs-and-tracking`

[Directory guide](<planning/ai-drafted-issue-content/docs-and-tracking/directory.md>)

- [plan_20260707.md](<planning/ai-drafted-issue-content/docs-and-tracking/plan_20260707.md>) — Implementation Plan — docs-and-tracking (2026-07-07): Documentation + tracking updates only — no code. Mirrors how every prior integration shipped with docs. task wizard when an LLM is configured (cloud BYOK **or** local…

## `docs/planning/ai-drafted-issue-content/frontend-draft-button`

[Directory guide](<planning/ai-drafted-issue-content/frontend-draft-button/directory.md>)

- [plan_20260707.md](<planning/ai-drafted-issue-content/frontend-draft-button/plan_20260707.md>) — Implementation Plan — frontend-draft-button (2026-07-07): `app/(dashboard)/feedbacks/[id]/__tests__/createIssueDraft.test.tsx` (or a focused component test). disabled button (`:290-301`), `toast.error` on failure. Mirror this…
- [spec.md](<planning/ai-drafted-issue-content/frontend-draft-button/spec.md>) — Aspect Spec — frontend-draft-button: A "✨ Draft with AI" button in the Jira and Asana branches of the create-issue/task wizard that calls the draft endpoint and fills the title/body fields for review — never auto-creates;…

## `docs/planning/asana-integration`

[Directory guide](<planning/asana-integration/directory.md>)

- [prd.md](<planning/asana-integration/prd.md>) — PRD — Asana Integration (slice 1): Rereflect turns customer feedback into insight, but acting on that insight means creating work items in whatever tool a team already runs on. Rereflect can already push feedback into **Jira**…
- [understanding.md](<planning/asana-integration/understanding.md>) — Understanding — Asana Integration (slice 1): Add Asana as the next integration, mirroring the **Jira** precedent, which is the closest match: an **own-auth, outbound** integration whose core action is **create an Asana task from…

## `docs/planning/asana-integration/backend-connection`

[Directory guide](<planning/asana-integration/backend-connection/directory.md>)

- [plan_20260706.md](<planning/asana-integration/backend-connection/plan_20260706.md>) — Implementation Plan — backend-connection (2026-07-06): 1. RED: `tests/test_asana_models.py` — assert columns, `uq_asana_integrations_org_id`, org index, `connected_by_user_id` SET NULL, `feedback_id` cascade; encrypted-token…
- [spec.md](<planning/asana-integration/backend-connection/spec.md>) — Aspect: backend-connection: An operator connects their Asana account with a Personal Access Token and can test/disconnect it. This aspect delivers the model, migration, encrypted-token storage, the `AsanaClient` (auth + validate…

## `docs/planning/asana-integration/backend-create-task`

[Directory guide](<planning/asana-integration/backend-create-task/directory.md>)

- [plan_20260706.md](<planning/asana-integration/backend-create-task/plan_20260706.md>) — Implementation Plan — backend-create-task (2026-07-06): 2. GREEN: implement `create_task({name, notes, project_gid, workspace_gid})`. `tests/test_asana_issues.py` mirrors `test_jira_issues.py`. Mock `AsanaClient` at the route…
- [spec.md](<planning/asana-integration/backend-create-task/spec.md>) — Aspect: backend-create-task: From a feedback item, a user creates an Asana task. This aspect delivers the `FeedbackAsanaTask` link model, the create-task route with a duplicate guard and timeline event, the…

## `docs/planning/asana-integration/frontend`

[Directory guide](<planning/asana-integration/frontend/directory.md>)

- [plan_20260706.md](<planning/asana-integration/frontend/plan_20260706.md>) — Implementation Plan — frontend (2026-07-06): 1. RED: `asana.test.ts` (`vi.mock('@/lib/api-client')`) asserts each `asanaAPI.*` hits the right URL/payload; **connect sends only `{api_token}`**. `asanaIssueWizard.test.ts` covers…
- [spec.md](<planning/asana-integration/frontend/spec.md>) — Aspect: frontend: Last (needs the backend endpoints). API client + connect page can start against the contract once backend-connection lands; the wizard branch needs backend-create-task.

## `docs/planning/asana-integration/landing`

[Directory guide](<planning/asana-integration/landing/directory.md>)

- [plan_20260706.md](<planning/asana-integration/landing/plan_20260706.md>) — Implementation Plan — landing (2026-07-06): Build + lint the landing site (`npm run build && npm run lint`). Visual check: `/integrations` grid shows Asana as available; `/integrations/asana` renders; marquee includes it. Docs:…
- [spec.md](<planning/asana-integration/landing/spec.md>) — Aspect: landing: The marketing site lists Asana as an available integration with its own page, and self-hosters have setup docs for pasting the PAT. Mirror how Jira/Zendesk shipped their landing + docs together. Fully independent…

## `docs/planning/asana-integration/source-type-registration`

[Directory guide](<planning/asana-integration/source-type-registration/directory.md>)

- [plan_20260706.md](<planning/asana-integration/source-type-registration/plan_20260706.md>) — Implementation Plan — source-type-registration (2026-07-06)
- [spec.md](<planning/asana-integration/source-type-registration/spec.md>) — Aspect: source-type-registration: `asana` appears as a selectable own-auth source type, for parity with Jira/Zendesk/Linear. This is a **lightweight backend registration only** — the worker has no Jira adapter and gets no Asana…

## `docs/planning/asana-status-sync`

[Directory guide](<planning/asana-status-sync/directory.md>)

- [prd.md](<planning/asana-status-sync/prd.md>) — PRD — Asana Inbound Status-Sync: The Asana integration (slice 1, shipped 2026-07-06) is **outbound-only**: an operator can create an Asana task from a feedback item, but when the engineer later completes that task in Asana, the

## `docs/planning/asana-status-sync/asana-client-get-task`

[Directory guide](<planning/asana-status-sync/asana-client-get-task/directory.md>)

- [plan_20260712.md](<planning/asana-status-sync/asana-client-get-task/plan_20260712.md>) — Implementation Plan — asana-status-sync / asana-client-get-task: phases, or split Phase 1 (backend) from Phases 2–3 (worker); the two services never share files. This aspect adds the **read** capability the poller needs — nothing…
- [spec.md](<planning/asana-status-sync/asana-client-get-task/spec.md>) — Aspect: asana-client-get-task: The reconcile core needs each linked Asana task's current completion state. Today `AsanaClient` can only create tasks. Add a read method (backend + a worker copy), so the poller has something to…

## `docs/planning/asana-status-sync/backend-routes`

[Directory guide](<planning/asana-status-sync/backend-routes/directory.md>)

- [plan_20260712.md](<planning/asana-status-sync/backend-routes/plan_20260712.md>) — Implementation Plan — asana-status-sync / backend-routes: Existing codebase — no scaffolding. This aspect is the **operator control surface** for Asana inbound `services/backend-api/src/api/routes/jira_integration.py` onto the…
- [spec.md](<planning/asana-status-sync/backend-routes/spec.md>) — Aspect: backend-routes: Operator controls: toggle status-sync + set mapping, trigger a manual sync, and see sync state. Mirror the three Jira endpoints in `routes/jira_integration.py`.

## `docs/planning/asana-status-sync/docs-and-tracking`

[Directory guide](<planning/asana-status-sync/docs-and-tracking/directory.md>)

- [plan_20260712.md](<planning/asana-status-sync/docs-and-tracking/plan_20260712.md>) — Implementation Plan — docs-and-tracking (2026-07-12): Documentation + tracking updates only — **no code, no tests**. This aspect records the shipped Asana inbound status-sync in the operator docs and the two tracking files,…
- [spec.md](<planning/asana-status-sync/docs-and-tracking/spec.md>) — Aspect: docs-and-tracking: Ship the operator-facing docs and mark the feature shipped in the roadmap/tracking files, honestly and default), the default mapping `{done: resolved, new: new}`, how to remap via the API, poll-first (no

## `docs/planning/asana-status-sync/frontend`

[Directory guide](<planning/asana-status-sync/frontend/directory.md>)

- [plan_20260712.md](<planning/asana-status-sync/frontend/plan_20260712.md>) — Implementation Plan — frontend (2026-07-12): Asana settings detail page — a line-for-line parity of the shipped Jira card. No new design, no mapping editor. This aspect is a mechanical `jira → asana` mirror of the already-merged…
- [spec.md](<planning/asana-status-sync/frontend/spec.md>) — Aspect: frontend: Give operators the status-sync toggle, last-synced/error indicator, and "Sync now" button on the Asana settings detail page — a line-for-line parity of the Jira card.

## `docs/planning/asana-status-sync/model-migrations`

[Directory guide](<planning/asana-status-sync/model-migrations/directory.md>)

- [plan_20260712.md](<planning/asana-status-sync/model-migrations/plan_20260712.md>) — Tech Plan — Asana Status-Sync · Aspect: model-migrations: Add the durable state inbound status-sync reads/writes. Five new columns, one migration, worker mirror models. **No routes, no tasks, no client logic** — those are later…
- [spec.md](<planning/asana-status-sync/model-migrations/spec.md>) — Aspect: model-migrations: Add the durable state that inbound status-sync reads and writes: the per-org opt-in flag + mapping on `AsanaIntegration`, and per-link sync state on `FeedbackAsanaTask`. Without these columns nothing else

## `docs/planning/asana-status-sync/worker-sync-task`

[Directory guide](<planning/asana-status-sync/worker-sync-task/directory.md>)

- [plan_20260712.md](<planning/asana-status-sync/worker-sync-task/plan_20260712.md>) — Implementation Plan — asana-status-sync / worker-sync-task: mirror already carries the new columns; if it does not yet, STOP and hand back to model-migrations (see already contains `{"done": "resolved", "new": "new",…
- [spec.md](<planning/asana-status-sync/worker-sync-task/spec.md>) — Aspect: worker-sync-task: The heart of the feature: a poll-first Celery task that reconciles Asana task completion onto linked feedback, reusing the pure `status_sync_core.py`. Mirror `worker-service/src/tasks/jira_sync.py`.

## `docs/planning/automation-action-support`

[Directory guide](<planning/automation-action-support/directory.md>)

- [prd.md](<planning/automation-action-support/prd.md>) — PRD — Automation action support per trigger: `run_playbook` sit on any trigger — intended?" Investigating it found real inert behaviour. `routes/automations.py` validates action *types* but never checks them against the trigger,…

## `docs/planning/automation-playbook-dispatch-commit`

[Directory guide](<planning/automation-playbook-dispatch-commit/directory.md>)

- [prd.md](<planning/automation-playbook-dispatch-commit/prd.md>) — PRD — Automation playbook dispatch: commit before publish: Automation rules that carry a `run_playbook` action create a `ChurnPlaybookExecution` row, `flush()` it for an id, and publish that id to Celery **before committing**.…
- [understanding.md](<planning/automation-playbook-dispatch-commit/understanding.md>) — Understanding — automation-playbook-dispatch-commit: Dig date: 2026-09-25, against `origin/master` @ `6ecae609`. Three read-only agents (backend engine, worker mirrors, repo-wide sweep) plus direct verification of every cited…

## `docs/planning/automation-playbook-dispatch-commit/dispatch-ordering`

[Directory guide](<planning/automation-playbook-dispatch-commit/dispatch-ordering/directory.md>)

- [plan_20260925.md](<planning/automation-playbook-dispatch-commit/dispatch-ordering/plan_20260925.md>) — Plan — dispatch-ordering (2026-09-25): mirroring `tests/test_automation_engine_send_customer_email.py:445-484` (spy `db.commit`, Run → FAIL (commit only at `_evaluate_rule:203`, after send_task).
- [spec.md](<planning/automation-playbook-dispatch-commit/dispatch-ordering/spec.md>) — Spec — dispatch-ordering: publishing its id, so the worker can always find it (PRD M1–M3). Deferred dispatch; retry on `not found`; publish-failure handling; trigger/action restriction.

## `docs/planning/automation-playbook-dispatch-commit/live-acceptance-and-tracking`

[Directory guide](<planning/automation-playbook-dispatch-commit/live-acceptance-and-tracking/directory.md>)

- [evidence.md](<planning/automation-playbook-dispatch-commit/live-acceptance-and-tracking/evidence.md>) — Live acceptance evidence — 2026-09-25: rule (threshold 0.5, `run_playbook` → that playbook), 40 `customer_health_scores` rows. (`ValueError: not enough values to unpack` in `fast_trace_task`) before running any task.
- [plan_20260925.md](<planning/automation-playbook-dispatch-commit/live-acceptance-and-tracking/plan_20260925.md>) — Plan — live-acceptance-and-tracking (2026-09-25): `churn_probability_threshold` rule (threshold low, cooldown 1h) with `run_playbook`, a `CustomerHealth`
- [spec.md](<planning/automation-playbook-dispatch-commit/live-acceptance-and-tracking/spec.md>) — Spec — live-acceptance-and-tracking: real Celery worker from the worktree on an isolated Redis DB index; drive `evaluate_churn_probability_triggers` against an active `churn_probability_threshold` rule with a

## `docs/planning/automation-playbook-dispatch-commit/source-events-dispatch`

[Directory guide](<planning/automation-playbook-dispatch-commit/source-events-dispatch/directory.md>)

- [plan_20260925.md](<planning/automation-playbook-dispatch-commit/source-events-dispatch/plan_20260925.md>) — Plan — source-events-dispatch (2026-09-25): add `test_auto_import_commits_before_enqueueing_analysis`: spy `db.commit` / patch `src.tasks.analysis.analyze_single_feedback` `.delay` side_effect; assert order + id. FAIL on master.
- [spec.md](<planning/automation-playbook-dispatch-commit/source-events-dispatch/spec.md>) — Spec — source-events-dispatch: published, so analysis never returns `not_found` for a fresh item (PRD S1). `services/worker-service/src/tasks/source_events.py`: `_process_event_for_source` stops calling

## `docs/planning/automation-send-customer-email`

[Directory guide](<planning/automation-send-customer-email/directory.md>)

- [prd.md](<planning/automation-send-customer-email/prd.md>) — PRD — Automations `send_customer_email` action: Automation rules — the heart of the churn → health → playbook → automations loop (`AI-TRACKING.md:5`) — can only act *inside* the app. The four action types

## `docs/planning/automation-send-customer-email/action-core`

[Directory guide](<planning/automation-send-customer-email/action-core/directory.md>)

- [plan_20260819.md](<planning/automation-send-customer-email/action-core/plan_20260819.md>) — Plan — action-core (backend action type + delivery model): Scope: **backend-api only.** The worker task (`tasks.outreach.send_automation_email`), the three worker mirrors, the frontend editor, the seeded template and docs are…
- [spec.md](<planning/automation-send-customer-email/action-core/spec.md>) — Spec — action-core (backend action type + delivery model): The automations engine has no way to email the customer. This aspect adds the backend half: the `send_customer_email` action type, its config validation, the

## `docs/planning/automation-send-customer-email/docs-and-templates`

[Directory guide](<planning/automation-send-customer-email/docs-and-templates/directory.md>)

- [plan_20260819.md](<planning/automation-send-customer-email/docs-and-templates/plan_20260819.md>) — Implementation Plan — `docs-and-templates` (seeded shadow template + documentation): Every claim below was read from the worktree before writing this plan. This is the contract the implementation must match. There is no…
- [spec.md](<planning/automation-send-customer-email/docs-and-templates/spec.md>) — Spec — docs-and-templates (seeded shadow template + documentation): The feature is invisible without an in-product example and operator docs. This aspect seeds a shadow-mode template that uses the action, and updates all…

## `docs/planning/automation-send-customer-email/frontend-editor`

[Directory guide](<planning/automation-send-customer-email/frontend-editor/directory.md>)

- [plan_20260819.md](<planning/automation-send-customer-email/frontend-editor/plan_20260819.md>) — Implementation Plan — frontend-editor (send_customer_email editor + labels + deliveries surface): All paths below are relative to `services/frontend-web/` unless prefixed. All validation runs from `services/frontend-web/` (`npm…
- [spec.md](<planning/automation-send-customer-email/frontend-editor/spec.md>) — Spec — frontend-editor (action editor + labels + deliveries surface): Operators can't configure the new action or see its outcome. This aspect adds the `send_customer_email` action to the automations editor (template + recipient…

## `docs/planning/automation-send-customer-email/worker-mirrors`

[Directory guide](<planning/automation-send-customer-email/worker-mirrors/directory.md>)

- [plan_20260819.md](<planning/automation-send-customer-email/worker-mirrors/plan_20260819.md>) — Implementation Plan — worker-mirrors (task + three evaluator mirrors): `automation_email_deliveries` model + migration + the task-name contract (`tasks.outreach.send_automation_email`) live in the backend and are authored by
- [spec.md](<planning/automation-send-customer-email/worker-mirrors/spec.md>) — Spec — worker-mirrors (task + three evaluator mirrors): The send actually happens in the worker. This aspect adds the single `send_automation_email` worker task (the only place that sends) and extends all three

## `docs/planning/automations-delivery-integrity`

[Directory guide](<planning/automations-delivery-integrity/directory.md>)

- [prd.md](<planning/automations-delivery-integrity/prd.md>) — PRD — Automations Delivery Integrity: Rereflect's automations surface tells users it is doing things it is not doing. Two independent, **verified** defects compound on the same code path.

## `docs/planning/automations-delivery-integrity/slack-channel-and-loudness`

[Directory guide](<planning/automations-delivery-integrity/slack-channel-and-loudness/directory.md>)

- [plan_20260729.md](<planning/automations-delivery-integrity/slack-channel-and-loudness/plan_20260729.md>) — Implementation Plan — `slack-channel-and-loudness` (2026-07-29): (system `python3` is 3.9.6 and fails on Authlib — use `python3.12` explicitly). `services/backend-api/src/services/automation_engine.py`:
- [spec.md](<planning/automations-delivery-integrity/slack-channel-and-loudness/spec.md>) — Spec — `slack-channel-and-loudness`: `AutomationEngine._execute_notify` (`services/backend-api/src/services/automation_engine.py:485-571`) silently drops any channel it does not implement, and reports the resulting no-op as a

## `docs/planning/automations-delivery-integrity/worker-trigger-mirror`

[Directory guide](<planning/automations-delivery-integrity/worker-trigger-mirror/directory.md>)

- [plan_20260729.md](<planning/automations-delivery-integrity/worker-trigger-mirror/plan_20260729.md>) — Implementation Plan — `worker-trigger-mirror` (2026-07-29): - Worker: `cd services/worker-service && ./venv/bin/pytest tests/ -v` - Backend (migration): `cd services/backend-api && ./venv/bin/pytest tests/ -v`
- [spec.md](<planning/automations-delivery-integrity/worker-trigger-mirror/spec.md>) — Spec — `worker-trigger-mirror`: `services/worker-service/src/tasks/analysis.py:175` imports `AutomationEngine` from a module that does not exist in worker-service, inside a `try/except Exception` that logs a

## `docs/planning/backend-security-smalls`

[Directory guide](<planning/backend-security-smalls/directory.md>)

- [plan_20260818.md](<planning/backend-security-smalls/plan_20260818.md>) — Implementation plan — backend-security-smalls (2026-08-18): Source: `docs/planning/backend-security-smalls/prd.md`. House commit style. - `services/backend-api/src/api/routes/integrations.py` — delete `oauth_states`
- [prd.md](<planning/backend-security-smalls/prd.md>) — PRD — Backend security smalls (oauth state, generic webhook secret, events-emit): TTL: OAuth callbacks (Slack :841-871, Intercom :1032-1062) fail intermittently on any multi-replica backend, and entries never expire (the stored…

## `docs/planning/batch-sentiment-trigger`

[Directory guide](<planning/batch-sentiment-trigger/directory.md>)

- [prd.md](<planning/batch-sentiment-trigger/prd.md>) — PRD — Batch sentiment threshold trigger: A v1.0.0 user asked to be pinged when *"a batch of new feedback crosses a certain sentiment The closest trigger, `sentiment_pattern`, fires when **one customer** sends ≥`count`

## `docs/planning/batch-sentiment-trigger/trigger-core`

[Directory guide](<planning/batch-sentiment-trigger/trigger-core/directory.md>)

- [spec.md](<planning/batch-sentiment-trigger/trigger-core/spec.md>) — Spec — `trigger-core`: `automation_cooldown:{rule_id}:{customer_email}`. This trigger is org-wide, so it must use a single per-rule key. Pass the sentinel `"__org__"` as the **cooldown identity only**.

## `docs/planning/churn-customer-factor-coverage`

[Directory guide](<planning/churn-customer-factor-coverage/directory.md>)

- [prd.md](<planning/churn-customer-factor-coverage/prd.md>) — PRD — Churn customer-level factor coverage: `_compute_heuristic_churn_risk` (`services/worker-service/src/tasks/analysis.py`) scores customers on 9 weighted factors totalling 100 points. One of them has never worked, and

## `docs/planning/churn-customer-factor-coverage/customer-factor-coverage`

[Directory guide](<planning/churn-customer-factor-coverage/customer-factor-coverage/directory.md>)

- [plan_20260729.md](<planning/churn-customer-factor-coverage/customer-factor-coverage/plan_20260729.md>) — Implementation Plan — `customer-factor-coverage` (2026-07-29): (`sqlite:///:memory:`, `TestingSessionLocal`). The DB-backed tests were always possible; nobody wrote them. Use it; do not build a new harness.
- [spec.md](<planning/churn-customer-factor-coverage/customer-factor-coverage/spec.md>) — Spec — `customer-factor-coverage`: Fix the dead `resolution_time` factor, and close the coverage hole that let it stay dead: five customer-level factors (50 of 100 points) are never executed against a real DB session

## `docs/planning/churn-triggered-playbooks`

[Directory guide](<planning/churn-triggered-playbooks/directory.md>)

- [plan_20260718.md](<planning/churn-triggered-playbooks/plan_20260718.md>) — Implementation Plan — Churn-Triggered Playbook Auto-Execution: trigger + a `run_playbook` action + `off/shadow/active` `mode`. Health/`risk_level` auto-runs flow through the backend engine (already dispatched from
- [prd.md](<planning/churn-triggered-playbooks/prd.md>) — PRD — Churn-Triggered Playbook Auto-Execution: Rereflect closes most of the churn loop: it computes a calibrated **churn probability** and a **customer health score** (M4.1), and it ships **churn playbooks** — reusable

## `docs/planning/classifier-model-versioning-rollback`

[Directory guide](<planning/classifier-model-versioning-rollback/directory.md>)

- [plan_20260724.md](<planning/classifier-model-versioning-rollback/plan_20260724.md>) — Implementation Plan — Durable Classifier Model Rollback + Versioning (2026-07-24): (`sentiment_autopromote_hold` / `category_autopromote_hold` / `urgency_autopromote_hold`, Boolean, default false). NOT a row-pin. The
- [prd.md](<planning/classifier-model-versioning-rollback/prd.md>) — PRD — Durable Classifier Model Rollback + Versioning: Rereflect's flagship moat is the **per-org self-improving classifier flywheel** (M5.2 — sentiment/category/urgency heads trained on the org's own corrections,
- [understanding.md](<planning/classifier-model-versioning-rollback/understanding.md>) — Understanding — durable classifier model rollback + versioning: originally-recommended feature already shipped. See `_card/card.md` for the Commits `a630c9c` + `cea261b` (M5.2 settings), documented `AI-TRACKING.md:63-65`:

## `docs/planning/classifier-model-versioning-rollback/backend-routes`

[Directory guide](<planning/classifier-model-versioning-rollback/backend-routes/directory.md>)

- [spec.md](<planning/classifier-model-versioning-rollback/backend-routes/spec.md>) — Aspect spec — backend-routes: All under existing router `services/backend-api/src/api/routes/classifier_accuracy.py` (prefix `/api/v1/settings/ai`). Schemas in `src/schemas/classifier_accuracy.py`.

## `docs/planning/classifier-model-versioning-rollback/data-model-and-migration`

[Directory guide](<planning/classifier-model-versioning-rollback/data-model-and-migration/directory.md>)

- [spec.md](<planning/classifier-model-versioning-rollback/data-model-and-migration/spec.md>) — Aspect spec — data-model-and-migration: Add the durable per-type "auto-promotion hold" storage. No hold field exists today. `sentiment_autopromote_hold`, `category_autopromote_hold`,

## `docs/planning/classifier-model-versioning-rollback/docs-and-tracking`

[Directory guide](<planning/classifier-model-versioning-rollback/docs-and-tracking/directory.md>)

- [spec.md](<planning/classifier-model-versioning-rollback/docs-and-tracking/spec.md>) — Aspect spec — docs-and-tracking: Record the durable-rollback behavior for operators and correct the stale roadmap model performance over time, rollback if accuracy drops") — now delivered. Add a

## `docs/planning/classifier-model-versioning-rollback/frontend-versioning-ui`

[Directory guide](<planning/classifier-model-versioning-rollback/frontend-versioning-ui/directory.md>)

- [spec.md](<planning/classifier-model-versioning-rollback/frontend-versioning-ui/spec.md>) — Aspect spec — frontend-versioning-ui: Files: `services/frontend-web/components/settings/ClassifierAccuracyCard.tsx`, `services/frontend-web/lib/api/classifier-accuracy.ts` (+ tests). pnpm.

## `docs/planning/classifier-model-versioning-rollback/worker-hold-guard`

[Directory guide](<planning/classifier-model-versioning-rollback/worker-hold-guard/directory.md>)

- [spec.md](<planning/classifier-model-versioning-rollback/worker-hold-guard/spec.md>) — Aspect spec — worker-hold-guard: Make the weekly auto-promotion honor the hold, race-safely, without freezing the after acquiring the per-(type,org) Redis refit lock and after `evaluate()`, and

## `docs/planning/copilot-suggested-actions`

[Directory guide](<planning/copilot-suggested-actions/directory.md>)

- [prd.md](<planning/copilot-suggested-actions/prd.md>) — PRD: AI Copilot Suggested Actions: The AI Copilot can answer any question about an org's feedback and can do nothing about the answer. A CS lead asks "which customers mentioned billing friction this month?", gets a

## `docs/planning/copilot-suggested-actions/action-contract`

[Directory guide](<planning/copilot-suggested-actions/action-contract/directory.md>)

- [plan_20260906.md](<planning/copilot-suggested-actions/action-contract/plan_20260906.md>) — Implementation plan — action-contract (2026-09-06): Source: `docs/planning/copilot-suggested-actions/prd.md` + `action-contract/spec.md`. House commit style (`feat(...): ... (TDD)` / `test(...): RED — ...`).
- [spec.md](<planning/copilot-suggested-actions/action-contract/spec.md>) — Spec: action-contract: Both ends of this feature must agree on one JSON shape that neither can see the other define. `MessageBubble.tsx:269-282` **silently skips** any unrecognised `data_type`, so a backend that

## `docs/planning/copilot-suggested-actions/action-registry`

[Directory guide](<planning/copilot-suggested-actions/action-registry/directory.md>)

- [plan_20260909.md](<planning/copilot-suggested-actions/action-registry/plan_20260909.md>) — Implementation Plan — action-registry: - `services/backend-api/src/services/copilot/action_registry.py` — the registry + executor wiring. - `services/backend-api/src/services/customer_tags.py` — extracted shared tag-apply logic…
- [spec.md](<planning/copilot-suggested-actions/action-registry/spec.md>) — Spec: action-registry: Something must decide what is executable, who may execute it, and what happens when it runs. Without a registry the only alternatives are trusting a model to name an executor or wiring

## `docs/planning/copilot-suggested-actions/deterministic-proposer`

[Directory guide](<planning/copilot-suggested-actions/deterministic-proposer/directory.md>)

- [plan_20260909.md](<planning/copilot-suggested-actions/deterministic-proposer/plan_20260909.md>) — Implementation Plan — deterministic-proposer: - `services/backend-api/src/services/copilot/action_proposer.py` — pure, synchronous, **no LLM**. - `extract_customer_emails(["customer_email", "sentiment"], [["a@x.com", "neg"],…
- [spec.md](<planning/copilot-suggested-actions/deterministic-proposer/spec.md>) — Spec: deterministic-proposer: Something must decide *when* to offer an action, without an LLM in the loop. Using the model to propose would put customer-authored feedback text in the path that produces a clickable

## `docs/planning/copilot-suggested-actions/docs-tracking`

[Directory guide](<planning/copilot-suggested-actions/docs-tracking/directory.md>)

- [plan_20260909.md](<planning/copilot-suggested-actions/docs-tracking/plan_20260909.md>) — Implementation Plan — docs-tracking: - The new `actions` item in `structured_data`: after a `data`/`analysis` query whose result carries a customer-email column, the copilot appends one **Tag these N customers…** action; clicking…
- [spec.md](<planning/copilot-suggested-actions/docs-tracking/spec.md>) — Spec: docs-tracking: This repo's tracking files are the roadmap's source of truth, and `rereflect-next` reads them to choose what to build. A capability that ships without updating them causes the exact drift

## `docs/planning/copilot-suggested-actions/frontend-actions-ui`

[Directory guide](<planning/copilot-suggested-actions/frontend-actions-ui/directory.md>)

- [plan_20260909.md](<planning/copilot-suggested-actions/frontend-actions-ui/plan_20260909.md>) — Implementation Plan — frontend-actions-ui: - `services/frontend-web/lib/api/copilot-actions.ts` — the execute API function. - `services/frontend-web/components/copilot/CopilotActionButton.tsx` (or inline in MessageBubble — see…
- [spec.md](<planning/copilot-suggested-actions/frontend-actions-ui/spec.md>) — Spec: frontend-actions-ui: The proposal is invisible until something renders it. `MessageBubble` currently branches only (`MessageBubble.tsx:269-282`) with an `actions` branch, rendering one button per entry using

## `docs/planning/crm-churn-labels`

[Directory guide](<planning/crm-churn-labels/directory.md>)

- [prd.md](<planning/crm-churn-labels/prd.md>) — PRD — CRM-Sourced Churn Labels (lost-renewal suggestions + operator review): (5-agent dig), `PRD-ADVANCED-CHURN-PREDICTION.md` §9, `AI-TRACKING.md` M3.1/M3.1b/M5.0/M5.3 Rereflect's stated killer feature is "churn prediction that…

## `docs/planning/crm-churn-labels/data-model`

[Directory guide](<planning/crm-churn-labels/data-model/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/data-model/plan_20260715.md>) — Implementation Plan — data-model: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. `cd services/backend-api && /Users/aliz/dev/at/rereflect/services/backend-api/venv/bin/python -m alembic heads`
- [spec.md](<planning/crm-churn-labels/data-model/spec.md>) — Aspect spec — data-model: Every other aspect (harvester, review queue, settings cards, readiness) needs a place to put a suggestion and a per-org opt-in flag to read. This aspect owns **the single Alembic revision and

## `docs/planning/crm-churn-labels/docs-and-tracking`

[Directory guide](<planning/crm-churn-labels/docs-and-tracking/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/docs-and-tracking/plan_20260715.md>) — Implementation Plan — docs-and-tracking: Strict TDD where testable (the grep gates + landing tests). Keep the branch green after every phase. aspect as "wave 4 — blocked on everything", listing `review-queue` (M5) and…
- [spec.md](<planning/crm-churn-labels/docs-and-tracking/spec.md>) — Aspect spec — docs-and-tracking: Every recent feature here ships `docs(...)` commits — CRM enrichment, writeback, status-sync and public-API v3 all landed with `SELF_HOSTING.md` + `CHANGELOG.md` + tracking updates in the same

## `docs/planning/crm-churn-labels/harvester-core`

[Directory guide](<planning/crm-churn-labels/harvester-core/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/harvester-core/plan_20260715.md>) — Implementation Plan — harvester-core: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. Wave 1 is merged; re-verified in this worktree, all file:line-checked.
- [spec.md](<planning/crm-churn-labels/harvester-core/spec.md>) — Aspect spec — harvester-core: `provider-churn-fetch` makes lost-renewal records reachable; `data-model` makes suggestions storable. This aspect is the decision + wiring between them: given a closed-lost HubSpot deal or

## `docs/planning/crm-churn-labels/historical-backfill`

[Directory guide](<planning/crm-churn-labels/historical-backfill/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/historical-backfill/plan_20260715.md>) — Implementation Plan — historical-backfill: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. rows. ~50 real churns/year for a 1,000-customer org ⇒ forward-only reaches the 500 gate in ~10 years. The
- [spec.md](<planning/crm-churn-labels/historical-backfill/spec.md>) — Aspect spec — historical-backfill: (`ai_readiness.py:74-79`) and the calibrator gate (`churn_calibration.py:50`) count `CustomerChurnEvent` rows — *actual churns*. An org with 1,000 customers at 5% annual churn

## `docs/planning/crm-churn-labels/org-config-api-and-ui`

[Directory guide](<planning/crm-churn-labels/org-config-api-and-ui/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/org-config-api-and-ui/plan_20260715.md>) — Implementation Plan — org-config-api-and-ui: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. No new deps, no migration, no env vars. Frontend deps only if `node_modules` is absent (it is): **`pnpm…
- [spec.md](<planning/crm-churn-labels/org-config-api-and-ui/spec.md>) — Aspect spec — org-config-api-and-ui: The churn rule is **default-deny** (PRD M2): no suggestion is produced unless the lost deal's HubSpot `pipeline` / Salesforce `Opportunity.Type` is in the org's configured renewal set. Both

## `docs/planning/crm-churn-labels/provider-churn-fetch`

[Directory guide](<planning/crm-churn-labels/provider-churn-fetch/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/provider-churn-fetch/plan_20260715.md>) — Implementation Plan — provider-churn-fetch: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. Every line below was opened and read in this worktree on 2026-07-15. Corrections to the spec/dig are…
- [spec.md](<planning/crm-churn-labels/provider-churn-fetch/spec.md>) — Aspect spec — provider-churn-fetch: Neither CRM client can see a lost renewal today. HubSpot fetches `closedlost` and throws it away (`clients/hubspot.py:280-284`); Salesforce excludes it at the API…

## `docs/planning/crm-churn-labels/readiness-honesty`

[Directory guide](<planning/crm-churn-labels/readiness-honesty/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/readiness-honesty/plan_20260715.md>) — Implementation Plan — readiness-honesty: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. `CustomerChurnEvent` filtered on `organization_id` **only** — no source filter.
- [spec.md](<planning/crm-churn-labels/readiness-honesty/spec.md>) — Aspect spec — readiness-honesty: use.** `_churn_label_counts` (`routes/ai_readiness.py:74-79`) counts `CustomerChurnEvent` with `services/calibration_refit.py:64,191`. The report and the fit disagree about what a label is —

## `docs/planning/crm-churn-labels/review-queue`

[Directory guide](<planning/crm-churn-labels/review-queue/directory.md>)

- [plan_20260715.md](<planning/crm-churn-labels/review-queue/plan_20260715.md>) — Implementation Plan — review-queue: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. This aspect is the feature's **trust boundary**. Waves 1–2 shipped a harvester that writes
- [spec.md](<planning/crm-churn-labels/review-queue/spec.md>) — Aspect spec — review-queue: A CRM suggestion is a guess. Nothing trains a model until a **human confirms** it — this queue is the only thing that turns a `churn_label_suggestions` row into a real `CustomerChurnEvent` the…

## `docs/planning/crm-writeback`

[Directory guide](<planning/crm-writeback/directory.md>)

- [prd.md](<planning/crm-writeback/prd.md>) — PRD — Bidirectional CRM Writeback (HubSpot, slice 1): Rereflect computes a per-customer **health score** (and churn signals), but that intelligence lives only inside Rereflect. The people who act on it — CSMs, account owners —…

## `docs/planning/crm-writeback/hubspot-write-client`

[Directory guide](<planning/crm-writeback/hubspot-write-client/directory.md>)

- [plan_20260703.md](<planning/crm-writeback/hubspot-write-client/plan_20260703.md>) — Plan — hubspot-write-client (worker): - modify `services/worker-service/src/clients/hubspot.py` - create `services/worker-service/tests/test_hubspot_write_client.py`
- [spec.md](<planning/crm-writeback/hubspot-write-client/spec.md>) — Aspect: hubspot-write-client (worker): The worker's `HubSpotClient` (`src/clients/hubspot.py`) is read-only (GET). Add the outbound write surface so the push task can set a contact property and validate the target field.

## `docs/planning/crm-writeback/writeback-config-api`

[Directory guide](<planning/crm-writeback/writeback-config-api/directory.md>)

- [plan_20260703.md](<planning/crm-writeback/writeback-config-api/plan_20260703.md>) — Plan — writeback-config-api (backend + worker model mirror): - modify `services/backend-api/src/models/hubspot_integration.py` - modify `services/backend-api/src/models/crm_enrichment.py`
- [spec.md](<planning/crm-writeback/writeback-config-api/spec.md>) — Aspect: writeback-config-api (backend + worker model mirror): Persist the per-org writeback opt-in + field name + status, and expose an API to configure and read it. This is the config/state backbone the task and UI build on.

## `docs/planning/crm-writeback/writeback-task-trigger`

[Directory guide](<planning/crm-writeback/writeback-task-trigger/directory.md>)

- [plan_20260703.md](<planning/crm-writeback/writeback-task-trigger/plan_20260703.md>) — Plan — writeback-task-trigger (worker task + backend health hook): 4. **property 404** (`HubSpotNotFoundError` from GET/def or PATCH property) → `field_not_found` status, no `is_active` change. 5. **contact 404** → skip that…
- [spec.md](<planning/crm-writeback/writeback-task-trigger/spec.md>) — Aspect: writeback-task-trigger (worker task + backend health hook): When a customer's health score changes, push it to HubSpot — idempotently, gated to opted-in orgs, and soft-pausing (never breaking read-sync) on permanent…

## `docs/planning/crm-writeback/writeback-ui`

[Directory guide](<planning/crm-writeback/writeback-ui/directory.md>)

- [plan_20260703.md](<planning/crm-writeback/writeback-ui/plan_20260703.md>) — Plan — writeback-ui (frontend): 1. Failing tests (mock `apiClient`): `updateWriteback({enabled, field_name})` → `PATCH /api/v1/integrations/hubspot/writeback` with body; `testWriteback()` → `POST…
- [spec.md](<planning/crm-writeback/writeback-ui/spec.md>) — Aspect: writeback-ui (frontend): Let an admin/owner turn writeback on/off, set the custom-field name, run a validation check, and see writeback status — all on the existing HubSpot detail page, mirroring the ARR-property +

## `docs/planning/customer-360-unified-timeline`

[Directory guide](<planning/customer-360-unified-timeline/directory.md>)

- [prd.md](<planning/customer-360-unified-timeline/prd.md>) — PRD — Customer 360 Unified Timeline: A self-hosted operator looking at a customer in Rereflect cannot see that customer's *last-10* widget (`GET /api/v1/customers/{email}/activity`,

## `docs/planning/customer-360-unified-timeline/frontend-timeline-ui`

[Directory guide](<planning/customer-360-unified-timeline/frontend-timeline-ui/directory.md>)

- [plan_20260629.md](<planning/customer-360-unified-timeline/frontend-timeline-ui/plan_20260629.md>) — Implementation Plan — `frontend-timeline-ui`: `{ events: ActivityEvent[]; next_cursor: string / null }`. the existing `type, description, timestamp, feedback_id, old_score, new_score`.
- [spec.md](<planning/customer-360-unified-timeline/frontend-timeline-ui/spec.md>) — Aspect Spec — `frontend-timeline-ui`: The profile Overview tab shows a capped "Recent Activity" card (`ActivityTimeline.tsx`, `app/(dashboard)/customers/[email]/page.tsx:795-803`) that omits usage

## `docs/planning/customer-360-unified-timeline/public-api-customer360`

[Directory guide](<planning/customer-360-unified-timeline/public-api-customer360/directory.md>)

- [plan_20260629.md](<planning/customer-360-unified-timeline/public-api-customer360/plan_20260629.md>) — Implementation Plan — `public-api-customer360`: `CustomerProfileResponse` and the public profile can't diverge. confidence, 5 components incl. usage, churn_probability/bucket, llm summary fields, feedback_count,
- [spec.md](<planning/customer-360-unified-timeline/public-api-customer360/spec.md>) — Aspect Spec — `public-api-customer360`: The public REST API exposes only a customers *list* and a thin `/customers/{email}/health` (`routes/public_api.py:305-364`). M3.4 calls for a **Customer 360 API + health-score API +

## `docs/planning/customer-360-unified-timeline/timeline-service-v1`

[Directory guide](<planning/customer-360-unified-timeline/timeline-service-v1/directory.md>)

- [plan_20260629.md](<planning/customer-360-unified-timeline/timeline-service-v1/plan_20260629.md>) — Implementation Plan — `timeline-service-v1`: - Existing `/activity` logic to port: `src/api/routes/customers.py:512-611` (`get_customer_activity`). - `ActivityEvent` / `CustomerActivityResponse` schemas: `customers.py:143-153`…
- [spec.md](<planning/customer-360-unified-timeline/timeline-service-v1/spec.md>) — Aspect Spec — `timeline-service-v1`: Today `GET /api/v1/customers/{email}/activity` merges 5 sources inline and truncates to 10 (`routes/customers.py:512-611`). Usage (M3.2) and churn (M4.1) are absent and there is no

## `docs/planning/customer-outreach-email-actions`

[Directory guide](<planning/customer-outreach-email-actions/directory.md>)

- [prd.md](<planning/customer-outreach-email-actions/prd.md>) — PRD — Customer Outreach Email Actions: `churn-triggered-playbooks/prd.md:247-249` (deferred email/outreach actions), `playbook_seeder.py:109-113, 213-217` (shipped-but-broken `send_email` steps),

## `docs/planning/customer-outreach-email-actions/bulk-campaign-api`

[Directory guide](<planning/customer-outreach-email-actions/bulk-campaign-api/directory.md>)

- [plan_20260812.md](<planning/customer-outreach-email-actions/bulk-campaign-api/plan_20260812.md>) — Implementation Plan — bulk-campaign-api: `services/backend-api/src/models/outreach_campaign.py` (or the campaign model classes wherever outreach-core put them), `services/worker-service/src/services/outreach_sender.py`,
- [spec.md](<planning/customer-outreach-email-actions/bulk-campaign-api/spec.md>) — Spec — bulk-campaign-api: resolution with loud skips, campaign + per-recipient audit rows, the per-recipient Celery send task, the campaign list + retry endpoints, and the AI draft endpoint.

## `docs/planning/customer-outreach-email-actions/bulk-campaign-ui`

[Directory guide](<planning/customer-outreach-email-actions/bulk-campaign-ui/directory.md>)

- [plan_20260812.md](<planning/customer-outreach-email-actions/bulk-campaign-ui/plan_20260812.md>) — Implementation Plan — bulk-campaign-ui: (pnpm workspace, `@rereflect/ui` workspace dep). **Verify first** that no new packages are needed: the dialog uses only existing deps (`@radix-ui/react-*`,
- [spec.md](<planning/customer-outreach-email-actions/bulk-campaign-ui/spec.md>) — Spec — bulk-campaign-ui: the `BulkOutreachDialog` on `/customers`, the campaign list surface, the public unsubscribe page, and the `lib/api/outreach.ts` client. No backend, no worker, no

## `docs/planning/customer-outreach-email-actions/outreach-core`

[Directory guide](<planning/customer-outreach-email-actions/outreach-core/directory.md>)

- [plan_20260812.md](<planning/customer-outreach-email-actions/outreach-core/plan_20260812.md>) — Implementation Plan — outreach-core: `APP_URL`); new optional `OUTREACH_COOLDOWN_HOURS` (default 24) — read via `os.getenv("OUTREACH_COOLDOWN_HOURS", "24")`, int-cast defensively.
- [spec.md](<planning/customer-outreach-email-actions/outreach-core/spec.md>) — Spec — outreach-core: template registry, the worker send helper (opt-out + cooldown + List-Unsubscribe), the unsubscribe token/endpoint, and the per-customer opt-out mutation. No playbook/bulk

## `docs/planning/customer-outreach-email-actions/playbook-editor-email-config`

[Directory guide](<planning/customer-outreach-email-actions/playbook-editor-email-config/directory.md>)

- [plan_20260812.md](<planning/customer-outreach-email-actions/playbook-editor-email-config/plan_20260812.md>) — Implementation Plan — playbook-editor-email-config: Then `cd services/frontend-web && pnpm test` once to confirm the baseline suite is green. `PATCH /api/v1/customers/{email}` come from the `outreach-core` aspect
- [spec.md](<planning/customer-outreach-email-actions/playbook-editor-email-config/spec.md>) — Spec — playbook-editor-email-config: `send_email` config in `PlaybookEditor`, the `send_email` action type/labels in the frontend playbook API client, correct render of the seeded templates' steps through the

## `docs/planning/customer-outreach-email-actions/playbook-send-email-step`

[Directory guide](<planning/customer-outreach-email-actions/playbook-send-email-step/directory.md>)

- [plan_20260812.md](<planning/customer-outreach-email-actions/playbook-send-email-step/plan_20260812.md>) — Implementation Plan — playbook-send-email-step: vars. The engine *consumes* `send_outreach_email` (outreach-core) — opt-out/cooldown/ List-Unsubscribe/no-key handling is the sender's, never reimplemented here.
- [spec.md](<planning/customer-outreach-email-actions/playbook-send-email-step/spec.md>) — Spec — playbook-send-email-step: worker-service: the `_dispatch_action` branch, the `_handle_send_email` handler, two worker-model mirror columns, tests, and a CHANGELOG line. **Zero backend-api changes, zero migrations.**

## `docs/planning/customer-segments`

[Directory guide](<planning/customer-segments/directory.md>)

- [prd.md](<planning/customer-segments/prd.md>) — PRD — Customer Segments (rule-based): Rereflect surfaces every customer as an individual row on the Customers page with a health score and churn risk, but gives operators **no way to group customers by behavior**. A CS lead can't…
- [understanding.md](<planning/customer-segments/understanding.md>) — Understanding — Customer Segments (Phase 2 dig): Group customers into **rule-based behavioral cohorts** (power users, silent churners, happy advocates, at-risk, dormant, …) computed **only from signals that already exist** — no…

## `docs/planning/customer-segments/segment-api`

[Directory guide](<planning/customer-segments/segment-api/directory.md>)

- [plan_20260708.md](<planning/customer-segments/segment-api/plan_20260708.md>) — Implementation Plan — segment-api (2026-07-08): (`VALID_SORT_FIELDS`, `VALID_RISK_LEVELS`). Query build :276-306. Item assembly :322-337. `CustomerListItem` schema :39-50. `CustomerProfileResponse` :83-116; route filters returned…
- [spec.md](<planning/customer-segments/segment-api/spec.md>) — Aspect Spec — segment-api: The persisted `segment` is exposed on the customers-list endpoint (as a returned field + a filter param) and on the shared customer profile serializer — so both the internal dashboard route and the…

## `docs/planning/customer-segments/segment-engine`

[Directory guide](<planning/customer-segments/segment-engine/directory.md>)

- [plan_20260708.md](<planning/customer-segments/segment-engine/plan_20260708.md>) — Implementation Plan — segment-engine (2026-07-08): unique index `ix_customer_health_org_email` (:80). **Add `segment` column here.** Note existing partial-index precedent (`ix_customer_health_risk` on `(org, risk_level)`, :82) —…
- [spec.md](<planning/customer-segments/segment-engine/spec.md>) — Aspect Spec — segment-engine: Every non-archived `CustomerHealth` row resolves to exactly one segment slug (or `unsegmented`), persisted on the row, kept fresh on feedback ingest and by a nightly recompute. Pure, unit-tested,

## `docs/planning/customer-segments/segment-ui`

[Directory guide](<planning/customer-segments/segment-ui/directory.md>)

- [plan_20260708.md](<planning/customer-segments/segment-ui/plan_20260708.md>) — Implementation Plan — segment-ui (2026-07-08): gate on `npm run lint` + `npx tsc --noEmit` (typecheck) + component test IF vitest is present. :53), `customersAPI.list()` :232-245 (`query.set` around :238), `CustomerProfileData`…
- [spec.md](<planning/customer-segments/segment-ui/spec.md>) — Aspect Spec — segment-ui: Operators see each customer's segment as a labeled chip in the Customers list and on the profile, and can filter the list by segment — with honest "rule-based" framing and theme-correct colors.

## `docs/planning/discord-channel-preferences`

[Directory guide](<planning/discord-channel-preferences/directory.md>)

- [prd.md](<planning/discord-channel-preferences/prd.md>) — PRD — Discord channel preferences: Discord alerting **rides the Slack per-type toggle**. In the worker's `notification_dispatch.py`, the Discord webhook fires only when at least one user

## `docs/planning/discord-channel-preferences/backend-prefs-api`

[Directory guide](<planning/discord-channel-preferences/backend-prefs-api/directory.md>)

- [plan_20260809.md](<planning/discord-channel-preferences/backend-prefs-api/plan_20260809.md>) — Plan — backend-prefs-api: (`./start.sh` creates it if missing, or `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`). - `services/backend-api/tests/test_notifications.py` — extend…
- [spec.md](<planning/discord-channel-preferences/backend-prefs-api/spec.md>) — Spec — backend-prefs-api: The data model and API must be able to store and round-trip a per-type that PUTs preferences without the new field silently flipping Discord off.

## `docs/planning/discord-channel-preferences/docs`

[Directory guide](<planning/discord-channel-preferences/docs/directory.md>)

- [plan_20260809.md](<planning/discord-channel-preferences/docs/plan_20260809.md>) — Plan — docs: 2. Replace the block from "**⚠️ Discord currently rides on the Slack toggle.**" through "A dedicated `channel_discord` preference is a schema change and is
- [spec.md](<planning/discord-channel-preferences/docs/spec.md>) — Spec — docs: The operator documentation and changelog must describe the new per-type Discord channel behavior instead of the old "Discord rides the Slack toggle" limitation,

## `docs/planning/discord-channel-preferences/frontend-page`

[Directory guide](<planning/discord-channel-preferences/frontend-page/directory.md>)

- [plan_20260809.md](<planning/discord-channel-preferences/frontend-page/plan_20260809.md>) — Plan — frontend-page: `components/icons/DiscordIcon.tsx` (verify the import path used elsewhere: per-worktree — if missing, run `npm install` from the worktree root per pnpm
- [spec.md](<planning/discord-channel-preferences/frontend-page/spec.md>) — Spec — frontend-page: The Settings → Notifications page exposes a per-type **Discord** channel toggle so a user can route each alert type to Discord independently of Slack, and the row

## `docs/planning/discord-channel-preferences/worker-dispatch`

[Directory guide](<planning/discord-channel-preferences/worker-dispatch/directory.md>)

- [plan_20260809.md](<planning/discord-channel-preferences/worker-dispatch/plan_20260809.md>) — Plan — worker-dispatch: migration — the worker mirror is a code-only model copy). - `services/worker-service/tests/test_discord_dispatch.py`
- [spec.md](<planning/discord-channel-preferences/worker-dispatch/spec.md>) — Spec — worker-dispatch: The worker must dispatch Discord alerts off **their own** per-type `channel_discord` preference, independently of the Slack toggle, on **both**

## `docs/planning/discord-notifications`

[Directory guide](<planning/discord-notifications/directory.md>)

- [prd.md](<planning/discord-notifications/prd.md>) — PRD — Discord as an outbound alert destination: A v1.0.0 user asked to be pinged in "Slack **or Discord**". Slack works. Discord does not exist as an outbound destination anywhere — every `discord` string in the repo today is a

## `docs/planning/discord-notifications/alert-pipe`

[Directory guide](<planning/discord-notifications/alert-pipe/directory.md>)

- [spec.md](<planning/discord-notifications/alert-pipe/spec.md>) — Spec — `alert-pipe`: Discord webhooks accept a JSON body that **must** contain `content` and/or `embeds`. Posting anything else returns **400**. Always send both: `content` as a short plain-text

## `docs/planning/frontend-cleanup-smalls`

[Directory guide](<planning/frontend-cleanup-smalls/directory.md>)

- [plan_20260818.md](<planning/frontend-cleanup-smalls/plan_20260818.md>) — Implementation plan — frontend-cleanup-smalls (2026-08-18): Source: `docs/planning/frontend-cleanup-smalls/prd.md`. House commit style (`feat(ui): ... (TDD)` / `test(ui): RED — ...`). Commands from `services/frontend-web`:
- [prd.md](<planning/frontend-cleanup-smalls/prd.md>) — PRD — Frontend cleanup smalls (promo banner, integration role guards): (:50-66, banner JSX :332-352). There is no promo backend and no billing — the offer could never be honoured or withheld. The inline comment already flags it.

## `docs/planning/hubspot-crm-enrichment`

[Directory guide](<planning/hubspot-crm-enrichment/directory.md>)

- [prd.md](<planning/hubspot-crm-enrichment/prd.md>) — PRD — HubSpot CRM Enrichment for Customer 360 + Churn: Selected by `rereflect-next` as the highest-leverage next feature. Rereflect's killer feature is "churn prediction that actually works"

## `docs/planning/hubspot-crm-enrichment/crm-health-component`

[Directory guide](<planning/hubspot-crm-enrichment/crm-health-component/directory.md>)

- [_impl-report.md](<planning/hubspot-crm-enrichment/crm-health-component/_impl-report.md>) — Implementation Report — crm-health-component
- [plan_20260630.md](<planning/hubspot-crm-enrichment/crm-health-component/plan_20260630.md>) — Tech Plan — crm-health-component: This aspect wires a sixth health-score component (`crm`) that encodes commercial renewal-proximity risk drawn from the `crm_enrichment` table written by the
- [spec.md](<planning/hubspot-crm-enrichment/crm-health-component/spec.md>) — Aspect Spec — crm-health-component: An operator can opt CRM signal into the health/churn score. By default (weight 0%) nothing changes — existing scores are untouched. When the operator raises

## `docs/planning/hubspot-crm-enrichment/crm-profile-and-timeline`

[Directory guide](<planning/hubspot-crm-enrichment/crm-profile-and-timeline/directory.md>)

- [_impl-report.md](<planning/hubspot-crm-enrichment/crm-profile-and-timeline/_impl-report.md>) — Implementation Report — `crm-profile-and-timeline`: A single enrichment snapshot cannot detect a deal stage *change* — there is no per-sync history table in v1. `crm_contact_synced` and `crm_renewal_upcoming` are the only…
- [plan_20260630.md](<planning/hubspot-crm-enrichment/crm-profile-and-timeline/plan_20260630.md>) — Implementation Plan — `crm-profile-and-timeline`: row and emit these EXACT `Optional` fields (`None` when the row/value is absent): `CustomerProfileResponse` (customers.py) and `PublicCustomerProfile360` (public_api.py)
- [spec.md](<planning/hubspot-crm-enrichment/crm-profile-and-timeline/spec.md>) — Aspect Spec — crm-profile-and-timeline: A CS lead viewing `/customers/{email}` sees a **CRM / Company** card (company, lifecycle stage, ARR, renewal date, primary deal + stage + amount) and CRM events

## `docs/planning/hubspot-crm-enrichment/hubspot-connection`

[Directory guide](<planning/hubspot-crm-enrichment/hubspot-connection/directory.md>)

- [_impl-report.md](<planning/hubspot-crm-enrichment/hubspot-connection/_impl-report.md>) — HubSpot Connection — Implementation Report: Result: **43 passed** (6 plans + 5 model + 32 routes), 0 failed, 0 errors. Backend full regression (entire test suite run separately in previous session):
- [plan_20260630.md](<planning/hubspot-crm-enrichment/hubspot-connection/plan_20260630.md>) — TDD Implementation Plan — hubspot-connection aspect: `services/backend-api/src/utils/encryption.py:14` — `_get_fernet()` raises producing an unhandled 500 on `POST /connect`. The route **must** catch
- [spec.md](<planning/hubspot-crm-enrichment/hubspot-connection/spec.md>) — Aspect Spec — hubspot-connection: An org-admin connects their own HubSpot portal by pasting a private-app access token, can test it, see connection status (with last-synced time + a token hint,

## `docs/planning/hubspot-crm-enrichment/hubspot-sync`

[Directory guide](<planning/hubspot-crm-enrichment/hubspot-sync/directory.md>)

- [_impl-report.md](<planning/hubspot-crm-enrichment/hubspot-sync/_impl-report.md>) — HubSpot Sync — Implementation Report: Result: **4 passed**, 0 failed. (Confirmed during Phase 5 GREEN run; full backend suite not re-run due to ~83s Sentry initialization overhead per isolated run.) The existing…
- [plan_20260630.md](<planning/hubspot-crm-enrichment/hubspot-sync/plan_20260630.md>) — Tech Plan — hubspot-sync: This aspect delivers the data-movement layer of HubSpot CRM enrichment. After the `hubspot-connection` aspect establishes the `hubspot_integrations` table and token encryption, this aspect: Out of scope…
- [spec.md](<planning/hubspot-crm-enrichment/hubspot-sync/spec.md>) — Aspect Spec — hubspot-sync: After connecting, the operator's HubSpot Contacts/Companies/Deals are pulled, matched to Rereflect customers by email, and written to a per-customer enrichment

## `docs/planning/ingestion-source-visibility`

[Directory guide](<planning/ingestion-source-visibility/directory.md>)

- [prd.md](<planning/ingestion-source-visibility/prd.md>) — PRD — Ingestion source visibility: A post-1.0.0 user asked for "Intercom or Zendesk so feedback flows in automatically instead of pasting tickets manually." Zendesk shipped 2026-07-06 and fully satisfies the ask.
- [understanding.md](<planning/ingestion-source-visibility/understanding.md>) — Understanding — ingestion source visibility (Phase 2): It was scoped as "fix the README source list and write the missing Intercom setup docs." The deep dig confirms the docs gap is real, but it is a **symptom**. The actual…

## `docs/planning/ingestion-source-visibility/intercom-setup-docs`

[Directory guide](<planning/ingestion-source-visibility/intercom-setup-docs/directory.md>)

- [plan_20260729.md](<planning/ingestion-source-visibility/intercom-setup-docs/plan_20260729.md>) — Plan — Aspect B: `intercom-setup-docs` (2026-07-29): Write the missing Intercom self-hosting documentation so an operator can connect Intercom end-to-end from committed docs alone, and add the env vars to both example files.

## `docs/planning/ingestion-source-visibility/source-copy-accuracy`

[Directory guide](<planning/ingestion-source-visibility/source-copy-accuracy/directory.md>)

- [plan_20260729.md](<planning/ingestion-source-visibility/source-copy-accuracy/plan_20260729.md>) — Plan — Aspect A: `source-copy-accuracy` (2026-07-29): Correct every public surface that enumerates Rereflect's ingestion sources. (lines 157–221): `slack`, `intercom`, `webhook`, `linear`, `jira`, `zendesk`, `asana`,

## `docs/planning/integration-auth-tenancy-hardening`

[Directory guide](<planning/integration-auth-tenancy-hardening/directory.md>)

- [prd.md](<planning/integration-auth-tenancy-hardening/prd.md>) — PRD — Integration auth & tenancy hardening: Rereflect's inbound webhook path for **Intercom** and **Slack** accepts unauthenticated requests on a default install and, on certain payloads, writes rows attributed to organizations…

## `docs/planning/integration-auth-tenancy-hardening/webhook-auth-tenancy`

[Directory guide](<planning/integration-auth-tenancy-hardening/webhook-auth-tenancy/directory.md>)

- [plan_20260729.md](<planning/integration-auth-tenancy-hardening/webhook-auth-tenancy/plan_20260729.md>) — Implementation plan — `webhook-auth-tenancy`: `alembic heads` must still print exactly one head at the end — assert it, don't assume it. across `worker-service/src` and `analysis-engine/src`. `emit_event` itself is used heavily…
- [spec.md](<planning/integration-auth-tenancy-hardening/webhook-auth-tenancy/spec.md>) — Aspect spec — `webhook-auth-tenancy`: Every unauthenticated write path into Rereflect either accepts unsigned requests by default, or resolves the owning organization from an attacker-supplied field with no fallback, or both. This

## `docs/planning/integration-routes-rbac`

[Directory guide](<planning/integration-routes-rbac/directory.md>)

- [prd.md](<planning/integration-routes-rbac/prd.md>) — PRD — Enforce RBAC on integration routes: (sibling pattern) · feedback-sources writes only · backend-only (UI guards deferred) · The RBAC matrix (CLAUDE.md) grants "Manage integrations" to **Owner / Admin only**.

## `docs/planning/integration-routes-rbac/routes-rbac`

[Directory guide](<planning/integration-routes-rbac/routes-rbac/directory.md>)

- [plan_20260809.md](<planning/integration-routes-rbac/routes-rbac/plan_20260809.md>) — Implementation Plan — `routes-rbac` (2026-08-09): parallel; task D runs after A+B+C land. Integrator (lead) sequences and commits per task. (backend venv exists in the worktree — `.env` copied at worktree creation; if venv is
- [spec.md](<planning/integration-routes-rbac/routes-rbac/spec.md>) — Spec — `routes-rbac` (single aspect): Three backend route modules let a `member`-role user manage integrations via the API (contradicting "Manage integrations: Owner ✅ / Admin ✅ / Member ❌"):

## `docs/planning/intercom-backlog-drain-visibility`

[Directory guide](<planning/intercom-backlog-drain-visibility/directory.md>)

- [prd.md](<planning/intercom-backlog-drain-visibility/prd.md>) — PRD — Intercom backlog drain visibility: A large Intercom backlog drains over **several 20-page runs** (first connect with a big history; the cursor resumes where it stopped each run). The operator has **no

## `docs/planning/intercom-backlog-drain-visibility/client-total-count`

[Directory guide](<planning/intercom-backlog-drain-visibility/client-total-count/directory.md>)

- [plan_20260815.md](<planning/intercom-backlog-drain-visibility/client-total-count/plan_20260815.md>) — Implementation Plan — Client surfaces search `total_count`: Existing codebase — no scaffolding. No new dependencies, no env vars, no migrations, no frontend/backend changes. - Modify…
- [spec.md](<planning/intercom-backlog-drain-visibility/client-total-count/spec.md>) — Aspect spec — Client surfaces search total_count: The sync needs Intercom's per-query `total_count` to compute the remaining-backlog estimate, but `search_conversations` (services/worker-service/src/clients/intercom.py)

## `docs/planning/intercom-backlog-drain-visibility/db-status-api`

[Directory guide](<planning/intercom-backlog-drain-visibility/db-status-api/directory.md>)

- [plan_20260815.md](<planning/intercom-backlog-drain-visibility/db-status-api/plan_20260815.md>) — Implementation Plan — intercom-backlog-drain-visibility `db-status-api` (R3 + R4): dependencies, no scaffolding. This aspect adds one nullable ORM column, one Alembic migration off the single head, the worker model-mirror column…
- [spec.md](<planning/intercom-backlog-drain-visibility/db-status-api/spec.md>) — Aspect spec — Column, migration, mirrors, status API: The estimate needs storage (one nullable column), a migration off the single head, both model mirrors with the parity type-tuple fix, and a status-API field so the frontend

## `docs/planning/intercom-backlog-drain-visibility/docs-tracking-changelog`

[Directory guide](<planning/intercom-backlog-drain-visibility/docs-tracking-changelog/directory.md>)

- [plan_20260815.md](<planning/intercom-backlog-drain-visibility/docs-tracking-changelog/plan_20260815.md>) — Implementation Plan — docs-tracking-changelog (aspect 5 of 5, close-out, runs last): `sync-estimate`, `db-status-api`, `frontend-remaining-row`) have merged into the branch. Merge facts are **placeholders** in this plan (`(merged…
- [spec.md](<planning/intercom-backlog-drain-visibility/docs-tracking-changelog/spec.md>) — Aspect spec — Docs, changelog & tracking markers: The feature adds an operator-visible number with honest semantics that must be documented, and closes the last unblocked Intercom deferred-v2 entry.

## `docs/planning/intercom-backlog-drain-visibility/frontend-remaining-row`

[Directory guide](<planning/intercom-backlog-drain-visibility/frontend-remaining-row/directory.md>)

- [plan_20260815.md](<planning/intercom-backlog-drain-visibility/frontend-remaining-row/plan_20260815.md>) — Implementation Plan — frontend-remaining-row (aspect 4, R5): `app/(dashboard)/settings/integrations/intercom/page.tsx` (dl grid :178-203, ingested row :199-202, zero-ingested alert :212-224, writeback card mount :238-240),…
- [spec.md](<planning/intercom-backlog-drain-visibility/frontend-remaining-row/spec.md>) — Aspect spec — Frontend "≈ N remaining" row: The Connection card on the Intercom settings page must render the drain estimate honestly — only when it exists and is positive — without contradicting the existing

## `docs/planning/intercom-backlog-drain-visibility/sync-estimate`

[Directory guide](<planning/intercom-backlog-drain-visibility/sync-estimate/directory.md>)

- [plan_20260815.md](<planning/intercom-backlog-drain-visibility/sync-estimate/plan_20260815.md>) — Implementation Plan — sync-estimate: repo's venv works against the worktree — `services/worker-service/tests/test_intercom_sync.py` → with `/Users/aliz/dev/at/rereflect/services/worker-service/venv/bin/pytest` (pull-enrichment
- [spec.md](<planning/intercom-backlog-drain-visibility/sync-estimate/spec.md>) — Aspect spec — Sync computes + persists the estimate: `_sync_org` must compute `max(0, total_count − conversations_seen)` after the loop and `_sync_intercom_org_body` must persist it — and the error paths must reset it so a

## `docs/planning/intercom-pull-replies-and-ratings`

[Directory guide](<planning/intercom-pull-replies-and-ratings/directory.md>)

- [prd.md](<planning/intercom-pull-replies-and-ratings/prd.md>) — PRD — Intercom pull: replies & ratings enrichment: The Intercom **15-minute pull ingests the first message of a conversation only** (intercom_sync.py D3; pull-sync/spec.md:65-66). Replies and ratings were assumed to

## `docs/planning/intercom-pull-replies-and-ratings/adapter-reply-rating-extraction`

[Directory guide](<planning/intercom-pull-replies-and-ratings/adapter-reply-rating-extraction/directory.md>)

- [plan_20260815.md](<planning/intercom-pull-replies-and-ratings/adapter-reply-rating-extraction/plan_20260815.md>) — Implementation Plan — Adapter: reply & rating extraction + merge: Existing codebase — no scaffolding, no new dependencies, no env vars, no migrations. - Create `services/worker-service/tests/test_intercom_parts.py`
- [spec.md](<planning/intercom-pull-replies-and-ratings/adapter-reply-rating-extraction/spec.md>) — Aspect spec — Adapter: reply & rating extraction + merge: The pull must turn fetched conversation parts into content the sync task can merge into the existing per-conversation FeedbackItem, idempotently and without corrupting…

## `docs/planning/intercom-pull-replies-and-ratings/client-conversation-parts`

[Directory guide](<planning/intercom-pull-replies-and-ratings/client-conversation-parts/directory.md>)

- [plan_20260815.md](<planning/intercom-pull-replies-and-ratings/client-conversation-parts/plan_20260815.md>) — Implementation Plan — Client conversation-parts access: Existing codebase — no scaffolding. No new dependencies, no env vars, no migrations. - Modify…
- [spec.md](<planning/intercom-pull-replies-and-ratings/client-conversation-parts/spec.md>) — Aspect spec — Client conversation-parts access: The pull needs the conversation's reply parts + rating. Search results carry only the first message (`test_intercom_sync.py:89-107` fixture shape). The client

## `docs/planning/intercom-pull-replies-and-ratings/docs-tracking-changelog`

[Directory guide](<planning/intercom-pull-replies-and-ratings/docs-tracking-changelog/directory.md>)

- [plan_20260815.md](<planning/intercom-pull-replies-and-ratings/docs-tracking-changelog/plan_20260815.md>) — Implementation Plan — docs-tracking-changelog (aspect 5 of 5, close-out, runs last): `adapter-reply-rating-extraction`, `pull-enrichment`, `reanalysis-seam`) have merged into the branch. This plan's placeholders (merge sha, PR…
- [spec.md](<planning/intercom-pull-replies-and-ratings/docs-tracking-changelog/spec.md>) — Aspect spec — Docs, changelog & tracking markers: The feature flips several shipped claims ("first message only / replies via webhook only") and corrects one pre-existing falsehood (OAuth orgs do not get pull sync). Docs

## `docs/planning/intercom-pull-replies-and-ratings/pull-enrichment`

[Directory guide](<planning/intercom-pull-replies-and-ratings/pull-enrichment/directory.md>)

- [plan_20260815.md](<planning/intercom-pull-replies-and-ratings/pull-enrichment/plan_20260815.md>) — Implementation Plan — pull-enrichment: main repo's venv works against the worktree — `services/worker-service/tests/test_intercom_sync.py` → **19 passed** with…
- [spec.md](<planning/intercom-pull-replies-and-ratings/pull-enrichment/spec.md>) — Aspect spec — Pull enrichment integration: The `_sync_org` pull loop (`services/worker-service/src/tasks/intercom_sync.py:111-214`) must fetch parts for the conversations it sees, merge new reply content into the

## `docs/planning/intercom-pull-replies-and-ratings/reanalysis-seam`

[Directory guide](<planning/intercom-pull-replies-and-ratings/reanalysis-seam/directory.md>)

- [plan_20260815.md](<planning/intercom-pull-replies-and-ratings/reanalysis-seam/plan_20260815.md>) — Implementation Plan — `reanalysis-seam` (2026-08-15): - New seam file: `cd services/worker-service && ./venv/bin/pytest tests/test_reanalysis_seam.py -v` - Full worker suite: `cd services/worker-service && ./venv/bin/pytest…
- [spec.md](<planning/intercom-pull-replies-and-ratings/reanalysis-seam/spec.md>) — Aspect spec — Re-analysis seam (verify + reuse): Enriched items must be re-analyzed so sentiment/categories/churn reflect the full thread — but the analysis task skips already-analyzed items by default

## `docs/planning/intercom-selfhost-ingestion`

[Directory guide](<planning/intercom-selfhost-ingestion/directory.md>)

- [prd.md](<planning/intercom-selfhost-ingestion/prd.md>) — PRD — Intercom ingestion, operable on a self-host: the landing page, and documented in `docs/SELF_HOSTING.md:1571`. A self-hoster can click Connect, complete an OAuth flow, see webhook events arrive — and never get a single

## `docs/planning/intercom-selfhost-ingestion/cleanup-and-docs`

[Directory guide](<planning/intercom-selfhost-ingestion/cleanup-and-docs/directory.md>)

- [spec.md](<planning/intercom-selfhost-ingestion/cleanup-and-docs/spec.md>) — Aspect Spec — `cleanup-and-docs`: `BaseConnector` / `IntercomConnector` / `ZendeskConnector`, all `return []` stubs carrying "TODO: implement in Month 2", plus `sync_all_integrations`, which was **on the daily beat**

## `docs/planning/intercom-selfhost-ingestion/envelope-seam-fix`

[Directory guide](<planning/intercom-selfhost-ingestion/envelope-seam-fix/directory.md>)

- [plan_20260731.md](<planning/intercom-selfhost-ingestion/envelope-seam-fix/plan_20260731.md>) — Implementation Plan — `envelope-seam-fix`: 3. Confirm `IntercomConnector.fetch_new_items` returns `[]` and creates nothing (`worker-service/src/tasks/integrations.py:170-177`) — it is deleted in a later aspect.
- [spec.md](<planning/intercom-selfhost-ingestion/envelope-seam-fix/spec.md>) — Aspect Spec — `envelope-seam-fix`: Intercom webhook deliveries are received and authenticated, but produce **no feedback item, in any release**. The backend route hands the worker adapter a payload shape the

## `docs/planning/intercom-selfhost-ingestion/pull-sync`

[Directory guide](<planning/intercom-selfhost-ingestion/pull-sync/directory.md>)

- [spec.md](<planning/intercom-selfhost-ingestion/pull-sync/spec.md>) — Aspect Spec — `pull-sync`: The originating user ask was for feedback to "flow in automatically instead of pasting tickets manually" — the **pull** path. Intercom had none: `IntercomConnector.fetch_new_items`

## `docs/planning/intercom-selfhost-ingestion/tenancy-discriminator`

[Directory guide](<planning/intercom-selfhost-ingestion/tenancy-discriminator/directory.md>)

- [spec.md](<planning/intercom-selfhost-ingestion/tenancy-discriminator/spec.md>) — Aspect Spec — `tenancy-discriminator`: `token-paste-connect` shipped a working connect flow that **ingests nothing**. `_find_matching_sources` (`services/worker-service/src/tasks/source_events.py`) resolves an

## `docs/planning/intercom-selfhost-ingestion/token-paste-connect`

[Directory guide](<planning/intercom-selfhost-ingestion/token-paste-connect/directory.md>)

- [plan_20260731.md](<planning/intercom-selfhost-ingestion/token-paste-connect/plan_20260731.md>) — Implementation Plan — `token-paste-connect`: `tests/test_zendesk_integration.py`. Mock the Intercom client at the module boundary the route imports, exactly as the Zendesk tests mock `ZendeskClient`.
- [spec.md](<planning/intercom-selfhost-ingestion/token-paste-connect/spec.md>) — Aspect Spec — `token-paste-connect`: Intercom connect is OAuth-only. `routes/integrations.py:981-984` returns **403 "Intercom OAuth is not configured. Set INTERCOM_CLIENT_ID environment variable"**, and a self-hoster

## `docs/planning/intercom-selfhost-ingestion/webhook-per-org-secret`

[Directory guide](<planning/intercom-selfhost-ingestion/webhook-per-org-secret/directory.md>)

- [spec.md](<planning/intercom-selfhost-ingestion/webhook-per-org-secret/spec.md>) — Aspect Spec — `webhook-per-org-secret`: True while OAuth was the only connect path. **Token-paste dissolves it:** obtaining an Access Token requires creating a Developer Hub app, and that app's Client Secret is exactly

## `docs/planning/intercom-webhook-reply-rating`

[Directory guide](<planning/intercom-webhook-reply-rating/directory.md>)

- [prd.md](<planning/intercom-webhook-reply-rating/prd.md>) — PRD — Intercom webhook reply/rating enrichment: follow-up defect note from #16 (DEV-TRACKING.md:518-522) The Intercom **webhook reply/rating path is inert** — and has been since the

## `docs/planning/intercom-webhook-reply-rating/core-branch-dispatch`

[Directory guide](<planning/intercom-webhook-reply-rating/core-branch-dispatch/directory.md>)

- [plan_20260816.md](<planning/intercom-webhook-reply-rating/core-branch-dispatch/plan_20260816.md>) — Implementation Plan — core-branch-dispatch: main repo's venv works against the worktree — `services/worker-service/tests/test_intercom_sync.py` is the precedent. Use…
- [spec.md](<planning/intercom-webhook-reply-rating/core-branch-dispatch/spec.md>) — Aspect spec — Core branch + enriched status + post-commit dispatch: The shared core (`source_events.py`) must route intercom replied/rating events into the enrichment module instead of the trigger/dedup/create path, log them with…

## `docs/planning/intercom-webhook-reply-rating/docs-tracking-changelog`

[Directory guide](<planning/intercom-webhook-reply-rating/docs-tracking-changelog/directory.md>)

- [plan_20260816.md](<planning/intercom-webhook-reply-rating/docs-tracking-changelog/plan_20260816.md>) — Implementation Plan — docs-tracking-changelog (aspect 4 of 4, close-out, runs last): `webhook-enrich-module`, `golden-fixtures-route-pins`) have merged into the branch. This plan's placeholders (merge sha, PR number, merge date)…
- [spec.md](<planning/intercom-webhook-reply-rating/docs-tracking-changelog/spec.md>) — Aspect spec — Docs, changelog & tracking markers: The feature flips the honest-limits claims from #16 ("the webhook's replied/rating events are still dedup-inert — flagged follow-up, not fixed") and closes the

## `docs/planning/intercom-webhook-reply-rating/golden-fixtures-route-pins`

[Directory guide](<planning/intercom-webhook-reply-rating/golden-fixtures-route-pins/directory.md>)

- [plan_20260816.md](<planning/intercom-webhook-reply-rating/golden-fixtures-route-pins/plan_20260816.md>) — Implementation Plan — `golden-fixtures-route-pins`: deliverables are two cross-service fixtures, their raise-if-missing loaders in both suites, the backend replied/rating route kwargs pins, and one worker seam test that pins
- [spec.md](<planning/intercom-webhook-reply-rating/golden-fixtures-route-pins/spec.md>) — Aspect spec — Golden fixtures + route kwargs pins: conversation id; parts at conversation_parts.conversation_parts[]; rating at conversation_rating). Nothing pins that shape today (only `created` has a golden

## `docs/planning/intercom-webhook-reply-rating/webhook-enrich-module`

[Directory guide](<planning/intercom-webhook-reply-rating/webhook-enrich-module/directory.md>)

- [plan_20260816.md](<planning/intercom-webhook-reply-rating/webhook-enrich-module/plan_20260816.md>) — Implementation plan — Webhook enrichment module: A new worker service-layer module that turns a `conversation.user.replied` / `conversation.rating.added` webhook event into a **merge into the existing
- [spec.md](<planning/intercom-webhook-reply-rating/webhook-enrich-module/spec.md>) — Aspect spec — Webhook enrichment module: A seam-tested module that turns a replied/rating webhook event into a merge into the existing per-conversation FeedbackItem — conversation id extraction, item lookup,

## `docs/planning/intercom-writeback`

[Directory guide](<planning/intercom-writeback/directory.md>)

- [prd.md](<planning/intercom-writeback/prd.md>) — PRD — Intercom write-back (close the loop on resolve): `services/backend-api/src/services/intercom_service.py` — `add_note_to_conversation`, `close_conversation`, `get_admin_id` — has **zero production callers** anywhere in the

## `docs/planning/intercom-writeback/config-api-routes`

[Directory guide](<planning/intercom-writeback/config-api-routes/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/config-api-routes/plan_20260815.md>) — Implementation Plan — Write-back config API routes: Existing codebase — no scaffolding. No new dependencies, no env vars, no migration (the migration belongs to `db-config-model`). - Modify…
- [spec.md](<planning/intercom-writeback/config-api-routes/spec.md>) — Aspect spec — Write-back config API routes: Operators need a programmatic + UI surface to flip the opt-in toggle and read the write-back's honest state. Today the Intercom router has exactly three routes

## `docs/planning/intercom-writeback/db-config-model`

[Directory guide](<planning/intercom-writeback/db-config-model/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/db-config-model/plan_20260815.md>) — Implementation Plan — intercom-writeback `db-config-model` (R1 + R4): dependencies, no scaffolding. This aspect only adds ORM columns, one Alembic migration, and worker model-mirror columns with a parity test — everything already…
- [spec.md](<planning/intercom-writeback/db-config-model/spec.md>) — Aspect spec — DB config & model changes: The write-back needs a per-org opt-in switch with honest status readout (R1) and a durable per-feedback idempotency marker (R4). Nothing exists today: the token-paste

## `docs/planning/intercom-writeback/dispatch-seams`

[Directory guide](<planning/intercom-writeback/dispatch-seams/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/dispatch-seams/plan_20260815.md>) — Plan — dispatch-seams: `services/worker-service` (2 writer dispatches + name-consistency test). Frontend and `FeedbackItem.source` / `workflow_status` only and never touches
- [spec.md](<planning/intercom-writeback/dispatch-seams/spec.md>) — Aspect spec — Dispatch seams (5 call sites + timeline fetcher): The write-back only works if **every** writer that can move an Intercom-sourced item to `resolved` dispatches the task. The repo has shipped this bug class four times

## `docs/planning/intercom-writeback/docs-tracking-changelog`

[Directory guide](<planning/intercom-writeback/docs-tracking-changelog/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/docs-tracking-changelog/plan_20260815.md>) — Implementation Plan — docs-tracking-changelog (aspect 6, close-out, runs last): `config-api-routes`, `dispatch-seams`, `worker-write-client`, `worker-writeback-task`, `frontend-writeback-card`) have merged into the branch. This…
- [spec.md](<planning/intercom-writeback/docs-tracking-changelog/spec.md>) — Aspect spec — Docs, changelog & tracking markers: The feature ships with honesty obligations: flip the operator-facing "No write-back" statement, record the claim discipline ("Two-Way Sync" returns only as what shipped),

## `docs/planning/intercom-writeback/frontend-writeback-card`

[Directory guide](<planning/intercom-writeback/frontend-writeback-card/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/frontend-writeback-card/plan_20260815.md>) — Implementation Plan — frontend-writeback-card: All paths relative to the worktree root; everything under `services/frontend-web/`. Required, not optional — HubSpot's writeback fields are required in its status type; the…
- [spec.md](<planning/intercom-writeback/frontend-writeback-card/spec.md>) — Aspect spec — Frontend write-back card: Operators need to see and control the write-back where they already manage the Intercom connection: Settings → Integrations → Intercom. Today that page

## `docs/planning/intercom-writeback/worker-write-client`

[Directory guide](<planning/intercom-writeback/worker-write-client/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/worker-write-client/plan_20260815.md>) — Implementation Plan — Worker Intercom write client: Existing codebase — no scaffolding. No new dependencies, no env vars, no migrations. - Modify `services/worker-service/src/clients/intercom.py`
- [spec.md](<planning/intercom-writeback/worker-write-client/spec.md>) — Aspect spec — Worker Intercom write client: The write-back needs outbound Intercom calls with the worker's proper error taxonomy. Today the only implementation is the orphaned backend `intercom_service.py`

## `docs/planning/intercom-writeback/worker-writeback-task`

[Directory guide](<planning/intercom-writeback/worker-writeback-task/directory.md>)

- [plan_20260815.md](<planning/intercom-writeback/worker-writeback-task/plan_20260815.md>) — Implementation plan — Worker write-back task: Build the core execution unit of the Intercom write-back: a Celery task that, given an org and a list of feedback ids that just transitioned to `resolved`, appends a note to
- [spec.md](<planning/intercom-writeback/worker-writeback-task/spec.md>) — Aspect spec — Worker write-back task: The core execution unit: given an org + the feedback ids that just transitioned to `resolved`, append a note to each linked Intercom conversation and close it — guarded,

## `docs/planning/jira-integration`

[Directory guide](<planning/jira-integration/directory.md>)

- [prd.md](<planning/jira-integration/prd.md>) — PRD — Jira Cloud Integration (slice 1): Rereflect can turn a piece of feedback into an issue in **Linear**, but not in **Jira** — the most widely deployed enterprise issue tracker and the next pending integration in the backlog

## `docs/planning/jira-integration/backend-connection`

[Directory guide](<planning/jira-integration/backend-connection/directory.md>)

- [plan_20260704.md](<planning/jira-integration/backend-connection/plan_20260704.md>) — Implementation Plan — backend-connection (Jira Cloud Integration): one migration, and edits two existing files. No new dependencies (`httpx`, `cryptography` already present).…
- [spec.md](<planning/jira-integration/backend-connection/spec.md>) — Aspect Spec — backend-connection: The foundation of the Jira integration: an operator can connect one Jira Cloud site per org with a pasted **email + Atlassian API token** (Basic auth), have it validated + encrypted + stored, and

## `docs/planning/jira-integration/backend-create-issue`

[Directory guide](<planning/jira-integration/backend-create-issue/directory.md>)

- [spec.md](<planning/jira-integration/backend-create-issue/spec.md>) — Aspect Spec — backend-create-issue: Turn a feedback item into a Jira issue. The backend exposes the project/issue-type pickers the wizard needs and the create endpoint that actually files the issue, stores the link, and records a…

## `docs/planning/jira-integration/frontend`

[Directory guide](<planning/jira-integration/frontend/directory.md>)

- [spec.md](<planning/jira-integration/frontend/spec.md>) — Aspect Spec — frontend: The operator- and user-facing surface in the dashboard app: connect Jira from Settings, create a Jira issue from a feedback item, and see Jira as a source option. Outcome: token-paste connect works,

## `docs/planning/jira-integration/landing`

[Directory guide](<planning/jira-integration/landing/directory.md>)

- [spec.md](<planning/jira-integration/landing/spec.md>) — Aspect Spec — landing: Keep the public integrations story accurate and give self-hosters the setup steps to mint an Atlassian API token. Outcome: a `/integrations/jira` marketing page renders (data-driven) and operator setup

## `docs/planning/jira-integration/source-type-registration`

[Directory guide](<planning/jira-integration/source-type-registration/directory.md>)

- [spec.md](<planning/jira-integration/source-type-registration/spec.md>) — Aspect Spec — source-type-registration: Make `jira` a **selectable** feedback-source type (own-auth, like Linear) so it appears in the source wizard. This is *registration only* — NO inbound Jira→feedback ingestion. Outcome: `GET

## `docs/planning/jira-status-sync`

[Directory guide](<planning/jira-status-sync/directory.md>)

- [prd.md](<planning/jira-status-sync/prd.md>) — PRD — Jira Inbound Status-Sync (close the integration loop): Rereflect's Jira integration (slice 1, shipped 2026-07-05) is **outbound-only**: it creates a Jira issue from a feedback item and records the link in…

## `docs/planning/jira-status-sync/inbound-status-sync`

[Directory guide](<planning/jira-status-sync/inbound-status-sync/directory.md>)

- [plan_20260711.md](<planning/jira-status-sync/inbound-status-sync/plan_20260711.md>) — Implementation Plan — jira-status-sync / inbound-status-sync: `feedback_jira_issues`. **CORRECTED (verified live during Phase 1):** the real current head is a already has descendants and `k2l3m4n5o6p7` is taken by the Salesforce…
- [spec.md](<planning/jira-status-sync/inbound-status-sync/spec.md>) — Aspect spec — inbound-status-sync: For an org that opts in, a linked Jira issue moving status category (To Do / In Progress / Done) automatically updates the linked Rereflect feedback item's `workflow_status`, with a timeline…

## `docs/planning/linear-webhook-secret-encryption`

[Directory guide](<planning/linear-webhook-secret-encryption/directory.md>)

- [prd.md](<planning/linear-webhook-secret-encryption/prd.md>) — PRD — Encrypt Linear webhook secret at rest: Linear's `webhook_secret` — the HMAC key that authenticates inbound Linear webhook deliveries — is stored in plaintext in the database on every self-hosted install.

## `docs/planning/linear-webhook-secret-encryption/webhook-secret-encryption`

[Directory guide](<planning/linear-webhook-secret-encryption/webhook-secret-encryption/directory.md>)

- [plan_20260809.md](<planning/linear-webhook-secret-encryption/webhook-secret-encryption/plan_20260809.md>) — Implementation Plan — Linear webhook-secret encryption at rest: `services/backend-api` (`pytest tests/ -v`). One commit per phase. Branch stays green. the current sole head `c7d8e9f0a1b2`; `alembic heads` must print exactly one…
- [spec.md](<planning/linear-webhook-secret-encryption/webhook-secret-encryption/spec.md>) — Spec — Webhook-secret encryption (Linear): Linear's `webhook_secret` (the HMAC key for inbound webhook auth) is the last plaintext credential in the system. After this aspect: it is Fernet-encrypted at rest on every path

## `docs/planning/local-analyzer-sentiment-model`

[Directory guide](<planning/local-analyzer-sentiment-model/directory.md>)

- [prd.md](<planning/local-analyzer-sentiment-model/prd.md>) — PRD — Local Analyzer Sentiment Model (M5.1 spine v1): Rereflect scores sentiment with **VADER only** (`analysis-engine/src/analyzer/sentiment.py`), a fixed lexicon that cannot improve and misreads negation, sarcasm, and domain…

## `docs/planning/local-analyzer-sentiment-model/eval-harness-and-card`

[Directory guide](<planning/local-analyzer-sentiment-model/eval-harness-and-card/directory.md>)

- [plan_20260710.md](<planning/local-analyzer-sentiment-model/eval-harness-and-card/plan_20260710.md>) — Implementation Plan — eval-harness-and-card: `frontend-web` only for the card (component + API client + settings-page wiring). classes (built by `sentiment-provider-core`), it does not modify them.
- [spec.md](<planning/local-analyzer-sentiment-model/eval-harness-and-card/spec.md>) — Aspect Spec — eval-harness-and-card: (hard dep: needs both `VaderSentimentProvider` and `TransformerSentimentProvider` importable), soft-depends on `model-packaging` (transformer deps must actually be installed to run the model

## `docs/planning/local-analyzer-sentiment-model/m5.0-readiness-report`

[Directory guide](<planning/local-analyzer-sentiment-model/m5.0-readiness-report/directory.md>)

- [plan_20260710.md](<planning/local-analyzer-sentiment-model/m5.0-readiness-report/plan_20260710.md>) — Implementation Plan — m5.0-readiness-report (2026-07-10): is **independent** of the sentiment-provider-core / per-org-resolution / model-packaging / eval-harness-and-card aspects — no ML, no `analysis-engine` changes, no…
- [spec.md](<planning/local-analyzer-sentiment-model/m5.0-readiness-report/spec.md>) — Aspect Spec — m5.0-readiness-report: `per-org-resolution`, `model-packaging`, or `eval-harness-and-card`. Can be built fully in parallel; owns PRD must-have #8 and `AI-TRACKING.md:313` (M5.0 — Data & Model Readiness Assessment,…

## `docs/planning/local-analyzer-sentiment-model/model-packaging`

[Directory guide](<planning/local-analyzer-sentiment-model/model-packaging/directory.md>)

- [plan_20260710.md](<planning/local-analyzer-sentiment-model/model-packaging/plan_20260710.md>) — Implementation Plan — model-packaging: aspect ships no Python application logic — `docker build` + smoke-test scripts are the tests). `services/backend-api` (requirements.txt, Dockerfile), root `docker-compose.yml` +
- [spec.md](<planning/local-analyzer-sentiment-model/model-packaging/spec.md>) — Aspect Spec — model-packaging: (needs its final model id + pinned revision to finish the pre-bake command), but can be **built in parallel**: every phase here is Docker/deps/docs work with no import of provider code.

## `docs/planning/local-analyzer-sentiment-model/per-org-resolution`

[Directory guide](<planning/local-analyzer-sentiment-model/per-org-resolution/directory.md>)

- [plan_20260710.md](<planning/local-analyzer-sentiment-model/per-org-resolution/plan_20260710.md>) — Tech Plan — per-org-resolution: (backend); `src/llm/org_resolver.py` (worker); `c3d4e5f6a7b8_add_crm_health_component.py` (migration shape); `worker-service/tests/test_keyword_analysis.py` (call-site mocking pattern).
- [spec.md](<planning/local-analyzer-sentiment-model/per-org-resolution/spec.md>) — Aspect Spec — per-org-resolution: `SentimentProviderFactory`). Can be built in parallel with `model-packaging` and Today both sentiment call sites — the worker's async pipeline

## `docs/planning/local-analyzer-sentiment-model/sentiment-provider-core`

[Directory guide](<planning/local-analyzer-sentiment-model/sentiment-provider-core/directory.md>)

- [plan_20260710.md](<planning/local-analyzer-sentiment-model/sentiment-provider-core/plan_20260710.md>) — Implementation Plan — sentiment-provider-core: `services/analysis-engine/src/analyzer/sentiment.py:29-64` today: 7 keys, in this exact order: `compound, pos, neu, neg, label, is_extreme, churn_risk`. Floats are
- [spec.md](<planning/local-analyzer-sentiment-model/sentiment-provider-core/spec.md>) — Aspect Spec — sentiment-provider-core: `per-org-resolution`, `model-packaging`, and `eval-harness-and-card`. Today `analysis-engine/src/analyzer/sentiment.py` hardwires VADER: `SentimentAnalyzer.__init__`

## `docs/planning/local-embedding-quality`

[Directory guide](<planning/local-embedding-quality/directory.md>)

- [prd.md](<planning/local-embedding-quality/prd.md>) — PRD — Local Embedding Quality (M5.4): Rereflect's AI Copilot matches a user's natural-language question against stored **query templates** (canned SQL) using embeddings, and only falls through to LLM NL→SQL when no template…
- [understanding.md](<planning/local-embedding-quality/understanding.md>) — Phase 2 Understanding — local-embedding-quality (M5.4): AI Copilot's template matching — the quality dimension that `local-embeddings-offline-copilot` deliberately deferred (that initiative shipped the plumbing and stated…

## `docs/planning/local-embedding-quality/in-process-provider`

[Directory guide](<planning/local-embedding-quality/in-process-provider/directory.md>)

- [plan_20260725.md](<planning/local-embedding-quality/in-process-provider/plan_20260725.md>) — Implementation Plan — in-process-provider (Aspect 2): Add a genuinely in-process, CPU, air-gappable embedding provider `local` (sentence-transformers), strictly opt-in, plugged into the existing provider abstraction. Byte-stable:…
- [spec.md](<planning/local-embedding-quality/in-process-provider/spec.md>) — Aspect spec — in-process-provider: Today "local" embeddings require an external Ollama/vLLM server (the `ollama`/`openai_compatible` HTTP path). There is no CPU, in-process, air-gappable embedding provider. Outcome: a self-hosting

## `docs/planning/local-embedding-quality/offline-packaging`

[Directory guide](<planning/local-embedding-quality/offline-packaging/directory.md>)

- [plan_20260725.md](<planning/local-embedding-quality/offline-packaging/plan_20260725.md>) — Implementation Plan — offline-packaging (Aspect 4): Make the in-process `bge-small-en-v1.5` embedding model air-gap-capable and lean-by-default, exactly `CHANGELOG.md` entry, and mark **M5.4 COMPLETE** in `AI-TRACKING.md`.
- [spec.md](<planning/local-embedding-quality/offline-packaging/spec.md>) — Aspect spec — offline-packaging: The in-process local model must run air-gapped and must not bloat the default image for operators who never opt in. Mirror the M5.1 `model-packaging` pattern. Outcome: default builds pull zero…

## `docs/planning/local-embedding-quality/ollama-default-bump`

[Directory guide](<planning/local-embedding-quality/ollama-default-bump/directory.md>)

- [plan_20260725.md](<planning/local-embedding-quality/ollama-default-bump/plan_20260725.md>) — Implementation Plan — ollama-default-bump (Aspect 5): Make the recommended Ollama embedding model (for operators who run the external Ollama server path) (`mxbai-embed-large`, `bge-m3`) against the current default…
- [spec.md](<planning/local-embedding-quality/ollama-default-bump/spec.md>) — Aspect spec — ollama-default-bump: Operators who already run Ollama use `nomic-embed-text` (the current default recommendation). The retrieval eval (Aspect 3) can also score stronger Ollama models, so we can make an…

## `docs/planning/local-embedding-quality/retrieval-eval-card`

[Directory guide](<planning/local-embedding-quality/retrieval-eval-card/directory.md>)

- [plan_20260725.md](<planning/local-embedding-quality/retrieval-eval-card/plan_20260725.md>) — Implementation Plan — retrieval-eval-card (Aspect 3): Mirror the M5.1 sentiment eval (`scripts/eval_sentiment.py` + `eval_results/*.json` + read-only `/…/accuracy` endpoint + a frontend accuracy card). Here the domain is…
- [spec.md](<planning/local-embedding-quality/retrieval-eval-card/spec.md>) — Aspect spec — retrieval-eval-card: "Better local embedding model" is only credible with honest, reproducible proof. Mirror the M5.1 sentiment eval-harness-and-card pattern for **retrieval**. Outcome: an operator opens the AI…

## `docs/planning/local-embedding-quality/staleness-model-key`

[Directory guide](<planning/local-embedding-quality/staleness-model-key/directory.md>)

- [plan_20260724.md](<planning/local-embedding-quality/staleness-model-key/plan_20260724.md>) — Implementation Plan — staleness-model-key (Aspect 1): Today the template matcher's cross-space skip-filter keys on `(embedding_provider, embedding_dimension)` only. A model change under the same provider+dimension silently…
- [spec.md](<planning/local-embedding-quality/staleness-model-key/spec.md>) — Aspect spec — staleness-model-key: `TemplateMatcher.find_match` skip-filters stored template vectors on `(embedding_provider, embedding_dimension)` only — not the model. Any embedding-model change under the same provider string

## `docs/planning/local-embeddings-offline-copilot`

[Directory guide](<planning/local-embeddings-offline-copilot/directory.md>)

- [prd.md](<planning/local-embeddings-offline-copilot/prd.md>) — PRD — Local Embeddings & Fully-Offline AI Copilot: Rereflect pivoted to open-source, self-hosted, BYOK/local-LLM (MIT, all features unlocked). The analysis pipeline already runs **fully offline** — Ollama or any

## `docs/planning/local-embeddings-offline-copilot/copilot-llm-local`

[Directory guide](<planning/local-embeddings-offline-copilot/copilot-llm-local/directory.md>)

- [plan_20260628.md](<planning/local-embeddings-offline-copilot/copilot-llm-local/plan_20260628.md>) — Implementation Plan — copilot-llm-local: sequenced **after** `template-matching-local` (both edit `copilot_ws.py`; this aspect rewrites the the generation calls), the LLM-calling generators (`SQLGenerator` and the analysis/report
- [spec.md](<planning/local-embeddings-offline-copilot/copilot-llm-local/spec.md>) — Aspect Spec — copilot-llm-local: A keyless local-LLM org can open the Copilot and get end-to-end answers. The Copilot's answer-generation (NL→SQL, analysis, reports) routes through the local-capable provider

## `docs/planning/local-embeddings-offline-copilot/embedding-provider-layer`

[Directory guide](<planning/local-embeddings-offline-copilot/embedding-provider-layer/directory.md>)

- [plan_20260628.md](<planning/local-embeddings-offline-copilot/embedding-provider-layer/plan_20260628.md>) — Implementation Plan — embedding-provider-layer: `template_matcher.py`); Google uses the existing provider dependency if present, else add `google-generativeai` to `services/backend-api/requirements.txt` **only if** not already
- [spec.md](<planning/local-embeddings-offline-copilot/embedding-provider-layer/spec.md>) — Aspect Spec — embedding-provider-layer: A pluggable embeddings abstraction in **backend-api** (the Copilot's home) that produces a `list[float]` from text via the org's configured provider — local/keyless or cloud BYOK —

## `docs/planning/local-embeddings-offline-copilot/template-matching-local`

[Directory guide](<planning/local-embeddings-offline-copilot/template-matching-local/directory.md>)

- [plan_20260628.md](<planning/local-embeddings-offline-copilot/template-matching-local/plan_20260628.md>) — Implementation Plan — template-matching-local: `models/query_template_mapping.py`, `api/main.py` (lifespan seeding), and the matching-side calls in `api/routes/copilot_ws.py` (L557-560 `find_match`, L788-798 `save_template`).
- [spec.md](<planning/local-embeddings-offline-copilot/template-matching-local/spec.md>) — Aspect Spec — template-matching-local: The Copilot's query→template fast-path generates and compares embeddings via the new provider layer instead of a hardcoded OpenAI client, with provider/dimension-aware storage

## `docs/planning/mutation-route-rbac`

[Directory guide](<planning/mutation-route-rbac/directory.md>)

- [plan_index_20261002.md](<planning/mutation-route-rbac/plan_index_20261002.md>) — Execution order: Tasks 2 and 3 are independent and can be dispatched as parallel agents after 1 is merged on the branch; each agent works strict TDD (RED test first, commit RED, then GREEN). Shared-file caution: backend-gating…
- [prd.md](<planning/mutation-route-rbac/prd.md>) — PRD: Mutation-route RBAC: Of 190 in-scope mutation routes in `services/backend-api/src/api/routes/`, 64 carry no role check. Where a `require_feature(...)` gate exists it is not a role gate and always passes under `SELF_HOSTED`…

## `docs/planning/mutation-route-rbac/backend-gating`

[Directory guide](<planning/mutation-route-rbac/backend-gating/directory.md>)

- [plan_20261002.md](<planning/mutation-route-rbac/backend-gating/plan_20261002.md>) — Plan: backend-gating (2026-10-02): Source: `../prd.md` R1/R2/R4, `spec.md`. Work in `services/backend-api`; venv must be `python3.12` (see memory: system python3 is 3.9). Verify `venv/pyvenv.cfg` first. Also add member-success…
- [spec.md](<planning/mutation-route-rbac/backend-gating/spec.md>) — Aspect: backend-gating (PRD R1, R2, R4)

## `docs/planning/mutation-route-rbac/docs-tracking`

[Directory guide](<planning/mutation-route-rbac/docs-tracking/directory.md>)

- [plan_20261002.md](<planning/mutation-route-rbac/docs-tracking/plan_20261002.md>) — Plan: docs-tracking (2026-10-02) — after the other three aspects merge to the branch: Commit: `docs(rbac): changelog, permission matrix, tracking`.
- [spec.md](<planning/mutation-route-rbac/docs-tracking/spec.md>) — Aspect: docs-tracking (PRD R7)

## `docs/planning/mutation-route-rbac/frontend-gating`

[Directory guide](<planning/mutation-route-rbac/frontend-gating/directory.md>)

- [plan_20261002.md](<planning/mutation-route-rbac/frontend-gating/plan_20261002.md>) — Plan: frontend-gating (2026-10-02): Source: `../prd.md` R5/R6. `services/frontend-web`; pnpm workspace (install from repo root). Tests: Vitest, hoisted `authMock` (`__tests__/customers/ChurnSuggestionsPage.test.tsx:12-30`).…
- [spec.md](<planning/mutation-route-rbac/frontend-gating/spec.md>) — Aspect: frontend-gating (PRD R5, R6)

## `docs/planning/mutation-route-rbac/sweep-guard`

[Directory guide](<planning/mutation-route-rbac/sweep-guard/directory.md>)

- [plan_20261002.md](<planning/mutation-route-rbac/sweep-guard/plan_20261002.md>) — Plan: sweep-guard (2026-10-02): Source: `../prd.md` R3. Model on `tests/test_integration_rbac_sweep.py` (registry + marker) and `test_webhook_verifiers_fail_closed.py` (pinned allowlist, stale-entry test) but per-route via `ast`.…
- [spec.md](<planning/mutation-route-rbac/sweep-guard/spec.md>) — Aspect: sweep-guard (PRD R3)

## `docs/planning/oauth-tokens-encryption-at-rest`

[Directory guide](<planning/oauth-tokens-encryption-at-rest/directory.md>)

- [prd.md](<planning/oauth-tokens-encryption-at-rest/prd.md>) — PRD — OAuth tokens encryption at rest: Slack and Intercom OAuth flows in `services/backend-api/src/api/routes/integrations.py` store the provider access token **in plaintext** in the generic `integrations` table

## `docs/planning/oauth-tokens-encryption-at-rest/backend-encrypt-decrypt`

[Directory guide](<planning/oauth-tokens-encryption-at-rest/backend-encrypt-decrypt/directory.md>)

- [plan_20260809.md](<planning/oauth-tokens-encryption-at-rest/backend-encrypt-decrypt/plan_20260809.md>) — Implementation Plan — backend-encrypt-decrypt: (`InvalidToken` from `cryptography.fernet`; `ValueError` when the key is unset.) Keep the existing `if not access_token` 400 for the truly-absent case.
- [spec.md](<planning/oauth-tokens-encryption-at-rest/backend-encrypt-decrypt/spec.md>) — Spec — Backend encrypt/decrypt (write sites + backend read sites): Slack and Intercom OAuth callbacks store raw tokens (`integrations.py:912`, `:1089`); the backend read sites (`test_slack_integration`, `list_slack_channels`)…

## `docs/planning/oauth-tokens-encryption-at-rest/backfill-migration`

[Directory guide](<planning/oauth-tokens-encryption-at-rest/backfill-migration/directory.md>)

- [plan_20260809.md](<planning/oauth-tokens-encryption-at-rest/backfill-migration/plan_20260809.md>) — Implementation Plan — backfill-migration: Mirror the exact pattern of `services/backend-api/tests/test_usage_history_trend_columns_migration.py`: - `downgrade()` restores the plaintext row to the original string (best-effort…
- [spec.md](<planning/oauth-tokens-encryption-at-rest/backfill-migration/spec.md>) — Spec — Backfill migration: Existing plaintext `oauth_access_token` rows in the `integrations` table must be encrypted in place when this fix deploys, with a fail-closed behavior for installs

## `docs/planning/oauth-tokens-encryption-at-rest/docs-and-tracking`

[Directory guide](<planning/oauth-tokens-encryption-at-rest/docs-and-tracking/directory.md>)

- [plan_20260809.md](<planning/oauth-tokens-encryption-at-rest/docs-and-tracking/plan_20260809.md>) — Implementation Plan — docs-and-tracking: - Slack/Intercom OAuth tokens are now encrypted at rest with Fernet (same as every other integration). - Note that existing plaintext rows are encrypted in place on the first upgrade, and…
- [spec.md](<planning/oauth-tokens-encryption-at-rest/docs-and-tracking/spec.md>) — Spec — Docs & tracking: The roadmap-hygiene rule (DEV-TRACKING.md:497: "When closing work, correct the marker in the same commit") and the decision-confirmed hard-abort behavior need operator-facing

## `docs/planning/oauth-tokens-encryption-at-rest/worker-decrypt-mirrors`

[Directory guide](<planning/oauth-tokens-encryption-at-rest/worker-decrypt-mirrors/directory.md>)

- [plan_20260809.md](<planning/oauth-tokens-encryption-at-rest/worker-decrypt-mirrors/plan_20260809.md>) — Implementation Plan — worker-decrypt-mirrors: worker must carry its own module-local `_decrypt` Fernet helper — never Add it (module-level, exactly this body) to each of the four files that read the token.
- [spec.md](<planning/oauth-tokens-encryption-at-rest/worker-decrypt-mirrors/spec.md>) — Spec — Worker decrypt mirrors (5 read sites + intercom_sync fix): worker-service cannot import backend-api code (image ships only `worker-service/src` + `analysis-engine/src/analyzer`), yet it reads…

## `docs/planning/oidc-sso`

[Directory guide](<planning/oidc-sso/directory.md>)

- [prd.md](<planning/oidc-sso/prd.md>) — PRD — OIDC Single Sign-On (self-hosted): An operator running a self-hosted Rereflect instance cannot connect their identity provider to login. which an enterprise IT function will accept as the access path to an internal…
- [understanding.md](<planning/oidc-sso/understanding.md>) — Understanding — `oidc-sso` (Phase 2 dig): All paths below are in the worktree. Every claim is cited; where I could not verify something, it is Let an operator of a **self-hosted** Rereflect deployment plug their own identity…

## `docs/planning/oidc-sso/auth-test-harness`

[Directory guide](<planning/oidc-sso/auth-test-harness/directory.md>)

- [plan_20260716.md](<planning/oidc-sso/auth-test-harness/plan_20260716.md>) — Implementation Plan — `auth-test-harness`: Verified live in the worktree on 2026-07-16 — the PRD's R3 ("zero auth tests") is **frontend-only**: the substance, but small and infra-ready. The PRD's "M1 may dwarf the feature" worry…
- [spec.md](<planning/oidc-sso/auth-test-harness/spec.md>) — Aspect Spec — `auth-test-harness`: must not change behaviour** (PRD S4). Before any OIDC production code is written, we need a green, trustworthy characterization net around the **current** auth behaviour, so that any regression

## `docs/planning/oidc-sso/oidc-config`

[Directory guide](<planning/oidc-sso/oidc-config/directory.md>)

- [plan_20260717.md](<planning/oidc-sso/oidc-config/plan_20260717.md>) — Implementation Plan — `oidc-config`: (`src/api/routes/zendesk_integration.py`) — same Fernet pattern, same `token_hint`/`secret_hint` - `services/backend-api/src/models/oidc_config.py` **(new)** — the model per spec §1. Docstring
- [spec.md](<planning/oidc-sso/oidc-config/spec.md>) — Aspect Spec — `oidc-config`: Give an operator a place to store their IdP connection — issuer, client id, client secret, the domain allowlist, and an on/off switch — and give the rest of the system two read paths: an admin-only…

## `docs/planning/oidc-sso/oidc-docs-and-compose`

[Directory guide](<planning/oidc-sso/oidc-docs-and-compose/directory.md>)

- [plan_20260717.md](<planning/oidc-sso/oidc-docs-and-compose/plan_20260717.md>) — Implementation Plan — `oidc-docs-and-compose`: deployment (D5), JIT→member + verified-email linking, callback `{BACKEND_URL}/api/v1/auth/oidc/callback`. Add a one-line comment on the existing `FRONTEND_URL`/`BACKEND_URL` noting…
- [spec.md](<planning/oidc-sso/oidc-docs-and-compose/spec.md>) — Aspect Spec — `oidc-docs-and-compose`: An operator can discover, configure, and test OIDC SSO without reading source. This aspect makes the feature real to a human: env docs, a self-hosting guide section, a local IdP to test…

## `docs/planning/oidc-sso/oidc-frontend`

[Directory guide](<planning/oidc-sso/oidc-frontend/directory.md>)

- [plan_20260717.md](<planning/oidc-sso/oidc-frontend/plan_20260717.md>) — Implementation Plan — `oidc-frontend`: `npx eslint <path>`. Do NOT run repo-wide `npm run lint` (≈34 pre-existing unrelated errors); gate is idiom (`GoogleSignInButton.tsx:98`, `login/page.tsx:317`).
- [spec.md](<planning/oidc-sso/oidc-frontend/spec.md>) — Aspect Spec — `oidc-frontend`: Make the backend flow usable from the browser: (1) a "Sign in with SSO" button on the login page that appears only when the operator enabled SSO, sending the user to the backend `/auth/oidc/start`;…

## `docs/planning/oidc-sso/oidc-login-flow`

[Directory guide](<planning/oidc-sso/oidc-login-flow/directory.md>)

- [plan_20260717.md](<planning/oidc-sso/oidc-login-flow/plan_20260717.md>) — Implementation Plan — `oidc-login-flow` (THE SECURITY CORE): NEVER a user/org id. Identity comes from the validated ID token. `_sign_state`/`_verify_state` (HMAC keyed on `JWT_SECRET` via `from src.api.auth import JWT_SECRET`),
- [spec.md](<planning/oidc-sso/oidc-login-flow/spec.md>) — Aspect Spec — `oidc-login-flow`: Turn the stored `OidcConfig` into a working login: a user clicks "Sign in with SSO", is redirected to the operator's IdP, authenticates, and returns authenticated to Rereflect — provisioned (JIT)…

## `docs/planning/per-org-category-classifier`

[Directory guide](<planning/per-org-category-classifier/directory.md>)

- [prd.md](<planning/per-org-category-classifier/prd.md>) — PRD — Per-Org Category Classifier (M5.2 v2): `docs/planning/per-org-corrections-classifier/prd.md:145`) time an operator overrides the AI-assigned pain-point or feature-request category on a feedback item —
- [understanding.md](<planning/per-org-category-classifier/understanding.md>) — Phase 2 — Understanding note: per-org category classifier (M5.2 v2): Synthesis of four read-only service maps (analysis-engine, worker, backend, frontend), 2026-07-11. Extend the shipped M5.2 per-org self-improving classifier…

## `docs/planning/per-org-category-classifier/category-core`

[Directory guide](<planning/per-org-category-classifier/category-core/directory.md>)

- [plan_20260711.md](<planning/per-org-category-classifier/category-core/plan_20260711.md>) — Implementation Plan — category-core (analysis-engine spine): This plan is written for an autonomous coding agent to execute unattended, strict TDD, small commits per phase. Every phase: write/extend the failing test(s) first, run…
- [spec.md](<planning/per-org-category-classifier/category-core/spec.md>) — Aspect: category-core (analysis-engine spine): The spine is ~90% generic; only four sentiment touch-points block a category head. Parameterize them (sentiment default preserved, byte-stable) and add a category dataset builder…

## `docs/planning/per-org-category-classifier/data-and-config`

[Directory guide](<planning/per-org-category-classifier/data-and-config/directory.md>)

- [plan_20260711.md](<planning/per-org-category-classifier/data-and-config/plan_20260711.md>) — Tech Plan — data-and-config (per-org-category-classifier, M5.2 v2): (predict-seam), `frontend-web` (settings-and-frontend). See §7 Out of Scope Guardrails. No new dependencies, no new services, no env vars. This is a single…
- [spec.md](<planning/per-org-category-classifier/data-and-config/spec.md>) — Aspect: data-and-config: Operators need to enable/disable the category head independently of sentiment. Add `category_classifier_mode` (off/shadow/auto) to `OrgAIConfig` and expose it on the AI settings

## `docs/planning/per-org-category-classifier/predict-seam`

[Directory guide](<planning/per-org-category-classifier/predict-seam/directory.md>)

- [plan_20260711.md](<planning/per-org-category-classifier/predict-seam/plan_20260711.md>) — Implementation plan — predict-seam (per-org category classifier, M5.2 v2): `services/worker-service/src/services/{classifier_resolver,classifier_predict}.py`, `services/backend-api/src/api/routes/feedback.py`,…
- [spec.md](<planning/per-org-category-classifier/predict-seam/spec.md>) — Aspect: predict-seam: by reading the per-type mode and routing the predicted label to the right category field. `apply_classifier_override` already threads `classifier_type` but hard-writes `sentiment_label/score`.

## `docs/planning/per-org-category-classifier/settings-and-frontend`

[Directory guide](<planning/per-org-category-classifier/settings-and-frontend/directory.md>)

- [plan_20260711.md](<planning/per-org-category-classifier/settings-and-frontend/plan_20260711.md>) — Implementation Plan — settings-and-frontend (2026-07-11): (`GET/PATCH /api/v1/settings/ai`). **No backend change in this aspect.** The accuracy/rollback route query param on both `GET .../classifier/accuracy` and `POST…
- [spec.md](<planning/per-org-category-classifier/settings-and-frontend/spec.md>) — Aspect: settings-and-frontend: already-type-parameterized backend accuracy/rollback API. The backend `GET/POST .../classifier/accuracy/rollback` already accept `classifier_type` (default

## `docs/planning/per-org-category-classifier/worker-trainer`

[Directory guide](<planning/per-org-category-classifier/worker-trainer/directory.md>)

- [plan_20260711.md](<planning/per-org-category-classifier/worker-trainer/plan_20260711.md>) — Implementation Plan — worker-trainer (weekly retrain loop): Pre-flight §3), any `analysis-engine` file (owned by `category-core`, assumed already merged — see Pre-flight §1), any predict-seam / `OrgAIConfig` / migration file (out…
- [spec.md](<planning/per-org-category-classifier/worker-trainer/spec.md>) — Aspect: worker-trainer: Extend `retrain_all_orgs` to run both classifier types. The promote/eval/lock/purge machinery is already type-agnostic once `_CLASSIFIER_TYPE` is a parameter; add a category incumbent and the category…

## `docs/planning/per-org-churn-model`

[Directory guide](<planning/per-org-churn-model/directory.md>)

- [prd.md](<planning/per-org-churn-model/prd.md>) — PRD — Per-Org Churn ML Model (M5.3): isotonic-calibrated heuristic — with the heuristic preserved as the automatic fallback. For whom: the self-hosting operator of Rereflect who labels churn events (manually, via

## `docs/planning/per-org-churn-model/calibration-beat-fix`

[Directory guide](<planning/per-org-churn-model/calibration-beat-fix/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/calibration-beat-fix/plan_20260814.md>) — Implementation Plan — calibration-beat-fix (aspect 1): The dig found the bug in `churn_calibration.py`. **Planning-time verification found the same bug class in `classifier_training.py`**: `retrain_all_orgs` (beat
- [spec.md](<planning/per-org-churn-model/calibration-beat-fix/spec.md>) — Spec — calibration-beat-fix (prerequisite): The calibrated-heuristic incumbent has never run: `tasks/churn_calibration.py` defines `refit_all_orgs`, `refit_global_calibration`, `purge_old_calibration_models` as plain

## `docs/planning/per-org-churn-model/churn-classifier-core`

[Directory guide](<planning/per-org-churn-model/churn-classifier-core/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/churn-classifier-core/plan_20260814.md>) — Implementation Plan — churn-classifier-core (aspect 3, slice 2a): (trainer.py, predict.py, evaluate.py, dataset.py, metrics.py, labels.py) — the patterns to mirror — and their tests in…
- [spec.md](<planning/per-org-churn-model/churn-classifier-core/spec.md>) — Spec — churn-classifier-core (slice 2a): The analysis-engine needs a churn-specific training/eval core: a customer-level feature vector, a JSON-only logistic trainer, a pure-stdlib predictor, and a leakage-free A/B

## `docs/planning/per-org-churn-model/churn-label-gate-study`

[Directory guide](<planning/per-org-churn-model/churn-label-gate-study/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/churn-label-gate-study/plan_20260814.md>) — Implementation Plan — churn-label-gate-study (aspect 2, slice 1): if the harness imports the classifier core — **it must not**: the study runs before the core exists, so the harness implements a minimal logistic stand-in inline…
- [spec.md](<planning/per-org-churn-model/churn-label-gate-study/spec.md>) — Spec — churn-label-gate-study (slice 1): a pre-pivot hosted-SaaS criterion; half of it ("≥ 5,000 globally") is dead single-tenant, and nobody has re-derived what a per-org churn classifier needs. `AI-TRACKING.md:551-553`

## `docs/planning/per-org-churn-model/churn-predict-seam-resolver`

[Directory guide](<planning/per-org-churn-model/churn-predict-seam-resolver/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/churn-predict-seam-resolver/plan_20260814.md>) — Implementation Plan — churn-predict-seam-resolver (aspect 5, slice 2c): worker-service (models mirror + resolver copy + `probability_updater` seam). (existing mode columns),…
- [spec.md](<planning/per-org-churn-model/churn-predict-seam-resolver/spec.md>) — Spec — churn-predict-seam-resolver (slice 2c): The per-org mode gate and the prediction override: `OrgAIConfig.churn_classifier_mode` (off/shadow/auto) + `churn_autopromote_hold`, a resolver mirroring

## `docs/planning/per-org-churn-model/docs-changelog-tracking`

[Directory guide](<planning/per-org-churn-model/docs-changelog-tracking/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/docs-changelog-tracking/plan_20260814.md>) — Implementation Plan — docs-changelog-tracking (aspect 7, close-out): - `AI-TRACKING.md` (M5.3 markers + gate caveat 542-553 + M5.2/M5.4 rows if needed) - `DEV-TRACKING.md` (FIXED markers for both registration bugs; the…
- [spec.md](<planning/per-org-churn-model/docs-changelog-tracking/spec.md>) — Spec — docs-changelog-tracking (close-out): Repo convention (visible across every shipped feature's commit history) is that a feature lands with its docs: CHANGELOG entries, SELF_HOSTING upgrade callouts, AI-TRACKING

## `docs/planning/per-org-churn-model/settings-api-and-churn-accuracy-card`

[Directory guide](<planning/per-org-churn-model/settings-api-and-churn-accuracy-card/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/settings-api-and-churn-accuracy-card/plan_20260814.md>) — Implementation Plan — settings-api-and-churn-accuracy-card (aspect 6, slice 2d): (Settings → AI General + Accuracy tabs, readiness card). fields ~84-100, validation blocks ~578-654, `VALID_CLASSIFIER_MODES`,
- [spec.md](<planning/per-org-churn-model/settings-api-and-churn-accuracy-card/spec.md>) — Spec — settings-api-and-churn-accuracy-card (slice 2d): Surface the churn head to the operator: mode toggle in Settings → AI, a fourth incumbent-vs-challenger accuracy card with versions/rollback/resume, and a readiness

## `docs/planning/per-org-churn-model/worker-churn-trainer-and-schedule`

[Directory guide](<planning/per-org-churn-model/worker-churn-trainer-and-schedule/directory.md>)

- [plan_20260814.md](<planning/per-org-churn-model/worker-churn-trainer-and-schedule/plan_20260814.md>) — Implementation Plan — worker-churn-trainer-and-schedule (aspect 4, slice 2b): core (aspect 3) via lazy imports. Depends on aspect 1 (incumbent real) and aspect 5's migration for the OrgAIConfig columns — **read them…
- [spec.md](<planning/per-org-churn-model/worker-churn-trainer-and-schedule/spec.md>) — Spec — worker-churn-trainer-and-schedule (slice 2b): A scheduled per-org training task that runs the churn core's A/B, promotes on a measurable margin, and stays reversible — following the M5.2 worker conventions exactly,

## `docs/planning/per-org-corrections-classifier`

[Directory guide](<planning/per-org-corrections-classifier/directory.md>)

- [prd.md](<planning/per-org-corrections-classifier/prd.md>) — PRD — Per-Org Self-Improving Corrections Classifier (M5.2): Rereflect has collected human corrections of its AI output since M3.3 (`AICorrection`, table `ai_corrections`) — but **nothing trains on them**. The analyzer that…

## `docs/planning/per-org-corrections-classifier/data-layer`

[Directory guide](<planning/per-org-corrections-classifier/data-layer/directory.md>)

- [plan_20260710.md](<planning/per-org-corrections-classifier/data-layer/plan_20260710.md>) — Tech Plan — data-layer (M5.2 per-org-corrections-classifier): Persist per-org classifier artifacts + eval history + the per-org mode toggle, mirroring the proven `churn_calibration_models` / `ChurnBacktestRun` conventions, in…
- [spec.md](<planning/per-org-corrections-classifier/data-layer/spec.md>) — Aspect Spec — data-layer: Persist per-org classifier artifacts + eval history + the per-org mode toggle, mirroring the proven `churn_calibration_models` conventions, in **both** the backend ORM and the worker mirror. After this

## `docs/planning/per-org-corrections-classifier/predict-seam-resolver`

[Directory guide](<planning/per-org-corrections-classifier/predict-seam-resolver/directory.md>)

- [plan_20260710.md](<planning/per-org-corrections-classifier/predict-seam-resolver/plan_20260710.md>) — Tech Plan — predict-seam-resolver (M5.2): Wire the trained per-org classifier artifact into the **live sentiment path** with `off`/`shadow`/`auto` semantics + a 3-tier load fallback, exactly mirroring how M5.1's…
- [spec.md](<planning/per-org-corrections-classifier/predict-seam-resolver/spec.md>) — Aspect Spec — predict-seam-resolver: Wire the trained per-org model into the live analysis path with `off`/`shadow`/`auto` semantics, a three-tier load fallback, and shadow logging — mirroring exactly how M5.1's…

## `docs/planning/per-org-corrections-classifier/settings-api-and-accuracy-card`

[Directory guide](<planning/per-org-corrections-classifier/settings-api-and-accuracy-card/directory.md>)

- [plan_20260710.md](<planning/per-org-corrections-classifier/settings-api-and-accuracy-card/plan_20260710.md>) — Implementation Plan — settings-api-and-accuracy-card (2026-07-10): This aspect **only reads** those tables (rollback is the single write); tests **seed** rows directly. STRICT TDD: RED test first each phase → GREEN → commit.…
- [spec.md](<planning/per-org-corrections-classifier/settings-api-and-accuracy-card/spec.md>) — Aspect Spec — settings-api-and-accuracy-card: Operator-facing surface: a per-org mode toggle (off/shadow/auto) and an honest accuracy/delta card under Settings → AI, mirroring the M5.1 `SentimentAccuracyCard` + churn-accuracy…

## `docs/planning/per-org-corrections-classifier/training-and-eval-core`

[Directory guide](<planning/per-org-corrections-classifier/training-and-eval-core/directory.md>)

- [plan_20260710.md](<planning/per-org-corrections-classifier/training-and-eval-core/plan_20260710.md>) — Tech Plan — training-and-eval-core (M5.2 per-org-corrections-classifier): A CPU-only, offline, per-org **sentiment** classifier core: with the promote/retain/skip decision. Disclosure only, never fails a build.
- [spec.md](<planning/per-org-corrections-classifier/training-and-eval-core/spec.md>) — Aspect Spec — training-and-eval-core: The pure-compute brain: build a labeled dataset from an org's sentiment corrections, train a CPU-only TF-IDF + logistic-regression classifier into a **JSON** artifact, and run the shadow-A/B

## `docs/planning/per-org-corrections-classifier/worker-trainer-and-schedule`

[Directory guide](<planning/per-org-corrections-classifier/worker-trainer-and-schedule/directory.md>)

- [plan_20260710.md](<planning/per-org-corrections-classifier/worker-trainer-and-schedule/plan_20260710.md>) — Tech Plan — worker-trainer-and-schedule (M5.2 per-org-corrections-classifier): A Celery task module `services/worker-service/src/tasks/classifier_training.py` that runs the pure training/eval core across all orgs weekly, persists…
- [spec.md](<planning/per-org-corrections-classifier/worker-trainer-and-schedule/spec.md>) — Aspect Spec — worker-trainer-and-schedule: The Celery driver that runs the core across all orgs on a schedule, persists versioned artifacts with an **atomic** active-model swap, records an eval-run row every time, and purges old…

## `docs/planning/playbook-action-types`

[Directory guide](<planning/playbook-action-types/directory.md>)

- [prd.md](<planning/playbook-action-types/prd.md>) — PRD — Complete the seeded playbook action types: The churn-playbook engine implements 5 of the 11 action types the seeder declares valid, so **6 of the 7 seeded playbook templates contain steps that fail on every execution**

## `docs/planning/playbook-action-types/playbook-tasks`

[Directory guide](<planning/playbook-action-types/playbook-tasks/directory.md>)

- [plan_20260827.md](<planning/playbook-action-types/playbook-tasks/plan_20260827.md>) — Implementation Plan — `playbook-tasks`: house rules) and `services/worker-service` (SQLite in-memory tests) in the worktree. Backend test command: `pytest tests/ -q` (CI runs against migrated PostgreSQL).
- [spec.md](<planning/playbook-action-types/playbook-tasks/spec.md>) — Aspect — `playbook-tasks`: Seeded steps like `{"type": "create_task", "config": {"description": "Follow-up check-in", "due_in_days": 3}}` persist a durable follow-up task for the customer instead of failing

## `docs/planning/playbook-action-types/seeder-and-ui`

[Directory guide](<planning/playbook-action-types/seeder-and-ui/directory.md>)

- [plan_20260827.md](<planning/playbook-action-types/seeder-and-ui/plan_20260827.md>) — Implementation Plan — `seeder-and-ui`: `services/frontend-web` (pnpm workspace — install once from repo root: `pnpm install` at the worktree root, then `npm run test` / `npm run lint` inside
- [spec.md](<planning/playbook-action-types/seeder-and-ui/spec.md>) — Aspect — `seeder-and-ui`: 5 new action types, and execution action logs become visible. Existing installs converge (seeded templates stop carrying dead steps), operators can build

## `docs/planning/playbook-action-types/tag-notify-actions`

[Directory guide](<planning/playbook-action-types/tag-notify-actions/directory.md>)

- [plan_20260827.md](<planning/playbook-action-types/tag-notify-actions/plan_20260827.md>) — Implementation Plan — `tag-notify-actions`: migrations (the `tags` column already exists in the DB). `.claude/worktrees/feat-playbook-action-types` (venv already per-worktree; run
- [spec.md](<planning/playbook-action-types/tag-notify-actions/spec.md>) — Aspect — `tag-notify-actions`: Pure worker-side, no schema change beyond a model-mirror column. A seeded playbook step `{"type": "tag", "config": {"tag": "at-risk"}}` writes the tag to the

## `docs/planning/playbook-action-types/trigger-automation`

[Directory guide](<planning/playbook-action-types/trigger-automation/directory.md>)

- [plan_20260827.md](<planning/playbook-action-types/trigger-automation/plan_20260827.md>) — Implementation Plan — `trigger-automation`: Strict TDD: **RED → GREEN → REFACTOR**. **No changes** to `automation_churn_trigger.py`, `automation_usage_trend_trigger.py`, or
- [spec.md](<planning/playbook-action-types/trigger-automation/spec.md>) — Aspect — `trigger-automation`: to **churn_probability_threshold rules only**; `usage_trend` is transition-based and not A seeded step `{"type": "trigger_automation", "config": {"automation_name": "..."}}` fires a

## `docs/planning/playbook-execution-reaper`

[Directory guide](<planning/playbook-execution-reaper/directory.md>)

- [prd.md](<planning/playbook-execution-reaper/prd.md>) — PRD — Playbook execution reaper: A `ChurnPlaybookExecution` can be stuck at `queued` forever: batch route, backend engine, worker mirrors) logs and moves on; nothing re-publishes.

## `docs/planning/product-usage-enrichment`

[Directory guide](<planning/product-usage-enrichment/directory.md>)

- [prd.md](<planning/product-usage-enrichment/prd.md>) — PRD — Product Usage Enrichment: Rereflect's stated killer feature is "churn prediction that actually works," but the prediction has **no product-usage signal** — the single most predictive leading indicator of SaaS churn (a…

## `docs/planning/product-usage-enrichment/frontend-surface`

[Directory guide](<planning/product-usage-enrichment/frontend-surface/directory.md>)

- [plan_20260628.md](<planning/product-usage-enrichment/frontend-surface/plan_20260628.md>) — Implementation Plan — frontend-surface (2026-06-28)
- [spec.md](<planning/product-usage-enrichment/frontend-surface/spec.md>) — Aspect Spec — frontend-surface: The operator sees product usage on the Customer 360 profile (a "Usage Activity" card + usage-over-time chart), the 5th component in the health breakdown, and a settings/docs section explaining how…

## `docs/planning/product-usage-enrichment/health-component`

[Directory guide](<planning/product-usage-enrichment/health-component/directory.md>)

- [plan_20260628.md](<planning/product-usage-enrichment/health-component/plan_20260628.md>) — Implementation Plan — health-component (2026-06-28): - `org_ai_config.health_weight_usage` `INTEGER NOT NULL DEFAULT 0` - `customer_health_scores.usage_component` `INTEGER NULL` (semantically neutral 50 when unset; nullable so…
- [spec.md](<planning/product-usage-enrichment/health-component/spec.md>) — Aspect Spec — health-component: The customer health score gains an **opt-in** 5th component (usage), defaulting to weight 0 so **no existing org's score changes** until an operator re-weights. The change is protected by a…

## `docs/planning/product-usage-enrichment/ingestion-receiver`

[Directory guide](<planning/product-usage-enrichment/ingestion-receiver/directory.md>)

- [plan_20260628.md](<planning/product-usage-enrichment/ingestion-receiver/plan_20260628.md>) — Implementation Plan — ingestion-receiver (2026-06-28): 3. Email resolution helper: `event.email or event.traits.get("email")`. 4. `properties` size guard helper (serialize, if >16 KB truncate + flag).
- [spec.md](<planning/product-usage-enrichment/ingestion-receiver/spec.md>) — Aspect Spec — ingestion-receiver: A self-hosted operator can POST product-usage events to Rereflect with an existing ingest-scoped API key. The endpoint validates, dedups, and hands events to the worker — returning accurate…

## `docs/planning/product-usage-enrichment/usage-rollup-and-score`

[Directory guide](<planning/product-usage-enrichment/usage-rollup-and-score/directory.md>)

- [plan_20260628.md](<planning/product-usage-enrichment/usage-rollup-and-score/plan_20260628.md>) — Implementation Plan — usage-rollup-and-score (2026-06-28): - **Recency** from `last_active_at`: ≤2d→100, ≤7d→80, ≤14d→60, ≤30d→40, ≤60d→20, else 5; `None`→neutral. - **Frequency** from `active_days_30d`: ≥20→100 … 0→low (define…
- [spec.md](<planning/product-usage-enrichment/usage-rollup-and-score/spec.md>) — Aspect Spec — usage-rollup-and-score: Raw usage events become a per-customer rollup with a 0-100 `usage_score` (recency + frequency + breadth), recomputed as events arrive and on a schedule, so a customer going quiet lowers their…

## `docs/planning/public-api-crud-v3`

[Directory guide](<planning/public-api-crud-v3/directory.md>)

- [prd.md](<planning/public-api-crud-v3/prd.md>) — PRD — Public API CRUD v3 (bulk feedback writes + custom-taxonomy CRUD): The public REST API (`/api/public/v1`) is a named moat pillar for the open-source, self-hosted edition: operators automate their own instance with their own…

## `docs/planning/public-api-crud-v3/bulk-feedback-write`

[Directory guide](<planning/public-api-crud-v3/bulk-feedback-write/directory.md>)

- [plan_20260714.md](<planning/public-api-crud-v3/bulk-feedback-write/plan_20260714.md>) — Implementation Plan — bulk-feedback-write: Strict TDD (RED → GREEN → REFACTOR). Keep the branch green after every phase. All new tests under already validates tags (≤20, ≤50). Its "≥1 mutating field" rule lives in the *handler*…
- [spec.md](<planning/public-api-crud-v3/bulk-feedback-write/spec.md>) — Aspect spec — bulk-feedback-write: A `write`-scoped public API key can update `workflow_status` / `tags` / `is_urgent` (and optionally record a `correction`) for up to 500 feedback items in **one** request, and gets a **per-item…

## `docs/planning/public-api-crud-v3/docs-and-tracking`

[Directory guide](<planning/public-api-crud-v3/docs-and-tracking/directory.md>)

- [plan_20260715.md](<planning/public-api-crud-v3/docs-and-tracking/plan_20260715.md>) — Implementation Plan — docs-and-tracking: shapes + route paths from the merged code (do not copy from the plans — copy from what shipped). `docs(public-api-crud-v3): SELF_HOSTING + CHANGELOG + AI/DEV-TRACKING for bulk + taxonomy…
- [spec.md](<planning/public-api-crud-v3/docs-and-tracking/spec.md>) — Aspect spec — docs-and-tracking: Ship the docs/tracking that every prior public-API slice shipped, so the two new capabilities are discoverable

## `docs/planning/public-api-crud-v3/public-taxonomy-crud`

[Directory guide](<planning/public-api-crud-v3/public-taxonomy-crud/directory.md>)

- [plan_20260715.md](<planning/public-api-crud-v3/public-taxonomy-crud/plan_20260715.md>) — Implementation Plan — public-taxonomy-crud: Strict TDD. Independent of `bulk-feedback-write` — can build in parallel. category_type ∈ pain_point/feature_request/urgency/general, is_active}`. No unique constraint (dedup in route).
- [spec.md](<planning/public-api-crud-v3/public-taxonomy-crud/spec.md>) — Aspect spec — public-taxonomy-crud: A public API key can manage the org's custom categories programmatically, mirroring the internal `/api/v1/categories/custom` CRUD, with a delete/rename warning when the name is referenced by an…

## `docs/planning/public-api-write-crud`

[Directory guide](<planning/public-api-write-crud/directory.md>)

- [prd.md](<planning/public-api-write-crud/prd.md>) — PRD — Public API Write Scope & Feedback Mutation (slice 1): Rereflect's public REST API (`/api/public/v1`) is **read + ingest only**. An operator with an API key can pull feedback/customers/analytics (`read` scope) and submit new…

## `docs/planning/public-api-write-crud/feedback-write-endpoint`

[Directory guide](<planning/public-api-write-crud/feedback-write-endpoint/directory.md>)

- [plan_20260706.md](<planning/public-api-write-crud/feedback-write-endpoint/plan_20260706.md>) — Implementation Plan — `feedback-write-endpoint` (2026-07-06): The meaty aspect: extract shared helpers from the internal status-change + correction routes, then add the public `PATCH /api/public/v1/feedback/{id}`. Strict TDD;…
- [spec.md](<planning/public-api-write-crud/feedback-write-endpoint/spec.md>) — Aspect Spec — `feedback-write-endpoint`: A `write`-scoped API key can `PATCH /api/public/v1/feedback/{id}` to (a) change `workflow_status` and (b) submit a category/sentiment correction — through the **same internal code paths**…

## `docs/planning/public-api-write-crud/write-scope`

[Directory guide](<planning/public-api-write-crud/write-scope/directory.md>)

- [plan_20260706.md](<planning/public-api-write-crud/write-scope/plan_20260706.md>) — Implementation Plan — `write-scope` (2026-07-06): Small, self-contained aspect. Register the `write` scope end-to-end (backend allowlist + docs + frontend picker/type/badge). No DB migration.
- [spec.md](<planning/public-api-write-crud/write-scope/spec.md>) — Aspect Spec — `write-scope`: The public API has no `write` scope. Register a new `write` scope end-to-end so operators can *grant* it on an API key and see it documented, before any write endpoint uses it. Outcome: a user creates…

## `docs/planning/public-api-write-v2`

[Directory guide](<planning/public-api-write-v2/directory.md>)

- [prd.md](<planning/public-api-write-v2/prd.md>) — PRD — Public API Write Expansion v2 (tags, is_urgent, DELETE): The public REST API's write surface is half-open. Slice 1 added a `write` scope and `PATCH /api/public/v1/feedback/{id}` that can move `workflow_status` and record…

## `docs/planning/public-api-write-v2/docs-openapi`

[Directory guide](<planning/public-api-write-v2/docs-openapi/directory.md>)

- [plan_20260707.md](<planning/public-api-write-v2/docs-openapi/plan_20260707.md>) — Implementation Plan — docs-openapi (2026-07-07): 1. `:8-12` module scope table → `write` line: "PATCH (workflow status, corrections, tags, is_urgent) + DELETE feedback". 2. `:753-758` `info.description` → update the `write`…
- [spec.md](<planning/public-api-write-v2/docs-openapi/spec.md>) — Aspect Spec — docs-openapi: The public API docs, OpenAPI description, and tracking accurately describe the expanded `write` surface (tags/is_urgent edits + DELETE).

## `docs/planning/public-api-write-v2/patch-tags-urgent`

[Directory guide](<planning/public-api-write-v2/patch-tags-urgent/directory.md>)

- [plan_20260707.md](<planning/public-api-write-v2/patch-tags-urgent/plan_20260707.md>) — Implementation Plan — patch-tags-urgent (2026-07-07): 1. Run the existing suite green: `pytest tests/test_public_api_write.py -v`. Record pass count. This is the regression baseline (status change, no-op same-status, correction…
- [spec.md](<planning/public-api-write-v2/patch-tags-urgent/spec.md>) — Aspect Spec — patch-tags-urgent: An operator with a `write` key can set a feedback item's `tags` and `is_urgent` via the existing `PATCH /api/public/v1/feedback/{id}`, in the same request that may also carry…

## `docs/planning/public-api-write-v2/public-delete-feedback`

[Directory guide](<planning/public-api-write-v2/public-delete-feedback/directory.md>)

- [plan_20260707.md](<planning/public-api-write-v2/public-delete-feedback/plan_20260707.md>) — Implementation Plan — public-delete-feedback (2026-07-07): 1. `pytest tests/test_feedback.py -k delete -v` and `pytest tests/test_customer_analyze_archive.py -v` → green baseline. - New/edit…
- [spec.md](<planning/public-api-write-v2/public-delete-feedback/spec.md>) — Aspect Spec — public-delete-feedback: An operator with a `write` key can delete a feedback item via `DELETE /api/public/v1/feedback/{id}`, with the same side effects as the internal dashboard delete.

## `docs/planning/salesforce-crm-enrichment`

[Directory guide](<planning/salesforce-crm-enrichment/directory.md>)

- [prd.md](<planning/salesforce-crm-enrichment/prd.md>) — PRD — Salesforce CRM Enrichment for Customer 360 + Churn: Rereflect's killer feature is "churn prediction that actually works." CRM signals — ARR, deal stage, and especially **contract renewal date** — are among the most…

## `docs/planning/salesforce-crm-enrichment/crm-provider-generalization`

[Directory guide](<planning/salesforce-crm-enrichment/crm-provider-generalization/directory.md>)

- [plan_20260701.md](<planning/salesforce-crm-enrichment/crm-provider-generalization/plan_20260701.md>) — Implementation Plan — crm-provider-generalization (2026-07-01): 1. Fixture: org + customer + a `CrmEnrichment` row (semantic fields incl. `renewal_date`; leave `provider` unset so it defaults). Reuse existing CRM/health fixtures…
- [spec.md](<planning/salesforce-crm-enrichment/crm-provider-generalization/spec.md>) — Aspect Spec — crm-provider-generalization: Make `crm_enrichment` and its read paths provider-aware so a second CRM (Salesforce) can populate the same semantic fields without ambiguity — while every existing HubSpot-enriched org…

## `docs/planning/salesforce-crm-enrichment/salesforce-connection`

[Directory guide](<planning/salesforce-crm-enrichment/salesforce-connection/directory.md>)

- [plan_20260701.md](<planning/salesforce-crm-enrichment/salesforce-connection/plan_20260701.md>) — Implementation Plan — salesforce-connection (2026-07-01): 2. `purge_crm_enrichment(db, org_id, provider)`: delete `crm_enrichment` rows for `(org, provider)`, collect affected emails, call `update_customer_health(org_id, email,…
- [spec.md](<planning/salesforce-crm-enrichment/salesforce-connection/spec.md>) — Aspect Spec — salesforce-connection: An admin/owner connects their Salesforce org via web-server OAuth (mirroring Linear) and can see status / test / disconnect. Credentials are stored encrypted; only one CRM may be active per…

## `docs/planning/salesforce-crm-enrichment/salesforce-frontend`

[Directory guide](<planning/salesforce-crm-enrichment/salesforce-frontend/directory.md>)

- [plan_20260701.md](<planning/salesforce-crm-enrichment/salesforce-frontend/plan_20260701.md>) — Implementation Plan — salesforce-frontend (2026-07-01)
- [spec.md](<planning/salesforce-crm-enrichment/salesforce-frontend/spec.md>) — Aspect Spec — salesforce-frontend: An admin/owner discovers, connects (via OAuth redirect), and manages Salesforce from Settings → Integrations, and sees which CRM populated the Customer 360 card.

## `docs/planning/salesforce-crm-enrichment/salesforce-sync`

[Directory guide](<planning/salesforce-crm-enrichment/salesforce-sync/directory.md>)

- [plan_20260701.md](<planning/salesforce-crm-enrichment/salesforce-sync/plan_20260701.md>) — Implementation Plan — salesforce-sync (2026-07-01): 2. `SalesforceClient(refresh_token, instance_url, login_base, api_version)` context manager. 3. Per match: resolve Account via `Contact.AccountId` (direct FK — no associations)…
- [spec.md](<planning/salesforce-crm-enrichment/salesforce-sync/spec.md>) — Aspect Spec — salesforce-sync: - Token refresh: exchange stored `refresh_token` → short-lived `access_token` (against `{login_base}/services/oauth2/token`), using it as `Authorization: Bearer` against `instance_url`. -…

## `docs/planning/salesforce-crm-writeback`

[Directory guide](<planning/salesforce-crm-writeback/directory.md>)

- [prd.md](<planning/salesforce-crm-writeback/prd.md>) — PRD — Salesforce CRM Writeback (health score, slice 2): `crm-writeback/prd.md:144`. See `../_card/card.md` + `../_card/understanding.md` (4-agent dig). Rereflect computes a per-customer **health score** (and churn signals), but…

## `docs/planning/salesforce-crm-writeback/model-migrations`

[Directory guide](<planning/salesforce-crm-writeback/model-migrations/directory.md>)

- [plan_20260705.md](<planning/salesforce-crm-writeback/model-migrations/plan_20260705.md>) — Implementation Plan — model-migrations: `services/backend-api` (2 models + 1 migration), `services/worker-service` (CrmEnrichment mirror). No new deps. **DB change: yes — one Alembic migration.**
- [spec.md](<planning/salesforce-crm-writeback/model-migrations/spec.md>) — Aspect Spec — model-migrations: The Salesforce writeback config and the matched-Contact target have nowhere to live. Add the schema so every downstream aspect (config-api, push-task, sync) has stable columns to read/write, without

## `docs/planning/salesforce-crm-writeback/push-task-trigger`

[Directory guide](<planning/salesforce-crm-writeback/push-task-trigger/directory.md>)

- [plan_20260705.md](<planning/salesforce-crm-writeback/push-task-trigger/plan_20260705.md>) — Implementation Plan — push-task-trigger: `services/worker-service` (new task + sync edit + celery include), `services/backend-api` (trigger `services/worker-service/tests/test_salesforce_sync.py` (extend or new)
- [spec.md](<planning/salesforce-crm-writeback/push-task-trigger/spec.md>) — Aspect Spec — push-task-trigger: When a customer's health score changes, the score is pushed to their matched Salesforce Contact — idempotently, safely, and only when Salesforce writeback is enabled — without disturbing the…

## `docs/planning/salesforce-crm-writeback/salesforce-write-client`

[Directory guide](<planning/salesforce-crm-writeback/salesforce-write-client/directory.md>)

- [plan_20260705.md](<planning/salesforce-crm-writeback/salesforce-write-client/plan_20260705.md>) — Implementation Plan — salesforce-write-client: `services/worker-service` (client PATCH + describe), `services/backend-api` (validation service). - `services/worker-service/src/clients/salesforce.py` (add methods + maybe…
- [spec.md](<planning/salesforce-crm-writeback/salesforce-write-client/spec.md>) — Aspect Spec — salesforce-write-client: The shipped Salesforce client is query/read-only, and there is no field-validation service. Provide (a) a client method to PATCH a Contact field and (b) a describe-based validation service,…

## `docs/planning/salesforce-crm-writeback/writeback-config-api`

[Directory guide](<planning/salesforce-crm-writeback/writeback-config-api/directory.md>)

- [plan_20260705.md](<planning/salesforce-crm-writeback/writeback-config-api/plan_20260705.md>) — Implementation Plan — writeback-config-api: `services/backend-api` (routes + Pydantic schemas). No new deps. No DB change (columns from aspect 1). - `services/backend-api/src/api/routes/salesforce_integration.py` (schemas +…
- [spec.md](<planning/salesforce-crm-writeback/writeback-config-api/spec.md>) — Aspect Spec — writeback-config-api: An operator can enable/configure/validate Salesforce writeback and read its status from the app, with legible errors and a backfill kicked off on enable — mirroring the shipped HubSpot…

## `docs/planning/salesforce-crm-writeback/writeback-ui`

[Directory guide](<planning/salesforce-crm-writeback/writeback-ui/directory.md>)

- [plan_20260705.md](<planning/salesforce-crm-writeback/writeback-ui/plan_20260705.md>) — Implementation Plan — writeback-ui: `services/frontend-web` only (api client + component + settings page). No new deps. - `services/frontend-web/lib/api/__tests__/salesforce.test.ts` (extend)
- [spec.md](<planning/salesforce-crm-writeback/writeback-ui/spec.md>) — Aspect Spec — writeback-ui: An admin/owner can enable, configure, and validate Salesforce writeback and see its status from the Salesforce integration settings page — mirroring the shipped HubSpot writeback card.

## `docs/planning/saml-sso`

[Directory guide](<planning/saml-sso/directory.md>)

- [prd.md](<planning/saml-sso/prd.md>) — PRD — SAML 2.0 Single Sign-On (self-hosted): Rereflect's self-hosted edition shipped **OIDC** SSO (`feat/oidc-sso`). A large share of enterprises that self-host internal tools standardize on **SAML 2.0** IdPs (Okta, Azure AD /…

## `docs/planning/saml-sso/config-model-and-crud`

[Directory guide](<planning/saml-sso/config-model-and-crud/directory.md>)

- [impl-report.md](<planning/saml-sso/config-model-and-crud/impl-report.md>) — Implementation Report — config-model-and-crud (SAML SSO, aspect 2/6): Implemented the SAML config model + CRUD + cross-provider single-enabled guard exactly per `plan_20260717.md`, mirroring the shipped OIDC aspect. Strict TDD…
- [plan_20260717.md](<planning/saml-sso/config-model-and-crud/plan_20260717.md>) — Tech Plan — SAML SSO · config-model-and-crud: This plan mirrors the shipped OIDC aspect (`oidc_config.py` model + `routes/oidc_config.py` + `c9d0e1f2a3b4` / `n8o9p0q1r2s3` migrations + `test_oidc_config.py`) exactly in shape and…
- [spec.md](<planning/saml-sso/config-model-and-crud/spec.md>) — Aspect Spec — config-model-and-crud: An admin/owner can store and manage the deployment's single SAML IdP connection, and the deployment enforces **one SSO protocol total** (OIDC xor SAML). Mirrors `oidc_config` exactly in…

## `docs/planning/saml-sso/deps-and-docker`

[Directory guide](<planning/saml-sso/deps-and-docker/directory.md>)

- [impl-report.md](<planning/saml-sso/deps-and-docker/impl-report.md>) — Implementation Report — `deps-and-docker` (SAML SSO, aspect 1 of 6): The RED→GREEN cycle for `test_saml_deps.py` could **not** be fully closed in this macOS venv — well-understood, host-specific reason documented in detail below.…
- [plan_20260717.md](<planning/saml-sso/deps-and-docker/plan_20260717.md>) — Tech Plan — `deps-and-docker` (SAML SSO, slice 1, aspect 1 of N): Land the SAML native dependency + Docker build changes and **prove they import** — nothing else. When this aspect is green, `from onelogin.saml2.auth import…
- [spec.md](<planning/saml-sso/deps-and-docker/spec.md>) — Aspect Spec — deps-and-docker: `python3-saml` depends on `xmlsec`, which needs native `libxmlsec1` / `libxml2` (+ `pkg-config`) system libraries. If the backend image / CI environment lacks them, **the entire test suite fails to…

## `docs/planning/saml-sso/docs-and-dev-idp`

[Directory guide](<planning/saml-sso/docs-and-dev-idp/directory.md>)

- [impl-report.md](<planning/saml-sso/docs-and-dev-idp/impl-report.md>) — Implementation Report — `docs-and-dev-idp` aspect: Documented the SAML 2.0 SSO slice that shipped across the five functional aspects (`deps-and-docker`, `config-model-and-crud`, `provider-and-replay-store`,
- [plan_20260717.md](<planning/saml-sso/docs-and-dev-idp/plan_20260717.md>) — Implementation Plan — `saml-sso` / aspect `docs-and-dev-idp`: This aspect runs LAST precisely so the docs match reality. **Do this verification block first** and record the answers; every later phase consumes them. Run from the…
- [spec.md](<planning/saml-sso/docs-and-dev-idp/spec.md>) — Aspect Spec — docs-and-dev-idp: A self-hosting operator can follow docs to register Rereflect as a SAML SP with their IdP, configure it, - Register the SP with your IdP: ACS URL `{BACKEND_URL}/api/v1/auth/saml/callback`…

## `docs/planning/saml-sso/frontend-saml-ui`

[Directory guide](<planning/saml-sso/frontend-saml-ui/directory.md>)

- [impl-report.md](<planning/saml-sso/frontend-saml-ui/impl-report.md>) — Implementation Report — frontend-saml-ui: `npm run test` / `npx vitest` are intercepted by the user's `rtk` shell hook and silently return 0 suites (a proxy artifact, not a project issue). All commands below were run with the…
- [plan_20260717.md](<planning/saml-sso/frontend-saml-ui/plan_20260717.md>) — Implementation Plan — frontend-saml-ui: Mirror the shipped **OIDC frontend surface** for SAML. Every file below has an OIDC counterpart already in the tree — we clone the pattern, swap OIDC → SAML nouns/endpoints, and (for the…
- [spec.md](<planning/saml-sso/frontend-saml-ui/spec.md>) — Aspect Spec — frontend-saml-ui: An admin configures SAML at `/settings/sso`, and end users get one "Sign in with SSO" button that starts the SAML flow. Mirrors the OIDC frontend surface; exactly one SSO button ever shows…

## `docs/planning/saml-sso/login-routes-and-identity`

[Directory guide](<planning/saml-sso/login-routes-and-identity/directory.md>)

- [impl-report.md](<planning/saml-sso/login-routes-and-identity/impl-report.md>) — Impl Report — `login-routes-and-identity` (SAML 2.0 SSO, aspect 4): Two routes wired into `src/api/routes/auth.py` (riding the existing `auth.router`, prefix `/api/v1/auth`), plus the reused OIDC-shaped identity-resolution block.…
- [plan_20260717.md](<planning/saml-sso/login-routes-and-identity/plan_20260717.md>) — Tech Plan — `login-routes-and-identity` (SAML 2.0 SSO): This aspect wires the **SP-initiated SAML login flow** into the reused OIDC identity-resolution block: `sso_error` constants + `SAML_ACS_PATH`, the identity-resolution…
- [spec.md](<planning/saml-sso/login-routes-and-identity/spec.md>) — Aspect Spec — login-routes-and-identity: The end-to-end SP-initiated login: start → IdP → ACS → validated assertion → resolved user → JWT → persist the returned `request_id` (pending) via the replay store; 302 to the IdP redirect…

## `docs/planning/saml-sso/provider-and-replay-store`

[Directory guide](<planning/saml-sso/provider-and-replay-store/directory.md>)

- [impl-report.md](<planning/saml-sso/provider-and-replay-store/impl-report.md>) — Implementation Report — SAML SSO · provider-and-replay-store (aspect 3): Aspect 3 of 6: the pure `SamlProvider` (build AuthnRequest + validate SAML Response/Assertion) and the DB-backed replay store. No FastAPI routes (aspect 4
- [plan_20260717.md](<planning/saml-sso/provider-and-replay-store/plan_20260717.md>) — Tech Plan — SAML SSO · provider-and-replay-store: (OneLogin): builds an SP-initiated **unsigned** AuthnRequest (HTTP-Redirect) and validates a returned SAML Response/Assertion to a trusted identity, delegating signature +…
- [spec.md](<planning/saml-sso/provider-and-replay-store/spec.md>) — Aspect Spec — provider-and-replay-store: A pure, testable service that (a) builds an SP-initiated AuthnRequest and (b) validates a returned SAML Response/Assertion to a trusted identity — plus the server-side replay store that…

## `docs/planning/scheduled-ai-reports`

[Directory guide](<planning/scheduled-ai-reports/directory.md>)

- [prd.md](<planning/scheduled-ai-reports/prd.md>) — PRD — Scheduled & Emailed AI Reports: Rereflect's On-Demand AI Reports (M2.4, `COMPLETE`) require a user to open the Copilot (Cmd+K) and ask for a report each time. The only recurring communication today is the
- [understanding.md](<planning/scheduled-ai-reports/understanding.md>) — Understanding note — scheduled & emailed AI reports (Phase 2 dig): A follow-on slice of shipped M2.4 On-Demand AI Reports (`AI-TRACKING.md:51`; non-goals at `PRD-ON-DEMAND-AI-REPORTS.md:37-38`): let an org configure a **report…

## `docs/planning/scheduled-ai-reports/backend-schedule-crud`

[Directory guide](<planning/scheduled-ai-reports/backend-schedule-crud/directory.md>)

- [plan_20260825.md](<planning/scheduled-ai-reports/backend-schedule-crud/plan_20260825.md>) — Implementation Plan — backend-schedule-crud: Worktree root: `/Users/aliz/dev/at/rereflect/.claude/worktrees/feat-scheduled-ai-reports`. Run all commands from the worktree. TDD strictly: failing test → implementation → refactor.
- [spec.md](<planning/scheduled-ai-reports/backend-schedule-crud/spec.md>) — Aspect spec — backend-schedule-crud: An org must be able to create, read, update, enable/disable and delete a report schedule through the backend API. Without this aspect nothing can be configured; the worker task

## `docs/planning/scheduled-ai-reports/frontend-scheduled-reports-ui`

[Directory guide](<planning/scheduled-ai-reports/frontend-scheduled-reports-ui/directory.md>)

- [deviations.md](<planning/scheduled-ai-reports/frontend-scheduled-reports-ui/deviations.md>) — Deviations — frontend-scheduled-reports-ui: Recorded at completion (2026-08-25) per the aspect plan §7 ("Do not restructure the existing Reports list view beyond wrapping it in Tabs").
- [plan_20260825.md](<planning/scheduled-ai-reports/frontend-scheduled-reports-ui/plan_20260825.md>) — Implementation Plan — frontend-scheduled-reports-ui: Worktree root: `/Users/aliz/dev/at/rereflect/.claude/worktrees/feat-scheduled-ai-reports`. TDD strictly. `Select`/`Table`/`Badge` already present; `@radix-ui/react-tabs` in…
- [spec.md](<planning/scheduled-ai-reports/frontend-scheduled-reports-ui/spec.md>) — Aspect spec — frontend-scheduled-reports-ui: On the existing `/reports` page, an operator (admin/owner) can manage report schedules from a **Scheduled** tab: see them in a table (type, cadence, day/hour, recipients, last run),

## `docs/planning/scheduled-ai-reports/worker-email-delivery`

[Directory guide](<planning/scheduled-ai-reports/worker-email-delivery/directory.md>)

- [plan_20260825.md](<planning/scheduled-ai-reports/worker-email-delivery/plan_20260825.md>) — Implementation Plan — worker-email-delivery: Worktree root: `/Users/aliz/dev/at/rereflect/.claude/worktrees/feat-scheduled-ai-reports`. TDD strictly. `FROM_EMAIL`, `FROM_NAME`, `APP_URL` from `src/email.py`).
- [spec.md](<planning/scheduled-ai-reports/worker-email-delivery/spec.md>) — Aspect spec — worker-email-delivery: each recipient on the schedule receives the report by email. With no key (or empty recipients) nothing is sent and nothing fails — the in-app report is always produced.

## `docs/planning/scheduled-ai-reports/worker-scheduled-generation`

[Directory guide](<planning/scheduled-ai-reports/worker-scheduled-generation/directory.md>)

- [plan_20260825.md](<planning/scheduled-ai-reports/worker-scheduled-generation/plan_20260825.md>) — Implementation Plan — worker-scheduled-generation: Worktree root: `/Users/aliz/dev/at/rereflect/.claude/worktrees/feat-scheduled-ai-reports`. TDD strictly. `worker-email-delivery` (sender) merged on the branch before the final…
- [spec.md](<planning/scheduled-ai-reports/worker-scheduled-generation/spec.md>) — Aspect spec — worker-scheduled-generation: A Celery beat task materializes each due, enabled report schedule into a real `Report` row — exactly once per cadence window — with data sections identical to on-demand reports plus a

## `docs/planning/segment-actions`

[Directory guide](<planning/segment-actions/directory.md>)

- [prd.md](<planning/segment-actions/prd.md>) — PRD — Segment Actions (Actionable Customer Segments): Customer **Segments** shipped in M3.4 (commit `010bfdf`): every customer is classified into one of 7 rule-based cohorts (`at_risk`, `silent_churner`, `dormant`, `power_user`,…

## `docs/planning/segment-actions/bulk-actions-api`

[Directory guide](<planning/segment-actions/bulk-actions-api/directory.md>)

- [plan_20260709.md](<planning/segment-actions/bulk-actions-api/plan_20260709.md>) — Implementation Plan — bulk-actions-api (2026-07-09): `src/api/routes/customers.py` (or a new `customers_bulk.py` router included before parametric routes). 1. Characterization test: snapshot `list_customers` results across param…
- [spec.md](<planning/segment-actions/bulk-actions-api/spec.md>) — Aspect Spec — bulk-actions-api: and `customers-bulk-ui` consume. Blocks `customers-bulk-ui`. Provide the shared **cohort contract** and the three non-playbook bulk actions: server-side CSV export, bulk

## `docs/planning/segment-actions/customer-fields-model`

[Directory guide](<planning/segment-actions/customer-fields-model/directory.md>)

- [plan_20260709.md](<planning/segment-actions/customer-fields-model/plan_20260709.md>) — Implementation Plan — customer-fields-model (2026-07-09): test `tests/test_migrations_segment_actions.py` (or extend an existing migration test). 1. Write a test that upgrades to head, asserts `customer_health_scores.tags` +…
- [spec.md](<planning/segment-actions/customer-fields-model/spec.md>) — Aspect Spec — customer-fields-model: Customers (the `CustomerHealth` / `customer_health_scores` record) have no `tags` and no CS-owner field. Add both so the bulk tag/assign actions have something to write, and surface them on…

## `docs/planning/segment-actions/customers-bulk-ui`

[Directory guide](<planning/segment-actions/customers-bulk-ui/directory.md>)

- [plan_20260709.md](<planning/segment-actions/customers-bulk-ui/plan_20260709.md>) — Implementation Plan — customers-bulk-ui (2026-07-09): `components/customers/`, `lib/api/customers.ts`, `lib/api/playbooks.ts`, `SegmentBadge`/tags display. 1. Add `tags?: string[]` and `cs_owner?: {id:number; email:string} /…
- [spec.md](<planning/segment-actions/customers-bulk-ui/spec.md>) — Aspect Spec — customers-bulk-ui: Give `/customers` a working selection + bulk-actions surface: check rows (or "select all N matching the filter"), then Export / Tag / Assign owner / Run playbook against the cohort. Surface `tags`…

## `docs/planning/segment-actions/playbook-cohort-run`

[Directory guide](<planning/segment-actions/playbook-cohort-run/directory.md>)

- [plan_20260709.md](<planning/segment-actions/playbook-cohort-run/plan_20260709.md>) — Implementation Plan — playbook-cohort-run (2026-07-09): `bulk-actions-api` (imports `Cohort`/`resolve_cohort`/`_apply_customer_filters`). probability-range selection, daily-limit, one execution/customer, celery dispatch mock.…
- [spec.md](<planning/segment-actions/playbook-cohort-run/spec.md>) — Aspect Spec — playbook-cohort-run: Let an operator run an existing churn playbook against a **cohort** (selected emails or a segment/filter), not just a probability band. This is the headline moat action. **No playbook-model…

## `docs/planning/slack-email-signature-enforcement`

[Directory guide](<planning/slack-email-signature-enforcement/directory.md>)

- [prd.md](<planning/slack-email-signature-enforcement/prd.md>) — PRD — Slack & email webhook signature enforcement (fail-closed flip): follow-up recorded in DEV-TRACKING.md:423-426 from the P0 webhook hardening. The P0 webhook hardening (2026-07-29) shipped the Slack and inbound-email (Resend)

## `docs/planning/slack-email-signature-enforcement/fail-closed-flip`

[Directory guide](<planning/slack-email-signature-enforcement/fail-closed-flip/directory.md>)

- [plan_20260817.md](<planning/slack-email-signature-enforcement/fail-closed-flip/plan_20260817.md>) — Implementation plan — fail-closed-flip (2026-08-17): Feature: `slack-email-signature-enforcement` · Aspect: `fail-closed-flip` Source: `docs/planning/slack-email-signature-enforcement/prd.md` + `spec.md`.
- [spec.md](<planning/slack-email-signature-enforcement/fail-closed-flip/spec.md>) — Aspect spec — Fail-closed flip: The two shadow-mode verifiers (Slack, email/Resend) flip to fail closed; the sweep guard's allowlist empties; the shadow tests flip; the startup warning re-scopes; docs

## `docs/planning/status-sync-realtime-mapping`

[Directory guide](<planning/status-sync-realtime-mapping/directory.md>)

- [prd.md](<planning/status-sync-realtime-mapping/prd.md>) — PRD — Real-time, Operator-mapped Integration Status-Sync (v2): Rereflect closes the feedback→ticket loop for three issue trackers (Jira, Asana, Zendesk): a feedback item can spawn an issue/ticket, and inbound **status-sync**

## `docs/planning/status-sync-realtime-mapping/asana-webhook`

[Directory guide](<planning/status-sync-realtime-mapping/asana-webhook/directory.md>)

- [plan_20260718.md](<planning/status-sync-realtime-mapping/asana-webhook/plan_20260718.md>) — Implementation Plan — `asana-webhook` (2026-07-18): Strict TDD. **Depends on `status-writer-race-guard` merged.** Branch: nullable, Fernet-encrypted) + `webhook_gid` (String, nullable). **Alembic
- [spec.md](<planning/status-sync-realtime-mapping/asana-webhook/spec.md>) — Aspect spec — `asana-webhook`: Part of PRD `status-sync-realtime-mapping`. Depends on `status-writer-race-guard`. An Asana task completion change is reflected on the linked feedback item's

## `docs/planning/status-sync-realtime-mapping/jira-webhook`

[Directory guide](<planning/status-sync-realtime-mapping/jira-webhook/directory.md>)

- [plan_20260718.md](<planning/status-sync-realtime-mapping/jira-webhook/plan_20260718.md>) — Implementation Plan — `jira-webhook` (2026-07-18): Strict TDD. **Depends on `status-writer-race-guard` merged.** Branch: Fernet-encrypted). **Alembic migration required** — confirm single head first:
- [spec.md](<planning/status-sync-realtime-mapping/jira-webhook/spec.md>) — Aspect spec — `jira-webhook`: Part of PRD `status-sync-realtime-mapping`. Depends on `status-writer-race-guard`. A Jira issue status change is reflected on the linked feedback item's

## `docs/planning/status-sync-realtime-mapping/mapping-editor`

[Directory guide](<planning/status-sync-realtime-mapping/mapping-editor/directory.md>)

- [plan_20260718.md](<planning/status-sync-realtime-mapping/mapping-editor/plan_20260718.md>) — Implementation Plan — `mapping-editor` (2026-07-18): Strict TDD (RED → GREEN → REFACTOR). Branch: `feat/status-sync-realtime-mapping`. - `services/backend-api/src/api/routes/jira_integration.py` — add
- [spec.md](<planning/status-sync-realtime-mapping/mapping-editor/spec.md>) — Aspect spec — `mapping-editor`: Part of PRD `status-sync-realtime-mapping`. Independently shippable; no webhooks. An operator (admin/owner) can **see and edit** the foreign-status →

## `docs/planning/status-sync-realtime-mapping/status-writer-race-guard`

[Directory guide](<planning/status-sync-realtime-mapping/status-writer-race-guard/directory.md>)

- [plan_20260718.md](<planning/status-sync-realtime-mapping/status-writer-race-guard/plan_20260718.md>) — Implementation Plan — `status-writer-race-guard` (2026-07-18): Strict TDD. Branch: `feat/status-sync-realtime-mapping`. migration, no new deps. (The backend-api webhook reconcile ports that reuse
- [spec.md](<planning/status-sync-realtime-mapping/status-writer-race-guard/spec.md>) — Aspect spec — `status-writer-race-guard`: Part of PRD `status-sync-realtime-mapping`. Prereq for the webhook aspects' Concurrent status applies (15-min poll + a new real-time webhook, or two

## `docs/planning/teams-notifications`

[Directory guide](<planning/teams-notifications/directory.md>)

- [prd.md](<planning/teams-notifications/prd.md>) — PRD: Microsoft Teams Notification Integration: Outbound alerts reach Slack, Discord, email and the in-app dashboard — but not Microsoft Teams, even though the codebase has reserved `'teams'` as a provider type since before the

## `docs/planning/teams-notifications/automations-notify`

[Directory guide](<planning/teams-notifications/automations-notify/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/automations-notify/plan_20260902.md>) — Implementation Plan: automations-notify: 1. RED: extend the `_execute_notify` tests (find them: `grep -rl "_execute_notify" services/backend-api/tests/`): rule with `channels: ["teams"]` + active Teams integration → sender called…
- [spec.md](<planning/teams-notifications/automations-notify/spec.md>) — Spec: automations-notify: Automation rules can notify a Teams channel — the `send_notification` action gains Teams in both the backend engine and the worker's mirror evaluator.

## `docs/planning/teams-notifications/backend-connector`

[Directory guide](<planning/teams-notifications/backend-connector/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/backend-connector/plan_20260902.md>) — Implementation Plan: backend-connector: 1. RED: write tests first (new file `services/backend-api/tests/test_teams_integration.py`, mirroring the existing discord test file — find it with `grep -rl "discord/webhook" tests/`).…
- [spec.md](<planning/teams-notifications/backend-connector/spec.md>) — Spec: backend-connector: The backend can connect, validate, test and send to a Teams webhook — the provider plumbing Slack/Discord already have in `services/backend-api/src/api/routes/integrations.py`.

## `docs/planning/teams-notifications/channel-preference`

[Directory guide](<planning/teams-notifications/channel-preference/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/channel-preference/plan_20260902.md>) — Implementation Plan: channel-preference: - New: `services/backend-api/alembic/versions/<rev>_add_channel_teams.py` 1. RED: model test asserting the column exists with default True.
- [spec.md](<planning/teams-notifications/channel-preference/spec.md>) — Spec: channel-preference: Users can opt out of Teams alerts per notification type, exactly like `channel_discord` one Alembic migration, chained off the current single head.

## `docs/planning/teams-notifications/docs-landing`

[Directory guide](<planning/teams-notifications/docs-landing/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/docs-landing/plan_20260902.md>) — Implementation Plan: docs-landing: 1. Copy the Slack entry (:96-134) as the shape template; write the Teams entry with: - `slug: 'teams'`, `status: 'available'` (do NOT use `'coming_soon'` — nothing may claim "coming soon" for…
- [spec.md](<planning/teams-notifications/docs-landing/spec.md>) — Spec: docs-landing: Every place the product claims its integration surface is honest on day one — no 'available'`), mirroring the Slack outbound entry (:96-134) — name, tagline,

## `docs/planning/teams-notifications/frontend-ui`

[Directory guide](<planning/teams-notifications/frontend-ui/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/frontend-ui/plan_20260902.md>) — Implementation Plan: frontend-ui: 1. RED: component test — renders with brand color `#6264A7`. 1. RED: extend the integrations client tests (find: `grep -rl "createDiscordWebhook" services/frontend-web/`) —…
- [spec.md](<planning/teams-notifications/frontend-ui/spec.md>) — Spec: frontend-ui: The Settings → Integrations surface offers Teams as a first-class provider: live tile, webhook connect page, detail page, API client — Discord parity.

## `docs/planning/teams-notifications/playbook-notify`

[Directory guide](<planning/teams-notifications/playbook-notify/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/playbook-notify/plan_20260902.md>) — Implementation Plan: playbook-notify: 1. RED: extend the `_handle_notify` tests (find them: `grep -rl "_handle_notify" services/worker-service/tests/` or the playbook engine test file): `channel: "teams"` + active integration →…
- [spec.md](<planning/teams-notifications/playbook-notify/spec.md>) — Spec: playbook-notify: The churn-playbook `notify` action can target a Teams channel — worker engine branch plus the editor's channel select, matching the existing discord precedent.

## `docs/planning/teams-notifications/worker-dispatch`

[Directory guide](<planning/teams-notifications/worker-dispatch/directory.md>)

- [plan_20260902.md](<planning/teams-notifications/worker-dispatch/plan_20260902.md>) — Implementation Plan: worker-dispatch: 1. RED: new tests (find the discord sender test file: `grep -rl "send_discord_message_webhook" tests/`) — assert: posts `{"@type": "MessageCard", ..., "themeColor": "6264A7"}` JSON;…
- [spec.md](<planning/teams-notifications/worker-dispatch/spec.md>) — Spec: worker-dispatch: The worker can deliver Teams cards on every notification pipe, with the same per-process raise-on-failure contract and org-wide gating Slack/Discord use.

## `docs/planning/urgency-classifier-head`

[Directory guide](<planning/urgency-classifier-head/directory.md>)

- [prd.md](<planning/urgency-classifier-head/prd.md>) — PRD — Per-Org Self-Improving Urgency Classifier Head: Rereflect flags urgent (churn-risk) feedback with a **static keyword+sentiment heuristic** from operator corrections. The other two analyzer outputs — sentiment and category —…

## `docs/planning/urgency-classifier-head/capture-seam`

[Directory guide](<planning/urgency-classifier-head/capture-seam/directory.md>)

- [plan_20260714.md](<planning/urgency-classifier-head/capture-seam/plan_20260714.md>) — Implementation Plan — capture-seam (backend + frontend): original_value, corrected_value, feedback_text)` (`services/ai_correction_service.py:15`) — the shared helper; commits internally; `user_id` nullable for API-key writes.
- [spec.md](<planning/urgency-classifier-head/capture-seam/spec.md>) — Aspect Spec — capture-seam (backend + frontend): `services/frontend-web/` (feedback detail page + API client). Every user-driven change to a feedback item's urgent flag is recorded as a training signal

## `docs/planning/urgency-classifier-head/data-and-config`

[Directory guide](<planning/urgency-classifier-head/data-and-config/directory.md>)

- [plan_20260714.md](<planning/urgency-classifier-head/data-and-config/plan_20260714.md>) — Implementation Plan — data-and-config (backend + worker mirror): Add `urgency_classifier_mode` (off/shadow/auto) to `OrgAIConfig`, exposed via the AI settings GET/PATCH, and register it in the worker's resolver map — a…
- [spec.md](<planning/urgency-classifier-head/data-and-config/spec.md>) — Aspect Spec — data-and-config (backend): `services/worker-service` (OrgAIConfig mirror), `services/backend-api/alembic/`. Operators can set `urgency_classifier_mode ∈ {off, shadow, auto}` per org, persisted and exposed via the

## `docs/planning/urgency-classifier-head/predict-seam`

[Directory guide](<planning/urgency-classifier-head/predict-seam/directory.md>)

- [plan_20260714.md](<planning/urgency-classifier-head/predict-seam/plan_20260714.md>) — Implementation Plan — predict-seam (worker + backend mirror, at ingest): (a promoted urgency model to resolve). Highest-stakes — it can change `feedback.is_urgent`. At ingest, apply the resolved per-org urgency model to…
- [spec.md](<planning/urgency-classifier-head/predict-seam/spec.md>) — Aspect Spec — predict-seam (worker / analysis at ingest): must exist to resolve). Highest-stakes aspect — it can overwrite `feedback.is_urgent`. At ingest, the resolved per-org urgency model conditionally overrides the keyword…

## `docs/planning/urgency-classifier-head/settings-frontend`

[Directory guide](<planning/urgency-classifier-head/settings-frontend/directory.md>)

- [plan_20260714.md](<planning/urgency-classifier-head/settings-frontend/plan_20260714.md>) — Implementation Plan — settings-frontend (Next.js): Add an off/shadow/auto urgency mode toggle to Settings → AI (General) and an urgency accuracy card — a mechanical copy of the category head. Grounded against the frontend dig…
- [spec.md](<planning/urgency-classifier-head/settings-frontend/spec.md>) — Aspect Spec — settings-frontend (Next.js): card works as soon as the accuracy API returns urgency data (post worker-trainer). Operators control the urgency head from Settings → AI (off/shadow/auto toggle) and see an urgency…

## `docs/planning/urgency-classifier-head/urgency-core`

[Directory guide](<planning/urgency-classifier-head/urgency-core/directory.md>)

- [plan_20260714.md](<planning/urgency-classifier-head/urgency-core/plan_20260714.md>) — Implementation Plan — urgency-core (analysis-engine): Add a **binary urgency vocabulary** and a **dataset builder** to the already-generic `corrections_classifier` package, so the urgency head trains/evaluates on the same…
- [spec.md](<planning/urgency-classifier-head/urgency-core/spec.md>) — Aspect Spec — urgency-core (analysis-engine): Give the generic classifier spine a binary "urgency" vocabulary and dataset builder, so a per-org urgency model can be trained/evaluated by the exact same primitives that serve…

## `docs/planning/urgency-classifier-head/worker-trainer`

[Directory guide](<planning/urgency-classifier-head/worker-trainer/directory.md>)

- [plan_20260714.md](<planning/urgency-classifier-head/worker-trainer/plan_20260714.md>) — Implementation Plan — worker-trainer (worker + binary incumbent): Fold "urgency" into the weekly per-org retrain, wrapping the keyword heuristic as the binary incumbent. `(dataset, incumbent_predict, eval_labels)`. Add an…
- [spec.md](<planning/urgency-classifier-head/worker-trainer/spec.md>) — Aspect Spec — worker-trainer (worker + analysis-engine incumbent): retrain (trainer runs regardless of mode), but land data-and-config alongside to avoid churn. The weekly per-org retrain trains, evaluates, and promotes an…

## `docs/planning/usage-decline-churn-labels`

[Directory guide](<planning/usage-decline-churn-labels/directory.md>)

- [prd.md](<planning/usage-decline-churn-labels/prd.md>) — PRD — Usage-Decline Churn Labels (sustained-decline suggestions + operator review): dig), `docs/planning/crm-churn-labels/prd.md` (the pattern this extends), `AI-TRACKING.md` M3.2b / M5.3 — the upgrade from a calibrated churn…

## `docs/planning/usage-decline-churn-labels/config-and-migration`

[Directory guide](<planning/usage-decline-churn-labels/config-and-migration/directory.md>)

- [plan_20260723.md](<planning/usage-decline-churn-labels/config-and-migration/plan_20260723.md>) — Implementation Plan — config-and-migration: `./venv/bin/python` / `./venv/bin/pytest` / `./venv/bin/alembic` explicitly. **Re-run it anyway** (Phase 2, step 1) — see the warning there.
- [spec.md](<planning/usage-decline-churn-labels/config-and-migration/spec.md>) — Aspect — config-and-migration: There is no non-CRM home for a churn-label opt-in. Default-deny is the house pattern (`models/hubspot_integration.py:47-48`) and the safety property; without a config home this feature

## `docs/planning/usage-decline-churn-labels/detector-core`

[Directory guide](<planning/usage-decline-churn-labels/detector-core/directory.md>)

- [plan_20260723.md](<planning/usage-decline-churn-labels/detector-core/plan_20260723.md>) — Implementation Plan — detector-core: Never bare `python3` (3.9.6, cannot install this repo's requirements). here. Verify the mirrored copy with `diff`, exactly as the `config-and-migration` agent did.
- [spec.md](<planning/usage-decline-churn-labels/detector-core/spec.md>) — Aspect — detector-core: "Sustained decline" is a level-based concept, and the shipped trend stack only exposes **edges** (`worker-service/src/tasks/usage_metrics.py:635-638` appends to `pending_trend_transitions` only on

## `docs/planning/usage-decline-churn-labels/docs-and-tracking`

[Directory guide](<planning/usage-decline-churn-labels/docs-and-tracking/directory.md>)

- [spec.md](<planning/usage-decline-churn-labels/docs-and-tracking/spec.md>) — Aspect — docs-and-tracking: Every recent feature in this repo ships `docs(...)` commits, and `AI-TRACKING.md` currently carries a stale claim: the M5.3 note calls usage-derived churn labels "feasible but **unplanned**"

## `docs/planning/usage-decline-churn-labels/frontend-settings-and-evidence`

[Directory guide](<planning/usage-decline-churn-labels/frontend-settings-and-evidence/directory.md>)

- [plan_20260723.md](<planning/usage-decline-churn-labels/frontend-settings-and-evidence/plan_20260723.md>) — Implementation Plan — frontend-settings-and-evidence: `node_modules` is per-worktree — run `npm install` first if it is missing. against the fixed `evidence` key names (below) and the settings API already shipped.
- [spec.md](<planning/usage-decline-churn-labels/frontend-settings-and-evidence/spec.md>) — Aspect — frontend-settings-and-evidence: The operator needs somewhere to turn this on, a way to judge whether it is working, and an evidence display that isn't CRM-shaped. Today the review queue's `EvidenceCell` reads…

## `docs/planning/usage-decline-churn-labels/worker-detector`

[Directory guide](<planning/usage-decline-churn-labels/worker-detector/directory.md>)

- [plan_20260723.md](<planning/usage-decline-churn-labels/worker-detector/plan_20260723.md>) — Implementation Plan — worker-detector: directly. See §5 for how this aspect is tested anyway — this is the aspect where it hurts. `usage_churn_label_config` (+ migration `0a3382154c27`, + worker model mirror), the settings API,
- [spec.md](<planning/usage-decline-churn-labels/worker-detector/spec.md>) — Aspect — worker-detector: Wire the pure core to real data: scan each enabled org's usage history daily, find qualifying sustained declines, and write `ChurnLabelSuggestion` rows — without touching the churn stack, without

## `docs/planning/usage-trend-automation-trigger`

[Directory guide](<planning/usage-trend-automation-trigger/directory.md>)

- [prd.md](<planning/usage-trend-automation-trigger/prd.md>) — PRD — Usage-Trend Timeline Event & Automation Trigger (N1 + N2): M3.2b (`usage-trend-churn-signal`, shipped 2026-07-22, merge `6270adc`) detects that a customer's product usage is declining and classifies it into

## `docs/planning/usage-trend-automation-trigger/automations-frontend`

[Directory guide](<planning/usage-trend-automation-trigger/automations-frontend/directory.md>)

- [spec.md](<planning/usage-trend-automation-trigger/automations-frontend/spec.md>) — Aspect — `automations-frontend`: An operator can build a usage-trend rule in the UI, it starts in shadow, and the execution log - `TriggerType` union — `lib/api/automations.ts:5-10`

## `docs/planning/usage-trend-automation-trigger/snapshot-trend-columns`

[Directory guide](<planning/usage-trend-automation-trigger/snapshot-trend-columns/directory.md>)

- [plan_20260723.md](<planning/usage-trend-automation-trigger/snapshot-trend-columns/plan_20260723.md>) — Implementation Plan — `snapshot-trend-columns`: (`a5b63dbbce9b_add_usage_trend_fields.py`, the M3.2b trend-fields migration). ⚠️ **Verify live before generating** — run `alembic heads` in
- [spec.md](<planning/usage-trend-automation-trigger/snapshot-trend-columns/spec.md>) — Aspect — `snapshot-trend-columns`: `customer_usage` holds only the *current* trend state; `customer_usage_history` carries no trend columns at all. The timeline is assembled at read time from durable rows (F6), so without this

## `docs/planning/usage-trend-automation-trigger/template-and-docs`

[Directory guide](<planning/usage-trend-automation-trigger/template-and-docs/directory.md>)

- [spec.md](<planning/usage-trend-automation-trigger/template-and-docs/spec.md>) — Aspect — `template-and-docs`: An operator finds the usage-trend trigger without knowing it exists, can see whether it can fire for them at all, and reads an honest account of its limits.

## `docs/planning/usage-trend-automation-trigger/timeline-trend-event`

[Directory guide](<planning/usage-trend-automation-trigger/timeline-trend-event/directory.md>)

- [spec.md](<planning/usage-trend-automation-trigger/timeline-trend-event/spec.md>) — Aspect — `timeline-trend-event`: An operator opening a Customer 360 profile can see when the customer's usage trend changed and in which direction — so an auto-run playbook has a visible cause.

## `docs/planning/usage-trend-automation-trigger/trigger-registration`

[Directory guide](<planning/usage-trend-automation-trigger/trigger-registration/directory.md>)

- [plan_20260723.md](<planning/usage-trend-automation-trigger/trigger-registration/plan_20260723.md>) — Implementation Plan — `trigger-registration`: Runs fully in parallel with `snapshot-trend-columns` — zero file overlap. (PRD F3). Isolating it in a small dependency-free module means `worker-trend-evaluator`
- [spec.md](<planning/usage-trend-automation-trigger/trigger-registration/spec.md>) — Aspect — `trigger-registration`: The automation engine can validate, store and evaluate a `usage_trend` rule. No firing seam yet - `states: list[str]`, non-empty, subset of `{"declining", "sharp_decline"}`

## `docs/planning/usage-trend-automation-trigger/worker-trend-evaluator`

[Directory guide](<planning/usage-trend-automation-trigger/worker-trend-evaluator/directory.md>)

- [spec.md](<planning/usage-trend-automation-trigger/worker-trend-evaluator/spec.md>) — Aspect — `worker-trend-evaluator`: A customer entering `declining`/`sharp_decline` during the nightly recompute causes matching active rules to run their playbook, and matching shadow rules to log a would-have-run.

## `docs/planning/usage-trend-churn-signal`

[Directory guide](<planning/usage-trend-churn-signal/directory.md>)

- [prd.md](<planning/usage-trend-churn-signal/prd.md>) — PRD — Usage Trend Churn Signal: Rereflect's customer health score has had a product-usage component since M3.2 (`AI-TRACKING.md:207`), but it measures **level, not direction**. It can tell you a customer is

## `docs/planning/usage-trend-churn-signal/frontend-trend-and-weights`

[Directory guide](<planning/usage-trend-churn-signal/frontend-trend-and-weights/directory.md>)

- [plan_20260722.md](<planning/usage-trend-churn-signal/frontend-trend-and-weights/plan_20260722.md>) — Implementation Plan — frontend-trend-and-weights: `cd services/frontend-web`. Try `npm install` first (worked in a recent worktree per the repo gotchas note); if it fails with `EUNSUPPORTEDPROTOCOL`, run `pnpm install` at the…
- [spec.md](<planning/usage-trend-churn-signal/frontend-trend-and-weights/spec.md>) — Aspect Spec — frontend-trend-and-weights: Two frontend-only slices, both about making a shipped-but-invisible capability reachable. `usage_trend_state` / `usage_trend_pct` on the usage API response; without a UI they exist only

## `docs/planning/usage-trend-churn-signal/rollup-rewindow-fix`

[Directory guide](<planning/usage-trend-churn-signal/rollup-rewindow-fix/directory.md>)

- [plan_20260721.md](<planning/usage-trend-churn-signal/rollup-rewindow-fix/plan_20260721.md>) — Implementation Plan — rollup-rewindow-fix: No frontend, no analysis-engine. No new packages. No new env vars. Redis is shared machine-wide — one `redis-server` is enough.
- [spec.md](<planning/usage-trend-churn-signal/rollup-rewindow-fix/spec.md>) — Aspect Spec — rollup-rewindow-fix: The rolling-window fields on `customer_usage` (`active_days_7d/30d`, `login_count_7d/30d`) are computed only when an event arrives, so for a customer whose event rate falls they **freeze at

## `docs/planning/usage-trend-churn-signal/trend-detection-and-health`

[Directory guide](<planning/usage-trend-churn-signal/trend-detection-and-health/directory.md>)

- [plan_20260722.md](<planning/usage-trend-churn-signal/trend-detection-and-health/plan_20260722.md>) — Implementation Plan — trend-detection-and-health: The highest-risk aspect. The single boundary that matters more than all others: is the executable form of that boundary and must exist even though it asserts absence.
- [spec.md](<planning/usage-trend-churn-signal/trend-detection-and-health/spec.md>) — Aspect Spec — trend-detection-and-health: Depends on: `../rollup-rewindow-fix/spec.md`, `../usage-history-snapshot/` (both must land first) With re-windowing fixed (`rollup-rewindow-fix`) and a durable daily snapshot in place

## `docs/planning/usage-trend-churn-signal/usage-history-snapshot`

[Directory guide](<planning/usage-trend-churn-signal/usage-history-snapshot/directory.md>)

- [plan_20260722.md](<planning/usage-trend-churn-signal/usage-history-snapshot/plan_20260722.md>) — Implementation Plan — usage-history-snapshot: Storage only. No trend, no score change, no API. Backend model + worker mirror + migration + Venvs installed and verified: backend `services/backend-api/venv` (py3.12),
- [spec.md](<planning/usage-trend-churn-signal/usage-history-snapshot/spec.md>) — Aspect Spec — usage-history-snapshot: `customer_usage` is one **mutable** row per `(organization_id, customer_email)` — it records the customer's usage *now* and keeps nothing about the customer's usage *then*. There is therefore…

## `docs/planning/worker-cleanup-smalls`

[Directory guide](<planning/worker-cleanup-smalls/directory.md>)

- [plan_20260818.md](<planning/worker-cleanup-smalls/plan_20260818.md>) — Implementation plan — worker-cleanup-smalls (2026-08-18): Source: `docs/planning/worker-cleanup-smalls/prd.md`. House commit style. - `services/worker-service/src/tasks/anomaly.py` — delete `_send_anomaly_slack`
- [prd.md](<planning/worker-cleanup-smalls/prd.md>) — PRD — Worker cleanup: dead anomaly-alert functions (P6): `_send_anomaly_slack` (anomaly.py:238-310) and `_send_anomaly_discord` (anomaly.py:313-363) are fully implemented and **never called** — anomaly alerts

## `docs/planning/zendesk-integration`

[Directory guide](<planning/zendesk-integration/directory.md>)

- [prd.md](<planning/zendesk-integration/prd.md>) — PRD — Zendesk Inbound Feedback-Source Integration: Support tickets are the single richest, highest-intent customer-feedback channel for most SaaS teams, and **Zendesk is the most widely used support platform**. Rereflect already…

## `docs/planning/zendesk-integration/backend-connection`

[Directory guide](<planning/zendesk-integration/backend-connection/directory.md>)

- [_impl-report.md](<planning/zendesk-integration/backend-connection/_impl-report.md>) — Implementation report — Zendesk backend-connection aspect: Implemented the Zendesk BYOK connection slice end-to-end, mirroring the Jira Ran `alembic heads` **twice** (once before writing the migration, once again
- [plan_20260705.md](<planning/zendesk-integration/backend-connection/plan_20260705.md>) — Plan — Zendesk backend-connection (aspect): This plan covers **only** the backend-connection aspect per `docs/planning/zendesk-integration/backend-connection/spec.md`: the
- [spec.md](<planning/zendesk-integration/backend-connection/spec.md>) — Aspect: backend-connection: Fernet-encrypted `api_token` (+ encrypted nullable `webhook_secret`), `subdomain`, `email`, `token_hint`, identity (`account_user_id`, `display_name`), `is_active`, `last_synced_at`,

## `docs/planning/zendesk-integration/frontend`

[Directory guide](<planning/zendesk-integration/frontend/directory.md>)

- [_impl-report.md](<planning/zendesk-integration/frontend/_impl-report.md>) — Implementation report — Zendesk frontend aspect: Implemented the Zendesk connect UI end-to-end, mirroring the Jira token-paste integration precisely, plus the two genuinely-new behaviors the plan called
- [plan_20260705.md](<planning/zendesk-integration/frontend/plan_20260705.md>) — Plan — frontend (2026-07-05): (`POST/GET/DELETE /api/v1/integrations/zendesk/{connect,status,disconnect,test}`, `zendesk` in `feedback_sources.py` `/types` + `valid_types`, auto-provisioned `zendesk`
- [spec.md](<planning/zendesk-integration/frontend/spec.md>) — Aspect: frontend: `ZendeskConnect{Request,Response}`, `ZendeskDisconnectResponse`, `ZendeskTestResponse`, and `zendeskAPI.{connect,getStatus,disconnect,testConnection}` → `/api/v1/integrations/zendesk/*`.

## `docs/planning/zendesk-integration/ingestion-core`

[Directory guide](<planning/zendesk-integration/ingestion-core/directory.md>)

- [_impl-report.md](<planning/zendesk-integration/ingestion-core/_impl-report.md>) — Implementation Report — ingestion-core (Zendesk): Each `feat(zendesk)` commit corresponds 1:1 to a plan phase (1–6), built strict RED→GREEN (test written and confirmed failing before the production code was
- [plan_20260705.md](<planning/zendesk-integration/ingestion-core/plan_20260705.md>) — Implementation Plan — ingestion-core: backend). **Blocks:** `ingestion-pull`, `ingestion-webhook`. `services/worker-service` only: `src/adapters/zendesk.py` (new), `src/adapters/__init__.py`
- [spec.md](<planning/zendesk-integration/ingestion-core/spec.md>) — Aspect: ingestion-core: `FeedbackItem`. Both entry points (pull, webhook) funnel through this. - `check_triggers(event_type, event_data, triggers)` — match configured triggers (new-ticket;

## `docs/planning/zendesk-integration/ingestion-pull`

[Directory guide](<planning/zendesk-integration/ingestion-pull/directory.md>)

- [_impl-report.md](<planning/zendesk-integration/ingestion-pull/_impl-report.md>) — Implementation Report — ingestion-pull (Zendesk): Each commit was built strict RED→GREEN (test file written and confirmed failing via `ModuleNotFoundError`/404 before the corresponding production
- [plan_20260705.md](<planning/zendesk-integration/ingestion-pull/plan_20260705.md>) — Plan — Zendesk Integration: `ingestion-pull` aspect: `docs/planning/zendesk-integration/ingestion-pull/spec.md`, `docs/planning/zendesk-integration/ingestion-core/spec.md`.
- [spec.md](<planning/zendesk-integration/ingestion-pull/spec.md>) — Aspect: ingestion-pull (default entry point): tickets through the ingestion core. Works with no public ingress — the default for self-host. `tasks/integrations.py`; retire/leave-unwired that stub):

## `docs/planning/zendesk-integration/ingestion-webhook`

[Directory guide](<planning/zendesk-integration/ingestion-webhook/directory.md>)

- [_impl-report.md](<planning/zendesk-integration/ingestion-webhook/_impl-report.md>) — Implementation Report — ingestion-webhook (Zendesk real-time entry point): `backend-connection`, `ingestion-core`, and `ingestion-pull` aspects) RED tests for all five plan phases were written up front in one file
- [plan_20260705.md](<planning/zendesk-integration/ingestion-webhook/plan_20260705.md>) — Implementation Plan — ingestion-webhook (Zendesk real-time entry point) (2026-07-05): auto-provisioned `zendesk` FeedbackSource) and **ingestion-core** (`ZendeskAdapter`, `_find_matching_sources` zendesk branch in…
- [spec.md](<planning/zendesk-integration/ingestion-webhook/spec.md>) — Aspect: ingestion-webhook (optional real-time entry point): in real time, reusing the ingestion core. Optional accelerator on top of pull. `X-Zendesk-Webhook-Signature-Timestamp` + **raw body**)); compare against the integration's

## `docs/planning/zendesk-integration/landing-docs`

[Directory guide](<planning/zendesk-integration/landing-docs/directory.md>)

- [_impl-report.md](<planning/zendesk-integration/landing-docs/_impl-report.md>) — Implementation Report — Zendesk landing-docs (flip to "available"): Flipped the Zendesk marketing surface from "coming soon" to a shipped/"available" integration and documented operator setup for self-hosters. Copy/data/docs only…
- [plan_20260705.md](<planning/zendesk-integration/landing-docs/plan_20260705.md>) — Tech Plan — Zendesk landing-docs (flip to "available"): Sources: `docs/planning/zendesk-integration/prd.md`, `docs/planning/zendesk-integration/landing-docs/spec.md`. Flip the marketing surface for Zendesk from "coming soon" to a…
- [spec.md](<planning/zendesk-integration/landing-docs/spec.md>) — Aspect: landing-docs: `'available'`; fill `useCases` and `setupSteps` (connect via subdomain+email+token; optional full available layout (mirror `app/integrations/intercom/page.tsx` — hero, how-it-works,

## `docs/planning/zendesk-status-sync`

[Directory guide](<planning/zendesk-status-sync/directory.md>)

- [prd.md](<planning/zendesk-status-sync/prd.md>) — PRD — Inbound Zendesk Status-Sync: Rereflect's Zendesk integration is **one-way**: support tickets flow *in* and become feedback items, but when an agent resolves or progresses a ticket **in Zendesk**, the linked Rereflect…

## `docs/planning/zendesk-status-sync/backend-routes`

[Directory guide](<planning/zendesk-status-sync/backend-routes/directory.md>)

- [plan_20260712.md](<planning/zendesk-status-sync/backend-routes/plan_20260712.md>) — Plan — backend-routes (2026-07-12)
- [spec.md](<planning/zendesk-status-sync/backend-routes/spec.md>) — Aspect: backend-routes: Operator control surface: toggle status-sync on/off (+ set the per-org mapping override), trigger a manual "Sync now", and expose sync state on `GET /status`. Mirrors

## `docs/planning/zendesk-status-sync/client-batch-status`

[Directory guide](<planning/zendesk-status-sync/client-batch-status/directory.md>)

- [plan_20260712.md](<planning/zendesk-status-sync/client-batch-status/plan_20260712.md>) — Plan — client-batch-status (2026-07-12)
- [spec.md](<planning/zendesk-status-sync/client-batch-status/spec.md>) — Aspect: client-batch-status: Add the one genuinely-missing capability: fetch the current status of a set of Zendesk tickets by ID in batches, reusing the existing auth + throttle behavior.

## `docs/planning/zendesk-status-sync/frontend`

[Directory guide](<planning/zendesk-status-sync/frontend/directory.md>)

- [plan_20260712.md](<planning/zendesk-status-sync/frontend/plan_20260712.md>) — Plan — frontend (2026-07-12): - `patchZendeskStatusSync(enabled: boolean, statusMapping?: Record<string,string>)` → `apiClient.patch('/api/v1/integrations/zendesk/status-sync', { enabled, ...(statusMapping ? { status_mapping:…
- [spec.md](<planning/zendesk-status-sync/frontend/spec.md>) — Aspect: frontend: Admin/owner UI to control Zendesk status-sync on the Zendesk settings page: a toggle, a last-synced/ error indicator, and a "Sync Now" button — a direct clone of `JiraStatusSyncCard`.

## `docs/planning/zendesk-status-sync/poll-task`

[Directory guide](<planning/zendesk-status-sync/poll-task/directory.md>)

- [plan_20260712.md](<planning/zendesk-status-sync/poll-task/plan_20260712.md>) — Plan — poll-task (2026-07-12): - guards not_found / inactive / disabled (re-check `status_sync_enabled`). - per-run cap (mirror ingest `PER_RUN_PAGE_CAP`): cap the number of ids processed per beat.
- [spec.md](<planning/zendesk-status-sync/poll-task/spec.md>) — Aspect: poll-task: The 15-minute poll-first reconcile: fan out per opted-in org, batch-fetch linked tickets' statuses, reconcile via the shared core, and apply changes with a source-tagged timeline event. Mirrors

## `docs/planning/zendesk-status-sync/reconcile-core-and-model`

[Directory guide](<planning/zendesk-status-sync/reconcile-core-and-model/directory.md>)

- [plan_20260712.md](<planning/zendesk-status-sync/reconcile-core-and-model/plan_20260712.md>) — Plan — reconcile-core-and-model (2026-07-12): - mapping defaults (all 6 statuses), override merge, unknown status → None, bad target → None
- [spec.md](<planning/zendesk-status-sync/reconcile-core-and-model/spec.md>) — Aspect: reconcile-core-and-model: The pure, I/O-free heart of Zendesk status-sync: map a Zendesk ticket status → Rereflect `workflow_status`, decide seed/noop/changed against the last-observed status, and the persistence

## `docs/planning/zendesk-status-sync/webhook-realtime`

[Directory guide](<planning/zendesk-status-sync/webhook-realtime/directory.md>)

- [dig.md](<planning/zendesk-status-sync/webhook-realtime/dig.md>) — Phase 0 dig — webhook-realtime event shape (GO)
- [plan_20260712.md](<planning/zendesk-status-sync/webhook-realtime/plan_20260712.md>) — Plan — webhook-realtime (2026-07-12)
- [spec.md](<planning/zendesk-status-sync/webhook-realtime/spec.md>) — Aspect: webhook-realtime: Near-real-time status-sync: when Zendesk sends a ticket-update webhook, reconcile that single ticket's status immediately (subject to the same opt-in + change-gate), instead of waiting for the 15-min…

## `packages`

[Directory guide](<../packages/directory.md>)

No immediate baseline/preparation files.

## `packages/ui`

[Directory guide](<../packages/ui/directory.md>)

- [package.json](<../packages/ui/package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [tailwind.config.ts](<../packages/ui/tailwind.config.ts>) — Static/configuration artifact; inspect its consumer.
- [tsconfig.json](<../packages/ui/tsconfig.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## `packages/ui/src`

[Directory guide](<../packages/ui/src/directory.md>)

- [index.ts](<../packages/ui/src/index.ts>) — Static/configuration artifact; inspect its consumer.
- [utils.ts](<../packages/ui/src/utils.ts>) — Declarations: cn

## `packages/ui/src/components`

[Directory guide](<../packages/ui/src/components/directory.md>)

- [Logo.tsx](<../packages/ui/src/components/Logo.tsx>) — Declarations: Logo, LogoWithText
- [select.tsx](<../packages/ui/src/components/select.tsx>) — Static/configuration artifact; inspect its consumer.

## `packages/ui/src/styles`

[Directory guide](<../packages/ui/src/styles/directory.md>)

- [globals.css](<../packages/ui/src/styles/globals.css>) — Static/configuration artifact; inspect its consumer.

## `scripts`

[Directory guide](<../scripts/directory.md>)

- [check_docs_honesty.sh](<../scripts/check_docs_honesty.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [prospect.py](<../scripts/prospect.py>) — Prospect research helper for Rereflect outreach. Usage: python3 scripts/prospect.py add # Add a new prospect interactively python3 scripts/prospect.py dm # Generate personalized DMs for…

## `services`

[Directory guide](<../services/directory.md>)

- [.dockerignore](<../services/.dockerignore>) — Static/configuration artifact; inspect its consumer.

## `services/analysis-engine`

[Directory guide](<../services/analysis-engine/directory.md>)

- [.env.example](<../services/analysis-engine/.env.example>) — Static/configuration artifact; inspect its consumer.
- [README.md](<../services/analysis-engine/README.md>) — Analysis Engine: Core analysis engine that processes customer feedback using: This service is **production-ready** and powers the entire SaaS platform.
- [quickstart.sh](<../services/analysis-engine/quickstart.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [requirements.txt](<../services/analysis-engine/requirements.txt>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.

## `services/analysis-engine/examples`

[Directory guide](<../services/analysis-engine/examples/directory.md>)

- [analysis_output.json](<../services/analysis-engine/examples/analysis_output.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [api_example.py](<../services/analysis-engine/examples/api_example.py>) — Example of using the API with requests.
- [sample_data.json](<../services/analysis-engine/examples/sample_data.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [usage_example.py](<../services/analysis-engine/examples/usage_example.py>) — Example usage of the feedback analyzer.

## `services/analysis-engine/src`

[Directory guide](<../services/analysis-engine/src/directory.md>)

- [__init__.py](<../services/analysis-engine/src/__init__.py>) — Customer feedback analyzer package.

## `services/analysis-engine/src/analyzer`

[Directory guide](<../services/analysis-engine/src/analyzer/directory.md>)

- [__init__.py](<../services/analysis-engine/src/analyzer/__init__.py>) — Feedback analyzer package.
- [categorizer.py](<../services/analysis-engine/src/analyzer/categorizer.py>) — Categorizers for pain points, feature requests, and urgent feedback.
- [core.py](<../services/analysis-engine/src/analyzer/core.py>) — Core feedback analyzer implementation.
- [extractors.py](<../services/analysis-engine/src/analyzer/extractors.py>) — Extractors for pain points, feature requests, and patterns.
- [models.py](<../services/analysis-engine/src/analyzer/models.py>) — Data models for feedback analysis.
- [sentiment.py](<../services/analysis-engine/src/analyzer/sentiment.py>) — Sentiment analysis — composes a pluggable SentimentProvider with provider-independent label / is_extreme / churn_risk logic. Default provider ('vader') is byte-identical to the…
- [tag_extractor.py](<../services/analysis-engine/src/analyzer/tag_extractor.py>) — Tag extraction module for categorizing feedback.

## `services/analysis-engine/src/analyzer/churn_classifier`

[Directory guide](<../services/analysis-engine/src/analyzer/churn_classifier/directory.md>)

- [__init__.py](<../services/analysis-engine/src/analyzer/churn_classifier/__init__.py>) — Per-org churn classifier core — pure-compute head for the M5.3 ML challenger. CPU-only, offline, per-org logistic-regression churn classifier built on the leakage-free A/B spine of…
- [dataset.py](<../services/analysis-engine/src/analyzer/churn_classifier/dataset.py>) — Churn dataset builder (M5.3 churn-classifier-core). Split into a pure transform (`rows_to_dataset`) and a lazy-SQL fetch seam (`fetch_churn_rows`), mirroring…
- [evaluate.py](<../services/analysis-engine/src/analyzer/churn_classifier/evaluate.py>) — Shadow-A/B evaluate for the churn head (M5.3 churn-classifier-core). Runs the incumbent-vs-challenger shootout on a held-out split (stratified; k-fold when tiny) and returns the…
- [features.py](<../services/analysis-engine/src/analyzer/churn_classifier/features.py>) — Frozen churn feature vector builder (M5.3 churn-classifier-core). The FROZEN field set (fixed by the gate study, aspect 2, and locked here — see tests/churn_classifier/test_features.py):…
- [labels.py](<../services/analysis-engine/src/analyzer/churn_classifier/labels.py>) — Locked knobs for the per-org churn classifier core (M5.3, aspect 3). Every constant here is parity-pinned to its source-of-truth definition in the pre-existing churn calibration path — see…
- [metrics.py](<../services/analysis-engine/src/analyzer/churn_classifier/metrics.py>) — Binary churn metrics — pure stdlib (M5.3 churn-classifier-core). `compute_binary_metrics` mirrors the corrections_classifier/metrics.py style (threshold-derived counts, every division…
- [predict.py](<../services/analysis-engine/src/analyzer/churn_classifier/predict.py>) — Pure-stdlib churn predict from JSON artifact (M5.3 churn-classifier-core). Reconstructs the binary logistic decision from a trainer.py JSON artifact WITHOUT sklearn/numpy — stdlib only…
- [trainer.py](<../services/analysis-engine/src/analyzer/churn_classifier/trainer.py>) — Churn logistic-regression trainer — JSON-only artifact (M5.3 churn-classifier-core). Serializes ONLY to JSON-native types (never pickle): the linear-logistic coefficients/intercept + the…

## `services/analysis-engine/src/analyzer/corrections_classifier`

[Directory guide](<../services/analysis-engine/src/analyzer/corrections_classifier/directory.md>)

- [__init__.py](<../services/analysis-engine/src/analyzer/corrections_classifier/__init__.py>) — Per-org sentiment and category corrections classifier — pure-compute core (M5.2). CPU-only, offline, per-org TF-IDF + logistic-regression classifier, mirroring the churn split…
- [dataset.py](<../services/analysis-engine/src/analyzer/corrections_classifier/dataset.py>) — Corrections dataset builder — task-generic (sentiment + category), Phase 1 (M5.2 training-and-eval-core). Split into a pure transform (`rows_to_dataset`) and a lazy-SQL fetch seam…
- [evaluate.py](<../services/analysis-engine/src/analyzer/corrections_classifier/evaluate.py>) — Shadow-A/B evaluate — Phase 4b (M5.2 training-and-eval-core). Runs the incumbent-vs-challenger shootout on a held-out split (stratified; k-fold when tiny) and returns the…
- [labels.py](<../services/analysis-engine/src/analyzer/corrections_classifier/labels.py>) — Fixed sentiment label vocabulary + locked knobs for the corrections classifier (M5.2). `SENTIMENT_LABELS` is sorted so it matches sklearn's `classes_` ordering when the trainer fits on…
- [metrics.py](<../services/analysis-engine/src/analyzer/corrections_classifier/metrics.py>) — Multiclass confusion-matrix metrics — Phase 4a (M5.2 training-and-eval-core). VERBATIM port of `_safe_precision_recall_f1_accuracy` / `confusion_to_binary_counts` /…
- [predict.py](<../services/analysis-engine/src/analyzer/corrections_classifier/predict.py>) — Pure-Python predict-from-JSON — Phase 3 (M5.2 training-and-eval-core). Reconstructs the TF-IDF + logistic-regression decision from a JSON artifact (see trainer.py's schema) WITHOUT…
- [trainer.py](<../services/analysis-engine/src/analyzer/corrections_classifier/trainer.py>) — TF-IDF + logistic-regression trainer — Phase 2 (M5.2 training-and-eval-core). Serializes ONLY to JSON-native types (never pickle) — vocabulary/idf weights + logreg coef_/intercept_/classes_…

## `services/analysis-engine/src/analyzer/sentiment_providers`

[Directory guide](<../services/analysis-engine/src/analyzer/sentiment_providers/directory.md>)

- [__init__.py](<../services/analysis-engine/src/analyzer/sentiment_providers/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [base.py](<../services/analysis-engine/src/analyzer/sentiment_providers/base.py>) — Declarations: SentimentScore, SentimentProvider
- [factory.py](<../services/analysis-engine/src/analyzer/sentiment_providers/factory.py>) — Declarations: SentimentProviderFactory

## `services/analysis-engine/src/analyzer/sentiment_providers/providers`

[Directory guide](<../services/analysis-engine/src/analyzer/sentiment_providers/providers/directory.md>)

- [__init__.py](<../services/analysis-engine/src/analyzer/sentiment_providers/providers/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [transformer.py](<../services/analysis-engine/src/analyzer/sentiment_providers/providers/transformer.py>) — Declarations: _get_model_and_tokenizer, TransformerSentimentProvider
- [vader.py](<../services/analysis-engine/src/analyzer/sentiment_providers/providers/vader.py>) — Declarations: VaderSentimentProvider

## `services/analysis-engine/src/api`

[Directory guide](<../services/analysis-engine/src/api/directory.md>)

- [__init__.py](<../services/analysis-engine/src/api/__init__.py>) — API package.
- [main.py](<../services/analysis-engine/src/api/main.py>) — FastAPI application for feedback analysis. · Routes: GET /; GET /health; POST /api/v1/analyze; POST /api/v1/analyze/quick

## `services/analysis-engine/tests`

[Directory guide](<../services/analysis-engine/tests/directory.md>)

- [__init__.py](<../services/analysis-engine/tests/__init__.py>) — Tests package.
- [test_analyzer.py](<../services/analysis-engine/tests/test_analyzer.py>) — Tests for the main analyzer.
- [test_api.py](<../services/analysis-engine/tests/test_api.py>) — Tests for the API endpoints.
- [test_custom_categorizer.py](<../services/analysis-engine/tests/test_custom_categorizer.py>) — TDD tests for Feature B1: custom category augmentation of keyword categorisers. Tests cover PainPointCategorizer, FeatureRequestCategorizer, and UrgentCategorizer after the…
- [test_extractors.py](<../services/analysis-engine/tests/test_extractors.py>) — Tests for extractors.
- [test_sentiment.py](<../services/analysis-engine/tests/test_sentiment.py>) — Tests for sentiment analyzer.
- [test_sentiment_characterization.py](<../services/analysis-engine/tests/test_sentiment_characterization.py>) — Characterization test — pins SentimentAnalyzer().analyze()'s exact output for a fixed set of inputs, against the pre-refactor sentiment.py. This is the load-bearing safety net for the…
- [test_sentiment_fallback.py](<../services/analysis-engine/tests/test_sentiment_fallback.py>) — Tests for SentimentAnalyzer's runtime fallback to VADER when the configured provider's score() raises (PRD #9) — analyze() must never raise.

## `services/analysis-engine/tests/churn_classifier`

[Directory guide](<../services/analysis-engine/tests/churn_classifier/directory.md>)

- [__init__.py](<../services/analysis-engine/tests/churn_classifier/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [conftest.py](<../services/analysis-engine/tests/churn_classifier/conftest.py>) — Test-environment shim — NOT part of the churn_classifier public surface. Mirror of tests/corrections_classifier/conftest.py: `src/analyzer/__init__.py` eagerly imports FeedbackAnalyzer ->…
- [test_dataset.py](<../services/analysis-engine/tests/churn_classifier/test_dataset.py>) — Tests for churn_classifier.dataset (M5.3 churn-classifier-core). `rows_to_dataset` is pure (plain dicts in, no DB). `fetch_churn_rows` needs sqlalchemy — guarded with `pytest.importorskip`…
- [test_evaluate.py](<../services/analysis-engine/tests/churn_classifier/test_evaluate.py>) — Tests for churn_classifier.evaluate (M5.3 churn-classifier-core). `evaluate_churn` runs the incumbent-vs-challenger A/B on a leakage-free stratified holdout (k-fold when tiny), scoring BOTH…
- [test_features.py](<../services/analysis-engine/tests/churn_classifier/test_features.py>) — Tests for churn_classifier.features (M5.3 churn-classifier-core). Pins the FROZEN feature vector — the field set fixed by the gate study (aspect 2) and locked here: 6 health components +…
- [test_labels.py](<../services/analysis-engine/tests/churn_classifier/test_labels.py>) — Tests for churn_classifier.labels (M5.3 churn-classifier-core). Every constant here is parity-pinned to its source-of-truth definition elsewhere in the repo (the churn calibration path that…
- [test_lazy_import.py](<../services/analysis-engine/tests/churn_classifier/test_lazy_import.py>) — Proves sklearn/numpy are truly optional at import time for churn_classifier (mirror of tests/corrections_classifier/test_lazy_import.py). Only train_churn_classifier needs them, and it…
- [test_metrics.py](<../services/analysis-engine/tests/churn_classifier/test_metrics.py>) — Tests for churn_classifier.metrics (M5.3 churn-classifier-core). Hand-computed golden tests for `compute_binary_metrics` (positive-class precision/recall/F1 at the 0.5 threshold, rank-based…
- [test_predict.py](<../services/analysis-engine/tests/churn_classifier/test_predict.py>) — Tests for churn_classifier.predict (M5.3 churn-classifier-core). predict() is pure stdlib (math.sigmoid of the linear score) — no sklearn/numpy at runtime, even though the sklearn-parity…
- [test_trainer.py](<../services/analysis-engine/tests/churn_classifier/test_trainer.py>) — Tests for churn_classifier.trainer (M5.3 churn-classifier-core). Guards the whole file with pytest.importorskip("sklearn") so wheels-less venvs skip training tests entirely…

## `services/analysis-engine/tests/corrections_classifier`

[Directory guide](<../services/analysis-engine/tests/corrections_classifier/directory.md>)

- [__init__.py](<../services/analysis-engine/tests/corrections_classifier/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [conftest.py](<../services/analysis-engine/tests/corrections_classifier/conftest.py>) — Test-environment shim — NOT part of the corrections_classifier public surface. `src/analyzer/__init__.py` eagerly imports `FeedbackAnalyzer` -> `core` -> `sentiment` ->…
- [test_dataset.py](<../services/analysis-engine/tests/corrections_classifier/test_dataset.py>) — Tests for corrections_classifier.dataset — Phase 1 (M5.2 training-and-eval-core). `rows_to_dataset` is pure (plain dicts in, no DB). `fetch_sentiment_correction_rows` /…
- [test_evaluate.py](<../services/analysis-engine/tests/corrections_classifier/test_evaluate.py>) — Tests for corrections_classifier.evaluate — Phase 4b (M5.2 training-and-eval-core). `evaluate` itself is pure (predict/metrics are pure stdlib), but it now TRAINS the challenger itself via…
- [test_labels.py](<../services/analysis-engine/tests/corrections_classifier/test_labels.py>) — Tests for corrections_classifier.labels — urgency-core (M urgency-classifier-head). `URGENCY_LABELS` is a fixed, lexicographically-sorted binary vocab — mirrors `SENTIMENT_LABELS`'s…
- [test_lazy_import.py](<../services/analysis-engine/tests/corrections_classifier/test_lazy_import.py>) — Proves sklearn/numpy are truly optional at import time for corrections_classifier (mirror of tests/sentiment_providers/test_lazy_import.py). Only train_classifier needs them, and it imports…
- [test_metrics_parity.py](<../services/analysis-engine/tests/corrections_classifier/test_metrics_parity.py>) — Parity anchor for corrections_classifier.metrics — Phase 4a (M5.2 training-and-eval-core). metrics.py is a VERBATIM port of `_safe_precision_recall_f1_accuracy` /…
- [test_predict.py](<../services/analysis-engine/tests/corrections_classifier/test_predict.py>) — Tests for corrections_classifier.predict — Phase 3 (M5.2 training-and-eval-core). predict() and score_from_proba() are pure stdlib (re, math) — no sklearn/numpy needed at runtime, even…
- [test_trainer.py](<../services/analysis-engine/tests/corrections_classifier/test_trainer.py>) — Tests for corrections_classifier.trainer — Phase 2 (M5.2 training-and-eval-core). Guards the whole file with pytest.importorskip("sklearn") so the wheels-less CI venv (worker-service…
- [test_urgency_end_to_end.py](<../services/analysis-engine/tests/corrections_classifier/test_urgency_end_to_end.py>) — Cross-cutting sanity: binary urgency train/predict/evaluate end-to-end — urgency-core (Phase 4, M urgency-classifier-head). Test-only phase: proves the untouched trainer/predict/evaluate…

## `services/analysis-engine/tests/sentiment_providers`

[Directory guide](<../services/analysis-engine/tests/sentiment_providers/directory.md>)

- [__init__.py](<../services/analysis-engine/tests/sentiment_providers/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [test_base.py](<../services/analysis-engine/tests/sentiment_providers/test_base.py>) — Tests for the SentimentProvider ABC + SentimentScore contract (AC3).
- [test_factory.py](<../services/analysis-engine/tests/sentiment_providers/test_factory.py>) — Tests for SentimentProviderFactory — name -> provider dispatch (AC7).
- [test_lazy_import.py](<../services/analysis-engine/tests/sentiment_providers/test_lazy_import.py>) — Proves torch/transformers are truly optional at import time — the vader path never requires them; requesting/constructing the transformer provider is fine, only scoring with it needs them…
- [test_transformer_provider.py](<../services/analysis-engine/tests/sentiment_providers/test_transformer_provider.py>) — Tests for TransformerSentimentProvider — mocked model/tokenizer, no real weights/download (AC4, AC10, AC11).
- [test_vader_provider.py](<../services/analysis-engine/tests/sentiment_providers/test_vader_provider.py>) — Tests for VaderSentimentProvider — proves the extraction adds zero transformation vs. calling vaderSentiment directly (AC3).

## `services/backend-api`

[Directory guide](<../services/backend-api/directory.md>)

- [.env.example](<../services/backend-api/.env.example>) — Static/configuration artifact; inspect its consumer.
- [Dockerfile](<../services/backend-api/Dockerfile>) — Static/configuration artifact; inspect its consumer.
- [README.md](<../services/backend-api/README.md>) — Backend API
- [alembic.ini](<../services/backend-api/alembic.ini>) — Static/configuration artifact; inspect its consumer.
- [pytest.ini](<../services/backend-api/pytest.ini>) — Static/configuration artifact; inspect its consumer.
- [railway.toml](<../services/backend-api/railway.toml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [reanalyze_all.py](<../services/backend-api/reanalyze_all.py>) — Script to re-analyze all existing feedback items. Use this after updating the analysis logic to apply it to existing data.
- [reanalyze_for_pain_points.py](<../services/backend-api/reanalyze_for_pain_points.py>) — Re-analyze all existing feedback to extract pain points. This is needed because the pain point extraction was added after initial analysis.
- [requirements.txt](<../services/backend-api/requirements.txt>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [start.sh](<../services/backend-api/start.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [test_api.sh](<../services/backend-api/test_api.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [test_week2.sh](<../services/backend-api/test_week2.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.

## `services/backend-api/alembic`

[Directory guide](<../services/backend-api/alembic/directory.md>)

- [README](<../services/backend-api/alembic/README>) — Static/configuration artifact; inspect its consumer.
- [env.py](<../services/backend-api/alembic/env.py>) — Declarations: run_migrations_offline, run_migrations_online
- [script.py.mako](<../services/backend-api/alembic/script.py.mako>) — Static/configuration artifact; inspect its consumer.

## `services/backend-api/alembic/versions`

[Directory guide](<../services/backend-api/alembic/versions/directory.md>)

- [093c65b07d95_fix_slack_alert_logs_feedback_id_.py](<../services/backend-api/alembic/versions/093c65b07d95_fix_slack_alert_logs_feedback_id_.py>) — fix slack_alert_logs feedback_id ondelete set null Revision ID: 093c65b07d95 Revises: d3e4f5g6h7i8 Create Date: 2026-02-13 03:11:17.940274
- [0a3382154c27_add_usage_churn_label_config.py](<../services/backend-api/alembic/versions/0a3382154c27_add_usage_churn_label_config.py>) — add_usage_churn_label_config Revision ID: 0a3382154c27 Revises: a1c2d3e4f5a6 Create Date: 2026-07-23 00:00:00.000000 usage-decline-churn-labels — config-and-migration aspect. Adds…
- [0bf182dad44d_playbook_tasks_table.py](<../services/backend-api/alembic/versions/0bf182dad44d_playbook_tasks_table.py>) — playbook tasks table Revision ID: 0bf182dad44d Revises: fb57e62a2820 Create Date: 2026-08-27 02:57:08.281148 playbook-action-types M3 — durable follow-up tasks created by create_task /…
- [12a1003fbfe0_shadow_repaired_automation_triggers.py](<../services/backend-api/alembic/versions/12a1003fbfe0_shadow_repaired_automation_triggers.py>) — shadow_repaired_automation_triggers Revision ID: 12a1003fbfe0 Revises: b2262e51eeb5 Create Date: 2026-07-29 02:01:49.626081 Phase 4 of the worker-trigger-mirror aspect…
- [16905e989875_add_usage_event.py](<../services/backend-api/alembic/versions/16905e989875_add_usage_event.py>) — add_usage_event Revision ID: 16905e989875 Revises: z5a6b7c8d9e0 Create Date: 2026-06-28 21:29:20.783877 Creates the ``usage_events`` raw-log table for the product-usage ingestion receiver…
- [241f650d7068_add_active_days_14d_to_customer_usage.py](<../services/backend-api/alembic/versions/241f650d7068_add_active_days_14d_to_customer_usage.py>) — add active_days_14d to customer_usage Revision ID: 241f650d7068 Revises: u4v5w6x7y8z9 Create Date: 2026-07-21 21:19:14.137905 Adds the 14-day active-days window field used by the…
- [3cb9a0d1456b_add_churn_classifier_mode.py](<../services/backend-api/alembic/versions/3cb9a0d1456b_add_churn_classifier_mode.py>) — add_churn_classifier_mode Revision ID: 3cb9a0d1456b Revises: f6a7b8c9d0e1 Create Date: 2026-08-14 03:55:59.883435 per-org-churn-model (churn-predict-seam-resolver, data layer): -…
- [3e26b38cbd15_add_feedback_source_lookup_index.py](<../services/backend-api/alembic/versions/3e26b38cbd15_add_feedback_source_lookup_index.py>) — add feedback source lookup index Fix wave (post-review, zendesk-status-sync): both the worker's poll query (services/worker-service/src/tasks/zendesk_status_sync.py) and the webhook's…
- [4988b7bbd0b6_add_customer_usage_history.py](<../services/backend-api/alembic/versions/4988b7bbd0b6_add_customer_usage_history.py>) — add_customer_usage_history Revision ID: 4988b7bbd0b6 Revises: 241f650d7068 Create Date: 2026-07-22 01:30:07.249184 Creates the ``customer_usage_history`` table for the…
- [5ee1b2567a02_add_linear_integration_tables.py](<../services/backend-api/alembic/versions/5ee1b2567a02_add_linear_integration_tables.py>) — add_linear_integration_tables Revision ID: 5ee1b2567a02 Revises: n3o4p5q6r7s8 Create Date: 2026-03-08 02:15:55.284090
- [65fe1d5fdc48_initial_schema_organizations_users_.py](<../services/backend-api/alembic/versions/65fe1d5fdc48_initial_schema_organizations_users_.py>) — Initial schema - organizations, users, feedback Revision ID: 65fe1d5fdc48 Revises: Create Date: 2025-12-27 15:08:16.373890
- [6ad1dc4335f1_add_sentiment_provider.py](<../services/backend-api/alembic/versions/6ad1dc4335f1_add_sentiment_provider.py>) — add_sentiment_provider Revision ID: 6ad1dc4335f1 Revises: a6b703d7a303 Create Date: 2026-07-10 13:51:52.679933 Adds the per-org sentiment engine opt-in (local-analyzer-sentiment-model,…
- [6d7e00e682c7_add_segment_to_customer_health.py](<../services/backend-api/alembic/versions/6d7e00e682c7_add_segment_to_customer_health.py>) — add segment to customer_health_scores Adds a `segment` column (nullable String(30)) to `customer_health_scores` for the rule-based customer segment classifier (at_risk, silent_churner,…
- [6e4501930bf0_add_churn_risk_factors_and_confidence_.py](<../services/backend-api/alembic/versions/6e4501930bf0_add_churn_risk_factors_and_confidence_.py>) — add_churn_risk_factors_and_confidence_score Revision ID: 6e4501930bf0 Revises: g0h1i2j3k4l5 Create Date: 2026-02-21 02:07:21.189405
- [719deb6ac0a0_org_ai_config_autopromote_hold_flags.py](<../services/backend-api/alembic/versions/719deb6ac0a0_org_ai_config_autopromote_hold_flags.py>) — org_ai_config autopromote_hold flags Revision ID: 719deb6ac0a0 Revises: 0a3382154c27 Create Date: 2026-07-24 19:48:29.446881
- [8114adde5d96_intercom_integrations.py](<../services/backend-api/alembic/versions/8114adde5d96_intercom_integrations.py>) — intercom_integrations Revision ID: 8114adde5d96 Revises: 12a1003fbfe0 Create Date: 2026-07-31 12:56:01.487362 Adds the per-org Intercom connection table for the token-paste connect path…
- [8bbf7dfee1e9_merge_embedding_model_and_classifier_.py](<../services/backend-api/alembic/versions/8bbf7dfee1e9_merge_embedding_model_and_classifier_.py>) — merge embedding_model and classifier-versioning heads Revision ID: 8bbf7dfee1e9 Revises: 719deb6ac0a0, hbsh5o3gbwv4 Create Date: 2026-07-25 13:51:24.096807
- [8ceaecca3d8e_add_provider_to_crm_enrichment.py](<../services/backend-api/alembic/versions/8ceaecca3d8e_add_provider_to_crm_enrichment.py>) — add provider to crm_enrichment Revision ID: 8ceaecca3d8e Revises: d4e5f6a7b8c9 Create Date: 2026-07-01 16:48:07.548159 Adds crm_enrichment.provider (crm-provider-generalization, aspect 1 of…
- [9214a01bdb16_add_notifications_and_alert_preferences.py](<../services/backend-api/alembic/versions/9214a01bdb16_add_notifications_and_alert_preferences.py>) — add_notifications_and_alert_preferences Revision ID: 9214a01bdb16 Revises: m3n4o5p6q7r8 Create Date: 2026-02-08 01:06:08.612602
- [9232cfa0634d_add_critical_feedback_indexes.py](<../services/backend-api/alembic/versions/9232cfa0634d_add_critical_feedback_indexes.py>) — add_critical_feedback_indexes Revision ID: 9232cfa0634d Revises: 093c65b07d95 Create Date: 2026-02-15 01:36:27.356609
- [9f2a1dfcdb55_add_tags_column_to_feedback.py](<../services/backend-api/alembic/versions/9f2a1dfcdb55_add_tags_column_to_feedback.py>) — add_tags_column_to_feedback Revision ID: 9f2a1dfcdb55 Revises: 65fe1d5fdc48 Create Date: 2025-12-27 19:46:34.784805
- [9f56f9a4f999_add_salesforce_integrations_table.py](<../services/backend-api/alembic/versions/9f56f9a4f999_add_salesforce_integrations_table.py>) — add salesforce_integrations table Revision ID: 9f56f9a4f999 Revises: 8ceaecca3d8e Create Date: 2026-07-01 17:30:00.000000 Adds the salesforce_integrations table (salesforce-connection,…
- [a1b2c3d4e5f6_add_categorization_columns.py](<../services/backend-api/alembic/versions/a1b2c3d4e5f6_add_categorization_columns.py>) — add_categorization_columns Revision ID: a1b2c3d4e5f6 Revises: 9f2a1dfcdb55 Create Date: 2025-12-28 10:00:00.000000
- [a1c2d3e4f5a6_add_trend_to_usage_history.py](<../services/backend-api/alembic/versions/a1c2d3e4f5a6_add_trend_to_usage_history.py>) — add_trend_to_usage_history Revision ID: a1c2d3e4f5a6 Revises: a5b63dbbce9b Create Date: 2026-07-23 00:00:00.000000 Adds the two trend columns for the snapshot-trend-columns aspect…
- [a2b3c4d5e6f7_add_automation_email_deliveries.py](<../services/backend-api/alembic/versions/a2b3c4d5e6f7_add_automation_email_deliveries.py>) — add_automation_email_deliveries Revision ID: a2b3c4d5e6f7 Revises: f5a6b7c8d9e0 Create Date: 2026-08-19 00:00:00.000000 automation-send-customer-email (action-core aspect, M3): -…
- [a4b5c6d7e8f9_add_customer_health_and_email.py](<../services/backend-api/alembic/versions/a4b5c6d7e8f9_add_customer_health_and_email.py>) — add customer_email to feedback_items and customer_health_scores table Revision ID: a4b5c6d7e8f9 Revises: 9232cfa0634d Create Date: 2026-02-16 00:00:00.000000
- [a5b63dbbce9b_add_usage_trend_fields.py](<../services/backend-api/alembic/versions/a5b63dbbce9b_add_usage_trend_fields.py>) — add_usage_trend_fields Revision ID: a5b63dbbce9b Revises: 4988b7bbd0b6 Create Date: 2026-07-22 03:10:00.000000 Adds the two trend columns for the trend-detection-and-health aspect…
- [a5b6c7d8e9f0_add_asana_integration_tables.py](<../services/backend-api/alembic/versions/a5b6c7d8e9f0_add_asana_integration_tables.py>) — add asana integration tables Creates asana_integrations (one row/org, Fernet-encrypted api_token, Bearer PAT auth against the fixed host https://app.asana.com/api/1.0 — no site_url/email…
- [a6b703d7a303_add_tags_and_cs_owner_to_customer_health.py](<../services/backend-api/alembic/versions/a6b703d7a303_add_tags_and_cs_owner_to_customer_health.py>) — add tags and cs_owner to customer_health Adds `tags` (JSON list of strings, nullable, app-level default `[]`) and `cs_owner_user_id` (nullable FK -> users.id, ondelete=SET NULL) to…
- [a6b7c8d9e0f1_add_hubspot_integrations_table.py](<../services/backend-api/alembic/versions/a6b7c8d9e0f1_add_hubspot_integrations_table.py>) — add_hubspot_integrations_table Revision ID: a6b7c8d9e0f1 Revises: a8b9c0d1e2f3 Create Date: 2026-06-30 00:00:00.000000 Creates the hubspot_integrations table for the hubspot-connection…
- [a7b8c9d0e1f2_notification_improvements.py](<../services/backend-api/alembic/versions/a7b8c9d0e1f2_notification_improvements.py>) — Notification improvements: digest scheduling, per-type retention. Revision ID: a7b8c9d0e1f2 Revises: 9214a01bdb16 Create Date: 2026-02-07
- [a8b9c0d1e2f3_add_customer_usage.py](<../services/backend-api/alembic/versions/a8b9c0d1e2f3_add_customer_usage.py>) — add_customer_usage Revision ID: a8b9c0d1e2f3 Revises: 16905e989875 Create Date: 2026-06-28 22:00:00.000000 Creates the ``customer_usage`` rollup table for the usage-rollup-and-score aspect…
- [a9b8c7d6e5f4_add_channel_discord_to_alert_prefs.py](<../services/backend-api/alembic/versions/a9b8c7d6e5f4_add_channel_discord_to_alert_prefs.py>) — Add channel_discord to user_alert_preferences. Revision ID: a9b8c7d6e5f4 Revises: 8114adde5d96 Create Date: 2026-08-09
- [ad76527a185e_add_channel_teams_to_user_alert_.py](<../services/backend-api/alembic/versions/ad76527a185e_add_channel_teams_to_user_alert_.py>) — add channel_teams to user alert preferences Revision ID: ad76527a185e Revises: 0bf182dad44d Create Date: 2026-09-02 16:57:20.107904
- [b1c2d3e4f5a6_add_analytics_tables.py](<../services/backend-api/alembic/versions/b1c2d3e4f5a6_add_analytics_tables.py>) — Add saved_views and shared_links tables for enhanced analytics. Revision ID: b1c2d3e4f5a6 Revises: a7b8c9d0e1f2 Create Date: 2026-02-08
- [b2262e51eeb5_drop_organizations_promo_code_used_dead_.py](<../services/backend-api/alembic/versions/b2262e51eeb5_drop_organizations_promo_code_used_dead_.py>) — drop organizations.promo_code_used (dead stripe promo surface) Revision ID: b2262e51eeb5 Revises: 8bbf7dfee1e9 Create Date: 2026-07-26 00:44:26.425588 Completes the OSS-pivot Stripe…
- [b2c3d4e5f6a7_add_crm_enrichment_table.py](<../services/backend-api/alembic/versions/b2c3d4e5f6a7_add_crm_enrichment_table.py>) — add_crm_enrichment_table Revision ID: b2c3d4e5f6a7 Revises: a6b7c8d9e0f1 Create Date: 2026-06-30 00:00:00.000000 hubspot-sync aspect: second chained migration. down_revision verified…
- [b2c3d4e5f6g7_add_integrations_and_slack_alerts.py](<../services/backend-api/alembic/versions/b2c3d4e5f6g7_add_integrations_and_slack_alerts.py>) — Add integrations and slack_alert_logs tables Revision ID: b2c3d4e5f6g7 Revises: a1b2c3d4e5f6 Create Date: 2026-01-31
- [b3c4d5e6f7a8_add_category_classifier_mode.py](<../services/backend-api/alembic/versions/b3c4d5e6f7a8_add_category_classifier_mode.py>) — add_category_classifier_mode Revision ID: b3c4d5e6f7a8 Revises: v2w3x4y5z6a7 Create Date: 2026-07-11 00:00:00.000000 M5.2 v2 per-org category classifier — data-and-config aspect. Adds…
- [b5c6d7e8f9g0_add_last_synced_at_to_integrations.py](<../services/backend-api/alembic/versions/b5c6d7e8f9g0_add_last_synced_at_to_integrations.py>) — add last_synced_at to integrations Revision ID: b5c6d7e8f9g0 Revises: a4b5c6d7e8f9 Create Date: 2026-02-16 02:45:00.000000
- [b8c9d0e1f2a3_add_churn_backfill_progress_columns.py](<../services/backend-api/alembic/versions/b8c9d0e1f2a3_add_churn_backfill_progress_columns.py>) — add backfill_status/progress/last_run_at/error to CRM integrations historical-backfill aspect of crm-churn-labels (PRD M7). See docs/planning/crm-churn-labels/historical-backfill/spec.md §6…
- [c2d3e4f5a6b7_add_feedback_workflow.py](<../services/backend-api/alembic/versions/c2d3e4f5a6b7_add_feedback_workflow.py>) — Add feedback workflow tables and columns. Revision ID: c2d3e4f5a6b7 Revises: b1c2d3e4f5a6 Create Date: 2026-02-08 Adds: - workflow_status, assigned_to columns to feedback_items -…
- [c3d4e5f6a7b8_add_crm_health_component.py](<../services/backend-api/alembic/versions/c3d4e5f6a7b8_add_crm_health_component.py>) — add_crm_health_component Revision ID: c3d4e5f6a7b8 Revises: b2c3d4e5f6a7 Create Date: 2026-06-30 00:00:00.000000 Adds the opt-in CRM health component: - org_ai_config.health_weight_crm…
- [c3d4e5f6g7h8_add_message_template_to_integrations.py](<../services/backend-api/alembic/versions/c3d4e5f6g7h8_add_message_template_to_integrations.py>) — Add message_template to integrations Revision ID: c3d4e5f6g7h8 Revises: b2c3d4e5f6g7 Create Date: 2026-01-31
- [c4d5e6f7a8b9_add_jira_status_sync_columns.py](<../services/backend-api/alembic/versions/c4d5e6f7a8b9_add_jira_status_sync_columns.py>) — add jira status sync columns Phase 1 of Jira inbound status sync: adds status_sync_enabled and status_mapping to jira_integrations, plus jira_status, jira_status_category, and…
- [c6d7e8f9g0h1_add_user_dashboard_layouts.py](<../services/backend-api/alembic/versions/c6d7e8f9g0h1_add_user_dashboard_layouts.py>) — add user_dashboard_layouts table Revision ID: c6d7e8f9g0h1 Revises: b5c6d7e8f9g0 Create Date: 2026-02-16 10:00:00.000000
- [c7d8e9f0a1b2_encrypt_integration_oauth_tokens.py](<../services/backend-api/alembic/versions/c7d8e9f0a1b2_encrypt_integration_oauth_tokens.py>) — encrypt_integration_oauth_tokens Encrypts existing plaintext ``integrations.oauth_access_token`` rows in place with Fernet. Online-only: uses ``op.get_bind()`` and does not support…
- [c9d0e1f2a3b4_add_oidc_config_table.py](<../services/backend-api/alembic/versions/c9d0e1f2a3b4_add_oidc_config_table.py>) — add oidc config table Creates oidc_configs (one row/org, Fernet-encrypted client_secret) for the oidc-config aspect of oidc-sso (PRD M2). Stores issuer_url/client_id/…
- [d3a2c5b7e9f4_encrypt_linear_webhook_secret.py](<../services/backend-api/alembic/versions/d3a2c5b7e9f4_encrypt_linear_webhook_secret.py>) — encrypt_linear_webhook_secret Encrypts existing plaintext ``linear_integrations.webhook_secret`` rows in place with Fernet. Online-only: uses ``op.get_bind()`` and does not support…
- [d3e4f5g6h7i8_add_channel_intercom_to_alert_prefs.py](<../services/backend-api/alembic/versions/d3e4f5g6h7i8_add_channel_intercom_to_alert_prefs.py>) — Add channel_intercom to user_alert_preferences. Revision ID: d3e4f5g6h7i8 Revises: c2d3e4f5a6b7 Create Date: 2026-02-12
- [d4e5f6a7b8c9_add_model_embeddings_to_org_ai_config.py](<../services/backend-api/alembic/versions/d4e5f6a7b8c9_add_model_embeddings_to_org_ai_config.py>) — add_model_embeddings_to_org_ai_config Revision ID: d4e5f6a7b8c9 Revises: c3d4e5f6a7b8 Create Date: 2026-07-01 00:00:00.000000 Adds the per-org embedding-model override…
- [d4e5f6g7h8i9_add_feedback_sources.py](<../services/backend-api/alembic/versions/d4e5f6g7h8i9_add_feedback_sources.py>) — Add feedback sources, events, and pending feedbacks tables Revision ID: d4e5f6g7h8i9 Revises: c3d4e5f6g7h8 Create Date: 2026-02-01
- [d5e6f7a8b9c0_add_asana_status_sync_columns.py](<../services/backend-api/alembic/versions/d5e6f7a8b9c0_add_asana_status_sync_columns.py>) — add asana status sync columns model-migrations aspect of asana-status-sync: adds status_sync_enabled and status_mapping to asana_integrations, plus asana_completed, asana_status_category,…
- [d7e8f9g0h1i2_add_promo_code_used_to_organizations.py](<../services/backend-api/alembic/versions/d7e8f9g0h1i2_add_promo_code_used_to_organizations.py>) — add promo_code_used to organizations Revision ID: d7e8f9g0h1i2 Revises: c6d7e8f9g0h1 Create Date: 2026-02-17 12:00:00.000000
- [df55269cbdec_add_google_oauth_columns.py](<../services/backend-api/alembic/versions/df55269cbdec_add_google_oauth_columns.py>) — add_google_oauth_columns Revision ID: df55269cbdec Revises: h8i9j0k1l2m3 Create Date: 2026-02-04 03:14:33.926857
- [e4f5a6b7c8d9_add_intercom_writeback_columns.py](<../services/backend-api/alembic/versions/e4f5a6b7c8d9_add_intercom_writeback_columns.py>) — add_intercom_writeback_columns Revision ID: e4f5a6b7c8d9 Revises: 3cb9a0d1456b Create Date: 2026-08-15 00:00:00.000000 intercom-writeback (db-config-model aspect, R1 + R4): -…
- [e5f6g7h8i9j0_add_billing_tables.py](<../services/backend-api/alembic/versions/e5f6g7h8i9j0_add_billing_tables.py>) — Add billing tables (subscriptions, usage_records) and seat tracking Revision ID: e5f6g7h8i9j0 Revises: d4e5f6g7h8i9 Create Date: 2026-02-01
- [e6f7a8b9c0d1_add_urgency_classifier_mode.py](<../services/backend-api/alembic/versions/e6f7a8b9c0d1_add_urgency_classifier_mode.py>) — add_urgency_classifier_mode Revision ID: e6f7a8b9c0d1 Revises: 3e26b38cbd15 Create Date: 2026-07-14 00:00:00.000000 urgency-classifier-head — data-and-config aspect. Adds…
- [e8f9g0h1i2j3_fix_user_deletion_fk_constraints.py](<../services/backend-api/alembic/versions/e8f9g0h1i2j3_fix_user_deletion_fk_constraints.py>) — fix user deletion FK constraints Make FK columns nullable where user data should be preserved after user deletion, and add ondelete behavior to all user FKs. Revision ID: e8f9g0h1i2j3…
- [f1a2b3c4d5e6_add_zendesk_status_sync.py](<../services/backend-api/alembic/versions/f1a2b3c4d5e6_add_zendesk_status_sync.py>) — add zendesk status sync reconcile-core-and-model aspect of Zendesk inbound status-sync: adds status_sync_enabled, status_mapping, last_status_synced_at, and last_status_sync_error to…
- [f5a6b7c8d9e0_add_intercom_backlog_remaining.py](<../services/backend-api/alembic/versions/f5a6b7c8d9e0_add_intercom_backlog_remaining.py>) — add_intercom_backlog_remaining Revision ID: f5a6b7c8d9e0 Revises: e4f5a6b7c8d9 Create Date: 2026-08-15 00:00:00.000000 intercom-backlog-drain-visibility (db-status-api aspect, R3): -…
- [f6a7b8c9d0e1_add_outreach_tables.py](<../services/backend-api/alembic/versions/f6a7b8c9d0e1_add_outreach_tables.py>) — add_outreach_tables Revision ID: f6a7b8c9d0e1 Revises: d3a2c5b7e9f4 Create Date: 2026-08-12 00:00:00.000000 Outreach-core aspect (customer-outreach-email-actions): -…
- [f6g7h8i9j0k1_add_team_management_fields_to_users.py](<../services/backend-api/alembic/versions/f6g7h8i9j0k1_add_team_management_fields_to_users.py>) — Add team management fields to users table (RBAC support) Revision ID: f6g7h8i9j0k1 Revises: e5f6g7h8i9j0 Create Date: 2026-02-02
- [f7a8b9c0d1e2_add_churn_label_suggestions.py](<../services/backend-api/alembic/versions/f7a8b9c0d1e2_add_churn_label_suggestions.py>) — add churn_label_suggestions + CRM churn-label opt-in columns data-model aspect of crm-churn-labels (PRD M3, M4). See docs/planning/crm-churn-labels/data-model/spec.md and…
- [f9g0h1i2j3k4_customer_360_history_and_fields.py](<../services/backend-api/alembic/versions/f9g0h1i2j3k4_customer_360_history_and_fields.py>) — customer_360: add is_archived, confidence_level to customer_health_scores; create customer_health_history Revision ID: f9g0h1i2j3k4 Revises: e8f9g0h1i2j3 Create Date: 2026-02-19…
- [fb57e62a2820_add_report_schedules_table.py](<../services/backend-api/alembic/versions/fb57e62a2820_add_report_schedules_table.py>) — add_report_schedules_table Revision ID: fb57e62a2820 Revises: a2b3c4d5e6f7 Create Date: 2026-08-25 02:24:50.630849 scheduled-ai-reports (backend-schedule-crud aspect): - report_schedules —…
- [g0h1i2j3k4l5_add_structured_llm_analysis.py](<../services/backend-api/alembic/versions/g0h1i2j3k4l5_add_structured_llm_analysis.py>) — add structured llm_analysis_data JSON, llm_raw_response JSON, customer_analysis_actions table Revision ID: g0h1i2j3k4l5 Revises: f9g0h1i2j3k4 Create Date: 2026-02-19 12:00:00.000000
- [g7h8i9j0k1l2_add_team_invites_table.py](<../services/backend-api/alembic/versions/g7h8i9j0k1l2_add_team_invites_table.py>) — Add team_invites table for invitation system Revision ID: g7h8i9j0k1l2 Revises: f6g7h8i9j0k1 Create Date: 2026-02-02
- [h1i2j3k4l5m6_add_multi_model_support.py](<../services/backend-api/alembic/versions/h1i2j3k4l5m6_add_multi_model_support.py>) — add_multi_model_support Revision ID: h1i2j3k4l5m6 Revises: 6e4501930bf0 Create Date: 2026-02-22 10:00:00.000000
- [h8i9j0k1l2m3_add_audit_logs_table.py](<../services/backend-api/alembic/versions/h8i9j0k1l2m3_add_audit_logs_table.py>) — Add audit_logs table for team management action tracking Revision ID: h8i9j0k1l2m3 Revises: g7h8i9j0k1l2 Create Date: 2026-02-02
- [hbsh5o3gbwv4_add_embedding_model_to_mappings.py](<../services/backend-api/alembic/versions/hbsh5o3gbwv4_add_embedding_model_to_mappings.py>) — add_embedding_model_to_mappings Revision ID: hbsh5o3gbwv4 Revises: 0a3382154c27 Create Date: 2026-07-24 00:00:00.000000 Adds embedding_model (String(100), nullable) to…
- [i2j3k4l5m6n7_add_copilot_tables.py](<../services/backend-api/alembic/versions/i2j3k4l5m6n7_add_copilot_tables.py>) — add_copilot_tables Revision ID: i2j3k4l5m6n7 Revises: h1i2j3k4l5m6 Create Date: 2026-02-23 10:00:00.000000
- [i9j0k1l2m3n4_add_weekly_digest_enabled.py](<../services/backend-api/alembic/versions/i9j0k1l2m3n4_add_weekly_digest_enabled.py>) — add_weekly_digest_enabled Revision ID: i9j0k1l2m3n4 Revises: df55269cbdec Create Date: 2026-02-07
- [j0k1l2m3n4o5_add_ai_enhancements_schema.py](<../services/backend-api/alembic/versions/j0k1l2m3n4o5_add_ai_enhancements_schema.py>) — add_ai_enhancements_schema Revision ID: j0k1l2m3n4o5 Revises: i9j0k1l2m3n4 Create Date: 2026-02-07 Adds: - ai_analysis_enabled and openai_api_key to organizations - custom_categories table…
- [j1k2l3m4n5o6_add_jira_integration_tables.py](<../services/backend-api/alembic/versions/j1k2l3m4n5o6_add_jira_integration_tables.py>) — add jira integration tables Creates jira_integrations (one row/org, Fernet-encrypted api_token) and feedback_jira_issues (feedback -> Jira issue links) for the Jira Cloud integration…
- [k1l2m3n4o5p6_add_anomalies_and_alert_prefs.py](<../services/backend-api/alembic/versions/k1l2m3n4o5p6_add_anomalies_and_alert_prefs.py>) — add_anomalies_and_alert_prefs Revision ID: k1l2m3n4o5p6 Revises: j0k1l2m3n4o5 Create Date: 2026-02-07 Adds: - sentiment_anomalies table - alert_channels to users (per-user override) -…
- [k2l3m4n5o6p7_add_salesforce_writeback_columns.py](<../services/backend-api/alembic/versions/k2l3m4n5o6p7_add_salesforce_writeback_columns.py>) — add_salesforce_writeback_columns Revision ID: k2l3m4n5o6p7 Revises: j1k2l3m4n5o6 Create Date: 2026-07-05 00:00:00.000000 model-migrations aspect (salesforce-crm-writeback PRD, slice 1):…
- [l2m3n4o5p6q7_add_weekly_insights.py](<../services/backend-api/alembic/versions/l2m3n4o5p6q7_add_weekly_insights.py>) — add_weekly_insights Revision ID: l2m3n4o5p6q7 Revises: k1l2m3n4o5p6 Create Date: 2026-02-07 Adds: - weekly_insights table for AI-generated insight summaries
- [m3n4o5p6q7r8_add_changelog_entries.py](<../services/backend-api/alembic/versions/m3n4o5p6q7r8_add_changelog_entries.py>) — add_changelog_entries Revision ID: m3n4o5p6q7r8 Revises: l2m3n4o5p6q7 Create Date: 2026-02-07 Adds: - changelog_entries table for public changelog - is_system_admin column on users table
- [n3o4p5q6r7s8_add_conversation_public_id.py](<../services/backend-api/alembic/versions/n3o4p5q6r7s8_add_conversation_public_id.py>) — add_conversation_public_id Revision ID: n3o4p5q6r7s8 Revises: i2j3k4l5m6n7 Create Date: 2026-02-25 02:30:00.000000
- [n7o8p9q0r1s2_add_crm_writeback_columns.py](<../services/backend-api/alembic/versions/n7o8p9q0r1s2_add_crm_writeback_columns.py>) — add_crm_writeback_columns Revision ID: a1b2c3d4e5f6 Revises: 9f56f9a4f999 Create Date: 2026-07-03 00:00:00.000000 writeback-config-api aspect (crm-writeback PRD, slice 1): persists per-org…
- [n8o9p0q1r2s3_add_user_oidc_sub.py](<../services/backend-api/alembic/versions/n8o9p0q1r2s3_add_user_oidc_sub.py>) — add user oidc sub Adds `users.oidc_sub` (String(255), unique, nullable, indexed) for the oidc-login-flow aspect of oidc-sso (PRD M7). Populated on JIT-provision/link during OIDC callback…
- [o4p5q6r7s8t9_add_response_suggestions.py](<../services/backend-api/alembic/versions/o4p5q6r7s8t9_add_response_suggestions.py>) — add_response_suggestions Revision ID: o4p5q6r7s8t9 Revises: n3o4p5q6r7s8 Create Date: 2026-03-09 00:00:00.000000
- [o9p0q1r2s3t4_add_saml_config_table.py](<../services/backend-api/alembic/versions/o9p0q1r2s3t4_add_saml_config_table.py>) — add saml config table Creates saml_configs (one row/org, plaintext idp_x509_cert — a PUBLIC signing certificate, not a secret, so it is NOT Fernet-encrypted, unlike…
- [p0q1r2s3t4u5_add_user_saml_subject.py](<../services/backend-api/alembic/versions/p0q1r2s3t4u5_add_user_saml_subject.py>) — add user saml subject Adds `users.saml_subject` (String(255), unique, nullable, indexed) for the config-model-and-crud aspect of saml-sso (PRD M1). Populated on JIT-provision/link during…
- [p5q6r7s8t9u0_add_webhook_tables.py](<../services/backend-api/alembic/versions/p5q6r7s8t9u0_add_webhook_tables.py>) — add_webhook_tables Revision ID: p5q6r7s8t9u0 Revises: o4p5q6r7s8t9 Create Date: 2026-03-15 00:00:00.000000
- [q1r2s3t4u5v6_add_saml_auth_requests.py](<../services/backend-api/alembic/versions/q1r2s3t4u5v6_add_saml_auth_requests.py>) — add saml auth requests Creates saml_auth_requests, the DB-backed InResponseTo / replay store for the provider-and-replay-store aspect of saml-sso (PRD M3 replay defense). One row per…
- [q6r7s8t9u0v1_add_reports_table.py](<../services/backend-api/alembic/versions/q6r7s8t9u0v1_add_reports_table.py>) — add_reports_table Revision ID: q6r7s8t9u0v1 Revises: p5q6r7s8t9u0 Create Date: 2026-03-17 00:00:00.000000
- [r1s2t3u4v5w6_add_jira_webhook_secret.py](<../services/backend-api/alembic/versions/r1s2t3u4v5w6_add_jira_webhook_secret.py>) — add jira webhook secret Adds `jira_integrations.webhook_secret` (Text, nullable, Fernet-encrypted at the route layer) for the jira-webhook aspect of status-sync-realtime-mapping (PRD).…
- [r7s8t9u0v1w2_add_gdpr_fields_to_users.py](<../services/backend-api/alembic/versions/r7s8t9u0v1w2_add_gdpr_fields_to_users.py>) — add_gdpr_fields_to_users Revision ID: r7s8t9u0v1w2 Revises: q6r7s8t9u0v1 Create Date: 2026-04-12 00:00:00.000000
- [s2t3u4v5w6x7_add_asana_webhook_columns.py](<../services/backend-api/alembic/versions/s2t3u4v5w6x7_add_asana_webhook_columns.py>) — add asana webhook columns Adds `asana_integrations.webhook_secret` (Text, nullable, Fernet-encrypted at the receiver/route layer) and `asana_integrations.webhook_gid` (String(255),…
- [s8t9u0v1w2x3_add_ai_corrections_table.py](<../services/backend-api/alembic/versions/s8t9u0v1w2x3_add_ai_corrections_table.py>) — add_ai_corrections_table Revision ID: s8t9u0v1w2x3 Revises: r7s8t9u0v1w2 Create Date: 2026-04-12 00:00:00.000000
- [t3u4v5w6x7y8_add_asana_webhook_url_token.py](<../services/backend-api/alembic/versions/t3u4v5w6x7y8_add_asana_webhook_url_token.py>) — add asana_integrations.webhook_url_token (unguessable webhook URL) Security fix (sec review, CRITICAL): the asana-webhook receiver previously resolved the integration by a guessable integer…
- [t9u0v1w2x3y4_add_automation_tables.py](<../services/backend-api/alembic/versions/t9u0v1w2x3y4_add_automation_tables.py>) — add_automation_tables Revision ID: t9u0v1w2x3y4 Revises: s8t9u0v1w2x3 Create Date: 2026-04-13 00:00:00.000000
- [u0v1w2x3y4z5_add_advanced_churn_prediction.py](<../services/backend-api/alembic/versions/u0v1w2x3y4z5_add_advanced_churn_prediction.py>) — add_advanced_churn_prediction Revision ID: u0v1w2x3y4z5 Revises: t9u0v1w2x3y4 Create Date: 2026-05-20 00:00:00.000000 M4.1 — Advanced Churn Prediction foundation. Creates five new tables…
- [u4v5w6x7y8z9_add_automation_rule_mode.py](<../services/backend-api/alembic/versions/u4v5w6x7y8z9_add_automation_rule_mode.py>) — add_automation_rule_mode Revision ID: u4v5w6x7y8z9 Revises: t3u4v5w6x7y8 Create Date: 2026-07-18 00:00:00.000000 Adds `automation_rules.mode` (off / shadow / active) — the execution-state…
- [v1w2x3y4z5a6_drop_dead_billing_budget_columns.py](<../services/backend-api/alembic/versions/v1w2x3y4z5a6_drop_dead_billing_budget_columns.py>) — drop_dead_billing_budget_columns Revision ID: v1w2x3y4z5a6 Revises: u0v1w2x3y4z5 Create Date: 2026-06-14 00:00:00.000000 B4 (OSS Self-Hosted Pivot) — Drop the four dead billing/budget…
- [v2w3x4y5z6a7_add_org_classifier_tables.py](<../services/backend-api/alembic/versions/v2w3x4y5z6a7_add_org_classifier_tables.py>) — add_org_classifier_tables Revision ID: v2w3x4y5z6a7 Revises: 6ad1dc4335f1 Create Date: 2026-07-10 14:30:00.000000 M5.2 per-org self-improving corrections classifier — data layer. Creates…
- [w2x3y4z5a6b7_drop_stripe_byok_columns_oss_pivot.py](<../services/backend-api/alembic/versions/w2x3y4z5a6b7_drop_stripe_byok_columns_oss_pivot.py>) — drop_stripe_byok_columns_oss_pivot Revision ID: w2x3y4z5a6b7 Revises: v1w2x3y4z5a6 Create Date: 2026-06-14 00:00:00.000000 B4 (OSS Self-Hosted Pivot) — Drop all remaining dead…
- [x3y4z5a6b7c8_add_local_llm_health_weights_api_keys.py](<../services/backend-api/alembic/versions/x3y4z5a6b7c8_add_local_llm_health_weights_api_keys.py>) — add local-llm base_url + health weights to org_ai_config; create api_keys Feature batch (Local LLM / Custom AI / Public API): - org_ai_config: base_url (local/custom OpenAI-compatible…
- [y4z5a6b7c8d9_add_embedding_provider_dim_to_mappings.py](<../services/backend-api/alembic/versions/y4z5a6b7c8d9_add_embedding_provider_dim_to_mappings.py>) — add_embedding_provider_dim_to_mappings Revision ID: y4z5a6b7c8d9 Revises: x3y4z5a6b7c8 Create Date: 2026-06-28 00:00:00.000000 Adds embedding_provider (String(50), nullable) and…
- [z1a2b3c4d5e6_add_zendesk_integration_tables.py](<../services/backend-api/alembic/versions/z1a2b3c4d5e6_add_zendesk_integration_tables.py>) — add zendesk integration tables Creates zendesk_integrations (one row/org, Fernet-encrypted api_token + nullable Fernet-encrypted webhook_secret) for the Zendesk integration…
- [z5a6b7c8d9e0_add_usage_health_component.py](<../services/backend-api/alembic/versions/z5a6b7c8d9e0_add_usage_health_component.py>) — add_usage_health_component Revision ID: z5a6b7c8d9e0 Revises: y4z5a6b7c8d9 Create Date: 2026-06-28 00:00:00.000000 Adds the opt-in usage health component: -…

## `services/backend-api/eval_results`

[Directory guide](<../services/backend-api/eval_results/directory.md>)

- [churn_label_gate.json](<../services/backend-api/eval_results/churn_label_gate.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [retrieval_accuracy.json](<../services/backend-api/eval_results/retrieval_accuracy.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [sentiment_accuracy.json](<../services/backend-api/eval_results/sentiment_accuracy.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## `services/backend-api/scripts`

[Directory guide](<../services/backend-api/scripts/directory.md>)

- [backfill_churn_factors.py](<../services/backend-api/scripts/backfill_churn_factors.py>) — Backfill churn_risk_factors for existing feedback items that have a churn_risk_score but no factor breakdown. Also recomputes confidence_score on all CustomerHealth records. Usage: python…
- [backfill_customer_email.py](<../services/backend-api/scripts/backfill_customer_email.py>) — Backfill customer_email on existing feedback items from source_metadata. Run: cd services/backend-api && source venv/bin/activate && python scripts/backfill_customer_email.py
- [backfill_health_history.py](<../services/backend-api/scripts/backfill_health_history.py>) — Backfill initial health score history for existing customers who have no history records. This seeds the first data point so the Health Score History chart has something to show. Run: cd…
- [backfill_health_scores.py](<../services/backend-api/scripts/backfill_health_scores.py>) — Backfill customer health scores for all customers with customer_email set. Run AFTER backfill_customer_email.py. Run: cd services/backend-api && source venv/bin/activate && python…
- [backtest_churn.py](<../services/backend-api/scripts/backtest_churn.py>) — Backtest churn prediction accuracy against historical data. Usage: python scripts/backtest_churn.py --days 30 --output results.csv --db-url postgresql://... The script evaluates churn…
- [eval_churn_label_gate.py](<../services/backend-api/scripts/eval_churn_label_gate.py>) — Offline churn label-gate study harness (M5.3, aspect 2 — churn-label-gate-study). Re-derives the per-org churn-label activation gate (CHURN_LABEL_TARGET, currently 500 in…
- [eval_embeddings.py](<../services/backend-api/scripts/eval_embeddings.py>) — Offline retrieval eval harness — runs one or more embedding providers over the held-out template-matching fixtures and computes recall@1, MRR, and false-match rate at the production…
- [eval_sentiment.py](<../services/backend-api/scripts/eval_sentiment.py>) — Offline sentiment eval harness — runs VaderSentimentProvider and TransformerSentimentProvider (analysis-engine) over labeled CSVs, computes per-class + macro precision/recall/F1/confusion,…
- [manage_resend_templates.py](<../services/backend-api/scripts/manage_resend_templates.py>) — Resend Email Template Management Script Usage: python scripts/manage_resend_templates.py list python scripts/manage_resend_templates.py get <template_id> python…
- [run_batch_churn_analysis.py](<../services/backend-api/scripts/run_batch_churn_analysis.py>) — Batch LLM churn analysis for at-risk customers (health_score < 40). Reads all CustomerHealth records with health_score < 40, fetches their recent feedback, calls OpenAI with the same…
- [simulate_health_history.py](<../services/backend-api/scripts/simulate_health_history.py>) — Simulate realistic weekly health score history for all customers. Replaces the single-point backfill with a week-by-week simulation going back to each customer's earliest feedback date,…
- [sync_changelog.py](<../services/backend-api/scripts/sync_changelog.py>) — Sync git commits to changelog_entries table. Parses conventional commit messages and creates changelog entries. Skips commits that already exist (by commit_hash). Modes: --github Fetch from…

## `services/backend-api/src`

[Directory guide](<../services/backend-api/src/directory.md>)

- [__init__.py](<../services/backend-api/src/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [notification_dispatch_helpers.py](<../services/backend-api/src/notification_dispatch_helpers.py>) — Helpers for dispatching targeted workflow notifications directly from the backend-api. Creates Notification records in the database for specific users, respecting their alert preferences.
- [seed.py](<../services/backend-api/src/seed.py>) — Seed script to create initial owner user. Runs on application startup if owner user doesn't exist.
- [seed_byok.py](<../services/backend-api/src/seed_byok.py>) — Env-seed BYOK keys for single-tenant self-hosted convenience (OSS Pivot Q1). On application startup, for each of the three provider env vars that is present, ensure an OrgApiKey row exists…

## `services/backend-api/src/api`

[Directory guide](<../services/backend-api/src/api/directory.md>)

- [__init__.py](<../services/backend-api/src/api/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [auth.py](<../services/backend-api/src/api/auth.py>) — Declarations: hash_password, verify_password, create_access_token, decode_access_token
- [dependencies.py](<../services/backend-api/src/api/dependencies.py>) — Declarations: get_current_user, get_current_user_allow_deactivated, get_current_org, get_current_usage, check_feedback_limit, track_feedback_usage
- [main.py](<../services/backend-api/src/api/main.py>) — Declarations: seed_copilot_system_templates, warn_unconfigured_webhook_secrets, run_migrations, lifespan, CacheControlMiddleware, root · Routes: GET /; GET /health; GET /worker/status; GET /tasks/{task_id}

## `services/backend-api/src/api/public`

[Directory guide](<../services/backend-api/src/api/public/directory.md>)

- [__init__.py](<../services/backend-api/src/api/public/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [auth.py](<../services/backend-api/src/api/public/auth.py>) — Public API authentication — API-key based auth dependency. Keys are formatted ``rrf_<urlsafe-random>`` and stored as sha256(key) in ``api_keys.key_hash``. The full key is shown exactly once…

## `services/backend-api/src/api/routes`

[Directory guide](<../services/backend-api/src/api/routes/directory.md>)

- [_oidc_state.py](<../services/backend-api/src/api/routes/_oidc_state.py>) — Stateless `state` signing + PKCE helpers for the OIDC login flow (`GET /auth/oidc/start` and `GET /auth/oidc/callback`). Mirrors `salesforce_integration.py`'s…
- [_sso_guard.py](<../services/backend-api/src/api/routes/_sso_guard.py>) — Cross-provider single-SSO guard (saml-sso M6). At most ONE SSO protocol may be enabled per deployment. Enabling SAML must fail if any OIDC config is enabled, and vice-versa. This is the…
- [account.py](<../services/backend-api/src/api/routes/account.py>) — GDPR-compliant account management endpoints. Endpoints --------- GET /api/v1/account/export — Download a ZIP of all personal data POST /api/v1/account/delete-request — Request account… · Routes: GET /export; POST /delete-request; POST /cancel-deletion
- [activity_feed.py](<../services/backend-api/src/api/routes/activity_feed.py>) — Activity feed endpoint — aggregates recent events across the organization. · Routes: GET /
- [admin_ai_models.py](<../services/backend-api/src/api/routes/admin_ai_models.py>) — System Admin: AI Model Price Management API endpoints. All endpoints require system admin access. · Routes: GET ; PATCH /{model_id}; POST /sync-prices
- [admin_backtest.py](<../services/backend-api/src/api/routes/admin_backtest.py>) — Admin Backtest API endpoint. Evaluates churn prediction accuracy against historical data. Requires system admin access. · Routes: POST /backtest
- [admin_orgs.py](<../services/backend-api/src/api/routes/admin_orgs.py>) — Admin Organization management API endpoints. All endpoints require system admin access. · Routes: GET ; GET /{org_id}; DELETE /{org_id}
- [admin_users.py](<../services/backend-api/src/api/routes/admin_users.py>) — Admin User management API endpoints. All endpoints require system admin access. · Routes: GET ; GET /{user_id}; PATCH /{user_id}; DELETE /{user_id}
- [ai_corrections.py](<../services/backend-api/src/api/routes/ai_corrections.py>) — AI Human-in-the-Loop corrections API (Track B, M3.8). Endpoints: POST /api/v1/ai-corrections Submit a correction/rating (any authenticated user) GET /api/v1/ai-corrections/stats Correction… · Routes: POST ; GET /stats; GET
- [ai_readiness.py](<../services/backend-api/src/api/routes/ai_readiness.py>) — AI training-readiness report API (M5.0 — Data & Model Readiness Assessment). GET /api/v1/analytics/ai-readiness — per-org, read-only aggregation over FeedbackItem / AICorrection /… · Routes: GET /ai-readiness
- [ai_settings.py](<../services/backend-api/src/api/routes/ai_settings.py>) — AI settings API endpoints. Manage AI analysis configuration, BYOK keys, usage, and budget for the organization. · Routes: GET ; PATCH ; GET /keys; POST /keys; DELETE /keys/{provider}
- [analytics.py](<../services/backend-api/src/api/routes/analytics.py>) — Analytics trends API endpoint. Provides time-series data, sentiment/source distributions, and top items. · Routes: GET /trends
- [analyze.py](<../services/backend-api/src/api/routes/analyze.py>) — Declarations: AnalyzeFeedbackRequest, AnalyzeFeedbackResponse, analyze_feedback, analyze_all_unanalyzed · Routes: POST /; POST /batch
- [anomalies.py](<../services/backend-api/src/api/routes/anomalies.py>) — Anomaly detection API endpoints. Provides listing and resolution of sentiment anomalies. · Routes: GET /; PATCH /{anomaly_id}/resolve
- [api_keys.py](<../services/backend-api/src/api/routes/api_keys.py>) — Public-API key management (JWT-authenticated, admin/owner only). Endpoints --------- POST /api/v1/api-keys Create a new key (returns full key ONCE) GET /api/v1/api-keys List org keys… · Routes: POST ; GET ; POST /{key_id}/revoke; DELETE /{key_id}
- [asana_integration.py](<../services/backend-api/src/api/routes/asana_integration.py>) — Asana integration routes (backend-connection aspect, Phase 3; backend-routes / inbound status-sync aspect). Routes: POST /api/v1/integrations/asana/connect — validate + encrypt + store GET… · Routes: POST /connect; GET /status; DELETE /disconnect; POST /test; POST /webhook/enable
- [asana_webhook.py](<../services/backend-api/src/api/routes/asana_webhook.py>) — Asana inbound real-time webhook receiver (status-sync-realtime-mapping/asana-webhook aspect). Generalizes Jira's receiver (routes/jira_webhook.py) but Asana's protocol differs in one… · Routes: POST /inbound/{token}
- [audit_logs.py](<../services/backend-api/src/api/routes/audit_logs.py>) — Audit Log API routes for viewing organization audit logs. · Routes: GET
- [auth.py](<../services/backend-api/src/api/routes/auth.py>) — Declarations: signup, login, get_current_user_info, get_preferences, update_preferences, google_signup · Routes: POST /signup; POST /login; GET /me; GET /me/preferences; PATCH /me/preferences
- [automations.py](<../services/backend-api/src/api/routes/automations.py>) — AI Workflow Automation API (M4.4 — Phase 1). Endpoints: GET /api/v1/automations List org rules POST /api/v1/automations Create rule (Admin+) GET /api/v1/automations/templates List pre-built… · Routes: GET /action-support; GET /templates; POST /templates/{template_id}/enable; GET ; POST
- [billing.py](<../services/backend-api/src/api/routes/billing.py>) — Billing API routes for subscription management and usage tracking. SELF-HOSTED OSS NOTE (B3): Stripe-only routes have been removed: - POST /checkout - POST /portal - GET /invoices - POST… · Routes: GET /plans; GET /usage
- [categories.py](<../services/backend-api/src/api/routes/categories.py>) — Custom categories API endpoints. Allows organizations to define custom categories for AI-powered categorization. · Routes: GET /custom; POST /custom; PATCH /custom/{category_id}; DELETE /custom/{category_id}; GET /health-weights
- [changelog.py](<../services/backend-api/src/api/routes/changelog.py>) — Changelog API endpoints. Public endpoint for listing changelog entries + admin endpoints for management. · Routes: GET ; GET /admin; PATCH /admin/{entry_id}; DELETE /admin/{entry_id}
- [churn_accuracy.py](<../services/backend-api/src/api/routes/churn_accuracy.py>) — Churn accuracy API endpoints (M4.1 Phase 6.2a). GET /api/v1/analytics/churn-accuracy — org-level accuracy card (Business+) GET /api/v1/system/churn-accuracy — cross-org admin overview… · Routes: GET /churn-accuracy; GET /churn-accuracy; GET /churn-accuracy/{org_id}/history
- [churn_analytics.py](<../services/backend-api/src/api/routes/churn_analytics.py>) — Churn cohort analytics API endpoint (M4.1 Phase 4). GET /api/v1/analytics/churn-cohorts?dimension=source/month/volume&range=30d/90d/all Plan gate: Business+ (churn_cohorts feature).… · Routes: GET /churn-cohorts
- [churn_events.py](<../services/backend-api/src/api/routes/churn_events.py>) — Churn Events API routes (M4.1 Phase 2.1). All endpoints live under /api/v1/customers and are plan-gated to Business+ via require_feature("advanced_churn_prediction"), except CSV import… · Routes: POST /churn-events/bulk; POST /churn-events/import; GET /churn-events; POST /{email}/churn-event; POST /{email}/recover
- [churn_label_gate.py](<../services/backend-api/src/api/routes/churn_label_gate.py>) — GET /api/v1/settings/ai/churn/label-gate (churn-label-gate-study aspect 2, M5.3 disclosure layer). Reads the committed eval_churn_label_gate.py results artifact… · Routes: GET /churn/label-gate
- [churn_suggestions.py](<../services/backend-api/src/api/routes/churn_suggestions.py>) — CRM churn-suggestion review queue (review-queue aspect, M5). This is the feature's whole trust boundary: a `ChurnLabelSuggestion` row is a CRM's guess. Confirm is the ONLY code path that… · Routes: GET /churn-suggestions; POST /churn-suggestions/bulk; POST /churn-suggestions/{suggestion_id}/confirm; POST /churn-suggestions/{suggestion_id}/reject
- [classifier_accuracy.py](<../services/backend-api/src/api/routes/classifier_accuracy.py>) — GET /api/v1/settings/ai/classifier/accuracy (settings-api-and-accuracy-card aspect, M5.2 disclosure layer). Read-only surface over OrgClassifierModel + OrgClassifierEvalRun, org-scoped. No… · Routes: GET /classifier/accuracy; GET /classifier/versions; POST /classifier/rollback; POST /classifier/resume
- [conversation_folders.py](<../services/backend-api/src/api/routes/conversation_folders.py>) — Conversation Folders REST API (M2.2 AI Copilot). Covers: - GET /api/v1/conversations/folders — List folders - POST /api/v1/conversations/folders — Create folder (Pro+) - PATCH… · Routes: GET ; POST ; PATCH /{folder_id}; DELETE /{folder_id}
- [conversations.py](<../services/backend-api/src/api/routes/conversations.py>) — Conversations REST API (M2.2 AI Copilot). Covers: - GET /api/v1/conversations — List conversations - POST /api/v1/conversations — Create conversation - GET /api/v1/conversations/:id — Get… · Routes: GET /templates; GET ; POST ; GET /{conversation_id}; PATCH /{conversation_id}
- [copilot.py](<../services/backend-api/src/api/routes/copilot.py>) — Copilot REST API supplementary endpoints (M2.2). - GET /api/v1/copilot/usage — User's copilot usage stats - POST /api/v1/conversations/suggestions — Dynamic query suggestions · Routes: GET /usage
- [copilot_actions.py](<../services/backend-api/src/api/routes/copilot_actions.py>) — Copilot suggested-actions execute route (copilot-suggested-actions, action-registry aspect; PRD M4/M5/M6/M7/M9). `POST /api/v1/copilot/actions/execute` takes the message a proposal came… · Routes: POST /actions/execute
- [copilot_ws.py](<../services/backend-api/src/api/routes/copilot_ws.py>) — Copilot WebSocket endpoint (M2.2 AI Copilot). Protocol: wss://{host}/ws/copilot?token={jwt} Client -> Server messages: - query: Submit a question - stop: Cancel ongoing generation -…
- [customer_health.py](<../services/backend-api/src/api/routes/customer_health.py>) — Declarations: CustomerHealthResponse, get_customer_health · Routes: GET /{email}
- [customers.py](<../services/backend-api/src/api/routes/customers.py>) — Customer 360 API routes. Provides list, profile, history, feedbacks, and activity endpoints. · Routes: GET /; GET /export; POST /bulk/tags; POST /bulk/assign-owner; POST /bulk/outreach
- [dashboard.py](<../services/backend-api/src/api/routes/dashboard.py>) — Declarations: SentimentStats, PainPoint, FeatureRequest, CategoryCount, TopCategory, UrgentFeedback · Routes: GET /; GET /comparison; GET /trends; GET /team-activity; GET /activity-feed
- [dashboard_layout.py](<../services/backend-api/src/api/routes/dashboard_layout.py>) — Dashboard layout CRUD — per-user widget layout persistence. · Routes: GET /; PUT /; DELETE /
- [email_webhooks.py](<../services/backend-api/src/api/routes/email_webhooks.py>) — Inbound email webhook endpoint for Resend. Receives forwarded emails, looks up the org by inbound address, applies rate limiting and deduplication, fetches the full email content from… · Routes: POST /inbound
- [embedding_accuracy.py](<../services/backend-api/src/api/routes/embedding_accuracy.py>) — GET /api/v1/settings/ai/embeddings/accuracy (retrieval-eval-card aspect, M5.4 disclosure layer). Reads the committed eval_embeddings.py results artifact… · Routes: GET /embeddings/accuracy
- [events_ws.py](<../services/backend-api/src/api/routes/events_ws.py>) — Real-time events WebSocket endpoint. Protocol: wss://{host}/ws/events?token={jwt} This is a passive endpoint — clients connect to receive push events. The server sends heartbeat pings every…
- [feedback.py](<../services/backend-api/src/api/routes/feedback.py>) — Declarations: get_sentiment_analyzer, get_categorizers, analyze_single_feedback, FeedbackCreateRequest, UrgentUpdateRequest, FeedbackResponse · Routes: POST /; GET /; GET /{feedback_id}; DELETE /{feedback_id}; POST /bulk-delete
- [feedback_issue_draft.py](<../services/backend-api/src/api/routes/feedback_issue_draft.py>) — AI-drafted issue content endpoint. POST /api/v1/feedback/{feedback_id}/issue-draft — draft a {title, body} work-tracker (Jira/Asana) issue from a feedback item using the org's configured… · Routes: POST /{feedback_id}/issue-draft
- [feedback_responses.py](<../services/backend-api/src/api/routes/feedback_responses.py>) — Feedback Responses endpoints. Endpoints (all nested under /api/v1/feedback/{feedback_id}): GET /responses — List response history for a feedback item POST /responses/generate — AI-generate… · Routes: GET /{feedback_id}/responses; POST /{feedback_id}/responses/generate; POST /{feedback_id}/responses/send
- [feedback_sources.py](<../services/backend-api/src/api/routes/feedback_sources.py>) — Feedback Sources API - CRUD endpoints for managing inbound feedback sources. Supports Slack, Discord, Webhooks, and other integrations. · Routes: GET /types; GET /; POST /; GET /{source_id}; PATCH /{source_id}
- [health.py](<../services/backend-api/src/api/routes/health.py>) — Enhanced health check endpoint — system admin only. GET /health/detailed Returns: database, redis, worker, memory and uptime diagnostics. · Routes: GET /health/detailed
- [hubspot_integration.py](<../services/backend-api/src/api/routes/hubspot_integration.py>) — HubSpot CRM integration routes. Routes: POST /api/v1/integrations/hubspot/connect — store encrypted token GET /api/v1/integrations/hubspot/status — connection status (no token) DELETE… · Routes: POST /connect; GET /status; DELETE /disconnect; POST /test; PATCH /writeback
- [insights.py](<../services/backend-api/src/api/routes/insights.py>) — Weekly insights API endpoints. Provides access to AI-generated weekly insight summaries. · Routes: GET /weekly; GET /weekly/history
- [integrations.py](<../services/backend-api/src/api/routes/integrations.py>) — Integrations API routes for managing Slack, Intercom, and other third-party integrations. · Routes: GET /; POST /slack/webhook; POST /discord/webhook; POST /teams/webhook; POST /discord/test
- [intercom_integration.py](<../services/backend-api/src/api/routes/intercom_integration.py>) — Intercom token-paste connection routes. Connect, status and disconnect for an Intercom **private app** Access Token. Why this exists alongside the OAuth routes in `integrations.py`:… · Routes: POST /connect; GET /status; DELETE /disconnect; PATCH /writeback; POST /writeback/test
- [invites.py](<../services/backend-api/src/api/routes/invites.py>) — Public Invite API routes for accepting team invitations. These endpoints are PUBLIC - they do not require authentication. They are used by invited users to view and accept invitations. · Routes: GET /{token}; POST /{token}/accept
- [jira_integration.py](<../services/backend-api/src/api/routes/jira_integration.py>) — Jira Cloud integration routes (backend-connection aspect, Phase 3). Routes: POST /api/v1/integrations/jira/connect — validate + encrypt + store GET /api/v1/integrations/jira/status —… · Routes: POST /connect; GET /status; DELETE /disconnect; POST /test; PATCH /status-sync
- [jira_webhook.py](<../services/backend-api/src/api/routes/jira_webhook.py>) — Jira Cloud inbound real-time webhook receiver (status-sync-realtime-mapping/jira-webhook aspect). Generalizes Zendesk's receiver (source_webhooks.py::handle_zendesk_webhook, fail-closed)… · Routes: POST /inbound
- [linear_integration.py](<../services/backend-api/src/api/routes/linear_integration.py>) — Linear integration API routes. Covers: OAuth flow, issue creation, configuration endpoints (team/status mappings), and proxy endpoints to the Linear API (teams, projects, labels). · Routes: GET /connect; GET /callback; DELETE /disconnect; GET /status; GET /config
- [linear_webhook.py](<../services/backend-api/src/api/routes/linear_webhook.py>) — Linear webhook receiver. Handles inbound events from Linear (issue status changes) and syncs them to Rereflect. · Routes: POST /inbound
- [notifications.py](<../services/backend-api/src/api/routes/notifications.py>) — Notification & Alert Preference API routes. All endpoints require authentication and are scoped to the current user. · Routes: GET ; GET /unread-count; PATCH /{notification_id}/read; POST /read-all; PATCH /{notification_id}/dismiss
- [oidc_config.py](<../services/backend-api/src/api/routes/oidc_config.py>) — OIDC SSO configuration routes (oidc-config aspect, Task 2). Routes: GET /api/v1/settings/oidc — read the org's config (or configured:false) PUT /api/v1/settings/oidc — upsert (encrypt… · Routes: GET ; PUT ; DELETE
- [organizations.py](<../services/backend-api/src/api/routes/organizations.py>) — Declarations: OrganizationUpdateRequest, OrganizationResponse, OrganizationStatsResponse, get_my_organization, update_my_organization, get_organization_stats · Routes: GET /me; PATCH /me; GET /me/stats
- [outreach.py](<../services/backend-api/src/api/routes/outreach.py>) — Outreach routes (outreach-core + bulk-campaign-api aspects). Read-only template registry for all roles, the public tokenized unsubscribe endpoint, the org-scoped campaign list (admin/owner)… · Routes: GET /campaigns; POST /campaigns/{campaign_id}/retry; GET /templates; GET /unsubscribe
- [pending_feedback.py](<../services/backend-api/src/api/routes/pending_feedback.py>) — Pending Feedback API - Endpoints for reviewing and approving/rejecting pending feedback items. · Routes: GET /; GET /{pending_id}; POST /{pending_id}/approve; POST /{pending_id}/reject; POST /bulk-approve
- [playbooks.py](<../services/backend-api/src/api/routes/playbooks.py>) — Churn Playbook API (M4.1 Phase 5.1). All endpoints gated by require_feature("churn_playbooks") (Business+). Endpoints: GET /api/v1/playbooks List org playbooks + system templates POST… · Routes: GET ; POST ; GET /executions; GET /{playbook_id}; PUT /{playbook_id}
- [public_api.py](<../services/backend-api/src/api/routes/public_api.py>) — Public REST API — /api/public/v1 (Feature C, PRD §6). All endpoints are authenticated via API-key (``rrf_...``) resolved by ``verify_api_key``. Every query is hard-scoped to the… · Routes: GET /feedback; GET /feedback/{feedback_id}; POST /feedback; POST /feedback/bulk; PATCH /feedback/{feedback_id}
- [report_schedules.py](<../services/backend-api/src/api/routes/report_schedules.py>) — Scheduled AI Reports — ReportSchedule CRUD + toggle API (backend-schedule-crud). Endpoints: GET /api/v1/report-schedules List org's schedules (newest first) GET… · Routes: GET ; GET /{schedule_id}; POST ; PATCH /{schedule_id}; DELETE /{schedule_id}
- [reports.py](<../services/backend-api/src/api/routes/reports.py>) — On-Demand AI Reports — CRUD API (M2.4). Endpoints: GET /api/v1/reports List org's saved reports (Business+) GET /api/v1/reports/{id} Get report with full sections (Business+) DELETE… · Routes: GET ; GET /{report_id}; DELETE /{report_id}
- [response_settings.py](<../services/backend-api/src/api/routes/response_settings.py>) — Response Settings endpoints — brand voice, tone, product name, support email. Endpoints: GET /api/v1/response-settings — Get org response settings PUT /api/v1/response-settings — Update… · Routes: GET ; PUT ; GET /usage
- [response_templates.py](<../services/backend-api/src/api/routes/response_templates.py>) — Response Templates CRUD + suggestion endpoint. Endpoints: GET /api/v1/response-templates — List all (system + org custom) POST /api/v1/response-templates — Create custom template… · Routes: GET ; POST ; GET /{template_id}; PUT /{template_id}; DELETE /{template_id}
- [salesforce_integration.py](<../services/backend-api/src/api/routes/salesforce_integration.py>) — Salesforce CRM integration routes — web-server OAuth 2.0. Mirrors the in-repo Linear OAuth pattern (getConnectUrl -> auth_url -> callback), NOT HubSpot's pasted-token form. Credentials are… · Routes: GET /connect-url; GET /status; GET /callback; POST /test; DELETE /disconnect
- [saml_config.py](<../services/backend-api/src/api/routes/saml_config.py>) — SAML SSO configuration routes (saml-sso: config-model-and-crud aspect). Routes: GET /api/v1/settings/saml — read the org's config (or configured:false) PUT /api/v1/settings/saml — upsert… · Routes: GET ; PUT ; DELETE
- [saved_views.py](<../services/backend-api/src/api/routes/saved_views.py>) — Saved views CRUD endpoints. Allows users to save and restore analytics page state configurations. · Routes: GET /; POST /; PATCH /{view_id}; DELETE /{view_id}; PATCH /reorder
- [sentiment_accuracy.py](<../services/backend-api/src/api/routes/sentiment_accuracy.py>) — GET /api/v1/settings/ai/sentiment/accuracy (eval-harness-and-card aspect, M5.1 disclosure layer). Reads the committed eval_sentiment.py results artifact… · Routes: GET /sentiment/accuracy
- [shared_links.py](<../services/backend-api/src/api/routes/shared_links.py>) — Shared links endpoints for public dashboard sharing. Both authenticated (create/list/deactivate) and public (view) endpoints. · Routes: POST /; GET /; GET /all; DELETE /{link_id}; GET /analytics/{token}
- [source_webhooks.py](<../services/backend-api/src/api/routes/source_webhooks.py>) — Webhook endpoints for receiving events from external sources (Slack, Intercom, generic webhooks). These endpoints handle signature verification and queue events for async processing. · Routes: POST /slack/events; POST /inbound/{webhook_id}; POST /intercom/events; POST /zendesk/events
- [team.py](<../services/backend-api/src/api/routes/team.py>) — Team Management API routes for managing organization members. · Routes: GET /members; GET ; PATCH /members/{user_id}/role; PATCH /{user_id}/role; DELETE /members/{user_id}
- [usage_webhooks.py](<../services/backend-api/src/api/routes/usage_webhooks.py>) — Inbound product-usage event receiver. POST /api/v1/webhooks/usage Accepts a Segment-compatible normalized batch of usage events from self-hosted operators. Authentication uses the existing… · Routes: POST
- [webhooks.py](<../services/backend-api/src/api/routes/webhooks.py>) — Custom Webhook Endpoints — CRUD API (M3.1). Endpoints: GET /api/v1/webhooks List org's webhook endpoints POST /api/v1/webhooks Create webhook endpoint (admin+) GET /api/v1/webhooks/{id} Get… · Routes: GET ; POST ; GET /{webhook_id}; PUT /{webhook_id}; DELETE /{webhook_id}
- [workflow.py](<../services/backend-api/src/api/routes/workflow.py>) — Workflow API routes — status tracking, assignment, notes, timeline, assignment rules. · Routes: POST /status; POST /assign; GET /overview; GET /status-counts; GET /{feedback_id}/timeline
- [zendesk_integration.py](<../services/backend-api/src/api/routes/zendesk_integration.py>) — Zendesk integration routes (backend-connection aspect, Phase 3). Routes: POST /api/v1/integrations/zendesk/connect — validate + encrypt + store GET /api/v1/integrations/zendesk/status —… · Routes: POST /connect; GET /status; DELETE /disconnect; POST /sync; PATCH /status-sync

## `services/backend-api/src/api/schemas`

[Directory guide](<../services/backend-api/src/api/schemas/directory.md>)

- [__init__.py](<../services/backend-api/src/api/schemas/__init__.py>) — Declarations: SignupRequest, LoginRequest, GoogleLoginRequest, GoogleSignupRequest, TokenResponse, UserResponse
- [usage.py](<../services/backend-api/src/api/schemas/usage.py>) — Pydantic schemas for the product-usage ingest endpoint. POST /api/v1/webhooks/usage accepts a Segment-compatible batch body.

## `services/backend-api/src/background`

[Directory guide](<../services/backend-api/src/background/directory.md>)

- [__init__.py](<../services/backend-api/src/background/__init__.py>) — Background jobs via Celery + Redis.
- [celery_client.py](<../services/backend-api/src/background/celery_client.py>) — Celery client for queueing tasks to worker-service. This module provides a way to queue analysis tasks from the backend-api to the separate worker-service for distributed processing. Redis…
- [gdpr_purge.py](<../services/backend-api/src/background/gdpr_purge.py>) — GDPR Purge Task — deletes user data after the 30-day grace period. This module exposes `check_deletion_requests(db)` which is called: - By the Celery Beat scheduler (daily) - Directly in…

## `services/backend-api/src/config`

[Directory guide](<../services/backend-api/src/config/directory.md>)

- [__init__.py](<../services/backend-api/src/config/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [automation_templates.py](<../services/backend-api/src/config/automation_templates.py>) — Pre-built automation rule templates (M4.4 — Phase 1; template 6 added by usage-trend-automation-trigger's template-and-docs aspect, M10; template 7 added by batch-sentiment-trigger, Track…
- [plans.py](<../services/backend-api/src/config/plans.py>) — Pricing plan configuration for Rereflect. Tiers: - Free: $0, 250 feedback/mo, 2 seats - Pro: $29/mo, 2,500 feedback/mo, 10 seats - Business: $99/mo, 25,000 feedback/mo, 25 seats -…
- [readiness_thresholds.py](<../services/backend-api/src/config/readiness_thresholds.py>) — Static/configuration artifact; inspect its consumer.
- [system_templates.py](<../services/backend-api/src/config/system_templates.py>) — Default system response templates for Rereflect. These 8 templates are seeded at startup/migration and are read-only. They cannot be edited or deleted by any organization.

## `services/backend-api/src/database`

[Directory guide](<../services/backend-api/src/database/directory.md>)

- [__init__.py](<../services/backend-api/src/database/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [session.py](<../services/backend-api/src/database/session.py>) — Declarations: get_db

## `services/backend-api/src/models`

[Directory guide](<../services/backend-api/src/models/directory.md>)

- [__init__.py](<../services/backend-api/src/models/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [ai_correction.py](<../services/backend-api/src/models/ai_correction.py>) — Declarations: AICorrection
- [anomaly.py](<../services/backend-api/src/models/anomaly.py>) — Declarations: SentimentAnomaly
- [api_key.py](<../services/backend-api/src/models/api_key.py>) — Declarations: ApiKey
- [asana_integration.py](<../services/backend-api/src/models/asana_integration.py>) — Asana integration model. One row per organization. api_token is Fernet-encrypted via encrypt_api_key (never stored plaintext). Encryption happens in the route layer, not here. See…
- [assignment_rule.py](<../services/backend-api/src/models/assignment_rule.py>) — Declarations: AssignmentRule
- [audit_log.py](<../services/backend-api/src/models/audit_log.py>) — AuditLog model for tracking team management actions.
- [automation_email_delivery.py](<../services/backend-api/src/models/automation_email_delivery.py>) — AutomationEmailDelivery — SQLAlchemy model (automation-send-customer-email, action-core aspect). Audit row for one automation `send_customer_email` action. Status lifecycle: `queued` ->…
- [automation_execution.py](<../services/backend-api/src/models/automation_execution.py>) — AutomationExecution — SQLAlchemy model (M4.4). Audit log of every automation rule execution. Retained for 90 days (Celery Beat weekly purge in Phase 2).
- [automation_rule.py](<../services/backend-api/src/models/automation_rule.py>) — AutomationRule — SQLAlchemy model (M4.4). Stores IF/THEN automation rules scoped to an organization.
- [base.py](<../services/backend-api/src/models/base.py>) — Static/configuration artifact; inspect its consumer.
- [changelog_entry.py](<../services/backend-api/src/models/changelog_entry.py>) — Declarations: ChangelogEntry
- [churn_calibration.py](<../services/backend-api/src/models/churn_calibration.py>) — ChurnCalibrationModel + ChurnBacktestRun — SQLAlchemy models (M4.1). ChurnCalibrationModel: versioned isotonic regression models. - organization_id=NULL → global fallback model. - At most…
- [churn_event.py](<../services/backend-api/src/models/churn_event.py>) — CustomerChurnEvent — SQLAlchemy model (M4.1). Stores manual, CSV-imported, and auto-suggested churn labels. Drives the calibration training set.
- [churn_label_suggestion.py](<../services/backend-api/src/models/churn_label_suggestion.py>) — ChurnLabelSuggestion — SQLAlchemy model (crm-churn-labels, data-model aspect). CRM-sourced lost-renewal suggestions awaiting operator review. Pending suggestions never enter…
- [churn_playbook.py](<../services/backend-api/src/models/churn_playbook.py>) — ChurnPlaybook + ChurnPlaybookExecution — SQLAlchemy models (M4.1). ChurnPlaybook: reusable prevention plans binding a probability range to a sequence of automation actions. System templates…
- [conversation.py](<../services/backend-api/src/models/conversation.py>) — Declarations: Conversation
- [conversation_folder.py](<../services/backend-api/src/models/conversation_folder.py>) — Declarations: ConversationFolder
- [conversation_message.py](<../services/backend-api/src/models/conversation_message.py>) — Declarations: ConversationMessage
- [copilot_schema_whitelist.py](<../services/backend-api/src/models/copilot_schema_whitelist.py>) — Declarations: CopilotSchemaWhitelist
- [crm_enrichment.py](<../services/backend-api/src/models/crm_enrichment.py>) — CRM enrichment model — per-customer HubSpot data store. One row per (organization_id, customer_email). Written by the hubspot-sync worker task and read by the crm-health-component and…
- [custom_category.py](<../services/backend-api/src/models/custom_category.py>) — Declarations: CustomCategory
- [customer_analysis_action.py](<../services/backend-api/src/models/customer_analysis_action.py>) — Declarations: CustomerAnalysisAction
- [customer_health.py](<../services/backend-api/src/models/customer_health.py>) — Declarations: CustomerHealth
- [customer_health_history.py](<../services/backend-api/src/models/customer_health_history.py>) — Declarations: CustomerHealthHistory
- [customer_usage.py](<../services/backend-api/src/models/customer_usage.py>) — Per-customer product-usage rollup for the product-usage-enrichment feature. One row per ``(organization_id, customer_email)``. Populated and refreshed by the Celery task…
- [customer_usage_history.py](<../services/backend-api/src/models/customer_usage_history.py>) — Daily per-customer snapshot of the ``customer_usage`` rollup — storage only. One immutable row per ``(organization_id, customer_email, snapshot_date)``, written by the worker's daily…
- [dashboard_layout.py](<../services/backend-api/src/models/dashboard_layout.py>) — Declarations: UserDashboardLayout
- [feedback.py](<../services/backend-api/src/models/feedback.py>) — Declarations: FeedbackItem
- [feedback_note.py](<../services/backend-api/src/models/feedback_note.py>) — Declarations: FeedbackNote
- [feedback_response.py](<../services/backend-api/src/models/feedback_response.py>) — Declarations: FeedbackResponse
- [feedback_source.py](<../services/backend-api/src/models/feedback_source.py>) — Declarations: FeedbackSource
- [feedback_source_event.py](<../services/backend-api/src/models/feedback_source_event.py>) — Declarations: FeedbackSourceEvent
- [feedback_workflow_event.py](<../services/backend-api/src/models/feedback_workflow_event.py>) — Declarations: FeedbackWorkflowEvent
- [feedback_zendesk_sync.py](<../services/backend-api/src/models/feedback_zendesk_sync.py>) — Feedback-Zendesk status sync sidecar. Remembers the last-observed Zendesk ticket status per feedback item. Written by the status-sync poll/webhook path (poll-task, webhook-realtime…
- [hubspot_integration.py](<../services/backend-api/src/models/hubspot_integration.py>) — HubSpot CRM integration model. One row per organization. access_token is Fernet-encrypted via encrypt_api_key (never stored plaintext). See src/utils/encryption.py.
- [integration.py](<../services/backend-api/src/models/integration.py>) — Declarations: Integration, SlackAlertLog
- [intercom_integration.py](<../services/backend-api/src/models/intercom_integration.py>) — Org-wide Intercom connection via a private-app Access Token (token-paste). Mirrors ZendeskIntegration: one row per organization, BYO credential, secrets Fernet-encrypted at the route layer.…
- [jira_integration.py](<../services/backend-api/src/models/jira_integration.py>) — Jira Cloud integration model. One row per organization. api_token is Fernet-encrypted via encrypt_api_key (never stored plaintext). Encryption happens in the route layer, not here. See…
- [linear_integration.py](<../services/backend-api/src/models/linear_integration.py>) — Declarations: LinearIntegration, LinearTeamMapping, LinearStatusMapping, FeedbackLinearIssue
- [llm_model_price.py](<../services/backend-api/src/models/llm_model_price.py>) — Declarations: LLMModelPrice
- [llm_usage_log.py](<../services/backend-api/src/models/llm_usage_log.py>) — Declarations: LLMUsageLog
- [notification.py](<../services/backend-api/src/models/notification.py>) — Declarations: Notification
- [oidc_config.py](<../services/backend-api/src/models/oidc_config.py>) — OIDC SSO configuration model. One row per organization. client_secret is Fernet-encrypted via encrypt_api_key (never stored plaintext). secret_hint holds the last chars of plaintext for…
- [org_ai_config.py](<../services/backend-api/src/models/org_ai_config.py>) — Declarations: OrgAIConfig
- [org_api_key.py](<../services/backend-api/src/models/org_api_key.py>) — Declarations: OrgApiKey
- [org_classifier.py](<../services/backend-api/src/models/org_classifier.py>) — OrgClassifierModel + OrgClassifierEvalRun — SQLAlchemy models (M5.2). OrgClassifierModel: versioned per-org corrections classifier artifact (TF-IDF vocab/idf + logreg coef/intercept +…
- [organization.py](<../services/backend-api/src/models/organization.py>) — Declarations: Organization
- [outreach_campaign.py](<../services/backend-api/src/models/outreach_campaign.py>) — Declarations: OutreachCampaign, OutreachCampaignRecipient
- [pending_feedback.py](<../services/backend-api/src/models/pending_feedback.py>) — Declarations: PendingFeedback
- [playbook_task.py](<../services/backend-api/src/models/playbook_task.py>) — PlaybookTask — SQLAlchemy model (playbook-action-types M3). A durable follow-up task spawned by `create_task` / `schedule_task` playbook actions. Internal and self-host native (offline);…
- [query_template.py](<../services/backend-api/src/models/query_template.py>) — Declarations: QueryTemplate
- [query_template_mapping.py](<../services/backend-api/src/models/query_template_mapping.py>) — Declarations: QueryTemplateMapping
- [report.py](<../services/backend-api/src/models/report.py>) — Declarations: Report
- [report_schedule.py](<../services/backend-api/src/models/report_schedule.py>) — Declarations: ReportSchedule
- [response_template.py](<../services/backend-api/src/models/response_template.py>) — Declarations: ResponseTemplate
- [salesforce_integration.py](<../services/backend-api/src/models/salesforce_integration.py>) — Salesforce CRM integration model. One row per organization. refresh_token is Fernet-encrypted via encrypt_api_key (never stored plaintext). See src/utils/encryption.py. Mirrors…
- [saml_auth_request.py](<../services/backend-api/src/models/saml_auth_request.py>) — SAML replay / InResponseTo store model. One row per SP-initiated AuthnRequest we issue. The AuthnRequest `ID` is the primary key; the ACS marks it `consumed_at` exactly once via a…
- [saml_config.py](<../services/backend-api/src/models/saml_config.py>) — SAML SSO configuration model. One row per organization. idp_x509_cert is the IdP's PUBLIC signing certificate (PEM) — it is NOT a secret and NOT encrypted (contrast…
- [saved_view.py](<../services/backend-api/src/models/saved_view.py>) — SavedView model for persisting analytics page state.
- [shared_link.py](<../services/backend-api/src/models/shared_link.py>) — SharedLink model for public dashboard sharing via token-based links.
- [subscription.py](<../services/backend-api/src/models/subscription.py>) — Declarations: Subscription
- [team_invite.py](<../services/backend-api/src/models/team_invite.py>) — TeamInvite model for managing team invitations.
- [usage.py](<../services/backend-api/src/models/usage.py>) — Declarations: UsageRecord
- [usage_event.py](<../services/backend-api/src/models/usage_event.py>) — Raw usage-event log for the product-usage enrichment feature. Each accepted event from POST /api/v1/webhooks/usage is persisted here before being handed to the Celery worker for rollup and…
- [user.py](<../services/backend-api/src/models/user.py>) — Declarations: User
- [user_alert_preference.py](<../services/backend-api/src/models/user_alert_preference.py>) — Declarations: UserAlertPreference
- [webhook_delivery.py](<../services/backend-api/src/models/webhook_delivery.py>) — Declarations: WebhookDelivery
- [webhook_endpoint.py](<../services/backend-api/src/models/webhook_endpoint.py>) — Declarations: WebhookEndpoint
- [weekly_insight.py](<../services/backend-api/src/models/weekly_insight.py>) — WeeklyInsight model for storing AI-generated weekly insight summaries.
- [zendesk_integration.py](<../services/backend-api/src/models/zendesk_integration.py>) — Zendesk integration model. One row per organization. api_token is Fernet-encrypted via encrypt_api_key (never stored plaintext). webhook_secret is likewise Fernet-encrypted, but nullable —…

## `services/backend-api/src/schemas`

[Directory guide](<../services/backend-api/src/schemas/directory.md>)

- [__init__.py](<../services/backend-api/src/schemas/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [ai_readiness.py](<../services/backend-api/src/schemas/ai_readiness.py>) — Pydantic schema for the AI training-readiness report (M5.0). Covers: - GET /api/v1/analytics/ai-readiness (org-level, any authenticated role)
- [churn_accuracy.py](<../services/backend-api/src/schemas/churn_accuracy.py>) — Pydantic schemas for churn accuracy API endpoints (M4.1 Phase 6.2a). Covers: - GET /api/v1/analytics/churn-accuracy (org-level, Business+) - GET /api/v1/system/churn-accuracy (system admin…
- [churn_calibration.py](<../services/backend-api/src/schemas/churn_calibration.py>) — Pydantic schemas for ChurnCalibrationModel and ChurnBacktestRun (M4.1).
- [churn_cohort.py](<../services/backend-api/src/schemas/churn_cohort.py>) — Pydantic response schemas for the churn cohort analytics endpoint (M4.1 Phase 4).
- [churn_event.py](<../services/backend-api/src/schemas/churn_event.py>) — Pydantic schemas for CustomerChurnEvent (M4.1). Separate from src/api/schemas.py to keep churn schemas self-contained.
- [churn_label_gate.py](<../services/backend-api/src/schemas/churn_label_gate.py>) — Pydantic schemas for GET /api/v1/settings/ai/churn/label-gate (churn-label-gate-study aspect 2, M5.3 disclosure layer). Mirrors the eval_churn_label_gate.py script's committed JSON artifact…
- [churn_playbook.py](<../services/backend-api/src/schemas/churn_playbook.py>) — Pydantic schemas for ChurnPlaybook and ChurnPlaybookExecution (M4.1).
- [churn_suggestion.py](<../services/backend-api/src/schemas/churn_suggestion.py>) — Pydantic schemas for ChurnLabelSuggestion — review-queue aspect. Confirm is the ONLY path that turns a CRM-sourced suggestion into a trainable CustomerChurnEvent(source='manual'). See…
- [classifier_accuracy.py](<../services/backend-api/src/schemas/classifier_accuracy.py>) — Pydantic schemas for GET /api/v1/settings/ai/classifier/accuracy (settings-api-and-accuracy-card aspect, M5.2 disclosure layer). Mirrors src/schemas/sentiment_accuracy.py's /…
- [cohort.py](<../services/backend-api/src/schemas/cohort.py>) — Shared cohort contract — segment-actions / bulk-actions-api. `Cohort` is how an operator selects a set of customers to act on, either by an explicit email list or by the same filter…
- [embedding_accuracy.py](<../services/backend-api/src/schemas/embedding_accuracy.py>) — Pydantic schemas for GET /api/v1/settings/ai/embeddings/accuracy (retrieval-eval-card aspect, M5.4 disclosure layer). Mirrors the eval_embeddings.py script's committed JSON artifact…
- [sentiment_accuracy.py](<../services/backend-api/src/schemas/sentiment_accuracy.py>) — Pydantic schemas for GET /api/v1/settings/ai/sentiment/accuracy (eval-harness-and-card aspect, M5.1 disclosure layer). Mirrors the eval_sentiment.py script's committed JSON artifact…

## `services/backend-api/src/scripts`

[Directory guide](<../services/backend-api/src/scripts/directory.md>)

- [setup_email_templates.py](<../services/backend-api/src/scripts/setup_email_templates.py>) — Script to create/update email templates in Resend. Usage: cd services/backend-api python -m src.scripts.setup_email_templates --create # Create new templates python -m…

## `services/backend-api/src/services`

[Directory guide](<../services/backend-api/src/services/directory.md>)

- [__init__.py](<../services/backend-api/src/services/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [ai_correction_service.py](<../services/backend-api/src/services/ai_correction_service.py>) — AI correction service — shared helper for persisting human-in-the-loop correction/rating signals. Extracted from the internal ``POST /api/v1/ai-corrections`` route so that both the internal…
- [asana_adapter.py](<../services/backend-api/src/services/asana_adapter.py>) — Pure Asana task-state -> status_sync_core category adapter (no I/O). Verbatim mirror of the worker-owned services/worker-service/src/services/asana_adapter.py (backend-api cannot import the…
- [asana_client.py](<../services/backend-api/src/services/asana_client.py>) — Asana REST API client (backend-connection aspect, Phase 2). Thin httpx wrapper around the Asana API v1, authenticated with a Bearer Personal Access Token (PAT) against the fixed host…
- [asana_status_reconcile.py](<../services/backend-api/src/services/asana_status_reconcile.py>) — Backend-side reconcile port for inbound Asana status-sync (status-sync-realtime-mapping/asana-webhook aspect). This is the backend-api mirror of the worker poller's `_sync_asana_org_body`…
- [audit_service.py](<../services/backend-api/src/services/audit_service.py>) — Audit logging service for tracking team management actions.
- [automation_engine.py](<../services/backend-api/src/services/automation_engine.py>) — AutomationEngine — Phase 2 execution engine for AI Workflow Automation (M4.4). Evaluates active automation rules against events and fires their actions. Dispatch points (callers): -…
- [cache_service.py](<../services/backend-api/src/services/cache_service.py>) — Redis cache service for server-side caching. Uses Redis DB 2 (reserved for application cache).
- [churn_calibrator.py](<../services/backend-api/src/services/churn_calibrator.py>) — Churn probability calibration service. Maps 0–100 heuristic churn risk scores to calibrated 30-day churn probabilities using isotonic regression with bootstrap confidence intervals. No I/O,…
- [classifier_predict.py](<../services/backend-api/src/services/classifier_predict.py>) — Per-org corrections-classifier loader + predict + override helper — backend-api (M5.2 predict-seam-resolver). Independent mirror of…
- [classifier_resolver.py](<../services/backend-api/src/services/classifier_resolver.py>) — Org-scoped corrections-classifier mode resolver — M5.2 predict-seam-resolver. Single entry point for both classifier call sites: resolved = resolve_classifier(org_id, "sentiment", db) if…
- [cohort_service.py](<../services/backend-api/src/services/cohort_service.py>) — Cohort resolution — segment-actions / bulk-actions-api. Resolves a `Cohort` (explicit email list OR filter) into the matching `CustomerHealth` rows for the caller's organization. Shared by…
- [copilot_rate_limiter.py](<../services/backend-api/src/services/copilot_rate_limiter.py>) — Copilot rate limiter service (M2.2 AI Copilot). Enforces: - Free tier: 10 queries/day per user - Monthly token budget per organization
- [crm_churn_label_options.py](<../services/backend-api/src/services/crm_churn_label_options.py>) — CRM churn-label options seam (org-config-api-and-ui aspect, Phase 1). `fetch_renewal_options(provider, integration) -> (options, reason)` is the single backend-side CRM metadata call shared…
- [crm_integration_common.py](<../services/backend-api/src/services/crm_integration_common.py>) — Shared CRM integration helpers: one-CRM-per-org guard + provider purge. Used by both hubspot_integration.py and salesforce_integration.py so the one-CRM-per-org invariant (PRD locked…
- [custom_category_service.py](<../services/backend-api/src/services/custom_category_service.py>) — Shared CRUD for CustomCategory — used by both the internal ``/api/v1/categories/custom`` routes and the public ``/api/public/v1/categories`` routes so create/update/delete/list semantics…
- [customer_profile_serializer.py](<../services/backend-api/src/services/customer_profile_serializer.py>) — Shared Customer 360 profile serializer. Extracted from ``routes/customers.py:get_customer_profile`` so that the v1 route and the public REST API surface share exactly one field-mapping…
- [customer_tags.py](<../services/backend-api/src/services/customer_tags.py>) — Shared customer tag application — extracted from the `bulk/tags` handler (`src/api/routes/customers.py`) so the copilot action registry can reuse the exact same set-union/difference…
- [customer_timeline_service.py](<../services/backend-api/src/services/customer_timeline_service.py>) — Customer Timeline Service — merges multiple event sources into a reverse-chronological, cursor-paged event stream. Constants (module-level): DORMANCY_DAYS = 14 — gap threshold for…
- [email_parser.py](<../services/backend-api/src/services/email_parser.py>) — Smart email body parsing for inbound email feedback. Strips forwarding headers, signatures, quoted replies, and HTML to extract clean feedback text from forwarded emails.
- [email_service.py](<../services/backend-api/src/services/email_service.py>) — Email service using Resend for sending transactional emails. Fetches templates from Resend, renders variables locally, then sends.
- [event_connection_manager.py](<../services/backend-api/src/services/event_connection_manager.py>) — WebSocket connection manager for real-time event broadcasting. Tracks active connections grouped per organization. Supports broadcast to an entire org (with optional actor exclusion) and…
- [event_emitter.py](<../services/backend-api/src/services/event_emitter.py>) — Event emitter helper for broadcasting real-time events to org members. Usage from route handlers: from src.services.event_emitter import emit_event await emit_event( org_id=current_org.id,…
- [feedback_service.py](<../services/backend-api/src/services/feedback_service.py>) — Shared feedback-mutation helpers used by both the internal dashboard API (``src/api/routes/feedback.py``) and the public write API (``src/api/routes/public_api.py``). Keeping this logic in…
- [google_auth.py](<../services/backend-api/src/services/google_auth.py>) — Google OAuth token verification service.
- [health_score_service.py](<../services/backend-api/src/services/health_score_service.py>) — Customer health score computation service. Computes a 0-100 health score per customer using churn-heavy weights. Higher score = healthier customer.
- [hubspot_writeback_validation.py](<../services/backend-api/src/services/hubspot_writeback_validation.py>) — HubSpot writeback-field validation (writeback-config-api aspect). Backend owns this validation (it cannot import the worker's write-client), so it mirrors the same httpx-Bearer GET pattern…
- [issue_drafter.py](<../services/backend-api/src/services/issue_drafter.py>) — Issue Drafter Service (ai-drafted-issue-content). Generates a work-tracker (Jira/Asana) title + body draft from a customer feedback item using the org's configured LLM (cloud BYOK or…
- [jira_client.py](<../services/backend-api/src/services/jira_client.py>) — Jira Cloud REST API client (backend-connection aspect, Phase 2). Thin httpx wrapper around the Jira Cloud REST API v3, authenticated with HTTP Basic auth (email + Atlassian API token) — see…
- [jira_status_reconcile.py](<../services/backend-api/src/services/jira_status_reconcile.py>) — Backend-side reconcile port for inbound Jira status-sync (status-sync-realtime-mapping/jira-webhook aspect). This is the backend-api mirror of the worker poller's `_sync_jira_org_body` +…
- [linear_client.py](<../services/backend-api/src/services/linear_client.py>) — Linear GraphQL API client. Wraps Linear's GraphQL API using httpx.AsyncClient. All mutations require an OAuth access token from the connected org.
- [oauth_state.py](<../services/backend-api/src/services/oauth_state.py>) — Stateless `state` signing for the OAuth connect flows (Slack, Intercom, Linear). Mirrors `salesforce_integration.py`'s `_sign_state`/`_verify_state` mechanics (HMAC-SHA256 keyed on the…
- [oidc_provider.py](<../services/backend-api/src/services/oidc_provider.py>) — OIDC provider service: discovery, JWKS, authorize-URL construction, code exchange, and ID-token validation for `oidc-login-flow`. No route wiring lives here — `src/api/routes/auth.py` calls…
- [outreach_drafter.py](<../services/backend-api/src/services/outreach_drafter.py>) — Outreach Drafter Service (bulk-campaign-api aspect). Drafts an outreach campaign {subject, body} from org context (product name, brand voice, tone) plus optional cohort context (count +…
- [outreach_sender_contract.py](<../services/backend-api/src/services/outreach_sender_contract.py>) — Outreach send-path contract constants (outreach-core aspect). The worker's `outreach_sender` and (future) backend send paths must agree on the shared Redis cooldown key scheme —…
- [outreach_templates.py](<../services/backend-api/src/services/outreach_templates.py>) — Built-in outreach template registry (outreach-core aspect). Single source of truth for the two seeded send_email template keys (`playbook_seeder.py:111,215` reference `weekly_digest_entry`…
- [outreach_tokens.py](<../services/backend-api/src/services/outreach_tokens.py>) — Unsubscribe token helpers — canonical backend implementation (outreach-core aspect). Stateless, signed token over ``'{org_id}:{email}'`` (HMAC-SHA256 keyed by `LLM_ENCRYPTION_KEY`),…
- [playbook_seeder.py](<../services/backend-api/src/services/playbook_seeder.py>) — Playbook template seeder (M4.1 Phase 5.1). Idempotent — safe to call on every startup. Inserts the 7 pre-built system templates defined in SEED_TEMPLATES if they don't already exist…
- [response_generator.py](<../services/backend-api/src/services/response_generator.py>) — Response Generator Service. Handles: - Variable resolution: replace {{var}} placeholders in template bodies - AI response generation: build LLM prompt from feedback context, call the model
- [response_sender.py](<../services/backend-api/src/services/response_sender.py>) — Response Sender Service. Handles sending a response through various integration channels: - Slack: thread reply via chat.postMessage - Intercom: admin reply to conversation - Linear:…
- [salesforce_writeback_validation.py](<../services/backend-api/src/services/salesforce_writeback_validation.py>) — Salesforce writeback-field validation (writeback-config-api aspect). Backend owns this validation (it cannot import the worker's write-client), so it mints a short-lived access token…
- [saml_provider.py](<../services/backend-api/src/services/saml_provider.py>) — SAML provider service: build an SP-initiated (unsigned) AuthnRequest and validate a returned SAML Response/Assertion to a trusted identity. No route wiring lives here —…
- [saml_replay.py](<../services/backend-api/src/services/saml_replay.py>) — SAML replay / InResponseTo store — the explicit pending -> consumed state machine over `saml_auth_requests` that makes the ACS safe. Route-free by design (mirrors saml_provider.py):…
- [segment_service.py](<../services/backend-api/src/services/segment_service.py>) — Customer segment classifier. ``classify_segment(...) -> str`` is a PURE, no-DB rule engine that assigns a single segment slug to a customer, given already-computed health/usage/ sentiment…
- [sentiment_resolver.py](<../services/backend-api/src/services/sentiment_resolver.py>) — Org-scoped sentiment provider resolver. Single entry point for both sentiment call sites: resolved = resolve_sentiment_provider(org_id, db) provider_name = resolved.provider if resolved…
- [status_sync_core.py](<../services/backend-api/src/services/status_sync_core.py>) — Pure, no-I/O reconcile core for inbound Jira status sync. This module MUST NOT import FastAPI, SQLAlchemy, or any DB/network client. It is copied verbatim into the worker service (see…
- [usage_decline_labels_core.py](<../services/backend-api/src/services/usage_decline_labels_core.py>) — Usage-decline churn-label detector core (detector-core aspect). Pure logic only — no database, no Celery, no HTTP. Every function here takes plain data and returns plain data so it is…
- [usage_score_service.py](<../services/backend-api/src/services/usage_score_service.py>) — Usage score computation service. ``compute_usage_score(rollup, now) -> int`` blends three dimensions: - Recency (weight 0.50): time since last_active_at - Frequency (weight 0.30):…
- [usage_trend_severity.py](<../services/backend-api/src/services/usage_trend_severity.py>) — Usage-trend severity ordering — the single source of truth for "is this transition strictly worsening?" used by the AutomationEngine's usage_trend trigger checker (backend-api) and the…
- [user_service.py](<../services/backend-api/src/services/user_service.py>) — Shared user service for cleanup and deletion operations.
- [webhook_dispatcher.py](<../services/backend-api/src/services/webhook_dispatcher.py>) — Webhook Dispatch Engine (M3.1 Phase 2). dispatch_webhook_event() is the main public entry point. It queries all active WebhookEndpoints for an organisation that subscribe to the given…
- [workflow_service.py](<../services/backend-api/src/services/workflow_service.py>) — Workflow service — auto-assignment engine and timeline event helpers.
- [ws_connection_manager.py](<../services/backend-api/src/services/ws_connection_manager.py>) — WebSocket connection manager for the AI Copilot (M2.2). Tracks active connections per user, supports sending targeted messages.
- [zendesk_client.py](<../services/backend-api/src/services/zendesk_client.py>) — Zendesk REST API client (backend-connection aspect, Phase 2). Thin httpx wrapper around the Zendesk REST API v2, authenticated with HTTP Basic auth using the token-auth convention…
- [zendesk_status_core.py](<../services/backend-api/src/services/zendesk_status_core.py>) — Pure, no-I/O reconcile core for inbound Zendesk status sync. This module MUST NOT import FastAPI, SQLAlchemy, or any DB/network client. It is copied verbatim into the worker service (see…
- [zendesk_status_reconcile.py](<../services/backend-api/src/services/zendesk_status_reconcile.py>) — Backend-side reconcile port for inbound Zendesk status-sync (zendesk-status-sync/webhook-realtime aspect). See…

## `services/backend-api/src/services/copilot`

[Directory guide](<../services/backend-api/src/services/copilot/directory.md>)

- [__init__.py](<../services/backend-api/src/services/copilot/__init__.py>) — AI Copilot query engine — intent classification, SQL generation, safety guardrails, and self-learning template system.
- [action_proposer.py](<../services/backend-api/src/services/copilot/action_proposer.py>) — Deterministic action proposer for the AI Copilot (M2.2). Pure, synchronous proposal logic: inspects a SQL result's columns to decide which registry actions apply and builds the `actions`…
- [action_registry.py](<../services/backend-api/src/services/copilot/action_registry.py>) — Copilot action registry (copilot-suggested-actions, PRD M1/M5). The registry is the ONLY dispatch path for copilot-suggested actions: a stable `action` id maps to an `ActionEntry` declaring…
- [context_resolver.py](<../services/backend-api/src/services/copilot/context_resolver.py>) — Context Scope Resolver — builds LLM context based on selected scope + @mentions. Scopes: all_data, feedbacks, customers, pain_points, feature_requests, dashboard @mentions: @customer:email,…
- [intent_classifier.py](<../services/backend-api/src/services/copilot/intent_classifier.py>) — Intent Classifier — classifies user messages into data, analysis, or general intents. Classification approach: 1. Rule-based regex patterns (fast, no LLM cost) 2. If ambiguous (low…
- [llm_resolver.py](<../services/backend-api/src/services/copilot/llm_resolver.py>) — LLM resolver for the Copilot's answer-generation path. Mirrors the worker-service's local/keyless pattern (worker-service/src/llm/org_resolver.py) but lives in backend-api to avoid…
- [report_generator.py](<../services/backend-api/src/services/copilot/report_generator.py>) — Report Generator — generates structured report data for On-Demand AI Reports (M2.4). Supports 4 report types: - executive_summary: High-level overview for leadership - customer_health:…
- [response_formatter.py](<../services/backend-api/src/services/copilot/response_formatter.py>) — Response formatter for AI Copilot (M2.2 Task #7). Converts SQL results + LLM text into structured, renderable responses: - Table formatter: converts SQL rows to table structure - Chart…
- [schema_whitelist.py](<../services/backend-api/src/services/copilot/schema_whitelist.py>) — Schema Whitelist — defines the approved tables and columns for copilot SQL queries. Only tables/columns in this whitelist are allowed in LLM-generated SQL. Sensitive tables (users,…
- [sql_executor.py](<../services/backend-api/src/services/copilot/sql_executor.py>) — SQL Executor — executes validated SQL with safety features. Features: - Parameterized query execution - 5-second timeout enforcement - Structured result format: { columns, rows, row_count,…
- [sql_generator.py](<../services/backend-api/src/services/copilot/sql_generator.py>) — SQL Generator — generates safe SQL from natural language queries using LLM. Generation flow: 1. Build LLM prompt with schema whitelist + examples 2. LLM generates candidate SQL (via…
- [sql_validator.py](<../services/backend-api/src/services/copilot/sql_validator.py>) — SQL Validator — enforces all safety guardrails on LLM-generated SQL. Guardrails (PRD §5.3): - Read-only: Only SELECT statements - Schema whitelist: Only approved tables/columns - Join…
- [template_matcher.py](<../services/backend-api/src/services/copilot/template_matcher.py>) — Template Matcher — semantic matching of user questions against saved query templates. Matching flow: 1. Normalize user question (lowercase, remove stopwords) 2. Generate embedding via the…
- [template_saver.py](<../services/backend-api/src/services/copilot/template_saver.py>) — Template Saver — auto-saves successful LLM-generated SQL as query templates. Saving flow: 1. Check if identical SQL already exists as a template (idempotent) 2. If SQL exists → add new…

## `services/backend-api/src/services/embeddings`

[Directory guide](<../services/backend-api/src/services/embeddings/directory.md>)

- [__init__.py](<../services/backend-api/src/services/embeddings/__init__.py>) — Embeddings package — provider-agnostic embedding abstraction for backend-api. Public surface: EmbeddingProvider — ABC (for type hints in consumers) EmbeddingProviderFactory — name →…
- [base.py](<../services/backend-api/src/services/embeddings/base.py>) — EmbeddingProvider — abstract base class for all embedding providers. Every provider must: - Implement embed(text: str) -> list[float] Normalise the provider SDK's response to a flat Python…
- [defaults.py](<../services/backend-api/src/services/embeddings/defaults.py>) — Provider → default embedding model lookup. Pure helper, no route/DB imports. Mirrors src/api/routes/ai_settings.py::_default_embedding_model exactly (see that function's docstring) — this…
- [factory.py](<../services/backend-api/src/services/embeddings/factory.py>) — EmbeddingProviderFactory — creates embedding provider instances by name. Mirrors the shape of services/worker-service/src/llm/factory.py (LLMProviderFactory) for consistency. Cross-service…
- [resolver.py](<../services/backend-api/src/services/embeddings/resolver.py>) — Org-scoped embedding provider resolver. Single entry point for all consumers (template-matching-local, copilot-llm-local): embedder = resolve_embedding_provider(org_id, db) if embedder is…

## `services/backend-api/src/services/embeddings/providers`

[Directory guide](<../services/backend-api/src/services/embeddings/providers/directory.md>)

- [__init__.py](<../services/backend-api/src/services/embeddings/providers/__init__.py>) — Embedding provider implementations.
- [google.py](<../services/backend-api/src/services/embeddings/providers/google.py>) — Google (Gemini) embedding provider. Uses google-generativeai SDK (google-generativeai>=0.8.0, already in requirements.txt for both backend-api and worker-service). Note: the…
- [local.py](<../services/backend-api/src/services/embeddings/providers/local.py>) — LocalEmbeddingProvider — in-process, CPU, air-gappable embedding provider. Uses sentence-transformers to run embedding models locally (no network call per embed(), no API key). Mirrors the…
- [openai.py](<../services/backend-api/src/services/embeddings/providers/openai.py>) — OpenAI embedding provider. Mirrors the embedding call already in template_matcher._call_embedding_api (L120-134), but wraps it in the EmbeddingProvider interface so it is injectable and…
- [openai_compatible.py](<../services/backend-api/src/services/embeddings/providers/openai_compatible.py>) — OpenAI-compatible embedding provider (keyless / local). Targets any server that exposes the OpenAI Embeddings API format: - Ollama (http://localhost:11434/v1) - LM Studio, vLLM, llama.cpp,…

## `services/backend-api/src/templates`

[Directory guide](<../services/backend-api/src/templates/directory.md>)

- [__init__.py](<../services/backend-api/src/templates/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [email_templates.py](<../services/backend-api/src/templates/email_templates.py>) — Rereflect Email Templates - Sunset Horizon Design System These templates use email-safe CSS with the Rereflect color palette: - Primary gradient: #f97316 → #ea580c (coral/orange) -…

## `services/backend-api/src/utils`

[Directory guide](<../services/backend-api/src/utils/directory.md>)

- [__init__.py](<../services/backend-api/src/utils/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [byok.py](<../services/backend-api/src/utils/byok.py>) — BYOK (Bring Your Own Key) resolution helper. Provides a single shared helper `resolve_org_byok_key` that retrieves a decrypted API key for a provider from the org's OrgApiKey table. This…
- [encryption.py](<../services/backend-api/src/utils/encryption.py>) — Fernet symmetric encryption utilities for BYOK API key storage. The encryption key is sourced from the LLM_ENCRYPTION_KEY environment variable. Generate once: python -c "from…
- [ssrf.py](<../services/backend-api/src/utils/ssrf.py>) — Shared SSRF gate for hosts derived from untrusted operator/IdP-supplied input (e.g. an OIDC issuer or jwks_uri) that this service is about to fetch. Same semantics as the per-integration…

## `services/backend-api/templates`

[Directory guide](<../services/backend-api/templates/directory.md>)

No immediate baseline/preparation files.

## `services/backend-api/templates/email`

[Directory guide](<../services/backend-api/templates/email/directory.md>)

- [alert_notification.html](<../services/backend-api/templates/email/alert_notification.html>) — Static/configuration artifact; inspect its consumer.
- [daily_alert_digest.html](<../services/backend-api/templates/email/daily_alert_digest.html>) — Static/configuration artifact; inspect its consumer.
- [member_removed.html](<../services/backend-api/templates/email/member_removed.html>) — Static/configuration artifact; inspect its consumer.
- [role_change.html](<../services/backend-api/templates/email/role_change.html>) — Static/configuration artifact; inspect its consumer.

## `services/backend-api/tests`

[Directory guide](<../services/backend-api/tests/directory.md>)

- [__init__.py](<../services/backend-api/tests/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [conftest.py](<../services/backend-api/tests/conftest.py>) — Pytest configuration and fixtures for backend tests.
- [saml_fixtures.py](<../services/backend-api/tests/saml_fixtures.py>) — Test fixtures for SAML provider tests. Everything is generated in-test with a throwaway RSA key + self-signed X.509 cert (no network, no live IdP). `make_keypair_cert()` yields the PEM…
- [test_action_proposer.py](<../services/backend-api/tests/test_action_proposer.py>) — Phase D TDD — deterministic action proposer (copilot-suggested-actions). Unit tests for the pure, synchronous proposer module (`src/services/copilot/action_proposer.py`): -…
- [test_action_registry.py](<../services/backend-api/tests/test_action_registry.py>) — TDD tests — action registry (`src/services/copilot/action_registry.py`). The registry is the ONLY dispatch path for copilot-suggested actions (PRD M1): it maps a stable `action` id to an…
- [test_active_days_14d_migration.py](<../services/backend-api/tests/test_active_days_14d_migration.py>) — TDD migration test for Phase B of the usage-trend-churn-signal aspect (rollup-rewindow-fix): `customer_usage.active_days_14d` (Integer, nullable, no server_default, no backfill). Strategy…
- [test_ai_correction_service.py](<../services/backend-api/tests/test_ai_correction_service.py>) — Characterization + behavior tests for `create_ai_correction` (src/services/ai_correction_service.py). Locks the current (pre-bulk) default behavior — commits internally — before adding an…
- [test_ai_correction_service_urgency.py](<../services/backend-api/tests/test_ai_correction_service_urgency.py>) — TDD tests for the shared urgency corrected-value constant/helper (capture-seam Phase 1) — `services/ai_correction_service.py`. Goal: a single backend source of truth for…
- [test_ai_corrections.py](<../services/backend-api/tests/test_ai_corrections.py>) — TDD tests for AI Human-in-the-Loop corrections (Track B). Covers: 1. test_submit_thumbs_up 2. test_submit_thumbs_down_with_text 3. test_submit_category_correction 4.…
- [test_ai_readiness.py](<../services/backend-api/tests/test_ai_readiness.py>) — Tests for the AI training-readiness report (M5.0) — strict TDD. Endpoint under test: GET /api/v1/analytics/ai-readiness — per-org, no-ML, read-only aggregation over FeedbackItem /…
- [test_ai_readiness_usage_trend.py](<../services/backend-api/tests/test_ai_readiness_usage_trend.py>) — SM1 surface — usage-trend addressable-population count on the M5.0 AI-readiness report (usage-trend-automation-trigger, template-and-docs aspect, S0) — strict TDD. SM1 (PRD): "The…
- [test_ai_settings.py](<../services/backend-api/tests/test_ai_settings.py>) — Tests for AI settings API endpoints. Updated for M2.1: schema expanded with provider, models, budget. BYOK key management moved to /api/v1/settings/ai/keys.
- [test_ai_settings_category_classifier_mode.py](<../services/backend-api/tests/test_ai_settings_category_classifier_mode.py>) — TDD tests for category_classifier_mode in the AI settings GET/PATCH (services/backend-api/src/api/routes/ai_settings.py). Field-substituted mirror of test_ai_settings_classifier_mode.py…
- [test_ai_settings_churn_mode.py](<../services/backend-api/tests/test_ai_settings_churn_mode.py>) — Phase 1 RED: Tests for churn_classifier_mode in the AI settings GET/PATCH (services/backend-api/src/api/routes/ai_settings.py). Mirrors test_ai_settings_classifier_mode.py's structure…
- [test_ai_settings_classifier_mode.py](<../services/backend-api/tests/test_ai_settings_classifier_mode.py>) — Phase 1 RED: Tests for classifier_mode in the AI settings GET/PATCH (services/backend-api/src/api/routes/ai_settings.py). Mirrors test_ai_settings_sentiment_provider.py's structure exactly,…
- [test_ai_settings_local_llm.py](<../services/backend-api/tests/test_ai_settings_local_llm.py>) — Tests for Feature A: Local LLM support in the AI settings API. Covers the GET/PATCH /api/v1/settings/ai endpoints: - GET returns provider, base_url, and model fields - PATCH accepts local…
- [test_ai_settings_sentiment_provider.py](<../services/backend-api/tests/test_ai_settings_sentiment_provider.py>) — Phase 3 RED: Tests for sentiment_provider in the AI settings GET/PATCH (services/backend-api/src/api/routes/ai_settings.py). Covers: - GET /api/v1/settings/ai returns sentiment_provider…
- [test_ai_settings_urgency_classifier_mode.py](<../services/backend-api/tests/test_ai_settings_urgency_classifier_mode.py>) — TDD tests for urgency_classifier_mode in the AI settings GET/PATCH (services/backend-api/src/api/routes/ai_settings.py). Field-substituted mirror of…
- [test_ai_settings_usage_churn_labels.py](<../services/backend-api/tests/test_ai_settings_usage_churn_labels.py>) — TDD tests for usage_churn_labels_mode + usage_churn_label_config in the AI settings GET/PATCH (services/backend-api/src/api/routes/ai_settings.py). Field-substituted mirror of…
- [test_analytics.py](<../services/backend-api/tests/test_analytics.py>) — Tests for the analytics trends endpoint.
- [test_anomalies.py](<../services/backend-api/tests/test_anomalies.py>) — Tests for anomaly detection API: listing, resolving, and alert preferences.
- [test_anomalies_auth.py](<../services/backend-api/tests/test_anomalies_auth.py>) — Tests for anomaly API authentication and organization isolation.
- [test_api_keys.py](<../services/backend-api/tests/test_api_keys.py>) — Tests for the `write` API-key scope (Aspect `write-scope`, Phase 1). TDD: RED -> GREEN -> REFACTOR. Coverage: - Creating a key with scopes=["write"] persists a scope string containing…
- [test_asana_client.py](<../services/backend-api/tests/test_asana_client.py>) — TDD tests for AsanaClient (src/services/asana_client.py) — Phase 2 (backend-connection). No real HTTP. Uses unittest.mock.patch on httpx.Client. Covers: construction, fixed base URL, Bearer…
- [test_asana_connection.py](<../services/backend-api/tests/test_asana_connection.py>) — TDD tests for the Asana connection routes (backend-connection aspect, Phase 3). Covers: POST /connect, GET /status, DELETE /disconnect, POST /test, GET /workspaces, GET /projects. Mocks…
- [test_asana_issues.py](<../services/backend-api/tests/test_asana_issues.py>) — TDD tests for the Asana create-task aspect (backend-create-task, Phase 2). Covers: POST /tasks, GET /tasks (list linked). Mocks AsanaClient at the route module…
- [test_asana_models.py](<../services/backend-api/tests/test_asana_models.py>) — TDD tests for Asana integration database models. Tests cover 2 new tables: 1. AsanaIntegration — org-wide Asana connection (Personal Access Token, Bearer auth) 2. FeedbackAsanaTask — links…
- [test_asana_status_sync_migration.py](<../services/backend-api/tests/test_asana_status_sync_migration.py>) — TDD tests for the model-migrations aspect of asana-status-sync: new columns on AsanaIntegration (status_sync_enabled, status_mapping) and FeedbackAsanaTask (asana_completed,…
- [test_asana_status_sync_routes.py](<../services/backend-api/tests/test_asana_status_sync_routes.py>) — TDD tests for the Asana inbound status-sync operator control routes (backend-routes aspect). Covers: - GET /api/v1/integrations/asana/status (extended with 2 new fields) - PATCH…
- [test_asana_webhook.py](<../services/backend-api/tests/test_asana_webhook.py>) — TDD tests for the Asana inbound real-time webhook receiver (status-sync-realtime-mapping/asana-webhook aspect, Phase 3). Covers: POST /api/v1/webhooks/asana/inbound/{webhook_url_token}.…
- [test_asana_webhook_migration.py](<../services/backend-api/tests/test_asana_webhook_migration.py>) — TDD tests for Phase 1 of the asana-webhook aspect (status-sync-realtime-mapping PRD): new `asana_integrations.webhook_secret` (Text, nullable, Fernet-encrypted at the route layer) and…
- [test_asana_webhook_routes.py](<../services/backend-api/tests/test_asana_webhook_routes.py>) — TDD tests for Phase 2 of the asana-webhook aspect (status-sync-realtime-mapping PRD): the enable/disable control surface for the inbound real-time Asana webhook. Covers: - POST…
- [test_auth.py](<../services/backend-api/tests/test_auth.py>) — Tests for authentication endpoints.
- [test_automation_action_support.py](<../services/backend-api/tests/test_automation_action_support.py>) — Tests for the automation trigger→action support matrix (automation-action-support R3/R4/R5) — strict TDD (RED first). The matrix is pinned to a golden fixture shared with the worker-service…
- [test_automation_email_delivery_model.py](<../services/backend-api/tests/test_automation_email_delivery_model.py>) — TDD tests for the AutomationEmailDelivery model (automation-send-customer-email, action-core aspect, Phase A). The model is the audit row for one automation `send_customer_email` action:…
- [test_automation_engine.py](<../services/backend-api/tests/test_automation_engine.py>) — TDD tests for AutomationEngine (M4.4 Phase 2). All 16 required tests — written RED first, then driven to GREEN by the implementation in src/services/automation_engine.py. Run: cd…
- [test_automation_engine_churn_trigger.py](<../services/backend-api/tests/test_automation_engine_churn_trigger.py>) — TDD tests for AutomationEngine — churn_probability_threshold trigger + mode gating (churn-triggered-playbooks, task 2). Run: cd services/backend-api && source venv/bin/activate pytest…
- [test_automation_engine_run_playbook.py](<../services/backend-api/tests/test_automation_engine_run_playbook.py>) — TDD tests for AutomationEngine — run_playbook action (churn-triggered-playbooks, task 3). An `active` automation rule can auto-run a designated churn playbook by reusing the EXISTING…
- [test_automation_engine_send_customer_email.py](<../services/backend-api/tests/test_automation_engine_send_customer_email.py>) — TDD tests for AutomationEngine — send_customer_email action (automation-send-customer-email, action-core Phase C). An automation rule can email the customer (or their CS owner) by rendering…
- [test_automation_engine_usage_trend.py](<../services/backend-api/tests/test_automation_engine_usage_trend.py>) — TDD tests for AutomationEngine — usage_trend trigger (trigger-registration, Phase 2) — strict TDD (RED first). Edge-triggered semantics: fire only on a strictly-worsening transition…
- [test_automation_rule_mode.py](<../services/backend-api/tests/test_automation_rule_mode.py>) — Tests for AutomationRule.mode (off / shadow / active) — execution-state field. `mode` is the single source of truth for evaluation. `is_active` is kept as a derived, write-through alias so…
- [test_automation_template_batch_sentiment.py](<../services/backend-api/tests/test_automation_template_batch_sentiment.py>) — Tests for the "Batch Sentiment Alert" pre-built automation template (batch-sentiment-trigger, Track A) — strict TDD (RED first). Mirrors test_automation_template_usage_trend.py. Covers: -…
- [test_automation_template_send_customer_email.py](<../services/backend-api/tests/test_automation_template_send_customer_email.py>) — Tests for the "At-Risk Customer Outreach" pre-built automation template (automation-send-customer-email, docs-and-templates aspect) — strict TDD. Mirrors…
- [test_automation_template_usage_trend.py](<../services/backend-api/tests/test_automation_template_usage_trend.py>) — Tests for the "Usage Decline Outreach" pre-built automation template (usage-trend-automation-trigger, template-and-docs aspect) — strict TDD. Covers: AC1 — GET /api/v1/automations/templates…
- [test_automations.py](<../services/backend-api/tests/test_automations.py>) — Tests for AI Workflow Automation API (M4.4) — Phase 1. TDD: tests written before implementation.
- [test_automations_activation_seeding.py](<../services/backend-api/tests/test_automations_activation_seeding.py>) — Tests for churn-cooldown seeding on rule activation (M4.4 churn-triggered- playbooks, Task 7) — strict TDD (RED first). Feature context: the churn trigger is level-based, so flipping a rule…
- [test_automations_api_batch_sentiment.py](<../services/backend-api/tests/test_automations_api_batch_sentiment.py>) — Tests for Automations API — batch_sentiment_threshold trigger config validation (batch-sentiment-trigger, Track A) — strict TDD (RED first). THE CONTRACT…
- [test_automations_api_churn.py](<../services/backend-api/tests/test_automations_api_churn.py>) — Tests for Automations API — churn_probability_threshold trigger, run_playbook action, and `mode` (M4.4 churn-triggered-playbooks, Task 5) — strict TDD (RED first).
- [test_automations_api_usage_trend.py](<../services/backend-api/tests/test_automations_api_usage_trend.py>) — Tests for Automations API — usage_trend trigger config validation (trigger-registration, Phase 3) — strict TDD (RED first).
- [test_backtest_backfill_scripts.py](<../services/backend-api/tests/test_backtest_backfill_scripts.py>) — TDD tests for backtest and backfill scripts (M1.4 Phase 7). Tests cover core logic of both scripts, not the CLI wrapper.
- [test_billing.py](<../services/backend-api/tests/test_billing.py>) — Tests for billing endpoints: checkout, portal, subscription, usage, webhooks, and feature gating.
- [test_categories.py](<../services/backend-api/tests/test_categories.py>) — Tests for custom categories API endpoints.
- [test_changelog.py](<../services/backend-api/tests/test_changelog.py>) — Tests for changelog API endpoints.
- [test_churn_accuracy_api.py](<../services/backend-api/tests/test_churn_accuracy_api.py>) — Tests for churn accuracy API endpoints (M4.1 Phase 6.2a) — strict TDD. Endpoints under test: GET /api/v1/analytics/churn-accuracy — org-level card (Business+) GET…
- [test_churn_api_extensions.py](<../services/backend-api/tests/test_churn_api_extensions.py>) — TDD tests for churn prediction API extensions (M1.4 Phase 4): - Feedback detail includes churn_risk_factors in response - Customer health response includes confidence_score and…
- [test_churn_backfill_migration.py](<../services/backend-api/tests/test_churn_backfill_migration.py>) — TDD migration tests for the historical-backfill aspect (crm-churn-labels, M7). Adds four backfill_* progress columns to BOTH hubspot_integrations and salesforce_integrations:…
- [test_churn_backfill_routes.py](<../services/backend-api/tests/test_churn_backfill_routes.py>) — Tests for historical churn-label backfill trigger/cancel routes (historical-backfill aspect, Phase 6). Routes (mirrored for both providers): POST…
- [test_churn_calibrator.py](<../services/backend-api/tests/test_churn_calibrator.py>) — Tests for ChurnCalibrator service. TDD — all 26 tests written before implementation.
- [test_churn_cohorts_api.py](<../services/backend-api/tests/test_churn_cohorts_api.py>) — Tests for GET /api/v1/analytics/churn-cohorts (M4.1 Phase 4) — strict TDD. All tests are written before the implementation (RED phase). Tests run on SQLite in-memory; production uses…
- [test_churn_events_api.py](<../services/backend-api/tests/test_churn_events_api.py>) — Tests for Churn Events API (M4.1 Phase 2.1) — strict TDD. All tests are written before the implementation (RED phase).
- [test_churn_label_gate_harness.py](<../services/backend-api/tests/test_churn_label_gate_harness.py>) — Unit tests for the churn label-gate study harness core (scripts/eval_churn_label_gate.py — importable, no DB, no CLI). Pins the things the committed artifact depends on: - the DGP produces…
- [test_churn_label_gate_route.py](<../services/backend-api/tests/test_churn_label_gate_route.py>) — Tests for GET /api/v1/settings/ai/churn/label-gate (churn-label-gate-study aspect 2). Reads the committed eval_churn_label_gate.py results artifact…
- [test_churn_label_suggestion_model.py](<../services/backend-api/tests/test_churn_label_suggestion_model.py>) — TDD tests for ChurnLabelSuggestion SQLAlchemy model (crm-churn-labels, data-model aspect). Model on test_jira_status_sync_migration.py — same fixtures, model-level asserts, no raw DDL. See…
- [test_churn_models.py](<../services/backend-api/tests/test_churn_models.py>) — TDD tests for Advanced Churn Prediction ORM models (M4.1 Phase 1.3). RED phase: all tests fail until models are implemented. Migration NOT yet available — uses in-memory SQLite via conftest…
- [test_churn_prediction_migration.py](<../services/backend-api/tests/test_churn_prediction_migration.py>) — TDD migration tests for M4.1 Advanced Churn Prediction. Strategy -------- We cannot run the full Alembic chain against SQLite (existing migrations use PostgreSQL-specific DDL such as…
- [test_churn_prediction_models.py](<../services/backend-api/tests/test_churn_prediction_models.py>) — TDD tests for churn prediction accuracy data model changes (M1.4 Phase 1): - FeedbackItem.churn_risk_factors (JSON, nullable) - CustomerHealth.confidence_score (Integer, default=0)
- [test_churn_risk.py](<../services/backend-api/tests/test_churn_risk.py>) — Tests for churn risk features: dashboard summary, feedback filters/sorting.
- [test_churn_risk_edge_cases.py](<../services/backend-api/tests/test_churn_risk_edge_cases.py>) — Tests for churn risk edge cases: NULL scores, boundary filters, mixed data.
- [test_churn_schemas.py](<../services/backend-api/tests/test_churn_schemas.py>) — TDD tests for Advanced Churn Prediction Pydantic schemas (M4.1 Phase 1.3). RED phase: all tests fail until schemas are implemented.
- [test_churn_suggestions_api.py](<../services/backend-api/tests/test_churn_suggestions_api.py>) — Tests for the CRM churn-suggestion review queue (review-queue aspect) — strict TDD, RED first. This is the feature's trust boundary: nothing a CRM suggests is trainable until a human…
- [test_classifier_accuracy_churn.py](<../services/backend-api/tests/test_classifier_accuracy_churn.py>) — Phase 2 RED: Tests for classifier_type='churn' across accuracy/versions/rollback/ resume (services/backend-api/src/api/routes/classifier_accuracy.py). Purely additive: extends…
- [test_classifier_accuracy_route.py](<../services/backend-api/tests/test_classifier_accuracy_route.py>) — Phase 2 RED: Tests for GET /api/v1/settings/ai/classifier/accuracy (settings-api-and-accuracy-card aspect, M5.2). Uses the self-contained test-helper pattern (mirrors test_ai_readiness.py)…
- [test_classifier_predict_category_routing.py](<../services/backend-api/tests/test_classifier_predict_category_routing.py>) — Phase 2 RED: Tests for _route_category_label + LoadedClassifier.predict_label_only (backend-api). Covers the built-in-vocab routing table (predict-seam spec's unambiguous-routing rule) and…
- [test_classifier_predict_contract.py](<../services/backend-api/tests/test_classifier_predict_contract.py>) — Phase 6: Contract-adapter test pinning aspect B's real `predict(artifact, text) -> (label, proba)` / `score_from_proba(proba) -> float` signature (analysis-engine's corrections_classifier…
- [test_classifier_predict_helper.py](<../services/backend-api/tests/test_classifier_predict_helper.py>) — Phase 3 RED: Tests for apply_classifier_override — off/shadow/auto branching + score mapping (backend-api). Fake feedback object + injected fake LoadedClassifier (no dependency on aspect…
- [test_classifier_predict_loader.py](<../services/backend-api/tests/test_classifier_predict_loader.py>) — Phase 2 RED: Tests for load_active_classifier — 3-tier fallback + corrupt- artifact defense + per-org cache (backend-api). Mirrors probability_updater._load_active_model /…
- [test_classifier_predict_mirror.py](<../services/backend-api/tests/test_classifier_predict_mirror.py>) — Phase 3/6 RED->GREEN: Mirror-equivalence guard (worker-service side). Diffs the normalized bodies of classifier_resolver.py and classifier_predict.py between backend-api and worker-service:…
- [test_classifier_resolver.py](<../services/backend-api/tests/test_classifier_resolver.py>) — Phase 1 RED: Tests for resolve_classifier (backend-api). Mirrors test_sentiment_resolver.py's degrade matrix, adapted for the off/shadow/auto corrections-classifier mode (M5.2…
- [test_classifier_rollback.py](<../services/backend-api/tests/test_classifier_rollback.py>) — Phase 3 RED: Tests for POST /api/v1/settings/ai/classifier/rollback (settings-api-and-accuracy-card aspect, M5.2 — optional should-have, included). Mirrors…
- [test_classifier_seam_matrix.py](<../services/backend-api/tests/test_classifier_seam_matrix.py>) — Phase 6: `test_classifier_seam_matrix` — CLASSIFIER_SEAM_CASES driven end-to-end (backend-api), through REAL resolve_classifier + load_active_classifier + aspect B's real…
- [test_classifier_versions.py](<../services/backend-api/tests/test_classifier_versions.py>) — Phase 3 RED->GREEN: Tests for classifier-model-versioning-rollback aspect (backend-routes): classifier_type validation (M8), GET .../classifier/versions (M6), durable rollback with…
- [test_cohort.py](<../services/backend-api/tests/test_cohort.py>) — TDD tests — bulk-actions-api aspect (segment-actions feature), Phase 2. Coverage: - `Cohort` validator: exactly one of emails/filter (else ValueError -> 422 when used as a request body). -…
- [test_confidence_scoring.py](<../services/backend-api/tests/test_confidence_scoring.py>) — TDD tests for confidence scoring (M1.4 Phase 3): - compute_confidence_score(feedback_count, last_feedback_at, unique_categories) -> int - update_customer_health() integrates…
- [test_context_resolver.py](<../services/backend-api/tests/test_context_resolver.py>) — TDD tests for the Context Scope Resolver (RED → GREEN → REFACTOR). Tests cover: - @mention parsing from user messages - Scope-based context building for each scope type - Org isolation…
- [test_conversation_folders_api.py](<../services/backend-api/tests/test_conversation_folders_api.py>) — TDD tests for Conversation Folders REST API (M2.2). Tests cover: - Folders CRUD: list, create, update, delete - Org scoping - Plan gating (Pro+ required) - Move conversations to null folder…
- [test_conversations_api.py](<../services/backend-api/tests/test_conversations_api.py>) — TDD tests for Conversations REST API (M2.2). Tests cover: - Conversations CRUD: list, create, get, update, soft delete - Org scoping (multi-tenant isolation) - Pagination - Folder filtering…
- [test_copilot_actions_contract.py](<../services/backend-api/tests/test_copilot_actions_contract.py>) — Contract test for the AI Copilot "actions" structured_data item. The `actions` item is a new structured_data envelope (alongside the existing `table` and `chart` items formatted in…
- [test_copilot_actions_execute.py](<../services/backend-api/tests/test_copilot_actions_execute.py>) — TDD tests — POST /api/v1/copilot/actions/execute (copilot-suggested-actions, action-registry aspect, PRD M4/M5/M6/M7/M9). The execute route is a normal authenticated REST endpoint —…
- [test_copilot_generators_local.py](<../services/backend-api/tests/test_copilot_generators_local.py>) — Phase 2 TDD — Generators accept base_url / keyless local endpoints. Tests: - SQLGenerator.generate accepts base_url kwarg (signature check) - With base_url + api_key=None: builds…
- [test_copilot_llm_resolution.py](<../services/backend-api/tests/test_copilot_llm_resolution.py>) — Phase 1 TDD — LLM resolution for Copilot generation. Tests for src/services/copilot/llm_resolver.py: - Local org (openai_compatible + base_url, no key) → usable config, is_configured=True -…
- [test_copilot_models.py](<../services/backend-api/tests/test_copilot_models.py>) — TDD tests for AI Copilot (M2.2) database models. Tests cover all 6 new tables: 1. conversation_folders 2. conversations 3. conversation_messages 4. query_templates 5.…
- [test_copilot_proposer_emission.py](<../services/backend-api/tests/test_copilot_proposer_emission.py>) — Phase E TDD — the deterministic proposer hooked into copilot_ws. These tests drive the genuine `copilot_ws._handle_query` path (SQL results fed via a patched `SQLExecutor`, so no real DB)…
- [test_copilot_sql_safety_provider_agnostic.py](<../services/backend-api/tests/test_copilot_sql_safety_provider_agnostic.py>) — Phase 3 TDD — Provider-agnostic SQL safety + honest weak-model UX. Tests: 1. SQL safety validator rejects malicious/unsafe SQL regardless of provider (DROP, cross-org, 5-join, subquery,…
- [test_copilot_streaming_local.py](<../services/backend-api/tests/test_copilot_streaming_local.py>) — Phase 4 TDD — Streaming compatibility for local/OpenAI-compatible endpoints. Tests verify: 1. call_llm_stream with base_url uses AsyncOpenAI with base_url kwarg (local OpenAI-compatible…
- [test_copilot_ws.py](<../services/backend-api/tests/test_copilot_ws.py>) — TDD tests for Copilot WebSocket endpoint (M2.2). Tests cover: - WebSocket connection with valid/invalid JWT - Sending query messages and receiving streamed responses - Stop message cancels…
- [test_copilot_ws_matching.py](<../services/backend-api/tests/test_copilot_ws_matching.py>) — Phase 5 — TDD tests for copilot_ws.py matching-side embedder wiring. Tests that the matching/saving calls in _handle_query pass the resolved embedder through. Does NOT test the generation…
- [test_credential_encryption_sweep.py](<../services/backend-api/tests/test_credential_encryption_sweep.py>) — R8 sweep-guard: no integration route may write a credential column unencrypted. The DB contract (DEV-TRACKING ``oauth-tokens-stored-plaintext`` + ``linear-webhook-secret-plaintext``) is…
- [test_crm_churn_label_columns.py](<../services/backend-api/tests/test_crm_churn_label_columns.py>) — TDD tests for churn_labels_enabled / churn_label_config columns on both CRM integration models (crm-churn-labels, data-model aspect, Phase 3). Model on test_jira_status_sync_migration.py —…
- [test_crm_churn_label_options.py](<../services/backend-api/tests/test_crm_churn_label_options.py>) — Tests for the backend CRM churn-label options seam (org-config-api-and-ui aspect, Phase 1). fetch_renewal_options(provider, integration) -> (options, reason) is the single source of truth…
- [test_crm_integration_common.py](<../services/backend-api/tests/test_crm_integration_common.py>) — Tests for shared CRM integration helpers (Phase 2 of salesforce-connection). - another_crm_active(db, org_id, exclude_provider): symmetric one-CRM guard. - purge_crm_enrichment(db, org_id,…
- [test_crm_provider_generalization.py](<../services/backend-api/tests/test_crm_provider_generalization.py>) — TDD tests for crm-provider-generalization aspect (aspect 1 of 4, salesforce-crm-enrichment feature). Phase 1 (RED characterization): locks the health-score + serializer output for a fixture…
- [test_custom_category_service.py](<../services/backend-api/tests/test_custom_category_service.py>) — Unit tests for src/services/custom_category_service.py. Covers the ``rules_referencing_category`` helper (Phase 2 — delete/rename warning lookup). CRUD behavior itself is…
- [test_customer_analyze_archive.py](<../services/backend-api/tests/test_customer_analyze_archive.py>) — TDD tests for: - POST /api/v1/customers/{email}/analyze — on-demand LLM analysis (202 Accepted) - Archive trigger: feedback delete → is_archived=True when 0 remaining - Unarchive: already…
- [test_customer_health_fields_model.py](<../services/backend-api/tests/test_customer_health_fields_model.py>) — TDD tests — segment-actions PRD, aspect `customer-fields-model`, Phase 2. Coverage: CustomerHealth.tags (JSON list, callable default) and CustomerHealth.cs_owner_user_id / cs_owner…
- [test_customer_health_history_model.py](<../services/backend-api/tests/test_customer_health_history_model.py>) — TDD tests for CustomerHealthHistory model and CustomerHealth model extensions. RED phase: these tests should fail until the model is created.
- [test_customer_profile.py](<../services/backend-api/tests/test_customer_profile.py>) — TDD tests for customer profile, history, feedbacks, and activity endpoints. Tests: GET /api/v1/customers/{email} - Customer profile GET /api/v1/customers/{email}/history - Health score…
- [test_customer_tags.py](<../services/backend-api/tests/test_customer_tags.py>) — Characterization tests for the shared customer tag-apply service. Drives `src.services.customer_tags.apply_tags` directly, pinning exactly the behaviours the existing `POST…
- [test_customer_timeline_endpoint.py](<../services/backend-api/tests/test_customer_timeline_endpoint.py>) — Tests for customer timeline endpoints: Phase 0: Characterization test — locks /activity contract before refactor. Phase 5: Tests for new GET /api/v1/customers/{email}/timeline endpoint.…
- [test_customer_timeline_service.py](<../services/backend-api/tests/test_customer_timeline_service.py>) — Unit tests for customer_timeline_service.build_timeline(). TDD phases 1-4: RED → GREEN → REFACTOR. Phase 1: Port existing 5 sources (feedback_created, status_changed, health_score_changed,…
- [test_customers.py](<../services/backend-api/tests/test_customers.py>) — TDD tests for GET /api/v1/customers/ list endpoint.
- [test_customers_bulk.py](<../services/backend-api/tests/test_customers_bulk.py>) — TDD tests — bulk-actions-api aspect (segment-actions feature), Phase 4. Coverage: - POST /api/v1/customers/bulk/tags: add/remove (union/difference), trim/ dedupe/drop-empty/50-char…
- [test_customers_export.py](<../services/backend-api/tests/test_customers_export.py>) — TDD tests — bulk-actions-api aspect (segment-actions feature), Phase 3. Coverage: - GET /api/v1/customers/export -> 200, text/csv, attachment header. - Filename reflects segment param…
- [test_customers_filter_characterization.py](<../services/backend-api/tests/test_customers_filter_characterization.py>) — Characterization test — segment-actions / bulk-actions-api, Phase 1. Locks the exact output of GET /api/v1/customers/ across a grid of filter param combinations (segment, risk_level,…
- [test_customers_segment.py](<../services/backend-api/tests/test_customers_segment.py>) — TDD tests — segment-api aspect (customer-segments feature). Coverage: Phase 1: `segment` query param + column on GET /api/v1/customers/ Phase 2: `segment` field on the shared Customer 360…
- [test_customers_tags_owner.py](<../services/backend-api/tests/test_customers_tags_owner.py>) — TDD tests — customer-fields-model aspect (segment-actions feature), Phase 3. Coverage: - `tags` + `cs_owner` on CustomerListItem (GET /api/v1/customers/) - `tags` + `cs_owner` on the…
- [test_customers_usage.py](<../services/backend-api/tests/test_customers_usage.py>) — TDD tests for GET /api/v1/customers/{email}/usage — Phase 5. Acceptance criteria (AC6): - Returns rollup snapshot + daily bucketed event time series. - Scoped to the caller's organisation.…
- [test_dashboard.py](<../services/backend-api/tests/test_dashboard.py>) — Tests for dashboard endpoints.
- [test_drop_dead_billing_columns.py](<../services/backend-api/tests/test_drop_dead_billing_columns.py>) — RED → GREEN TDD test for B4: drop dead billing/budget columns. Tests assert that the FOUR columns that have zero live code references outside model declarations have been removed from the…
- [test_email_alert_dispatch.py](<../services/backend-api/tests/test_email_alert_dispatch.py>) — Tests for outbound email alert dispatch. TDD: Tests written BEFORE implementation.
- [test_email_parser.py](<../services/backend-api/tests/test_email_parser.py>) — Tests for email body parser - smart stripping of forwarded email noise.
- [test_email_source.py](<../services/backend-api/tests/test_email_source.py>) — Tests for email feedback source creation and plan gating.
- [test_email_webhooks.py](<../services/backend-api/tests/test_email_webhooks.py>) — Tests for inbound email webhook endpoint (Resend inbound).
- [test_embedding_accuracy_route.py](<../services/backend-api/tests/test_embedding_accuracy_route.py>) — Tests for GET /api/v1/settings/ai/embeddings/accuracy (retrieval-eval-card aspect, M5.4 disclosure layer). Reads the committed eval_retrieval.py results artifact and serves it as a typed,…
- [test_embedding_model_key_integration.py](<../services/backend-api/tests/test_embedding_model_key_integration.py>) — Task 5 -- Integration + regression sweep for model-keyed template matching. Part of local-embedding-quality (M5.4), aspect staleness-model-key (Task 5 of 5, closes the aspect). Prereqs (all…
- [test_embeddings_status.py](<../services/backend-api/tests/test_embeddings_status.py>) — Tests for GET /api/v1/settings/ai/embeddings/status (S3 backend). Covers: - Unconfigured org (no OrgAIConfig / no key) → configured=False, never 500s. - openai_compatible + base_url…
- [test_env_byok_seed.py](<../services/backend-api/tests/test_env_byok_seed.py>) — TDD tests for Q1 env-seed BYOK key convenience (A7 / OSS Self-Hosted Pivot). On startup, if OPENAI_API_KEY / ANTHROPIC_API_KEY / GOOGLE_AI_API_KEY is set in the environment, the operator's…
- [test_eval_embeddings.py](<../services/backend-api/tests/test_eval_embeddings.py>) — Tests for scripts/eval_embeddings.py — the offline retrieval eval harness (retrieval-eval-card aspect, M5.4 disclosure layer, Task 2 of 5). TDD: RED first, then production code in…
- [test_eval_sentiment_script.py](<../services/backend-api/tests/test_eval_sentiment_script.py>) — Tests for scripts/eval_sentiment.py — the offline sentiment eval harness (eval-harness-and-card aspect, M5.1 disclosure layer). Phase 1: multiclass metrics core (pure, no CSV, no…
- [test_event_connection_manager.py](<../services/backend-api/tests/test_event_connection_manager.py>) — TDD tests for EventConnectionManager (realtime events infrastructure). Tests cover: - Per-org connection registration/deregistration - Broadcast to org (with and without actor exclusion) -…
- [test_event_emitter.py](<../services/backend-api/tests/test_event_emitter.py>) — TDD tests for event_emitter helper. Tests cover: - emit_event() wraps broadcast_to_org with correct event structure - Timestamp field in ISO format - Type/event_type fields - Actor…
- [test_events_ws.py](<../services/backend-api/tests/test_events_ws.py>) — TDD tests for /ws/events WebSocket endpoint. Tests cover: - Connection auth (no token, invalid token, valid token) - Heartbeat ping - Idle timeout - Client ping resets idle timer - Event…
- [test_feedback.py](<../services/backend-api/tests/test_feedback.py>) — Tests for feedback endpoints.
- [test_feedback_classifier_seam.py](<../services/backend-api/tests/test_feedback_classifier_seam.py>) — Phase 5 RED: Tests for the classifier-override injection at the backend inline call site (src/api/routes/feedback.py::analyze_single_feedback), the SHADOW-ONLY site (allow_override=False —…
- [test_feedback_sentiment_injection.py](<../services/backend-api/tests/test_feedback_sentiment_injection.py>) — Phase 5 RED: Tests for per-org sentiment provider injection at the backend call site (src/api/routes/feedback.py). Covers: - get_sentiment_analyzer(provider_name) process-level cache…
- [test_feedback_sources_asana.py](<../services/backend-api/tests/test_feedback_sources_asana.py>) — TDD tests for registering `asana` as a selectable feedback-source type. Asana brings its own auth (like Jira/Linear) so it must be: - listed in GET /api/v1/feedback-sources/types with…
- [test_feedback_sources_jira.py](<../services/backend-api/tests/test_feedback_sources_jira.py>) — TDD tests for registering `jira` as a selectable feedback-source type. Jira brings its own auth (like Linear) so it must be: - listed in GET /api/v1/feedback-sources/types with…
- [test_feedback_sources_rbac.py](<../services/backend-api/tests/test_feedback_sources_rbac.py>) — RBAC tests for feedback-sources routes. Per the permission matrix, integration management is Owner/Admin only, so the three WRITE routes (POST /, PATCH /{source_id}, DELETE /{source_id})…
- [test_feedback_sources_zendesk.py](<../services/backend-api/tests/test_feedback_sources_zendesk.py>) — TDD tests for registering `zendesk` as a selectable feedback-source type. Zendesk brings its own auth (like Linear/Jira) so it must be: - listed in GET /api/v1/feedback-sources/types with…
- [test_feedback_urgent_toggle.py](<../services/backend-api/tests/test_feedback_urgent_toggle.py>) — TDD tests for the internal urgent-toggle endpoint — PATCH /api/v1/feedback/{id}/urgent (capture-seam Phase 2). Coverage: - value change -> 200, is_urgent flips, exactly one…
- [test_gdpr.py](<../services/backend-api/tests/test_gdpr.py>) — TDD tests for GDPR Compliance (Track A): - Data export (ZIP) - Deletion request - Cancel deletion - Deactivated user auth blocking - Purge task
- [test_generic_webhook_secret.py](<../services/backend-api/tests/test_generic_webhook_secret.py>) — Tests for the generic inbound webhook per-source secret posture. New webhook sources get a minted `secret_token` at creation (display-once in the create response) and fail closed on…
- [test_google_auth.py](<../services/backend-api/tests/test_google_auth.py>) — Characterization tests for the Google OAuth token verifiers in src/services/google_auth.py. These lock down the `email_verified` enforcement (present-and-False, and entirely-absent both…
- [test_health.py](<../services/backend-api/tests/test_health.py>) — Tests for /health/detailed endpoint. TDD cycles for enhanced health check (Phase 5).
- [test_health_alert_preferences.py](<../services/backend-api/tests/test_health_alert_preferences.py>) — TDD tests for Phase 2: Preferences API extension for customer_health_drop. RED → GREEN → REFACTOR. Tests for GET/PUT /api/v1/notifications/preferences handling of the customer_health_drop…
- [test_health_alerts.py](<../services/backend-api/tests/test_health_alerts.py>) — TDD tests for Customer Sentiment Alerts (M1.3) — Phase 1. Tests for _check_health_drop_alert() in health_score_service.py. RED → GREEN → REFACTOR.
- [test_health_crm_component.py](<../services/backend-api/tests/test_health_crm_component.py>) — TDD tests for crm-health-component aspect. Phase 1 (RED): all tests fail because _compute_crm_component does not exist yet. Phase 4 (GREEN): all tests pass after service implementation.…
- [test_health_score_service.py](<../services/backend-api/tests/test_health_score_service.py>) — TDD tests for health_score_service.py updates: - Confidence level computation (low/medium/high) - History recording (≥2 point change) - Sentiment trend calculation…
- [test_health_usage_component.py](<../services/backend-api/tests/test_health_usage_component.py>) — Phase 1 — RED: Characterization tests for compute_health_score() score stability. Phase 3 — Usage component math tests (wired at weight 0 by default). Phase 4 — Health-weights API accepts 5…
- [test_health_weights.py](<../services/backend-api/tests/test_health_weights.py>) — TDD tests for Feature B2: Configurable health-score weights. Tests cover: - GET /api/v1/categories/health-weights — returns defaults when no OrgAIConfig - PUT…
- [test_health_weights_6fields.py](<../services/backend-api/tests/test_health_weights_6fields.py>) — TDD tests for the 6-weight health-score endpoint extension (crm-health-component). Tests cover: - PUT /api/v1/categories/health-weights with crm as the 6th weight - 6-weight sum=100…
- [test_health_writeback_enqueue.py](<../services/backend-api/tests/test_health_writeback_enqueue.py>) — TDD tests for the CRM writeback enqueue hook in health_score_service.py (writeback-task-trigger aspect, Phase 2). Covers _maybe_enqueue_writeback() directly and through…
- [test_hubspot_churn_label_routes.py](<../services/backend-api/tests/test_hubspot_churn_label_routes.py>) — Tests for HubSpot CRM-sourced churn-label config API routes (org-config-api-and-ui aspect, Phase 2). Routes: PATCH /api/v1/integrations/hubspot/churn-labels — opt-in + renewal set GET…
- [test_hubspot_model.py](<../services/backend-api/tests/test_hubspot_model.py>) — Tests for HubSpotIntegration SQLAlchemy model (Phase 2).
- [test_hubspot_plans.py](<../services/backend-api/tests/test_hubspot_plans.py>) — Tests for HubSpot feature registration in plans.py (Phase 1).
- [test_hubspot_routes.py](<../services/backend-api/tests/test_hubspot_routes.py>) — Tests for HubSpot integration API routes (Phase 3 + Phase 4). Role-matrix pattern mirrors tests/test_health_weights.py. R6 test: POST /connect with missing LLM_ENCRYPTION_KEY returns 422…
- [test_hubspot_symmetric_guard.py](<../services/backend-api/tests/test_hubspot_symmetric_guard.py>) — Tests for the symmetric one-CRM guard + shared purge on hubspot_integration.py (Phase 5 of salesforce-connection aspect). Ensures the collision cannot be created from the HubSpot side…
- [test_hubspot_sync_endpoint.py](<../services/backend-api/tests/test_hubspot_sync_endpoint.py>) — Tests for POST /api/v1/integrations/hubspot/sync (manual trigger endpoint). Phase 5 of hubspot-sync aspect. Mirrors pattern from test_hubspot_routes.py.
- [test_hubspot_writeback_routes.py](<../services/backend-api/tests/test_hubspot_writeback_routes.py>) — Tests for HubSpot writeback config/status API routes (Phase 3 of writeback-config-api). Routes: PATCH /api/v1/integrations/hubspot/writeback — configure opt-in + field GET…
- [test_hubspot_writeback_validation.py](<../services/backend-api/tests/test_hubspot_writeback_validation.py>) — Tests for the backend HubSpot writeback-field validation helper (Phase 2 of writeback-config-api). Mirrors the httpx-Bearer GET pattern used by _validate_hubspot_token in…
- [test_insights.py](<../services/backend-api/tests/test_insights.py>) — Tests for weekly insights API endpoints.
- [test_integration_rbac_sweep.py](<../services/backend-api/tests/test_integration_rbac_sweep.py>) — Repo-wide guard: every integration/config route module must be role-gated. The class of defect this guards against: a route module that deals with integrations, SSO config or API…
- [test_integrations.py](<../services/backend-api/tests/test_integrations.py>) — Tests for integrations endpoints.
- [test_intent_classifier.py](<../services/backend-api/tests/test_intent_classifier.py>) — TDD tests for the Intent Classifier (RED → GREEN → REFACTOR). Tests cover: - Rule-based classification for data, analysis, and general intents - Confidence score thresholds - Ambiguous…
- [test_intercom.py](<../services/backend-api/tests/test_intercom.py>) — Tests for Intercom integration endpoints.
- [test_intercom_backlog_remaining_migration.py](<../services/backend-api/tests/test_intercom_backlog_remaining_migration.py>) — TDD migration tests for intercom-backlog-drain-visibility (db-status-api aspect, R3). Same strategy as test_intercom_writeback_columns_migration.py: build a pre-migration SQLite schema…
- [test_intercom_connection.py](<../services/backend-api/tests/test_intercom_connection.py>) — TDD tests for the Intercom token-paste connection routes. Covers POST /connect, GET /status, DELETE /disconnect. Intercom is the last integration that required OAuth. Every other…
- [test_intercom_webhook_per_org_secret.py](<../services/backend-api/tests/test_intercom_webhook_per_org_secret.py>) — Per-tenant Intercom webhook signature verification. The 1.0.0 changelog recorded this as a limitation that could not be fixed: "A valid signature cannot identify a tenant here.…
- [test_intercom_writeback_columns.py](<../services/backend-api/tests/test_intercom_writeback_columns.py>) — TDD ORM-level tests for intercom-writeback (db-config-model aspect, R1 + R4). Default-deny (spec AC2): a freshly-built IntercomIntegration is writeback_enabled=False with action…
- [test_intercom_writeback_columns_migration.py](<../services/backend-api/tests/test_intercom_writeback_columns_migration.py>) — TDD migration tests for intercom-writeback (db-config-model aspect, R1 + R4). Same strategy as test_org_ai_config_churn_mode_migration.py: build a pre-migration SQLite schema…
- [test_intercom_writeback_config.py](<../services/backend-api/tests/test_intercom_writeback_config.py>) — TDD tests for the Intercom write-back config API routes (intercom-writeback R7 + S1). Covers PATCH /writeback, the GET /status writeback extension, and the POST /writeback/test credential…
- [test_intercom_writeback_dispatch.py](<../services/backend-api/tests/test_intercom_writeback_dispatch.py>) — Seam tests for the intercom write-back dispatch (dispatch-seams aspect, R6). Strict TDD: written FIRST (RED) — no dispatch exists yet. Every backend writer that can move an Intercom-sourced…
- [test_issue_draft.py](<../services/backend-api/tests/test_issue_draft.py>) — TDD tests for backend-draft-service (ai-drafted-issue-content). Phase 1 — service (`src/services/issue_drafter.py`): - Gate via resolve_generation_llm: raises LLMNotConfiguredError, no LLM…
- [test_jira_client.py](<../services/backend-api/tests/test_jira_client.py>) — TDD tests for JiraClient (src/services/jira_client.py) — Phase 2 (backend-connection). No real HTTP. Uses unittest.mock.patch on httpx.Client. Covers: construction, base URL, Basic auth,…
- [test_jira_client_search.py](<../services/backend-api/tests/test_jira_client_search.py>) — TDD tests for JiraClient.search_issues (src/services/jira_client.py) — Phase 3 (backend Jira status-fetch read method, jira-status-sync/inbound-status-sync). No real HTTP. Uses…
- [test_jira_connection.py](<../services/backend-api/tests/test_jira_connection.py>) — TDD tests for the Jira connection routes (backend-connection aspect, Phase 3). Covers: POST /connect, GET /status, DELETE /disconnect, POST /test. Mocks JiraClient at the route module…
- [test_jira_issues.py](<../services/backend-api/tests/test_jira_issues.py>) — TDD tests for the Jira create-issue aspect (backend-create-issue, Phase 4). Covers: text_to_adf helper, GET /projects, GET /issuetypes, POST /issues, GET /issues (list linked). Mocks…
- [test_jira_models.py](<../services/backend-api/tests/test_jira_models.py>) — TDD tests for Jira Cloud integration database models. Tests cover 2 new tables: 1. JiraIntegration — org-wide Jira Cloud connection (email + API token, Basic auth) 2. FeedbackJiraIssue —…
- [test_jira_status_sync_migration.py](<../services/backend-api/tests/test_jira_status_sync_migration.py>) — TDD tests for Phase 1 of Jira inbound status sync: new columns on JiraIntegration (status_sync_enabled, status_mapping) and FeedbackJiraIssue (jira_status, jira_status_category,…
- [test_jira_status_sync_routes.py](<../services/backend-api/tests/test_jira_status_sync_routes.py>) — TDD tests for the Jira inbound status-sync operator control routes (Phase 5). Covers: - GET /api/v1/integrations/jira/status (extended with 4 new fields) - PATCH…
- [test_jira_webhook.py](<../services/backend-api/tests/test_jira_webhook.py>) — TDD tests for the Jira inbound real-time webhook receiver (status-sync-realtime-mapping/jira-webhook aspect, Phase 3). Covers: POST /api/v1/webhooks/jira/inbound. Mirrors…
- [test_jira_webhook_migration.py](<../services/backend-api/tests/test_jira_webhook_migration.py>) — TDD tests for Phase 1 of the jira-webhook aspect (status-sync-realtime-mapping PRD): a new `jira_integrations.webhook_secret` column (Text, nullable, Fernet-encrypted at the route layer —…
- [test_jira_webhook_routes.py](<../services/backend-api/tests/test_jira_webhook_routes.py>) — TDD tests for Phase 2 of the jira-webhook aspect (status-sync-realtime-mapping PRD): the enable/disable/secret-reveal control surface for the inbound real-time Jira webhook. Covers: - POST…
- [test_jwt_secret_required.py](<../services/backend-api/tests/test_jwt_secret_required.py>) — JWT_SECRET must be supplied, never defaulted. `src/api/auth.py` shipped with `os.getenv("JWT_SECRET", "dev-secret-key")`. That literal is in a public repository, `.env.example` had the…
- [test_linear_client.py](<../services/backend-api/tests/test_linear_client.py>) — TDD tests for Linear GraphQL API client. All HTTP calls are mocked — no real Linear API is needed.
- [test_linear_config.py](<../services/backend-api/tests/test_linear_config.py>) — TDD tests for Linear configuration endpoints (Task #6). Tests cover: 1. GET /team-mappings — returns org's category-to-team mappings 2. PUT /team-mappings — replaces all mappings (full…
- [test_linear_integration_rbac.py](<../services/backend-api/tests/test_linear_integration_rbac.py>) — RBAC tests for Linear integration routes. Regression coverage for the P1 gap where member-role users could drive Linear OAuth connect/disconnect, edit config, and create issues. Per the…
- [test_linear_issues.py](<../services/backend-api/tests/test_linear_issues.py>) — Tests for Linear issue creation endpoint. Covers: AI generation, issue creation, duplicate warning, linked issues query, timeline entry.
- [test_linear_models.py](<../services/backend-api/tests/test_linear_models.py>) — TDD tests for Linear Integration database models. Tests cover all 4 new tables: 1. LinearIntegration — org-wide OAuth connection 2. LinearTeamMapping — maps Rereflect categories to Linear…
- [test_linear_oauth.py](<../services/backend-api/tests/test_linear_oauth.py>) — Tests for Linear OAuth flow endpoints. Covers: connect URL generation, callback token exchange, disconnect, status check.
- [test_linear_plan_gating.py](<../services/backend-api/tests/test_linear_plan_gating.py>) — TDD tests for Linear integration plan gating. Covers: 1. plans.py — linear_integration feature present in Pro, Business, Enterprise; absent in Free 2. FEATURE_PLANS — linear_integration…
- [test_linear_webhook.py](<../services/backend-api/tests/test_linear_webhook.py>) — TDD tests for Linear webhook receiver (Task #5). Tests cover: 1. Route exists at POST /api/v1/webhooks/linear/inbound 2. Signature verification (reject missing/invalid, accept valid) 3.…
- [test_linear_webhook_secret_backfill_migration.py](<../services/backend-api/tests/test_linear_webhook_secret_backfill_migration.py>) — TDD migration test for the Linear webhook-secret encryption-at-rest backfill (bug/linear-webhook-secret-plaintext): `linear_integrations.webhook_secret` (String(255), plaintext) rows are…
- [test_main.py](<../services/backend-api/tests/test_main.py>) — Tests for main API endpoints.
- [test_mapping_embedding_model_migration.py](<../services/backend-api/tests/test_mapping_embedding_model_migration.py>) — TDD migration tests for the staleness-model-key aspect (local-embedding-quality, M5.4). Adds embedding_model (String(100), nullable) to query_template_mappings and reworks the covering…
- [test_mapping_provider_columns.py](<../services/backend-api/tests/test_mapping_provider_columns.py>) — Phase 1 — TDD (RED → GREEN) tests for embedding_provider + embedding_dimension columns on QueryTemplateMapping, and the length-based backfill rule. Tests: - Model has the two new columns as…
- [test_migrations_segment_actions.py](<../services/backend-api/tests/test_migrations_segment_actions.py>) — TDD migration tests — segment-actions PRD, aspect `customer-fields-model`. Adds `tags` (JSON) and `cs_owner_user_id` (FK -> users.id, ON DELETE SET NULL) to `customer_health_scores`, plus…
- [test_multi_model_api.py](<../services/backend-api/tests/test_multi_model_api.py>) — Tests for M2.1 Multi-Model Support API endpoints. Covers: - Encryption utility (encrypt/decrypt round-trip, key hint) - Updated GET/PATCH /api/v1/settings/ai (expanded schema) - API Key…
- [test_mutation_route_rbac_sweep.py](<../services/backend-api/tests/test_mutation_route_rbac_sweep.py>) — Per-route guard: every mutation route is role-gated, or deliberately listed. `test_integration_rbac_sweep.py` works per *module* ("does the source contain a role marker anywhere"), which…
- [test_notifications.py](<../services/backend-api/tests/test_notifications.py>) — Tests for notification and alert preference endpoints. TDD: Written BEFORE implementation (Phase 6→3).
- [test_oauth_state.py](<../services/backend-api/tests/test_oauth_state.py>) — Tests for the stateless OAuth `state` signing helpers (src/services/oauth_state.py). Shared by the Slack, Intercom and Linear OAuth flows. Fail-closed contract: any invalid/forged/expired…
- [test_oauth_token_backfill_migration.py](<../services/backend-api/tests/test_oauth_token_backfill_migration.py>) — TDD migration test for the oauth-tokens-encryption-at-rest backfill (bug/oauth-tokens-stored-plaintext): `integrations.oauth_access_token` (Text, nullable) plaintext rows are encrypted in…
- [test_oidc_config.py](<../services/backend-api/tests/test_oidc_config.py>) — TDD tests for the OidcConfig database model and admin CRUD route. Mirrors test_zendesk_models.py's TestZendeskIntegrationModel — one row per org, Fernet-encrypted client_secret (encryption…
- [test_oidc_login.py](<../services/backend-api/tests/test_oidc_login.py>) — TDD tests for the `oidc-login-flow` aspect of `oidc-sso`. Task 1: `users.oidc_sub` column (additive, unique, nullable) that OIDC login will populate on JIT-provision/link. Task 3: `GET…
- [test_oidc_provider.py](<../services/backend-api/tests/test_oidc_provider.py>) — Unit tests for `src/services/oidc_provider.py`. The IdP is entirely mocked over httpx via a custom `httpx.BaseTransport` (no live network). ID tokens are signed in-test with a…
- [test_org_ai_config_autopromote_hold.py](<../services/backend-api/tests/test_org_ai_config_autopromote_hold.py>) — Data-model test for the per-type auto-promotion hold flags on OrgAIConfig (classifier-model-versioning-rollback, aspect data-model-and-migration / PRD M1). A held (org, classifier_type) is…
- [test_org_ai_config_category_classifier_mode.py](<../services/backend-api/tests/test_org_ai_config_category_classifier_mode.py>) — TDD tests for per-org-category-classifier (M5.2 v2) — OrgAIConfig.category_classifier_mode. 'off' / 'shadow' / 'auto'. NULL/unrecognized will be treated as 'off' by the predict-seam…
- [test_org_ai_config_category_mode_migration.py](<../services/backend-api/tests/test_org_ai_config_category_mode_migration.py>) — TDD migration tests for per-org-category-classifier (M5.2 v2) — data-and-config aspect. Same strategy as test_org_classifier_migration.py: build a pre-migration SQLite schema (org_ai_config…
- [test_org_ai_config_churn_mode.py](<../services/backend-api/tests/test_org_ai_config_churn_mode.py>) — TDD tests for per-org-churn-model (churn-predict-seam-resolver, data layer) — OrgAIConfig.churn_classifier_mode + churn_autopromote_hold. churn_classifier_mode: 'off' / 'shadow' / 'auto'.…
- [test_org_ai_config_churn_mode_migration.py](<../services/backend-api/tests/test_org_ai_config_churn_mode_migration.py>) — TDD migration tests for per-org-churn-model (churn-predict-seam-resolver, data-and-config aspect). Same strategy as test_org_ai_config_urgency_mode_migration.py: build a pre-migration…
- [test_org_ai_config_classifier_mode.py](<../services/backend-api/tests/test_org_ai_config_classifier_mode.py>) — TDD tests for M5.2 per-org-corrections-classifier — OrgAIConfig.classifier_mode. 'off' / 'shadow' / 'auto'. NULL/unrecognized treated as 'off' by resolve_classifier (aspect D) — defense in…
- [test_org_ai_config_urgency_classifier_mode.py](<../services/backend-api/tests/test_org_ai_config_urgency_classifier_mode.py>) — TDD tests for per-org-urgency-classifier (urgency-classifier-head, data-and-config aspect) — OrgAIConfig.urgency_classifier_mode. 'off' / 'shadow' / 'auto'. Independent of `classifier_mode`…
- [test_org_ai_config_urgency_mode_migration.py](<../services/backend-api/tests/test_org_ai_config_urgency_mode_migration.py>) — TDD migration tests for per-org-urgency-classifier (urgency-classifier-head, data-and-config aspect). Same strategy as test_org_ai_config_category_mode_migration.py: build a pre-migration…
- [test_org_classifier_migration.py](<../services/backend-api/tests/test_org_classifier_migration.py>) — TDD migration tests for M5.2 per-org-corrections-classifier — data-layer aspect. Strategy -------- We cannot run the full Alembic chain against SQLite (existing migrations use…
- [test_org_classifier_models.py](<../services/backend-api/tests/test_org_classifier_models.py>) — TDD tests for M5.2 per-org-corrections-classifier — data-layer aspect. OrgClassifierModel + OrgClassifierEvalRun mirror the proven ChurnCalibrationModel / ChurnBacktestRun conventions: -…
- [test_organizations.py](<../services/backend-api/tests/test_organizations.py>) — Tests for organization endpoints.
- [test_oss_b4_drop_stripe_columns.py](<../services/backend-api/tests/test_oss_b4_drop_stripe_columns.py>) — TDD test for B4 second wave: drop remaining dead Stripe/billing columns. RED → must fail before changes. GREEN → must pass after migration, model removals, and org_resolver cleanup. Columns…
- [test_oss_pivot.py](<../services/backend-api/tests/test_oss_pivot.py>) — Tests for OSS Self-Hosted Pivot (Workstreams A4, A6, A7, B1, B2, B3). TDD Red → Green for every new behavior: - B1: SELF_HOSTED flag short-circuits all plan gates (all features unlocked,…
- [test_oss_stripe_cleanup.py](<../services/backend-api/tests/test_oss_stripe_cleanup.py>) — TDD tests for OSS Stripe cleanup (B3 + B4 code references). These tests assert the *target* state after cleanup — they must FAIL (RED) before any production changes are made, then PASS…
- [test_outreach_bulk.py](<../services/backend-api/tests/test_outreach_bulk.py>) — TDD tests — bulk-campaign-api aspect, Phase 2 (route) + Phase 3 (list/retry). Route contract (consumed by bulk-campaign-ui): POST /api/v1/customers/bulk/outreach (admin/owner) body {cohort:…
- [test_outreach_draft.py](<../services/backend-api/tests/test_outreach_draft.py>) — TDD tests — bulk-campaign-api aspect, Phase 4 (outreach draft endpoint). Service (`src/services/outreach_drafter.py`), mirroring test_issue_draft.py: - Gate via resolve_generation_llm: not…
- [test_outreach_migration.py](<../services/backend-api/tests/test_outreach_migration.py>) — TDD migration test for the outreach-core aspect: `outreach_opt_out` on `customer_health_scores` + the `outreach_campaigns` and `outreach_campaign_recipients` tables. Strategy --------…
- [test_outreach_templates.py](<../services/backend-api/tests/test_outreach_templates.py>) — Tests for the outreach template registry + GET /api/v1/outreach/templates. Strict TDD: written FIRST (RED) before the registry/endpoint implementation. Also pins the additive…
- [test_outreach_unsubscribe.py](<../services/backend-api/tests/test_outreach_unsubscribe.py>) — Tests for outreach unsubscribe tokens + endpoint + customer opt-out PATCH (outreach-core aspect, Phase 4). Strict TDD: written FIRST (RED) before the implementations.
- [test_playbook_seeder.py](<../services/backend-api/tests/test_playbook_seeder.py>) — Tests for playbook_seeder.py (M4.1 Phase 5.1) — strict TDD.
- [test_playbook_task_model.py](<../services/backend-api/tests/test_playbook_task_model.py>) — TDD tests — playbook-action-types PRD, aspect `playbook-tasks`, Phase 1. Coverage (AC7, model half): PlaybookTask columns exist with the right types/nullability, description is required,…
- [test_playbooks_api.py](<../services/backend-api/tests/test_playbooks_api.py>) — Tests for Churn Playbook API (M4.1 Phase 5.1) — strict TDD (RED first). Covers: auth/gating, CRUD, run, run-batch, executions list.
- [test_playbooks_run_batch.py](<../services/backend-api/tests/test_playbooks_run_batch.py>) — Characterization + extension tests — playbook-cohort-run aspect (segment-actions feature), M4.1 run-batch extension. Phase 1 pins the EXISTING `POST /playbooks/{id}/run-batch` behavior…
- [test_preferences.py](<../services/backend-api/tests/test_preferences.py>) — Tests for user preferences endpoints.
- [test_public_api.py](<../services/backend-api/tests/test_public_api.py>) — Tests for Feature C — Public REST API (PRD §6). TDD: RED → GREEN → REFACTOR. Coverage: - API key management (create / list / revoke) via JWT auth - verify_api_key dependency (valid,…
- [test_public_api_bulk_feedback.py](<../services/backend-api/tests/test_public_api_bulk_feedback.py>) — Tests for the public bulk-write endpoint — POST /api/public/v1/feedback/bulk. TDD: RED -> GREEN -> REFACTOR. See docs/planning/public-api-crud-v3/bulk-feedback-write/plan_20260714.md for…
- [test_public_api_categories.py](<../services/backend-api/tests/test_public_api_categories.py>) — Tests for the public custom-categories CRUD — /api/public/v1/categories. Mirrors the internal /api/v1/categories/custom CRUD (see tests/test_categories.py and…
- [test_public_api_customer360.py](<../services/backend-api/tests/test_public_api_customer360.py>) — TDD tests — public-api-customer360 aspect. Coverage: Phase 1: Shared Customer 360 profile serializer Phase 2: GET /api/public/v1/customers/{email} — full profile Phase 3: GET…
- [test_public_api_write.py](<../services/backend-api/tests/test_public_api_write.py>) — Tests for the public write endpoint — PATCH /api/public/v1/feedback/{id}. TDD: RED → GREEN → REFACTOR. Coverage: - write scope required (read/ingest keys → 403) - workflow_status change:…
- [test_rbac_analyze_batch.py](<../services/backend-api/tests/test_rbac_analyze_batch.py>) — RBAC for POST /analyze/batch (org-wide LLM analysis); POST /analyze/ stays member-open.
- [test_rbac_churn_events.py](<../services/backend-api/tests/test_rbac_churn_events.py>) — RBAC for churn-event mutations (mutation-route-rbac, backend-gating).
- [test_rbac_feedback_destructive.py](<../services/backend-api/tests/test_rbac_feedback_destructive.py>) — RBAC for destructive feedback routes; member-open feedback routes stay open.
- [test_rbac_playbooks.py](<../services/backend-api/tests/test_rbac_playbooks.py>) — RBAC for playbook mutations: admin/owner only (mutation-route-rbac, backend-gating).
- [test_rbac_workflow_config.py](<../services/backend-api/tests/test_rbac_workflow_config.py>) — RBAC for assignment-rule CRUD and auto-assignment settings (mutation-route-rbac).
- [test_report_generator.py](<../services/backend-api/tests/test_report_generator.py>) — TDD tests for the ReportGenerator service (M2.4). Covers: - ReportGenerator instantiation - Data query methods for each report type - Section building with expected keys - Report type…
- [test_report_schedules.py](<../services/backend-api/tests/test_report_schedules.py>) — TDD tests for Scheduled AI Reports — ReportSchedule model + CRUD API. Covers: - ReportSchedule model fields, defaults and registration - CRUD API endpoints (GET list, GET by id, POST…
- [test_report_ws.py](<../services/backend-api/tests/test_report_ws.py>) — TDD tests for On-Demand AI Reports — Phase 2 (WebSocket Integration, M2.4). Tests cover: 1. Report intent routes to the report pipeline (not the regular LLM path) 2. Report is saved to the…
- [test_reports.py](<../services/backend-api/tests/test_reports.py>) — TDD tests for On-Demand AI Reports — Phase 1 (M2.4). Covers: - Report model creation and persistence - Report CRUD API endpoints (GET list, GET by id, DELETE) - Plan gating: ai_reports…
- [test_response_formatter.py](<../services/backend-api/tests/test_response_formatter.py>) — TDD tests for Copilot Response Formatter (M2.2 Task #7). Tests cover: - Table formatting from SQL results - Chart type auto-detection - Chart data format (Recharts-compatible) - Deep link…
- [test_response_generation.py](<../services/backend-api/tests/test_response_generation.py>) — Tests for AI response generation endpoint. TDD order: 1. GET /feedback/{id}/responses — list responses (empty then with records) 2. POST /feedback/{id}/responses/generate — AI generation a.…
- [test_response_send.py](<../services/backend-api/tests/test_response_send.py>) — Tests for POST /api/v1/feedback/{id}/responses/send endpoint. TDD order: 1. Clipboard channel — saves status='copied', returns success=True 2. Send via Slack — dispatches to…
- [test_response_settings.py](<../services/backend-api/tests/test_response_settings.py>) — Tests for Response Settings endpoints. TDD order: 1. GET /response-settings — returns org settings 2. PUT /response-settings — updates settings (admin/owner) 3. GET /response-settings/usage…
- [test_response_templates.py](<../services/backend-api/tests/test_response_templates.py>) — Tests for Response Templates CRUD and suggestion algorithm. TDD order: 1. List system templates returns 8 defaults 2. Create custom template 3. Get single template by ID 4. Update custom…
- [test_route_events.py](<../services/backend-api/tests/test_route_events.py>) — TDD tests for event emissions from route handlers. RED phase: These tests are written BEFORE the implementation. They verify that emit_event() is called with the correct arguments after DB…
- [test_salesforce_churn_label_routes.py](<../services/backend-api/tests/test_salesforce_churn_label_routes.py>) — Tests for Salesforce CRM-sourced churn-label config API routes (org-config-api-and-ui aspect, Phase 3 — symmetric with tests/test_hubspot_churn_label_routes.py, spec AC12). Routes: PATCH…
- [test_salesforce_model.py](<../services/backend-api/tests/test_salesforce_model.py>) — Tests for SalesforceIntegration SQLAlchemy model (Phase 1). Mirrors tests/test_hubspot_model.py.
- [test_salesforce_oauth_lifecycle.py](<../services/backend-api/tests/test_salesforce_oauth_lifecycle.py>) — Tests for Salesforce OAuth callback + test + disconnect + manual sync (Phase 4 of salesforce-connection aspect). Mocks ALL Salesforce HTTP — no live org.
- [test_salesforce_routes.py](<../services/backend-api/tests/test_salesforce_routes.py>) — Tests for Salesforce integration API routes (salesforce-connection aspect). Role-matrix pattern mirrors tests/test_hubspot_routes.py. Mock ALL Salesforce HTTP — no live org.
- [test_salesforce_writeback_routes.py](<../services/backend-api/tests/test_salesforce_writeback_routes.py>) — Tests for Salesforce writeback config/status API routes (writeback-config-api aspect of salesforce-crm-writeback). Routes: PATCH /api/v1/integrations/salesforce/writeback — configure opt-in…
- [test_salesforce_writeback_validation.py](<../services/backend-api/tests/test_salesforce_writeback_validation.py>) — Tests for the backend Salesforce writeback-field validation helper (salesforce-write-client aspect, Phase 2). Mirrors test_hubspot_writeback_validation.py's structure and (bool, reason)…
- [test_saml_config.py](<../services/backend-api/tests/test_saml_config.py>) — TDD tests for the SamlConfig database model, admin CRUD route, the public SAML status probe, and the cross-provider single-SSO guard. Mirrors test_oidc_config.py exactly in shape/security…
- [test_saml_deps.py](<../services/backend-api/tests/test_saml_deps.py>) — Dependency smoke test for the SAML 2.0 SSO feature (saml-sso, slice 1 / deps-and-docker). This is the RED->GREEN anchor for the whole feature: python3-saml pulls the native `xmlsec`…
- [test_saml_login.py](<../services/backend-api/tests/test_saml_login.py>) — TDD tests for the `login-routes-and-identity` aspect of `saml-sso` (aspect 4). Wires the SP-initiated SAML flow into HTTP routes on `src/api/routes/auth.py`: GET /api/v1/auth/saml/login ->…
- [test_saml_provider.py](<../services/backend-api/tests/test_saml_provider.py>) — Unit tests for `src/services/saml_provider.py`. Real crypto runs here (xmlsec + python3-saml): every signed-fixture test actually signs and validates XML — nothing is skipped. Fixtures are…
- [test_saml_replay.py](<../services/backend-api/tests/test_saml_replay.py>) — Unit tests for `src/services/saml_replay.py` — the DB-backed InResponseTo / replay store (aspect provider-and-replay-store, gap 1 state machine). No migration needed: the `db` fixture…
- [test_segment_on_ingest.py](<../services/backend-api/tests/test_segment_on_ingest.py>) — TDD tests for Phase 3 (segment-engine): on-ingest segment assignment. `update_customer_health` must compute and persist `CustomerHealth.segment` via `health_score_service.resolve_segment`,…
- [test_segment_service.py](<../services/backend-api/tests/test_segment_service.py>) — TDD tests for classify_segment() — customer-segments Phase 1 (segment-engine). RED -> GREEN workflow: these tests were written BEFORE the implementation in src/services/segment_service.py.…
- [test_sentiment_accuracy_route.py](<../services/backend-api/tests/test_sentiment_accuracy_route.py>) — Tests for GET /api/v1/settings/ai/sentiment/accuracy (eval-harness-and-card aspect, Phase 6). Reads the committed eval_sentiment.py results artifact and serves it as a typed, never-raising…
- [test_sentiment_resolver.py](<../services/backend-api/tests/test_sentiment_resolver.py>) — Phase 1 RED: Tests for resolve_sentiment_provider (backend-api). Degrade matrix: 1. sentiment_provider is None/unset -> None (caller falls back to "vader") 2. No OrgAIConfig row at all ->…
- [test_sentiment_status.py](<../services/backend-api/tests/test_sentiment_status.py>) — Phase 3 RED: Tests for GET /api/v1/settings/ai/sentiment/status. Never raises to the caller — mirrors GET /embeddings/status. Covers all 4 states: no config, explicit vader, transformer…
- [test_sentry.py](<../services/backend-api/tests/test_sentry.py>) — Tests for Sentry integration in the FastAPI backend. Sentry is opt-in: a self-hosted install must send nothing anywhere unless the operator sets SENTRY_DSN. These tests exercise the real…
- [test_shadow_repair_migration.py](<../services/backend-api/tests/test_shadow_repair_migration.py>) — TDD migration test for Phase 4 of the worker-trigger-mirror aspect (automations-delivery-integrity): the repaired trigger types (`feedback_category_match`, `sentiment_pattern`) are moved…
- [test_slack_webhook.py](<../services/backend-api/tests/test_slack_webhook.py>) — Tests for the Slack Events API webhook signature verification. Slack ingestion has live production traffic (unlike Intercom, whose ingestion never worked because of a separate…
- [test_sql_executor.py](<../services/backend-api/tests/test_sql_executor.py>) — TDD tests for SQL Executor (RED → GREEN → REFACTOR). Tests cover: - Basic query execution - 5-second timeout enforcement - Parameterized query execution (SQL injection prevention) -…
- [test_sql_validator.py](<../services/backend-api/tests/test_sql_validator.py>) — TDD tests for SQL Validator — safety guardrails (RED → GREEN → REFACTOR). Every guardrail from PRD §5.3 is tested individually: - Read-only enforcement - Schema whitelist - Join limit - No…
- [test_ssrf.py](<../services/backend-api/tests/test_ssrf.py>) — Unit tests for the shared SSRF gate (`src/utils/ssrf.py`). `socket.getaddrinfo` is mocked in every test to avoid real DNS lookups; we assert purely on how resolved-IP classes…
- [test_startup_seeding.py](<../services/backend-api/tests/test_startup_seeding.py>) — Phase 4 — TDD tests for provider-aware system-template seeding in lifespan. Tests: - seed_copilot_system_templates() calls TemplateSaver.seed_system_templates with the resolved embedder…
- [test_startup_webhook_secret_warnings.py](<../services/backend-api/tests/test_startup_webhook_secret_warnings.py>) — Boot-time fail-closed notice for unconfigured Slack / email webhook secrets. source_webhooks.verify_slack_signature and email_webhooks._verify_webhook_signature fail closed: when their…
- [test_status_sync_core.py](<../services/backend-api/tests/test_status_sync_core.py>) — Pure unit tests for src.services.status_sync_core. No I/O, no DB, no FastAPI. This module is later copied verbatim into the worker service, so these tests must never import anything beyond…
- [test_team.py](<../services/backend-api/tests/test_team.py>) — Tests for Team Management RBAC feature. TDD RED Phase - These tests are designed to FAIL because the production code doesn't exist yet. They define the expected behavior for: 1. Role field…
- [test_teams_integration.py](<../services/backend-api/tests/test_teams_integration.py>) — Tests for the Microsoft Teams integration (backend connector). Teams is webhook-only, like Discord: the webhook URL carries its own credential, so there is no OAuth flow. These tests pin…
- [test_template_matcher.py](<../services/backend-api/tests/test_template_matcher.py>) — TDD tests for the Template Matcher (RED → GREEN → REFACTOR). Updated for template-matching-local: embedder injection, provider/dim skip-filter, no hardcoded OpenAI client or _EMBEDDING_DIMS…
- [test_template_saver.py](<../services/backend-api/tests/test_template_saver.py>) — TDD tests for the Template Saver (RED → GREEN → REFACTOR). Updated for template-matching-local: embedder injection, provider/dim persistence on every mapping (ORM + raw-SQL fallback), and…
- [test_usage_churn_label_config_migration.py](<../services/backend-api/tests/test_usage_churn_label_config_migration.py>) — TDD migration test for the config-and-migration aspect of usage-decline-churn-labels: `org_ai_config.usage_churn_labels_mode` (String(20), nullable, server_default 'off') and…
- [test_usage_churn_label_config_model.py](<../services/backend-api/tests/test_usage_churn_label_config_model.py>) — TDD tests for usage-decline-churn-labels (config-and-migration aspect) — OrgAIConfig.usage_churn_labels_mode + OrgAIConfig.usage_churn_label_config. 'off' / 'shadow' / 'active' — NOT the…
- [test_usage_decline_labels_core.py](<../services/backend-api/tests/test_usage_decline_labels_core.py>) — TDD tests for the usage-decline-churn-labels detector core (detector-core aspect) — strict TDD (RED first). Pure logic only: no DB, no fixtures, no mocks. Run: cd services/backend-api &&…
- [test_usage_history_migration.py](<../services/backend-api/tests/test_usage_history_migration.py>) — TDD migration test for the usage-history-snapshot aspect: ``customer_usage_history`` table (create + drop). Mirrors tests/test_active_days_14d_migration.py's approach: 1. Build a…
- [test_usage_history_model.py](<../services/backend-api/tests/test_usage_history_model.py>) — TDD tests for the CustomerUsageHistory model — usage-history-snapshot aspect. RED phase: these tests should fail until src/models/customer_usage_history.py exists and is exported from…
- [test_usage_history_trend_columns_migration.py](<../services/backend-api/tests/test_usage_history_trend_columns_migration.py>) — TDD migration test for the snapshot-trend-columns aspect (usage-trend-automation-trigger, M3): `customer_usage_history.usage_trend_state` (String(30), nullable, NO server_default) and…
- [test_usage_ingest.py](<../services/backend-api/tests/test_usage_ingest.py>) — Tests for ingestion-receiver — POST /api/v1/webhooks/usage. TDD: RED → GREEN per phase. Coverage (spec acceptance criteria 1-7): 1. Valid mixed batch → 202, correct accepted/skipped counts,…
- [test_usage_score.py](<../services/backend-api/tests/test_usage_score.py>) — TDD tests for compute_usage_score() — Phase 2. RED → GREEN workflow: these tests were written BEFORE the implementation. Acceptance criteria: AC3: recent+frequent+broad usage → high (>70)…
- [test_usage_score_service_sync.py](<../services/backend-api/tests/test_usage_score_service_sync.py>) — AC 15 (trend-detection-and-health): usage_score_service.py must stay byte-identical between backend-api and worker-service — both files carry the "DUPLICATED: keep in sync" header at the…
- [test_usage_trend_churn_boundary.py](<../services/backend-api/tests/test_usage_trend_churn_boundary.py>) — AC 10 — the single most important test in the trend-detection-and-health aspect: the executable form of the calibration boundary. `churn_probability` =…
- [test_usage_trend_core.py](<../services/backend-api/tests/test_usage_trend_core.py>) — Phase A — RED: pure trend core (no I/O). Covers the two pure functions plus the lookback-selection helper added to usage_score_service.py for the trend-detection-and-health aspect: -…
- [test_usage_trend_fields_migration.py](<../services/backend-api/tests/test_usage_trend_fields_migration.py>) — TDD migration test for Phase C of the trend-detection-and-health aspect: `customer_usage.usage_trend_state` (String(30), NOT NULL, server_default 'insufficient_history') and…
- [test_usage_trend_severity.py](<../services/backend-api/tests/test_usage_trend_severity.py>) — TDD tests for the usage-trend severity ordering helper (trigger-registration, Phase 1) — strict TDD (RED first). Run: cd services/backend-api && ./venv/bin/pytest…
- [test_webhook_dispatcher.py](<../services/backend-api/tests/test_webhook_dispatcher.py>) — TDD tests for webhook_dispatcher service (M3.1 Phase 2). Tests are written first; the implementation must make them pass.
- [test_webhook_hardening.py](<../services/backend-api/tests/test_webhook_hardening.py>) — Two webhook hardening fixes carried over from the auth/tenancy sweep. `zendesk-replay-window` and `generic-webhook-persists-headers`, both filed in DEV-TRACKING under "Follow-ups opened by…
- [test_webhook_verifiers_fail_closed.py](<../services/backend-api/tests/test_webhook_verifiers_fail_closed.py>) — Repo-wide guard: every inbound-webhook signature verifier must fail CLOSED. A verifier that returns True when its secret is unset accepts arbitrary unsigned payloads from anyone who knows…
- [test_webhooks.py](<../services/backend-api/tests/test_webhooks.py>) — Tests for custom webhook endpoints (M3.1). TDD approach: each test is written first, then the implementation makes it pass.
- [test_winback_notification.py](<../services/backend-api/tests/test_winback_notification.py>) — Tests for winback_suggested notification type — Phase 3.2 (M4.1). Verifies: 15. winback_suggested is a valid notification type (can be stored and queried) 16. POST /recover clears…
- [test_workflow_status.py](<../services/backend-api/tests/test_workflow_status.py>) — Characterization tests for POST /api/v1/workflow/status. These lock the CURRENT behavior of the internal bulk status-change route so that the upcoming service-helper extraction…
- [test_zendesk_client.py](<../services/backend-api/tests/test_zendesk_client.py>) — TDD tests for ZendeskClient (src/services/zendesk_client.py) — Phase 2 (backend-connection). No real HTTP. Uses unittest.mock.patch on httpx.Client. Covers: construction, base URL, Basic…
- [test_zendesk_connection.py](<../services/backend-api/tests/test_zendesk_connection.py>) — TDD tests for the Zendesk connection routes (backend-connection aspect, Phase 3). Covers: POST /connect, GET /status, DELETE /disconnect, POST /test. Mocks ZendeskClient at the route module…
- [test_zendesk_models.py](<../services/backend-api/tests/test_zendesk_models.py>) — TDD tests for the ZendeskIntegration database model. Mirrors test_jira_models.py's TestJiraIntegrationModel, minus the link-table class — there is no FeedbackZendeskIssue equivalent (this…
- [test_zendesk_status_core.py](<../services/backend-api/tests/test_zendesk_status_core.py>) — Pure unit tests for src.services.zendesk_status_core. No I/O, no DB, no FastAPI. This module is later copied verbatim into the worker service, so these tests must never import anything…
- [test_zendesk_status_reconcile.py](<../services/backend-api/tests/test_zendesk_status_reconcile.py>) — TDD tests for src.services.zendesk_status_reconcile (webhook-realtime aspect of zendesk-status-sync) — the backend-side mirror of the worker's `reconcile_feedback`…
- [test_zendesk_status_sync_routes.py](<../services/backend-api/tests/test_zendesk_status_sync_routes.py>) — TDD tests for the Zendesk inbound status-sync operator control routes. Covers: - GET /api/v1/integrations/zendesk/status (extended with 4 new fields) - PATCH…
- [test_zendesk_sync_endpoint.py](<../services/backend-api/tests/test_zendesk_sync_endpoint.py>) — Tests for POST /api/v1/integrations/zendesk/sync (manual "Sync now" trigger). Phase 6 (should-have) of ingestion-pull aspect. Mirrors tests/test_hubspot_sync_endpoint.py — but per plan D7…
- [test_zendesk_webhook.py](<../services/backend-api/tests/test_zendesk_webhook.py>) — TDD tests for the Zendesk webhook entry point (ingestion-webhook aspect). Covers: POST /api/v1/webhooks/zendesk/events. Mirrors TestIntercomWebhook in test_intercom.py; seeds…

## `services/backend-api/tests/embeddings`

[Directory guide](<../services/backend-api/tests/embeddings/directory.md>)

- [__init__.py](<../services/backend-api/tests/embeddings/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [test_base.py](<../services/backend-api/tests/embeddings/test_base.py>) — Phase 1 RED: Tests for the EmbeddingProvider abstract base interface. Asserts: - EmbeddingProvider is abstract (cannot be instantiated directly) - embed(text: str) -> list[float] is…
- [test_factory.py](<../services/backend-api/tests/embeddings/test_factory.py>) — Phase 4 RED: Tests for EmbeddingProviderFactory. - create("openai", api_key="k", model=None) → OpenAIEmbeddingProvider - create("openai_compatible", base_url=..., model="nomic-embed-text")…
- [test_google_provider.py](<../services/backend-api/tests/embeddings/test_google_provider.py>) — Phase 3 RED: Tests for GoogleEmbeddingProvider. AC3: google provider normalizes its response to list[float]. - Mock google.generativeai client; assert embed() returns list[float] -…
- [test_local_provider.py](<../services/backend-api/tests/embeddings/test_local_provider.py>) — Aspect 2 / Task 1 RED: Tests for LocalEmbeddingProvider. In-process, CPU, air-gappable embedding provider using sentence-transformers. Mirrors the M5.1 TransformerSentimentProvider…
- [test_openai_compatible_provider.py](<../services/backend-api/tests/embeddings/test_openai_compatible_provider.py>) — Phase 2 RED: Tests for OpenAICompatibleEmbeddingProvider. AC2: openai_compatible provider calls configured base_url with no api_key, returns the model's native dims (mock a 768-dim…
- [test_openai_provider.py](<../services/backend-api/tests/embeddings/test_openai_provider.py>) — Phase 2 RED: Tests for OpenAIEmbeddingProvider. AC1: openai provider returns a 1536-dim vector (mocked client) for given text. - Mock openai.OpenAI client - Assert embed("hi") returns a…
- [test_resolver.py](<../services/backend-api/tests/embeddings/test_resolver.py>) — Phase 5 RED: Tests for resolve_embedding_provider. Degrade matrix (the contract the whole feature leans on): 1. Org with default_provider="openai" + valid BYOK key → ResolvedEmbedder with…
- [test_resolver_model.py](<../services/backend-api/tests/embeddings/test_resolver_model.py>) — RED: Tests for the effective embedding model threaded through ResolvedEmbedder. Part of feature local-embedding-quality (M5.4), aspect staleness-model-key (Task 1). Contract: -…

## `services/backend-api/tests/fixtures`

[Directory guide](<../services/backend-api/tests/fixtures/directory.md>)

- [copilot_actions_item.json](<../services/backend-api/tests/fixtures/copilot_actions_item.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

## `services/backend-api/tests/fixtures/embedding_eval`

[Directory guide](<../services/backend-api/tests/fixtures/embedding_eval/directory.md>)

- [queries.jsonl](<../services/backend-api/tests/fixtures/embedding_eval/queries.jsonl>) — Static/configuration artifact; inspect its consumer.
- [queries_tiny.jsonl](<../services/backend-api/tests/fixtures/embedding_eval/queries_tiny.jsonl>) — Static/configuration artifact; inspect its consumer.
- [test_fixtures_valid.py](<../services/backend-api/tests/fixtures/embedding_eval/test_fixtures_valid.py>) — Validation tests for the held-out retrieval-eval fixtures (local-embedding-quality, aspect retrieval-eval-card, Task 1). These fixtures back an eval of embedding retrieval quality: given a…

## `services/backend-api/tests/fixtures/sentiment_eval`

[Directory guide](<../services/backend-api/tests/fixtures/sentiment_eval/directory.md>)

- [in_domain_eval.csv](<../services/backend-api/tests/fixtures/sentiment_eval/in_domain_eval.csv>) — Static/configuration artifact; inspect its consumer.
- [public_eval.csv](<../services/backend-api/tests/fixtures/sentiment_eval/public_eval.csv>) — Static/configuration artifact; inspect its consumer.
- [tiny_fixture.csv](<../services/backend-api/tests/fixtures/sentiment_eval/tiny_fixture.csv>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web`

[Directory guide](<../services/frontend-web/directory.md>)

- [.env.example](<../services/frontend-web/.env.example>) — Static/configuration artifact; inspect its consumer.
- [Dockerfile](<../services/frontend-web/Dockerfile>) — Static/configuration artifact; inspect its consumer.
- [components.json](<../services/frontend-web/components.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [eslint.config.mjs](<../services/frontend-web/eslint.config.mjs>) — Static/configuration artifact; inspect its consumer.
- [instrumentation-client.ts](<../services/frontend-web/instrumentation-client.ts>) — Sentry client-side configuration. Runs in the browser. Initializes only when NEXT_PUBLIC_SENTRY_DSN is set, so a self-hosted install sends nothing anywhere unless the operator…
- [instrumentation.ts](<../services/frontend-web/instrumentation.ts>) — Declarations: register, onRequestError
- [middleware.ts](<../services/frontend-web/middleware.ts>) — Declarations: middleware, config
- [next-env.d.ts](<../services/frontend-web/next-env.d.ts>) — Static/configuration artifact; inspect its consumer.
- [next.config.ts](<../services/frontend-web/next.config.ts>) — Static/configuration artifact; inspect its consumer.
- [package.json](<../services/frontend-web/package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [postcss.config.js](<../services/frontend-web/postcss.config.js>) — Static/configuration artifact; inspect its consumer.
- [railway.toml](<../services/frontend-web/railway.toml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [sentry.client.config.ts](<../services/frontend-web/sentry.client.config.ts>) — Sentry client-side configuration. Runs in the browser. Initializes only when NEXT_PUBLIC_SENTRY_DSN is set, so local dev and preview environments without a DSN are unaffected.…
- [sentry.edge.config.ts](<../services/frontend-web/sentry.edge.config.ts>) — Sentry configuration for edge features (middleware, edge routes). Initializes only when SENTRY_DSN is set, so a self-hosted install sends nothing anywhere unless the operator opts…
- [sentry.server.config.ts](<../services/frontend-web/sentry.server.config.ts>) — Sentry server-side configuration. Runs whenever the Next.js server handles a request. Initializes only when SENTRY_DSN is set, so a self-hosted install sends nothing anywhere…
- [start.sh](<../services/frontend-web/start.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [tailwind.config.ts](<../services/frontend-web/tailwind.config.ts>) — /*.{js,ts,jsx,tsx,mdx}", "./components/*
- [tsconfig.json](<../services/frontend-web/tsconfig.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [vitest.config.ts](<../services/frontend-web/vitest.config.ts>) — Static/configuration artifact; inspect its consumer.
- [vitest.setup.ts](<../services/frontend-web/vitest.setup.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__`

[Directory guide](<../services/frontend-web/__tests__/directory.md>)

No immediate baseline/preparation files.

## `services/frontend-web/__tests__/admin`

[Directory guide](<../services/frontend-web/__tests__/admin/directory.md>)

- [AIModelsAdmin.test.tsx](<../services/frontend-web/__tests__/admin/AIModelsAdmin.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [QueryTemplatesAdmin.test.tsx](<../services/frontend-web/__tests__/admin/QueryTemplatesAdmin.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/analytics`

[Directory guide](<../services/frontend-web/__tests__/analytics/directory.md>)

- [AccuracyTrendChart.test.tsx](<../services/frontend-web/__tests__/analytics/AccuracyTrendChart.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnCohortsPage.test.tsx](<../services/frontend-web/__tests__/analytics/ChurnCohortsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CohortHeatmap.test.tsx](<../services/frontend-web/__tests__/analytics/CohortHeatmap.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ReasonCodeBreakdown.test.tsx](<../services/frontend-web/__tests__/analytics/ReasonCodeBreakdown.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/api`

[Directory guide](<../services/frontend-web/__tests__/api/directory.md>)

- [responses.test.ts](<../services/frontend-web/__tests__/api/responses.test.ts>) — Static/configuration artifact; inspect its consumer.
- [sentiment-accuracy.test.ts](<../services/frontend-web/__tests__/api/sentiment-accuracy.test.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/copilot`

[Directory guide](<../services/frontend-web/__tests__/copilot/directory.md>)

- [ChatArea.test.tsx](<../services/frontend-web/__tests__/copilot/ChatArea.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CommandBar.test.tsx](<../services/frontend-web/__tests__/copilot/CommandBar.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ConversationList.test.tsx](<../services/frontend-web/__tests__/copilot/ConversationList.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ConversationsPage.test.tsx](<../services/frontend-web/__tests__/copilot/ConversationsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CopilotIntegration.test.tsx](<../services/frontend-web/__tests__/copilot/CopilotIntegration.test.tsx>) — E2E-style integration tests for the AI Copilot conversation flow. These tests verify the full lifecycle: - Template click → conversation creation → first message auto-sent - New…
- [MessageBubble.test.tsx](<../services/frontend-web/__tests__/copilot/MessageBubble.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [MessageBubbleActions.test.tsx](<../services/frontend-web/__tests__/copilot/MessageBubbleActions.test.tsx>) — TDD tests for the copilot suggested-actions UI (frontend-actions-ui, Phase G): the tag-confirm dialog, the execute call, and the honest outcome display on MessageBubble. The…
- [MessageBubbleRating.test.tsx](<../services/frontend-web/__tests__/copilot/MessageBubbleRating.test.tsx>) — TDD tests for Human-in-the-Loop thumbs rating on MessageBubble (Track B). Tests: 7. test_thumbs_buttons_visible_on_ai_messages 8. test_thumbs_down_shows_feedback_input 9.…
- [PlanGating.test.tsx](<../services/frontend-web/__tests__/copilot/PlanGating.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [actionsContract.test.tsx](<../services/frontend-web/__tests__/copilot/actionsContract.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [conversations-api.test.ts](<../services/frontend-web/__tests__/copilot/conversations-api.test.ts>) — Static/configuration artifact; inspect its consumer.
- [useCopilotWebSocket.test.ts](<../services/frontend-web/__tests__/copilot/useCopilotWebSocket.test.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/customers`

[Directory guide](<../services/frontend-web/__tests__/customers/directory.md>)

- [ActivityTimeline.test.tsx](<../services/frontend-web/__tests__/customers/ActivityTimeline.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ActivityTimelineIcons.test.tsx](<../services/frontend-web/__tests__/customers/ActivityTimelineIcons.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [BulkAssignOwnerDialog.test.tsx](<../services/frontend-web/__tests__/customers/BulkAssignOwnerDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [BulkMarkChurnedDialog.test.tsx](<../services/frontend-web/__tests__/customers/BulkMarkChurnedDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [BulkOutreachDialog.test.tsx](<../services/frontend-web/__tests__/customers/BulkOutreachDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [BulkReviewSuggestionsDialog.test.tsx](<../services/frontend-web/__tests__/customers/BulkReviewSuggestionsDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [BulkRunPlaybookDialog.test.tsx](<../services/frontend-web/__tests__/customers/BulkRunPlaybookDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [BulkTagDialog.test.tsx](<../services/frontend-web/__tests__/customers/BulkTagDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnCsvImportDialog.test.tsx](<../services/frontend-web/__tests__/customers/ChurnCsvImportDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnProbabilityBadge.test.tsx](<../services/frontend-web/__tests__/customers/ChurnProbabilityBadge.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnRiskDrivers.test.tsx](<../services/frontend-web/__tests__/customers/ChurnRiskDrivers.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnSuggestionsEvidenceCell.test.tsx](<../services/frontend-web/__tests__/customers/ChurnSuggestionsEvidenceCell.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnSuggestionsEvidenceCellUsageDecline.test.tsx](<../services/frontend-web/__tests__/customers/ChurnSuggestionsEvidenceCellUsageDecline.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnSuggestionsPage.test.tsx](<../services/frontend-web/__tests__/customers/ChurnSuggestionsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnSuggestionsPageCopy.test.tsx](<../services/frontend-web/__tests__/customers/ChurnSuggestionsPageCopy.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnTimelineBadge.test.tsx](<../services/frontend-web/__tests__/customers/ChurnTimelineBadge.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ComponentProgressBars.test.tsx](<../services/frontend-web/__tests__/customers/ComponentProgressBars.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ConfirmSuggestionDialog.test.tsx](<../services/frontend-web/__tests__/customers/ConfirmSuggestionDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CrmCompanyCard.test.tsx](<../services/frontend-web/__tests__/customers/CrmCompanyCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CsOwnerBadge.test.tsx](<../services/frontend-web/__tests__/customers/CsOwnerBadge.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomerFeedbackList.test.tsx](<../services/frontend-web/__tests__/customers/CustomerFeedbackList.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomerProfilePage.test.tsx](<../services/frontend-web/__tests__/customers/CustomerProfilePage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomerTimeline.test.tsx](<../services/frontend-web/__tests__/customers/CustomerTimeline.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomersPage.test.tsx](<../services/frontend-web/__tests__/customers/CustomersPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomersPageChurnSuggestionsStatCard.test.tsx](<../services/frontend-web/__tests__/customers/CustomersPageChurnSuggestionsStatCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomersPageCohort.test.tsx](<../services/frontend-web/__tests__/customers/CustomersPageCohort.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [CustomersPageRoleGate.test.tsx](<../services/frontend-web/__tests__/customers/CustomersPageRoleGate.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [FeedbackDetailCustomerLink.test.tsx](<../services/frontend-web/__tests__/customers/FeedbackDetailCustomerLink.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [HealthScoreCircle.test.tsx](<../services/frontend-web/__tests__/customers/HealthScoreCircle.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [HealthTimeline.test.tsx](<../services/frontend-web/__tests__/customers/HealthTimeline.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [MarkAsChurnedDialog.test.tsx](<../services/frontend-web/__tests__/customers/MarkAsChurnedDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [OutreachCampaignsCard.test.tsx](<../services/frontend-web/__tests__/customers/OutreachCampaignsCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [OutreachOptOutToggle.test.tsx](<../services/frontend-web/__tests__/customers/OutreachOptOutToggle.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PotentialWinbackBanner.test.tsx](<../services/frontend-web/__tests__/customers/PotentialWinbackBanner.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [RecoverCustomerDialog.test.tsx](<../services/frontend-web/__tests__/customers/RecoverCustomerDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [RiskDistributionBar.test.tsx](<../services/frontend-web/__tests__/customers/RiskDistributionBar.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [RunPlaybookDropdown.test.tsx](<../services/frontend-web/__tests__/customers/RunPlaybookDropdown.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [SegmentBadge.test.tsx](<../services/frontend-web/__tests__/customers/SegmentBadge.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [TagChips.test.tsx](<../services/frontend-web/__tests__/customers/TagChips.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [UsageTimeline.test.tsx](<../services/frontend-web/__tests__/customers/UsageTimeline.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/dashboard`

[Directory guide](<../services/frontend-web/__tests__/dashboard/directory.md>)

- [ModelAccuracyCard.test.tsx](<../services/frontend-web/__tests__/dashboard/ModelAccuracyCard.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/feedback`

[Directory guide](<../services/frontend-web/__tests__/feedback/directory.md>)

- [FeedbackDetailActions.test.tsx](<../services/frontend-web/__tests__/feedback/FeedbackDetailActions.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [FeedbackDetailUrgentToggle.test.tsx](<../services/frontend-web/__tests__/feedback/FeedbackDetailUrgentToggle.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ResponseModal.test.tsx](<../services/frontend-web/__tests__/feedback/ResponseModal.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [TemplateBrowser.test.tsx](<../services/frontend-web/__tests__/feedback/TemplateBrowser.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/feedback-sources`

[Directory guide](<../services/frontend-web/__tests__/feedback-sources/directory.md>)

- [FeedbackSourcesDetailPage.guard.test.tsx](<../services/frontend-web/__tests__/feedback-sources/FeedbackSourcesDetailPage.guard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [FeedbackSourcesListPage.guard.test.tsx](<../services/frontend-web/__tests__/feedback-sources/FeedbackSourcesListPage.guard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [FeedbackSourcesNewPage.guard.test.tsx](<../services/frontend-web/__tests__/feedback-sources/FeedbackSourcesNewPage.guard.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/feedbacks`

[Directory guide](<../services/frontend-web/__tests__/feedbacks/directory.md>)

- [ChurnFactorBreakdown.test.tsx](<../services/frontend-web/__tests__/feedbacks/ChurnFactorBreakdown.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ConfidenceDisplay.test.tsx](<../services/frontend-web/__tests__/feedbacks/ConfidenceDisplay.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [FeedbackDeleteRoleGate.test.tsx](<../services/frontend-web/__tests__/feedbacks/FeedbackDeleteRoleGate.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/hooks`

[Directory guide](<../services/frontend-web/__tests__/hooks/directory.md>)

- [useRole.test.tsx](<../services/frontend-web/__tests__/hooks/useRole.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/integrations`

[Directory guide](<../services/frontend-web/__tests__/integrations/directory.md>)

- [CreateIssueButton.test.tsx](<../services/frontend-web/__tests__/integrations/CreateIssueButton.test.tsx>) — Task #11: Tests for "Create Issue" button placement on - Feedback detail page - Pain points page - Feature requests page Button behavior: - Hidden if no integration is connected -…
- [CreateIssueDialog.test.tsx](<../services/frontend-web/__tests__/integrations/CreateIssueDialog.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [LinearSettings.test.tsx](<../services/frontend-web/__tests__/integrations/LinearSettings.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [LinkedIssuesCard.test.tsx](<../services/frontend-web/__tests__/integrations/LinkedIssuesCard.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/notifications`

[Directory guide](<../services/frontend-web/__tests__/notifications/directory.md>)

- [NotificationDisplay.test.tsx](<../services/frontend-web/__tests__/notifications/NotificationDisplay.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/playbooks`

[Directory guide](<../services/frontend-web/__tests__/playbooks/directory.md>)

- [PlaybookEditor.actionTypes.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybookEditor.actionTypes.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PlaybookEditor.sendEmail.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybookEditor.sendEmail.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PlaybookEditor.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybookEditor.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PlaybookExecutionsList.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybookExecutionsList.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PlaybookPagesRoleGate.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybookPagesRoleGate.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PlaybookTemplateCard.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybookTemplateCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [PlaybooksListPage.test.tsx](<../services/frontend-web/__tests__/playbooks/PlaybooksListPage.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/realtime`

[Directory guide](<../services/frontend-web/__tests__/realtime/directory.md>)

- [ActivityFeedWidget.realtime.test.tsx](<../services/frontend-web/__tests__/realtime/ActivityFeedWidget.realtime.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [DashboardLayout.realtime.test.tsx](<../services/frontend-web/__tests__/realtime/DashboardLayout.realtime.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [FeedbacksPage.realtime.test.tsx](<../services/frontend-web/__tests__/realtime/FeedbacksPage.realtime.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [NotificationBell.realtime.test.tsx](<../services/frontend-web/__tests__/realtime/NotificationBell.realtime.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [RealtimeContext.test.tsx](<../services/frontend-web/__tests__/realtime/RealtimeContext.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [WorkflowPage.realtime.test.tsx](<../services/frontend-web/__tests__/realtime/WorkflowPage.realtime.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [useRealtimeEvents.test.ts](<../services/frontend-web/__tests__/realtime/useRealtimeEvents.test.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/reports`

[Directory guide](<../services/frontend-web/__tests__/reports/directory.md>)

- [ReportPreview.test.tsx](<../services/frontend-web/__tests__/reports/ReportPreview.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ReportsPage.test.tsx](<../services/frontend-web/__tests__/reports/ReportsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ReportsPageScheduled.test.tsx](<../services/frontend-web/__tests__/reports/ReportsPageScheduled.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/settings`

[Directory guide](<../services/frontend-web/__tests__/settings/directory.md>)

- [AIReadinessCard.test.tsx](<../services/frontend-web/__tests__/settings/AIReadinessCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsAIPage.accuracyTab.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsAIPage.accuracyTab.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsEmbeddings.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsEmbeddings.test.tsx>) — Tests for S3: surfacing the embedding provider/model in AI Settings. Verifies that: - The editable "Embedding model" input renders, bound to model_embeddings, and its value…
- [AISettingsGeneral.categoryClassifier.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsGeneral.categoryClassifier.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsGeneral.churnClassifier.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsGeneral.churnClassifier.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsGeneral.classifier.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsGeneral.classifier.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsGeneral.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsGeneral.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsGeneral.urgencyClassifier.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsGeneral.urgencyClassifier.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsProviders.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsProviders.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AISettingsProvidersLocalLLM.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsProvidersLocalLLM.test.tsx>) — Tests for Feature A: Local LLM provider options in AISettingsProviders. Verifies that: - "Ollama" and "Custom (OpenAI-compatible)" provider options are rendered - Selecting Ollama…
- [AISettingsSentiment.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsSentiment.test.tsx>) — Tests for the "Sentiment engine" toggle in AI Settings → General (M5.1 local-analyzer-sentiment-model, per-org-resolution aspect). Verifies that: - The toggle renders, defaults to…
- [AISettingsUsage.test.tsx](<../services/frontend-web/__tests__/settings/AISettingsUsage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AppSidebar.test.tsx](<../services/frontend-web/__tests__/settings/AppSidebar.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AutomationForm.test.tsx](<../services/frontend-web/__tests__/settings/AutomationForm.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [AutomationsList.test.tsx](<../services/frontend-web/__tests__/settings/AutomationsList.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnLabelGateCard.test.tsx](<../services/frontend-web/__tests__/settings/ChurnLabelGateCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ClassifierAccuracyCard.churn.test.tsx](<../services/frontend-web/__tests__/settings/ClassifierAccuracyCard.churn.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ClassifierAccuracyCard.test.tsx](<../services/frontend-web/__tests__/settings/ClassifierAccuracyCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [HealthWeightsEditor.test.tsx](<../services/frontend-web/__tests__/settings/HealthWeightsEditor.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [IntegrationDetailPage.discord.test.tsx](<../services/frontend-web/__tests__/settings/IntegrationDetailPage.discord.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [IntegrationDetailPage.teams.test.tsx](<../services/frontend-web/__tests__/settings/IntegrationDetailPage.teams.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [IntegrationsListPage.discord.test.tsx](<../services/frontend-web/__tests__/settings/IntegrationsListPage.discord.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [IntegrationsListPage.signatureBadge.test.tsx](<../services/frontend-web/__tests__/settings/IntegrationsListPage.signatureBadge.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [IntegrationsListPage.teams.test.tsx](<../services/frontend-web/__tests__/settings/IntegrationsListPage.teams.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [NewIntegrationPage.discord.test.tsx](<../services/frontend-web/__tests__/settings/NewIntegrationPage.discord.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [NewIntegrationPage.teams.test.tsx](<../services/frontend-web/__tests__/settings/NewIntegrationPage.teams.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [NotificationsSettingsPage.test.tsx](<../services/frontend-web/__tests__/settings/NotificationsSettingsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ResponseTemplates.test.tsx](<../services/frontend-web/__tests__/settings/ResponseTemplates.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [RetrievalAccuracyCard.test.tsx](<../services/frontend-web/__tests__/settings/RetrievalAccuracyCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [SentimentAccuracyCard.test.tsx](<../services/frontend-web/__tests__/settings/SentimentAccuracyCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [TeamsIcon.test.tsx](<../services/frontend-web/__tests__/settings/TeamsIcon.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [UsageChurnLabelsCard.test.tsx](<../services/frontend-web/__tests__/settings/UsageChurnLabelsCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [UsageEventsPage.test.tsx](<../services/frontend-web/__tests__/settings/UsageEventsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [WebhookDetail.test.tsx](<../services/frontend-web/__tests__/settings/WebhookDetail.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [WebhooksSettings.test.tsx](<../services/frontend-web/__tests__/settings/WebhooksSettings.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [WorkflowSettingsRoleGate.test.tsx](<../services/frontend-web/__tests__/settings/WorkflowSettingsRoleGate.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/__tests__/system`

[Directory guide](<../services/frontend-web/__tests__/system/directory.md>)

- [ChurnAccuracyDrillIn.test.tsx](<../services/frontend-web/__tests__/system/ChurnAccuracyDrillIn.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnAccuracyPage.test.tsx](<../services/frontend-web/__tests__/system/ChurnAccuracyPage.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ChurnEventsPage.test.tsx](<../services/frontend-web/__tests__/system/ChurnEventsPage.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/app`

[Directory guide](<../services/frontend-web/app/directory.md>)

- [global-error.tsx](<../services/frontend-web/app/global-error.tsx>) — Declarations: GlobalError
- [globals.css](<../services/frontend-web/app/globals.css>) — Static/configuration artifact; inspect its consumer.
- [icon.svg](<../services/frontend-web/app/icon.svg>) — Static/configuration artifact; inspect its consumer.
- [layout.tsx](<../services/frontend-web/app/layout.tsx>) — Declarations: metadata, RootLayout
- [page.tsx](<../services/frontend-web/app/page.tsx>) — Declarations: Home
- [providers.tsx](<../services/frontend-web/app/providers.tsx>) — Declarations: Providers

## `services/frontend-web/app/(dashboard)`

[Directory guide](<../services/frontend-web/app/(dashboard)/directory.md>)

- [layout.tsx](<../services/frontend-web/app/(dashboard)/layout.tsx>) — Declarations: DashboardLayout

## `services/frontend-web/app/(dashboard)/analytics`

[Directory guide](<../services/frontend-web/app/(dashboard)/analytics/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/analytics/page.tsx>) — Declarations: AnalyticsPage

## `services/frontend-web/app/(dashboard)/analytics/churn-cohorts`

[Directory guide](<../services/frontend-web/app/(dashboard)/analytics/churn-cohorts/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/analytics/churn-cohorts/page.tsx>) — Declarations: ChurnCohortsPage

## `services/frontend-web/app/(dashboard)/categories`

[Directory guide](<../services/frontend-web/app/(dashboard)/categories/directory.md>)

No immediate baseline/preparation files.

## `services/frontend-web/app/(dashboard)/categories/[category]`

[Directory guide](<../services/frontend-web/app/(dashboard)/categories/[category]/directory.md>)

- [columns.tsx](<../services/frontend-web/app/(dashboard)/categories/[category]/columns.tsx>) — Declarations: createColumns
- [page.tsx](<../services/frontend-web/app/(dashboard)/categories/[category]/page.tsx>) — Declarations: CategoryPage

## `services/frontend-web/app/(dashboard)/churn-risks`

[Directory guide](<../services/frontend-web/app/(dashboard)/churn-risks/directory.md>)

- [columns.tsx](<../services/frontend-web/app/(dashboard)/churn-risks/columns.tsx>) — Declarations: createColumns
- [page.tsx](<../services/frontend-web/app/(dashboard)/churn-risks/page.tsx>) — Declarations: ChurnRisksPage

## `services/frontend-web/app/(dashboard)/conversations`

[Directory guide](<../services/frontend-web/app/(dashboard)/conversations/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/conversations/page.tsx>) — Declarations: ConversationsPage

## `services/frontend-web/app/(dashboard)/customers`

[Directory guide](<../services/frontend-web/app/(dashboard)/customers/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/customers/page.tsx>) — Declarations: CustomersPage

## `services/frontend-web/app/(dashboard)/customers/[email]`

[Directory guide](<../services/frontend-web/app/(dashboard)/customers/[email]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/customers/[email]/page.tsx>) — Declarations: CustomerProfilePage

## `services/frontend-web/app/(dashboard)/customers/churn-suggestions`

[Directory guide](<../services/frontend-web/app/(dashboard)/customers/churn-suggestions/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/customers/churn-suggestions/page.tsx>) — Declarations: EvidenceCell, ChurnSuggestionsPage

## `services/frontend-web/app/(dashboard)/dashboard`

[Directory guide](<../services/frontend-web/app/(dashboard)/dashboard/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/dashboard/page.tsx>) — Declarations: DashboardPage

## `services/frontend-web/app/(dashboard)/feature-requests`

[Directory guide](<../services/frontend-web/app/(dashboard)/feature-requests/directory.md>)

- [columns.tsx](<../services/frontend-web/app/(dashboard)/feature-requests/columns.tsx>) — Declarations: createColumns
- [page.tsx](<../services/frontend-web/app/(dashboard)/feature-requests/page.tsx>) — Declarations: FeatureRequestsPage

## `services/frontend-web/app/(dashboard)/feedback-sources`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedback-sources/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/feedback-sources/page.tsx>) — Declarations: FeedbackSourcesPage

## `services/frontend-web/app/(dashboard)/feedback-sources/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedback-sources/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/feedback-sources/[id]/page.tsx>) — Declarations: SourceDetailPage

## `services/frontend-web/app/(dashboard)/feedback-sources/new`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedback-sources/new/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/feedback-sources/new/page.tsx>) — Declarations: NewSourcePage

## `services/frontend-web/app/(dashboard)/feedback-sources/pending`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedback-sources/pending/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/feedback-sources/pending/page.tsx>) — Declarations: PendingFeedbackPage

## `services/frontend-web/app/(dashboard)/feedbacks`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedbacks/directory.md>)

- [columns.tsx](<../services/frontend-web/app/(dashboard)/feedbacks/columns.tsx>) — Declarations: createColumns
- [data-table.tsx](<../services/frontend-web/app/(dashboard)/feedbacks/data-table.tsx>) — Declarations: DataTable
- [page.tsx](<../services/frontend-web/app/(dashboard)/feedbacks/page.tsx>) — Declarations: FeedbackPage

## `services/frontend-web/app/(dashboard)/feedbacks/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedbacks/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/feedbacks/[id]/page.tsx>) — Declarations: FeedbackDetailPage

## `services/frontend-web/app/(dashboard)/feedbacks/[id]/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedbacks/[id]/__tests__/directory.md>)

- [createIssueDraft.test.tsx](<../services/frontend-web/app/(dashboard)/feedbacks/[id]/__tests__/createIssueDraft.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/app/(dashboard)/feedbacks/[id]/create-issue`

[Directory guide](<../services/frontend-web/app/(dashboard)/feedbacks/[id]/create-issue/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/feedbacks/[id]/create-issue/page.tsx>) — Declarations: CreateIssuePage

## `services/frontend-web/app/(dashboard)/notifications`

[Directory guide](<../services/frontend-web/app/(dashboard)/notifications/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/notifications/page.tsx>) — Declarations: NotificationsPage

## `services/frontend-web/app/(dashboard)/notifications/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/notifications/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/notifications/[id]/page.tsx>) — Declarations: NotificationDetailPage

## `services/frontend-web/app/(dashboard)/pain-points`

[Directory guide](<../services/frontend-web/app/(dashboard)/pain-points/directory.md>)

- [columns.tsx](<../services/frontend-web/app/(dashboard)/pain-points/columns.tsx>) — Declarations: createColumns
- [page.tsx](<../services/frontend-web/app/(dashboard)/pain-points/page.tsx>) — Declarations: PainPointsPage

## `services/frontend-web/app/(dashboard)/reports`

[Directory guide](<../services/frontend-web/app/(dashboard)/reports/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/reports/page.tsx>) — Declarations: ReportsPage

## `services/frontend-web/app/(dashboard)/settings`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/page.tsx>) — Declarations: SettingsPage

## `services/frontend-web/app/(dashboard)/settings/ai`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/ai/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/ai/page.tsx>) — Declarations: AISettingsPage

## `services/frontend-web/app/(dashboard)/settings/api-keys`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/api-keys/directory.md>)

- [page.test.tsx](<../services/frontend-web/app/(dashboard)/settings/api-keys/page.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/api-keys/page.tsx>) — Declarations: SCOPE_BADGE_STYLES, SCOPE_DESCRIPTIONS, ScopeBadge, ApiKeysPage

## `services/frontend-web/app/(dashboard)/settings/automations`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/automations/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/page.tsx>) — Declarations: AutomationsPage

## `services/frontend-web/app/(dashboard)/settings/automations/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/automations/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/[id]/page.tsx>) — The category-match branch owns a text input, so it needs local state. It used to call useState() inline inside TriggerConfigFields' if-chain, which changed the hook order whenever…

## `services/frontend-web/app/(dashboard)/settings/automations/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/directory.md>)

- [CategoryMatchConfigKeys.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/CategoryMatchConfigKeys.test.tsx>) — The category-match editor must write the keys the backend actually reads. DEV-TRACKING P4: `[id]/page.tsx`'s CategoryMatchTriggerFields read and wrote `config.tags` /…
- [SendCustomerEmailConfigKeys.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/SendCustomerEmailConfigKeys.test.tsx>) — The send_customer_email editor must write EXACTLY the two keys the backend accepts. `SendCustomerEmailConfig` (backend `automations.py`) is `extra="forbid"`, so a config carrying…
- [id-action-support.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-action-support.test.tsx>) — R6 (automation-action-support) on the rule detail/edit page: the action select is filtered by the trigger's supported actions, a rule saved before the matrix existed shows an…
- [id-batch-sentiment-trigger.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-batch-sentiment-trigger.test.tsx>) — Tests for the `batch_sentiment_threshold` trigger additions to the automation rule detail/edit page: the trigger type option, config field pre-population from trigger_config,…
- [id-churn-playbook.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-churn-playbook.test.tsx>) — Tests for the churn-triggered-playbooks additions to the automation rule detail/edit page: the `churn_probability_threshold` trigger config, the `run_playbook` action config…
- [id-email-deliveries.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-email-deliveries.test.tsx>) — Tests for the Email Deliveries surface on the automation rule detail page (automation-send-customer-email, frontend-editor Phase 4). A `skipped` row is the honest record of a send…
- [id-send-customer-email.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-send-customer-email.test.tsx>) — Tests for the `send_customer_email` action editor on the automation rule detail/edit page (automation-send-customer-email, frontend-editor Phase 2). The contract this pins:…
- [id-shadow-execution-badge.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-shadow-execution-badge.test.tsx>) — Test for the M8 shadow-badge fix on the automation rule detail page's execution log: an execution with status "shadow" must render a distinct, non-destructive badge — not the red…
- [id-usage-trend-trigger.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/id-usage-trend-trigger.test.tsx>) — Tests for the `usage_trend` trigger additions to the automation rule detail/edit page: the trigger type option, states config pre-population from trigger_config, client-side…
- [list-shadow-badge.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/list-shadow-badge.test.tsx>) — Tests for the "Shadow" badge added to the automations list page next to rules whose mode === 'shadow', and that the existing is_active Switch keeps working unmodified.
- [new-action-support.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/new-action-support.test.tsx>) — R6 (automation-action-support): the New rule page only offers the actions the selected trigger supports (served by GET /automations/action-support), warns on an unsupported action…
- [new-batch-sentiment-trigger.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/new-batch-sentiment-trigger.test.tsx>) — Tests for the `batch_sentiment_threshold` trigger additions to the "New Automation Rule" page: the trigger type option, the config fields (sentiment / window_hours / mode /…
- [new-churn-playbook.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/new-churn-playbook.test.tsx>) — Tests for the churn-triggered-playbooks additions to the "New Automation Rule" page: the `churn_probability_threshold` trigger config, the `run_playbook` action config (playbook…
- [new-send-customer-email.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/new-send-customer-email.test.tsx>) — Tests for the `send_customer_email` action editor on the "New Automation Rule" page (automation-send-customer-email, frontend-editor Phase 2). The save payload must carry EXACTLY…
- [new-usage-trend-trigger.test.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/__tests__/new-usage-trend-trigger.test.tsx>) — Tests for the `usage_trend` trigger additions to the "New Automation Rule" page: the trigger type option, the states config (declining/sharp_decline checkboxes, both…

## `services/frontend-web/app/(dashboard)/settings/automations/new`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/automations/new/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/automations/new/page.tsx>) — Action types the rule's trigger supports (see allowedActionTypes).

## `services/frontend-web/app/(dashboard)/settings/integrations`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/page.tsx>) — Declarations: IntegrationsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/[id]/page.tsx>) — Declarations: IntegrationDetailPage

## `services/frontend-web/app/(dashboard)/settings/integrations/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/__tests__/directory.md>)

- [IntegrationsPage.test.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/__tests__/IntegrationsPage.test.tsx>) — Smoke test: verifies hubspotAPI.getStatus is exported and callable, and that the HubSpotConnectionStatus type is exported. Full page render tests would require Next.js test…
- [SalesforceTile.test.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/__tests__/SalesforceTile.test.tsx>) — Render tests for the Salesforce tile on the integrations index page (Phase 2). Verifies: 1. When disconnected, an "Available" Salesforce tile renders under Available Integrations,…

## `services/frontend-web/app/(dashboard)/settings/integrations/asana`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/asana/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/asana/page.tsx>) — Declarations: AsanaSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/hubspot`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/hubspot/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/hubspot/page.tsx>) — Declarations: HubSpotSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/hubspot/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/hubspot/__tests__/directory.md>)

- [HubSpotPage.test.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/hubspot/__tests__/HubSpotPage.test.tsx>) — Tests for HubSpot detail page (Phase 7). API contract tests verify: 1. hubspotAPI.connect is callable with access_token and arr_property_name 2. hubspotAPI.disconnect is callable…

## `services/frontend-web/app/(dashboard)/settings/integrations/intercom`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/intercom/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/intercom/page.tsx>) — Declarations: IntercomSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/intercom/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/intercom/__tests__/directory.md>)

- [IntercomPage.test.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/intercom/__tests__/IntercomPage.test.tsx>) — Tests for the Intercom token-paste connect page. Mirrors ZendeskPage.test.tsx, the shipped precedent for an own-auth token-paste connect page. Verifies: 1. getStatus is called on…

## `services/frontend-web/app/(dashboard)/settings/integrations/jira`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/jira/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/jira/page.tsx>) — Declarations: JiraSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/linear`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/linear/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/linear/page.tsx>) — Declarations: LinearSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/new`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/new/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/new/page.tsx>) — Declarations: NewIntegrationPage

## `services/frontend-web/app/(dashboard)/settings/integrations/salesforce`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/salesforce/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/salesforce/page.tsx>) — Declarations: SalesforceSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/salesforce/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/salesforce/__tests__/directory.md>)

- [SalesforcePage.test.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/salesforce/__tests__/SalesforcePage.test.tsx>) — Tests for the Salesforce connect/detail page (Phase 3). API contract tests verify: 1. salesforceAPI.getConnectUrl / getStatus / disconnect / test are callable. Component rendering…

## `services/frontend-web/app/(dashboard)/settings/integrations/zendesk`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/zendesk/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/zendesk/page.tsx>) — Declarations: ZendeskSettingsPage

## `services/frontend-web/app/(dashboard)/settings/integrations/zendesk/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/integrations/zendesk/__tests__/directory.md>)

- [ZendeskPage.test.tsx](<../services/frontend-web/app/(dashboard)/settings/integrations/zendesk/__tests__/ZendeskPage.test.tsx>) — Tests for the Zendesk connect page (frontend Phase 2). Mirrors HubSpotPage.test.tsx's pattern (closer structural match than Jira's untested page): full RTL render of an own-auth…

## `services/frontend-web/app/(dashboard)/settings/notifications`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/notifications/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/notifications/page.tsx>) — Declarations: NotificationsSettingsPage

## `services/frontend-web/app/(dashboard)/settings/playbooks`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/playbooks/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/playbooks/page.tsx>) — Declarations: PlaybooksPage

## `services/frontend-web/app/(dashboard)/settings/playbooks/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/playbooks/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/playbooks/[id]/page.tsx>) — Declarations: PlaybookDetailPage

## `services/frontend-web/app/(dashboard)/settings/playbooks/new`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/playbooks/new/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/playbooks/new/page.tsx>) — Declarations: NewPlaybookPage

## `services/frontend-web/app/(dashboard)/settings/preferences`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/preferences/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/preferences/page.tsx>) — Declarations: PreferencesPage

## `services/frontend-web/app/(dashboard)/settings/response-templates`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/response-templates/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/response-templates/page.tsx>) — Declarations: ResponseTemplatesPage

## `services/frontend-web/app/(dashboard)/settings/sso`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/sso/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/sso/page.tsx>) — Declarations: SsoSettingsPage

## `services/frontend-web/app/(dashboard)/settings/sso/__tests__`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/sso/__tests__/directory.md>)

- [page.test.tsx](<../services/frontend-web/app/(dashboard)/settings/sso/__tests__/page.test.tsx>) — Tests for the admin SSO settings page — the OIDC config card plus the SAML config card rendered below it (SamlConfigCard, a separate child component). Verifies: 1. Non-admin…

## `services/frontend-web/app/(dashboard)/settings/team`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/team/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/team/page.tsx>) — Declarations: TeamSettingsPage

## `services/frontend-web/app/(dashboard)/settings/usage-events`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/usage-events/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/usage-events/page.tsx>) — Declarations: UsageEventsPage

## `services/frontend-web/app/(dashboard)/settings/webhooks`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/webhooks/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/webhooks/page.tsx>) — Declarations: WebhooksPage

## `services/frontend-web/app/(dashboard)/settings/webhooks/[id]`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/webhooks/[id]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/webhooks/[id]/page.tsx>) — Declarations: WebhookDetailPage

## `services/frontend-web/app/(dashboard)/settings/webhooks/new`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/webhooks/new/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/webhooks/new/page.tsx>) — Declarations: NewWebhookPage

## `services/frontend-web/app/(dashboard)/settings/workflow`

[Directory guide](<../services/frontend-web/app/(dashboard)/settings/workflow/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/settings/workflow/page.tsx>) — Declarations: WorkflowPage

## `services/frontend-web/app/(dashboard)/shared-links`

[Directory guide](<../services/frontend-web/app/(dashboard)/shared-links/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/shared-links/page.tsx>) — Declarations: SharedLinksPage

## `services/frontend-web/app/(dashboard)/system`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/directory.md>)

No immediate baseline/preparation files.

## `services/frontend-web/app/(dashboard)/system/ai-models`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/ai-models/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/ai-models/page.tsx>) — Declarations: AIModelsAdminPage

## `services/frontend-web/app/(dashboard)/system/changelog`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/changelog/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/changelog/page.tsx>) — Declarations: AdminChangelogPage

## `services/frontend-web/app/(dashboard)/system/churn-accuracy`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/churn-accuracy/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/churn-accuracy/page.tsx>) — Declarations: ChurnAccuracyPage

## `services/frontend-web/app/(dashboard)/system/churn-accuracy/[orgId]`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/churn-accuracy/[orgId]/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/churn-accuracy/[orgId]/page.tsx>) — Declarations: ChurnAccuracyDrillInPage

## `services/frontend-web/app/(dashboard)/system/churn-events`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/churn-events/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/churn-events/page.tsx>) — /system/churn-events — System admin view of all churn events across all organizations. Read-only in v1. Supports filtering, server-side pagination, and CSV export.

## `services/frontend-web/app/(dashboard)/system/organizations`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/organizations/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/organizations/page.tsx>) — Declarations: AdminOrganizationsPage

## `services/frontend-web/app/(dashboard)/system/query-templates`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/query-templates/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/query-templates/page.tsx>) — Declarations: QueryTemplatesAdminPage

## `services/frontend-web/app/(dashboard)/system/users`

[Directory guide](<../services/frontend-web/app/(dashboard)/system/users/directory.md>)

- [page.tsx](<../services/frontend-web/app/(dashboard)/system/users/page.tsx>) — Declarations: AdminUsersPage

## `services/frontend-web/app/(dashboard)/urgent-feedbacks`

[Directory guide](<../services/frontend-web/app/(dashboard)/urgent-feedbacks/directory.md>)

- [columns.tsx](<../services/frontend-web/app/(dashboard)/urgent-feedbacks/columns.tsx>) — Declarations: createColumns
- [page.tsx](<../services/frontend-web/app/(dashboard)/urgent-feedbacks/page.tsx>) — Declarations: UrgentFeedbackPage

## `services/frontend-web/app/(dashboard)/workflow`

[Directory guide](<../services/frontend-web/app/(dashboard)/workflow/directory.md>)

- [kanban-card.tsx](<../services/frontend-web/app/(dashboard)/workflow/kanban-card.tsx>) — Declarations: KanbanCard
- [kanban-view.tsx](<../services/frontend-web/app/(dashboard)/workflow/kanban-view.tsx>) — Declarations: KanbanView
- [page.tsx](<../services/frontend-web/app/(dashboard)/workflow/page.tsx>) — Declarations: WorkflowPage

## `services/frontend-web/app/invite`

[Directory guide](<../services/frontend-web/app/invite/directory.md>)

No immediate baseline/preparation files.

## `services/frontend-web/app/invite/[token]`

[Directory guide](<../services/frontend-web/app/invite/[token]/directory.md>)

- [page.tsx](<../services/frontend-web/app/invite/[token]/page.tsx>) — Declarations: InvitePage

## `services/frontend-web/app/login`

[Directory guide](<../services/frontend-web/app/login/directory.md>)

- [page.tsx](<../services/frontend-web/app/login/page.tsx>) — Resolve a `?sso_error=<code>` query param to a friendly message, without a protocol tag on the code itself. Deterministic, code-set based (no magic-string compare against either…

## `services/frontend-web/app/login/__tests__`

[Directory guide](<../services/frontend-web/app/login/__tests__/directory.md>)

- [page.test.tsx](<../services/frontend-web/app/login/__tests__/page.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/app/login/callback`

[Directory guide](<../services/frontend-web/app/login/callback/directory.md>)

- [page.tsx](<../services/frontend-web/app/login/callback/page.tsx>) — Declarations: LoginCallbackPage

## `services/frontend-web/app/login/callback/__tests__`

[Directory guide](<../services/frontend-web/app/login/callback/__tests__/directory.md>)

- [page.test.tsx](<../services/frontend-web/app/login/callback/__tests__/page.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/app/outreach`

[Directory guide](<../services/frontend-web/app/outreach/directory.md>)

No immediate baseline/preparation files.

## `services/frontend-web/app/outreach/unsubscribe`

[Directory guide](<../services/frontend-web/app/outreach/unsubscribe/directory.md>)

- [page.tsx](<../services/frontend-web/app/outreach/unsubscribe/page.tsx>) — Declarations: UnsubscribePage

## `services/frontend-web/app/outreach/unsubscribe/__tests__`

[Directory guide](<../services/frontend-web/app/outreach/unsubscribe/__tests__/directory.md>)

- [page.test.tsx](<../services/frontend-web/app/outreach/unsubscribe/__tests__/page.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/app/shared`

[Directory guide](<../services/frontend-web/app/shared/directory.md>)

No immediate baseline/preparation files.

## `services/frontend-web/app/shared/[token]`

[Directory guide](<../services/frontend-web/app/shared/[token]/directory.md>)

- [page.tsx](<../services/frontend-web/app/shared/[token]/page.tsx>) — Declarations: SharedAnalyticsPage

## `services/frontend-web/app/signup`

[Directory guide](<../services/frontend-web/app/signup/directory.md>)

- [page.tsx](<../services/frontend-web/app/signup/page.tsx>) — Declarations: SignupPage

## `services/frontend-web/components`

[Directory guide](<../services/frontend-web/components/directory.md>)

- [AppSidebar.tsx](<../services/frontend-web/components/AppSidebar.tsx>) — Declarations: AppSidebar
- [Button.tsx](<../services/frontend-web/components/Button.tsx>) — Declarations: Button
- [Card.tsx](<../services/frontend-web/components/Card.tsx>) — Declarations: Card, CardHeader, CardContent, CardTitle
- [Checkbox.tsx](<../services/frontend-web/components/Checkbox.tsx>) — Declarations: CheckboxProps
- [GoogleSignInButton.tsx](<../services/frontend-web/components/GoogleSignInButton.tsx>) — Declarations: GoogleSignInButton
- [Header.tsx](<../services/frontend-web/components/Header.tsx>) — Declarations: Header
- [InviteMemberModal.tsx](<../services/frontend-web/components/InviteMemberModal.tsx>) — Declarations: InviteMemberModal
- [Logo.tsx](<../services/frontend-web/components/Logo.tsx>) — Static/configuration artifact; inspect its consumer.
- [NotificationBell.tsx](<../services/frontend-web/components/NotificationBell.tsx>) — Declarations: NotificationBell
- [OidcSignInButton.tsx](<../services/frontend-web/components/OidcSignInButton.tsx>) — Declarations: OidcSignInButton
- [SamlSignInButton.tsx](<../services/frontend-web/components/SamlSignInButton.tsx>) — Declarations: SamlSignInButton
- [SavedViewsBar.tsx](<../services/frontend-web/components/SavedViewsBar.tsx>) — Declarations: SavedViewsBar
- [ShareAnalyticsDialog.tsx](<../services/frontend-web/components/ShareAnalyticsDialog.tsx>) — Declarations: ShareAnalyticsDialog
- [SlackIntegration.tsx](<../services/frontend-web/components/SlackIntegration.tsx>) — Declarations: SlackIntegration
- [StatCard.tsx](<../services/frontend-web/components/StatCard.tsx>) — Declarations: StatCard
- [ThemeToggle.tsx](<../services/frontend-web/components/ThemeToggle.tsx>) — Declarations: ThemeToggle

## `services/frontend-web/components/__tests__`

[Directory guide](<../services/frontend-web/components/__tests__/directory.md>)

- [GoogleSignInButton.test.tsx](<../services/frontend-web/components/__tests__/GoogleSignInButton.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [OidcSignInButton.test.tsx](<../services/frontend-web/components/__tests__/OidcSignInButton.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [SamlSignInButton.test.tsx](<../services/frontend-web/components/__tests__/SamlSignInButton.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [StatCard.test.tsx](<../services/frontend-web/components/__tests__/StatCard.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/components/analytics`

[Directory guide](<../services/frontend-web/components/analytics/directory.md>)

- [AccuracyTrendChart.tsx](<../services/frontend-web/components/analytics/AccuracyTrendChart.tsx>) — Declarations: AccuracyTrendChart
- [ChurnCohortBarChart.tsx](<../services/frontend-web/components/analytics/ChurnCohortBarChart.tsx>) — Horizontal bar chart showing churn rate per cohort.
- [CohortHeatmap.tsx](<../services/frontend-web/components/analytics/CohortHeatmap.tsx>) — 2D heatmap of churn rate by cohort x time bucket.
- [ReasonCodeBreakdown.tsx](<../services/frontend-web/components/analytics/ReasonCodeBreakdown.tsx>) — Donut chart of aggregated churn reason codes across all cohorts.

## `services/frontend-web/components/copilot`

[Directory guide](<../services/frontend-web/components/copilot/directory.md>)

- [ChatArea.tsx](<../services/frontend-web/components/copilot/ChatArea.tsx>) — If set, auto-send this query as the first message after loading
- [CommandBar.tsx](<../services/frontend-web/components/copilot/CommandBar.tsx>) — Declarations: CommandBar
- [CommandBarContext.tsx](<../services/frontend-web/components/copilot/CommandBarContext.tsx>) — Declarations: useCommandBar
- [CommandBarProvider.tsx](<../services/frontend-web/components/copilot/CommandBarProvider.tsx>) — Declarations: CommandBarProvider
- [ContextScopeSelector.tsx](<../services/frontend-web/components/copilot/ContextScopeSelector.tsx>) — Where the dropdown opens relative to the trigger. Default: 'below'
- [ConversationList.tsx](<../services/frontend-web/components/copilot/ConversationList.tsx>) — Change this value to trigger a re-fetch of the conversation list
- [CopilotActionButton.tsx](<../services/frontend-web/components/copilot/CopilotActionButton.tsx>) — Persisted conversation id the proposal lives in — the execute route resolves the proposal by conversation_id + proposal_id. Never the WS turn message id. Absent (e.g.…
- [CopilotHeaderButton.tsx](<../services/frontend-web/components/copilot/CopilotHeaderButton.tsx>) — Declarations: CopilotHeaderButton
- [CopilotUsageSection.tsx](<../services/frontend-web/components/copilot/CopilotUsageSection.tsx>) — Declarations: CopilotUsageSection
- [MentionAutocomplete.tsx](<../services/frontend-web/components/copilot/MentionAutocomplete.tsx>) — If set, this option represents a scope chip rather than inline text
- [MessageActions.tsx](<../services/frontend-web/components/copilot/MessageActions.tsx>) — Declarations: StopButton, ThumbsRating, MessageActions
- [MessageBubble.tsx](<../services/frontend-web/components/copilot/MessageBubble.tsx>) — Persisted conversation id for suggested-action execution (numeric DB id, not the WS turn message id). Absent → action buttons render disabled.
- [ReportPreview.tsx](<../services/frontend-web/components/copilot/ReportPreview.tsx>) — Declarations: ReportPreview

## `services/frontend-web/components/customers`

[Directory guide](<../services/frontend-web/components/customers/directory.md>)

- [ActivityTimeline.tsx](<../services/frontend-web/components/customers/ActivityTimeline.tsx>) — Declarations: eventIconMap, ActivityTimeline
- [BulkAssignOwnerDialog.tsx](<../services/frontend-web/components/customers/BulkAssignOwnerDialog.tsx>) — Size of the resolved cohort — same value shown in the "Bulk Actions (N)" trigger.
- [BulkMarkChurnedDialog.tsx](<../services/frontend-web/components/customers/BulkMarkChurnedDialog.tsx>) — Declarations: BulkMarkChurnedDialog
- [BulkOutreachDialog.tsx](<../services/frontend-web/components/customers/BulkOutreachDialog.tsx>) — Size of the resolved cohort — same value shown in the "Bulk Actions (N)" trigger.
- [BulkReviewSuggestionsDialog.tsx](<../services/frontend-web/components/customers/BulkReviewSuggestionsDialog.tsx>) — Declarations: BulkReviewSuggestionsDialog
- [BulkRunPlaybookDialog.tsx](<../services/frontend-web/components/customers/BulkRunPlaybookDialog.tsx>) — Declarations: BulkRunPlaybookDialog
- [BulkTagDialog.tsx](<../services/frontend-web/components/customers/BulkTagDialog.tsx>) — Size of the resolved cohort — same value shown in the "Bulk Actions (N)" trigger.
- [ChurnCsvImportDialog.tsx](<../services/frontend-web/components/customers/ChurnCsvImportDialog.tsx>) — Declarations: ChurnCsvImportDialog
- [ChurnProbabilityBadge.tsx](<../services/frontend-web/components/customers/ChurnProbabilityBadge.tsx>) — Declarations: ChurnProbabilityBadgeProps, ChurnProbabilityBadge
- [ChurnRiskDrivers.tsx](<../services/frontend-web/components/customers/ChurnRiskDrivers.tsx>) — Declarations: ChurnRiskDrivers
- [ChurnTimelineBadge.tsx](<../services/frontend-web/components/customers/ChurnTimelineBadge.tsx>) — Declarations: TimeToChurnBucket, ChurnTimelineBadgeProps, ChurnTimelineBadge
- [ComponentProgressBars.tsx](<../services/frontend-web/components/customers/ComponentProgressBars.tsx>) — 0-100 usage component; defaults to 50 (neutral) when omitted
- [ConfirmSuggestionDialog.tsx](<../services/frontend-web/components/customers/ConfirmSuggestionDialog.tsx>) — Declarations: ConfirmSuggestionDialog
- [CrmCompanyCard.tsx](<../services/frontend-web/components/customers/CrmCompanyCard.tsx>) — Declarations: CrmCompanyCard
- [CsOwnerBadge.tsx](<../services/frontend-web/components/customers/CsOwnerBadge.tsx>) — Assigned CS-owner chip (segment-actions bulk assign-owner). Mirrors SegmentBadge's Sunset-Horizon theming. Renders a clean "Unassigned" label — no error state — when the customer…
- [CustomerFeedbackList.tsx](<../services/frontend-web/components/customers/CustomerFeedbackList.tsx>) — Declarations: CustomerFeedbackList
- [CustomerTimeline.tsx](<../services/frontend-web/components/customers/CustomerTimeline.tsx>) — Declarations: CustomerTimeline
- [HealthScoreCircle.tsx](<../services/frontend-web/components/customers/HealthScoreCircle.tsx>) — Declarations: getHealthColor, HealthScoreCircle
- [HealthTimeline.tsx](<../services/frontend-web/components/customers/HealthTimeline.tsx>) — Declarations: HealthTimeline
- [MarkAsChurnedDialog.tsx](<../services/frontend-web/components/customers/MarkAsChurnedDialog.tsx>) — Declarations: MarkAsChurnedDialog
- [OutreachCampaignsCard.tsx](<../services/frontend-web/components/customers/OutreachCampaignsCard.tsx>) — Declarations: OutreachCampaignsCard
- [OutreachOptOutToggle.tsx](<../services/frontend-web/components/customers/OutreachOptOutToggle.tsx>) — Per-customer outreach opt-out switch (outreach-core AC9). Bound directly to `outreach_opt_out`: checked = customer has opted out of outreach emails. Admin/owner only — members…
- [PotentialWinbackBanner.tsx](<../services/frontend-web/components/customers/PotentialWinbackBanner.tsx>) — Declarations: PotentialWinbackBanner
- [ReasonCodeSelect.tsx](<../services/frontend-web/components/customers/ReasonCodeSelect.tsx>) — Declarations: ReasonCodeSelect
- [RecoverCustomerDialog.tsx](<../services/frontend-web/components/customers/RecoverCustomerDialog.tsx>) — Declarations: RecoverCustomerDialog
- [RiskDistributionBar.tsx](<../services/frontend-web/components/customers/RiskDistributionBar.tsx>) — Declarations: RiskDistributionBar
- [RunPlaybookDropdown.tsx](<../services/frontend-web/components/customers/RunPlaybookDropdown.tsx>) — Declarations: RunPlaybookDropdown
- [SegmentBadge.tsx](<../services/frontend-web/components/customers/SegmentBadge.tsx>) — Rule-based customer segment chip. Mirrors ChurnTimelineBadge styling. Handles null/undefined/unrecognized segment values by rendering a subtle neutral "Unsegmented" chip instead…
- [TagChips.tsx](<../services/frontend-web/components/customers/TagChips.tsx>) — Max chips to render before collapsing the rest into a "+N" indicator.
- [UsageTimeline.tsx](<../services/frontend-web/components/customers/UsageTimeline.tsx>) — Declarations: UsageTimeline

## `services/frontend-web/components/dashboard`

[Directory guide](<../services/frontend-web/components/dashboard/directory.md>)

- [DashboardGrid.tsx](<../services/frontend-web/components/dashboard/DashboardGrid.tsx>) — Declarations: DashboardGrid
- [DateRangeSelector.tsx](<../services/frontend-web/components/dashboard/DateRangeSelector.tsx>) — Declarations: DateRangeSelector
- [WidgetCatalog.tsx](<../services/frontend-web/components/dashboard/WidgetCatalog.tsx>) — Declarations: WidgetCatalog
- [WidgetWrapper.tsx](<../services/frontend-web/components/dashboard/WidgetWrapper.tsx>) — Declarations: WidgetWrapper

## `services/frontend-web/components/dashboard/constants`

[Directory guide](<../services/frontend-web/components/dashboard/constants/directory.md>)

- [default-layouts.ts](<../services/frontend-web/components/dashboard/constants/default-layouts.ts>) — Declarations: defaultLayout, responsiveLayouts, gridBreakpoints, gridCols
- [widget-registry.ts](<../services/frontend-web/components/dashboard/constants/widget-registry.ts>) — Declarations: WidgetCategory, WidgetDefinition, widgetRegistry, widgetRegistryMap, widgetCategories

## `services/frontend-web/components/dashboard/hooks`

[Directory guide](<../services/frontend-web/components/dashboard/hooks/directory.md>)

- [useDashboardData.ts](<../services/frontend-web/components/dashboard/hooks/useDashboardData.ts>) — Declarations: useDashboardStats, useComparison, useTrends, useActivityFeed, useTeamActivity, useAnomalies
- [useDashboardLayout.ts](<../services/frontend-web/components/dashboard/hooks/useDashboardLayout.ts>) — Declarations: useDashboardLayout
- [useDateRange.ts](<../services/frontend-web/components/dashboard/hooks/useDateRange.ts>) — Declarations: DateRange, dateRangeToDays, useDateRange

## `services/frontend-web/components/dashboard/widgets`

[Directory guide](<../services/frontend-web/components/dashboard/widgets/directory.md>)

- [ActivityFeedWidget.tsx](<../services/frontend-web/components/dashboard/widgets/ActivityFeedWidget.tsx>) — Declarations: ActivityFeedWidget
- [AiInsightsWidget.tsx](<../services/frontend-web/components/dashboard/widgets/AiInsightsWidget.tsx>) — Declarations: AiInsightsWidget
- [AnomalyAlertsWidget.tsx](<../services/frontend-web/components/dashboard/widgets/AnomalyAlertsWidget.tsx>) — Declarations: AnomalyAlertsWidget
- [AtRiskCustomersWidget.tsx](<../services/frontend-web/components/dashboard/widgets/AtRiskCustomersWidget.tsx>) — Declarations: AtRiskCustomersWidget
- [ChurnRiskWidget.tsx](<../services/frontend-web/components/dashboard/widgets/ChurnRiskWidget.tsx>) — Declarations: ChurnRiskWidget
- [FeatureRequestsWidget.tsx](<../services/frontend-web/components/dashboard/widgets/FeatureRequestsWidget.tsx>) — Declarations: FeatureRequestsWidget
- [ModelAccuracyCard.tsx](<../services/frontend-web/components/dashboard/widgets/ModelAccuracyCard.tsx>) — Declarations: ModelAccuracyCard
- [NpsScoreWidget.tsx](<../services/frontend-web/components/dashboard/widgets/NpsScoreWidget.tsx>) — Declarations: NpsScoreWidget
- [PainPointsBarWidget.tsx](<../services/frontend-web/components/dashboard/widgets/PainPointsBarWidget.tsx>) — Declarations: PainPointsBarWidget
- [PainPointsListWidget.tsx](<../services/frontend-web/components/dashboard/widgets/PainPointsListWidget.tsx>) — Declarations: PainPointsListWidget
- [SentimentDonutWidget.tsx](<../services/frontend-web/components/dashboard/widgets/SentimentDonutWidget.tsx>) — Declarations: SentimentDonutWidget
- [StatCardWidget.tsx](<../services/frontend-web/components/dashboard/widgets/StatCardWidget.tsx>) — Declarations: StatCardWidget
- [TeamActivityWidget.tsx](<../services/frontend-web/components/dashboard/widgets/TeamActivityWidget.tsx>) — Declarations: TeamActivityWidget
- [TopCategoriesWidget.tsx](<../services/frontend-web/components/dashboard/widgets/TopCategoriesWidget.tsx>) — Declarations: TopCategoriesWidget
- [TrendLineWidget.tsx](<../services/frontend-web/components/dashboard/widgets/TrendLineWidget.tsx>) — Declarations: TrendLineWidget
- [UrgentFeedbackWidget.tsx](<../services/frontend-web/components/dashboard/widgets/UrgentFeedbackWidget.tsx>) — Declarations: UrgentFeedbackWidget

## `services/frontend-web/components/feedback`

[Directory guide](<../services/frontend-web/components/feedback/directory.md>)

- [LinkedIssuesCard.tsx](<../services/frontend-web/components/feedback/LinkedIssuesCard.tsx>) — Declarations: LinkedIssuesCard
- [ResponseModal.tsx](<../services/frontend-web/components/feedback/ResponseModal.tsx>) — Declarations: ResponseModalProps, ResponseModal
- [TemplateBrowser.tsx](<../services/frontend-web/components/feedback/TemplateBrowser.tsx>) — Declarations: TemplateBrowserProps, TemplateBrowser

## `services/frontend-web/components/feedbacks`

[Directory guide](<../services/frontend-web/components/feedbacks/directory.md>)

- [ChurnFactorBreakdown.tsx](<../services/frontend-web/components/feedbacks/ChurnFactorBreakdown.tsx>) — Declarations: ChurnFactor, ChurnRiskFactors, ChurnFactorBreakdown
- [ConfidenceBadge.tsx](<../services/frontend-web/components/feedbacks/ConfidenceBadge.tsx>) — Declarations: ConfidenceBadge
- [LowConfidenceWarning.tsx](<../services/frontend-web/components/feedbacks/LowConfidenceWarning.tsx>) — Declarations: LowConfidenceWarning

## `services/frontend-web/components/icons`

[Directory guide](<../services/frontend-web/components/icons/directory.md>)

- [AsanaIcon.tsx](<../services/frontend-web/components/icons/AsanaIcon.tsx>) — Declarations: AsanaIcon
- [DiscordIcon.tsx](<../services/frontend-web/components/icons/DiscordIcon.tsx>) — Declarations: DiscordIcon
- [IntercomIcon.tsx](<../services/frontend-web/components/icons/IntercomIcon.tsx>) — Declarations: IntercomIcon
- [JiraIcon.tsx](<../services/frontend-web/components/icons/JiraIcon.tsx>) — Declarations: JiraIcon
- [LinearIcon.tsx](<../services/frontend-web/components/icons/LinearIcon.tsx>) — Declarations: LinearIcon
- [ProviderLogos.tsx](<../services/frontend-web/components/icons/ProviderLogos.tsx>) — Declarations: OpenAILogo, AnthropicLogo, GoogleLogo, getProviderLogo, PROVIDER_NAMES, TierBadge
- [SalesforceIcon.tsx](<../services/frontend-web/components/icons/SalesforceIcon.tsx>) — Declarations: SalesforceIcon
- [SlackIcon.tsx](<../services/frontend-web/components/icons/SlackIcon.tsx>) — Declarations: SlackIcon
- [TeamsIcon.tsx](<../services/frontend-web/components/icons/TeamsIcon.tsx>) — Declarations: TeamsIcon
- [ZendeskIcon.tsx](<../services/frontend-web/components/icons/ZendeskIcon.tsx>) — Declarations: ZendeskIcon

## `services/frontend-web/components/integrations`

[Directory guide](<../services/frontend-web/components/integrations/directory.md>)

- [CreateIssueDialog.tsx](<../services/frontend-web/components/integrations/CreateIssueDialog.tsx>) — Called after issue is successfully created
- [LinearSettings.tsx](<../services/frontend-web/components/integrations/LinearSettings.tsx>) — Declarations: LinearSettings

## `services/frontend-web/components/playbooks`

[Directory guide](<../services/frontend-web/components/playbooks/directory.md>)

- [PlaybookEditor.tsx](<../services/frontend-web/components/playbooks/PlaybookEditor.tsx>) — Types whose config is reset to the type defaults on switch. send_email is deliberately excluded — switching away and back preserves its config (pinned behavior). The worker reads…
- [PlaybookExecutionsList.tsx](<../services/frontend-web/components/playbooks/PlaybookExecutionsList.tsx>) — Safe one-line summary of an action_log result (legacy rows may carry non-object results).
- [PlaybookTemplateCard.tsx](<../services/frontend-web/components/playbooks/PlaybookTemplateCard.tsx>) — Declarations: ActionTypeBadge, PlaybookTemplateCard

## `services/frontend-web/components/providers`

[Directory guide](<../services/frontend-web/components/providers/directory.md>)

- [QueryProvider.tsx](<../services/frontend-web/components/providers/QueryProvider.tsx>) — Declarations: QueryProvider

## `services/frontend-web/components/settings`

[Directory guide](<../services/frontend-web/components/settings/directory.md>)

- [AIReadinessCard.tsx](<../services/frontend-web/components/settings/AIReadinessCard.tsx>) — Declarations: AIReadinessCard
- [AISettingsGeneral.tsx](<../services/frontend-web/components/settings/AISettingsGeneral.tsx>) — Declarations: AISettingsGeneral
- [AISettingsProviders.tsx](<../services/frontend-web/components/settings/AISettingsProviders.tsx>) — Declarations: AISettingsProviders
- [AISettingsUsage.tsx](<../services/frontend-web/components/settings/AISettingsUsage.tsx>) — Declarations: AISettingsUsage
- [AsanaStatusSyncCard.tsx](<../services/frontend-web/components/settings/AsanaStatusSyncCard.tsx>) — Declarations: AsanaStatusSyncCard
- [ChurnLabelGateCard.tsx](<../services/frontend-web/components/settings/ChurnLabelGateCard.tsx>) — Declarations: ChurnLabelGateCard
- [ClassifierAccuracyCard.tsx](<../services/frontend-web/components/settings/ClassifierAccuracyCard.tsx>) — Per-classifier-type copy. Keeps the two PRD-mandated honesty clauses (critique #3) intact: (a) the model is "promoted only when it beats the keyword categorizer on your held-out…
- [HealthWeightsEditor.tsx](<../services/frontend-web/components/settings/HealthWeightsEditor.tsx>) — `crm` is intentionally excluded here: it round-trips through state and the save payload (see HealthWeights in lib/api/categories.ts) but is not yet an editable field in this UI.
- [HubSpotChurnLabelsCard.tsx](<../services/frontend-web/components/settings/HubSpotChurnLabelsCard.tsx>) — Declarations: HubSpotChurnLabelsCard
- [HubSpotWritebackCard.tsx](<../services/frontend-web/components/settings/HubSpotWritebackCard.tsx>) — Declarations: HubSpotWritebackCard
- [IntercomWritebackCard.tsx](<../services/frontend-web/components/settings/IntercomWritebackCard.tsx>) — Declarations: IntercomWritebackCard
- [JiraStatusSyncCard.tsx](<../services/frontend-web/components/settings/JiraStatusSyncCard.tsx>) — Declarations: JiraStatusSyncCard
- [RetrievalAccuracyCard.tsx](<../services/frontend-web/components/settings/RetrievalAccuracyCard.tsx>) — Declarations: RetrievalAccuracyCard
- [SalesforceChurnLabelsCard.tsx](<../services/frontend-web/components/settings/SalesforceChurnLabelsCard.tsx>) — Declarations: SalesforceChurnLabelsCard
- [SalesforceWritebackCard.tsx](<../services/frontend-web/components/settings/SalesforceWritebackCard.tsx>) — Declarations: SalesforceWritebackCard
- [SamlConfigCard.tsx](<../services/frontend-web/components/settings/SamlConfigCard.tsx>) — Declarations: SamlConfigCard
- [SentimentAccuracyCard.tsx](<../services/frontend-web/components/settings/SentimentAccuracyCard.tsx>) — Declarations: SentimentAccuracyCard
- [StatusMappingEditor.tsx](<../services/frontend-web/components/settings/StatusMappingEditor.tsx>) — Ordered list of the provider's foreign statuses/categories to map.
- [UsageChurnLabelsCard.tsx](<../services/frontend-web/components/settings/UsageChurnLabelsCard.tsx>) — Declarations: UsageChurnLabelsCard
- [ZendeskStatusSyncCard.tsx](<../services/frontend-web/components/settings/ZendeskStatusSyncCard.tsx>) — Declarations: ZendeskStatusSyncCard

## `services/frontend-web/components/settings/__tests__`

[Directory guide](<../services/frontend-web/components/settings/__tests__/directory.md>)

- [AsanaStatusSyncCard.test.tsx](<../services/frontend-web/components/settings/__tests__/AsanaStatusSyncCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [HubSpotChurnLabelsCard.test.tsx](<../services/frontend-web/components/settings/__tests__/HubSpotChurnLabelsCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [HubSpotWritebackCard.test.tsx](<../services/frontend-web/components/settings/__tests__/HubSpotWritebackCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [IntercomWritebackCard.test.tsx](<../services/frontend-web/components/settings/__tests__/IntercomWritebackCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [JiraStatusSyncCard.test.tsx](<../services/frontend-web/components/settings/__tests__/JiraStatusSyncCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [SalesforceChurnLabelsCard.test.tsx](<../services/frontend-web/components/settings/__tests__/SalesforceChurnLabelsCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [SalesforceWritebackCard.test.tsx](<../services/frontend-web/components/settings/__tests__/SalesforceWritebackCard.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [StatusMappingEditor.test.tsx](<../services/frontend-web/components/settings/__tests__/StatusMappingEditor.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ZendeskStatusSyncCard.test.tsx](<../services/frontend-web/components/settings/__tests__/ZendeskStatusSyncCard.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/components/shared`

[Directory guide](<../services/frontend-web/components/shared/directory.md>)

- [data-table.tsx](<../services/frontend-web/components/shared/data-table.tsx>) — Declarations: DataTable
- [page-skeletons.tsx](<../services/frontend-web/components/shared/page-skeletons.tsx>) — Declarations: DashboardSkeleton, DataTablePageSkeleton, FeedbacksPageSkeleton

## `services/frontend-web/components/ui`

[Directory guide](<../services/frontend-web/components/ui/directory.md>)

- [alert.tsx](<../services/frontend-web/components/ui/alert.tsx>) — Static/configuration artifact; inspect its consumer.
- [badge.tsx](<../services/frontend-web/components/ui/badge.tsx>) — Declarations: BadgeProps
- [breadcrumb.tsx](<../services/frontend-web/components/ui/breadcrumb.tsx>) — Static/configuration artifact; inspect its consumer.
- [button.tsx](<../services/frontend-web/components/ui/button.tsx>) — Declarations: ButtonProps
- [card.tsx](<../services/frontend-web/components/ui/card.tsx>) — Static/configuration artifact; inspect its consumer.
- [chart.tsx](<../services/frontend-web/components/ui/chart.tsx>) — Declarations: ChartConfig
- [checkbox.tsx](<../services/frontend-web/components/ui/checkbox.tsx>) — Static/configuration artifact; inspect its consumer.
- [collapsible.tsx](<../services/frontend-web/components/ui/collapsible.tsx>) — Static/configuration artifact; inspect its consumer.
- [dialog.tsx](<../services/frontend-web/components/ui/dialog.tsx>) — Static/configuration artifact; inspect its consumer.
- [dropdown-menu.tsx](<../services/frontend-web/components/ui/dropdown-menu.tsx>) — Static/configuration artifact; inspect its consumer.
- [input.tsx](<../services/frontend-web/components/ui/input.tsx>) — Static/configuration artifact; inspect its consumer.
- [label.tsx](<../services/frontend-web/components/ui/label.tsx>) — Static/configuration artifact; inspect its consumer.
- [popover.tsx](<../services/frontend-web/components/ui/popover.tsx>) — Static/configuration artifact; inspect its consumer.
- [progress.tsx](<../services/frontend-web/components/ui/progress.tsx>) — Static/configuration artifact; inspect its consumer.
- [scroll-area.tsx](<../services/frontend-web/components/ui/scroll-area.tsx>) — Static/configuration artifact; inspect its consumer.
- [select.tsx](<../services/frontend-web/components/ui/select.tsx>) — Static/configuration artifact; inspect its consumer.
- [separator.tsx](<../services/frontend-web/components/ui/separator.tsx>) — Static/configuration artifact; inspect its consumer.
- [sheet.tsx](<../services/frontend-web/components/ui/sheet.tsx>) — Static/configuration artifact; inspect its consumer.
- [sidebar.tsx](<../services/frontend-web/components/ui/sidebar.tsx>) — Static/configuration artifact; inspect its consumer.
- [skeleton.tsx](<../services/frontend-web/components/ui/skeleton.tsx>) — Static/configuration artifact; inspect its consumer.
- [switch.tsx](<../services/frontend-web/components/ui/switch.tsx>) — Static/configuration artifact; inspect its consumer.
- [table.tsx](<../services/frontend-web/components/ui/table.tsx>) — Static/configuration artifact; inspect its consumer.
- [tabs.tsx](<../services/frontend-web/components/ui/tabs.tsx>) — Static/configuration artifact; inspect its consumer.
- [textarea.tsx](<../services/frontend-web/components/ui/textarea.tsx>) — Static/configuration artifact; inspect its consumer.
- [toggle-group.tsx](<../services/frontend-web/components/ui/toggle-group.tsx>) — Static/configuration artifact; inspect its consumer.
- [toggle.tsx](<../services/frontend-web/components/ui/toggle.tsx>) — Static/configuration artifact; inspect its consumer.
- [tooltip.tsx](<../services/frontend-web/components/ui/tooltip.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/components/workflow`

[Directory guide](<../services/frontend-web/components/workflow/directory.md>)

- [BulkActionsBar.tsx](<../services/frontend-web/components/workflow/BulkActionsBar.tsx>) — Declarations: BulkActionsBar
- [FeedbackTimeline.tsx](<../services/frontend-web/components/workflow/FeedbackTimeline.tsx>) — Declarations: FeedbackTimeline
- [MarkdownContent.tsx](<../services/frontend-web/components/workflow/MarkdownContent.tsx>) — Declarations: MarkdownContent
- [MarkdownEditor.tsx](<../services/frontend-web/components/workflow/MarkdownEditor.tsx>) — Declarations: MarkdownEditor
- [NotesList.tsx](<../services/frontend-web/components/workflow/NotesList.tsx>) — Declarations: NotesList
- [WorkflowSection.tsx](<../services/frontend-web/components/workflow/WorkflowSection.tsx>) — Declarations: WorkflowSection

## `services/frontend-web/contexts`

[Directory guide](<../services/frontend-web/contexts/directory.md>)

- [AuthContext.tsx](<../services/frontend-web/contexts/AuthContext.tsx>) — Declarations: AuthProvider, useAuth
- [FeatureRequestsPageContext.tsx](<../services/frontend-web/contexts/FeatureRequestsPageContext.tsx>) — Declarations: FeatureRequestsPageProvider, useFeatureRequestsPage
- [FeedbackPageContext.tsx](<../services/frontend-web/contexts/FeedbackPageContext.tsx>) — Declarations: FeedbackPageProvider, useFeedbackPage
- [PainPointsPageContext.tsx](<../services/frontend-web/contexts/PainPointsPageContext.tsx>) — Declarations: PainPointsPageProvider, usePainPointsPage
- [RealtimeContext.tsx](<../services/frontend-web/contexts/RealtimeContext.tsx>) — Declarations: EventHandler, RealtimeContextType, RealtimeProvider, useRealtime
- [ThemeContext.tsx](<../services/frontend-web/contexts/ThemeContext.tsx>) — Declarations: ThemeProvider, useTheme
- [UrgentFeedbackPageContext.tsx](<../services/frontend-web/contexts/UrgentFeedbackPageContext.tsx>) — Declarations: UrgentFeedbackPageProvider, useUrgentFeedbackPage

## `services/frontend-web/contexts/__tests__`

[Directory guide](<../services/frontend-web/contexts/__tests__/directory.md>)

- [AuthContext.test.tsx](<../services/frontend-web/contexts/__tests__/AuthContext.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [ThemeContext.test.tsx](<../services/frontend-web/contexts/__tests__/ThemeContext.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/hooks`

[Directory guide](<../services/frontend-web/hooks/directory.md>)

- [use-mobile.tsx](<../services/frontend-web/hooks/use-mobile.tsx>) — Declarations: useIsMobile
- [useCopilotWebSocket.ts](<../services/frontend-web/hooks/useCopilotWebSocket.ts>) — Declarations: AssistantMessage, StructuredDataMessage, CopilotMessage, UseCopilotWebSocketOptions, UseCopilotWebSocketReturn, useCopilotWebSocket
- [useRealtimeEvents.ts](<../services/frontend-web/hooks/useRealtimeEvents.ts>) — Declarations: UseRealtimeEventsReturn, useRealtimeEvents
- [useRole.ts](<../services/frontend-web/hooks/useRole.ts>) — Declarations: useRole

## `services/frontend-web/lib`

[Directory guide](<../services/frontend-web/lib/directory.md>)

- [analytics.ts](<../services/frontend-web/lib/analytics.ts>) — Mixpanel Analytics Integration Tracks key user events for conversion optimization. Free tier: 20M events/month
- [api-client.ts](<../services/frontend-web/lib/api-client.ts>) — Declarations: apiClient, publicApiClient
- [asanaIssueWizard.ts](<../services/frontend-web/lib/asanaIssueWizard.ts>) — True when the backend responded 200 with `{warning: "duplicate", ...}` instead of a created task (feedback already linked to an Asana task and `force` was not set).
- [category-utils.ts](<../services/frontend-web/lib/category-utils.ts>) — Declarations: PAIN_POINT_CATEGORIES, FEATURE_REQUEST_CATEGORIES, URGENT_CATEGORIES, SEVERITY_STYLES, PRIORITY_STYLES, RESPONSE_TIME_STYLES
- [jiraIssueWizard.ts](<../services/frontend-web/lib/jiraIssueWizard.ts>) — True when the backend responded 200 with `{warning: "duplicate", ...}` instead of a created issue (feedback already linked to a Jira issue and `force` was not set).
- [notification-utils.ts](<../services/frontend-web/lib/notification-utils.ts>) — Declarations: TYPE_ICONS, TYPE_COLORS, timeAgo
- [oauthErrors.ts](<../services/frontend-web/lib/oauthErrors.ts>) — Shared OAuth error code → friendly message mapping. Used by both the integrations index page (`/settings/integrations`, which handles the Linear OAuth return) and per-provider…
- [oidcErrors.ts](<../services/frontend-web/lib/oidcErrors.ts>) — SSO error code → friendly message mapping, for the `?sso_error=` the backend appends when it redirects back to `/login` after a failed OIDC flow. Kept separate from…
- [pdf-export.ts](<../services/frontend-web/lib/pdf-export.ts>) — Resolve any CSS color (oklch, hsl, hex, etc.) to [r, g, b] by letting the browser do the conversion via a temporary element.
- [samlErrors.ts](<../services/frontend-web/lib/samlErrors.ts>) — SSO error code → friendly message mapping, for the `?sso_error=` the backend appends when it redirects back to `/login` after a failed SAML flow. Kept separate from…
- [utils.ts](<../services/frontend-web/lib/utils.ts>) — Static/configuration artifact; inspect its consumer.
- [workflow-utils.ts](<../services/frontend-web/lib/workflow-utils.ts>) — Declarations: WORKFLOW_STATUSES, WorkflowStatus, getStatusColor, getStatusLabel, getStatusIcon, getEventIcon

## `services/frontend-web/lib/__tests__`

[Directory guide](<../services/frontend-web/lib/__tests__/directory.md>)

- [api-client.test.ts](<../services/frontend-web/lib/__tests__/api-client.test.ts>) — Static/configuration artifact; inspect its consumer.
- [asanaIssueWizard.test.ts](<../services/frontend-web/lib/__tests__/asanaIssueWizard.test.ts>) — Static/configuration artifact; inspect its consumer.
- [jiraIssueWizard.test.ts](<../services/frontend-web/lib/__tests__/jiraIssueWizard.test.ts>) — Static/configuration artifact; inspect its consumer.
- [oidcErrors.test.ts](<../services/frontend-web/lib/__tests__/oidcErrors.test.ts>) — Static/configuration artifact; inspect its consumer.
- [samlErrors.test.ts](<../services/frontend-web/lib/__tests__/samlErrors.test.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/lib/api`

[Directory guide](<../services/frontend-web/lib/api/directory.md>)

- [account.ts](<../services/frontend-web/lib/api/account.ts>) — Download all personal data as a ZIP archive. Triggers a browser download automatically.
- [admin-orgs.ts](<../services/frontend-web/lib/api/admin-orgs.ts>) — Declarations: AdminOrg, AdminOrgUser, AdminOrgDetail, AdminOrgListResponse, adminOrgsAPI
- [admin-query-templates.ts](<../services/frontend-web/lib/api/admin-query-templates.ts>) — Declarations: QueryTemplate, QueryTemplateListResponse, QueryTemplateListParams, QueryTemplateUpdate, CopilotStats, adminQueryTemplatesAPI
- [admin-users.ts](<../services/frontend-web/lib/api/admin-users.ts>) — Declarations: AdminUser, AdminUserListResponse, AdminUserUpdate, adminUsersAPI
- [ai-corrections.ts](<../services/frontend-web/lib/api/ai-corrections.ts>) — Submit a correction or rating signal for an AI output. Available to all authenticated users.
- [ai-readiness.ts](<../services/frontend-web/lib/api/ai-readiness.ts>) — Declarations: AIReadiness, aiReadinessAPI
- [ai-settings.ts](<../services/frontend-web/lib/api/ai-settings.ts>) — Declarations: AIModels, AISettings, AISettingsUpdate, EmbeddingStatus, SentimentStatus, AIKey
- [analytics.ts](<../services/frontend-web/lib/api/analytics.ts>) — Declarations: TrendDataPoint, SentimentDistribution, SourceDistributionItem, TopItem, AnalyticsTrendsData, DateRange
- [anomalies.ts](<../services/frontend-web/lib/api/anomalies.ts>) — Declarations: SentimentAnomaly, AnomalyListResponse, anomaliesAPI
- [api-keys.ts](<../services/frontend-web/lib/api/api-keys.ts>) — Returned only on creation — includes the raw key shown exactly once.
- [asana.ts](<../services/frontend-web/lib/api/asana.ts>) — Declarations: AsanaConnectionStatus, AsanaConnectRequest, AsanaConnectResponse, AsanaDisconnectResponse, AsanaTestResponse, AsanaWorkspace
- [auth.ts](<../services/frontend-web/lib/api/auth.ts>) — Declarations: SignupData, LoginData, GoogleLoginData, GoogleSignupData, AuthResponse, UserResponse
- [automations.ts](<../services/frontend-web/lib/api/automations.ts>) — Who a `send_customer_email` action actually mails.
- [categories.ts](<../services/frontend-web/lib/api/categories.ts>) — All six weights the backend persists (`categories.py` `HealthWeightsUpdate`), summing to 100. `usage` is 0 until an operator opts in via Settings → AI → Health Score Weights.…
- [changelog.ts](<../services/frontend-web/lib/api/changelog.ts>) — Declarations: ChangelogEntry, ChangelogEntryAdmin, ChangelogListResponse, ChangelogAdminListResponse, ChangelogEntryUpdate, changelogAPI
- [churn-accuracy.ts](<../services/frontend-web/lib/api/churn-accuracy.ts>) — Format a 0.0–1.0 metric as a percentage string (e.g. "73%"). Returns "—" for null.
- [churn-analytics.ts](<../services/frontend-web/lib/api/churn-analytics.ts>) — Fetch churn cohort analytics for the given dimension and date range.
- [churn-events.ts](<../services/frontend-web/lib/api/churn-events.ts>) — Search by customer email (partial match). System admin endpoint only.
- [churn-label-gate.ts](<../services/frontend-web/lib/api/churn-label-gate.ts>) — Types + client for GET /api/v1/settings/ai/churn/label-gate (churn-label-gate-study aspect 2, M5.3 disclosure layer). Mirrors the backend's ChurnLabelGateResponse schema 1:1…
- [churn-suggestions.ts](<../services/frontend-web/lib/api/churn-suggestions.ts>) — Declarations: ChurnSuggestionStatus, ChurnSuggestionProvider, ChurnSuggestion, ChurnSuggestionsListParams, ChurnSuggestionsListResponse, SuggestionCohortFilter
- [classifier-accuracy.ts](<../services/frontend-web/lib/api/classifier-accuracy.ts>) — Types + client for GET /api/v1/settings/ai/classifier/accuracy and POST /api/v1/settings/ai/classifier/rollback (settings-api-and-accuracy-card aspect, M5.2). Mirrors the…
- [conversations.ts](<../services/frontend-web/lib/api/conversations.ts>) — Declarations: ConversationFolder, ConversationMessage, Conversation, ConversationListResponse, CreateConversationData, UpdateConversationData
- [copilot-actions.ts](<../services/frontend-web/lib/api/copilot-actions.ts>) — Outcome of `POST /api/v1/copilot/actions/execute` (backend `BulkActionSummary`). `errors[]` carries per-customer failures verbatim (e.g. the 20-tag cap message) and must never be…
- [copilot.ts](<../services/frontend-web/lib/api/copilot.ts>) — Static/configuration artifact; inspect its consumer.
- [customer-health.ts](<../services/frontend-web/lib/api/customer-health.ts>) — Declarations: CustomerHealthData, customerHealthAPI
- [customers.ts](<../services/frontend-web/lib/api/customers.ts>) — Compact CS-owner reference — mirrors backend `CustomerOwnerRef` (id + email only).
- [dashboard-v2.ts](<../services/frontend-web/lib/api/dashboard-v2.ts>) — Declarations: ComparisonData, TrendDataPoint, TrendResponse, ActivityFeedItem, ActivityFeedResponse, TeamMember
- [dashboard.ts](<../services/frontend-web/lib/api/dashboard.ts>) — Declarations: SentimentStats, PainPoint, FeatureRequest, CategoryCount, TopCategory, UrgentFeedback
- [embedding-accuracy.ts](<../services/frontend-web/lib/api/embedding-accuracy.ts>) — Types + client for GET /api/v1/settings/ai/embeddings/accuracy (retrieval-eval-card aspect, M5.4 disclosure layer). Mirrors the backend's RetrievalAccuracyResponse schema 1:1…
- [feedback-sources.ts](<../services/frontend-web/lib/api/feedback-sources.ts>) — Declarations: TriggerConfig, FieldMappingConfig, FeedbackSource, FeedbackSourceListResponse, CreateFeedbackSourceRequest, UpdateFeedbackSourceRequest
- [feedback.ts](<../services/frontend-web/lib/api/feedback.ts>) — Declarations: SourceMetadata, FeedbackItem, PainPointCategory, PainPointSeverity, FeatureRequestCategory, FeatureRequestPriority
- [hubspot.ts](<../services/frontend-web/lib/api/hubspot.ts>) — Declarations: HubSpotConnectionStatus, HubSpotConnectResponse, HubSpotTestResponse, HubSpotDisconnectResponse, HubSpotWritebackConfig, HubSpotWritebackResponse
- [insights.ts](<../services/frontend-web/lib/api/insights.ts>) — Declarations: InsightItem, WeeklyInsight, WeeklyInsightListResponse, insightsAPI
- [integrations.ts](<../services/frontend-web/lib/api/integrations.ts>) — Declarations: Integration, OAuthConnectResponse, IntegrationListResponse, CreateSlackWebhookData, CreateDiscordWebhookData, TeamsWebhookCreateData
- [intercom.ts](<../services/frontend-web/lib/api/intercom.ts>) — Declarations: IntercomConnectionStatus, IntercomConnectRequest, IntercomConnectResponse, IntercomDisconnectResponse, IntercomWritebackConfig, IntercomWritebackResponse
- [invites.ts](<../services/frontend-web/lib/api/invites.ts>) — Get invite details by token (public endpoint)
- [issueDraft.ts](<../services/frontend-web/lib/api/issueDraft.ts>) — Typed error for the issue-draft endpoint. Carries the HTTP status so callers can distinguish 409 (no LLM configured) from other failures (404 cross-org feedback, 502 bad/failed…
- [jira.ts](<../services/frontend-web/lib/api/jira.ts>) — Declarations: JiraConnectionStatus, JiraConnectRequest, JiraConnectResponse, JiraDisconnectResponse, JiraTestResponse, JiraProject
- [linear.ts](<../services/frontend-web/lib/api/linear.ts>) — Declarations: LinearConnectionStatus, LinearTeam, LinearProject, LinearLabel, LinearTeamMapping, LinearStatusMapping
- [notifications.ts](<../services/frontend-web/lib/api/notifications.ts>) — Declarations: NotificationItem, NotificationListResponse, AlertPreference, RetentionTypeItem, RetentionInfo, notificationsAPI
- [oidc.ts](<../services/frontend-web/lib/api/oidc.ts>) — Declarations: OidcStatus, OidcConfig, OidcConfigUpdate, getOidcStatus, getOidcConfig, putOidcConfig
- [organization.ts](<../services/frontend-web/lib/api/organization.ts>) — Declarations: Organization, OrganizationStats, UpdateOrganizationData, organizationAPI
- [outreach.ts](<../services/frontend-web/lib/api/outreach.ts>) — Typed error for the outreach draft endpoint. Carries the HTTP status so callers can distinguish 409 (no LLM configured) from 422 bad input or 502 provider failure and show an…
- [playbooks.ts](<../services/frontend-web/lib/api/playbooks.ts>) — Config for `notify`. Key names match exactly what the worker `_handle_notify` reads: `channel`, `target` (advisory — recorded in the result, not resolved to a channel), `message`.
- [preferences.ts](<../services/frontend-web/lib/api/preferences.ts>) — Declarations: AlertChannels, Preferences, PreferencesUpdate, preferencesAPI
- [reports.ts](<../services/frontend-web/lib/api/reports.ts>) — Declarations: ReportType, ReportSectionData, ReportSectionChart, ReportSection, Report, ReportsListResponse
- [responses.ts](<../services/frontend-web/lib/api/responses.ts>) — Declarations: ResponseTemplate, FeedbackResponseRecord, ResponseSettings, ResponseUsage, ToneOption, CreateTemplateRequest
- [salesforce.ts](<../services/frontend-web/lib/api/salesforce.ts>) — Declarations: SalesforceConnectionStatus, SalesforceConnectUrlResponse, SalesforceDisconnectResponse, SalesforceTestResponse, SalesforceWritebackConfig, SalesforceWritebackResponse
- [saml.ts](<../services/frontend-web/lib/api/saml.ts>) — Declarations: SamlStatus, SamlConfig, SamlConfigUpdate, getSamlStatus, getSamlConfig, putSamlConfig
- [saved-views.ts](<../services/frontend-web/lib/api/saved-views.ts>) — Declarations: SavedView, SavedViewCreateData, savedViewsAPI
- [scheduled-reports.ts](<../services/frontend-web/lib/api/scheduled-reports.ts>) — Declarations: ReportCadence, ScheduledReport, ScheduledReportCreatePayload, ScheduledReportUpdatePayload, scheduledReportsAPI
- [sentiment-accuracy.ts](<../services/frontend-web/lib/api/sentiment-accuracy.ts>) — Types + client for GET /api/v1/settings/ai/sentiment/accuracy (eval-harness-and-card aspect, M5.1 disclosure layer). Mirrors the backend's SentimentAccuracyResponse schema 1:1…
- [team.ts](<../services/frontend-web/lib/api/team.ts>) — Get all team members for the organization
- [webhooks.ts](<../services/frontend-web/lib/api/webhooks.ts>) — Declarations: WebhookEndpoint, WebhookDelivery, CreateWebhookRequest, CreateWebhookResponse, UpdateWebhookRequest, TestWebhookResult
- [workflow.ts](<../services/frontend-web/lib/api/workflow.ts>) — Declarations: WorkflowFeedbackItem, WorkflowOverviewResponse, TimelineEvent, FeedbackNote, AssignmentRule, WorkflowOverviewFilters
- [zendesk.ts](<../services/frontend-web/lib/api/zendesk.ts>) — Declarations: ZendeskConnectionStatus, ZendeskConnectRequest, ZendeskConnectResponse, ZendeskDisconnectResponse, ZendeskTestResponse, ZendeskSyncResponse

## `services/frontend-web/lib/api/__tests__`

[Directory guide](<../services/frontend-web/lib/api/__tests__/directory.md>)

- [ai-settings.category.test.ts](<../services/frontend-web/lib/api/__tests__/ai-settings.category.test.ts>) — Static/configuration artifact; inspect its consumer.
- [ai-settings.urgency.test.ts](<../services/frontend-web/lib/api/__tests__/ai-settings.urgency.test.ts>) — Static/configuration artifact; inspect its consumer.
- [ai-settings.usageChurnLabels.test.ts](<../services/frontend-web/lib/api/__tests__/ai-settings.usageChurnLabels.test.ts>) — Static/configuration artifact; inspect its consumer.
- [asana.test.ts](<../services/frontend-web/lib/api/__tests__/asana.test.ts>) — Static/configuration artifact; inspect its consumer.
- [automations.actionSupport.test.ts](<../services/frontend-web/lib/api/__tests__/automations.actionSupport.test.ts>) — Static/configuration artifact; inspect its consumer.
- [automations.sendCustomerEmail.test.ts](<../services/frontend-web/lib/api/__tests__/automations.sendCustomerEmail.test.ts>) — Static/configuration artifact; inspect its consumer.
- [churn-label-gate.test.ts](<../services/frontend-web/lib/api/__tests__/churn-label-gate.test.ts>) — Static/configuration artifact; inspect its consumer.
- [churn-suggestions.provider.test.ts](<../services/frontend-web/lib/api/__tests__/churn-suggestions.provider.test.ts>) — Static/configuration artifact; inspect its consumer.
- [classifier-accuracy.test.ts](<../services/frontend-web/lib/api/__tests__/classifier-accuracy.test.ts>) — Static/configuration artifact; inspect its consumer.
- [customers.bulk.test.ts](<../services/frontend-web/lib/api/__tests__/customers.bulk.test.ts>) — Static/configuration artifact; inspect its consumer.
- [customers.outreach.test.ts](<../services/frontend-web/lib/api/__tests__/customers.outreach.test.ts>) — Static/configuration artifact; inspect its consumer.
- [customers.usage.test.ts](<../services/frontend-web/lib/api/__tests__/customers.usage.test.ts>) — Static/configuration artifact; inspect its consumer.
- [hubspot.test.ts](<../services/frontend-web/lib/api/__tests__/hubspot.test.ts>) — Static/configuration artifact; inspect its consumer.
- [integrations.teams.test.ts](<../services/frontend-web/lib/api/__tests__/integrations.teams.test.ts>) — Static/configuration artifact; inspect its consumer.
- [intercom.test.ts](<../services/frontend-web/lib/api/__tests__/intercom.test.ts>) — Static/configuration artifact; inspect its consumer.
- [issueDraft.test.ts](<../services/frontend-web/lib/api/__tests__/issueDraft.test.ts>) — Static/configuration artifact; inspect its consumer.
- [jira.test.ts](<../services/frontend-web/lib/api/__tests__/jira.test.ts>) — Static/configuration artifact; inspect its consumer.
- [linear.test.ts](<../services/frontend-web/lib/api/__tests__/linear.test.ts>) — Static/configuration artifact; inspect its consumer.
- [oidc.test.ts](<../services/frontend-web/lib/api/__tests__/oidc.test.ts>) — Static/configuration artifact; inspect its consumer.
- [outreach.bulk.test.ts](<../services/frontend-web/lib/api/__tests__/outreach.bulk.test.ts>) — Static/configuration artifact; inspect its consumer.
- [outreach.test.ts](<../services/frontend-web/lib/api/__tests__/outreach.test.ts>) — Static/configuration artifact; inspect its consumer.
- [playbooks.actionTypes.test.ts](<../services/frontend-web/lib/api/__tests__/playbooks.actionTypes.test.ts>) — Static/configuration artifact; inspect its consumer.
- [playbooks.runBatch.test.ts](<../services/frontend-web/lib/api/__tests__/playbooks.runBatch.test.ts>) — Static/configuration artifact; inspect its consumer.
- [playbooks.sendEmail.test.ts](<../services/frontend-web/lib/api/__tests__/playbooks.sendEmail.test.ts>) — Static/configuration artifact; inspect its consumer.
- [salesforce.test.ts](<../services/frontend-web/lib/api/__tests__/salesforce.test.ts>) — Static/configuration artifact; inspect its consumer.
- [saml.test.ts](<../services/frontend-web/lib/api/__tests__/saml.test.ts>) — Static/configuration artifact; inspect its consumer.
- [scheduled-reports.test.ts](<../services/frontend-web/lib/api/__tests__/scheduled-reports.test.ts>) — Static/configuration artifact; inspect its consumer.
- [zendesk.test.ts](<../services/frontend-web/lib/api/__tests__/zendesk.test.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/lib/constants`

[Directory guide](<../services/frontend-web/lib/constants/directory.md>)

- [churn.ts](<../services/frontend-web/lib/constants/churn.ts>) — Returns a risk band string based on churn probability (0.0–1.0). Bands: <0.30 low, <0.50 medium, <0.70 high, >=0.70 critical.
- [segments.ts](<../services/frontend-web/lib/constants/segments.ts>) — Rule-based customer segment slugs (segment-engine contract). `unsegmented` (or `null` from the API) means the engine hasn't computed a segment for this customer yet — not an error…
- [status-sync-keys.ts](<../services/frontend-web/lib/constants/status-sync-keys.ts>) — Hardcoded canonical foreign-key lists for each inbound status-sync provider's `StatusMappingEditor` (mapping-editor aspect). No discovery endpoint — these mirror the backend's…
- [workflow-status.ts](<../services/frontend-web/lib/constants/workflow-status.ts>) — Rereflect's canonical feedback workflow statuses — the mapping *target* shared by every inbound status-sync integration (Linear, Jira, Asana, Zendesk). Relocated out of…

## `services/frontend-web/lib/constants/__tests__`

[Directory guide](<../services/frontend-web/lib/constants/__tests__/directory.md>)

- [workflow-status.test.ts](<../services/frontend-web/lib/constants/__tests__/workflow-status.test.ts>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/lib/utils`

[Directory guide](<../services/frontend-web/lib/utils/directory.md>)

- [relative-time.ts](<../services/frontend-web/lib/utils/relative-time.ts>) — Declarations: getRelativeTime

## `services/frontend-web/public`

[Directory guide](<../services/frontend-web/public/directory.md>)

- [theme-init.js](<../services/frontend-web/public/theme-init.js>) — Static/configuration artifact; inspect its consumer.

## `services/frontend-web/public/images`

[Directory guide](<../services/frontend-web/public/images/directory.md>)

- [logo-white.png](<../services/frontend-web/public/images/logo-white.png>) — Static/configuration artifact; inspect its consumer.
- [logo.png](<../services/frontend-web/public/images/logo.png>) — Static/configuration artifact; inspect its consumer.
- [logo.svg](<../services/frontend-web/public/images/logo.svg>) — Static/configuration artifact; inspect its consumer.

## `services/integration-service`

[Directory guide](<../services/integration-service/directory.md>)

- [README.md](<../services/integration-service/README.md>) — Integration Service: For integrations requiring OAuth (Intercom, Salesforce, HubSpot):

## `services/landing-web`

[Directory guide](<../services/landing-web/directory.md>)

- [.env.example](<../services/landing-web/.env.example>) — Static/configuration artifact; inspect its consumer.
- [Dockerfile](<../services/landing-web/Dockerfile>) — Static/configuration artifact; inspect its consumer.
- [docker-entrypoint.sh](<../services/landing-web/docker-entrypoint.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [next.config.ts](<../services/landing-web/next.config.ts>) — Static/configuration artifact; inspect its consumer.
- [nginx.conf](<../services/landing-web/nginx.conf>) — Static/configuration artifact; inspect its consumer.
- [nginx.conf.template](<../services/landing-web/nginx.conf.template>) — Static/configuration artifact; inspect its consumer.
- [package.json](<../services/landing-web/package.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [postcss.config.js](<../services/landing-web/postcss.config.js>) — Static/configuration artifact; inspect its consumer.
- [railway.toml](<../services/landing-web/railway.toml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [tailwind.config.ts](<../services/landing-web/tailwind.config.ts>) — /*.{js,ts,jsx,tsx,mdx}", "./components/*
- [tsconfig.json](<../services/landing-web/tsconfig.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [vitest.config.ts](<../services/landing-web/vitest.config.ts>) — Static/configuration artifact; inspect its consumer.
- [vitest.setup.ts](<../services/landing-web/vitest.setup.ts>) — Static/configuration artifact; inspect its consumer.

## `services/landing-web/__tests__`

[Directory guide](<../services/landing-web/__tests__/directory.md>)

No immediate baseline/preparation files.

## `services/landing-web/__tests__/landing`

[Directory guide](<../services/landing-web/__tests__/landing/directory.md>)

- [FAQ.test.tsx](<../services/landing-web/__tests__/landing/FAQ.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [Footer.test.tsx](<../services/landing-web/__tests__/landing/Footer.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [Navigation.test.tsx](<../services/landing-web/__tests__/landing/Navigation.test.tsx>) — Static/configuration artifact; inspect its consumer.
- [smoke.test.tsx](<../services/landing-web/__tests__/landing/smoke.test.tsx>) — Static/configuration artifact; inspect its consumer.

## `services/landing-web/app`

[Directory guide](<../services/landing-web/app/directory.md>)

- [globals.css](<../services/landing-web/app/globals.css>) — Static/configuration artifact; inspect its consumer.
- [icon.svg](<../services/landing-web/app/icon.svg>) — Static/configuration artifact; inspect its consumer.
- [landing.css](<../services/landing-web/app/landing.css>) — Static/configuration artifact; inspect its consumer.
- [layout.tsx](<../services/landing-web/app/layout.tsx>) — Declarations: metadata, RootLayout
- [page.tsx](<../services/landing-web/app/page.tsx>) — Declarations: metadata, Home

## `services/landing-web/app/blog`

[Directory guide](<../services/landing-web/app/blog/directory.md>)

- [page.tsx](<../services/landing-web/app/blog/page.tsx>) — Declarations: metadata, BlogPage

## `services/landing-web/app/blog/[slug]`

[Directory guide](<../services/landing-web/app/blog/[slug]/directory.md>)

- [page.tsx](<../services/landing-web/app/blog/[slug]/page.tsx>) — Declarations: generateStaticParams, generateMetadata, BlogPostPage

## `services/landing-web/app/integrations`

[Directory guide](<../services/landing-web/app/integrations/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/page.tsx>) — Declarations: IntegrationsPage

## `services/landing-web/app/integrations/asana`

[Directory guide](<../services/landing-web/app/integrations/asana/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/asana/page.tsx>) — Declarations: metadata, AsanaIntegrationPage

## `services/landing-web/app/integrations/email`

[Directory guide](<../services/landing-web/app/integrations/email/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/email/page.tsx>) — Declarations: metadata, EmailIntegrationPage

## `services/landing-web/app/integrations/hubspot`

[Directory guide](<../services/landing-web/app/integrations/hubspot/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/hubspot/page.tsx>) — Declarations: metadata, HubSpotIntegrationPage

## `services/landing-web/app/integrations/intercom`

[Directory guide](<../services/landing-web/app/integrations/intercom/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/intercom/page.tsx>) — Declarations: metadata, IntercomIntegrationPage

## `services/landing-web/app/integrations/jira`

[Directory guide](<../services/landing-web/app/integrations/jira/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/jira/page.tsx>) — Declarations: metadata, JiraIntegrationPage

## `services/landing-web/app/integrations/linear`

[Directory guide](<../services/landing-web/app/integrations/linear/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/linear/page.tsx>) — Declarations: metadata, LinearIntegrationPage

## `services/landing-web/app/integrations/salesforce`

[Directory guide](<../services/landing-web/app/integrations/salesforce/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/salesforce/page.tsx>) — Declarations: metadata, SalesforceIntegrationPage

## `services/landing-web/app/integrations/slack`

[Directory guide](<../services/landing-web/app/integrations/slack/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/slack/page.tsx>) — Declarations: metadata, SlackIntegrationPage

## `services/landing-web/app/integrations/teams`

[Directory guide](<../services/landing-web/app/integrations/teams/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/teams/page.tsx>) — Declarations: metadata, TeamsIntegrationPage

## `services/landing-web/app/integrations/zendesk`

[Directory guide](<../services/landing-web/app/integrations/zendesk/directory.md>)

- [page.tsx](<../services/landing-web/app/integrations/zendesk/page.tsx>) — Declarations: metadata, ZendeskIntegrationPage

## `services/landing-web/app/privacy`

[Directory guide](<../services/landing-web/app/privacy/directory.md>)

- [page.tsx](<../services/landing-web/app/privacy/page.tsx>) — Declarations: metadata, PrivacyPolicyPage

## `services/landing-web/app/terms`

[Directory guide](<../services/landing-web/app/terms/directory.md>)

- [page.tsx](<../services/landing-web/app/terms/page.tsx>) — Declarations: metadata, TermsOfServicePage

## `services/landing-web/components`

[Directory guide](<../services/landing-web/components/directory.md>)

No immediate baseline/preparation files.

## `services/landing-web/components/icons`

[Directory guide](<../services/landing-web/components/icons/directory.md>)

- [AsanaIcon.tsx](<../services/landing-web/components/icons/AsanaIcon.tsx>) — Declarations: AsanaIcon
- [EmailIcon.tsx](<../services/landing-web/components/icons/EmailIcon.tsx>) — Declarations: EmailIcon
- [HubSpotIcon.tsx](<../services/landing-web/components/icons/HubSpotIcon.tsx>) — Declarations: HubSpotIcon
- [IntercomIcon.tsx](<../services/landing-web/components/icons/IntercomIcon.tsx>) — Declarations: IntercomIcon
- [JiraIcon.tsx](<../services/landing-web/components/icons/JiraIcon.tsx>) — Declarations: JiraIcon
- [LinearIcon.tsx](<../services/landing-web/components/icons/LinearIcon.tsx>) — Declarations: LinearIcon
- [SalesforceIcon.tsx](<../services/landing-web/components/icons/SalesforceIcon.tsx>) — Declarations: SalesforceIcon
- [SlackIcon.tsx](<../services/landing-web/components/icons/SlackIcon.tsx>) — Declarations: SlackIcon
- [TeamsIcon.tsx](<../services/landing-web/components/icons/TeamsIcon.tsx>) — Declarations: TeamsIcon
- [ZendeskIcon.tsx](<../services/landing-web/components/icons/ZendeskIcon.tsx>) — Declarations: ZendeskIcon

## `services/landing-web/components/landing`

[Directory guide](<../services/landing-web/components/landing/directory.md>)

- [CTA.tsx](<../services/landing-web/components/landing/CTA.tsx>) — Declarations: CTA
- [Comparison.tsx](<../services/landing-web/components/landing/Comparison.tsx>) — Declarations: Comparison
- [Console.tsx](<../services/landing-web/components/landing/Console.tsx>) — Declarations: Console
- [FAQ.tsx](<../services/landing-web/components/landing/FAQ.tsx>) — Declarations: FAQ
- [Features.tsx](<../services/landing-web/components/landing/Features.tsx>) — Declarations: Features
- [Footer.tsx](<../services/landing-web/components/landing/Footer.tsx>) — Declarations: Footer
- [Hero.tsx](<../services/landing-web/components/landing/Hero.tsx>) — The specimen record shown in FIG. 01 — one feedback item, fully classified.
- [IntegrationPage.tsx](<../services/landing-web/components/landing/IntegrationPage.tsx>) — Declarations: IntegrationPage
- [IntegrationTile.tsx](<../services/landing-web/components/landing/IntegrationTile.tsx>) — Declarations: IntegrationTile
- [LegalPage.tsx](<../services/landing-web/components/landing/LegalPage.tsx>) — Declarations: LegalSection, LegalPage
- [Nav.tsx](<../services/landing-web/components/landing/Nav.tsx>) — Declarations: Nav
- [PageHero.tsx](<../services/landing-web/components/landing/PageHero.tsx>) — Trailing fragment of the headline, rendered in the accent colour.
- [Pipeline.tsx](<../services/landing-web/components/landing/Pipeline.tsx>) — Declarations: Pipeline
- [RevealGrid.tsx](<../services/landing-web/components/landing/RevealGrid.tsx>) — Declarations: RevealGrid
- [SubpageCTA.tsx](<../services/landing-web/components/landing/SubpageCTA.tsx>) — Declarations: SubpageCTA

## `services/landing-web/lib`

[Directory guide](<../services/landing-web/lib/directory.md>)

- [blog.ts](<../services/landing-web/lib/blog.ts>) — Declarations: BlogSection, BlogPost, getAllPosts, getPostBySlug, getRelatedPosts
- [integrations.ts](<../services/landing-web/lib/integrations.ts>) — Declarations: IntegrationStep, IntegrationFeature, IntegrationUseCase, IntegrationFAQ, IntegrationSetupStep, Integration

## `services/landing-web/lib/blog-posts`

[Directory guide](<../services/landing-web/lib/blog-posts/directory.md>)

- [batch1.ts](<../services/landing-web/lib/blog-posts/batch1.ts>) — Declarations: batch1
- [batch2.ts](<../services/landing-web/lib/blog-posts/batch2.ts>) — Declarations: batch2
- [batch3.ts](<../services/landing-web/lib/blog-posts/batch3.ts>) — Declarations: batch3
- [batch4.ts](<../services/landing-web/lib/blog-posts/batch4.ts>) — Declarations: batch4
- [batch5.ts](<../services/landing-web/lib/blog-posts/batch5.ts>) — Declarations: batch5
- [batch6.ts](<../services/landing-web/lib/blog-posts/batch6.ts>) — Declarations: batch6

## `services/landing-web/lib/landing`

[Directory guide](<../services/landing-web/lib/landing/directory.md>)

- [gsap.ts](<../services/landing-web/lib/landing/gsap.ts>) — Static/configuration artifact; inspect its consumer.
- [motion.ts](<../services/landing-web/lib/landing/motion.ts>) — Motion vocabulary for the schematic landing. The rules are deliberately narrow: short durations, expo/quart easing, small translations, and no blur, scale-bounce or glow. Anything…

## `services/landing-web/public`

[Directory guide](<../services/landing-web/public/directory.md>)

- [robots.txt](<../services/landing-web/public/robots.txt>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [sitemap.xml](<../services/landing-web/public/sitemap.xml>) — Static/configuration artifact; inspect its consumer.

## `services/landing-web/public/images`

[Directory guide](<../services/landing-web/public/images/directory.md>)

- [logo-white.png](<../services/landing-web/public/images/logo-white.png>) — Static/configuration artifact; inspect its consumer.
- [logo.png](<../services/landing-web/public/images/logo.png>) — Static/configuration artifact; inspect its consumer.
- [logo.svg](<../services/landing-web/public/images/logo.svg>) — Static/configuration artifact; inspect its consumer.

## `services/worker-service`

[Directory guide](<../services/worker-service/directory.md>)

- [.env.example](<../services/worker-service/.env.example>) — Static/configuration artifact; inspect its consumer.
- [Dockerfile](<../services/worker-service/Dockerfile>) — Static/configuration artifact; inspect its consumer.
- [README.md](<../services/worker-service/README.md>) — Worker Service
- [pytest.ini](<../services/worker-service/pytest.ini>) — Static/configuration artifact; inspect its consumer.
- [railway.toml](<../services/worker-service/railway.toml>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [requirements.txt](<../services/worker-service/requirements.txt>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.
- [start.sh](<../services/worker-service/start.sh>) — Service tooling or dependency specification; read invocation, environment, and version requirements before use.

## `services/worker-service/src`

[Directory guide](<../services/worker-service/src/directory.md>)

- [__init__.py](<../services/worker-service/src/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [cache.py](<../services/worker-service/src/cache.py>) — Cache invalidation utility for worker-service. Connects to Redis DB 2 (application cache) to invalidate stale entries when worker tasks create or modify feedback items.
- [celery_app.py](<../services/worker-service/src/celery_app.py>) — Celery application configuration. Uses Redis Streams as the message broker.
- [config.py](<../services/worker-service/src/config.py>) — Worker service configuration. Uses Redis logical databases for isolation: - DB 0: Celery broker (task queue) - DB 1: Session storage (reserved for backend-api) - DB 2: Application cache…
- [database.py](<../services/worker-service/src/database.py>) — Database session management for worker service. Shares the same database as backend-api.
- [email.py](<../services/worker-service/src/email.py>) — Email service for worker-service. Duplicates core Resend email logic for sending weekly digests.
- [email_parser.py](<../services/worker-service/src/email_parser.py>) — Smart email body parsing for inbound email feedback. Strips forwarding headers, signatures, quoted replies, and HTML to extract clean feedback text from forwarded emails. NOTE: This is a…
- [llm_client.py](<../services/worker-service/src/llm_client.py>) — LLM client — provider-agnostic replacement for openai_client.py. Provides the same function signatures as openai_client.py but routes calls through the LLM factory with per-org…
- [notification_dispatch.py](<../services/worker-service/src/notification_dispatch.py>) — Notification dispatch service. Routes alerts to the correct channels (in-app, Slack, email digest) based on per-user alert preferences.
- [plans.py](<../services/worker-service/src/plans.py>) — Plan configuration for worker service. Mirrors the feedback limits from backend-api/src/config/plans.py.

## `services/worker-service/src/adapters`

[Directory guide](<../services/worker-service/src/adapters/directory.md>)

- [__init__.py](<../services/worker-service/src/adapters/__init__.py>) — Source adapters for handling provider-specific event processing.
- [base.py](<../services/worker-service/src/adapters/base.py>) — Base adapter class for source-specific event handling.
- [email.py](<../services/worker-service/src/adapters/email.py>) — Email adapter for handling inbound email webhook events.
- [intercom.py](<../services/worker-service/src/adapters/intercom.py>) — Intercom adapter for handling Intercom webhook events.
- [intercom_parts.py](<../services/worker-service/src/adapters/intercom_parts.py>) — Reply/rating extraction from Intercom *conversation* objects (pull path). The webhook adapter (adapters/intercom.py) parses event-shaped payloads; this module parses the conversation object…
- [slack.py](<../services/worker-service/src/adapters/slack.py>) — Slack adapter for handling Slack Events API events.
- [webhook.py](<../services/worker-service/src/adapters/webhook.py>) — Generic webhook adapter for handling custom webhook events.
- [zendesk.py](<../services/worker-service/src/adapters/zendesk.py>) — Zendesk adapter for handling Zendesk ticket events (pull + webhook). Shared ingestion core consumed by both the ingestion-pull and ingestion-webhook aspects. See…

## `services/worker-service/src/clients`

[Directory guide](<../services/worker-service/src/clients/directory.md>)

- [__init__.py](<../services/worker-service/src/clients/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [asana.py](<../services/worker-service/src/clients/asana.py>) — Asana REST API client for the inbound status-sync worker task (asana-status-sync/asana-client-get-task). The worker cannot import backend-api, so this is a standalone mirror of…
- [hubspot.py](<../services/worker-service/src/clients/hubspot.py>) — HubSpot CRM HTTP client for the hubspot-sync worker task. Pulls Contacts, Companies, and Deals from HubSpot CRM v3 API. Handles pagination (cursor-based), 429 rate limits (Retry-After…
- [intercom.py](<../services/worker-service/src/clients/intercom.py>) — Intercom REST client for the conversation-pull and write-back paths. Mirrors src/clients/zendesk.py in error taxonomy and lifecycle. Lives in worker-service because worker-service cannot…
- [jira.py](<../services/worker-service/src/clients/jira.py>) — Jira Cloud REST API client for the inbound status-sync worker task (jira-status-sync/inbound-status-sync, Phase 4). The worker cannot import backend-api, so this is a standalone mirror of…
- [salesforce.py](<../services/worker-service/src/clients/salesforce.py>) — Salesforce REST/SOQL HTTP client for the salesforce-sync worker task. Mints a short-lived access_token from a stored OAuth refresh_token before each run (web-server OAuth 2.0 — mirrors…
- [zendesk.py](<../services/worker-service/src/clients/zendesk.py>) — Zendesk REST/incremental-export HTTP client for the zendesk-sync worker task (ingestion-pull aspect). Thin httpx wrapper, HTTP Basic auth using the token-access convention (`{email}/token`,…

## `services/worker-service/src/llm`

[Directory guide](<../services/worker-service/src/llm/directory.md>)

- [__init__.py](<../services/worker-service/src/llm/__init__.py>) — LLM abstraction layer for the worker service. Provides a provider-agnostic interface for calling OpenAI, Anthropic, and Google models, with automatic retry and fallback chain support.…
- [base.py](<../services/worker-service/src/llm/base.py>) — Abstract base class for LLM providers.
- [factory.py](<../services/worker-service/src/llm/factory.py>) — LLM Provider Factory — creates provider instances by name.
- [fallback.py](<../services/worker-service/src/llm/fallback.py>) — FallbackChain — orchestrates retry logic for LLM calls. Strategy: 1. Try primary provider (org's BYOK key) 2. On transient failure (429, 5xx, timeout): retry once with 2s backoff 3. If…
- [org_resolver.py](<../services/worker-service/src/llm/org_resolver.py>) — Resolves per-org LLM configuration: provider, model, API key. Strictly BYOK (bring-your-own-key): reads OrgApiKey from the database. If no valid BYOK key exists for an org, AI is disabled…
- [pricing.py](<../services/worker-service/src/llm/pricing.py>) — LLM pricing table and cost estimation utilities. Prices are in USD per 1M tokens (input/output). Cost is returned in cents.
- [prompts.py](<../services/worker-service/src/llm/prompts.py>) — All LLM prompts used by the worker service. Moved from openai_client.py — kept identical to preserve existing behavior.
- [types.py](<../services/worker-service/src/llm/types.py>) — Shared dataclasses for the LLM abstraction layer.

## `services/worker-service/src/llm/providers`

[Directory guide](<../services/worker-service/src/llm/providers/directory.md>)

- [__init__.py](<../services/worker-service/src/llm/providers/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [anthropic.py](<../services/worker-service/src/llm/providers/anthropic.py>) — Anthropic LLM provider implementation. Uses messages.create API. System messages are extracted into the separate 'system' parameter. JSON mode is handled via prompt instruction + stripping…
- [google.py](<../services/worker-service/src/llm/providers/google.py>) — Google Generative AI (Gemini) LLM provider implementation. Uses google-generativeai SDK. JSON mode is handled via response_mime_type="application/json". System messages are passed as…
- [openai.py](<../services/worker-service/src/llm/providers/openai.py>) — OpenAI LLM provider implementation. Uses chat.completions.create with json_object response format for JSON mode. System messages are kept in the messages array (OpenAI's native format).
- [openai_compatible.py](<../services/worker-service/src/llm/providers/openai_compatible.py>) — OpenAI-compatible LLM provider. Wraps the OpenAI client against a custom base_url, enabling local / offline models (Ollama, LM Studio, vLLM, etc.) as drop-in replacements. The api_key is…

## `services/worker-service/src/models`

[Directory guide](<../services/worker-service/src/models/directory.md>)

- [__init__.py](<../services/worker-service/src/models/__init__.py>) — Database models for worker service. Imports models from backend-api to ensure consistency. Note: In production, these should be in a shared package. For now, we duplicate the essential…
- [automation_execution.py](<../services/worker-service/src/models/automation_execution.py>) — AutomationExecution — lightweight SQLAlchemy mirror for worker-service. The full model lives in backend-api. This mirror is used by src/tasks/automation.py for the weekly purge task. No…
- [automation_rule.py](<../services/worker-service/src/models/automation_rule.py>) — AutomationRule — lightweight SQLAlchemy mirror for worker-service. The full model + engine live in backend-api (`services/backend-api/src/models/automation_rule.py`). This mirror is used…

## `services/worker-service/src/services`

[Directory guide](<../services/worker-service/src/services/directory.md>)

- [__init__.py](<../services/worker-service/src/services/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [asana_adapter.py](<../services/worker-service/src/services/asana_adapter.py>) — Pure Asana task-state -> status_sync_core category adapter (no I/O). Slice 1 maps only the boolean `completed` field: completed True -> "done" (status_sync_core resolves -> resolved by…
- [automation_churn_trigger.py](<../services/worker-service/src/services/automation_churn_trigger.py>) — automation_churn_trigger — focused `churn_probability_threshold` evaluator for the worker's probability-update seam (Task 4, churn-triggered-playbooks). Why this exists (read before…
- [automation_email_delivery.py](<../services/worker-service/src/services/automation_email_delivery.py>) — Shared worker-side plumbing for the automation `send_customer_email` action (automation-send-customer-email, worker-mirrors aspect). Two things live here: 1. **Delivery-row helpers** —…
- [automation_feedback_trigger.py](<../services/worker-service/src/services/automation_feedback_trigger.py>) — automation_feedback_trigger — worker-side mirror of the `feedback_category_match`, `sentiment_pattern`, and (added for batch-sentiment-trigger, Track B) `batch_sentiment_threshold` triggers…
- [automation_usage_trend_trigger.py](<../services/worker-service/src/services/automation_usage_trend_trigger.py>) — automation_usage_trend_trigger — focused `usage_trend` evaluator for the worker's daily usage-recompute seam (worker-trend-evaluator aspect, usage-trend-automation-trigger PRD, M1/M5). Why…
- [calibration_refit.py](<../services/worker-service/src/services/calibration_refit.py>) — Calibration refit logic — Phase 6.1 (M4.1). Entry point ----------- refit_org(org_id, db) -> dict Pure logic: no Celery, no FastAPI. All DB I/O is synchronous SQLAlchemy. The caller…
- [churn_backfill.py](<../services/worker-service/src/services/churn_backfill.py>) — Cancellable, window-bounded historical CRM churn-suggestion backfill (historical-backfill aspect). Why this exists: forward-only harvesting (churn_suggestion_harvester) reads only the CRM…
- [churn_harvest_adapters.py](<../services/worker-service/src/services/churn_harvest_adapters.py>) — Pure, no-I/O adapters normalizing a HubSpot deal / Salesforce Opportunity to one churn-suggestion candidate shape (harvester-core aspect). This module MUST NOT import Celery, SQLAlchemy,…
- [churn_harvest_core.py](<../services/worker-service/src/services/churn_harvest_core.py>) — Pure, no-I/O decision core for CRM lost-renewal churn suggestions. This module MUST NOT import Celery, SQLAlchemy, FastAPI, httpx, or any CRM client. Mirrors the purity contract of…
- [churn_suggestion_harvester.py](<../services/worker-service/src/services/churn_suggestion_harvester.py>) — Idempotent, capped churn-suggestion harvester (harvester-core aspect). Reads closed-lost CRM records via the injected client, applies `decide_suggestion` (churn_harvest_core) plus the…
- [classifier_predict.py](<../services/worker-service/src/services/classifier_predict.py>) — Per-org corrections-classifier loader + predict + override helper — worker-service (M5.2 predict-seam-resolver). Independent mirror of…
- [classifier_resolver.py](<../services/worker-service/src/services/classifier_resolver.py>) — Org-scoped corrections-classifier mode resolver — worker-service mirror (M5.2 predict-seam-resolver). Independent mirror of services/backend-api/src/services/classifier_resolver.py. No…
- [health_recompute.py](<../services/worker-service/src/services/health_recompute.py>) — Single seam for worker-side customer-health recomputation. WHAT IS BROKEN (GitHub #3) -------------------------- ``health_score_service`` lives only in ``services/backend-api``. The worker…
- [intercom_webhook_enrich.py](<../services/worker-service/src/services/intercom_webhook_enrich.py>) — Intercom webhook enrichment module (webhook-enrich-module aspect). Turns a `conversation.user.replied` / `conversation.rating.added` webhook event into a MERGE into the existing…
- [outreach_sender.py](<../services/worker-service/src/services/outreach_sender.py>) — outreach_sender — the shared per-recipient outreach send helper (outreach-core aspect). Both send paths (playbook `send_email` step, bulk campaign task) call this helper so opt-out,…
- [outreach_templates_mirror.py](<../services/worker-service/src/services/outreach_templates_mirror.py>) — Built-in outreach template registry — WORKER MIRROR. The worker cannot import backend-api packages, so this module duplicates the backend registry data verbatim (same…
- [playbook_engine.py](<../services/worker-service/src/services/playbook_engine.py>) — Playbook execution engine — Phase 5.2 (M4.1). Pure business logic called by the Celery task `tasks.churn_playbooks.run_playbook`. No Celery dependency here — fully testable with a plain…
- [probability_updater.py](<../services/worker-service/src/services/probability_updater.py>) — Probability updater service — Phase 3.1. Recomputes churn probability for a customer after their CustomerHealth row is refreshed by update_customer_health(). Pure logic: no Celery, no…
- [report_generator.py](<../services/worker-service/src/services/report_generator.py>) — Report Generator — generates structured report data for scheduled AI reports. DUPLICATED: mirrors services/backend-api/src/services/copilot/report_generator.py verbatim (data-only builders…
- [scheduled_report_email.py](<../services/worker-service/src/services/scheduled_report_email.py>) — scheduled_report_email — HTML renderer for scheduled AI reports (worker). Renders a generated report dict into a plain-HTML email body, following the worker's raw `_send_email` path (BYOK…
- [scheduled_report_narrative.py](<../services/worker-service/src/services/scheduled_report_narrative.py>) — scheduled_report_narrative — concise data-led LLM narrative for scheduled reports. The scheduled-report narrative is a short data-led summary (a few short paragraphs citing the section…
- [segment_service.py](<../services/worker-service/src/services/segment_service.py>) — Customer segment classifier. ``classify_segment(...) -> str`` is a PURE, no-DB rule engine that assigns a single segment slug to a customer, given already-computed health/usage/ sentiment…
- [sentiment_resolver.py](<../services/worker-service/src/services/sentiment_resolver.py>) — Org-scoped sentiment provider resolver — worker-service mirror. Independent mirror of services/backend-api/src/services/sentiment_resolver.py. No cross-service import: this reads the…
- [status_sync_core.py](<../services/worker-service/src/services/status_sync_core.py>) — Pure, no-I/O reconcile core for inbound Jira status sync. This module MUST NOT import FastAPI, SQLAlchemy, or any DB/network client. It is copied verbatim into the worker service (see…
- [status_writer.py](<../services/worker-service/src/services/status_writer.py>) — Shared, provider-agnostic status writer for inbound status-sync pollers (jira_sync.py, asana_sync.py — asana-status-sync/worker-sync-task aspect). Originally lifted verbatim from…
- [usage_decline_label_detector.py](<../services/worker-service/src/services/usage_decline_label_detector.py>) — Usage-decline churn-label detector (worker-detector aspect). Wires the pure `usage_decline_labels_core` functions to the worker's real CustomerUsage / CustomerUsageHistory / OrgAIConfig…
- [usage_decline_labels_core.py](<../services/worker-service/src/services/usage_decline_labels_core.py>) — Usage-decline churn-label detector core (detector-core aspect). Pure logic only — no database, no Celery, no HTTP. Every function here takes plain data and returns plain data so it is…
- [usage_score_service.py](<../services/worker-service/src/services/usage_score_service.py>) — Usage score computation service. ``compute_usage_score(rollup, now) -> int`` blends three dimensions: - Recency (weight 0.50): time since last_active_at - Frequency (weight 0.30):…
- [usage_trend_severity.py](<../services/worker-service/src/services/usage_trend_severity.py>) — Usage-trend severity ordering — the single source of truth for "is this transition strictly worsening?" used by the AutomationEngine's usage_trend trigger checker (backend-api) and the…
- [winback_detector.py](<../services/worker-service/src/services/winback_detector.py>) — Winback detector service — Phase 3.2 (M4.1). Detects when a previously churned customer submits new feedback and flags them as a potential winback by setting has_potential_winback=True and…
- [zendesk_status_core.py](<../services/worker-service/src/services/zendesk_status_core.py>) — Pure, no-I/O reconcile core for inbound Zendesk status sync. This module MUST NOT import FastAPI, SQLAlchemy, or any DB/network client. It is a verbatim copy of…

## `services/worker-service/src/tasks`

[Directory guide](<../services/worker-service/src/tasks/directory.md>)

- [__init__.py](<../services/worker-service/src/tasks/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [alerts.py](<../services/worker-service/src/tasks/alerts.py>) — Alert tasks for urgent feedback notifications. Supports configurable triggers and customizable message templates.
- [analysis.py](<../services/worker-service/src/tasks/analysis.py>) — Analysis tasks for processing customer feedback. Migrated from APScheduler to Celery for distributed processing. Supports LLM-powered categorization (OpenAI) with keyword fallback.
- [anomaly.py](<../services/worker-service/src/tasks/anomaly.py>) — Anomaly detection tasks for sentiment spike detection. Runs hourly via Celery Beat to detect negative sentiment spikes.
- [asana_sync.py](<../services/worker-service/src/tasks/asana_sync.py>) — Inbound Asana status-sync poller (asana-status-sync/worker-sync-task). See docs/planning/asana-status-sync/worker-sync-task/plan_20260712.md. Mirrors src/tasks/jira_sync.py — see that…
- [automation.py](<../services/worker-service/src/tasks/automation.py>) — Celery tasks for AI Workflow Automation (M4.4). Currently contains: - purge_old_automation_executions: weekly retention purge (90-day window)
- [churn_backfill_task.py](<../services/worker-service/src/tasks/churn_backfill_task.py>) — Historical CRM churn-suggestion backfill Celery task (historical-backfill aspect). Task: backfill_churn_suggestions(integration_id, months, provider) — a DISTINCT, cancellable task.…
- [churn_calibration.py](<../services/worker-service/src/tasks/churn_calibration.py>) — Celery tasks for weekly churn calibration — Phase 6.1 (M4.1). Beat schedule (registered in celery_app.py): - refit_all_orgs → Mondays 07:45 UTC - refit_global_calibration → Daily 03:00 UTC…
- [churn_classifier_training.py](<../services/worker-service/src/tasks/churn_classifier_training.py>) — Celery tasks for weekly per-org churn classifier retraining — worker-churn- trainer-and-schedule aspect (M5.3 per-org-churn-model). Beat schedule (registered in celery_app.py): -…
- [churn_playbooks.py](<../services/worker-service/src/tasks/churn_playbooks.py>) — Celery tasks for churn playbook execution — Phase 5.2 (M4.1). Tasks: run_playbook(execution_id) — Execute a ChurnPlaybookExecution. purge_old_executions() — Delete execution rows older than…
- [classifier_training.py](<../services/worker-service/src/tasks/classifier_training.py>) — Celery tasks for weekly per-org sentiment and category corrections classifier retraining — worker-trainer-and-schedule aspect (M5.2 per-org-corrections-classifier). Beat schedule…
- [hubspot_sync.py](<../services/worker-service/src/tasks/hubspot_sync.py>) — HubSpot CRM sync tasks (hubspot-sync aspect). Tasks: sync_all_hubspot — fan-out over orgs with active HubSpot integrations sync_hubspot_org — per-org retryable sync (max_retries=3) Core…
- [hubspot_writeback.py](<../services/worker-service/src/tasks/hubspot_writeback.py>) — HubSpot CRM writeback task (writeback-task-trigger aspect). Task: push_health_to_hubspot(org_id, customer_email) — idempotent, gated, soft-pausing push of a customer's current health score…
- [insights.py](<../services/worker-service/src/tasks/insights.py>) — Weekly insights generation task. Generates AI-powered weekly insight summaries for each organization.
- [intercom_sync.py](<../services/worker-service/src/tasks/intercom_sync.py>) — Intercom conversation-pull sync tasks (pull-sync aspect). Tasks: sync_all_intercom — fan-out over orgs with active Intercom integrations sync_intercom_org — per-org retryable sync…
- [intercom_writeback.py](<../services/worker-service/src/tasks/intercom_writeback.py>) — Intercom write-back task (intercom-writeback aspect, worker-writeback-task). Task: push_resolved_writeback(org_id, items) — given the org and the feedback items that just transitioned to…
- [jira_sync.py](<../services/worker-service/src/tasks/jira_sync.py>) — Inbound Jira status-sync poller (jira-status-sync/inbound-status-sync, Phase 4). See docs/planning/jira-status-sync/inbound-status-sync/plan_20260711.md. Tasks: sync_all_jira — fan-out over…
- [outreach.py](<../services/worker-service/src/tasks/outreach.py>) — Outreach send tasks — the only place an outreach email is actually sent. send_outreach_email(campaign_id, recipient_id) — send one outreach email via…
- [salesforce_sync.py](<../services/worker-service/src/tasks/salesforce_sync.py>) — Salesforce CRM sync tasks (salesforce-sync aspect). Tasks: sync_all_salesforce — fan-out over orgs with active Salesforce integrations sync_salesforce_org — per-org retryable sync…
- [salesforce_writeback.py](<../services/worker-service/src/tasks/salesforce_writeback.py>) — Salesforce CRM writeback task (push-task-trigger aspect). Task: push_health_to_salesforce(org_id, customer_email) — idempotent, gated, soft-pausing push of a customer's current health score…
- [scheduled_reports.py](<../services/worker-service/src/tasks/scheduled_reports.py>) — Celery tasks for scheduled AI report generation (worker-scheduled-generation). Beat schedule (registered in celery_app.py): - generate_scheduled_reports → hourly at :15 UTC; filters due…
- [segments.py](<../services/worker-service/src/tasks/segments.py>) — Celery task for nightly customer-segment recompute (segment-engine aspect, Phase 4). ``recompute_segments`` re-derives ``segment`` for every non-archived ``CustomerHealth`` row across all…
- [source_events.py](<../services/worker-service/src/tasks/source_events.py>) — Source event processing tasks. Handles events from all source types (Slack, webhooks, etc.) using the adapter pattern.
- [usage_metrics.py](<../services/worker-service/src/tasks/usage_metrics.py>) — Celery tasks for product-usage rollup and scoring (aspect 3), plus the usage-history-snapshot aspect's daily storage and pruning. Tasks: process_usage_event — triggered per event from…
- [webhook_delivery.py](<../services/worker-service/src/tasks/webhook_delivery.py>) — Celery task: deliver_webhook (M3.1 Phase 2). Handles: - HTTP POST to the webhook URL with HMAC-SHA256 signature + custom headers - Delivery logging (WebhookDelivery row) - Exponential…
- [workflow.py](<../services/worker-service/src/tasks/workflow.py>) — Workflow tasks — auto-assignment of feedback items. Mirrors the auto-assignment logic from backend-api/src/services/workflow_service.py but runs as a periodic Celery task to catch items…
- [zendesk_status_sync.py](<../services/worker-service/src/tasks/zendesk_status_sync.py>) — Inbound Zendesk status-sync poller (zendesk-status-sync/poll-task). See docs/planning/zendesk-status-sync/poll-task/plan_20260712.md. Mirrors src/tasks/jira_sync.py's two-task fan-out…
- [zendesk_sync.py](<../services/worker-service/src/tasks/zendesk_sync.py>) — Zendesk ticket-pull sync tasks (ingestion-pull aspect). Tasks: sync_all_zendesk — fan-out over orgs with active Zendesk integrations sync_zendesk_org — per-org retryable sync…

## `services/worker-service/tests`

[Directory guide](<../services/worker-service/tests/directory.md>)

- [__init__.py](<../services/worker-service/tests/__init__.py>) — Static/configuration artifact; inspect its consumer.
- [conftest.py](<../services/worker-service/tests/conftest.py>) — Pytest configuration and fixtures for worker service tests.
- [test_alert_preference_mirror.py](<../services/worker-service/tests/test_alert_preference_mirror.py>) — Drift-pin for the worker UserAlertPreference mirror. worker-service cannot import backend-api, so its model layer is a deliberate, hand-maintained duplicate of the backend models. The…
- [test_alerts.py](<../services/worker-service/tests/test_alerts.py>) — TDD tests for send_slack_alert() OAuth token decryption (worker decrypt mirrors). The backend encrypts Slack OAuth tokens at rest in `integrations.oauth_access_token`…
- [test_analysis_classifier_seam.py](<../services/worker-service/tests/test_analysis_classifier_seam.py>) — Phase 4 RED: Tests for the classifier-override injection at the worker call site (src/tasks/analysis.py::_apply_keyword_analysis / _analyze_feedback_item), the authoritative…
- [test_analysis_llm.py](<../services/worker-service/tests/test_analysis_llm.py>) — Tests for the LLM-integrated analysis pipeline.
- [test_analysis_winback_integration.py](<../services/worker-service/tests/test_analysis_winback_integration.py>) — Integration tests verifying that probability_updater and winback_detector are both called from _analyze_feedback_item, and that failures are isolated. Phase 3.2 — TDD GREEN phase. Strategy:…
- [test_anomaly_detection.py](<../services/worker-service/tests/test_anomaly_detection.py>) — Tests for anomaly detection logic.
- [test_anomaly_integration.py](<../services/worker-service/tests/test_anomaly_integration.py>) — Integration tests for anomaly detection with real SQLite database. Tests _check_org_for_anomaly, _dispatch_anomaly_alerts, detect_sentiment_anomalies.
- [test_asana_client_worker.py](<../services/worker-service/tests/test_asana_client_worker.py>) — TDD tests for the worker-owned AsanaClient (src/clients/asana.py) and the pure asana_category adapter (src/services/asana_adapter.py) — the asana-client-get-task aspect of…
- [test_asana_sync_task.py](<../services/worker-service/tests/test_asana_sync_task.py>) — TDD tests for src.tasks.asana_sync (inbound Asana status-sync poller) — asana-status-sync/worker-sync-task aspect. See docs/planning/asana-status-sync/worker-sync-task/plan_20260712.md.…
- [test_automation_churn_trigger.py](<../services/worker-service/tests/test_automation_churn_trigger.py>) — Tests for src.services.automation_churn_trigger — Task 4 (churn-triggered-playbooks). Strict TDD: written FIRST (RED) before the evaluator implementation. `run_playbook.delay` is patched…
- [test_automation_email_delivery.py](<../services/worker-service/tests/test_automation_email_delivery.py>) — Tests for the worker mirror of `automation_email_deliveries` + the shared send_customer_email helper (automation-send-customer-email, worker-mirrors aspect, Phase 1 + Phase 5). Strict TDD:…
- [test_automation_feedback_trigger.py](<../services/worker-service/tests/test_automation_feedback_trigger.py>) — Tests for src.services.automation_feedback_trigger (worker-trigger-mirror, aspect 2). Strict TDD: written FIRST (RED) before the evaluator implementation. `src.tasks.analysis` imports…
- [test_automation_usage_trend_trigger.py](<../services/worker-service/tests/test_automation_usage_trend_trigger.py>) — Tests for src.services.automation_usage_trend_trigger — worker-trend-evaluator aspect (M1/M5 of usage-trend-automation-trigger PRD). Strict TDD: written FIRST (RED) before the evaluator…
- [test_batch_sentiment_trigger_seam.py](<../services/worker-service/tests/test_batch_sentiment_trigger_seam.py>) — batch-sentiment-trigger / trigger-core, Track B — seam-capture tests for `src.tasks.analysis.analyze_single_feedback` genuinely invoking the `batch_sentiment_threshold` evaluator. Strict…
- [test_beat_schedule_integrity.py](<../services/worker-service/tests/test_beat_schedule_integrity.py>) — Every scheduled task must actually exist. This repo has shipped the same failure more than once: code that is registered, scheduled and visibly "on", but which does nothing. The automations…
- [test_byok_only.py](<../services/worker-service/tests/test_byok_only.py>) — Tests for the BYOK-only (bring-your-own-key) pivot. PRD Workstream A: A1 (org_resolver), A2 (fallback), A5 (analysis pending). RED → GREEN test sequence: - Write failing tests first (test…
- [test_calibration_refit.py](<../services/worker-service/tests/test_calibration_refit.py>) — Tests for calibration_refit.refit_org() — Phase 6.1 (M4.1). Written RED-first (TDD). All ~14 tests must fail before the implementation in src/services/calibration_refit.py exists, then pass…
- [test_churn_backfill.py](<../services/worker-service/tests/test_churn_backfill.py>) — TDD tests for churn_backfill.run_backfill (historical-backfill aspect). Strategy (mirrors test_churn_suggestion_harvester.py): file-local in-memory SQLite engine (not conftest's) + a…
- [test_churn_backfill_task.py](<../services/worker-service/tests/test_churn_backfill_task.py>) — TDD tests for churn_backfill_task (historical-backfill aspect, Phase 5). Strategy (mirrors test_churn_backfill.py): file-local in-memory SQLite engine + hand-written Fake CRM client (no…
- [test_churn_calibration_tasks.py](<../services/worker-service/tests/test_churn_calibration_tasks.py>) — Tests for Celery tasks in tasks.churn_calibration — Phase 6.1 (M4.1). Written RED-first (TDD). All ~9 tests must fail before the implementation in src/tasks/churn_calibration.py exists,…
- [test_churn_classifier_hold_guard.py](<../services/worker-service/tests/test_churn_classifier_hold_guard.py>) — Tests for the churn auto-promotion hold guard — worker-churn-trainer-and-schedule aspect (M5.3 per-org-churn-model), mirroring tests/test_classifier_hold_guard.py. retrain_org must re-read…
- [test_churn_classifier_training_tasks.py](<../services/worker-service/tests/test_churn_classifier_training_tasks.py>) — Tests for Celery tasks in tasks.churn_classifier_training — worker-churn-trainer- and-schedule aspect (M5.3 per-org-churn-model). Written RED-first (TDD), mirroring…
- [test_churn_factor_computation.py](<../services/worker-service/tests/test_churn_factor_computation.py>) — TDD tests for churn risk factor computation (M1.4 Phase 2): - _compute_heuristic_churn_risk() returns Tuple[int, Dict] - Factor dict contains all 9 keys with score/max/label - Factor scores…
- [test_churn_harvest_adapters.py](<../services/worker-service/tests/test_churn_harvest_adapters.py>) — TDD tests for the pure HubSpot / Salesforce candidate adapters (harvester-core aspect). Pure asserts only — no I/O, no fixtures, no DB, no mocks, no `patch`.
- [test_churn_harvest_core.py](<../services/worker-service/tests/test_churn_harvest_core.py>) — TDD tests for the pure churn-suggestion decision core (harvester-core aspect). Pure asserts only — no I/O, no fixtures, no DB, no mocks, no `patch`.
- [test_churn_heuristic.py](<../services/worker-service/tests/test_churn_heuristic.py>) — Tests for churn risk heuristic scoring (keyword fallback).
- [test_churn_suggestion_harvester.py](<../services/worker-service/tests/test_churn_suggestion_harvester.py>) — TDD tests for churn_suggestion_harvester.harvest_org_suggestions (harvester-core aspect). Strategy (mirrors test_hubspot_sync.py:29-66): file-local in-memory SQLite engine (not conftest's)…
- [test_classifier_hold_guard.py](<../services/worker-service/tests/test_classifier_hold_guard.py>) — Tests for the auto-promotion hold guard — worker-hold-guard aspect (classifier-model-versioning-rollback, M2/M3a). retrain_org must re-read the org's OrgAIConfig `*_autopromote_hold` column…
- [test_classifier_predict_category_routing.py](<../services/worker-service/tests/test_classifier_predict_category_routing.py>) — Phase 2 RED: Tests for _route_category_label + LoadedClassifier.predict_label_only (worker-service mirror). Covers the built-in-vocab routing table (predict-seam spec's unambiguous-routing…
- [test_classifier_predict_contract.py](<../services/worker-service/tests/test_classifier_predict_contract.py>) — Phase 6: Contract-adapter test pinning aspect B's real `predict(artifact, text) -> (label, proba)` / `score_from_proba(proba) -> float` signature (analysis-engine's corrections_classifier…
- [test_classifier_predict_helper.py](<../services/worker-service/tests/test_classifier_predict_helper.py>) — Phase 3 RED: Tests for apply_classifier_override — off/shadow/auto branching + score mapping (worker-service). Fake feedback object + injected fake LoadedClassifier (no dependency on aspect…
- [test_classifier_predict_loader.py](<../services/worker-service/tests/test_classifier_predict_loader.py>) — Phase 2 RED: Tests for load_active_classifier — 3-tier fallback + corrupt- artifact defense + per-org cache (worker-service). Mirrors probability_updater._load_active_model /…
- [test_classifier_predict_mirror.py](<../services/worker-service/tests/test_classifier_predict_mirror.py>) — Phase 3/6 RED->GREEN: Mirror-equivalence guard (worker-service side). Diffs the normalized bodies of classifier_resolver.py and classifier_predict.py between backend-api and worker-service:…
- [test_classifier_resolver.py](<../services/worker-service/tests/test_classifier_resolver.py>) — Phase 1 RED: Tests for resolve_classifier (worker-service mirror). Same degrade matrix as backend-api's test_classifier_resolver.py, against the worker's independent mirror resolver (reads…
- [test_classifier_seam_matrix.py](<../services/worker-service/tests/test_classifier_seam_matrix.py>) — Phase 6: `test_classifier_seam_matrix` — CLASSIFIER_SEAM_CASES driven end-to-end (worker-service), through REAL resolve_classifier + load_active_classifier + aspect B's real…
- [test_classifier_training_tasks.py](<../services/worker-service/tests/test_classifier_training_tasks.py>) — Tests for Celery tasks in tasks.classifier_training — worker-trainer-and-schedule aspect (M5.2 per-org-corrections-classifier). Written RED-first (TDD), phase by phase, mirroring…
- [test_custom_taxonomies.py](<../services/worker-service/tests/test_custom_taxonomies.py>) — TDD tests for Feature B: Custom taxonomies + configurable health weights. B1 — Custom categories wired into the LLM prompt and keyword matcher. B2 — Health-weight endpoints persist + reject…
- [test_discord_alerts.py](<../services/worker-service/tests/test_discord_alerts.py>) — TDD tests for Discord alert support (Track B — worker-service). Covers: - send_discord_message_webhook() in src/tasks/alerts.py (B1) - Discord embed builder + dispatch at all three alert…
- [test_discord_dispatch.py](<../services/worker-service/tests/test_discord_dispatch.py>) — TDD tests for Discord dispatch at the main alert pipe. notification_dispatch.py::_dispatch_slack_alert (~:501) is the main user-facing pipe for urgent_feedback / sentiment_spike /…
- [test_discord_health_dispatch.py](<../services/worker-service/tests/test_discord_health_dispatch.py>) — TDD tests for Discord dispatch of customer health drop/recovery alerts. notification_dispatch.py::_dispatch_slack_health_alert (~:59) plus build_health_alert_blocks (~:100-184) are the…
- [test_email.py](<../services/worker-service/tests/test_email.py>) — Tests for the worker service email module.
- [test_email_adapter.py](<../services/worker-service/tests/test_email_adapter.py>) — Tests for Email adapter.
- [test_health_dispatch.py](<../services/worker-service/tests/test_health_dispatch.py>) — TDD tests for dispatch_health_drop_alert() in notification_dispatch.py. RED → GREEN → REFACTOR.
- [test_health_recompute_seam.py](<../services/worker-service/tests/test_health_recompute_seam.py>) — Pins the real, unmocked state of worker-side health recomputation (GitHub #3). Every other worker test that touches this path injects a fake ``src.services.health_score_service`` into…
- [test_hubspot_client.py](<../services/worker-service/tests/test_hubspot_client.py>) — TDD tests for HubSpotClient (src/clients/hubspot.py). No real HTTP. Uses unittest.mock.patch on httpx.Client methods.
- [test_hubspot_sync.py](<../services/worker-service/tests/test_hubspot_sync.py>) — TDD tests for hubspot_sync tasks and _sync_org core. Strategy: in-memory SQLite, mocked httpx/client, NO Celery eager mode. Mirror test_usage_metrics.py structure exactly.
- [test_hubspot_write_client.py](<../services/worker-service/tests/test_hubspot_write_client.py>) — TDD tests for the HubSpotClient write surface (src/clients/hubspot.py): - update_contact_property(contact_id, property_name, value) -> PATCH - get_contact_property_def(name) -> GET property…
- [test_hubspot_writeback_task.py](<../services/worker-service/tests/test_hubspot_writeback_task.py>) — TDD tests for the push_health_to_hubspot writeback task (writeback-task-trigger aspect, Phase 1). Strategy: in-memory SQLite, mocked HubSpotClient, NO Celery eager mode. Mirrors…
- [test_insights_task.py](<../services/worker-service/tests/test_insights_task.py>) — Tests for weekly insights generation Celery task.
- [test_intercom_adapter.py](<../services/worker-service/tests/test_intercom_adapter.py>) — Tests for Intercom adapter.
- [test_intercom_client_conversation_parts.py](<../services/worker-service/tests/test_intercom_client_conversation_parts.py>) — Tests for the IntercomClient conversation-parts access (client-conversation-parts aspect). Task 0 verified the API shape against Intercom's published OpenAPI specification and adopted R1b:…
- [test_intercom_client_writeback.py](<../services/worker-service/tests/test_intercom_client_writeback.py>) — Tests for the IntercomClient write surface (write-back aspect). IntercomClient gains `add_note`, `close_conversation` and `fetch_admin_id` so the write-back task can annotate and close…
- [test_intercom_enrichment.py](<../services/worker-service/tests/test_intercom_enrichment.py>) — Tests for the pull-enrichment merge helper (pull-enrichment aspect). Phase 1 seam tests for `_enrich_conversation_replies(db, item, reply_parts, rating)` in src/tasks/intercom_sync.py — the…
- [test_intercom_envelope_seam.py](<../services/worker-service/tests/test_intercom_envelope_seam.py>) — Contract tests for the Intercom webhook -> adapter envelope seam. WHY THIS FILE EXISTS -------------------- Intercom ingestion produced no feedback item in any release up to 1.0.0. The…
- [test_intercom_parts.py](<../services/worker-service/tests/test_intercom_parts.py>) — Tests for the conversation-object reply/rating extraction (adapter-reply-rating-extraction). The webhook adapter (adapters/intercom.py) parses event-shaped payloads; the pull path works…
- [test_intercom_sync.py](<../services/worker-service/tests/test_intercom_sync.py>) — Tests for the Intercom conversation-pull sync (pull-sync aspect). This is the path the originating user ask actually named -- "so feedback flows in automatically instead of pasting tickets…
- [test_intercom_tenancy_discriminator.py](<../services/worker-service/tests/test_intercom_tenancy_discriminator.py>) — Tenancy tests for the Intercom branch of _find_matching_sources. This file guards the function that was the site of `intercom-webhook-unauthenticated-cross-org-write` (P0, fixed on…
- [test_intercom_webhook_enrich.py](<../services/worker-service/tests/test_intercom_webhook_enrich.py>) — Contract tests for the Intercom webhook enrichment module (webhook-enrich-module aspect). Exercises `src.services.intercom_webhook_enrich.enrich_webhook_item` — the worker service-layer…
- [test_intercom_writeback_dispatch_seam.py](<../services/worker-service/tests/test_intercom_writeback_dispatch_seam.py>) — Seam tests for the intercom write-back dispatch from worker writers (dispatch-seams aspect, R6 — worker side). Strict TDD: written FIRST (RED) — no dispatch exists in the writers yet. Every…
- [test_intercom_writeback_name_consistency.py](<../services/worker-service/tests/test_intercom_writeback_name_consistency.py>) — Name-consistency pin for the intercom write-back dispatch (dispatch-seams). The five dispatch sites (3 backend routes via send_task, 2 worker writers via .delay) all fire the task…
- [test_intercom_writeback_task.py](<../services/worker-service/tests/test_intercom_writeback_task.py>) — TDD tests for the Intercom write-back task push_resolved_writeback (intercom-writeback aspect, worker-writeback-task). Strategy: in-memory SQLite, mocked IntercomClient, NO Celery eager…
- [test_jira_client_worker.py](<../services/worker-service/tests/test_jira_client_worker.py>) — TDD tests for the worker-owned JiraClient (src/clients/jira.py) — Phase 4 of docs/planning/jira-status-sync/inbound-status-sync/plan_20260711.md. No real HTTP. Uses unittest.mock.patch on…
- [test_jira_sync_task.py](<../services/worker-service/tests/test_jira_sync_task.py>) — TDD tests for src.tasks.jira_sync (inbound Jira status-sync poller) — Phase 4 of docs/planning/jira-status-sync/inbound-status-sync/plan_20260711.md. Strategy: real SQLite (`db` fixture…
- [test_keyword_analysis.py](<../services/worker-service/tests/test_keyword_analysis.py>) — Tests for keyword-based analysis fallback (_apply_keyword_analysis). Verifies that when LLM is unavailable, the keyword pipeline correctly analyzes sentiment, urgency, pain points, feature…
- [test_keyword_analysis_sentiment_provider.py](<../services/worker-service/tests/test_keyword_analysis_sentiment_provider.py>) — Phase 5 RED: Tests for per-org sentiment provider injection at the worker call site (src/tasks/analysis.py::_apply_keyword_analysis). Covers: - get_sentiment_analyzer(provider_name)…
- [test_llm_client.py](<../services/worker-service/tests/test_llm_client.py>) — Tests for the provider-agnostic LLM client (llm_client.py).
- [test_llm_factory.py](<../services/worker-service/tests/test_llm_factory.py>) — Tests for LLMProviderFactory.
- [test_llm_fallback.py](<../services/worker-service/tests/test_llm_fallback.py>) — Tests for FallbackChain — retry + fallback logic. All LLM calls are mocked. No real API calls.
- [test_llm_pricing.py](<../services/worker-service/tests/test_llm_pricing.py>) — Tests for LLM pricing / cost estimation utilities.
- [test_llm_providers.py](<../services/worker-service/tests/test_llm_providers.py>) — Tests for LLM provider implementations: OpenAI, Anthropic, Google. All external API calls are mocked.
- [test_llm_service.py](<../services/worker-service/tests/test_llm_service.py>) — Tests for LLM service layer (org_resolver + fallback) — BYOK-only. NOTE: The old src/llm/service.py (dead parallel resolver with system-key fallback) was deleted as part of Workstream A3 of…
- [test_llm_types.py](<../services/worker-service/tests/test_llm_types.py>) — Tests for LLM types and dataclasses.
- [test_local_llm.py](<../services/worker-service/tests/test_local_llm.py>) — Tests for Feature A: Local / Offline LLM (Ollama + OpenAI-compatible endpoint). TDD sequence: RED first, then production code makes them GREEN. Covers: - OpenAICompatibleProvider:…
- [test_model_parity_classifier.py](<../services/worker-service/tests/test_model_parity_classifier.py>) — Backend <-> worker column-parity characterization tests for M5.2 classifier models (data-layer aspect R5 mitigation). Same sys.path/sys.modules swap technique as…
- [test_no_stripe_billing.py](<../services/worker-service/tests/test_no_stripe_billing.py>) — TDD guard: asserts that ALL Stripe billing machinery has been removed from worker-service/src/. RED phase: these tests FAIL against the current code (billing.py exists, beat entries are…
- [test_org_ai_config_category_classifier_mode.py](<../services/worker-service/tests/test_org_ai_config_category_classifier_mode.py>) — TDD test for per-org-category-classifier (M5.2 v2) — worker mirror of OrgAIConfig.category_classifier_mode. Mirrors test_org_classifier_mirror.py's…
- [test_org_ai_config_urgency_classifier_mode.py](<../services/worker-service/tests/test_org_ai_config_urgency_classifier_mode.py>) — TDD test for per-org-urgency-classifier (urgency-classifier-head, data-and-config aspect) — worker mirror of OrgAIConfig.urgency_classifier_mode. Mirrors…
- [test_org_classifier_mirror.py](<../services/worker-service/tests/test_org_classifier_mirror.py>) — TDD tests for M5.2 per-org-corrections-classifier — worker mirror aspect. Adds the currently-missing `AICorrection` mirror (table `ai_corrections`), lightweight `OrgClassifierModel` +…
- [test_outreach_sender.py](<../services/worker-service/tests/test_outreach_sender.py>) — Tests for worker outreach_sender — opt-out, cooldown, List-Unsubscribe, token composition (outreach-core aspect). Strict TDD: written FIRST (RED) before the implementation. Redis cooldown…
- [test_outreach_task.py](<../services/worker-service/tests/test_outreach_task.py>) — Tests for the per-recipient outreach Celery task (bulk-campaign-api aspect). Phase 1 — worker model mirrors (RED-first): - `OutreachCampaign` / `OutreachCampaignRecipient` exist on the…
- [test_playbook_engine.py](<../services/worker-service/tests/test_playbook_engine.py>) — Tests for playbook_engine.execute() — Phase 5.2 (M4.1). Written RED-first (TDD). All ~14 tests must fail before implementation, then pass after src/services/playbook_engine.py is complete.…
- [test_playbook_notify_action.py](<../services/worker-service/tests/test_playbook_notify_action.py>) — Tests for the `notify` playbook action — playbook_engine._handle_notify (tag-notify-actions aspect, M2). TDD: written RED-first — every test fails with `unsupported action type: 'notify'`…
- [test_playbook_tag_action.py](<../services/worker-service/tests/test_playbook_tag_action.py>) — Tests for the `tag` playbook action — playbook_engine._handle_tag (tag-notify-actions aspect, M1). TDD: written RED-first — every test fails with `unsupported action type: 'tag'` until the…
- [test_playbook_task_actions.py](<../services/worker-service/tests/test_playbook_task_actions.py>) — Tests for the `create_task` / `schedule_task` playbook actions — playbook_engine._handle_create_task / _handle_schedule_task (playbook-tasks aspect, M3). TDD: written RED-first — every test…
- [test_playbook_trigger_automation.py](<../services/worker-service/tests/test_playbook_trigger_automation.py>) — Tests for the `trigger_automation` playbook action — playbook_engine._handle_trigger_automation (trigger-automation aspect, M4). TDD: written RED-first — every test fails with `unsupported…
- [test_probability_updater.py](<../services/worker-service/tests/test_probability_updater.py>) — Tests for probability_updater.update() — Phase 3.1. All 14 tests follow strict TDD: written RED before implementation, then driven GREEN by src/services/probability_updater.py.
- [test_probability_updater_churn_seam.py](<../services/worker-service/tests/test_probability_updater_churn_seam.py>) — Phase 3 (GREEN) — per-org-churn-model predict seam at probability_updater. Pins the churn ML seam for `update()`: - off / no churn model -> byte-identical calibrated path…
- [test_reanalysis_seam.py](<../services/worker-service/tests/test_reanalysis_seam.py>) — reanalysis-seam aspect — seam-capture tests for `src.tasks.analysis.reanalyze_feedback`, the pull-facing half of the UI "Re-analyze" force seam (POST /api/v1/analyze with force=true; see…
- [test_reap_stale_playbook_executions.py](<../services/worker-service/tests/test_reap_stale_playbook_executions.py>) — Tests for reap_stale_executions (playbook-execution-reaper R2/R3). Rows can be stranded at `queued` (publish lost after commit) or `running` (worker died mid-run). The reaper re-publishes…
- [test_recompute_segments.py](<../services/worker-service/tests/test_recompute_segments.py>) — TDD tests for the segments Celery task — segment-engine Phase 4 (worker-service). Acceptance criteria (from plan_20260708.md, Phase 4): - recompute_segments re-derives ``segment`` for every…
- [test_run_playbook_task.py](<../services/worker-service/tests/test_run_playbook_task.py>) — Tests for Celery tasks: run_playbook and purge_old_executions — Phase 5.2 (M4.1). Written RED-first (TDD). Uses in-memory SQLite and monkeypatching of playbook_engine.execute to isolate…
- [test_salesforce_client.py](<../services/worker-service/tests/test_salesforce_client.py>) — TDD tests for SalesforceClient (src/clients/salesforce.py). No real HTTP. Uses unittest.mock.patch on httpx.Client methods. Mirrors test_hubspot_client.py structure.
- [test_salesforce_client_writeback.py](<../services/worker-service/tests/test_salesforce_client_writeback.py>) — TDD tests for SalesforceClient writeback methods (update_contact_field, describe_object) — salesforce-write-client aspect. No real HTTP. Uses unittest.mock.patch on httpx.Client methods.…
- [test_salesforce_sync.py](<../services/worker-service/tests/test_salesforce_sync.py>) — TDD tests for salesforce_sync tasks and _sync_org core. Strategy: in-memory SQLite, mocked SalesforceClient, NO Celery eager mode. Mirror test_hubspot_sync.py structure exactly.
- [test_salesforce_writeback_task.py](<../services/worker-service/tests/test_salesforce_writeback_task.py>) — TDD tests for the push_health_to_salesforce writeback task (push-task-trigger aspect, Phase 2). Strategy: in-memory SQLite, mocked SalesforceClient, NO Celery eager mode. Mirrors…
- [test_scheduled_report_email.py](<../services/worker-service/tests/test_scheduled_report_email.py>) — Tests for the scheduled-report email renderer and sender (worker-email-delivery). Report dict contract consumed by `render_scheduled_report_email`: { "organization_name": str, # org name,…
- [test_scheduled_reports.py](<../services/worker-service/tests/test_scheduled_reports.py>) — TDD tests for scheduled AI report generation (worker-scheduled-generation). Phase 1: mirrored ReportGenerator characterization (pins against drift). Later phases append: narrative writer,…
- [test_sentiment_resolver.py](<../services/worker-service/tests/test_sentiment_resolver.py>) — Phase 1 RED: Tests for resolve_sentiment_provider (worker-service mirror). Same degrade matrix as backend-api's test_sentiment_resolver.py, against the worker's independent mirror resolver…
- [test_sentry.py](<../services/worker-service/tests/test_sentry.py>) — Tests for Sentry integration in the Celery worker. Sentry is opt-in: a self-hosted worker must send nothing anywhere unless the operator sets SENTRY_DSN. These tests exercise the real…
- [test_source_events.py](<../services/worker-service/tests/test_source_events.py>) — Tests for the tenancy guards in `_find_matching_sources` (source_events.py). Four of five branches (slack, intercom, email, webhook) narrow the base query -- which only filters on…
- [test_status_sync_core.py](<../services/worker-service/tests/test_status_sync_core.py>) — Pure unit tests for src.services.status_sync_core (worker mirror). No I/O, no DB, no Celery. This module is a verbatim copy of services/backend-api/src/services/status_sync_core.py (see…
- [test_status_writer.py](<../services/worker-service/tests/test_status_writer.py>) — TDD tests for src.services.status_writer.apply_status_change_worker — status-sync-realtime-mapping/status-writer-race-guard aspect. See…
- [test_store_analysis_result.py](<../services/worker-service/tests/test_store_analysis_result.py>) — Tests for _store_analysis_result — stores LLM analysis on CustomerHealth records.
- [test_teams_alerts.py](<../services/worker-service/tests/test_teams_alerts.py>) — TDD tests for Teams alert support (worker-service). Covers: - send_teams_message_webhook() in src/tasks/alerts.py Per THE CONTRACT…
- [test_teams_dispatch.py](<../services/worker-service/tests/test_teams_dispatch.py>) — TDD tests for Teams dispatch at the main alert pipe. notification_dispatch.py::_dispatch_teams_alert sends a MessageCard (title + text) to the org's active Teams webhook integrations,…
- [test_teams_health_dispatch.py](<../services/worker-service/tests/test_teams_health_dispatch.py>) — TDD tests for Teams dispatch of customer health drop/recovery alerts. notification_dispatch.py::_dispatch_teams_health_alert sends a MessageCard (title + text) to the org's active Teams…
- [test_usage_decline_detector_seam.py](<../services/worker-service/tests/test_usage_decline_detector_seam.py>) — worker-detector aspect — Phase 5 seam-capture tests for `recompute_usage_scores` (src/tasks/usage_metrics.py). Strict TDD: written FIRST (RED) before the wiring. CRITICAL PLACEMENT (plan…
- [test_usage_decline_label_detector.py](<../services/worker-service/tests/test_usage_decline_label_detector.py>) — TDD tests for usage_decline_label_detector.detect_usage_decline_labels (worker-detector aspect — Phases 1-4. Phase 5 (wiring into recompute_usage_scores) lives in…
- [test_usage_metrics.py](<../services/worker-service/tests/test_usage_metrics.py>) — TDD tests for the usage_metrics Celery task — Phase 3. Acceptance criteria (from spec): AC1. process_usage_event upserts customer_usage (events_total increments, last_active_at advances,…
- [test_usage_trend_core.py](<../services/worker-service/tests/test_usage_trend_core.py>) — Phase A — RED: pure trend core (no I/O). Covers the two pure functions plus the lookback-selection helper added to usage_score_service.py for the trend-detection-and-health aspect: -…
- [test_usage_trend_severity.py](<../services/worker-service/tests/test_usage_trend_severity.py>) — TDD tests for the worker-service DUPLICATE of the usage-trend severity ordering helper (worker-trend-evaluator aspect) — strict TDD (RED first). This file is intentionally near-identical to…
- [test_usage_trend_snapshot_state.py](<../services/worker-service/tests/test_usage_trend_snapshot_state.py>) — snapshot-trend-columns aspect (usage-trend-automation-trigger, M3) — the ordering fix: a ``customer_usage_history`` snapshot row for a given day must carry the trend state/pct AS CLASSIFIED…
- [test_usage_trend_trigger_seam.py](<../services/worker-service/tests/test_usage_trend_trigger_seam.py>) — worker-trend-evaluator aspect — seam-capture tests for `recompute_usage_scores` (src/tasks/usage_metrics.py). Strict TDD: written FIRST (RED) before the seam-capture implementation. AC…
- [test_usage_trend_wiring.py](<../services/worker-service/tests/test_usage_trend_wiring.py>) — Phase D — wiring tests for the trend-detection-and-health aspect: trend classification/persistence inside `recompute_usage_scores`, sourced from a single batched `customer_usage_history`…
- [test_webhook_delivery.py](<../services/worker-service/tests/test_webhook_delivery.py>) — TDD tests for the deliver_webhook Celery task (M3.1 Phase 2). Tests are written first; the implementation at src/tasks/webhook_delivery.py must make them pass.
- [test_weekly_digest.py](<../services/worker-service/tests/test_weekly_digest.py>) — Tests for the weekly digest Celery task.
- [test_winback_detector.py](<../services/worker-service/tests/test_winback_detector.py>) — Tests for winback_detector.check() — Phase 3.2 (M4.1). Written RED-first before implementation. All 10 tests must fail initially with ImportError or AttributeError, then pass after…
- [test_worker_import_sweep.py](<../services/worker-service/tests/test_worker_import_sweep.py>) — R8 sweep-guard: worker source must never import backend-only modules. The worker image copies only ``worker-service/src`` and ``analysis-engine/src/analyzer`` under ``PYTHONPATH=/app``. Any…
- [test_zendesk_adapter.py](<../services/worker-service/tests/test_zendesk_adapter.py>) — Tests for Zendesk adapter (ingestion-core aspect).
- [test_zendesk_client.py](<../services/worker-service/tests/test_zendesk_client.py>) — TDD tests for ZendeskClient (src/clients/zendesk.py). No real HTTP. Uses unittest.mock.patch on httpx.Client methods. Mirrors test_salesforce_client.py structure (Phase 2 of ingestion-pull…
- [test_zendesk_client_show_many.py](<../services/worker-service/tests/test_zendesk_client_show_many.py>) — TDD tests for ZendeskClient.show_many (src/clients/zendesk.py). No real HTTP. Uses unittest.mock.patch on httpx.Client methods. Mirrors test_zendesk_client.py structure (client-batch-status…
- [test_zendesk_status_core.py](<../services/worker-service/tests/test_zendesk_status_core.py>) — Pure unit tests for src.services.zendesk_status_core. No I/O, no DB, no FastAPI. This module is a verbatim copy of services/backend-api/src/services/zendesk_status_core.py; these tests must…
- [test_zendesk_status_sync.py](<../services/worker-service/tests/test_zendesk_status_sync.py>) — TDD tests for src.tasks.zendesk_status_sync (poll-first inbound Zendesk status-sync poller) — poll-task aspect of zendesk-status-sync. See…
- [test_zendesk_sync.py](<../services/worker-service/tests/test_zendesk_sync.py>) — TDD tests for zendesk_sync tasks and _sync_org core (ingestion-pull aspect). Phase 1 (worker ZendeskIntegration model + column parity) was already delivered by the ingestion-core aspect —…

## `services/worker-service/tests/fixtures`

[Directory guide](<../services/worker-service/tests/fixtures/directory.md>)

- [automation_action_support.json](<../services/worker-service/tests/fixtures/automation_action_support.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [intercom_webhook_envelope.json](<../services/worker-service/tests/fixtures/intercom_webhook_envelope.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [intercom_webhook_rating_envelope.json](<../services/worker-service/tests/fixtures/intercom_webhook_rating_envelope.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.
- [intercom_webhook_reply_envelope.json](<../services/worker-service/tests/fixtures/intercom_webhook_reply_envelope.json>) — Configuration or structured fixture; inspect named settings and consumers before changing it. Secret values must remain outside tracked configuration.

