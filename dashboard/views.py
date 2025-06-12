from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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


# --- Partner Views ---
class PartnerListView(ListView):
    model = Partner
    template_name = 'dashboard/partner/list.html'  # mos template nomini o'zgartiring
    context_object_name = 'partners'


class PartnerCreateView(CreateView):
    model = Partner
    fields = ['context']
    template_name = 'dashboard/partner/form.html'
    success_url = reverse_lazy('partner_list')


class PartnerUpdateView(UpdateView):
    model = Partner
    fields = ['context']
    template_name = 'dashboard/partner/form.html'
    success_url = reverse_lazy('partner_list')


class PartnerDeleteView(DeleteView):
    model = Partner
    template_name = 'dashboard/partner/form.html'
    success_url = reverse_lazy('partner_list')


# --- OurTeam Views ---
class OurTeamListView(ListView):
    model = OurTeam
    template_name = 'dashboard/our_team/list.html'
    context_object_name = 'teams'


class OurTeamCreateView(CreateView):
    model = OurTeam
    fields = ['image']
    template_name = 'dashboard/our_team/form.html'
    success_url = reverse_lazy('ourteam_list')


class OurTeamUpdateView(UpdateView):
    model = OurTeam
    fields = ['image']
    template_name = 'dashboard/our_team/form.html'
    success_url = reverse_lazy('ourteam_list')


class OurTeamDeleteView(DeleteView):
    model = OurTeam
    template_name = 'dashboard/our_team/form.html'
    success_url = reverse_lazy('ourteam_list')


# --- FarmHistory Views ---
class FarmHistoryListView(ListView):
    model = FarmHistory
    template_name = 'dashboard/farm_history/list.html'
    context_object_name = 'farmhistories'


class FarmHistoryCreateView(CreateView):
    model = FarmHistory
    fields = ['year', 'title', 'slug', 'context']
    template_name = 'dashboard/farm_history/form.html'
    success_url = reverse_lazy('farmhistory_list')


class FarmHistoryUpdateView(UpdateView):
    model = FarmHistory
    fields = ['year', 'title', 'slug', 'context']
    template_name = 'dashboard/farm_history/form.html'
    success_url = reverse_lazy('farmhistory_list')


class FarmHistoryDeleteView(DeleteView):
    model = FarmHistory
    template_name = 'dashboard/farm_history/form.html'
    success_url = reverse_lazy('farmhistory_list')


# --- PartnerImage Views ---
class PartnerImageListView(ListView):
    model = PartnerImage
    template_name = 'dashboard/partner_image/list.html'
    context_object_name = 'partnerimages'


class PartnerImageCreateView(CreateView):
    model = PartnerImage
    fields = ['partner', 'image']
    template_name = 'dashboard/partner_image/form.html'
    success_url = reverse_lazy('partnerimage_list')


class PartnerImageUpdateView(UpdateView):
    model = PartnerImage
    fields = ['partner', 'image']
    template_name = 'dashboard/partner_image/form.html'
    success_url = reverse_lazy('partnerimage_list')


class PartnerImageDeleteView(DeleteView):
    model = PartnerImage
    template_name = 'dashboard/partner_image/form.html'
    success_url = reverse_lazy('partnerimage_list')


# --- Manufacturing Views ---
class ManufacturingListView(ListView):
    model = Manufacturing
    template_name = 'dashboard/manufacturing/list.html'
    context_object_name = 'manufacturings'


class ManufacturingCreateView(CreateView):
    model = Manufacturing
    fields = ['title', 'context', 'image']
    template_name = 'dashboard/manufacturing/form.html'
    success_url = reverse_lazy('manufacturing_list')


class ManufacturingUpdateView(UpdateView):
    model = Manufacturing
    fields = ['title', 'context', 'image']
    template_name = 'dashboard/manufacturing/form.html'
    success_url = reverse_lazy('manufacturing_list')


class ManufacturingDeleteView(DeleteView):
    model = Manufacturing
    template_name = 'dashboard/manufacturing/form.html'
    success_url = reverse_lazy('manufacturing_list')


# --- Category Views ---
class CategoryListView(ListView):
    model = Category
    template_name = 'dashboard/category/list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['title', 'slug']
    template_name = 'dashboard/category/form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['title', 'slug']
    template_name = 'dashboard/category/form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'dashboard/category/form.html'
    success_url = reverse_lazy('category_list')


# --- Animal Views ---
class AnimalListView(ListView):
    model = Animal
    template_name = 'dashboard/animal/list.html'
    context_object_name = 'animals'


class AnimalCreateView(CreateView):
    model = Animal
    fields = ['name']
    template_name = 'dashboard/animal/form.html'
    success_url = reverse_lazy('animal_list')


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = ['name']
    template_name = 'dashboard/animal/form.html'
    success_url = reverse_lazy('animal_list')


class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'dashboard/animal/form.html'
    success_url = reverse_lazy('animal_list')


# --- Service Views ---
class ServiceListView(ListView):
    model = Service
    template_name = 'dashboard/service/list.html'
    context_object_name = 'services'


