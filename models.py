from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


class Order(BaseModel):
    id: int
    customer_name: str
    shipping_address: str
    order_date: datetime
    order_total: float
