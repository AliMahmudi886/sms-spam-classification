# Resume and interview wording

## Resume bullet

Built a reproducible English SMS spam classification study and Streamlit demo using the UCI SMS Spam Collection; compared a transparent rule baseline with Multinomial Naive Bayes and Logistic Regression using stratified five-fold cross-validation, out-of-fold precision/recall/F1, fold-level variation, and confusion matrices. Logistic Regression reached pooled out-of-fold spam precision 0.998, recall 0.677, and F1 0.807; mean fold F1 was 0.806 ± 0.020. See [reports/RESULTS.md](../reports/RESULTS.md) for the full method and limits.

## Short interview explanation

“I built an end-to-end SMS spam classification project, from dataset provenance and license documentation through evaluation and a small Streamlit demo. I removed exact duplicate messages before stratified five-fold cross-validation, used pipelines so TF-IDF vocabulary was fit only within each training fold, and compared a transparent rule baseline with Naive Bayes and Logistic Regression. Logistic Regression reached a pooled out-of-fold F1 of 0.807 for spam, with fold mean F1 0.806 and sample standard deviation 0.020. The demo is described as English spam/ham classification: this historical dataset does not establish scam detection or performance on current messages.”

Use these statements only alongside the committed experiment report. Do not describe the work as a publication, a production deployment, or a general fraud-detection capability.
