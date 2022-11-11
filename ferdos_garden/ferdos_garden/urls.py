from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('apps.index.urls',namespace='index')),
    path("places/",include('apps.place.urls',namespace='places')),
    path("blog/",include('apps.blog.urls',namespace='blog')),
    path("contact_us/",include('apps.contact_us.urls',namespace='contact')),
    path("blogs/",include('apps.blog.urls',namespace='blogs')),
    path("acount/",include('apps.account.urls',namespace='account')),
    path("memories/",include('apps.memory.urls',namespace='memory')),
    path('search/',include('apps.search.urls',namespace='search'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# handler404 = "apps.index.views.error_404_view"