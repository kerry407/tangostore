# Generated by Django 3.2.8 on 2021-10-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
