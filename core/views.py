from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculos, MovRotativo, Mensalista, MovMensalista

def home(request):
    context = {'mensagem': 'Core - Home'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas':  pessoas})

def lista_veiculos(request):
    veiculos = Veiculos.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})

def lista_mov_rot(request):
    mov_rot = MovRotativo.objects.all()
    return render(request,'core/lista_mov_rot.html', {'mov_rot': mov_rot})

def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})

def lista_mov_mes(request):
    mov_mensal = MovMensalista.objects.all()
    return render(request, 'core/lista_mov_mensal.html', {'mov_mensal': mov_mensal})

