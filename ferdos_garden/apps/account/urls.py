from django.urls import path
from .views import RegisterUserView,LoginUserView,LogoutUser
app_name='account'

urlpatterns = [
    path('sign_up/',RegisterUserView.as_view(),name='sign_up'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('logout/',LogoutUser.as_view(),name='logout')
]