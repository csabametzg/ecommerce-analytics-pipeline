import argparse


def parse_args():

    parser = argparse.ArgumentParser(
        description="Ecommerce Analytics Pipeline"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Number of orders to fetch from API"
    )

    parser.add_argument(
        "--skip-charts",
        action="store_true",
        help="Skip chart generation"
    )

    return parser.parse_args()