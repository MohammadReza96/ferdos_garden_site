from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.main.urls',namespace='index'),name='index'),
    path('garden_parts/',include('apps.places.urls',namespace='parts'),name='parts'),
    path('blog/',include('apps.blog.urls',namespace='articles'),name='articles'),
    path('garden_contact/',include('apps.form.urls',namespace='garden_contact'))


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

