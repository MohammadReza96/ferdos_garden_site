from django.contrib import admin
from apps.form.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','time_added','is_seen_by_manager','text')