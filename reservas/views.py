from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento, Servico
from .forms import AgendamentoForm

def index(request):
    servicos = Servico.objects.all()
    return render(request, 'index.html', {'servicos': servicos})

@login_required
def agendamentos(request):
    agendamentos = Agendamento.objects.filter(cliente=request.user)
    return render(request, 'agendamentos.html', {'agendamentos': agendamentos})

@login_required
def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente = request.user
            agendamento.save()
            return redirect('agendamentos')
    else:
        # Preenche o serviço se passado via GET
        servico_id = request.GET.get('servico')
        if servico_id:
            form = AgendamentoForm(initial={'servico': servico_id})
        else:
            form = AgendamentoForm()
    return render(request, 'editar_agendamento.html', {'form': form, 'titulo': 'Novo Agendamento'})

@login_required
def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk, cliente=request.user)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'editar_agendamento.html', {'form': form, 'titulo': 'Editar Agendamento'})

@login_required
def cancelar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk, cliente=request.user)
    agendamento.status = 'cancelado'
    agendamento.save()
    return redirect('agendamentos')

@login_required
def pagar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk, cliente=request.user)
    agendamento.status = 'pago'
    agendamento.save()
    return redirect('agendamentos')
