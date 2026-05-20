from groq import Groq

from src.utils.config import (
    GROQ_API_KEY
)


# Initialize Groq Client
client = Groq(
    api_key=GROQ_API_KEY
)


def ask_energy_chatbot(
    user_question,
    metrics,
    total_anomalies
):

    # =========================
    # Context
    # =========================

    context = f"""
You are ChronoGrid AI,
an intelligent smart energy analytics assistant.

System Analytics Summary:

Forecasting Metrics:
- RMSE: {metrics['RMSE']:.4f}
- MAE: {metrics['MAE']:.4f}

Anomaly Detection:
- Total anomalies detected: {total_anomalies}

Your role:
- Explain forecasting performance
- Explain anomaly behavior
- Explain energy usage trends
- Answer user questions professionally
"""

    # =========================
    # LLM Response
    # =========================

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[

            {
                "role": "system",
                "content": context
            },

            {
                "role": "user",
                "content": user_question
            }
        ],

        temperature=0.5
    )

    # =========================
    # Extract Answer
    # =========================

    answer = (
        response
        .choices[0]
        .message.content
    )

    return answer