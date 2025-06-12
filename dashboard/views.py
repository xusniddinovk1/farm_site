from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.models.aboutUs import *
from core.models.misc import *
from core.models.product1 import *
from core.models.product import *
from core.models.product2 import *
from core.models.product3 import *
from dashboard.forms.misc import *
from dashboard.forms.aboutUs import *
from dashboard.forms.product2 import *
from dashboard.forms.product import *
from dashboard.forms.product1 import *
from dashboard.forms.product3 import *


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
def account_view(request):
    return render(request, 'dashboard/account.html')


@login_required_decorator
def settings_view(request):
    return render(request, 'dashboard/settings.html')


@login_required_decorator
def billing_view(request):
    return render(request, 'dashboard/billing.html')


@login_required_decorator
def home_page(request):
    return render(request, 'dashboard/index.html', )
