from django.urls import path
import apps.form.views as views

app_name='garden_contact'

urlpatterns = [
    path('',views.show_form,name='contact'),
]