from .db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    order_id TEXT UNIQUE,
    customer_name TEXT,
    total_amount REAL,
    created_at TEXT
)
        """)

    conn.commit()
    conn.close()