import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import docx

# Load model
model = joblib.load("classify_model.pkl")
categories = model.classes_

st.set_page_config(page_title="Document/News Classifier", layout="wide")
st.title("📰 Enhanced Document/News Classifier")

# Read document text from uploaded file
def read_document(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return None

# Input options
st.sidebar.header("📤 Input Method")
input_method = st.sidebar.radio("Choose Input Type:", ["Manual Entry", "Upload Document"])

if input_method == "Manual Entry":
    text_input = st.text_area("✍️ Enter document/news text:", height=250)
elif input_method == "Upload Document":
    uploaded_file = st.file_uploader("📂 Upload .txt or .docx file", type=["txt", "docx"])
    text_input = read_document(uploaded_file) if uploaded_file else ""

# Predict and Display
if st.button("Classify"):
    if not text_input.strip():
        st.warning("⚠️ Please provide some text to classify.")
    else:
        probs = model.predict_proba([text_input])[0]
        top_indices = np.argsort(probs)[::-1]
        top_category = categories[top_indices[0]]
        st.success(f"📌 Predicted Category: **{top_category}**")

        # Show confidence scores
        st.subheader("📊 Prediction Confidence Scores")
        score_df = pd.DataFrame({
            "Category": categories,
            "Confidence": probs
        }).sort_values(by="Confidence", ascending=False)

        st.bar_chart(score_df.set_index("Category"))

        # Show top 3 categories
        st.markdown("### 🔢 Top 3 Predictions")
        for idx in top_indices[:3]:
            st.write(f"➡️ {categories[idx]} — **{probs[idx]*100:.2f}%**")
