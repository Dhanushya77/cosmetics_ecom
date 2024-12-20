from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category = models.TextField()

class product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pid = models.TextField()
    name = models.TextField()
    dis = models.TextField()
    img = models.FileField()

class Details(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    price = models.IntegerField()
    offer_price = models.IntegerField()
    stock = models.IntegerField()
    weight = models.TextField()