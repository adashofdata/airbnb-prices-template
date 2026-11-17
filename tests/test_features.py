from src.features import is_shared_bath


def test_is_shared_bath_shared():
    assert is_shared_bath('Shared half-bath') == 1


def test_is_shared_bath_not_shared():
    assert is_shared_bath('2 baths') == 0
