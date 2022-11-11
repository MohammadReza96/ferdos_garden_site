from django.urls import path
from .views import ShowMemory,like,add_memory
app_name='memory'

urlpatterns = [
    path("",ShowMemory.as_view(),name='_memory'),
    path("addmemory/",add_memory,name='_add'),
    path("like/",like.as_view(),name='like'),
]