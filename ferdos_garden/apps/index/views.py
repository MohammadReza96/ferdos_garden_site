from django.shortcuts import render
from django.conf import settings


def media_admin(request):
    return {'media_url':settings.MEDIA_URL}

    
def show_home(request):
    return render(request,'index/home/home.html')



# def error_404_view(request,exception):
#     return render(request,'index/404/404.html')