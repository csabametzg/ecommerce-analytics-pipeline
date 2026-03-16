import logging
from pathlib import Path


def setup_logger():
    log_dir = Path("output/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "pipeline.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)