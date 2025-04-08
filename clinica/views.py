from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm
from django.contrib import messages

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def listar_consulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'clinica/listar_consulta.html', {'consultas': consultas})

def criar_consulta(request): 
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta criada com sucesso!')
            return redirect('listar_consulta')
        else:
            messages.error(request, 'Erro ao salvar a consulta. Verifique os dados informados.')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form': form})

def detalhes_consulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    return render(request, 'clinica/detalhes_consulta.html', {'consulta': consulta})