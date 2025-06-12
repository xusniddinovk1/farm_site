from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]