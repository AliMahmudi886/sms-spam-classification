# Dependency Security Review

**Review date:** 2026-11-22  
**Repository revision reviewed:** `c45093f34bcbcd497a775ddc98e1bc364d86f6c9`  
**Scope:** Exact packages and versions listed in `requirements.lock` (39 PyPI packages, including transitive dependencies).

## Method

Each locked package name and version was submitted to the public OSV batch query API as a PyPI package/version query. OSV documents that this endpoint accepts multiple package/version queries and returns matching vulnerability identifiers in input order: [OSV `POST /v1/querybatch` documentation](https://google.github.io/osv.dev/post-v1-querybatch/).

## Result

The API returned **zero vulnerability records for the 39 queried package/version pairs** on the review date. This is a point-in-time database lookup, not a guarantee that the dependencies or application are free of security issues.

## Limitations and maintenance

- This review covers the locked Python package versions only. It does not assess application logic, the base Docker image, GitHub Actions, the operating system, or vulnerabilities not represented in OSV.
- A clean lookup does not replace ongoing dependency updates, code review, or a security assessment before deployment.
- Re-run the query after changing `requirements.lock` and periodically if this snapshot is used as a maintenance reference.
- No local test suite or application runtime was executed as part of this review.
