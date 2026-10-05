# Directory guide: `docs/archive/prd`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Archived PRDs, primarily for shipped features. The archive README explicitly warns that Draft/Planned labels and historical pricing are stale; some Stripe-era plans were retired.

This directory has 20 immediate baseline/preparation files, 0 child directories, and 20 files in its subtree before generated guides/index inventories. Common formats: .md: 20.

## Read first

- [README.md](<README.md>) — Archived PRDs: Historical product requirement documents for features that have **shipped**. They are kept here for provenance — several are cited by name and line number from the per-feature planning
- [PRD-ADVANCED-CHURN-PREDICTION.md](<PRD-ADVANCED-CHURN-PREDICTION.md>) — PRD: Advanced Churn Prediction (M4.1): Turn Rereflect's existing 9-factor heuristic churn score into a **calibrated 30-day churn probability** with a confidence interval, time-to-churn timeline, cohort analytics, and…
- [PRD-AI-COPILOT.md](<PRD-AI-COPILOT.md>) — PRD: AI Copilot — Command Bar & Conversations (M2.2): The AI Copilot gives users a natural-language interface to query, analyze, and understand their feedback data. It consists of two connected surfaces: The Cmd+K modal…
- [PRD-AI-RESPONSE-SUGGESTIONS.md](<PRD-AI-RESPONSE-SUGGESTIONS.md>) — PRD: AI Response Suggestions (M2.3): When a team member reviews a feedback item, they often need to respond to the customer — acknowledge a bug, thank them for a feature suggestion, or reach out proactively to an…
- [PRD-AI-WORKFLOW-AUTOMATION.md](<PRD-AI-WORKFLOW-AUTOMATION.md>) — PRD: AI Workflow Automation (M4.4): Teams using Rereflect identify churn risks, critical bugs, and urgent feedback — but then must manually assign, escalate, and respond to each one. A CS lead seeing a customer's health…
- [PRD-CHURN-PREDICTION-ACCURACY.md](<PRD-CHURN-PREDICTION-ACCURACY.md>) — PRD: Churn Prediction Accuracy: Make churn predictions transparent, trustworthy, and measurable. Today, users see a single churn risk score (0-100) with no explanation of why it's high or low, no indication of how…
- [PRD-CUSTOM-WEBHOOKS-AND-TECH-DEBT.md](<PRD-CUSTOM-WEBHOOKS-AND-TECH-DEBT.md>) — PRD: Custom Webhooks & Technical Debt (M3.1): Rereflect users who want to automate workflows based on feedback events (e.g., post to Discord, trigger a Zapier flow, update an internal dashboard, page oncall) currently…

## Files, children, and contracts

[Complete file inventory](<../../DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Document sections to inspect: 1. Overview; Strategic context; 2. Goals; 1. Problem Statement; Current State; Part A: Custom Webhooks.

## Inputs, outputs, and change safety

Inputs are source contracts, requirements, or operational evidence; outputs are guidance/assets or CI configuration, not new product features. Keep historical evidence dated. Never record real secrets or private customer data in tracked documentation. Check factual claims against the current implementation and preserve upstream license attribution.

## Verification and limits

Check relative links, complete guide coverage, placeholder consistency, and git diff --check. For CI/deployment changes, read service build and environment contracts before attempting execution.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
