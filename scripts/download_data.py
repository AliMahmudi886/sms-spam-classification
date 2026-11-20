"""Download and extract the official UCI SMS Spam Collection archive."""

from __future__ import annotations

import hashlib
import io
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(URL, headers={"User-Agent": "sms-spam-classifier/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        archive_bytes = response.read()

    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        for member in ("SMSSpamCollection", "readme"):
            matches = [name for name in archive.namelist() if name.rsplit("/", 1)[-1] == member]
            if not matches:
                raise RuntimeError(f"Expected {member!r} in the UCI archive, found none.")
            destination = RAW_DIR / member
            destination.write_bytes(archive.read(matches[0]))

    checksum = hashlib.sha256((RAW_DIR / "SMSSpamCollection").read_bytes()).hexdigest()
    print(f"Saved raw data and readme under {RAW_DIR}")
    print(f"SMSSpamCollection SHA-256: {checksum}")


if __name__ == "__main__":
    main()
