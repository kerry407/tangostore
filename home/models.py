from django.db import models
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Setting(models.Model):

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, null=True,blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(null=True, max_length=15)
    secondary_phone = models.CharField(null=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    secondary_fax = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    secondary_email = models.CharField(blank=True, max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to='images')
    favicon = models.ImageField(blank=True, null=True, upload_to='images')
    About_img_1 = models.ImageField(blank=True, null=True, upload_to='images')
    About_img_2 = models.ImageField(blank=True, null=True, upload_to='images')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    message = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    

    def __str__(self):
        return self.title



    
class Brand(models.Model):
    title = models.CharField(max_length=50,blank=True)
    brands = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title


 
class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class About(models.Model):
    about = RichTextUploadingField(blank=True)
    about_image = models.ImageField(blank=True, null=True, upload_to='images')