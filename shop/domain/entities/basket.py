from dataclasses import dataclass
from typing import List

from shop.domain.entities.product import Product

@dataclass
class Basket:
    customer_id: str
    items: List[Product]

    def total_cost(self) -> float:
        return sum([i.price for i in self.items])
