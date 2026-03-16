from src.database.db import get_connection


def get_sql_metrics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM orders")
    total_orders = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM orders")
    total_revenue = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(AVG(total_amount), 0) FROM orders")
    avg_order_value = cursor.fetchone()[0]

    conn.close()

    return {
        "total_orders": total_orders,
        "total_revenue": round(total_revenue, 2),
        "avg_order_value": round(avg_order_value, 2),
    }

def get_top_customers(limit=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_name, SUM(total_amount) AS revenue
        FROM orders
        GROUP BY customer_name
        ORDER BY revenue DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows