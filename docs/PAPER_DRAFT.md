# Working Manuscript Draft

> **Status:** Academic-style draft based on the experiment already run in this repository. It is not a journal submission and does not claim a novel algorithm or general fraud-detection capability. The literature review and target venue have not been finalized.

## A Reproducible Baseline Comparison for English SMS Spam Classification on the UCI SMS Spam Collection

### Abstract

Short message service (SMS) spam classification is a useful text-classification task, but results on a single historical corpus should not be interpreted as evidence of current scam-detection performance. This study records a reproducible comparison of a predeclared URL/keyword rule baseline, Multinomial Naive Bayes, and Logistic Regression on the UCI SMS Spam Collection. After removing 403 exact duplicate rows, the evaluation contained 5,171 unique English messages (4,518 ham and 653 spam). Each method was assessed with stratified five-fold cross-validation (`shuffle=True`, `random_state=42`); learned TF-IDF pipelines were fit separately within each training fold. Pooled out-of-fold precision, recall, F1, accuracy, and confusion matrices were reported for the spam class. Logistic Regression obtained the highest pooled spam F1 in this experiment (0.807; precision 0.998, recall 0.677), while missing 211 of 653 spam messages. The results describe this corpus and protocol only. The dataset labels spam and ham rather than verified fraud, and the experiment contains no independent external test set. The contribution is a transparent, reproducible baseline report; further data and evaluation work is needed before a journal-level novelty claim can be made.

**Keywords:** SMS spam; text classification; TF-IDF; Logistic Regression; Multinomial Naive Bayes; cross-validation; reproducibility

## 1. Introduction

SMS remains a channel for both legitimate communication and unsolicited messages. A classifier trained to recognize a dataset's `spam` label does not, by itself, identify fraud or malicious intent. This distinction matters because the UCI SMS Spam Collection provides `spam` and `ham` labels, not a separately verified scam label. The corpus is also historical and combines messages from several sources; its composition does not establish how a classifier would perform on current campaigns or another population [1, 2].

The purpose of this study is deliberately limited: it documents a reproducible baseline comparison on the UCI SMS Spam Collection using a transparent rule, Multinomial Naive Bayes, and Logistic Regression. The research question is:

> Across stratified five-fold cross-validation on the deduplicated UCI SMS Spam Collection, how do a fixed URL/keyword rule, Multinomial Naive Bayes, and Logistic Regression compare on precision, recall, and F1 for the `spam` class?

The work is intended as a baseline study and educational research artifact. It does not propose a new classifier, claim external validity, or infer scam-detection capability.

## 2. Related work and positioning

Almeida and Hidalgo introduced the SMS Spam Collection as a public corpus for SMS spam research; their related study describes the dataset and filtering task [1, 2]. Many later experiments reuse this corpus, so reporting another within-corpus model comparison requires care when making novelty claims.

