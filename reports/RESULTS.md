# SMS Spam Classification: Experimental Results

> Results below were produced by `python -m src.train` using the protocol in `docs/EXPERIMENT.md`.
> They summarize one held-out split of the historical English SMS Spam Collection and do not establish performance on current SMS or scam detection generally.

## Data and split

- Raw rows: 5,574
- Duplicate exact-text rows removed before splitting: 403
- Unique messages used: 5,171 (4,518 ham, 653 spam)
- Training/test messages: 4,136/1,035
- Split: stratified 80/20, random state 42; positive class: spam.
- Software: Python 3.12.0, pandas 3.1.1, scikit-learn 1.9.1, joblib 1.6.0.

## Methods

All learned models use TF-IDF word unigrams and bigrams, lowercasing, and Unicode accent stripping. Multinomial Naive Bayes uses alpha=1.0. Logistic Regression uses C=1.0, lbfgs, max_iter=1000, random_state=42. No hyperparameter tuning was performed. The fixed keyword/URL rule baseline is specified in `docs/EXPERIMENT.md`.

## Held-out metrics

| Method | Precision (spam) | Recall (spam) | F1 (spam) | Accuracy |
|---|---:|---:|---:|---:|
| Rule baseline | 0.747 | 0.565 | 0.643 | 0.921 |
| Multinomial Naive Bayes | 1.000 | 0.527 | 0.690 | 0.940 |
| Logistic Regression | 1.000 | 0.656 | 0.793 | 0.957 |

## Confusion matrices

Rows are true labels and columns are predicted labels; order is ham, spam.

### Rule baseline

| True \ Predicted | ham | spam |
|---|---:|---:|
| ham | 879 | 25 |
| spam | 57 | 74 |

### Multinomial Naive Bayes

| True \ Predicted | ham | spam |
|---|---:|---:|
| ham | 904 | 0 |
| spam | 62 | 69 |

### Logistic Regression

| True \ Predicted | ham | spam |
|---|---:|---:|
| ham | 904 | 0 |
| spam | 45 | 86 |

## Interpretation and limits

A ham message predicted as spam is a false positive; a spam message predicted as ham is a false negative. These metrics estimate performance only on this fixed test split. The data is historical, English-only, and labeled spam/ham rather than verified scam/fraud. A single split does not establish performance on newer messages, other languages, or real-world deployments.

## References

Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5CC84>.

Almeida, T. A., Gómez Hidalgo, J. M., & Yamakami, A. (2011). Contributions to the Study of SMS Spam Filtering: New Collection and Results. Proceedings of the 2011 ACM Symposium on Document Engineering. <https://doi.org/10.1145/2034691.2034742>.

Experiment run (UTC): 2026-11-20T10:41:48.274984+00:00
