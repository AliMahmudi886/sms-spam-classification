# Topic Screening Protocol

**Status:** Preliminary scoping review in progress  
**Protocol date:** 2026-11-21  
**Purpose:** Identify a feasible computer-science research question with a plausible, evidence-based contribution and verifiable data access for a bachelor's-level project.

## Scope

The screen is limited to applied computer science topics that can be implemented and evaluated by one undergraduate researcher with ordinary computing resources. Initial areas are SMS spam/smishing, Persian/RTL interfaces and accessibility, software defect prediction, phishing URL detection, and vulnerability/software-supply-chain analysis. These are candidate areas, not preselected topics.

## Questions for each candidate

1. What is the narrow, testable research question and what result would answer it?
2. What are the closest primary studies, especially from 2024–2026, and how does the proposed question differ?
3. Can the data or test corpus be obtained from its official source, and are reuse and redistribution terms explicit?
4. Can the protocol be run with the available time, compute, and skills?
5. Are the outcome measures appropriate, and can the findings be stated without generalizing beyond the sample?

## Search plan

- **Search date:** 2026-11-21 (initial targeted search; update before any final topic selection).
- **Sources:** Crossref/DOI records, publisher or conference proceedings, arXiv for preprints clearly marked as such, official dataset repositories, standards bodies, and project repositories for license/provenance checks.
- **Date emphasis:** 2024–2026 for current overlap; older primary sources are retained when they define a benchmark, standard, or method.
- **Search method:** Search combinations of topic terms, task terms, data/validation terms, and evaluation terms. Follow references from directly relevant primary papers and search for close replications or competing datasets.
- **Record:** query, date, source, title, year, publication status, study/data relevance, license evidence, and reason for inclusion or exclusion.

## Eligibility rules

### Include

- Primary empirical studies, dataset papers, standards, and official repository documentation directly related to the candidate question.
- Studies with enough method detail to identify the data, task, and evaluation design.
- Sources that clarify dataset origin, labeling, license, access, or redistribution constraints.

### Exclude from novelty evidence

- Marketing pages, unsourced summaries, and non-primary commentary.
- Work that shares only broad keywords but studies a materially different task (retain as context where useful).
- Preprints represented as peer-reviewed publications; preprints may inform the scan but must be labeled.
- Dataset landing pages as proof of research quality; data source/license and study results are assessed separately.

## Candidate decision rubric

Score each item 0–2: **0** unresolved/weak; **1** plausible but needs verification; **2** supported by current evidence.

| Dimension | What a score of 2 requires |
|---|---|
| Research gap | Specific distinction from the closest recent primary studies; no broad novelty claim. |
| Data rights and access | Official source is reachable and reuse terms for the actual data are clear. |
| Feasibility | One student can complete collection/preparation, analysis, and reporting with available resources. |
| Evaluation validity | Protocol, baselines, metrics, and uncertainty/error analysis suit the question. |
| Reproducibility | Inputs, transformations, split rules, software versions, and outputs can be documented. |

A candidate is **not selected** if data rights/access score 0, or if research gap scores 0. Total scores are prioritization aids, not evidence of novelty or publication likelihood.

## Initial search log

This log summarizes targeted searches already performed in this project session. It is not an exhaustive database search and does not count as a completed systematic or scoping review.

### Query families and search evidence

Searches used general web search with exact topic/task combinations and follow-up searches on named papers and official standards/data sources. They were not run through authenticated Scopus, Web of Science, IEEE Xplore, or ACM Digital Library interfaces. Search results did not provide a stable, exportable result count, so no hit totals are reported.

| Query family (representative wording) | Sources retrieved/checked | Search and appraisal limitation |
|---|---|---|
| `SMS spam detection cross dataset UCI Mendeley 2026 paper`; `SMS spam detection duplicate leakage benchmark datasets`; `SMS smishing dataset label methodology` | UCI/Mendeley official records; recent IEEE, SAGE, Scientific Reports and conference records documented in [JOURNAL_READINESS.md](JOURNAL_READINESS.md). | Some full texts were inaccessible; the Mendeley landing record was accessible but its official archive was not retrieved, and no independent-corpus experiment was run. |
| `Persian RTL mixed direction interface layout browser study`; `Persian web accessibility screen reader RTL WCAG study`; `bidirectional interface directionality empirical study Persian RTL` | W3C HTML bidi requirements and test reports; Unicode UAX #9; WebAIM 2025; CHI 2025; IJHCS 2025; OUIID 2026. | Search identifies close prior work, including tests and user studies. It does not establish Persian-specific gap absence; publisher full texts were not all accessible. |
| `software defect prediction temporal leakage random split 2026`; `2025 software defect prediction time-aware evaluation data leakage` | Information and Software Technology 2026; 2026 audit preprint; empirical study of SZZ/data collection. | Broad temporal-leakage question is directly occupied; PROMISE/NASA data provenance and terms need source-by-source verification for any proposed reuse. |
| `phishing URL dataset temporal cross dataset evaluation benchmark 2025 2026`; `malicious URL benchmark dataset 2026` | LegitPhish Data in Brief record; EntroURL-Bench conference record; PhreshPhish preprint. | Dataset availability is not the same as permission to redistribute underlying URLs or full records; source terms and collection methodology must be checked before use. |
| `public vulnerability dataset license OSV NVD vulnerability intelligence dataset`; `software vulnerability prediction point-in-time benchmark 2026` | Official OSV data-source/license documentation; NIST data feeds and reuse guidance; VulZoo ASE 2024 dataset paper; recent vulnerability timing and package/security studies. | OSV is an aggregation with source-specific terms, including some non-commercial/no-derivatives terms. NVD/NIST attribution and reuse conditions must be followed; no data downloaded or analyzed. |

