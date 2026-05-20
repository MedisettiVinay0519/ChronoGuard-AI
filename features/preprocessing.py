import pandas as pd


def preprocess_data(df):

    # Create datetime column
    df['Datetime'] = pd.to_datetime(
        df['Date'] + ' ' + df['Time'],
        format='%d/%m/%Y %H:%M:%S'
    )

    # Set index
    df.set_index('Datetime', inplace=True)

    # Drop original columns
    df.drop(['Date', 'Time'], axis=1, inplace=True)

    # Convert columns to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors='coerce'
        )

    # Handle missing values
    df = df.interpolate(method='time')

    # Hourly resampling
    hourly_df = df.resample('h').mean()

    return hourly_df