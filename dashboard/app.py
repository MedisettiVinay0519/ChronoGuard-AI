import streamlit as st
import pandas as pd
from PIL import Image
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)
from src.pipeline import run_pipeline

from src.llm.chatbot import (
    ask_energy_chatbot
)

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="ChronoGrid AI",
    layout="wide"
)

# =========================
# Title
# =========================

st.title("⚡ ChronoGrid AI")

st.subheader(
    "AI-Powered Smart Energy Forecasting & Anomaly Detection Platform"
)

# =========================
# Run Pipeline
# =========================

results = run_pipeline()

# =========================
# Extract Results
# =========================

metrics = results['metrics']

total_anomalies = results['total_anomalies']

insights = results['insights']

# =========================
# Sidebar
# =========================

st.sidebar.title("ChronoGrid AI")

st.sidebar.success(
    "System Pipeline Loaded"
)

# =========================
# Metrics Section
# =========================

st.header("📊 Forecasting Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "RMSE",
    f"{metrics['RMSE']:.4f}"
)

col2.metric(
    "MAE",
    f"{metrics['MAE']:.4f}"
)

col3.metric(
    "Anomalies",
    total_anomalies
)

# =========================
# Forecast Plot
# =========================

st.header("📈 Forecasting & Anomaly Detection")

image = Image.open(
    "outputs/forecast_vs_actual.png"
)

st.image(
    image,
    use_container_width=True
)

# =========================
# AI Insights
# =========================

st.header("🤖 LLM Insights")

st.write(insights)

# =========================
# Chatbot Section
# =========================

st.header("💬 ChronoGrid AI Chatbot")

user_question = st.text_input(
    "Ask a question about the energy analytics system"
)

if st.button("Generate Response"):

    chatbot_response = ask_energy_chatbot(
        user_question,
        metrics,
        total_anomalies
    )

    st.success(chatbot_response)

# =========================
# Footer
# =========================

st.markdown("---")

st.write(
    "ChronoGrid AI • Smart Energy Forecasting Platform"
)