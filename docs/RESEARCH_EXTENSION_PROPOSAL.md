# Research Extension Proposal: Prompt-Injection Resistance in SMS Triage

**Protocol version:** 0.1
**Status:** Candidate for a scoped pilot; novelty is not established.
**Review date:** 2026-11-22

## Motivation

The existing app uses a classical TF-IDF Logistic Regression model, which does not follow natural-language instructions. Adding an LLM-based SMS assistant would introduce a different risk: the SMS itself is untrusted input, and it may contain text that attempts to override the classifier's task. This could cause a model to label a message incorrectly or violate a required output format.

This extension asks a narrow security question about that instruction/data boundary. It does not propose another generic LLM-versus-classical-model benchmark, generated explanation feature, or claim that prompt injection is a new threat. Existing work already studies SMS LLM classification, prompting, drift, and textual adversarial edits. Separate security research has demonstrated notification-based indirect prompt injection reaching device assistants through SMS. The specific behavior of instruction-like content embedded in an SMS body against an SMS triage classifier remains a candidate gap that needs a fuller literature search.

## Candidate research question

> When an SMS body contains instruction-like text that conflicts with an LLM triage task, how often does the triage label change, and which input-boundary controls reduce those changes while preserving clean-message performance?

The research object is **classification integrity under untrusted message content**. The comparison is between prompt/input-handling conditions, not a claim that one model family is generally safer.

## Scope and threat model

- The model receives a user-provided SMS body and returns only a fixed label from the dataset task, plus a brief safe-use notice.
- The SMS body is untrusted data. It may contain quoted or direct instructions such as requests to ignore the classification task or force a particular label.
- The evaluator has no access to model internals. The test measures output changes under paired clean and injected inputs.
- No tools, browsing, message sending, file access, account access, or external actions are available to the evaluated model.
- Attack strings are short, self-authored, non-operational test fixtures. They do not contain instructions for theft, malware, credential collection, or real-world targeting.
- Findings apply only to the tested model versions, prompts, message samples, and injection fixtures.

## Candidate hypotheses

1. Some instruction-following models will change the requested label more often when an instruction-like string is embedded in the message than under a matched clean or neutral-control condition.
2. Explicitly treating the message as untrusted quoted data and using a structured input boundary will reduce, but may not eliminate, attack-induced label changes.
3. The existing TF-IDF Logistic Regression model will not respond to the *instruction* as an instruction, although added words can still change its lexical score. It will act as a non-instruction-following control, not a security guarantee.
4. A boundary control that reduces label flips may also affect clean-message performance or output-format compliance; both effects must be measured.

These are testable expectations, not assumed results.

## Data and rights plan

