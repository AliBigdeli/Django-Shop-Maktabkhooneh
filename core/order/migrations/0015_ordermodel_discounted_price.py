# Generated by Django 4.2.6 on 2024-01-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_ordermodel_options_alter_ordermodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='discounted_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]