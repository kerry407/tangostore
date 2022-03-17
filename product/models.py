from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

   

    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True,upload_to='images')
    status = models.CharField(max_length=15,blank=True, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('True', 'True'),
    )

    AVAILABLE = (
        ('In Stock','In Stock'),
        ('Out of Stock','Out of Stock'),
        ('Restocked','Restocked'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    price = models.FloatField(null=True, blank=True)
    sizes = models.CharField(max_length=10, blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    available = models.CharField(max_length=30,blank=True, null=True, choices=AVAILABLE)
    quantity_instock = models.IntegerField(blank=True, null=True)
    minquantity = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True)
    status = models.CharField(max_length=30, blank=True, choices=STATUS)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(blank=True)
    latest = models.BooleanField(blank=True)
    banner = models.BooleanField(blank=True)
    offer = models.BooleanField(blank=True)
    detail = models.TextField(blank=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
