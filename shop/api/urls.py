from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path("v1/", lambda request: HttpResponse('{"name": "api"}', content_type="application/json"))
]