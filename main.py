from src.utils.logger import setup_logger
from src.database.schema import create_tables
from src.api.client import fetch_orders

logger = setup_logger()

logger.info("Pipline started")

create_tables()
logger.info("Database initialized")

orders = fetch_orders()
logger.info(f"Orders received: {len(orders)}")