class ServiceCreateView(CreateView):
    model = Service
    fields = ['title', 'slug', 'context', 'image']
    template_name = 'dashboard/service/form.html'
    success_url = reverse_lazy('service_list')


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['title', 'slug', 'context', 'image']
    template_name = 'dashboard/service/form.html'
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'dashboard/service/form.html'
    success_url = reverse_lazy('service_list')


# --- News Views ---
class NewsListView(ListView):
    model = News
    template_name = 'dashboard/news/list.html'
    context_object_name = 'news_list'


class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'slug', 'content', 'image']
    template_name = 'dashboard/news/form.html'
    success_url = reverse_lazy('news_list')


class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'slug', 'content', 'image']
    template_name = 'dashboard/news/form.html'
    success_url = reverse_lazy('news_list')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'dashboard/news/form.html'
    success_url = reverse_lazy('news_list')


# --- Gallery Views ---
class GalleryListView(ListView):
    model = Gallery
    template_name = 'dashboard/gallery/list.html'
    context_object_name = 'galleries'


class GalleryCreateView(CreateView):
    model = Gallery
    fields = ['image']
    template_name = 'dashboard/gallery/form.html'
    success_url = reverse_lazy('gallery_list')


class GalleryUpdateView(UpdateView):
    model = Gallery
    fields = ['image']
    template_name = 'dashboard/gallery/form.html'
    success_url = reverse_lazy('gallery_list')


class GalleryDeleteView(DeleteView):
    model = Gallery
    template_name = 'dashboard/gallery/form.html'
    success_url = reverse_lazy('gallery_list')


# --- VeterinaryDrugs Views ---
class VeterinaryDrugsListView(ListView):
    model = VeterinaryDrugs
    template_name = 'dashboard/veterinary/list.html'
    context_object_name = 'drugs'


class VeterinaryDrugsCreateView(CreateView):
    model = VeterinaryDrugs
    fields = [
        'category', 'for_what', 'animals', 'title', 'slug', 'image', 'structure',
        'instruction', 'dosage', 'release_period', 'manufacturer'
    ]
    template_name = 'dashboard/veterinary/form.html'
    success_url = reverse_lazy('veterinarydrugs_list')


class VeterinaryDrugsUpdateView(UpdateView):
    model = VeterinaryDrugs
    fields = [
        'category', 'for_what', 'animals', 'title', 'slug', 'image', 'structure',
        'instruction', 'dosage', 'release_period', 'manufacturer'
    ]
    template_name = 'dashboard/veterinary/form.html'
    success_url = reverse_lazy('veterinarydrugs_list')


class VeterinaryDrugsDeleteView(DeleteView):
    model = VeterinaryDrugs
    template_name = 'dashboard/veterinary/form.html'
    success_url = reverse_lazy('veterinarydrugs_list')


# --- Vaccine Views ---
class VaccineListView(ListView):
    model = Vaccine
    template_name = 'dashboard/vaccine/list.html'
    context_object_name = 'vaccines'


class VaccineCreateView(CreateView):
    model = Vaccine
    fields = [
        'category', 'title', 'slug', 'for_what', 'structure', 'animals',
        'image', 'manufacturer', 'drug', 'usage', 'expiration_date', 'storage'
    ]
    template_name = 'dashboard/vaccine/form.html'
    success_url = reverse_lazy('vaccine_list')


class VaccineUpdateView(UpdateView):
    model = Vaccine
    fields = [
        'category', 'title', 'slug', 'for_what', 'structure', 'animals',
        'image', 'manufacturer', 'drug', 'usage', 'expiration_date', 'storage'
    ]
    template_name = 'dashboard/vaccine/form.html'
    success_url = reverse_lazy('vaccine_list')


class VaccineDeleteView(DeleteView):
    model = Vaccine
    template_name = 'dashboard/vaccine/form.html'
    success_url = reverse_lazy('vaccine_list')


# --- CleaningProducts Views ---
class CleaningProductsListView(ListView):
    model = CleaningProducts
    template_name = 'dashboard/cleaning/list.html'
    context_object_name = 'cleaning_products'


class CleaningProductsCreateView(CreateView):
    model = CleaningProducts
    fields = [
        'category', 'for_what', 'animal', 'manufacturer', 'title', 'slug',
        'image', 'about', 'structure', 'usage', 'packaging'
    ]
    template_name = 'dashboard/cleaning/form.html'
    success_url = reverse_lazy('cleaningproducts_list')


class CleaningProductsUpdateView(UpdateView):
    model = CleaningProducts
    fields = [
        'category', 'for_what', 'animal', 'manufacturer', 'title', 'slug',
        'image', 'about', 'structure', 'usage', 'packaging'
    ]
    template_name = 'dashboard/cleaning/form.html'
    success_url = reverse_lazy('cleaningproducts_list')


class CleaningProductsDeleteView(DeleteView):
    model = CleaningProducts
    template_name = 'dashboard/cleaning/form.html'
    success_url = reverse_lazy('cleaningproducts_list')


