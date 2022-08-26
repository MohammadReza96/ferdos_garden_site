from django.urls import path
import apps.main.views as views

app_name='index'

urlpatterns = [
    path('',views.index,name='home'),
]