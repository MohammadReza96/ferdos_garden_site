from django.urls import path
import apps.blog.views as views

app_name='articles'

urlpatterns = [
    path('',views.show_blogs,name='show_blogs'),
]