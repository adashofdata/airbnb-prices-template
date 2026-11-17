import pandas as pd

from src.cleaning import clean_prices

# every test follows the same three steps:
#   1. arrange: build a tiny DataFrame by hand (don't load the real data)
#   2. act: call the function you're testing
#   3. assert: check the result is what you expected


def test_clean_prices_converts_text_to_numbers():
    # arrange
    df = pd.DataFrame({'price': ['$90.00', '$45.50']})

    # act
    result = clean_prices(df)

    # assert
    assert list(result['price']) == [90.0, 45.5]


def test_clean_prices_drops_missing_prices():
    df = pd.DataFrame({'price': ['$90.00', None]})
    result = clean_prices(df)
    assert len(result) == 1
