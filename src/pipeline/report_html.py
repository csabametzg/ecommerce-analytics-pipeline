from pathlib import Path
from datetime import datetime
from src.utils.formatters import format_currency


def generate_html_report(metrics, top_customers):

    output_dir = Path("output/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "report.html"

    html = f"""
    <html>
    <head>
        <title>Ecommerce Analytics Report</title>
        <style>
            body {{ font-family: Arial; margin: 40px; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 400px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #f4f4f4; }}
        </style>
    </head>

    <body>

    <h1>Ecommerce Analytics Report</h1>

    <p><b>Generated:</b> {datetime.now()}</p>

    <h2>Key Metrics</h2>

    <ul>
        <li>Total Orders: {metrics['total_orders']}</li>
        <li>Total Revenue: {format_currency(metrics['total_revenue'])}</li>
        <li>Average Order Value: {format_currency(metrics['avg_order_value'])}</li>
    </ul>

    <h2>Top Customers</h2>

    <table>
        <tr>
            <th>Customer</th>
            <th>Revenue</th>
        </tr>
    """

    for customer, revenue in top_customers:
        html += f"""
        <tr>
            <td>{customer}</td>
            <td>{format_currency(revenue)}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)