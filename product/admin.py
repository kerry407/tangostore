from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'status', 'image']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category','discount_price',  'status', 'image', 'quantity_instock',
                    'available', 'banner', 'slug', 'offer', 'featured']
    list_filter = ['category']
    list_display_links = ['title', 'category', 'status', 'image']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['banner', 'offer']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)