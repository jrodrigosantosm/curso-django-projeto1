
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),  
    ]
# serve para informar o caminho após o diretório raiz,#
# int:id e uma forma de validação de dados #
