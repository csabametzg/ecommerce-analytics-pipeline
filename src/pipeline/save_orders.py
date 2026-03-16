from src.database.db import get_connection

def save_orders_to_db(orders):
    conn = get_connection()
    cursor = conn.cursor()

    for order in orders:
        order_id = str(order.get("id"))
        customer_name = "Unknown Customer"
        total_amount = 0.0
        created_at = order.get("date_created", "")

        billing = order.get("billing", {})
        first_name = billing.get("first_name", "").strip()
        last_name = billing.get("last_name", "").strip()

        if first_name or last_name:
            customer_name = f"{first_name} {last_name}".strip()

        total_value = order.get("total", 0)
        try:
            total_amount = float(total_value)
        except (TypeError, ValueError):
            total_amount = 0.0

        cursor.execute("""
        INSERT OR IGNORE INTO orders (order_id, customer_name, total_amount, created_at)
            VALUES (?, ?, ?, ?)
        """, (order_id, customer_name, total_amount, created_at))

    conn.commit()
    conn.close()