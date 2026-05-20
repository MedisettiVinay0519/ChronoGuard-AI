import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt


def plot_forecast_vs_actual(
    y_test,
    predictions,
    anomalies
):

    plt.figure(figsize=(18,6))

    # Actual values
    plt.plot(
        y_test.index,
        y_test,
        label='Actual Consumption',
        color='blue'
    )

    # Predicted values
    plt.plot(
        y_test.index,
        predictions,
        label='Forecasted Consumption',
        color='green',
        linestyle='--'
    )

    # Anomalies
    plt.scatter(
        anomalies.index,
        y_test.loc[anomalies.index],
        color='red',
        s=60,
        label='Detected Anomalies'
    )

    plt.title(
        "ChronoGrid AI - Forecasting & Anomaly Detection"
    )

    plt.xlabel("Datetime")

    plt.ylabel("Power Consumption")

    plt.legend()

    plt.grid(True)

    # Save figure
    plt.savefig(
        "outputs/forecast_vs_actual.png",
        bbox_inches='tight'
    )

    # Close figure
    plt.close()