"""Report out-of-fold Logistic Regression errors by natural SMS text length."""

from sklearn.base import clone
from sklearn.model_selection import StratifiedKFold

from src.pipeline import load_messages, make_models
from src.train import N_SPLITS, RANDOM_STATE


BANDS = (("Short (0–80)", 0, 80), ("Medium (81–160)", 81, 160), ("Long (161+)", 161, None))


def counts(rows):
    return tuple(
        int(((rows.label == actual) & (rows.prediction == predicted)).sum())
        for actual, predicted in (("ham", "ham"), ("ham", "spam"), ("spam", "ham"), ("spam", "spam"))
    )


def main():
    data, _ = load_messages()
    data["length"] = data.text.str.len()
    data["prediction"] = ""
    data["fold"] = 0
    model = make_models()["Logistic Regression"]
    splitter = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=RANDOM_STATE)
    for fold, (train_idx, valid_idx) in enumerate(splitter.split(data.text, data.label), 1):
        train, valid = data.iloc[train_idx], data.iloc[valid_idx]
        fitted = clone(model).fit(train.text, train.label)
        data.loc[valid.index, "prediction"] = fitted.predict(valid.text)
        data.loc[valid.index, "fold"] = fold

    print("Overall (TN, FP, FN, TP):", counts(data))
    print("| Length | Ham | Spam | FP | FN | Spam recall | Recall range across folds |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for label, lower, upper in BANDS:
        subset = data[data.length.ge(lower)]
        if upper is not None:
            subset = subset[subset.length.le(upper)]
        tn, fp, fn, tp = counts(subset)
        fold_recall = []
        for _, rows in subset.groupby("fold"):
            _, _, fold_fn, fold_tp = counts(rows)
            if fold_fn + fold_tp:
                fold_recall.append(fold_tp / (fold_fn + fold_tp))
        spread = f"{min(fold_recall):.1%}–{max(fold_recall):.1%}" if fold_recall else "N/A"
        recall = f"{tp / (tp + fn):.1%}" if tp + fn else "N/A"
        print(f"| {label} | {tn + fp} | {tp + fn} | {fp} | {fn} | {recall} | {spread} |")


if __name__ == "__main__":
    main()
