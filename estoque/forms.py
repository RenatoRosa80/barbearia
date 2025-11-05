from django import forms
from .models import Produto, MovimentoEstoque

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade', 'preco_unitario']

class MovimentoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentoEstoque
        fields = ['produto', 'tipo', 'quantidade', 'observacoes']
