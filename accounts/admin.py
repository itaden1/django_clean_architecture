from django.apps import apps
from django.contrib import admin

class AccountAdminSite(admin.AdminSite):
    site_header = 'Accounts admin'
    site_title = 'Accounts admin portal'
    index_title = 'Welcom to the accounts admin site'

account_admin_site = AccountAdminSite(name='account_admin')

app = apps.get_app_config('accounts')
for model_name, model in app.models.items():
    account_admin_site.register(model)

auth_app = apps.get_app_config('auth')
for model_name, model in auth_app.models.items():
    account_admin_site.register(model)