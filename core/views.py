from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Veiculos, MovRotativo, Mensalista, MovMensalista
from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMesForm

def home(request):
    context = {'mensagem': 'Core - Home'}
    return render(request, 'core/index.html', context)

#########  PESSOAS #############

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cor_url_pessoas')

def pessoa_update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data = {'pessoa': pessoa, 'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cor_url_pessoas')
    else:
        return render(request, 'core/pessoas_update.html', data)

#########  PESSOAS #############



#########  Veiculos #############

def lista_veiculos(request):
    veiculos = Veiculos.objects.all()
    form = VeiculoForm()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos, 'form': form})

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_url_veiculos')

def veiculo_update(request, id):
    veiculo = Veiculos.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_url_veiculos')
    else:
        return render(request, 'core/veiculos_update.html', {'veiculo': veiculo, 'form': form})

#########  Veiculos #############


#########  Movimentação Rotativo #############

def lista_mov_rot(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    return render(request,'core/lista_mov_rot.html', {'mov_rot': mov_rot, 'form': form})

def mov_rot_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_url_mov_rot')

def mov_rot_update(request, id):
    mr = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mr)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_url_mov_rot')
    else:
        return render(request, 'core/mr_update.html', {'mr':mr, 'form': form})

#########  Movimentação Rotativo #############



#########  Mensalista #############

def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas, 'form': form})

def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_url_mensalista')

def mensalista_update(request, id):
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_url_mensalista')
    else:
        return render(request, 'core/mensalistas_update.html', {'mensalista': mensalista, 'form': form})

#########  Mensalista #############


#########  MOV Mensalista #############

def lista_mov_mes(request):
    mov_mensal = MovMensalista.objects.all()
    form = MovMesForm()
    return render(request, 'core/lista_mov_mensal.html', {'mov_mensal': mov_mensal, 'form': form})

def mov_mes_novo(request):
    form = MovMesForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_url_mov_mensalista')

def mov_mes_update(request, id):
    mm = MovMensalista.objects.get(id=id)
    form = MovMesForm(request.POST or None, instance=mm)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_url_mov_mensalista')
    else:
        return render(request, 'core/mm_update.html', {'mm': mm, 'form': form})

#########  MOV Mensalista #############