from django.contrib import admin
from .models import *

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['id','title','address','phone','email','logo','created_at','uploaded_at']
    list_per_page = 1

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','title','brands']
    list_per_page = 1


class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email', 'subject','message','status', 'note')
    readonly_fields = ('name', 'subject','email', 'message')
    list_filter= ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email', 'subject','message','status', 'note')
    list_per_page = 20

class AboutAdmin(admin.ModelAdmin):
    list_display=('about', 'about_image')

admin.site.register(Setting, SettingAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(About, AboutAdmin)