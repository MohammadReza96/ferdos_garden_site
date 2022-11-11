from django.contrib import admin
from apps.place.models import Place,VisitorType,Rule,Ticket

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display=('place_name','visiting_day','visiting_hour','register_date')
    prepopulated_fields={'place_slug':('place_name',)}

@admin.register(VisitorType)
class VisitorTypeAdmin(admin.ModelAdmin):
    list_display=('visitor_type',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=('visitor_type','place','price')

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display=('title',)
