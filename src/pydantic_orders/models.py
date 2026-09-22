from pydantic import BaseModel, Field


class Order(BaseModel):   # Minsta längd för category,quantity/price över 0,disc mellan 0-1
    order_id: int
    customer_id: int


    product_category: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    discount: float = Field(ge=0,le=1,)