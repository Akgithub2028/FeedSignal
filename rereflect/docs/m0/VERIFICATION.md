# M0 verification record

Date: **2026-10-06**. Baseline: `93359c4a2bf20310f98e42d570de50a1586812d8`.

## Verified scope

M0 is complete under the owner's revised **public research and repository preparation** scope. The initial repository preparation was checked on 5 October; this record refreshes the documentation/data checks for the 6 October research addition. No product feature, provider connection, runtime authorization code, Git remote or live database was changed.

| Check | Result |
|---|---|
| Baseline and navigation | 2,321 baseline tracked files and 595 Markdown files; 2,342 baseline/preparation files inventoried, 2,259 nonempty text files read by navigation extraction; no Python parser failures. Binary assets were inventoried, not visually audited. |
| Directory coverage | 546 guides: root + 542 baseline directories + three M0 research/data directories. No missing or unexpected source-directory guides. |
| Local Markdown links | 6,870 local links across 563 preparation/guide/README/workspace Markdown files checked; zero missing targets. External URLs and arbitrary historical links are outside this filesystem check. |
| Placeholder registry | Zero unregistered markers. Fixed a generated summary that truncated a marker by changing the disposable generator to truncate at word boundaries; complete check passes. |
| Environment examples | Seven examples checked; 21 credential assignments empty, no placeholder string assigned as a credential. Secret values were not provided or substituted. |
| Plan synchronization | Canonical and workspace plan copies byte-identical. New handoff references use repository-relative code paths so neither copy contains broken Markdown targets from its different location. |
| Source boundaries | Tracked changes limited to README and existing environment preparation; new artifacts are Markdown and M0 research/data files. No product source change. |
| Dataset acquisition | Banking77: 10,003 train + 3,080 test = 13,083 examples, 77 labels, zero empty texts. Four upstream files match publisher Git blob hashes and manifest SHA-256/size records. License/attribution retained. |
| Dataset quality | Four extra normalized duplicate rows in train, one in test; seven normalized texts overlap across splits. Label distributions checked against quality report. No model score is claimed. |
| Pricing records | 12 structured observations across six products/substitutes; source URLs, 6 October observation date, charging units and annual effective monthly cadence captured. These are public offers, not buyer/payment records. |
| Patch hygiene | `git diff --check` passed. Dataset originals retain publisher bytes, including their line endings. |

Research sources and limitations are recorded in [the research report](RESEARCH_REPORT.md) and [dataset catalogue](PUBLIC_DATASETS.md). Two additional dataset candidates were sourced and assessed, but not downloaded. No generated synthetic corpus or scraped social training dataset was substituted for customer evidence.

## Infrastructure observations carried forward from 5 October

PostgreSQL 16 and Redis are specified in Compose; Railway recipes remain. The earlier probe found no populated deployment environment files, no accessible local listeners on 5432/6379, Docker socket permission denial, and no `psql`, `pg_isready` or `pnpm` on PATH. These are dated setup observations, not newly executed deployment tests or proof about remote provider availability. Original hosted database ownership/access remains unknown.

During dataset acquisition, shell DNS resolution failed for the external host. The read-only GitHub connector successfully retrieved the public Banking77 files instead. Source-byte/hash verification demonstrates that the acquired local copies match the returned publisher blobs.

## Not verified or claimed

No production build, product test suite, migration, backup restore, hosted login, import/API/worker evaluation, model evaluation, Slack message, email, issue creation, live webhook, OAuth installation, database transfer or token revocation was performed. M0 public research completion does not make unresolved deployment credentials production ready.

No founder interview, five-team private feedback review, delivered real-team brief, continued-use commitment or FeedSignal price acceptance was obtained. Those former M0 prerequisites were waived or deferred by the revised scope, not satisfied. Commercial evidence remains unverified and is required at the M2 gate before broader feature investment; see [status](STATUS.md).

## Repeatable handoff checks

- Derive source directories from baseline plus new files, excluding generated guides; require root and every parent directory guide.
- Resolve local Markdown targets from their containing files; ignore external schemes/fragments and check both maintained plan contexts.
- Compare specific unanswered markers with the registry; exclude the ledger filename and generic convention only.
- Parse all seven tracked example environments, requiring private values to stay empty; retain confirmed owner contact and clearly labeled local development values.
- Verify every dataset file's size, Git blob SHA-1 and SHA-256 against its manifest. Parse CSV rather than counting physical lines; compare schema, row/label distributions and normalization overlap with the quality report.
- Parse pricing CSV and distinguish published offers from observed transactions. Compare both plans and run `git diff --check`; inspect source boundaries.

These checks verify documentation and data consistency. Runtime and commercial release claims require the later milestone evidence.
