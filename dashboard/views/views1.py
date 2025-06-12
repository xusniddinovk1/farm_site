from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect("home_page")
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
    aminoacids = Aminoacid.objects.all()
    animals = Animal.objects.all()
    categories = Category.objects.all()
    cleaning_products = CleaningProducts.objects.all()
    equipments = Equipment.objects.all()
    foods = Food.objects.all()
    photos = Gallery.objects.all()
    manufacturing = Manufacturing.objects.all()
    news = News.objects.all()
    paints = Paint.objects.all()
    vaccines = Vaccine.objects.all()
    veterinaries = VeterinaryDrugs.objects.all()
    vitamins = VitaminsMinerals.objects.all()

    ctx = {
        "counts": {
            "aminoacids": len(aminoacids),
            "educations": len(animals),
            "activities": len(categories),
            "hotels": len(cleaning_products),
            "rest_area": len(equipments),
            "foods": len(foods),
            "photos": len(photos),
            "manufacturing": len(manufacturing),
            "news": len(news),
            "paints": len(paints),
            "vaccines": len(vaccines),
            "veterinaries": len(veterinaries),
            "vitamins": len(vitamins),
        }
    }
    return render(request, 'dashboard/index.html', ctx)


# --- Gallery Views ---
@login_required_decorator
def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'dashboard/gallery/list.html', {'galleries': galleries})


@login_required_decorator
def gallery_create(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryForm()
    return render(request, 'dashboard/gallery/form.html', {'form': form})


@login_required_decorator
def gallery_update(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryForm(instance=gallery)
    return render(request, 'dashboard/gallery/form.html', {'form': form})


@login_required_decorator
def gallery_delete(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    gallery.delete()
    return redirect('gallery_list')
