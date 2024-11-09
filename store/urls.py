from django.urls import path
from .views import list_brands

urlpatterns = [

   path('brands/',list_brands,name='brand-list'),

]