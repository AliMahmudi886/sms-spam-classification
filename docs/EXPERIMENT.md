# Experiment protocol

## Research question

On a fixed held-out split of the UCI SMS Spam Collection, how do two classical text classifiers compare on the `spam` class, and how do they compare with a small, transparent rule-based baseline?

## Hypotheses

1. The learned text classifiers will have different precision/recall behavior from the hand-written rule baseline.
2. The two learned classifiers may trade precision against recall for the `spam` class. No model is assumed to win before measurement.

These are questions for this experiment, not claims about all SMS filtering systems.

## Data and split

- Source and licensing record: [../DATASET.md](../DATASET.md).
- Target: the dataset's binary `spam`/`ham` label.
- Preserve the source file unchanged. Inspection found 5,574 rows (4,827 `ham`, 747 `spam`), zero malformed rows, 403 extra rows whose exact message text is duplicated, and no conflicting labels for duplicate text. Remove exact duplicate message texts, keeping the first occurrence, before splitting. Record post-deduplication counts in the experiment output.
- Planned holdout: stratified 80% training / 20% test split after exact-text deduplication, `random_state=42`.
- Fit text preprocessing and vocabulary only on training data, using a pipeline; never fit vectorization on the complete dataset before splitting.
- Keep the test set untouched until model choices and preprocessing are fixed. Do not tune on the test set.

## Comparisons

1. **Rule baseline:** predict `spam` when the message contains a URL beginning with `http://`, `https://`, or `www.`, or contains at least one of these whole-word triggers (case-insensitive): `cash`, `claim`, `congratulations`, `credit`, `free`, `guaranteed`, `loan`, `offer`, `prize`, `reward`, `selected`, `urgent`, `winner`, `won`. Otherwise predict `ham`. Treat it as an illustrative baseline, not a production filter.
2. **Multinomial Naive Bayes:** TF-IDF word unigram and bigram features; `alpha=1.0`.
3. **Logistic Regression:** the same TF-IDF word unigram and bigram representation; `C=1.0`, `solver=lbfgs`, `max_iter=1000`, `random_state=42`. The local demo will use this preselected model so the held-out test scores are not used to select the deployed model.

Both vectorizers use lowercase text and Unicode accent stripping; other `TfidfVectorizer` settings use the documented scikit-learn defaults. No hyperparameter tuning is performed.

Use the same split for each method. Fit vectorization within each learned model's training pipeline. Record package versions and all non-default parameters in the results.

## Metrics and reporting

Treat `spam` as the positive class. Report for each method:

- precision, recall, and F1 for `spam`;
- confusion matrix with explicit axis/label order (`ham`, `spam`);
- accuracy as a secondary summary;
- test-set size and class counts.

The confusion matrix uses true labels as rows and predicted labels as columns, in the order `ham`, then `spam`. Include enough decimal places for comparisons without suggesting unwarranted precision. Explain false positives (ham flagged as spam) and false negatives (spam missed). State that metrics are estimates from one random split and do not prove generalization to newer messages.

## Reporting rule

The research report may include only results produced by the recorded experiment. Any change to the dataset, split, features, rules, or parameters must be documented. No result or citation will be presented as measured or verified unless it has been checked.
