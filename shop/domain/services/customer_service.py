

from shop.domain import entities
from shop.domain.abstract_shop_repository import AbstractShopRepository


class CustomerService():
    repository: AbstractShopRepository

    def __init__(self, repository: AbstractShopRepository):
        self.repository = repository
    
    def promote_user_to_customer(self, user_id: int) -> entities.Customer:
        customer: entities.Customer = self.repository.get_or_create_customer(user_id)
        return customer