# Journal Readiness and Research Direction

**Review date:** 2026-11-20  
**Current manuscript:** [PAPER_DRAFT.md](PAPER_DRAFT.md)  
**Current experiment:** [EXPERIMENT.md](EXPERIMENT.md) and [../reports/RESULTS.md](../reports/RESULTS.md)

## Recommendation

Keep the broad SMS spam/smishing area for now, but do not treat the current UCI-only comparison as journal-ready. The current experiment is a sound educational and reproducibility baseline. Its research question—one rule baseline and two classical classifiers on one known corpus—does not yet establish a distinct contribution over the existing literature.

Do not change topic solely because this first draft is not yet suitable for journal submission. First finish a scoped literature review and decide whether a feasible, legally usable evaluation can answer a more specific question. If the needed data or distinct contribution cannot be established, then choose a different research question or a new subject before spending time on journal formatting.

## What the preliminary literature scan shows

This is a focused first-pass scan, not a systematic review.

| Work | Relevance to this project | Consequence for the project |
|---|---|---|
| Almeida & Hidalgo (2011), UCI SMS Spam Collection | The source benchmark used here; it has 5,574 labeled English messages and `spam`/`ham` classes. [UCI record](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection) | A repeated comparison on this corpus should be presented as a baseline replication unless it adds a clearly differentiated analysis. |
| Reaves et al. (2016), *Detecting SMS Spam in the Age of Legitimate Bulk Messaging* | Studies legitimate bulk messaging and reports large gateway collections, while discussing representativeness and privacy considerations. [Paper](https://cise.ufl.edu/~butler/pubs/wisec16.pdf) | Dataset/source-aware evaluation is relevant, but the data include personal and gateway metadata; reuse needs a careful privacy and rights review. |
| Salman, Ikram & Kaafar (2024), *IEEE Access* | Introduces a 67,018-message English dataset and examines evasion, evolution over time, and model robustness. [Paper](https://doi.org/10.1109/ACCESS.2024.3364671) · [Data/code repository](https://github.com/smspamresearch/spstudy) | A simple “compare classic models” or generic robustness claim would overlap with prior work. The top-level repository materials inspected here do not establish dataset-specific reuse terms, so permission and licensing need to be resolved before using or adapting the corpus. |
| Anidjar et al. (2024), *Computers & Security* | Studies an OOD-based, GAN-like approach for extending limited SMS spam datasets. [Paper](https://doi.org/10.1016/j.cose.2024.103998) | A generic OOD/data-augmentation claim also overlaps; any extension must specify a different, testable question. |
| *Key insights into recommended SMS spam detection datasets* (2025), *Scientific Reports* | Compares ten SMS datasets using model performance and dataset-quality characteristics. [Paper](https://doi.org/10.1038/s41598-025-92223-1) | Dataset comparison and dataset-quality recommendations are already being studied; these alone are not a safe novelty claim. |
| Ali et al. (2025), *MOZ-Smishing* | Presents a Portuguese, Mozambique-specific mobile-money smishing benchmark and describes the data as open-licensed. [ACL Anthology paper](https://aclanthology.org/2025.africanlp-1.23/) | It may support a multilingual or domain-transfer direction, but the linked dataset is anonymized in the paper metadata, so the actual files and license have not been verified. Do not use it until verified. |
| Nahapetyan et al. (2024), *On SMS Phishing Tactics and Infrastructure* | Releases a large English SMS-phishing dataset associated with public gateways and labels based on VirusTotal/APWG reports. [Paper](https://bradreaves.net/publication/npc%2B24/npc%2B24.pdf) · [Data repository](https://github.com/wspr-ncsu/sms-phishing) | The repository's MIT license is clear for repository materials, but does not clearly establish rights to the underlying third-party message contents, numbers, URLs, or other included data. The README describes raw messages with destination numbers and campaign URLs/timestamps. This is phishing-only data, so it cannot alone support precision, F1, or a balanced external test. Do not download or use it until provenance, privacy, and data reuse rights are clarified. |
| Mishra & Soni (2022), *SMS Phishing Dataset for Machine Learning and Pattern Recognition* | Mendeley Data V1 reports 5,971 English messages labeled ham (4,844), spam (489), and smishing (638), under CC BY 4.0. [Dataset record](https://doi.org/10.17632/f45bkkt8pr.1) | This is the most promising candidate found so far for further inspection because the record states reuse terms and includes all three labels. However, it says messages were transcribed from Internet images and labeled according to extraction source, and thanks UCI SMS Spam Collection authors for making messages available. It may therefore overlap with UCI and its labels may reflect source-based rather than independently adjudicated ground truth. Do not treat it as an independent external test until provenance, exact/near duplicates, and label definitions are audited. |

## Candidate follow-up question

Subject to data rights and a fuller novelty review, a more defensible direction to investigate is:

> How much do within-corpus cross-validation estimates differ from evaluation on an independently collected SMS corpus for fixed, lightweight text classifiers, after checking and removing cross-corpus duplicates?

This is a candidate, not a verified research gap. Before accepting it, the review must determine whether the selected external corpus is legally usable, whether it overlaps with UCI or other known collections, whether its labels are sufficiently compatible, and whether comparable studies have already answered the question. A time-based study would additionally require trustworthy per-message timestamps; do not infer timestamps that are not present.

The 2024 Super SMS dataset is one possible research lead, not an approved data source. The repository includes data folders, but the inspected repository materials do not state a data-specific license or reuse permission. The paper's own CC BY-NC-ND license does not, by itself, establish the dataset's independent reuse terms. Obtain a clear license or permission before using, adapting, or redistributing it. No messages have been sent to the maintainers, and no download or modeling on that dataset has been performed.

The 2024 NCSU SMS-phishing release is also not approved for this project at this time. Its repository publishes an MIT license, but the README describes raw messages collected from external gateways and includes destination numbers; campaign data also include URLs and timestamps. The license does not expressly resolve the underlying third-party content and privacy questions. In addition, the release is positive-only phishing data, so it could at most be considered later as a carefully governed sensitivity/recall challenge set, not as a standalone test for precision, F1, or a full confusion matrix. This review did not download or inspect message rows. No contact has been made with its authors.

The Mishra & Soni Mendeley record states CC BY 4.0 and describes three classes, but its own provenance notes make independence uncertain: the messages were converted from Internet images, labels were assigned from extraction sources, and the authors thank the UCI SMS Spam Collection contributors for making messages available. A future audit must compare exact and normalized texts against UCI and inspect the dataset's label/source mapping before any experimental use. CC BY 4.0 is recorded as the published dataset license; the provenance and possible overlap caveats remain research-validity concerns, not a claim that the license is unclear. During this review the public landing page was accessible, but the Mendeley file-list API returned HTTP 401 without authentication. No dataset files have been downloaded or used in modeling, so the duplicate audit remains pending access to the official archive.

## Gaps before journal submission

- Complete and document a reproducible literature search, inclusion criteria, and comparison table.
- Establish a research contribution that is distinct from prior benchmark, robustness, evasion, and dataset-quality studies.
- Verify explicit data licenses and provenance for every added corpus; obtain permission where the terms are unclear. NCSU and Super SMS reuse terms remain unresolved. The Mendeley candidate has an explicit CC BY 4.0 record, but provenance, label construction, UCI overlap, and access to its official archive must be resolved before use.
- If adding external data, audit exact and near duplicates across corpora before splitting or evaluation.
- Predefine the evaluation protocol before the final evaluation; report positive-class metrics, confusion matrices, appropriate uncertainty estimates, and error analysis.
- Keep the distinction between spam, smishing, and verified fraud explicit; only make claims supported by the chosen labels.
- Select a target journal only after the research question and contribution are settled, then follow its current author instructions.
- Complete author, funding, conflict-of-interest, contribution, ethics, and data-availability declarations truthfully.

## Decision rule

Continue in the SMS domain for the current portfolio project; do not switch topics just because the draft is not journal-ready. For journal-oriented work, do not expand experiments with the external leads yet. The Mendeley candidate is worth an initial duplicate/provenance audit under its stated CC BY 4.0 terms, but it cannot be presumed independent or label-equivalent to UCI; its official file archive also needs to be retrieved before that audit. NCSU has unresolved rights/privacy and label-coverage limitations, while Super SMS has no verified data-specific reuse terms. If a valid, differentiated question and data protocol cannot be established, keep this work as an honest portfolio/capstone paper and select a different, feasible question before further journal-directed implementation. Do not claim that the current draft is ready for submission or likely to be accepted.

