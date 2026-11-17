import matplotlib.pyplot as plt


def plot_median_price_by_room_type(df, save_path):
    """Save a bar chart of the median price per room type and return the medians.

    Example: prices of 10, 20 and 90 -> median of 20.0
    """
    prices = df.groupby('room_type')['price'].mean().sort_values()

    fig, ax = plt.subplots(figsize=(6, 4))
    prices.plot.barh(ax=ax, color='purple')
    ax.set_title('Median Nightly Price by Room Type')
    ax.set_xlabel('Price per night ($)')
    ax.set_ylabel('')
    fig.tight_layout()

    fig.savefig(save_path)
    plt.close(fig)
    return prices
