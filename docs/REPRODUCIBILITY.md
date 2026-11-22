# Reproducing the experiment

This guide describes how to retrieve the documented public corpus, recreate the evaluation, and inspect the outputs. It complements the detailed [experiment protocol](EXPERIMENT.md), [dataset record](../DATASET.md), and [measured report](../reports/RESULTS.md).

## Requirements

- Python 3.12 for the exact pinned environment used in the reported experiment.
- Network access to install packages and retrieve the UCI archive.
- GitHub Actions is configured to run the same workflow on Ubuntu and Windows.

`requirements.txt` allows compatible package ranges for a general local setup. Use `requirements.lock` with Python 3.12 to recreate the recorded software environment.

## Run locally

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.lock
python scripts/download_data.py
python -m src.train
```

### macOS or Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python scripts/download_data.py
python -m src.train
```

The downloader retrieves the official UCI archive and verifies the raw message file's SHA-256 against the value recorded in [DATASET.md](../DATASET.md). The training command removes exact duplicate texts, evaluates the rule baseline and two TF-IDF classifiers with stratified five-fold cross-validation (`shuffle=True`, `random_state=42`), then fits the preselected Logistic Regression pipeline on all unique messages for the local demo.

## SMS encoding feasibility audit

After retrieving the dataset, reproduce the count-only encoding and spare-capacity summary with:

```bash
python scripts/audit_sms_encoding_feasibility.py
```

The audit checks the dataset SHA-256, removes exact duplicate texts for counting, and calls the same GSM-7/UCS-2 estimator used by the app. It performs no model training or inference and writes no output files. Pass `--data PATH` to inspect a copy stored elsewhere. The reported GSM-7 spare-capacity figures are based on one-part capacity before separators or added text are considered; they are feasibility counts, not attack results.

## Generated outputs

The training command creates local files that are excluded from Git:

- `reports/generated/experiment_results.json`: machine-readable fold and pooled out-of-fold results.
- `reports/RESULTS.md`: human-readable report generated from that JSON.
- `models/logistic_regression.joblib`: final demo model fitted on all unique messages.

The checked-in [`reports/RESULTS.md`](../reports/RESULTS.md) contains the recorded experiment summary. Each successful CI job also uploads its generated report and JSON metrics as a downloadable artifact retained by GitHub Actions for 30 days. The model file is not uploaded by CI.

## Interpreting the evaluation

Every unique message in this dataset was part of one validation fold in the reported five-fold cross-validation. There is no independent holdout set, and this experiment does not estimate performance on a newer or external dataset. The fold-level standard deviation describes variation among these five folds; it is not a confidence interval. Do not present these corpus-level results as proof of scam detection, current-threat performance, or deployment readiness.

## References

- Almeida, T. & Hidalgo, J. (2011). [SMS Spam Collection](https://doi.org/10.24432/C5CC84) [Dataset]. UCI Machine Learning Repository. UCI lists the dataset as CC BY 4.0; attribution and the source archive checksum are documented in [DATASET.md](../DATASET.md).
- Almeida, T. A., Gómez Hidalgo, J. M., & Yamakami, A. (2011). [Contributions to the Study of SMS Spam Filtering: New Collection and Results](https://doi.org/10.1145/2034691.2034742). Proceedings of the 2011 ACM Symposium on Document Engineering.
