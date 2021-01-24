from django.urls import path
from . import views

app_name='menus'

urlpatterns = [
    path('', views.create_menus, name='create_menus'),
    path('new', views.create_dishes, name='create_dishes'),
    path('join', views.create_menu_dishes, name='create_menu_dishes'),
    path('show/<uuid:uuid>', views.view_menus, name='view_menus'),
]
