import sqlite3
from pathlib import Path

def get_connection():
    db_path = Path("data/ecommerce.db")
    db_path.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(db_path)
    return conn
