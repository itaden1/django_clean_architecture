from abc import ABC, abstractmethod
from shop.domain import entities

class AbstractShopRepository(ABC):
    @abstractmethod
    def get_or_create_customer(self, customer: entities.Customer):
        pass