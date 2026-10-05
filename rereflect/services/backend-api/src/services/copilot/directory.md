# Directory guide: `services/backend-api/src/services/copilot`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Copilot query, conversation, intent, prompt, and execution logic. M1 must reproduce timeout/tenant-isolation concerns; a Python thread timeout is not proof that PostgreSQL cancelled a query.

This directory has 14 immediate baseline/preparation files, 0 child directories, and 14 files in its subtree before generated guides/index inventories. Common formats: .py: 14.

## Read first

- [__init__.py](<__init__.py>) — AI Copilot query engine — intent classification, SQL generation, safety guardrails, and self-learning template system.
- [action_proposer.py](<action_proposer.py>) — Deterministic action proposer for the AI Copilot (M2.2). Pure, synchronous proposal logic: inspects a SQL result's columns to decide which registry actions apply and builds the `actions`…
- [action_registry.py](<action_registry.py>) — Copilot action registry (copilot-suggested-actions, PRD M1/M5). The registry is the ONLY dispatch path for copilot-suggested actions: a stable `action` id maps to an `ActionEntry` declaring…
- [context_resolver.py](<context_resolver.py>) — Context Scope Resolver — builds LLM context based on selected scope + @mentions. Scopes: all_data, feedbacks, customers, pain_points, feature_requests, dashboard @mentions: @customer:email,…
- [intent_classifier.py](<intent_classifier.py>) — Intent Classifier — classifies user messages into data, analysis, or general intents. Classification approach: 1. Rule-based regex patterns (fast, no LLM cost) 2. If ambiguous (low…
- [llm_resolver.py](<llm_resolver.py>) — LLM resolver for the Copilot's answer-generation path. Mirrors the worker-service's local/keyless pattern (worker-service/src/llm/org_resolver.py) but lives in backend-api to avoid…
- [report_generator.py](<report_generator.py>) — Report Generator — generates structured report data for On-Demand AI Reports (M2.4). Supports 4 report types: - executive_summary: High-level overview for leadership - customer_health:…

## Files, children, and contracts

[Complete file inventory](<../../../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct declarations (navigation cues, not execution results): action_proposer.py: extract_customer_emails, propose_actions; action_registry.py: UnknownActionError, InsufficientRoleError, ActionEntry, get_entry, require_role; context_resolver.py: ContextResolver; intent_classifier.py: _score_patterns, IntentClassifier; llm_resolver.py: LLMConfig, resolve_generation_llm; report_generator.py: _matches_any, ReportGenerator.

Cross-service filename matches: `report_generator.py`. Compare backend/worker semantics and model columns before changing these; filename matches do not prove equivalent implementations.

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Use focused backend pytest checks for changed contracts; use real PostgreSQL for migration, transaction visibility, and database timeout behavior. CI also checks a clean migration and a single Alembic head.

M1 issue: reproduce SQL timeout/cancellation and organization-scope enforcement with real PostgreSQL; do not declare an exploit or fix from a summary alone.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../../../UNANSWERED_SECRETS.md>).
