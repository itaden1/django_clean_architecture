from django.contrib import admin
from django.apps import apps

app = apps.get_app_config("shop")

for model_name, model in app.models.items():
    admin.site.register(model)

from django.apps import apps
from django.contrib import admin

class StoreAdminSite(admin.AdminSite):
    site_header = "Shop admin"
    site_title = "Shop admin portal"
    index_title = "Welcom to the Shop admin site"

shop_admin_site = StoreAdminSite(name="shop_admin")

app = apps.get_app_config("shop")
for model_name, model in app.models.items():
    shop_admin_site.register(model)
