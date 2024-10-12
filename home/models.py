from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places = 2,max_digits = 8, default = 0)
    stock = models.IntegerField(default = 0)

    def __str__(self):
        return self.name




