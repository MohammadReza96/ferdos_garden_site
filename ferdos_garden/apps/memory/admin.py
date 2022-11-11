from django.contrib import admin
from .models import Memory,MemoryGallary



@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display=('memory_title','memory_register_date','memory_is_active','user_register')
    
    
@admin.register(MemoryGallary)
class MemoryGallaryAdmin(admin.ModelAdmin):
    list_display=('memory','memory_image')