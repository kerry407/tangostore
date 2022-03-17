
from django.db import models

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True,max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(blank=True,max_length=150)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    zipcode = models.CharField(blank=True, max_length=8)
    image = models.ImageField(blank=True, null=True, upload_to='images/users/', default='images/users/default.png')

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        if self.user_id is not None:
            return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'
    
    @property
    def email(self):
        if self.user_id is not None:
            return (self.user.email)
        
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    image_tag.short_description = 'image'

    class Meta:
        db_table = 'userprofile'
        managed = True
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

