from pathlib import Path
from datetime import datetime
from src.utils.formatters import format_currency


def generate_html_report(metrics, top_customers):
    output_dir = Path("output/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "report.html"

    top_customers_rows = ""
    for customer, revenue in top_customers:
        top_customers_rows += f"""
        <tr>
            <td>{customer}</td>
            <td>{format_currency(revenue)}</td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>Ecommerce Analytics Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f7f9fc;
                color: #1f2937;
            }}

            h1 {{
                margin-bottom: 8px;
            }}

            .generated {{
                color: #6b7280;
                margin-bottom: 30px;
            }}

            .cards {{
                display: flex;
                gap: 20px;
                margin-bottom: 30px;
                flex-wrap: wrap;
            }}

            .card {{
                background: white;
                border-radius: 12px;
                padding: 20px;
                min-width: 220px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            }}

            .card h3 {{
                margin: 0 0 10px 0;
                font-size: 16px;
                color: #6b7280;
            }}

            .card p {{
                margin: 0;
                font-size: 24px;
                font-weight: bold;
            }}

            .section {{
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                max-width: 700px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 10px;
            }}

            th, td {{
                text-align: left;
                padding: 12px;
                border-bottom: 1px solid #e5e7eb;
            }}

            th {{
                background-color: #f3f4f6;
            }}
        </style>
    </head>
    <body>

        <h1>Ecommerce Analytics Report</h1>
        <p class="generated">
            Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </p>

        <div class="cards">
            <div class="card">
                <h3>Total Orders</h3>
                <p>{metrics['total_orders']}</p>
            </div>

            <div class="card">
                <h3>Total Revenue</h3>
                <p>{format_currency(metrics['total_revenue'])}</p>
            </div>

            <div class="card">
                <h3>Average Order Value</h3>
                <p>{format_currency(metrics['avg_order_value'])}</p>
            </div>
        </div>

        <div class="section">
            <h2>Top Customers</h2>
            <table>
                <tr>
                    <th>Customer</th>
                    <th>Revenue</th>
                </tr>
                {top_customers_rows}
            </table>
        </div>

    </body>
    </html>
    """

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)