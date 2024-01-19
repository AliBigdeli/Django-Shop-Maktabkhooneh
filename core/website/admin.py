from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "subject","is_seen", "created_date")

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_date")