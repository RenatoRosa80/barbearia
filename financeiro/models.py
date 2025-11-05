from django.db import models

# Create your models here.

from django.db import models

class MovimentoFinanceiro(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]
    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.tipo} - R$ {self.valor}"
