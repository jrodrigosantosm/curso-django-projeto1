from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')

#recebe as requisições do urls e encaminha o conteúdo#
