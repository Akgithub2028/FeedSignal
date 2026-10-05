# Public datasets for FeedSignal development

Checked: **6 October 2026**. [Upstream application](https://github.com/haqaliz/rereflect). M0 requires a sourced dataset shortlist and a usable development corpus under the owner's revised research scope. It does not require private-team exports or model training.

## Selection and actual acquisition

| Dataset | Publisher-reported scale / labels | Provenance and fit | M0 state |
|---|---|---|---|
| [Banking77, PolyAI](https://github.com/PolyAI-LDN/task-specific-datasets) | 13,083 utterances; 77 intents; 10,003 train / 3,080 test. [Paper](https://arxiv.org/abs/2003.04807) | Banking queries with intent labels. Useful for import robustness and distinguishing similar support problems; lacks SaaS accounts/revenue/time context. | **Downloaded and checked locally.** |
| [Bitext customer-support dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset) | 26,872 question/answer pairs; 27 intents. Card says ten categories, while viewer lists eleven values: inspect raw values before mapping. | Publisher explicitly describes hybrid synthetic generation. Useful for typos and varied support language; not observed SaaS buyer behavior. | Card, file listing and license checked; **not downloaded**. |
| [ABCD, ASAPP Research](https://github.com/asappresearch/abcd) | Over 10,000 human-to-human dialogues; 55 intents. | Policy-constrained support dialogues collected through Expert Live Chat. Scenario-based collection; not tiny SaaS production logs or demand evidence. | README and repository license checked; **not downloaded**. |

These are different units and domains; do not total them as verified customer accounts, opportunities, or commitments. None provides a representative B2B SaaS account/revenue benchmark. Do not use account creation, support refunds or cancellation intents as willingness-to-pay labels.

## Banking77 local package and attribution

Files are in [datasets/banking77](datasets/banking77/directory.md): [train.csv](datasets/banking77/train.csv), [test.csv](datasets/banking77/test.csv), [categories.json](datasets/banking77/categories.json), [original license](datasets/banking77/LICENSE), [source manifest](datasets/banking77/source_manifest.json), and [quality report](datasets/banking77/quality_report.json).

Credit: **PolyAI; Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson and Ivan Vulić**, *Efficient Intent Detection with Dual Sentence Encoders* (2020). Data files are byte-for-byte upstream copies, unchanged, obtained via the GitHub connector because the shell could not resolve the external host. Original Git blob SHA-1 and local SHA-256 identify every file; `master` is the requested branch, not an immutable commit ID. Hash verification pins the acquired bytes without pretending the branch is immutable.

The publisher assigns CC BY 4.0 to the datasets. Preserve attribution, license and change notices on derivatives; this data's license is separate from the application's MIT license. [Publisher license](https://github.com/PolyAI-LDN/task-specific-datasets/blob/master/LICENSE), [CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/).

## Measured data quality

Parsing the local copies found the expected `text,category` schema, all 77 declared labels, and zero empty texts in either split. Using case folding and whitespace normalization:

| Check | Train | Test |
|---|---:|---:|
| Records | 10,003 | 3,080 |
| Unique normalized texts | 9,999 | 3,079 |
| Duplicate rows beyond first occurrence | 4 | 1 |
| Same normalized text with conflicting labels within split | 0 | 0 |
| Longest text, characters | 433 | 368 |

Seven normalized text values overlap between train and test. Keep the original splits for reproducible benchmark comparisons; disclose overlap. For a stricter development holdout, exclude the overlapping test texts in a separately versioned derived split and report the resulting size. Do not silently edit upstream files. Fuzzy duplicates, privacy and demographic representativeness have not been exhaustively audited.

## Rights and acquisition of the other candidates

**Bitext:** the card identifies **CDLA-Sharing-1.0**. Keep provenance and the license link; when publishing original or enhanced data, preserve credit, indicate changes and follow the same agreement's sharing requirements. Computational results have a different treatment from published enhanced data; keep third-party records separately from private customer exports. [Agreement](https://cdla.dev/sharing-1-0/).

Its [file listing](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset/tree/main) contains `Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv`. If an implementer chooses it, download from the publisher, pin the revision/checksum, parse `flags,instruction,category,intent,response`, measure real category values and preserve instructions separately from generated answers. Record the actual row count rather than assuming the viewer is complete.

**ABCD:** the repository publishes code and data together and carries an **MIT license**. Preserve its notice; use the official `data/abcd_v1.1.json.gz` identified by the README and record version/hash before use. Data is organized into train/dev/test conversations with scenario/original/delexed fields. Prefer the delexicalized view for development; preserve speaker and dialogue IDs. [Repository license](https://github.com/asappresearch/abcd/blob/master/LICENSE).

Do not substitute scraped Reddit/X content or arbitrary Kaggle mirrors for a licensed engineering corpus. Public discussions in the research report are qualitative sources, not redistributed training data.

## Natural-language implementation contract for later agents

1. **Keep original data separate.** Never seed these files into a customer's organization or production metrics. Use a demo organization with `is_demo` and visible source-provenance labels; exclude demos from activation, revenue and demand counts.
2. **Adapt without inventing business evidence.** Map text to an input message and original intent to a development label. Set account, contact, revenue, source timestamp and product-specific opportunity labels to unknown. An offline harness may assign isolated technical tenant/message IDs, but must identify them as artificial. Actual CSV mapping must be checked against the app's import contract; these are not promised drop-in seed files.
3. **Separate semantic tests from transport tests.** Replay imports/revisions for idempotency checks; synthetic batch timestamps and duplicates are test conditions, not additional customers. The small local corpus can exercise 13,083 imports; it does not prove throughput or million-event performance.
4. **Protect holdouts.** Tune on train only. For future target-domain data, split by account/conversation and time before prompt tuning, keeping revisions/duplicates together. For Banking77, lack of account IDs makes account-grouped evaluation impossible; use text-overlap analysis and clearly describe that limitation.
5. **Use labels only for their actual task.** Banking intents can benchmark retrieval or classification if an adapter exists; they do not label multi-issue SaaS extraction, urgency, account matching, opportunity merges, churn or brief usefulness. Report macro-F1/retrieval measures separately from the product's evidence and account metrics.
6. **Build missing cases explicitly during M2/M4.** Version a small reviewed target-domain fixture set covering multi-issue messages, contradictions, unknown identities, negative chatter, delivery retries, quiet weeks and source-text instructions. Label synthetic examples as synthetic. Do not manufacture account ARR or confidence values as real data. A large template-generated corpus alone is not an independent quality benchmark.
7. **Acceptance requires execution later.** M0 checks files, licenses, schema, provenance and quality counts. Import/API/worker/model evaluation is M1–M4 work; no model score or product throughput result has been produced here.

Private-team exports remain optional future evidence with permission, retention and deletion records. They are no longer a prerequisite for M0 completion. Genuine usage and payment checks remain required before broader commercial investment; see [research report](RESEARCH_REPORT.md).