Recent work has addressed problems beyond a basic within-corpus comparison. Salman, Ikram, and Kaafar released a larger English SMS collection and evaluated model performance against evasive message transformations and changes over time [3]. Anidjar et al. studied data extension for SMS spam using an out-of-distribution approach [4]. Ali et al. introduce MOZ-Smishing, a crowdsourced Portuguese corpus focused on mobile-money smishing, and evaluate large language models with in-context examples [5]. Agarwal et al. analyze messages collected from public user reports and release an artifact for measurement of smishing campaigns and infrastructure [6]. A 2026 IEEE conference paper reports comparing classical models across UCI and modern smishing datasets [7], directly overlapping with a generic cross-dataset extension. A 2026 IEEE Access review reports a broad review and dataset audit of English and non-English SMS corpora, including duplicate-aware split results and a UCI source-overlap audit [8]. Şenol et al. (2026) report a broader UCI-only pipeline spanning eight classifiers, three representations, feature selection, scaling, and class-imbalance strategies [9]. The author-shared pre-proof states that vectorizers were fit on training data, uses a stratified 70/30 split and five-fold CV, and tunes models with GridSearchCV. Its counts differ by one to five records between the abstract and methods tables; its final version should be checked before relying on exact figures. A 2026 *Procedia Computer Science* paper also reports a BERT–character-CNN model and Logistic Regression baseline on the 5,574-message SMS Spam Collection [10]. Its publisher abstract reports 92.8% F1 alongside 0.973 precision and 0.973 recall; these values are inconsistent if they refer to the same positive-class binary averaging, and the full text/protocol was not available to resolve the discrepancy. This abstract is not sufficient for a metric-level comparison. These works show that dataset age, distribution shift, evasion, domain-specific smishing, broad UCI model comparison, and dataset provenance are established research concerns. The present draft therefore positions its findings as a reproducible baseline reference, not as a new solution to those challenges. These studies do not validate the model here or establish its generalization. A generic “new SMS dataset,” “cross-dataset smishing classifier,” or “basic duplicate/provenance audit” framing would need a more specific gap and a separate review of source rights and privacy. The full text of [9] was inspected in an author-shared pre-proof; the full texts of [7], [8], and [10] were not appraised in this pass.

The literature review remains preliminary. In particular, [9] was inspected through an author-shared journal pre-proof because the publisher page was inaccessible during this review; its internal sample-count discrepancies require checking against the final version. For [10], only the publisher abstract was accessible, and the reported summary metrics require clarification from the full paper before they can be interpreted. A journal submission would require a broader, systematic search and a more precise comparison with prior evaluation protocols before asserting any research gap.

A 2026 study now evaluates large language models for English and Korean SMS spam classification, including prompt variants, temporal distribution shift, and adversarial text changes [11]. Its English experiments include the UCI corpus and a newer aggregated SMS dataset. This makes a generic LLM, drift, or adversarial-robustness extension especially difficult to present as a distinct contribution. The article is evidence about prior work, not evidence that its datasets are independently licensed for reuse; this project has not used those data.

Filali et al. (2026) report a broad comparison of classical and neural models, text representations, and GAN/SMOTE/ADASYN augmentation on monolingual and multilingual SMS data [12]. Their work further weakens the case for a generic imbalance-augmentation or cross-lingual extension. It does not validate the present study's UCI-only estimates, and the reported scores are not directly comparable under different data and protocols.

## 3. Data and methods

### 3.1 Dataset and preparation

The dataset was obtained from the UCI Machine Learning Repository. UCI lists 5,574 labeled messages and identifies the dataset license as CC BY 4.0. The repository's [dataset record](../DATASET.md) documents source provenance, attribution, retrieval, and the verified SHA-256 checksum [1].

Inspection found 5,574 rows and 403 additional rows containing repeated exact message text, with no conflicting labels for identical texts. We kept the first occurrence of each exact message text, leaving 5,171 unique messages: 4,518 ham and 653 spam. No text normalization or approximate duplicate grouping was used for deduplication. The raw corpus is not committed to the repository.

### 3.2 Compared methods

The rule baseline predicts spam when a message contains an `http://`, `https://`, or `www.` URL, or at least one predeclared whole-word trigger: `cash`, `claim`, `congratulations`, `credit`, `free`, `guaranteed`, `loan`, `offer`, `prize`, `reward`, `selected`, `urgent`, `winner`, or `won`. Otherwise, it predicts ham.

The two learned models use word-level TF-IDF unigrams and bigrams, lowercase conversion, and Unicode accent stripping. Multinomial Naive Bayes uses `alpha=1.0`. Logistic Regression uses `C=1.0`, the `lbfgs` solver, `max_iter=1000`, and `random_state=42`. No hyperparameter search was conducted. The Logistic Regression model was selected for the local demonstration before evaluation; it was not selected by tuning on these results.

### 3.3 Evaluation protocol

