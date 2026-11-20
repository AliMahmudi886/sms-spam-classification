# Experiment protocol

## Research question

Across stratified five-fold cross-validation on the UCI SMS Spam Collection, how do a transparent rule baseline, Multinomial Naive Bayes, and Logistic Regression compare on the `spam` class?

## Hypotheses

1. The learned text classifiers will differ from the hand-written rule baseline in precision and recall for `spam`.
2. Naive Bayes and Logistic Regression may show different precision/recall trade-offs across folds. No model is assumed to perform best before measurement.

These hypotheses concern this experiment and corpus only.

## Data and preparation

- Source, citation, license, provenance, and inspection record: [../DATASET.md](../DATASET.md).
- Target: the dataset's binary `spam`/`ham` label; `spam` is the positive class.
- Preserve the source file unchanged. Inspection found 5,574 rows (4,827 `ham`, 747 `spam`), zero malformed rows, 403 extra rows with repeated exact text, and no conflicting labels for repeated text.
- Remove exact duplicate message texts before evaluation, keeping the first occurrence. This prevents identical messages from appearing in multiple folds.
- The resulting 5,171 unique messages (4,518 `ham`, 653 `spam`) are evaluated with stratified five-fold cross-validation, `shuffle=True`, `random_state=42`.
- Each unique message receives one out-of-fold prediction. Each learned model's TF-IDF vectorizer is fit only on the other four folds.
- After evaluation, fit the preselected Logistic Regression pipeline on all unique messages for the local demonstration app. The app's training corpus does not create a separate test set.

## Comparisons

1. **Rule baseline:** predict `spam` when the message contains a URL beginning with `http://`, `https://`, or `www.`, or contains at least one of these whole-word triggers (case-insensitive): `cash`, `claim`, `congratulations`, `credit`, `free`, `guaranteed`, `loan`, `offer`, `prize`, `reward`, `selected`, `urgent`, `winner`, `won`. Otherwise predict `ham`. This is an illustrative baseline, not a production filter.
2. **Multinomial Naive Bayes:** TF-IDF word unigrams and bigrams; `alpha=1.0`.
3. **Logistic Regression:** the same TF-IDF word representation; `C=1.0`, `solver=lbfgs`, `max_iter=1000`, `random_state=42`. This model is preselected for the demo; results are not used to choose it.

Both vectorizers lowercase text and strip Unicode accents; other `TfidfVectorizer` settings use scikit-learn defaults. No hyperparameter tuning is performed.

## Metrics and reporting

For each method, report precision, recall, F1 for `spam`, accuracy as a secondary summary, and a pooled out-of-fold confusion matrix. The matrix uses true labels as rows and predicted labels as columns, in order `ham`, then `spam`.

Also report each fold's metrics and the mean and sample standard deviation across the five folds. Pooled out-of-fold metrics are computed by combining the five validation folds, so every unique message contributes one prediction. Fold standard deviation describes variation among these folds; it is not a confidence interval.

Explain false positives (ham flagged as spam) and false negatives (spam missed). Keep the distinction clear between out-of-fold performance and the final demo model, which is refit on all unique messages. Do not claim that cross-validation on this historical dataset establishes performance on newer messages, other languages, or scam detection.

## Reporting rule

The report may include only results produced by the recorded protocol. Any change to the data, duplicate handling, fold setup, features, rules, or parameters must be documented. No metric is described as a measured result unless it came from an actual run.
