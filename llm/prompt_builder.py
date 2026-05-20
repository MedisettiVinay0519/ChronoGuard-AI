def build_energy_prompt(
    metrics,
    total_anomalies
):

    prompt = f"""
You are an AI-powered smart energy analytics assistant.

Analyze the following forecasting results.

Forecasting Metrics:
- RMSE: {metrics['RMSE']:.4f}
- MAE: {metrics['MAE']:.4f}

Anomaly Detection:
- Total anomalies detected: {total_anomalies}

Generate:
1. Forecasting insights
2. Energy consumption insights
3. Anomaly detection insights
4. Overall system behavior summary

Keep the response professional and concise.
"""

    return prompt