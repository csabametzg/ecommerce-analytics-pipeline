import matplotlib.pyplot as plt
from pathlib import Path


def plot_daily_revenue(daily_revenue_df):
    if daily_revenue_df.empty:
        return

    output_dir = Path("output/charts")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure()

    plt.plot(
        daily_revenue_df["order_date"],
        daily_revenue_df["total_amount"]
    )

    plt.title("Daily Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    file_path = output_dir / "daily_revenue.png"

    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()