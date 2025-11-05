from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import MovimentoFinanceiro
from .forms import MovimentoFinanceiroForm

def lista_movimentos(request):
    movimentos = MovimentoFinanceiro.objects.all().order_by('-data_hora')
    return render(request, 'financeiro/movimentos.html', {'movimentos': movimentos})

def novo_movimento(request):
    if request.method == 'POST':
        form = MovimentoFinanceiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_movimentos')
    else:
        form = MovimentoFinanceiroForm()
    return render(request, 'financeiro/form_movimento.html', {'form': form, 'titulo': 'Novo Movimento Financeiro'})
