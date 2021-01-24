from django.urls import path
from . import views

app_name='notifications'

urlpatterns = [
    path('create', views.create_notifications, name='create_notifications'),
]