We used stratified five-fold cross-validation with shuffling and `random_state=42`. Each unique message received one out-of-fold prediction. Each learned model was implemented as a pipeline so that the TF-IDF vocabulary and weights were fit only on the four training folds for each iteration. After evaluation, Logistic Regression was refit on all unique messages for the local application. This final fit is not an independent test.

The primary metrics are spam-class precision, recall, and F1. Accuracy is reported as a secondary summary. Confusion matrices use true labels as rows and predicted labels as columns, ordered ham then spam. We report pooled out-of-fold metrics and fold-level F1 mean and sample standard deviation. The fold standard deviation is descriptive and is not a confidence interval.

## 4. Results

Table 1 summarizes the pooled out-of-fold results recorded by the experiment.

| Method | Precision (spam) | Recall (spam) | F1 (spam) | Fold F1 mean ± sample SD | Accuracy |
|---|---:|---:|---:|---:|---:|
| Rule baseline | 0.780 | 0.591 | 0.672 | 0.673 ± 0.027 | 0.927 |
| Multinomial Naive Bayes | 1.000 | 0.518 | 0.682 | 0.682 ± 0.015 | 0.939 |
| Logistic Regression | 0.998 | 0.677 | 0.807 | 0.806 ± 0.020 | 0.959 |

Logistic Regression had the highest pooled out-of-fold spam F1 among these three predeclared methods. Its pooled confusion matrix was 4,517 ham correctly predicted as ham, 1 ham predicted as spam, 211 spam predicted as ham, and 442 spam correctly predicted as spam. Thus, the high precision in this evaluation coexisted with 211 missed spam messages.

