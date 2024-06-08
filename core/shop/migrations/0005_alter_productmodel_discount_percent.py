# Generated by Django 4.2.6 on 2024-01-10 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productmodel_breif_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount_percent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
