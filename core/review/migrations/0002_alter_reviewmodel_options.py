# Generated by Django 4.2.6 on 2024-01-19 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewmodel',
            options={'ordering': ['-created_date']},
        ),
    ]