# --- VitaminsMinerals Views ---
class VitaminsMineralsListView(ListView):
    model = VitaminsMinerals
    template_name = 'dashboard/vitamins/list.html'
    context_object_name = 'vitaminsminerals'


class VitaminsMineralsCreateView(CreateView):
    model = VitaminsMinerals
    fields = [
        'category', 'for_what', 'animal', 'title', 'slug', 'image',
        'effect', 'dosage', 'contraindications', 'instruction', 'packaging'
    ]
    template_name = 'dashboard/vitamins/form.html'
    success_url = reverse_lazy('vitaminsminerals_list')


class VitaminsMineralsUpdateView(UpdateView):
    model = VitaminsMinerals
    fields = [
        'category', 'for_what', 'animal', 'title', 'slug', 'image',
        'effect', 'dosage', 'contraindications', 'instruction', 'packaging'
    ]
    template_name = 'dashboard/vitamins/form.html'
    success_url = reverse_lazy('vitaminsminerals_list')


class VitaminsMineralsDeleteView(DeleteView):
    model = VitaminsMinerals
    template_name = 'dashboard/vitamins/form.html'
    success_url = reverse_lazy('vitaminsminerals_list')


# --- Equipment Views ---
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'dashboard/equipment/list.html'
    context_object_name = 'equipment_list'


class EquipmentCreateView(CreateView):
    model = Equipment
    fields = ['title', 'slug', 'description', 'image']
    template_name = 'dashboard/equipment/form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentUpdateView(UpdateView):
    model = Equipment
    fields = ['title', 'slug', 'description', 'image']
    template_name = 'dashboard/equipment/form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'dashboard/equipment/form.html'
    success_url = reverse_lazy('equipment_list')


# --- Paint Views ---
class PaintListView(ListView):
    model = Paint
    template_name = 'dashboard/paint/list.html'
    context_object_name = 'paints'


class PaintCreateView(CreateView):
    model = Paint
    fields = ['category', 'title', 'slug', 'image', 'dosage', 'animals']
    template_name = 'dashboard/paint/form.html'
    success_url = reverse_lazy('paint_list')


class PaintUpdateView(UpdateView):
    model = Paint
    fields = ['category', 'title', 'slug', 'image', 'dosage', 'animals']
    template_name = 'dashboard/paint/form.html'
    success_url = reverse_lazy('paint_list')


class PaintDeleteView(DeleteView):
    model = Paint
    template_name = 'dashboard/paint/form.html'
    success_url = reverse_lazy('paint_list')


# --- Work Views ---
class WorkListView(ListView):
    model = Work
    template_name = 'dashboard/work/list.html'
    context_object_name = 'works'


class WorkCreateView(CreateView):
    model = Work
    fields = ['title', 'slug', 'context', 'image']
    template_name = 'dashboard/work/form.html'
    success_url = reverse_lazy('work_list')


class WorkUpdateView(UpdateView):
    model = Work
    fields = ['title', 'slug', 'context', 'image']
    template_name = 'dashboard/work/form.html'
    success_url = reverse_lazy('work_list')


class WorkDeleteView(DeleteView):
    model = Work
    template_name = 'dashboard/work/form.html'
    success_url = reverse_lazy('work_list')


# --- Aminoacid Views ---
class AminoacidListView(ListView):
    model = Aminoacid
    template_name = 'dashboard/aminoacid/list.html'
    context_object_name = 'aminoacids'


class AminoacidCreateView(CreateView):
    model = Aminoacid
    fields = [
        'category', 'for_what', 'animal', 'title', 'slug', 'image',
        'manufacturer', 'effect', 'instruction', 'advantages', 'preparation'
    ]
    template_name = 'dashboard/aminoacid/form.html'
    success_url = reverse_lazy('aminoacid_list')


class AminoacidUpdateView(UpdateView):
    model = Aminoacid
    fields = [
        'category', 'for_what', 'animal', 'title', 'slug', 'image',
        'manufacturer', 'effect', 'instruction', 'advantages', 'preparation'
    ]
    template_name = 'dashboard/aminoacid/form.html'
    success_url = reverse_lazy('aminoacid_list')


class AminoacidDeleteView(DeleteView):
    model = Aminoacid
    template_name = 'dashboard/aminoacid/form.html'
    success_url = reverse_lazy('aminoacid_list')


# --- Food Views ---
class FoodListView(ListView):
    model = Food
    template_name = 'dashboard/food/list.html'
    context_object_name = 'foods'


class FoodCreateView(CreateView):
    model = Food
    fields = [
        'category', 'for_what', 'animal', 'manufacturer', 'title', 'slug',
        'image', 'effect', 'instruction', 'packaging'
    ]
    template_name = 'dashboard/food/form.html'
    success_url = reverse_lazy('food_list')


class FoodUpdateView(UpdateView):
    model = Food
    fields = [
        'category', 'for_what', 'animal', 'manufacturer', 'title', 'slug',
        'image', 'effect', 'instruction', 'packaging'
    ]
    template_name = 'dashboard/food/form.html'
    success_url = reverse_lazy('food_list')


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'dashboard/food/form.html'
    success_url = reverse_lazy('food_list')
