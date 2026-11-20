"""Dataset loading, models, and evaluation helpers for the project."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


LABELS = ["ham", "spam"]
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "SMSSpamCollection"
EXPECTED_DATA_SHA256 = "7d039a24a6083ed9ef0f806ebad56bbb976e3aeb8de05669173bfdc4996c239d"


def load_messages(path: Path = DATA_PATH) -> tuple[pd.DataFrame, dict[str, int]]:
    """Load the tab-separated corpus and remove exact duplicate texts."""
    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Run `python scripts/download_data.py` first."
        )
    checksum = hashlib.sha256(path.read_bytes()).hexdigest()
    if checksum != EXPECTED_DATA_SHA256:
        raise ValueError(
            "Dataset checksum differs from the documented UCI corpus. "
            "Review DATASET.md before training on a changed file."
        )

    records = []
    with path.open("r", encoding="utf-8", newline="") as source:
        for line_number, raw_line in enumerate(source, start=1):
            line = raw_line.rstrip("\r\n")
            label, separator, message = line.partition("\t")
            if not separator or label not in LABELS:
                raise ValueError(f"Malformed dataset row at line {line_number}.")
            records.append((label, message))
    frame = pd.DataFrame.from_records(records, columns=["label", "text"])
    if not set(frame["label"].unique()).issubset(set(LABELS)):
        raise ValueError("Dataset contains labels outside the expected ham/spam classes.")
    conflicting_duplicates = frame.groupby("text")["label"].nunique().gt(1).any()
    if conflicting_duplicates:
        raise ValueError("Identical message text has conflicting labels; review the source before training.")
    duplicate_text_count = int(frame.duplicated(subset="text", keep="first").sum())
    deduplicated = frame.drop_duplicates(subset="text", keep="first").reset_index(drop=True)
    counts = {
        "raw_rows": len(frame),
        "duplicate_rows_removed": duplicate_text_count,
        "unique_rows": len(deduplicated),
        "ham": int((deduplicated["label"] == "ham").sum()),
        "spam": int((deduplicated["label"] == "spam").sum()),
    }
    return deduplicated, counts


def make_models() -> dict[str, Pipeline]:
    """Build fixed TF-IDF pipelines; fit vectorizers only on training data."""
    return {
        "Multinomial Naive Bayes": Pipeline(
            [
                (
                    "tfidf",
                    TfidfVectorizer(ngram_range=(1, 2), lowercase=True, strip_accents="unicode"),
                ),
                ("classifier", MultinomialNB(alpha=1.0)),
            ]
        ),
        "Logistic Regression": Pipeline(
            [
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True, strip_accents="unicode")),
                (
                    "classifier",
                    LogisticRegression(C=1.0, max_iter=1000, solver="lbfgs", random_state=42),
                ),
            ]
        ),
    }


SPAM_TERMS = {
    "claim", "congratulations", "credit", "free", "guaranteed", "offer", "prize",
    "selected", "urgent", "winner", "won", "cash", "loan", "reward",
}
URL_PATTERN = re.compile(r"(?:https?://|www\.)", re.IGNORECASE)


def rule_baseline_predict(messages: list[str] | pd.Series) -> list[str]:
    """Predict spam if a message has a URL or at least one predeclared trigger term."""
    predictions = []
    for message in messages:
        tokens = set(re.findall(r"[a-z]+", str(message).lower()))
        flagged = bool(URL_PATTERN.search(str(message))) or bool(tokens & SPAM_TERMS)
        predictions.append("spam" if flagged else "ham")
    return predictions


def score_predictions(y_true: list[str] | pd.Series, y_pred: list[str]) -> dict[str, object]:
    """Return class-spam metrics and a confusion matrix with stable class order."""
    return {
        "precision_spam": float(precision_score(y_true, y_pred, pos_label="spam", zero_division=0)),
        "recall_spam": float(recall_score(y_true, y_pred, pos_label="spam", zero_division=0)),
        "f1_spam": float(f1_score(y_true, y_pred, pos_label="spam", zero_division=0)),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "confusion_matrix_labels_ham_spam": confusion_matrix(y_true, y_pred, labels=LABELS).tolist(),
    }


def logistic_feature_contributions(
    model: Pipeline, message: str, top_k: int = 5
) -> dict[str, list[dict[str, float | str]]]:
    """Return the largest signed TF-IDF contributions to Logistic Regression's spam logit.

    These values decompose the fitted linear score over observed features. They are
    not causal or semantic explanations of why a message is spam.
    """
    if top_k < 1:
        raise ValueError("top_k must be a positive integer")

    vectorizer = model.named_steps["tfidf"]
    classifier = model.named_steps["classifier"]
    if not hasattr(classifier, "coef_"):
        raise TypeError("Feature contributions are available only for a linear classifier.")

    classes = list(classifier.classes_)
    if "spam" not in classes:
        raise ValueError("The fitted model does not contain the spam class.")
    spam_coefficients = classifier.coef_[0]
    if classes.index("spam") == 0:
        spam_coefficients = -spam_coefficients

    vector = vectorizer.transform([message])
    contributions = vector.multiply(spam_coefficients).tocoo()
    feature_names = vectorizer.get_feature_names_out()
    signed = [
        (str(feature_names[index]), float(value))
        for index, value in zip(contributions.col, contributions.data)
        if value != 0
    ]
    positive = sorted((item for item in signed if item[1] > 0), key=lambda item: item[1], reverse=True)
    negative = sorted((item for item in signed if item[1] < 0), key=lambda item: item[1])

    return {
        "toward_spam": [
            {"feature": feature, "logit_contribution": value}
            for feature, value in positive[:top_k]
        ],
        "toward_ham": [
            {"feature": feature, "logit_contribution": value}
            for feature, value in negative[:top_k]
        ],
    }