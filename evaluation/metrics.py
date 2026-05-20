from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error
)

import numpy as np


def calculate_metrics(
    y_true,
    y_pred
):

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    return {
        "RMSE": rmse,
        "MAE": mae
    }