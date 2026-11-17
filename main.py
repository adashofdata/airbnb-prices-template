from pathlib import Path

from src.cleaning import clean_prices, load_raw_data
from src.features import add_features
from src.plotting import plot_median_price_by_room_type
from src.pricing import price_per_guest

# build file paths starting from the folder this script is in
PROJECT_DIR = Path(__file__).parent
RAW_PATH = PROJECT_DIR / 'data' / 'raw' / 'airbnb_listings.csv'
PROCESSED_PATH = PROJECT_DIR / 'data' / 'processed' / 'airbnb_listings_clean.csv'
FIGURE_PATH = PROJECT_DIR / 'outputs' / 'price_by_room_type.png'


def main():
    # 1. load
    df = load_raw_data(RAW_PATH)
    print(f'Loaded {len(df)} listings from data/raw')

    # 2. clean prices (Person A)
    df = clean_prices(df)
    print(f'{len(df)} listings left after cleaning prices')

    # 3. shared bathrooms (Person B)
    df = add_features(df)
    print(f'{df["shared_bath"].sum()} listings have a shared bathroom')

    # 4. price per guest (Person C)
    df['price_per_guest'] = price_per_guest(df['price'], df['accommodates'])
    print(f'Median price per guest: ${df["price_per_guest"].median():.0f}')

    # save the clean data
    PROCESSED_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print('Saved clean data to data/processed')

    # 5. chart (Person D)
    FIGURE_PATH.parent.mkdir(exist_ok=True)
    prices = plot_median_price_by_room_type(df, FIGURE_PATH)
    print(f'Chart says the median Private room costs ${prices["Private room"]:.0f}')
    print('Saved chart to outputs')


if __name__ == '__main__':
    main()