The complete fold metrics and confusion matrices are available in [RESULTS.md](../reports/RESULTS.md) and can be regenerated using [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## 5. Discussion

Within this corpus and fixed protocol, Logistic Regression produced a higher pooled spam F1 and recall than the rule baseline and Multinomial Naive Bayes. Naive Bayes produced no false positives in the pooled folds but had lower spam recall. These are differences among the three methods in this experiment; they do not establish that one method is generally superior.

The pooled results and fold variation answer the stated within-corpus question. They do not show performance on a separate population, a later time period, another language, or verified fraud. All messages contributed to one validation fold, and the final application model was then fit on the complete deduplicated corpus. No independent external evaluation or inferential statistical test was performed.

## 6. Limitations

This study has several limitations. First, the corpus is historical and source-specific, and its labels do not distinguish unwanted advertising from verified phishing or fraud. Second, exact duplicate removal does not remove near-duplicate templates or account for source-level grouping. Third, evaluation uses one five-fold split configuration and no independent test corpus. Fourth, the rule baseline is intentionally simple and the learned models use fixed settings without hyperparameter tuning. Fifth, fold-level standard deviation is not a confidence interval, and no statistical significance claim is made. Finally, no conclusion can be drawn about contemporary SMS traffic, scam detection, deployment, or languages other than English.

## 7. Conclusion

This reproducible comparison documents how a fixed rule baseline, Multinomial Naive Bayes, and Logistic Regression performed on the deduplicated UCI SMS Spam Collection under stratified five-fold cross-validation. Logistic Regression obtained a pooled out-of-fold spam F1 of 0.807 in this experiment, while missing 211 spam messages. The result is a corpus-level benchmark observation, not a guarantee for other data or a claim of fraud detection. A journal-level extension would need a distinct and well-supported research question, a broader review of prior work, and a legally usable evaluation design that adds evidence beyond a new comparison on the same benchmark.

## Data and code availability

The project code, evaluation protocol, dataset provenance record, and retrieval script are public in this repository. The raw UCI corpus is not redistributed here; it can be obtained from the [official UCI page](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection) under the terms stated by UCI. Commands for recreating the experiment are in [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Declarations to complete before any submission

- Author names, affiliations, and corresponding author: to be supplied by the author.
- Funding: not recorded in the project materials.
- Conflicts of interest: not recorded in the project materials.
- Author contributions: to be completed by the actual contributors.
- Target journal and formatting requirements: not selected.

## References

1. Almeida, T. & Hidalgo, J. (2011). [SMS Spam Collection](https://doi.org/10.24432/C5CC84) [Dataset]. UCI Machine Learning Repository.
2. Almeida, T. A., Gómez Hidalgo, J. M., & Yamakami, A. (2011). [Contributions to the Study of SMS Spam Filtering: New Collection and Results](https://doi.org/10.1145/2034691.2034742). Proceedings of the 2011 ACM Symposium on Document Engineering.
3. Salman, M., Ikram, M., & Kaafar, M. A. (2024). [Investigating Evasive Techniques in SMS Spam Filtering: A Comparative Analysis of Machine Learning Models](https://doi.org/10.1109/ACCESS.2024.3364671). *IEEE Access, 12*, 24306–24324.
4. Anidjar, O. H., Marbel, R., Dubin, R., Dvir, A., & Hajaj, C. (2024). [Extending limited datasets with GAN-like self-supervision for SMS spam detection](https://doi.org/10.1016/j.cose.2024.103998). *Computers & Security, 145*, 103998.
5. Ali, F. D. M. A., Saide, S. M., Sousa-Silva, R., & Lopes Cardoso, H. (2025). [MOZ-Smishing: A Benchmark Dataset for Detecting Mobile Money Frauds](https://doi.org/10.18653/v1/2025.africanlp-1.23). In *Proceedings of the Sixth Workshop on African Natural Language Processing*, 158–166. Association for Computational Linguistics.
6. Agarwal, S., Papasavva, A., Suarez-Tangil, G., & Vasek, M. (2025). [Fishing for Smishing: Understanding SMS Phishing Infrastructure and Strategies by Mining Public User Reports](https://doi.org/10.1145/3730567.3764431). In *Proceedings of the 2025 ACM Internet Measurement Conference*.
7. Keshavamurthy, T. G., Viswanatha, V., Patel, D. M., Bharathi, J., Birajdar, S. S., & Bharath, B. (2026). [A Multi-Dataset Evaluation of Classical ML for SMS Spam Detection: Balancing Accuracy, Efficiency, and Generalizability](https://doi.org/10.1109/ICSCSA69367.2026.11708017). In *2026 6th International Conference on Soft Computing for Security Applications*.
8. Babu, B. P., Yenduri, G., Sidhardh, S., Kamath, A., Bert, J. G., & Amarsainadh, T. (2026). [Smishing Detection Beyond English Benchmarks: A Critical Review of Code-Mixed Indic Text and On-Device Language Models](https://doi.org/10.1109/ACCESS.2026.3748986). *IEEE Access* (Early Access).
9. Şenol, T., Takcı, H., & Şeker, A. (2026). [SMS spam detection via a systematic machine learning pipeline: Feature engineering, hyperparameter optimizing, scaling, and ensemble learning](https://doi.org/10.1016/j.jer.2026.05.020). *Journal of Engineering Research, 14*(3), 2941–2952.
10. Mishra, V., & Joshi, D. (2026). [Noise-robust SMS spam classification using a hybrid BERT and character-level CNN architecture](https://doi.org/10.1016/j.procs.2026.06.064). *Procedia Computer Science, 282*, 2970–2977.
11. Hur, M., Seo, S., Hwang, J., et al. (2026). [Are large language models effective for detecting spam messages?](https://doi.org/10.1007/s10207-026-01283-5). *International Journal of Information Security, 25*, Article 127.
12. Filali, A., Shorfuzzaman, M., Abdellaoui Alaoui, E. A., Merras, M., Es-Sabry, M., Berrajaa, A., Alroobaea, R., & Yousef, A. (2026). [Cross-lingual SMS spam detection using GAN-based augmentation for imbalanced datasets](https://doi.org/10.1038/s41598-026-37769-4). *Scientific Reports, 16*, Article 7128.
