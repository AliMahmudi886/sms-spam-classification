"""Summarize UCI message encoding and SMS-length feasibility without training."""

from __future__ import annotations

import argparse
import hashlib
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DATA_SHA256 = "7d039a24a6083ed9ef0f806ebad56bbb976e3aeb8de05669173bfdc4996c239d"
LABELS = ("ham", "spam")

sys.path.insert(0, str(ROOT))
from src.sms_encoding import estimate_sms_length  # noqa: E402


def summarize(path: Path) -> list[str]:
    """Validate the documented corpus and return a deterministic summary."""
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")

    checksum = hashlib.sha256(path.read_bytes()).hexdigest()
    if checksum != EXPECTED_DATA_SHA256:
        raise ValueError(
            "Dataset SHA-256 differs from the documented UCI corpus. "
            "Review DATASET.md before interpreting this audit."
        )

    rows: list[tuple[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as source:
        for line_number, raw_line in enumerate(source, start=1):
            line = raw_line.rstrip("\r\n")
            label, separator, text = line.partition("\t")
            if not separator or label not in LABELS:
                raise ValueError(f"Malformed dataset row at line {line_number}.")
            rows.append((label, text))

    labels_by_text: dict[str, str] = {}
    for label, text in rows:
        previous = labels_by_text.setdefault(text, label)
        if previous != label:
            raise ValueError("Identical message text has conflicting labels.")

    unique_rows = list(labels_by_text.items())
    encodings: Counter[tuple[str, str]] = Counter()
    single_part: Counter[tuple[str, str]] = Counter()
    gsm7_spare: Counter[tuple[str, int]] = Counter()

    for text, label in unique_rows:
        estimate = estimate_sms_length(text)
        encodings[(estimate.encoding, label)] += 1
        if estimate.segments == 1:
            single_part[(estimate.encoding, label)] += 1
        if estimate.encoding == "GSM-7":
            spare = estimate.single_segment_capacity - estimate.units
            for threshold in (30, 60):
                if spare >= threshold:
                    gsm7_spare[(label, threshold)] += 1

    output = [
        f"Dataset: {path}",
        f"SHA-256: {checksum}",
        f"Raw rows: {len(rows)}",
        f"Exact-text duplicates removed: {len(rows) - len(unique_rows)}",
        f"Unique messages: {len(unique_rows)}",
        "Unique messages by encoding and label:",
    ]
    for encoding in ("GSM-7", "UCS-2"):
        output.append(
            f"  {encoding}: ham={encodings[(encoding, 'ham')]}, "
            f"spam={encodings[(encoding, 'spam')]}, "
            f"total={encodings[(encoding, 'ham')] + encodings[(encoding, 'spam')]}"
        )
    output.append("Original single-part messages by encoding and label:")
    for encoding in ("GSM-7", "UCS-2"):
        output.append(
            f"  {encoding}: ham={single_part[(encoding, 'ham')]}, "
            f"spam={single_part[(encoding, 'spam')]}"
        )
    output.append("GSM-7 messages with at least this much one-part capacity left:")
    for threshold in (30, 60):
        output.append(
            f"  {threshold} septets: ham={gsm7_spare[('ham', threshold)]}, "
            f"spam={gsm7_spare[('spam', threshold)]}"
        )
    output.append(
        "Note: capacity counts do not account for separators or validate any added text."
    )
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=ROOT / "data" / "raw" / "SMSSpamCollection",
        help="path to the checksum-verified UCI SMSSpamCollection file",
    )
    args = parser.parse_args()
    for line in summarize(args.data):
        print(line)


if __name__ == "__main__":
    main()