| Source | Proposed role | Terms and limits | Gate |
|---|---|---|---|
| [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection) | Initial clean-message base for the existing `spam`/`ham` task. | UCI lists CC BY 4.0. The corpus is historical and has no separate scam label. | Preserve the current downloader/checksum and attribution. The project records an author-notification request; no notification is evidenced. Do not call `spam` a confirmed scam label. |
| [Mishra & Soni SMS Phishing dataset](https://data.mendeley.com/datasets/f45bkkt8pr/1) | Optional later `ham`/`spam`/`smishing` challenge, only after provenance and archive access review. | The landing page lists CC BY 4.0 and says text was extracted from Internet images. The record is not proof that the classes are independently adjudicated or free from overlap with UCI. | Do not download or train until the official archive is accessible, label definitions are appraised, and examples are checked for personal data and duplicates. |
| [IMC 2025 Smishing artifact](https://github.com/reportsmishing/Smishing-Dataset-IMC25) | Optional positive-only smishing sensitivity check, not a complete test set. | The repository states CC BY 4.0 and calls its release pseudo-anonymized. The associated [IMC paper](https://doi.org/10.1145/3730567.3764431) describes collection from public user reports. | Review actual fields and sample content for residual personal data and language/source bias before use. Positive-only data cannot yield precision, F1, specificity, or false-positive rates. |

No dataset files were downloaded for this proposal. Do not commit raw message text. Record source/version, retrieval date, checksum, license, attribution, transformations, and privacy review before any experimental use.

## Experimental design (draft)

### Paired input conditions

For each selected message, create matched variants whose underlying message text and gold label remain unchanged:

1. **Clean:** original message with the fixed classification instruction.
2. **Neutral control:** a similarly sized, non-instructional appended note, to separate instruction effects from simple length changes.
3. **Embedded instruction:** a self-authored line requesting the model to ignore the task or emit a specified label.
4. **Boundary control:** present the same message in an explicit untrusted-content field, with a fixed instruction to classify its contents rather than follow them.

All fixture variants must be frozen before model calls. A small human review should verify that each transformation preserves the original label-relevant message and does not introduce a genuine change of intent. Report exclusions and ambiguous cases.

### Comparators

- Existing Logistic Regression model as the non-instruction-following control.
- A small, locally runnable instruction-tuned model with a pinned model revision and decoding settings, if hardware permits.
- A second independently developed model only if it can be run reproducibly without introducing an unbudgeted paid API dependency.

Do not select models after seeing attack results. If local inference is not feasible on the available machine, stop at the protocol and revise the feasibility plan before using a paid hosted model.

### Primary and secondary measures

- **Primary:** paired label-flip rate from clean to embedded-instruction variants; also report the direction, especially `spam → ham`.
- **Clean utility:** per-class precision, recall, F1, confusion matrix, and macro-F1 on the untouched evaluation split.
- **Robust utility:** accuracy/F1 across injected variants with confidence intervals clustered by original message, so variants of the same base message are not treated as independent.
- **Controls:** label-flip rate on neutral variants and false alarm changes on legitimate (`ham`) examples.
- **Interface reliability:** percentage of responses matching the permitted schema; do not count a refusal or malformed answer as a correct label.
- **Resource cost:** inference latency and token/resource use for each pinned local configuration.

The original UCI split remains the baseline. Paired variants must stay in the same partition as their source message. No prompt or mitigation may be tuned on the final evaluation messages.

## Candidate mitigation conditions

Compare a small preregistered set: raw concatenation, explicit quoted/untrusted-data boundary, and structured-field input with a strict output parser. Keep tools disabled for every condition. These are test conditions, not assumed defenses; delimiters and output parsing must not be described as a complete security solution.

## Novelty screen so far

- The 2026 *International Journal of Information Security* study evaluates English and Korean SMS LLM classifiers, multiple prompting strategies, temporal drift, and semantic-preserving adversarial edits. The accessible method describes evasion/perturbation attacks but the targeted search did not find an explicit SMS-body instruction-override condition. This does not prove the full paper or supplementary materials omit it. [Publisher full text](https://link.springer.com/article/10.1007/s10207-026-01283-5)
- The 2025 USENIX SOUPS paper SmishX uses LLM agents to classify SMS phishing and generate evidence-based explanations, including a user study. It confirms that instruction-following LLMs are already being applied to SMS triage, so an LLM classifier alone is not a contribution. [USENIX paper](https://www.usenix.org/conference/soups2025/presentation/wang)
- SafeBreach publicly reports notification-based indirect prompt injection through SMS and other messaging applications against a voice assistant, with unauthorized device actions. This establishes practical relevance for the broader threat, but it is vendor security research, not evidence that the proposed classification-only experiment is novel or that the tested models share that vulnerability. [SafeBreach research](https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/)

This is a targeted exact-topic search, not a systematic review. The novelty gate remains **unresolved** until the related papers and prompt-injection literature are searched in scholarly indexes and full texts, including any supplementary materials and artifacts.

## Safety and publication boundaries

- Evaluate only local research models or a separately approved research endpoint; do not paste personal SMS into public services.
- Keep the model sandboxed with no tools or permissions. This protocol evaluates label integrity, not action execution or exfiltration.
- Use synthetic injection strings and public, rights-reviewed examples. Do not publish private messages, phone numbers, identifiers, or attack recipes aimed at real services.
- Report model/version/prompt hashes, random seeds, exclusions, and all conditions, including failures. Do not advertise an attack success rate as representative of deployed assistants.

## Stage plan

1. Complete a scholarly search for LLM prompt injection in SMS/phishing classification and classify closest work at the feature-level, not only by title.
2. Confirm local inference feasibility and data-rights/privacy gates. No paid API or new dataset access is assumed.
3. Freeze fixtures, split, threat model, model versions, metrics, and the stopping rule before any model query.
4. Implement the research harness in a separate path; leave the established classical app and its results intact.
5. Run the approved pilot, review errors, and decide whether the evidence supports a paper, a security engineering portfolio artifact, or neither.

No new model, test fixture, result, or claim has been created by this proposal. The existing project remains a portfolio-quality spam/ham demonstration; journal readiness does not increase until the novelty and data gates are passed and the experiment is actually run.
