from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from django.conf import settings

from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    next_url = request.GET.get("next", settings.LOGIN_REDIRECT_URL)

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get("next", next_url)
            parsed_url = urlparse(next_url)
            if not parsed_url.netloc and is_valid_path(next_url):
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    else:
        form = AuthenticationForm()
    return render(
        request, 
        "accounts/login.html", 
        {"form": form, "next": next_url}
    )
