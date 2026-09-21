from pathlib import Path

import pandas as pd
from pydantic import ValidationError

from pydantic_orders.models import Order


def validate_orders(path: Path) -> tuple[list[Order], list[dict]]:
    """Validera orderdata från en CSV-fil."""

    data = pd.read_csv(path)

    valid_orders = []
    invalid_orders = []

    for row_number, row in data.iterrows():
        try:
            order = Order(**row.to_dict())
            valid_orders.append(order)

        except ValidationError as error:
            invalid_orders.append(
                {
                    "row": row_number + 1,
                    "error": str(error),
                }
            )

    return valid_orders, invalid_orders