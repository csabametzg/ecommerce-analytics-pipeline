from src.utils.logger import setup_logger
from src.database.schema import create_tables
from src.api.client import fetch_orders
from src.pipeline.save_orders import save_orders_to_db
from src.pipeline.sql_metrics import get_sql_metrics, get_top_customers
from src.pipeline.analysis import load_orders_dataframe, analyze_orders

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

from src.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM orders")
count = cursor.fetchone()[0]
conn.close()

logger.info(f"Orders in database: {count}")

metrics = get_sql_metrics()

logger.info(f"Total orders: {metrics['total_orders']}")
logger.info(f"Total revenue: {metrics['total_revenue']}")
logger.info(f"Average order value: {metrics['avg_order_value']}")

top_customers = get_top_customers()

logger.info("Top customers:")
for customer_name, revenue in top_customers:
    logger.info(f"{customer_name}: {revenue}")


df = load_orders_dataframe()
analysis = analyze_orders(df)

logger.info(f"DataFrame rows: {len(df)}")
logger.info("Top 5 orders by value:")
logger.info(f"\n{analysis['top_orders']}")