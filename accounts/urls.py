from django.urls import path, include 

from accounts.admin import account_admin_site

urlpatterns = [
    path("", include("accounts.web.urls")),
    # path("auth/", include("django.contrib.auth.urls")),
    path("admin/", account_admin_site.urls),
]