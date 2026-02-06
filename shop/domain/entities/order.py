from dataclasses import dataclass
from typing import List

from shop.domain.entities.product import Product

@dataclass
class Order:
    customer_id: str
    items: List[Product]
    