from django.urls import path
from apps.place.views import show_places,ferdos_history,ferdos_path_garden,show_rules_prices

app_name='places'

urlpatterns = [
    path("",show_places,name='places'),
    path("ferdos_garden_history/",ferdos_history,name='history'),
    path('pdf/<str:filename>',ferdos_path_garden,name='pdf'),
    path('prices_rules/',show_rules_prices,name='price-rules')
]