import pandas as pd
from src.database.db import get_connection


def load_orders_dataframe():
    conn = get_connection()

    df = pd.read_sql_query("SELECT * FROM orders", conn)
    conn.close()

    return df


def analyze_orders(df):
    if df.empty:
        return {
            "daily_revenue": pd.DataFrame(),
            "top_orders": pd.DataFrame(),
        }

    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["order_date"] = df["created_at"].dt.date

    daily_revenue = (
        df.groupby("order_date", as_index=False)["total_amount"]
        .sum()
        .sort_values("order_date")
    )

    top_orders = (
        df[["order_id", "customer_name", "total_amount", "created_at"]]
        .sort_values("total_amount", ascending=False)
        .head(5)
    )

    return {
        "daily_revenue": daily_revenue,
        "top_orders": top_orders,
    }