"""Run the preregistered held-out comparison and save model/results artifacts."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from importlib.metadata import version
import platform
from pathlib import Path

import joblib
from sklearn.model_selection import train_test_split

from src.pipeline import LABELS, load_messages, make_models, rule_baseline_predict, score_predictions


ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
RESULTS_DIR = ROOT / "reports" / "generated"


def main() -> None:
    data, data_counts = load_messages()
    train, test = train_test_split(
        data,
        test_size=0.20,
        random_state=42,
        stratify=data["label"],
    )

    results: dict[str, object] = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "dataset": data_counts,
        "split": {
            "method": "stratified train_test_split",
            "test_size_fraction": 0.20,
            "random_state": 42,
            "train_rows": len(train),
            "test_rows": len(test),
            "train_label_counts": {
                label: int(count)
                for label, count in train["label"].value_counts().reindex(LABELS, fill_value=0).items()
            },
            "test_label_counts": {
                label: int(count)
                for label, count in test["label"].value_counts().reindex(LABELS, fill_value=0).items()
            },
        },
        "positive_class": "spam",
        "confusion_matrix_axis_order": ["ham", "spam"],
        "software_versions": {
            "python": platform.python_version(),
            "pandas": version("pandas"),
            "scikit_learn": version("scikit-learn"),
            "joblib": version("joblib"),
        },
        "models": {},
    }

    baseline_predictions = rule_baseline_predict(test["text"])
    results["models"]["Rule baseline"] = score_predictions(test["label"], baseline_predictions)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    for name, model in make_models().items():
        model.fit(train["text"], train["label"])
        predictions = model.predict(test["text"])
        results["models"][name] = score_predictions(test["label"], predictions)
        if name == "Logistic Regression":
            joblib.dump(model, MODEL_DIR / "logistic_regression.joblib")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RESULTS_DIR / "experiment_results.json"
    output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    report_dir = ROOT / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_lines = [
        "# SMS Spam Classification: Experimental Results",
        "",
        "> Results below were produced by `python -m src.train` using the protocol in `docs/EXPERIMENT.md`.",
        "> They summarize one held-out split of the historical English SMS Spam Collection and do not establish performance on current SMS or scam detection generally.",
        "",
        "## Data and split",
        "",
        f"- Raw rows: {data_counts['raw_rows']:,}",
        f"- Duplicate exact-text rows removed before splitting: {data_counts['duplicate_rows_removed']:,}",
        f"- Unique messages used: {data_counts['unique_rows']:,} ({data_counts['ham']:,} ham, {data_counts['spam']:,} spam)",
        f"- Training/test messages: {len(train):,}/{len(test):,}",
        "- Split: stratified 80/20, random state 42; positive class: spam.",
        f"- Software: Python {results['software_versions']['python']}, pandas {results['software_versions']['pandas']}, scikit-learn {results['software_versions']['scikit_learn']}, joblib {results['software_versions']['joblib']}.",
        "",
        "## Methods",
        "",
        "All learned models use TF-IDF word unigrams and bigrams, lowercasing, and Unicode accent stripping. Multinomial Naive Bayes uses alpha=1.0. Logistic Regression uses C=1.0, lbfgs, max_iter=1000, random_state=42. No hyperparameter tuning was performed. The fixed keyword/URL rule baseline is specified in `docs/EXPERIMENT.md`.",
        "",
        "## Held-out metrics",
        "",
        "| Method | Precision (spam) | Recall (spam) | F1 (spam) | Accuracy |",
        "|---|---:|---:|---:|---:|",
    ]
    for method, scores in results["models"].items():
        report_lines.append(
            f"| {method} | {scores['precision_spam']:.3f} | {scores['recall_spam']:.3f} "
            f"| {scores['f1_spam']:.3f} | {scores['accuracy']:.3f} |"
        )
    report_lines.extend(
        ["", "## Confusion matrices", "", "Rows are true labels and columns are predicted labels; order is ham, spam.", ""]
    )
    for method, scores in results["models"].items():
        matrix = scores["confusion_matrix_labels_ham_spam"]
        report_lines.extend(
            [
                f"### {method}",
                "",
                "| True \\ Predicted | ham | spam |",
                "|---|---:|---:|",
                f"| ham | {matrix[0][0]} | {matrix[0][1]} |",
                f"| spam | {matrix[1][0]} | {matrix[1][1]} |",
                "",
            ]
        )
    report_lines.extend(
        [
            "## Interpretation and limits",
            "",
            "A ham message predicted as spam is a false positive; a spam message predicted as ham is a false negative. These metrics estimate performance only on this fixed test split. The data is historical, English-only, and labeled spam/ham rather than verified scam/fraud. A single split does not establish performance on newer messages, other languages, or real-world deployments.",
            "",
            "## References",
            "",
            "Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5CC84>.",
            "",
            "Almeida, T. A., Gómez Hidalgo, J. M., & Yamakami, A. (2011). Contributions to the Study of SMS Spam Filtering: New Collection and Results. Proceedings of the 2011 ACM Symposium on Document Engineering. <https://doi.org/10.1145/2034691.2034742>.",
            "",
            f"Experiment run (UTC): {results['created_utc']}",
            "",
        ]
    )
    (report_dir / "RESULTS.md").write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Saved measured results to {output_path.relative_to(ROOT)} and reports/RESULTS.md")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
