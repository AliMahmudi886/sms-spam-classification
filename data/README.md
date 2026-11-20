# Data directory

The raw SMS Spam Collection is excluded from version control. Run `python scripts/download_data.py` from the repository root to download the official [UCI archive](https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip) and extract `SMSSpamCollection` under `data/raw/`.

The script retains the archive's accompanying readme and verifies the message file against the SHA-256 recorded in [../DATASET.md](../DATASET.md). If the upstream file changes, review the source and update the experiment record before training. Do not edit the raw file in place.
