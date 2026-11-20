# Model Card: English SMS Spam Classifier

## Summary

This repository contains an educational text-classification study and a local demonstration app. Its selected demo model is a scikit-learn Logistic Regression classifier using word-level TF-IDF unigrams and bigrams. It predicts the dataset labels `spam` and `ham` for English SMS-like text.

## Intended use

- Learn and demonstrate a reproducible classical machine-learning workflow.
- Explore how a fixed rule baseline, Multinomial Naive Bayes, and Logistic Regression compare on the documented corpus.
- Try a local prediction on English text, with model scores and linear feature contributions presented as limited inspection aids.

The model is not a security product and must not be the sole basis for deciding whether to trust a message, link, sender, or request.

## Out-of-scope use

- Claiming to detect scams, fraud, phishing, malware, or malicious intent. The source labels are only `spam` and `ham`.
- High-stakes financial, legal, security, or other consequential decisions.
- Assuming `ham` means safe or that `spam` identifies a confirmed scam.
- Applying the evaluation to other languages, other message channels, contemporary campaigns, or populations without a new evaluation.
- Treating displayed probabilities as calibrated risk estimates.

## Data

The model uses the public [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection), distributed under CC BY 4.0 according to UCI. Dataset composition, provenance, attribution, retrieval, checksum, and source limitations are documented in [DATASET.md](../DATASET.md). The raw data is downloaded locally and is not committed.

The original corpus has 5,574 rows. Exact duplicate message texts are removed before splitting; 403 duplicate rows were removed, leaving 5,171 unique messages (4,518 `ham`, 653 `spam`). No approximate deduplication or text normalization is used for duplicate detection. The corpus is historical, English-only, and inherits the source collections' sampling and labeling limitations.

## Methods

- TF-IDF word features with unigrams and bigrams, lowercase conversion, and Unicode accent stripping.
- Multinomial Naive Bayes (`alpha=1.0`) and Logistic Regression (`C=1.0`, `lbfgs`, `max_iter=1000`) are evaluated using scikit-learn pipelines.
- The comparison baseline flags a message when it contains a URL or a predeclared English trigger term; its terms are listed in `src/pipeline.py`.
- Stratified five-fold cross-validation with `random_state=42`; each vectorizer is fit only on its training fold.
- The app's selected Logistic Regression model is refit on all 5,171 unique labeled messages after evaluation.
- Exact package versions for the reported Python 3.12 environment are in `requirements.lock`.

See [docs/EXPERIMENT.md](EXPERIMENT.md) for the full protocol and [reports/RESULTS.md](../reports/RESULTS.md) for per-fold values and confusion matrices.

## Evaluation results

Pooled out-of-fold spam-class metrics from the recorded five-fold experiment:

| Method | Precision | Recall | F1 | Fold F1 mean ± sample SD | Accuracy |
|---|---:|---:|---:|---:|---:|
| Rule baseline | 0.780 | 0.591 | 0.672 | 0.673 ± 0.027 | 0.927 |
| Multinomial Naive Bayes | 1.000 | 0.518 | 0.682 | 0.682 ± 0.015 | 0.939 |
| Logistic Regression | 0.998 | 0.677 | 0.807 | 0.806 ± 0.020 | 0.959 |

These results describe only this corpus and protocol. Fold standard deviation is descriptive, not a confidence interval. Cross-validation does not establish performance on current SMS, external data, or scam detection.

## Limitations and risks

- Historical vocabulary and collection procedures may differ from current messages.
- The class balance and content are specific to the dataset; performance can change under distribution shift.
- False negatives are possible: a `ham` output can still be dangerous. False positives are also possible.
- `predict_proba` outputs are not calibrated and should not be read as real-world probabilities of harm.
- The app's feature contribution view decomposes a linear model score over present TF-IDF features. It is not a causal or semantic explanation and does not validate the model's reasoning.
- English-only training limits language coverage.

## Responsible use

Run the app locally and avoid entering private messages into a publicly hosted instance. Verify suspicious requests through an organization's official website or known phone number. Do not use this model as the sole decision-maker in consequential settings. Re-evaluate on an appropriately sourced, permissioned dataset before considering any use beyond education.