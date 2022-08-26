from django.urls import path,re_path
import apps.places.views as views


app_name='parts'

urlpatterns = [
    
    # type 1 (using path)
    # path('',views.show_garden_parts,name='garden_parts'),      
    # path('part/<int:id>/',views.show_garden_part,name='garden_part'),
    # path('garden_path/',views.download_path_garden,name='garden_path'),
    # path('garden_plans_rules/',views.show_plans_rules,name='garden_plans_rules'),

    
    # type 2 (using re_path)
    re_path(r'^parts',views.show_garden_parts,name='garden_parts'),
    re_path(r'^part/(?P<id>[\d]+)/$',views.show_garden_part,name='garden_part'),
    re_path(r'^garden_path',views.download_path_garden,name='garden_path'),
    re_path(r'^garden_plans_rules',views.show_plans_rules,name='garden_plans_rules'),


]
