from django.contrib import admin
from .models import ContactModel



@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=('name','family','title','register_time','email')