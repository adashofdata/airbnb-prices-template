import pandas as pd

MAX_PRICE = 2000  # nightly prices above this are treated as outliers


def load_raw_data(path):
    """Read the raw CSV file. Never edit the raw file itself."""
    return pd.read_csv(path)


def clean_prices(df):
    """Turn price text into numbers, then drop missing and outlier prices.

    Example: '$90.00' -> 90.0 and '$1,250.00' -> 1250.0
    """
    df = df.copy()  # don't change the original DataFrame
    df['price'] = df['price'].str.replace('$', '')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])
    return df[df['price'] <= MAX_PRICE]
