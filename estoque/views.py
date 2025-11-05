from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Produto, MovimentoEstoque
from .forms import ProdutoForm, MovimentoEstoqueForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/produtos.html', {'produtos': produtos})

def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/form_produto.html', {'form': form, 'titulo': 'Novo Produto'})

def novo_movimento(request):
    if request.method == 'POST':
        form = MovimentoEstoqueForm(request.POST)
        if form.is_valid():
            movimento = form.save()
            produto = movimento.produto
            if movimento.tipo == 'entrada':
                produto.quantidade += movimento.quantidade
            else:
                produto.quantidade -= movimento.quantidade
            produto.save()
            return redirect('lista_produtos')
    else:
        form = MovimentoEstoqueForm()
    return render(request, 'estoque/form_movimento.html', {'form': form, 'titulo': 'Movimento de Estoque'})
