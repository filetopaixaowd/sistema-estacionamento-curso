from django.contrib import admin
from django.urls import path
from .views import home, lista_pessoas, lista_veiculos, lista_mov_rot, lista_mensalista, lista_mov_mes

urlpatterns = [
    path('', home),
    path('pessoas/', lista_pessoas),
    path('veiculos/', lista_veiculos),
    path('movimento-rotativo/', lista_mov_rot),
    path('mensalistas/', lista_mensalista),
    path('movimento-mensalista/', lista_mov_mes),
]