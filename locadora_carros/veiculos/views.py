from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo
from .forms import VeiculoForm
from django.core.paginator import Paginator


def listar_veiculos(request):
    veiculos = Veiculo.objects.all().order_by('marca', 'modelo')


    marca_filter = request.GET.get('marca')
    if marca_filter:
        veiculos = veiculos.filter(marca__icontains=marca_filter)

    paginator = Paginator(veiculos, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'listar_veiculos.html', {'page_obj': page_obj, 'marca_filter': marca_filter})


def exibir_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    return render(request, 'exibir_veiculo.html', {'veiculo': veiculo})


def criar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'criar_veiculo.html', {'form': form})


def editar_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'editar_veiculo.html', {'form': form})


def excluir_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')
    return render(request, 'excluir_veiculo.html', {'veiculo': veiculo})




