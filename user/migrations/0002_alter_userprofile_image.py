# Generated by Django 3.2.8 on 2021-10-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/users/'),
        ),
    ]
