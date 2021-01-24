import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=150)

class Menus(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=150)
    create_date = models.DateField()
    url_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

class MenusDishes(models.Model):
    dishes_id = models.ForeignKey(Dishes, null=True, on_delete=models.SET_NULL)
    menus_id = models.ForeignKey(Menus, null=True, on_delete=models.SET_NULL)
