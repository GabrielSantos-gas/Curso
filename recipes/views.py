from django.shortcuts import render
from utils.recipes.factory import make_recipe



# views.py
def home(request):
    return render(request, 'recipes/pages/home.html', 
                  context={'recipes': [make_recipe() for _ in range(10)],
                           'is_detail_page': False})

def recipe(request, id):
    # Lógica para obter dados da receita com base no ID
    recipe_data = make_recipe()  # Supondo que make_recipe aceita um ID como argumento
    return render(request, 'recipes/pages/recipe-id.html', 
                  context={'recipe': recipe_data, 
                           'is_detail_page': True})
