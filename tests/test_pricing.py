from src.pricing import price_per_guest


def test_price_per_guest_one_guest():
    assert price_per_guest(100, 1) == 100.0
