from pathlib import Path
from datetime import datetime
from src.utils.formatters import format_currency


def generate_txt_report(metrics, top_customers):

    output_dir = Path("output/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "report.txt"

    with open(report_path, "w", encoding="utf-8") as f:

        f.write("Ecommerce Analytics Report\n")
        f.write("===========================\n\n")

        f.write(f"Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n\n")

        f.write("Key Metrics\n")
        f.write("-----------\n")

        f.write(f"Total Orders: {metrics['total_orders']}\n")
        f.write(f"Total Revenue: {format_currency(metrics['total_revenue'])}\n")
        f.write(f"Average Order Value: {format_currency(metrics['avg_order_value'])}\n\n")

        f.write("Top Customers\n")
        f.write("-------------\n")

        for customer, revenue in top_customers:
            f.write(f"{customer} - {format_currency(revenue)}\n")