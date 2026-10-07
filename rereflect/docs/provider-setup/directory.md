# Directory guide: provider-setup

FeedSignal owner app-registration material. No actual secret belongs here.

- [slack-manifest.json](slack-manifest.json): FeedSignal bot, six posting/history/channel-selection grants, owner API callback, signed event URL and message subscriptions. Reload verified these settings on 6 October 2026.

Owner workspace: https://feedsignal.slack.com, team `T0C7136FUE8`. Active FeedSignal app: `A0C6U45DBEZ`. The earlier `A0C7RSCJ7NU` is an unused Demo App; its irreversible PKCE/token-rotation settings are incompatible with the baseline, so leave it untouched. The new app disables both, as the baseline does not implement Slack refresh/PKCE.

Provider keys are private and installed in the owner Render API. Slack verified the event challenge; events `message.channels` and `message.groups` persisted after reload. The API-generated owner authorization completed and integration 1 is active. Channel selection, bot invitation and processed ingestion remain separate checks; the worker is still absent.

Read [deployment status](../OWNERSHIP_DEPLOYMENT_STATUS.md), [launch setup](../LAUNCH_SETUP.md) and [unanswered secrets](../../UNANSWERED_SECRETS.md). Credentials stay in ignored files/provider settings.
