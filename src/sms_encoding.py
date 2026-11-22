"""Estimate SMS transport encoding and segment count from message text."""

from __future__ import annotations

from dataclasses import dataclass


# 3GPP TS 23.038 default alphabet. Characters in the extension table consume
# an escape septet plus the character septet.
_GSM7_BASIC = frozenset(
    "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?¡"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
)
_GSM7_EXTENSION = frozenset("\f^{}\\[~]|€")


@dataclass(frozen=True)
class SmsLengthEstimate:
    """A standard-based estimate; carrier and client behavior may differ."""

    encoding: str
    units: int
    unit_name: str
    segments: int
    single_segment_capacity: int
    multipart_segment_capacity: int


def estimate_sms_length(text: str) -> SmsLengthEstimate:
    """Estimate GSM-7 or UCS-2 payload units and required SMS segments.

    GSM-7 extension-table characters count as two septets. Any character
    outside the GSM-7 alphabets switches the whole message to UCS-2, whose
    length is counted as UTF-16 code units. Standard single-part capacities
    are 160 septets or 70 UCS-2 units; concatenated parts use 153 or 67 units.
    This is an estimate and does not model every carrier gateway or handset.
    Capacities follow 3GPP TS 23.040; alphabet counts follow TS 23.038.
    """
    if all(character in _GSM7_BASIC or character in _GSM7_EXTENSION for character in text):
        units = sum(2 if character in _GSM7_EXTENSION else 1 for character in text)
        encoding = "GSM-7"
        unit_name = "septets"
        single_capacity = 160
        multipart_capacity = 153
    else:
        units = len(text.encode("utf-16-le", errors="surrogatepass")) // 2
        encoding = "UCS-2"
        unit_name = "code units"
        single_capacity = 70
        multipart_capacity = 67

    if units == 0:
        segments = 0
    elif units <= single_capacity:
        segments = 1
    else:
        segments = (units + multipart_capacity - 1) // multipart_capacity

    return SmsLengthEstimate(
        encoding=encoding,
        units=units,
        unit_name=unit_name,
        segments=segments,
        single_segment_capacity=single_capacity,
        multipart_segment_capacity=multipart_capacity,
    )
