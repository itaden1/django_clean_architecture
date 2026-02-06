from django.urls import path, include

from shop.admin import shop_admin_site

urlpatterns = [
    path("", include("shop.web.urls")),
    path("api/", include("shop.api.urls")),
    path("admin/", shop_admin_site.urls)
]