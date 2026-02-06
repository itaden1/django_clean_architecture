from django.shortcuts import render

from shop.domain.abstract_shop_repository import AbstractShopRepository
from shop.domain.services.customer_service import CustomerService
from shop.models.repository import ShopRepository


def _get_service() -> AbstractShopRepository:
    repository = ShopRepository()
    service = CustomerService(repository)
    return service


def index(request):
    user = request.user
    if user.is_authenticated:
        service = _get_service()
        service.promote_user_to_customer(user.id)

    return render(request, "shop/home.html", {"user": user})
