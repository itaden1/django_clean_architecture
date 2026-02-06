from typing import List

from django.db.models import Q

from shop.domain.abstract_shop_repository import AbstractShopRepository


class ShopRepository(AbstractShopRepository):
    def get_or_create_customer(self, customer):
        pass