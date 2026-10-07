# Shared customer-health scorer: design for review

Status: **design only; implementation is not authorized by this document**. Owner approved preparing this design on 7 October 2026. Repository: [Akgithub2028/FeedSignal](https://github.com/Akgithub2028/FeedSignal). Keep the current $0 Vercel/Render development topology.

## Problem and required outcome

Actual worker logs show `customer-health recompute is UNAVAILABLE`. `worker-service/src/services/health_recompute.py` imports a backend-only module that is absent from its image. Analysis, usage ingestion and HubSpot enrichment commit their primary work, but the customer's derived health score does not refresh. Existing tests often insert a fake scoring module and therefore hide the deployment failure. GitHub issue #3 is broader than CRM scoring alone.

Keep one scoring implementation for both processes. A worker-triggered recomputation must have the same score, history, segment, alert, automation and opted-in HubSpot writeback behavior as a backend-triggered recomputation. Do not remove side effects to make importing the scorer succeed. Do not import the FastAPI application or copy all backend code into the worker.

## Verified integration points

- Canonical current implementation: `services/backend-api/src/services/health_score_service.py`.
- Worker seam: `services/worker-service/src/services/health_recompute.py`; callers in `tasks/analysis.py`, `tasks/usage_metrics.py`, and `tasks/hubspot_sync.py`.
- Backend models live in separate modules; worker models mostly live in `src/models/__init__.py`. Both already contain health/history, feedback, org AI config, usage and HubSpot mappings. Verify every field/query dependency before extracting; matching table names alone are insufficient.
- Segment/usage helpers already exist in both services. Health alert delivery already exists in worker `src/notification_dispatch.py`; backend delivery is `src/notification_dispatch_helpers.py`.
- Backend `AutomationEngine` invokes `health_score_threshold` and `churn_risk_level_change`. The support-matrix fixture permits **send_notification, run_playbook, send_customer_email** for both. Worker already implements these actions for other triggers. Reuse those handlers; share health-trigger policy rather than creating another policy mirror.
- The scorer's writeback queues only opted-in HubSpot work. Retired Salesforce dispatch must remain disabled.

## Selected structure

Add a small importable `feedsignal_health` package under `services/shared-health/`, copied into both existing Docker images and included in local test import paths. No published package, new production dependency, additional cloud service or database migration is required by this design.

1. **Canonical scoring/orchestration module.** Move the existing component calculations, weights, confidence, risk boundaries, upsert/history decisions and orchestration into this package. Preserve numeric defaults and public return dictionaries. Keep the caller's database session and current transaction boundaries.
2. **Explicit host bindings.** The core receives the specific ORM classes it queries and three required effects: health-alert delivery, health-automation evaluation and HubSpot task enqueue. These are narrow typed bindings, not a generic plugin/service framework. No optional no-op effect. Backend binds its existing models/helpers; worker binds its existing models/handlers. Pure segment/usage calculations also come from one shared source for this path.
3. **Shared health automation policy.** Extract only the two health triggers' condition evaluation, mode gating, cooldown keys and execution/statistics policy. Keep other backend automation triggers unchanged. Use each host's existing action handlers for the three supported actions. Unsupported/misconfigured actions remain explicit failures; shadow/off never send messages. Do not duplicate action code or silently skip an enabled rule.
4. **Compatibility entry points.** Keep `src.services.health_score_service.update_customer_health(org_id, customer_email, db)` and existing scoring function contracts in the backend. Replace their internals with thin shared-package delegates. Give the worker seam a real binding to the shared scorer; remove its permanent import-failure path only after actual image import tests pass. Preserve legitimate existing patch seams while updating tests that relied on fake production availability.
5. **Packaging verification.** Both Docker build contexts are already `rereflect/services`; add only the shared-package copy/import path. CI and local tests must use the same package source. Do not download sentiment models or raise free-service memory requirements as a side effect.

## Invariants and failure behavior

- Every feedback/usage/CRM/health/history/rule query includes the requested organization and customer. Identical email addresses across tenants cannot share records or actions.
- Keep usage/CRM opt-in weights and neutral missing-data behavior. Keep history's significant-change threshold, recovery/drop alerts, confidence and segment rules.
- Preserve shared Redis DB1 cooldown keys (`automation_cooldown:{rule_id}:{customer_email}`) across API and worker. Repeated recomputations must not duplicate eligible alerts or automation actions beyond existing documented semantics. Test concurrent same-customer updates before claiming retry safety; introduce row locking only if the existing flow requires it.
- Honor active/shadow/off, action support, notification preferences, owner/customer email policy, and HubSpot writeback opt-in. No test sends to customers under the current owner-only sender.
- Preserve rollback/commit ordering. Primary ingestion must not disappear because a derived update fails. Keep actual scoring failures observable and compatible with the caller's existing retry policy; do not convert failures into success.
- Do not introduce backend HTTP callbacks, shared admin JWT credentials, a new task broker, or a second scheduler.

## Implementation and acceptance sequence

1. Inventory exact scorer callers, model fields and both effect handlers. Write parity fixtures before extraction. Pin a clock and representative feedback/usage/CRM/rule data, including two tenants with the same email.
2. Extract numeric/query core and introduce explicit host bindings. Run existing backend health tests plus identical core vectors through real backend and worker mappings. Compare all returned components, score, risk, confidence, segment and stored history.
3. Extract health-trigger policy and bind existing action handlers. Verify all three actions for both triggers, mode gating, cooldowns, preference routing, opt-in writeback and failure recording. Use provider fakes only at actual external boundaries.
4. Replace worker seam; run analysis/usage/HubSpot caller regressions without injecting a fake scorer. Verify both image entry points can import and execute the actual shared code.
5. Review auth/tenant/transaction differences. Build both images. Check free-preview memory after imports; retain the current one-worker/one-Beat configuration.
6. Deploy the reviewed owner branch to API and worker. Use owner-controlled fixtures: feedback analysis, usage update and CRM sync must each change the appropriate persisted health record. Restart both services, replay the fixture and verify history, cooldowns and tenant separation.
7. Update pending/status/directory documentation only after these checks pass. Full backend collection is currently blocked locally by missing SAML dependencies; resolve the test environment or report that limitation explicitly rather than inventing a full-suite pass.

The change is accepted only when both processes use the same implementation and all required effects pass parity checks. Merely removing the error log or producing a numeric score is insufficient.

## Review decision

Approve this design before writing the implementation plan. Particular review points: extraction scope, model bindings, effect parity, concurrent recompute behavior and test environment. Then implement sequentially in the existing owner branch/worktree, preserving unrelated local files and the current deployment resources.
