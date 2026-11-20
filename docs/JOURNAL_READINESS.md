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

## Candidate follow-up question

Subject to data rights and a fuller novelty review, a more defensible direction to investigate is:

> How much do within-corpus cross-validation estimates differ from evaluation on an independently collected SMS corpus for fixed, lightweight text classifiers, after checking and removing cross-corpus duplicates?

This is a candidate, not a verified research gap. Before accepting it, the review must determine whether the selected external corpus is legally usable, whether it overlaps with UCI or other known collections, whether its labels are sufficiently compatible, and whether comparable studies have already answered the question. A time-based study would additionally require trustworthy per-message timestamps; do not infer timestamps that are not present.

The 2024 Super SMS dataset is one possible research lead, not an approved data source. The repository's top-level materials inspected in this review do not establish dataset-specific reuse rights. The paper's own CC BY-NC-ND license does not, by itself, establish the dataset's independent reuse terms. Inspect the data directory and obtain a clear license or permission before using, adapting, or redistributing it. No messages have been sent to the maintainers, and no download or modeling on that dataset has been performed.

## Gaps before journal submission

- Complete and document a reproducible literature search, inclusion criteria, and comparison table.
- Establish a research contribution that is distinct from prior benchmark, robustness, evasion, and dataset-quality studies.
- Verify explicit data licenses and provenance for every added corpus; obtain permission where the terms are unclear.
- If adding external data, audit exact and near duplicates across corpora before splitting or evaluation.
- Predefine the evaluation protocol before the final evaluation; report positive-class metrics, confusion matrices, appropriate uncertainty estimates, and error analysis.
- Keep the distinction between spam, smishing, and verified fraud explicit; only make claims supported by the chosen labels.
- Select a target journal only after the research question and contribution are settled, then follow its current author instructions.
- Complete author, funding, conflict-of-interest, contribution, ethics, and data-availability declarations truthfully.

## Decision rule

Continue in the SMS domain if the literature review identifies a specific open question and an accessible dataset with clear rights. If either condition fails, keep the current work as an honest portfolio/capstone paper and select a new topic for journal-oriented research before expanding the experiments. Do not claim that the current draft is ready for submission or likely to be accepted.