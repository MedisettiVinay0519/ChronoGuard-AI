import pandas as pd


def calculate_residuals(
    y_true,
    y_pred
):

    residuals = y_true - y_pred

    return residuals


def detect_anomalies(
    residuals,
    threshold_factor=1.5
):

    threshold = (
        threshold_factor
        * residuals.std()
    )

    anomalies = residuals[
        abs(residuals) > threshold
    ]

    return anomalies