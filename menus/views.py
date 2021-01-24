from django.shortcuts import render
from .forms import MenuForm, DishesForm, MenuDishesForm
from .models import Menus, Dishes, MenusDishes
# Create your views here.

class dishes_function:  
    def __init__(self, name, description):  
        self.name = name  
        self.description = description 

def create_menus(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.cleaned_data['name']
            form.cleaned_data['description']
            form.cleaned_data['create_date']
            form.save()
    else:
        form = MenuForm()
    return render(request, 'menus/menu/create.html', {'form': form})


def create_dishes(request):
    if request.method == 'POST':
        form = DishesForm(request.POST)
        if form.is_valid():
            form.cleaned_data['name']
            form.cleaned_data['description']
            form.save()
    else:
        form = DishesForm()
    return render(request, 'menus/dishes/create.html', {'form': form})

def create_menu_dishes(request):
    if request.method == 'POST':
        form = MenuDishesForm(request.POST)
        if form.is_valid():
            form.cleaned_data['dishes_id']
            form.cleaned_data['menus_id']
            form.save()
    else:
        form = MenuDishesForm()
    return render(request, 'menus/menu_dishes/create.html', {'form': form})

def view_menus(request, uuid):
    print(uuid)
    dishes = []
    menus = Menus.objects.get(url_id=str(uuid))
    menusDishes = MenusDishes.objects.filter(menus_id=menus.id)
    for md in menusDishes:
        d = Dishes.objects.filter(id=md.dishes_id.id)
        dishes.append(dishes_function(d[0].name, d[0].description))
    return render(request, 'menus/menu/show.html', {'menus':  menus, 'dishes': dishes})