from pathlib import Path

from pydantic_orders.validator import validate_orders


def main() -> None:
    valid_orders, invalid_orders = validate_orders(
        Path("data/orders.csv")
    )

    print(f"Giltiga ordrar: {len(valid_orders)}")
    print(f"Ogiltiga ordrar: {len(invalid_orders)}")

    if invalid_orders:
        print("\nValideringsfel:")

        for error in invalid_orders:
            print(
                f"Rad {error['row']}: "
                f"{error['error']}"
            )


if __name__ == "__main__":
    main()