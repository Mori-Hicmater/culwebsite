from django.shortcuts import render, get_object_or_404
from .models import Recipes

def index(request):
    cards = Recipes.objects.all()
    return render(request, 'main/index.html', {'cards': cards})

def about(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    return render(request, 'main/about.html', {'recipe': recipe})