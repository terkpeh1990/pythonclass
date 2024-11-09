from django.urls import path
from . import views

urlpatterns = [

   path('brands/',views.list_brands,name='brand-list'),

]