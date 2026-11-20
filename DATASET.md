# Dataset record

## Source and citation

- Dataset: SMS Spam Collection
- Maintainer/source: UCI Machine Learning Repository, dataset 228
- Official page: <https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection>
- Official download archive: <https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip>
- DOI: <https://doi.org/10.24432/C5CC84>
- Dataset citation listed by UCI: Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection* [Dataset]. UCI Machine Learning Repository.
- Introductory research paper: Almeida, T. A., Gómez Hidalgo, J. M., & Yamakami, A. (2011). “Contributions to the Study of SMS Spam Filtering: New Collection and Results.” Proceedings of the 2011 ACM Symposium on Document Engineering. DOI: <https://doi.org/10.1145/2034691.2034742>.

## License and attribution

The current UCI dataset page identifies the dataset license as **Creative Commons Attribution 4.0 International (CC BY 4.0)**. The license permits sharing and adaptation, including commercial use, provided appropriate credit is given and changes are indicated. See the [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode) and [human-readable summary](https://creativecommons.org/licenses/by/4.0/).

The archive's included README also asks users to cite the authors' paper and collection page, and asks users to notify the authors when using the corpus. We retain that request here; no message has been sent. The README says the corpus is supplied free with no limitations except its copyright and warranty disclaimer. We rely on UCI's current CC BY 4.0 metadata for the dataset license and include appropriate attribution. The raw corpus will remain outside version control; the repository includes a retrieval script and this source record.

## Contents and provenance

UCI describes 5,574 labeled SMS messages in one text file, with the class (`ham` or `spam`) followed by the raw message. The collection combines several sources, including spam messages manually extracted from the Grumbletext website, legitimate messages from the NUS SMS Corpus and Caroline Tagg's thesis, and messages from an earlier SMS spam corpus. It is a historical, English-language corpus assembled for SMS spam research.

## Inspection record

The official archive was downloaded on 2026-11-20 from the UCI archive URL above. The downloaded message file has SHA-256 `7d039a24a6083ed9ef0f806ebad56bbb976e3aeb8de05669173bfdc4996c239d`. Inspection found 5,574 rows: 4,827 `ham`, 747 `spam`, zero malformed rows, 281 message texts appearing more than once (403 extra duplicate rows), and zero repeated texts with conflicting labels. The file decoded as UTF-8 without replacement characters.

The experiment removes exact duplicate message texts before cross-validation, keeping the first occurrence. This prevents an identical message from appearing in multiple folds. The source file remains unchanged locally and is excluded from version control.

## Limitations and handling

- The labels are `spam` and `ham`; the corpus does not provide a separate, verified scam/fraud label.
- The corpus is old and drawn from specific sources. Its language, campaigns, and class distribution may not represent current SMS traffic.
- It does not provide all context a deployed filter might use, such as sender reputation or delivery metadata.
- Message text can contain personal or identifying information. Do not expose example messages unnecessarily in reports or logs.
- The project preserves the downloaded source file unchanged and keeps generated fold assignments/results separate. Any transformations are documented.

## Project data status

The source file has been downloaded and inspected locally. It is excluded from Git. See [data/README.md](data/README.md) for retrieval instructions.
