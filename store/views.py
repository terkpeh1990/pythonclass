from django.shortcuts import render,redirect
from .models import Brands,Categories,UnitOfMeasurements,Products
# Create your views here.
from .forms import BrandForm

def list_brands(request):
    brands = Brands.objects.all() # lists all brands and store it in a variable called brands
    template_name = 'store/brands.html' #Set the html file and store it in a variable called template_name
    context = {
        'brands': brands,
    }
    return render(request,template_name,context)


def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Brands.objects.create(name=name)
            return redirect('brand-list')
    form = BrandForm()
    template_name = 'store/create-brand.html'
    context = {
        'form':form
    }
    return render(request, template_name,context)


# CRUD = CREATE READ UPDATE DELETE