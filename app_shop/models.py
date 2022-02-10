from email.mime import image
from itertools import product
from os import name
from pydoc import describe
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    describtion = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True)
    quantity  = models.PositiveIntegerField(null=True)
    
    tag =  models.ManyToManyField('Tag')

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class ImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to ='gallery')

    def __str__(self):
        return self.image.url
