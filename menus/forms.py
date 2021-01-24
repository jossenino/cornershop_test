from django.forms import ModelForm
from .models import Menus, Dishes, MenusDishes


class MenuForm(ModelForm):
    class Meta:
        model = Menus
        fields = ['name', 'description', 'create_date']

class DishesForm(ModelForm):
    class Meta:
        model = Dishes
        fields = ['name', 'description']

class MenuDishesForm(ModelForm):
    class Meta:
        model = MenusDishes
        fields = ['dishes_id', 'menus_id']