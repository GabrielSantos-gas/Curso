from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render (request, 'recipes/pages/home.html', 
                   context={ 'recipes': [make_recipe() for _ in range(10)],
                            'is_detail_page': False

    }) 


def recipe(request, id):
    recipe_data = make_recipe()  # Substitua isso pela lógica real para obter os dados da receita
    return render(request, 'recipes/pages/recipe-id.html', 
                  context={'recipe': recipe_data, 
                           'is_detail_page': True})



