# Directory guide: `services/worker-service/tests`

**Baseline:** `93359c4a2bf20310f98e42d570de50a1586812d8` · **Updated:** 2026-10-06 · **Product:** FeedSignal

## Purpose and boundary

Automated tests and supporting fixtures for this service/feature. Read the fixtures, imports, test names, and assertions to learn intended boundaries; presence of a test file does not establish that it currently passes.

This directory has 126 immediate baseline/preparation files, 1 child directories, and 130 files in its subtree before generated guides/index inventories. Common formats: .py: 126, .json: 4.

## Read first

- [test_alert_preference_mirror.py](<test_alert_preference_mirror.py>) — Drift-pin for the worker UserAlertPreference mirror. worker-service cannot import backend-api, so its model layer is a deliberate, hand-maintained duplicate of the backend models. The…
- [test_alerts.py](<test_alerts.py>) — TDD tests for send_slack_alert() OAuth token decryption (worker decrypt mirrors). The backend encrypts Slack OAuth tokens at rest in `integrations.oauth_access_token`…
- [test_analysis_classifier_seam.py](<test_analysis_classifier_seam.py>) — Phase 4 RED: Tests for the classifier-override injection at the worker call site (src/tasks/analysis.py::_apply_keyword_analysis / _analyze_feedback_item), the authoritative…
- [test_analysis_llm.py](<test_analysis_llm.py>) — Tests for the LLM-integrated analysis pipeline.
- [test_analysis_winback_integration.py](<test_analysis_winback_integration.py>) — Integration tests verifying that probability_updater and winback_detector are both called from _analyze_feedback_item, and that failures are isolated. Phase 3.2 — TDD GREEN phase. Strategy:…
- [test_anomaly_detection.py](<test_anomaly_detection.py>) — Tests for anomaly detection logic.
- [test_anomaly_integration.py](<test_anomaly_integration.py>) — Integration tests for anomaly detection with real SQLite database. Tests _check_org_for_anomaly, _dispatch_anomaly_alerts, detect_sentiment_anomalies.

## Files, children, and contracts

[Complete file inventory](<../../../docs/DIRECTORY_FILE_INDEX.md>) lists every baseline/preparation file by directory; [guide index](<../../../docs/DIRECTORY_GUIDE_INDEX.md>) links every child and sibling guide.

Direct children: [fixtures](<fixtures/directory.md>).

Direct declarations (navigation cues, not execution results): test_alert_preference_mirror.py: test_user_alert_preference_mirror_has_channel_teams_column; test_alerts.py: _encrypt, _make_org, _make_oauth_integration, _make_feedback, _call_send_slack_alert; test_analysis_classifier_seam.py: _reset_caches, _make_feedback, _set_classifier_mode, _add_active_model, TestOffByteStability; test_analysis_llm.py: TestAnalyzeWithLLM, TestApplyLLMResult, TestRetryLLMAnalysis; test_analysis_winback_integration.py: _make_feedback, _make_prob_mock, _make_winback_mock, test_analyze_feedback_calls_probability_updater_after_update_customer_health,….

## Inputs, outputs, and change safety

Inputs include validated API/task payloads, organization-scoped database rows, and configured providers; outputs include records, normalized analysis, scheduled work, or responses. Verify organization identity in query, cache, job, and webhook paths. Preserve transactions, retry/idempotency contracts, and encrypted credential handling; workers must not assume backend imports exist.

## Verification and limits

Run the relevant existing tests from the service root using its configured dependencies. Read real assertions and fixtures; do not mark tests passing from this inventory.

This summary was generated from tracked filenames, source declarations/module documentation, and document headings/prose, then sampled for navigation quality. It is not a full semantic audit or a runtime verification. Read actual files before editing. Missing owner settings and validation evidence remain in [UNANSWERED_SECRETS.md](<../../../UNANSWERED_SECRETS.md>).
