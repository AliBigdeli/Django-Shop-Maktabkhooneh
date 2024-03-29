# Generated by Django 4.2.6 on 2024-01-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategorymodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='productimagemodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='breif_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
