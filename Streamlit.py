import streamlit as st
import joblib
import re

# ==========================
# Load Model and Vectorizer
# ==========================
try:
    model = joblib.load("../models/model.joblib")
    vectorizer = joblib.load("../models/vectorizer.joblib")
except Exception as e:
    st.error(f"❌ Error loading model files: {e}")
    st.stop()

# ==========================
# Cleaning Function
# ==========================
def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+|www.\S+", "", text)  # remove only URLs
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()     # normalize spaces
    return text

# ==========================
# Streamlit UI
# ==========================
st.set_page_config(page_title="Fake News Detection App", layout="wide")

st.title("📰 Fake News Detection ML App")
st.write(
    """
    This application predicts whether a news article is **REAL** or **FAKE**  
    using a **TF-IDF Vectorizer** and **Logistic Regression Model** trained offline.
    """
)

st.markdown("---")

# Input Box
news = st.text_area("📝 Paste the news article here:", height=250)

# Predict Button
if st.button("🔍 Predict"):
    if news.strip() == "":
        st.warning("⚠️ Please enter a news article.")
    else:
        cleaned = clean_text(news)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0][pred]

        st.markdown("---")
        st.subheader("📊 Prediction Result")

        if pred == 1:
            st.success(f"🟢 REAL NEWS (Confidence: {proba:.2f})")
        else:
            st.error(f"🔴 FAKE NEWS (Confidence: {proba:.2f})")

        st.markdown("---")
        st.info("Model: Logistic Regression | Vectorizer: TF-IDF | Offline Mode Enabled")

