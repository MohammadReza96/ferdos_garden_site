from django.urls import path
from .views import show_blogs,show_blog

app_name='blogs'

urlpatterns = [
    path('',show_blogs,name='_blogs'),
    path('<str:blog_slug>',show_blog,name='_blog')
]