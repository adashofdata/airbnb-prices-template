import pandas as pd


def is_shared_bath(text):
    """Return 1 if the bathroom is shared, otherwise 0.

    Example: '1 shared bath' -> 1 and '2 baths' -> 0
    """
    if pd.isna(text):
        return 0
    return int('Shared' in text)


def add_features(df):
    """Add a shared_bath column (1 = shared bathroom, 0 = not)."""
    df = df.copy()  # don't change the original DataFrame
    df['shared_bath'] = df['bathrooms_text'].apply(is_shared_bath)
    return df
