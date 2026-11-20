"""Local Streamlit interface for the trained SMS spam model."""

from pathlib import Path

import joblib
import streamlit as st


MODEL_PATH = Path(__file__).resolve().parent / "models" / "logistic_regression.joblib"

st.set_page_config(page_title="SMS Spam Classifier", page_icon="📩", layout="centered")
st.title("English SMS Spam Classifier")
st.write("Enter an English text message to see the model's estimated label.")

if not MODEL_PATH.is_file():
    st.info("The model has not been trained yet. Follow the setup steps in the project README.")
    st.stop()

model = joblib.load(MODEL_PATH)
message = st.text_area("Message", height=160, placeholder="Paste an SMS message here…")

if st.button("Classify message", type="primary", disabled=not message.strip()):
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    class_index = list(model.classes_).index(prediction)
    confidence = float(probabilities[class_index])

    if prediction == "spam":
        st.warning(f"Model prediction: SPAM (estimated probability {confidence:.1%})")
    else:
        st.success(f"Model prediction: HAM (estimated probability {confidence:.1%})")

st.caption(
    "Educational demonstration trained on a historical English SMS dataset. "
    "Predictions and probabilities can be wrong or poorly calibrated. This tool does not "
    "verify scams, links, senders, or current threats; do not use it as the sole basis "
    "for security, financial, or other consequential decisions."
)
