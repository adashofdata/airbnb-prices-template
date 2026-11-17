def price_per_guest(price, guests):
    """Split the nightly price across the guests.

    Example: $200 for 4 guests -> $50.0 per guest
    """
    return price * guests
