from django.contrib import admin
from .models import Categories, Brands, UnitOfMeasurements,Products
# Register your models here.

admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(UnitOfMeasurements)
admin.site.register(Products)