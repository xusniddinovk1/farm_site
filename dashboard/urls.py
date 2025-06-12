from django.urls import path
from dashboard.views.manufacturing import *
from .views.partner import partner_list, partner_create, partner_update, partner_delete, partner_image_list, \
    partner_image_create, partner_image_update, partner_image_delete
from .views.farm_history import *
from .views.equipment import *
from .views.misc import *
from .views.misc1 import *
from .views.our_team import *
from .views.service import *
from .views.veterinary import vaccine_list, vaccine_create, vaccine_update, vaccine_delete, veterinary_drugs_list, \
    veterinary_drugs_create, veterinary_drugs_update, veterinary_drugs_delete
from .views.vitamins import *
from .views.views1 import home_page, login_page, logout_page, gallery_list, gallery_create, gallery_update, \
    gallery_delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    # Partner
    path('partners/', partner_list, name='partner_list'),
    path('partners/add/', partner_create, name='partner_create'),
    path('partners/<int:pk>/edit/', partner_update, name='partner_edit'),
    path('partners/<int:pk>/delete/', partner_delete, name='partner_delete'),

    # OurTeam
    path('ourteam/', our_team_list, name='our_team_list'),
    path('ourteam/add/', our_team_create, name='our_team_create'),
    path('ourteam/<int:pk>/edit/', our_team_update, name='our_team_edit'),
    path('ourteam/<int:pk>/delete/', our_team_delete, name='our_team_delete'),

    # FarmHistory
    path('farmhistory/', farm_history_list, name='farm_history_list'),
    path('farmhistory/add/', farm_history_create, name='farm_history_create'),
    path('farmhistory/<int:pk>/edit/', farm_history_update, name='farm_history_edit'),
    path('farmhistory/<int:pk>/delete/', farm_history_delete, name='farm_history_delete'),

    # PartnerImage
    path('partnerimage/', partner_image_list, name='partner_image_list'),
    path('partnerimage/add/', partner_image_create, name='partner_image_create'),
    path('partnerimage/<int:pk>/edit/', partner_image_update, name='partner_image_edit'),
    path('partnerimage/<int:pk>/delete/', partner_image_delete, name='partner_image_delete'),

    # Manufacturing
    path('manufacturing/', manufacturing_list, name='manufacturing_list'),
    path('manufacturing/add/', manufacturing_create, name='manufacturing_create'),
    path('manufacturing/<int:pk>/edit/', manufacturing_update, name='manufacturing_edit'),
    path('manufacturing/<int:pk>/delete/', manufacturing_delete, name='manufacturing_delete'),

    # Category
    path('category/', category_list, name='category_list'),
    path('category/add/', category_create, name='category_create'),
    path('category/<int:pk>/edit/', category_update, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),

    # Animal
    path('animal/', animal_list, name='animal_list'),
    path('animal/add/', animal_create, name='animal_create'),
    path('animal/<int:pk>/edit/', animal_update, name='animal_edit'),
    path('animal/<int:pk>/delete/', animal_delete, name='animal_delete'),

    # Service
    path('service/', service_list, name='service_list'),
    path('service/add/', service_create, name='service_create'),
    path('service/<int:pk>/edit/', service_update, name='service_edit'),
    path('service/<int:pk>/delete/', service_delete, name='service_delete'),

    # News
    path('news/', news_list, name='news_list'),
    path('news/add/', news_create, name='news_create'),
    path('news/<int:pk>/edit/', news_update, name='news_edit'),
    path('news/<int:pk>/delete/', news_delete, name='news_delete'),

    # Gallery
    path('gallery/', gallery_list, name='gallery_list'),
    path('gallery/add/', gallery_create, name='gallery_create'),
    path('gallery/<int:pk>/edit/', gallery_update, name='gallery_edit'),
    path('gallery/<int:pk>/delete/', gallery_delete, name='gallery_delete'),

    # VeterinaryDrugs
    path('veterinarydrugs/', veterinary_drugs_list, name='veterinary-drugs_list'),
    path('veterinarydrugs/add/', veterinary_drugs_create, name='veterinary-drugs_create'),
    path('veterinarydrugs/<int:pk>/edit/', veterinary_drugs_update, name='veterinary-drugs_edit'),
    path('veterinarydrugs/<int:pk>/delete/', veterinary_drugs_delete, name='veterinary-drugs_delete'),

    # Vaccine
    path('vaccine/', vaccine_list(), name='vaccine_list'),
    path('vaccine/add/', vaccine_create, name='vaccine_create'),
    path('vaccine/<int:pk>/edit/', vaccine_update, name='vaccine_edit'),
    path('vaccine/<int:pk>/delete/', vaccine_delete, name='vaccine_delete'),

    # CleaningProducts
    path('cleaningproducts/', cleaning_products_list, name='cleaning_products_list'),
    path('cleaningproducts/add/', cleaning_products_create, name='cleaning_products_create'),
    path('cleaningproducts/<int:pk>/edit/', cleaning_products_update, name='cleaning_products_edit'),
    path('cleaningproducts/<int:pk>/delete/', cleaning_products_delete,
         name='cleaning_products_delete'),

    # VitaminsMinerals
    path('vitaminsminerals/', vitamins_minerals_list, name='vitamins_minerals_list'),
    path('vitaminsminerals/add/', vitamins_minerals_create, name='vitamins_minerals_create'),
    path('vitaminsminerals/<int:pk>/edit/', vitamins_minerals_update, name='vitamins_minerals_edit'),
    path('vitaminsminerals/<int:pk>/delete/', vitamins_minerals_delete,
         name='vitamins_minerals_delete'),

    # Equipment
    path('equipment/', equipments_list, name='equipment_list'),
    path('equipment/add/', equipment_create, name='equipment_create'),
    path('equipment/<int:pk>/edit/', equipment_update, name='equipment_edit'),
    path('equipment/<int:pk>/delete/', equipments_delete, name='equipment_delete'),

    # Paint
    path('paint/', paints_list, name='paint_list'),
    path('paint/add/', paint_create, name='paint_create'),
    path('paint/<int:pk>/edit/', paint_update, name='paint_edit'),
    path('paint/<int:pk>/delete/', paint_delete, name='paint_delete'),

    # Work
    path('work/', work_list, name='work_list'),
    path('work/add/', work_create, name='work_create'),
    path('work/<int:pk>/edit/', work_update, name='work_edit'),
    path('work/<int:pk>/delete/', work_delete, name='work_delete'),

    # Aminoacid
    path('aminoacid/', aminoacids_list, name='aminoacid_list'),
    path('aminoacid/add/', aminoacids_create, name='aminoacid_create'),
    path('aminoacid/<int:pk>/edit/', aminoacids_update, name='aminoacid_edit'),
    path('aminoacid/<int:pk>/delete/', aminoacids_delete, name='aminoacid_delete'),

    # Food
    path('food/', food_list, name='food_list'),
    path('food/add/', food_create, name='food_create'),
    path('food/<int:pk>/edit/', food_update, name='food_edit'),
    path('food/<int:pk>/delete/', food_delete, name='food_delete'),
]
