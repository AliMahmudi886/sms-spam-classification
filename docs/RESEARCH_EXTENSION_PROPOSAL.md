# Research Extension Proposal: SMS-Length-Bounded Prompt-Injection Evaluation

**Protocol version:** 0.2
**Status:** Narrow candidate for further screening; novelty and feasibility are not established.
**Review date:** 2026-11-22

## Motivation

The existing app uses a classical TF-IDF Logistic Regression model, which does not follow natural-language instructions. An LLM-based SMS assistant would introduce a different risk: the message body is untrusted input and may contain text that attempts to override the classifier's task.

The broad question of prompt injection against phishing classification is already directly addressed in recent email work, including a November 2026 staged-inference protocol with clean, injected-phishing, and injected-legitimate conditions. In addition, a 2026 Findings of IJCNLP-AACL paper evaluates prompt-trigger defenses on an SMS Spam test split, and an August 2026 preprint compares traditional and instruction-following classifiers under prompt injection on the SMS Spam Collection. Generic SMS prompt-injection evaluation is therefore not a defensible novelty claim. The remaining possibility is narrower: characterize the injection-length budget and label-flip behavior under standard single-part and concatenated-SMS encoding limits. No gap is established; this requires a broader, documented related-work search and supervisor review before any experiment. SMS segment limits are specified by 3GPP; GSM-7 and UCS-2 have different capacities. [3GPP TS 23.040](https://www.etsi.org/deliver/etsi_ts/123000_123099/123040/17.02.00_60/ts_123040v170200p.pdf) [UniGuardian, ACL Anthology](https://aclanthology.org/2026.findings-aacl.119/) [Asif, 2026 preprint](https://doi.org/10.5281/zenodo.21939849)

## Candidate research question

> For GSM-7 messages in the UCI spam/ham corpus, how do classifier-directed text length and estimated SMS segment count relate to paired label-flip rates in a fixed LLM triage setup, and how do the measured outcomes compare with length-matched neutral insertions and a non-instruction-following TF-IDF control?

UCS-2 is descriptive only in this corpus: just six unique messages are labeled `spam`, so the data do not support a useful class-balanced UCS-2 primary analysis. A future UCS-2 study would require a separately sourced dataset that passes independent license, provenance, and privacy review.

The research object is **channel-length-bounded classification integrity**. The comparison is between predeclared inference conditions over the same paired message variants, not a claim that one model family is generally safer.

## Scope and threat model

- The model receives a user-provided SMS body and returns only a fixed label from the dataset task, plus a brief safe-use notice.
- The SMS body is untrusted data. It may contain quoted or direct instructions such as requests to ignore the classification task or force a particular label.
- Test length bands must distinguish one-part GSM-7 (up to 160 septets), one-part UCS-2 (up to 70 code units), and concatenated message parts (typically 153 GSM-7 or 67 UCS-2 units per part when concatenation headers are used). Count encoded units, not just Unicode code points; specify the exact encoding/counting implementation and do not generalize beyond it.
- Segment count is a transport-cost measure, not necessarily an LLM input cap: many phones reassemble concatenated SMS before an app reads the body. Report both payload units and estimated SMS parts; do not claim a message stops at one segment.
- The evaluator has no access to model internals. The test measures output changes under paired clean and injected inputs.
- No tools, browsing, message sending, file access, account access, or external actions are available to the evaluated model.
- Attack strings are short, self-authored, non-operational test fixtures. They do not contain instructions for theft, malware, credential collection, or real-world targeting.
- Findings apply only to the tested model versions, prompts, message samples, and injection fixtures.

## Candidate hypotheses

1. Attack-induced label flips may vary with appended GSM-7 septet count and estimated SMS segment count; any observed effects apply only to the tested model/message pairs.
2. Direct and selected published defense conditions may have different label-flip and false-alarm curves as the inserted text length changes, if the comparison can be reproduced fairly.
3. The existing TF-IDF Logistic Regression model will not follow the instruction as an instruction, although added words can still change its lexical score. It is a non-instruction-following control, not a security guarantee.
4. A condition that reduces flips may also raise false alerts on legitimate messages or affect clean-message performance; all must be measured.

These are testable expectations, not assumed results.

## Data and rights plan

| Source | Proposed role | Terms and limits | Gate |
|---|---|---|---|
| [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection) | Initial clean-message base for the existing `spam`/`ham` task. | UCI lists CC BY 4.0. The corpus is historical and has no separate scam label. | Preserve the current downloader/checksum and attribution. The project records an author-notification request; no notification is evidenced. Do not call `spam` a confirmed scam label. |
| [Mishra & Soni SMS Phishing dataset](https://data.mendeley.com/datasets/f45bkkt8pr/1) | Optional later `ham`/`spam`/`smishing` challenge, only after provenance and archive access review. | The landing page lists CC BY 4.0 and says text was extracted from Internet images. The record is not proof that the classes are independently adjudicated or free from overlap with UCI. | Do not download or train until the official archive is accessible, label definitions are appraised, and examples are checked for personal data and duplicates. |
| [IMC 2025 Smishing artifact](https://github.com/reportsmishing/Smishing-Dataset-IMC25) | Optional positive-only smishing sensitivity check, not a complete test set. | The repository states CC BY 4.0 and calls its release pseudo-anonymized. The associated [IMC paper](https://doi.org/10.1145/3730567.3764431) describes collection from public user reports. | Review actual fields and sample content for residual personal data and language/source bias before use. Positive-only data cannot yield precision, F1, specificity, or false-positive rates. |

No dataset files were downloaded for this proposal. Do not commit raw message text. Record source/version, retrieval date, checksum, license, attribution, transformations, and privacy review before any experimental use.

The first candidate pilot should use only the existing UCI `spam`/`ham` task and inspect how many messages fall into each SMS encoding and length band. Do not manufacture a UCS-2 sample by appending arbitrary Unicode characters to messages. If authentic UCI text does not provide enough UCS-2 cases for a meaningful paired comparison, report that feasibility limit and constrain the primary experiment to GSM-7 rather than implying a balanced encoding study.

The count-only feasibility audit is reproducible from the checked-in script after the official dataset has been retrieved and checksum-verified:

```bash
python scripts/audit_sms_encoding_feasibility.py
```

The script does not download or modify data, train a model, or create attack fixtures. It rejects a dataset whose SHA-256 does not match the corpus recorded in `DATASET.md` and uses the same `estimate_sms_length` function as the app.

### Read-only UCI encoding feasibility check (2026-11-22)

The already-present official UCI file was parsed locally for this count-only audit; it was not downloaded again, modified, or used to train a model. After exact-text deduplication, the 5,171 unique messages yielded 5,082 GSM-7 candidates (4,435 `ham`, 647 `spam`) and 89 UCS-2 candidates (83 `ham`, 6 `spam`). Thus UCI does **not** support a class-balanced UCS-2 comparison; report UCS-2 only descriptively or exclude it from the primary comparison.

Of the GSM-7 messages, 4,248 `ham` and 594 `spam` fit in one part as-is. For a one-part message, 3,852 `ham` and 158 `spam` messages have at least 30 septets of spare capacity; 3,482 `ham` and 73 `spam` messages have at least 60. These are simple capacity counts before adding separators or validating any instruction text. They are not attack-success results or a guarantee that a meaningful payload fits. The practical candidate is therefore a primarily GSM-7 length-budget study, with conservative sample-size/error-bar planning required for the smaller positive-class subset. No model was queried and no test fixture was created.

The initial draft of this count recorded 3,858 `ham` messages at the 30-septet threshold. Re-running the documented septet-aware implementation produced 3,852; this proposal uses the reproducible script output as the corrected value.

## Experimental design (draft)

### Paired input conditions

For each selected GSM-7 message, create matched variants whose underlying message text and gold label remain unchanged. Restrict the primary injected and neutral text to GSM-7 default/extension characters so the added text does not silently switch a sample to UCS-2. Compute the base text's septets and available capacity with the checked-in estimator. Stratify or block by original label and remaining capacity. Vary the inserted text length across preregistered septet bands, including around the single-part boundary. If paraphrases of the same directive are used to reach a tier, label them as separate templates; do not treat length as an isolated causal variable when wording also changes. Keep UCS-2 examples out of the primary analysis and report their scarcity descriptively.

1. **Clean:** original message with the fixed classification instruction.
2. **Neutral control:** a similarly sized, non-instructional appended note, to separate instruction effects from simple length changes.
3. **Embedded instruction:** a self-authored line requesting the model to ignore the task or emit a specified label.
4. **Defense baselines:** compare direct classification, a generic untrusted-input instruction, and the published injection-first staged procedure if its exact protocol can be reproduced from the paper. Keep prompts and parsing rules fixed across length bands.
5. **Length-matched neutral controls:** for every directive template, include a harmless text insertion matched for encoded length and position. This helps distinguish instruction following from ordinary length/lexical effects.

All fixture variants must be frozen before model calls. A small human review should verify that each transformation preserves the original label-relevant message and that length-tier paraphrases retain the same directive intent. Report exclusions and ambiguous cases.

### Comparators

- Existing Logistic Regression model as the non-instruction-following control.
- A small, locally runnable instruction-tuned model with a pinned model revision and decoding settings, if hardware permits.
- A second independently developed model only if it can be run reproducibly without introducing an unbudgeted paid API dependency.

Do not select models after seeing attack results. If local inference is not feasible on the available machine, stop at the protocol and revise the feasibility plan before using a paid hosted model.

### Primary and secondary measures

- **Primary:** paired label-flip rate by injected GSM-7 septets/UCS-2 code units and estimated SMS parts; also report `spam → ham` separately.
- **Clean utility:** per-class precision, recall, F1, confusion matrix, and macro-F1 on the untouched evaluation split.
- **Robust utility:** accuracy/F1 across injected variants with confidence intervals clustered by original message, so variants of the same base message are not treated as independent.
- **Controls:** label-flip rate on neutral variants and false alarm changes on legitimate (`ham`) examples.
- **Interface reliability:** percentage of responses matching the permitted schema; do not count a refusal or malformed answer as a correct label.
- **Resource cost:** inference latency and token/resource use for each pinned local configuration.

The original UCI split remains the baseline. Paired variants must stay in the same partition as their source message. No prompt or mitigation may be tuned on the final evaluation messages.

## Candidate mitigation conditions

Compare the direct and defense baselines described above, including the published injection-first condition if reproducible. Keep tools disabled for every condition. These are test conditions, not assumed defenses; prompts, delimiters, and output parsing must not be described as complete security solutions.

## Novelty screen so far

- The 2026 *International Journal of Information Security* study evaluates English and Korean SMS LLM classifiers, multiple prompting strategies, temporal drift, and semantic-preserving adversarial edits. The accessible method describes evasion/perturbation attacks but the targeted search did not find an explicit SMS-body instruction-override condition. This does not prove the full paper or supplementary materials omit it. [Publisher full text](https://link.springer.com/article/10.1007/s10207-026-01283-5)
- Zhu and Liu (2026) directly study classifier-directed prompt injection in phishing emails and propose injection-first staged inference, with clean phishing, injected phishing, and matched injected legitimate email conditions. This directly overlaps the broad version of the current idea. Only the SMS encoding/segment-budget dimension remains a candidate distinction, and it has not been shown novel. [Publisher chapter and paper](https://publications.scrs.in/chapter/978-81-975670-4-9/3) · [full text](https://publications.scrs.in/uploads/final_menuscript/48c37c6c7d5b17d2ba27def123aeca9c.pdf)
- Borkowski (2025) reports proof-of-concept prompt-injection simulations against LLM-based spam filters using progressively modified phishing email messages and several commercial/open models. The accessible chapter explicitly defines its spam task around email, so it is not direct evidence on SMS segment limits; it does show that generic “prompt injection against an LLM spam filter” is already studied. [DOI record](https://doi.org/10.15611/2025.07.4.02) · [author-uploaded chapter text](https://www.researchgate.net/publication/403935032_Prompt_Injection_Attacks_on_LLM-Based_Spam_Filters)
- Koide, Nakano, and Chiba (2026) evaluate stealthy prompt injection in multimodal phishing-site detectors and propose InjectDefuser. It is a different medium and attack surface, but further limits any claim to generic phishing-detector prompt-injection novelty. [arXiv paper](https://arxiv.org/abs/2602.05484)
- An IEEE Security & Privacy 2025 poster evaluates few-shot SMS smishing detection with Gemma-2B, Phi-3 mini, and Qwen2.5-3B, including a 4-bit model and an on-device/privacy motivation. Its accessible text discusses misspellings, inserted tokens, and paraphrased perturbations, but does not explicitly describe classifier-directed prompt-injection tests. It is close work for small-model SMS robustness and makes model size/deployment constraints relevant to the comparison. [IEEE S&P poster](https://sp2025.ieee-security.org/downloads/posters/sp25posters-final23.pdf)
- 3GPP defines different payload capacities for GSM-7 and UCS-2 SMS, with reduced per-part capacity for concatenated messages. This supports an operationally measurable channel-budget variable; it does not by itself establish a research gap. [3GPP TS 23.040](https://www.etsi.org/deliver/etsi_ts/123000_123099/123040/17.02.00_60/ts_123040v170200p.pdf)
- The 2025 USENIX SOUPS paper SmishX uses LLM agents to classify SMS phishing and generate evidence-based explanations, including a user study. It confirms that instruction-following LLMs are already being applied to SMS triage, so an LLM classifier alone is not a contribution. [USENIX paper](https://www.usenix.org/conference/soups2025/presentation/wang)
- SafeBreach publicly reports notification-based indirect prompt injection through SMS and other messaging applications against a voice assistant, with unauthorized device actions. This establishes practical relevance for the broader threat, but it is vendor security research, not evidence that the proposed classification-only experiment is novel or that the tested models share that vulnerability. [SafeBreach research](https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/)

This is a targeted search, not a systematic review. The generic SMS prompt-injection proposal is **not sufficiently distinct** from existing email spam/phishing work to present as novel. The remaining length-budget question is only a candidate; novelty is **unresolved** until scholarly indexes are searched specifically for channel-constrained or length-bounded prompt-injection evaluation in mobile messaging, and the closest papers/artifacts are screened in full. Borkowski studies spam-filter injection, Zhu and Liu study injected phishing email and staged inference, and the IEEE S&P poster studies small SMS models under textual perturbations. The exact variable, controls, and contribution therefore need especially careful comparison; this project must not present “length matters,” “prompt injection breaks spam filters,” or “small models can classify SMS” as new by itself.

## Safety and publication boundaries

- Evaluate only local research models or a separately approved research endpoint; do not paste personal SMS into public services.
- Keep the model sandboxed with no tools or permissions. This protocol evaluates label integrity, not action execution or exfiltration.
- Use synthetic injection strings and public, rights-reviewed examples. Do not publish private messages, phone numbers, identifiers, or attack recipes aimed at real services.
- Report model/version/prompt hashes, random seeds, exclusions, and all conditions, including failures. Do not advertise an attack success rate as representative of deployed assistants.

## Stage plan

1. Search scholarly indexes for SMS/mobile-message prompt-injection work, attack-length budgets, encoding/segment constraints, and email-to-SMS transfer. Read the November 2026 staged-inference paper and artifacts closely.
2. Confirm local inference feasibility and data-rights/privacy gates. No paid API or new dataset access is assumed.
3. If a defensible gap remains, freeze encoding rules, fixtures, splits, prompts, model versions, metrics, and stopping rules before any model query.
4. Implement the research harness separately from the established classifier app and its results.
5. Run an authorized pilot, review paired transitions, and decide whether the evidence supports a paper, a security engineering portfolio artifact, or neither.

No new model, test fixture, result, or claim has been created by this proposal. The existing project remains a portfolio-quality spam/ham demonstration; journal readiness does not increase until the narrowed novelty and data gates are passed and the experiment is actually run.
