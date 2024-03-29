from django.contrib import admin
from django.urls import path
from .views import home, lista_pessoas, lista_veiculos, lista_mov_rot, lista_mensalista, lista_mov_mes,\
    pessoa_novo, veiculo_novo, mov_rot_novo, mensalista_novo, mov_mes_novo, pessoa_update, veiculo_update, \
    mov_rot_update, mensalista_update, mov_mes_update, pessoa_delete, veiculo_delete, mov_rot_delete, mensalista_delete, \
    mov_mes_delete

urlpatterns = [
    path('', home),
    path('pessoas/', lista_pessoas, name="cor_url_pessoas"),
    path('pessoas-novo/', pessoa_novo, name="cor_url_pessoas_novo"),
    path('pessoas-update/<int:id>', pessoa_update, name="cor_url_pessoas_update"),
    path('pessoas-delete/<int:id>', pessoa_delete, name="cor_url_pessoas_delete"),

    path('veiculos/', lista_veiculos, name='core_url_veiculos'),
    path('veiculos-novo/', veiculo_novo, name='core_url_veiculos_novo'),
    path('veiculos-update/<int:id>', veiculo_update, name='core_url_veiculos_update'),
    path('veiculos-delete/<int:id>', veiculo_delete, name='core_url_veiculos_delete'),

    path('movimento-rotativo/', lista_mov_rot, name='core_url_mov_rot'),
    path('movimento-rotativo-novo/', mov_rot_novo, name='core_url_mov_rot_novo'),
    path('movimento-rotativo-update/<int:id>', mov_rot_update, name='core_url_mov_rot_update'),
    path('movimento-rotativo-delete/<int:id>', mov_rot_delete, name='core_url_mov_rot_delete'),

    path('mensalistas/', lista_mensalista, name='core_url_mensalista'),
    path('mensalistas-novo/', mensalista_novo, name='core_url_mensalista_novo'),
    path('mensalistas-update/<int:id>', mensalista_update, name='core_url_mensalista_update'),
    path('mensalistas-delete/<int:id>', mensalista_delete, name='core_url_mensalista_delete'),


    path('movimento-mensalista/', lista_mov_mes, name='core_url_mov_mensalista'),
    path('movimento-mensalista-novo/', mov_mes_novo, name='core_url_mov_mensalista_novo'),
    path('movimento-mensalista-update/<int:id>', mov_mes_update, name='core_url_mov_men_update'),
    path('movimento-mensalista-delete/<int:id>', mov_mes_delete, name='core_url_mov_men_delete'),
]