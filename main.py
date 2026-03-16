from src.utils.logger import setup_logger
from src.database.schema import create_tables
from src.api.client import fetch_orders
from src.pipeline.save_orders import save_orders_to_db

logger = setup_logger()

logger.info("Pipline started")

create_tables()
logger.info("Database initialized")

orders = fetch_orders()
logger.info(f"Orders received: {len(orders)}")

save_orders_to_db(orders)
logger.info("Orders saved to database")

from src.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM orders")
count = cursor.fetchone()[0]
conn.close()

logger.info(f"Orders in database: {count}")