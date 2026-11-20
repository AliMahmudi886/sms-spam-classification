"""Streamlit demo for the trained English SMS spam classifier."""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import streamlit as st

from src.pipeline import logistic_feature_contributions


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "logistic_regression.joblib"
RESULTS_PATH = ROOT / "reports" / "generated" / "experiment_results.json"

st.set_page_config(page_title="SMS Spam Classifier", page_icon="📩", layout="centered")

st.title("English SMS Spam Classifier")
st.caption("A small research demo using TF-IDF and Logistic Regression")
st.markdown(
    "Classify an English text message as **spam** or **ham**. The prediction is a model estimate, "
    "not a verdict about whether a message is safe."
)

with st.sidebar:
    st.header("About this project")
    st.markdown(
        "The model was trained on the UCI SMS Spam Collection and evaluated with stratified "
        "five-fold cross-validation. The corpus is historical, English-only, and labeled "
        "`spam`/`ham`; it does not provide a separate scam or fraud label."
    )
    st.markdown("[Dataset, license, and source notes](https://github.com/AliMahmudi886/sms-spam-classification/blob/main/DATASET.md)")
    st.markdown("[Evaluation protocol](https://github.com/AliMahmudi886/sms-spam-classification/blob/main/docs/EXPERIMENT.md)")

if not MODEL_PATH.is_file():
    st.info("The demo model is not available yet. Follow the setup steps in the project README.")
    st.stop()

model = joblib.load(MODEL_PATH)
cv_f1 = None
if RESULTS_PATH.is_file():
    with RESULTS_PATH.open("r", encoding="utf-8") as results_file:
        experiment_results = json.load(results_file)
    cv_f1 = experiment_results["models"]["Logistic Regression"]["f1_spam"]

with st.form("message_classifier"):
    message = st.text_area(
        "Message text",
        height=150,
        placeholder="Paste an English SMS message here…",
        help="The project is designed to run locally. Do not paste private messages into a publicly hosted instance.",
    )
    submitted = st.form_submit_button("Classify message", type="primary")

if submitted and not message.strip():
    st.info("Enter a message before classifying it.")
elif submitted:
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    classes = list(model.classes_)
    spam_score = float(probabilities[classes.index("spam")])
    ham_score = float(probabilities[classes.index("ham")])

    if prediction == "spam":
        st.warning("Model prediction: SPAM")
    else:
        st.success("Model prediction: HAM")

    score_col, other_col = st.columns(2)
    score_col.metric("Model score for spam", f"{spam_score:.1%}")
    other_col.metric("Model score for ham", f"{ham_score:.1%}")
    st.caption(
        "These are uncalibrated model probabilities, not verified risk scores. A low spam score "
        "does not prove a message is safe."
    )

    with st.expander("Inspect largest feature contributions"):
        st.caption(
            "These values show how observed TF-IDF features add to or subtract from this linear "
            "model's spam score. They are not causal or semantic explanations, and depend on the "
            "training corpus."
        )
        contributions = logistic_feature_contributions(model, message)
        spam_col, ham_col = st.columns(2)
        if not contributions["toward_spam"] and not contributions["toward_ham"]:
            st.write("No message terms appeared in the fitted model vocabulary.")
        else:
            with spam_col:
                st.markdown("**Toward spam**")
                if contributions["toward_spam"]:
                    for item in contributions["toward_spam"]:
                        st.write(f"`{item['feature']}` (+{item['logit_contribution']:.3f})")
                else:
                    st.write("No observed features contributed toward spam.")
            with ham_col:
                st.markdown("**Toward ham**")
                if contributions["toward_ham"]:
                    for item in contributions["toward_ham"]:
                        st.write(f"`{item['feature']}` ({item['logit_contribution']:.3f})")
                else:
                    st.write("No observed features contributed toward ham.")

if cv_f1 is not None:
    st.metric("Cross-validation F1 for spam", f"{cv_f1:.3f}")
    st.caption("Pooled out-of-fold result from the documented five-fold experiment.")

st.divider()
st.subheader("Use the result carefully")
st.markdown(
    "- The corpus covers historical English messages and may not match current campaigns.\n"
    "- A `ham` prediction can still be a scam or phishing attempt.\n"
    "- Never use this demo as the sole basis for financial, security, or other consequential decisions.\n"
    "- Verify links and requests through the organization's official website or phone number."
)