The query wording above is a concise reconstruction of query families used during the live screening, not a timestamped export from a scholarly database. Because the search backend returned HTTP 404 on the attempted follow-up in this step, this update adds no new hits or result counts.

| Area | Search focus and representative sources | Preliminary decision |
|---|---|---|
| SMS spam/smishing | Cross-corpus evaluation, dataset quality, duplicates/provenance, and lightweight models. Recent directly relevant works are summarized in [JOURNAL_READINESS.md](JOURNAL_READINESS.md), including 2025–2026 studies on multi-dataset evaluation and UCI/Mendeley transfer. | Keep as a portfolio project. No distinct journal question with verified independent data has cleared the initial screen. |
| Persian RTL and BiDi interfaces | Persian accessibility and typography; HTML bidi input/rendering requirements; W3C browser tests; 2025/2026 empirical directionality studies. Sources: [W3C HTML bidi](https://www.w3.org/TR/html-bidi/), [W3C bidi tests](https://www.w3.org/International/i18n-tests/results/bidi-text-rendering), [IJHCS 2025](https://doi.org/10.1016/j.ijhcs.2024.103383), [OUIID 2026](https://doi.org/10.1080/10447318.2026.2663079), [WebAIM 2025](https://webaim.org/projects/million/2025). | A useful engineering project remains possible, but broad audit/test/direction questions overlap with existing work. A distinct Persian empirical question and participant/data protocol are not established. |
| Software defect prediction | Random versus chronological split, leakage, quality issues, and public PROMISE/NASA-style datasets. Sources: [temporal evaluation study (2026)](https://doi.org/10.1016/j.infsof.2026.108278), [experiment audit preprint (2026)](https://arxiv.org/abs/2601.18477), [SZZ/data collection study](https://doi.org/10.1007/s10664-021-10092-4). | Broad temporal-leakage question is already directly studied; dataset quality and provenance require careful treatment. No narrower gap selected. |
| Phishing URL detection | Public data and benchmark papers, temporal/cross-dataset evaluation, dataset source and label questions. Sources: [LegitPhish (2025)](https://doi.org/10.1016/j.dib.2025.111972), [EntroURL-Bench (2026)](https://doi.org/10.1145/3796563.3796574), [PhreshPhish (2025 preprint)](https://arxiv.org/abs/2507.10854). | Active and crowded. Any candidate requires source-specific license review; no question selected. |
| Vulnerability and software supply-chain security | CVE timing, package risk, cross-source metadata, and recent curated benchmarks. See [OSV data source terms](https://google.github.io/osv.dev/data/), [NVD data feeds](https://nvd.nist.gov/vuln/data-feeds), and [VulZoo dataset paper](https://doi.org/10.1145/3691620.3695345). OSV explicitly documents source-specific terms, including CC-BY-NC-ND 4.0 for Chainguard/Wolfi and mixed licenses across the aggregation. NIST provides data reuse conditions and citation guidance. [OSV sources](https://google.github.io/osv.dev/data/) · [NIST terms](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications) | Timely but complex and actively studied. Aggregated data can have mixed source licenses; no question selected pending source-level rights and narrower gap. |

## Current conclusion and next action

No candidate has yet passed both the research-gap and data-rights/access gates. The SMS project is complete enough to present as an undergraduate portfolio/reproducibility artifact, but its manuscript is not journal-ready. Do not start new model experiments, collect personal data, or claim journal novelty based on this screen.

The next research step is to complete the search log with database-specific queries and screening counts, retrieve/read the closest papers in full, and check each candidate dataset's official terms. A supervisor should review the shortlisted gap before a new study protocol or participant recruitment begins. If no candidate passes the gates, keep the resume project and postpone the journal article until a viable question is identified.

## Limitations of this screen

- The search has been targeted and iterative, not executed across a predefined set of scholarly databases with recorded result counts.
- Some publisher full texts were inaccessible during the initial screen; abstracts and official standards/repository records were used where available and must not be treated as full-text appraisal.
- No double screening, preregistration, or formal risk-of-bias assessment has been conducted.
- The 2026 sources are time-sensitive and should be rechecked at topic selection and submission.
