from django.urls import path
from apps.index.views import show_home


app_name='index'

urlpatterns = [
    path("",show_home,name='home')
]