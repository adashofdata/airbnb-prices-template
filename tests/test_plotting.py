import pandas as pd

from src.plotting import plot_median_price_by_room_type


def test_plot_saves_a_file(tmp_path):
    # tmp_path is a temporary folder pytest makes for you, so tests don't fill outputs/
    df = pd.DataFrame({'room_type': ['A', 'A'], 'price': [10.0, 30.0]})
    save_path = tmp_path / 'chart.png'
    plot_median_price_by_room_type(df, save_path)
    assert save_path.exists()


def test_plot_returns_median_price(tmp_path):
    # you don't test the picture: test the numbers the function returns
    df = pd.DataFrame({'room_type': ['A', 'A'], 'price': [10.0, 30.0]})
    result = plot_median_price_by_room_type(df, tmp_path / 'chart.png')
    assert result['A'] == 20.0
