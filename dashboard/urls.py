from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    # Partner
    path('partners/', views.PartnerListView.as_view(), name='partner_list'),
    path('partners/add/', views.PartnerCreateView.as_view(), name='partner_create'),
    path('partners/<int:pk>/edit/', views.PartnerUpdateView.as_view(), name='partner_edit'),
    path('partners/<int:pk>/delete/', views.PartnerDeleteView.as_view(), name='partner_delete'),

    # OurTeam
    path('ourteam/', views.OurTeamListView.as_view(), name='ourteam_list'),
    path('ourteam/add/', views.OurTeamCreateView.as_view(), name='ourteam_create'),
    path('ourteam/<int:pk>/edit/', views.OurTeamUpdateView.as_view(), name='ourteam_edit'),
    path('ourteam/<int:pk>/delete/', views.OurTeamDeleteView.as_view(), name='ourteam_delete'),

    # FarmHistory
    path('farmhistory/', views.FarmHistoryListView.as_view(), name='farmhistory_list'),
    path('farmhistory/add/', views.FarmHistoryCreateView.as_view(), name='farmhistory_create'),
    path('farmhistory/<int:pk>/edit/', views.FarmHistoryUpdateView.as_view(), name='farmhistory_edit'),
    path('farmhistory/<int:pk>/delete/', views.FarmHistoryDeleteView.as_view(), name='farmhistory_delete'),

    # PartnerImage
    path('partnerimage/', views.PartnerImageListView.as_view(), name='partnerimage_list'),
    path('partnerimage/add/', views.PartnerImageCreateView.as_view(), name='partnerimage_create'),
    path('partnerimage/<int:pk>/edit/', views.PartnerImageUpdateView.as_view(), name='partnerimage_edit'),
    path('partnerimage/<int:pk>/delete/', views.PartnerImageDeleteView.as_view(), name='partnerimage_delete'),

    # Manufacturing
    path('manufacturing/', views.ManufacturingListView.as_view(), name='manufacturing_list'),
    path('manufacturing/add/', views.ManufacturingCreateView.as_view(), name='manufacturing_create'),
    path('manufacturing/<int:pk>/edit/', views.ManufacturingUpdateView.as_view(), name='manufacturing_edit'),
    path('manufacturing/<int:pk>/delete/', views.ManufacturingDeleteView.as_view(), name='manufacturing_delete'),

    # Category
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/add/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Animal
    path('animal/', views.AnimalListView.as_view(), name='animal_list'),
    path('animal/add/', views.AnimalCreateView.as_view(), name='animal_create'),
    path('animal/<int:pk>/edit/', views.AnimalUpdateView.as_view(), name='animal_edit'),
    path('animal/<int:pk>/delete/', views.AnimalDeleteView.as_view(), name='animal_delete'),

    # Service
    path('service/', views.ServiceListView.as_view(), name='service_list'),
    path('service/add/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('service/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # News
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/add/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),

    # Gallery
    path('gallery/', views.GalleryListView.as_view(), name='gallery_list'),
    path('gallery/add/', views.GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/<int:pk>/edit/', views.GalleryUpdateView.as_view(), name='gallery_edit'),
    path('gallery/<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='gallery_delete'),

    # VeterinaryDrugs
    path('veterinarydrugs/', views.VeterinaryDrugsListView.as_view(), name='veterinarydrugs_list'),
    path('veterinarydrugs/add/', views.VeterinaryDrugsCreateView.as_view(), name='veterinarydrugs_create'),
    path('veterinarydrugs/<int:pk>/edit/', views.VeterinaryDrugsUpdateView.as_view(), name='veterinarydrugs_edit'),
    path('veterinarydrugs/<int:pk>/delete/', views.VeterinaryDrugsDeleteView.as_view(), name='veterinarydrugs_delete'),

    # Vaccine
    path('vaccine/', views.VaccineListView.as_view(), name='vaccine_list'),
    path('vaccine/add/', views.VaccineCreateView.as_view(), name='vaccine_create'),
    path('vaccine/<int:pk>/edit/', views.VaccineUpdateView.as_view(), name='vaccine_edit'),
    path('vaccine/<int:pk>/delete/', views.VaccineDeleteView.as_view(), name='vaccine_delete'),

    # CleaningProducts
    path('cleaningproducts/', views.CleaningProductsListView.as_view(), name='cleaningproducts_list'),
    path('cleaningproducts/add/', views.CleaningProductsCreateView.as_view(), name='cleaningproducts_create'),
    path('cleaningproducts/<int:pk>/edit/', views.CleaningProductsUpdateView.as_view(), name='cleaningproducts_edit'),
    path('cleaningproducts/<int:pk>/delete/', views.CleaningProductsDeleteView.as_view(),
         name='cleaningproducts_delete'),

    # VitaminsMinerals
    path('vitaminsminerals/', views.VitaminsMineralsListView.as_view(), name='vitaminsminerals_list'),
    path('vitaminsminerals/add/', views.VitaminsMineralsCreateView.as_view(), name='vitaminsminerals_create'),
    path('vitaminsminerals/<int:pk>/edit/', views.VitaminsMineralsUpdateView.as_view(), name='vitaminsminerals_edit'),
    path('vitaminsminerals/<int:pk>/delete/', views.VitaminsMineralsDeleteView.as_view(),
         name='vitaminsminerals_delete'),

    # Equipment
    path('equipment/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/add/', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/edit/', views.EquipmentUpdateView.as_view(), name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.EquipmentDeleteView.as_view(), name='equipment_delete'),

    # Paint
    path('paint/', views.PaintListView.as_view(), name='paint_list'),
    path('paint/add/', views.PaintCreateView.as_view(), name='paint_create'),
    path('paint/<int:pk>/edit/', views.PaintUpdateView.as_view(), name='paint_edit'),
    path('paint/<int:pk>/delete/', views.PaintDeleteView.as_view(), name='paint_delete'),

    # Work
    path('work/', views.WorkListView.as_view(), name='work_list'),
    path('work/add/', views.WorkCreateView.as_view(), name='work_create'),
    path('work/<int:pk>/edit/', views.WorkUpdateView.as_view(), name='work_edit'),
    path('work/<int:pk>/delete/', views.WorkDeleteView.as_view(), name='work_delete'),

    # Aminoacid
    path('aminoacid/', views.AminoacidListView.as_view(), name='aminoacid_list'),
    path('aminoacid/add/', views.AminoacidCreateView.as_view(), name='aminoacid_create'),
    path('aminoacid/<int:pk>/edit/', views.AminoacidUpdateView.as_view(), name='aminoacid_edit'),
    path('aminoacid/<int:pk>/delete/', views.AminoacidDeleteView.as_view(), name='aminoacid_delete'),

    # Food
    path('food/', views.FoodListView.as_view(), name='food_list'),
    path('food/add/', views.FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>/edit/', views.FoodUpdateView.as_view(), name='food_edit'),
    path('food/<int:pk>/delete/', views.FoodDeleteView.as_view(), name='food_delete'),
]
