from src.utils.logger import setup_logger
from src.database.schema import create_tables

logger = setup_logger()

logger.info("Pipline started")

create_tables()

logger.info("Database initialized")