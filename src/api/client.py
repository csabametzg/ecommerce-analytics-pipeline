import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

WC_BASE_URL = os.getenv("ENV_WC_BASE_URL")
WC_CONSUMER_KEY = os.getenv("ENV_WC_CONSUMER_KEY")
WC_CONSUMER_SECRET = os.getenv("ENV_WC_CONSUMER_SECRET")


def fetch_orders():
    logger.info("Fetching orders from API")

    if not WC_BASE_URL:
        raise ValueError("WC_BASE_URL is missing from .env file")

    if not WC_CONSUMER_KEY or not WC_CONSUMER_SECRET:
        raise ValueError("WooCommerce API credentials are missing from .env file")

    url = f"{WC_BASE_URL}/wp-json/wc/v3/orders"


    response = requests.get(
        url,
        auth=(WC_CONSUMER_KEY, WC_CONSUMER_SECRET),
        params={"per_page": 20},
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code} - {response.text}")

    data = response.json()
    logger.info(f"Fetched {len(data)} orders")

    return data