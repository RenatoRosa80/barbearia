from django import forms
from .models import MovimentoFinanceiro

class MovimentoFinanceiroForm(forms.ModelForm):
    class Meta:
        model = MovimentoFinanceiro
        fields = ['descricao', 'tipo', 'valor', 'observacoes']
