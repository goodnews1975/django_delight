from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import  DeleteView
from inventory.models import Ingredient, MenuItem, RecipeRequirement, Purchase

# Create your views here.

class IngredientListView(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy("ingredient-list")
   

class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"
    
class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
