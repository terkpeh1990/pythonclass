from django.shortcuts import render
from .models import Brands,Categories,UnitOfMeasurements,Products
# Create your views here.

def list_brands(request):
    brands = Brands.objects.all() # lists all brands and store it in a variable called brands
    template_name = 'store/brands.html' #Set the html file and store it in a variable called template_name
    context = {
        'brands': brands,
    }
    return render(request,template_name,context)

