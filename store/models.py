from django.db import models

# Create your models here.

class Brands(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"

class Categories(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.name}"

class UnitOfMeasurements(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=4)
    
    def __str__(self):
        return f"{self.name}"

class Products(models.Model):
    name = models.CharField(max_length=256)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)
    category_id = models.ForeignKey(Categories,on_delete=models.CASCADE)
    unitofmeasurement_id = models.ForeignKey(UnitOfMeasurements,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} {self.unit_price}"



