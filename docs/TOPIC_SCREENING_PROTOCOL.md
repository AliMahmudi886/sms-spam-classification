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

### Closest-source appraisal (current evidence level)

| Source | Type/status | What it studies (based on accessible record/text) | Relevance and boundary |
|---|---|---|---|
| Destefanis et al., *An Audit of Machine Learning Experiments on Software Defect Prediction* (2026) | arXiv preprint; full text accessible, not treated as peer-reviewed publication here. It reports auditing a random sample of 101 papers from 2019–2023. | Audits experimental design, analysis, reporting, and reproducibility; reports 427 issues across 101 papers, median four issues per paper. | A broad “audit defect-prediction experiment quality” question would overlap. Its reported search of ~1,585 studies is the paper's own method, not this project's search count. [Preprint](https://arxiv.org/abs/2601.18477) |
| Borowsky et al., *From “Right or Left” to “Optimal”* (2026) | Publisher abstract/search record; full text could not be retrieved in this review. | Reports an eye-tracking evaluation of 30 UI items with 42 BiDi users and argues that preferred direction depends on task/context and measures. | Broad direction-choice studies are already active; no claim is made here about its full methods, participant composition, or Persian-specific results. [DOI](https://doi.org/10.1080/10447318.2026.2663079) |
| Goldenberg & Tractinsky, *Exploring amBiDiguity* (2025) | Publisher abstract/search record; full text could not be retrieved in this review. | Reports an empirical study of 1,705 Arabic and Hebrew users on interpretation of ambiguous UI direction. | Strong adjacent prior work, but Arabic/Hebrew results cannot automatically be generalized to Persian. [DOI](https://doi.org/10.1016/j.ijhcs.2024.103383) |
| *When random splits lie* (search result indexed as 2026) | Search result only; publisher full text was inaccessible. The result lists a December 2026 volume, later than this review date. | Search snippet describes random, temporal, and walk-forward evaluation for temporal leakage. | Do not cite it as an already-published article until its online publication date/status is verified. The broader defect-prediction gap conclusion does not depend on this one record. [DOI](https://doi.org/10.1016/j.infsof.2026.108278) |
| VulZoo (Ruan et al., ASE 2024) | Official project repository and paper citation inspected; repository contains raw and processed material from many sources. | Provides an integrated vulnerability-intelligence dataset and utilities, combining 17 sources according to the paper/repository description. | Useful evidence that multi-source vulnerability datasets exist, not proof of uniform reuse rights. The data-source terms must be reviewed individually. [Project](https://github.com/NUS-Curiosity/VulZoo) · [Paper](https://doi.org/10.1145/3691620.3695345) |
| OSV official source list | Official documentation; directly inspected. | Lists source ecosystems and their different licenses; identifies some converted data and aggregate downloads. | Confirms that the aggregate must not be assumed to have one license. A study would need to filter to sources with compatible explicit terms and retain provenance. [OSV data](https://google.github.io/osv.dev/data/) |

The records for LegitPhish, EntroURL-Bench, CHI 2025, the 2025/2026 SMS works, and the W3C/WCAG material were found via publisher, standards, or official project pages/search excerpts, but were not all appraised from full text in this step. They are leads and proximity evidence, not a systematic inclusion set. The public project should preserve that distinction.

### Gap matrix and next research decision

| Candidate question | Closest evidence | Data/access | Feasibility | Novelty assessment | Decision |
|---|---|---|---|---|---|
| Repeat the UCI spam-vs-ham comparison with another model | Existing experiment plus extensive later SMS benchmark work, including current UCI/Mendeley comparison and feature/model studies already listed in [JOURNAL_READINESS.md](JOURNAL_READINESS.md). | UCI CC BY 4.0 and already documented. | High. | Low; an additional algorithm on the same known corpus is not a distinct contribution. | Do not extend for journal novelty. Keep as portfolio baseline. |
| Compare UCI internal CV against a modern external SMS corpus | Recent 2026 SMS papers already report multi-dataset and UCI/Mendeley evaluation. External-corpus overlap/labels/provenance remain questionable for Mendeley, while other candidate corpora have rights/privacy concerns. | Not cleared; no external corpus is approved for this project. | Medium to high, depending on data access. | Low without a clearly independent dataset and a narrower question. | Do not start until independent data and source-specific reuse terms are verified. |
| Test operating thresholds under class-prevalence or false-positive-cost changes | Recent work addresses robustness, evolving SMS spam, and operating points; e.g. [Johnny Still Receives Spam SMS (2026 preprint)](https://arxiv.org/abs/2609.01171) studies robustness and precision–recall operating points. | Could be explored with the existing out-of-fold scores, but simulated prevalence/costs are assumptions, not observed deployment data. | High for a sensitivity analysis. | Low as a standalone contribution; easy to overstate synthetic prevalence scenarios as real-world evidence. | Possible teaching/reproducibility add-on only; not selected as a journal contribution. |
| Study modern, source-authenticated smishing with new human/labeled data | Existing current SMS work and large datasets show the topic is active; a defensible study would require independent verified smishing labels, lawful collection, careful privacy design, and likely external domain expertise. | No approved source or collection/ethics plan currently exists. | Low for a solo bachelor's project. | Potentially differentiable only after a distinct threat/label/source question is demonstrated. | Do not collect or process personal messages; seek supervisor/industry collaboration before pursuing. |

**Decision:** The existing SMS study remains the strongest finished artifact, but no journal extension has cleared both novelty and data gates. Do not run more classifier experiments merely to increase the number of tables. The next legitimate research milestone is an independent, supervisor-reviewed gap search and source-level data-access decision. If the user wants immediate technical work without that research dependency, a clearly labeled threshold-sensitivity appendix can be added to the portfolio later, but it must not be called novel or external validation.

## Project completion estimate (2026-11-22)

These are milestone estimates, not scientific measures. The criteria are documented here so the percentage does not imply paper quality or publication likelihood.

| Track | Estimate | Completed evidence | Remaining milestones |
|---|---:|---|---|
| Resume/portfolio repository | **95%** | Public repository; app and model-training flow; documented UCI source; reproducibility instructions; actual baseline experiment, results, model card, and paper draft; recent research-direction records. CI run #15 for commit `3b8b3d4` completed successfully on Nov 21, 2026. On Nov 22, 2026, manually launched the app with the existing local environment and model, entered a synthetic sample message, observed a SPAM prediction, model scores, and limitation text, then stopped the local server. | Optional final README pass. Manual UI verification is limited to one synthetic input on this local environment; no local software test suite was run. |
| Academic manuscript as a complete draft | **55%** | English draft contains abstract, introduction, methods, actual results, discussion, limitations, declarations checklist, and references. | Complete a reproducible literature search, settle a defensible research question/contribution, fully appraise closest sources, and update the manuscript accordingly. |
| Journal submission readiness | **20%** | Honest baseline manuscript and published, reproducible code/results exist; data source for the baseline is documented. | No defensible journal contribution selected; no complete literature review; no target journal; no independent/approved data plan for an extension; author declarations and journal formatting remain incomplete. This is not a prediction of acceptance. |

The percentages use different denominators. Portfolio completion is about a public educational project; manuscript completion is about having a full draft; journal readiness requires a defensible contribution and complete research/submission checks. They should not be added or averaged. The GitHub Actions workflow reproduces the research experiment; its success is reported as CI evidence, not as a local software test run.

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
