# Generated by Django 4.2.6 on 2024-01-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.png', upload_to='profile/'),
        ),
    ]
