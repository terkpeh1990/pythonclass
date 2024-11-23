from django.urls import path
from . import views

urlpatterns = [

   path('brands/',views.list_brands,name='brand-list'),
   path('brands/new/',views.create_brand,name='create-brands'),

]