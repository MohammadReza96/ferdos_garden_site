from django.contrib import admin
from .models import *

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display=('place_name','place_image','visiting_day','visiting_hour','register_date','information','rules')
@admin.register(Visitor_Type)
class VisitorTypeAdmin(admin.ModelAdmin):
    list_display=('type_name',)
@admin.register(Ticket_price)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display=('place','visitor_type','price')
