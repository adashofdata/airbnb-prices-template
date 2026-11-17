# Chicago Airbnb Prices

What do Chicago Airbnb listings cost per night?

This project cleans Chicago Airbnb listings, adds a few useful columns, prints a summary and saves a chart.

## Team

<!-- Add one line for yourself directly below this comment: Name (@github-username): Issue # -->

## Setup

conda:
```
conda env create -f environment.yml
conda activate airbnb_prices
```

venv:
```
python3.14 -m venv .venv       # Windows: py -3.14 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run

`python main.py` cleans the raw data, prints a summary and saves a chart to `outputs/`

## How to Test

Run this from the project folder before every commit:

```
pytest            # run all the tests in tests/
```

GitHub runs `pytest` again on every pull request (see `.github/workflows/ci.yml`).

## Project Structure

```
airbnb-prices/
├── README.md
├── environment.yml / requirements.txt
├── pytest.ini                # test settings
├── .github/workflows/ci.yml  # checks GitHub runs on every pull request
├── data/
│   ├── raw/                  # original data, never edit
│   └── processed/            # created by main.py
├── src/
│   ├── cleaning.py           # load + clean prices
│   ├── features.py           # shared bathroom column
│   ├── pricing.py            # price per guest
│   └── plotting.py           # chart
├── tests/                    # one test file per src file
├── main.py                   # runs the full pipeline
└── outputs/                  # created by main.py
```

## Data

`data/raw/airbnb_listings.csv` is a random sample of 3,000 Chicago listings from the 19 September 2026 snapshot by [Inside Airbnb](https://insideairbnb.com/get-the-data/), used under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Only listing details are included (no host names).
