from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from menus.models import Menus

# Create your models here.

class Notifications(models.Model):
    type = models.CharField(max_length=10)
    description = models.CharField(max_length=150)
    send_date = models.DateField()
    menus_id = models.ForeignKey(Menus, null=True, on_delete=models.SET_NULL)