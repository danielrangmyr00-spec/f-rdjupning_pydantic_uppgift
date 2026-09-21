from pydantic import ValidationError
import pytest

from pydantic_orders.models import Order


def test_valid_order() -> None:
    order = Order(
        order_id=1,
        customer_id=1001,
        product_category="Electronics",
        quantity=2,
        unit_price=499.99,
        discount=0.10,
    )

    assert order.quantity == 2
    assert order.discount == 0.10


def test_negative_quantity() -> None:
    with pytest.raises(ValidationError):
        Order(
            order_id=1,
            customer_id=1001,
            product_category="Electronics",
            quantity= -1,
            unit_price=499.99,
            discount=0.10,
        )


def test_discount_above_one() -> None:
    with pytest.raises(ValidationError):
        Order(
            order_id=1,
            customer_id=1001,
            product_category="Electronics",
            quantity=2,
            unit_price=499.99,
            discount= 1.5,
        )