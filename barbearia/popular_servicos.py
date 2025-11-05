import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seu_projeto.settings")  # substitua 'seu_projeto' pelo nome do seu projeto
django.setup()

from reservas.models import Servico

servicos_basicos = [
    {"nome": "Corte a Tesoura", "descricao": "Corte tradicional com tesoura", "preco": 40.00},
    {"nome": "Corte a Máquina", "descricao": "Corte rápido com máquina", "preco": 30.00},
    {"nome": "Química", "descricao": "Tratamento químico para cabelos", "preco": 150.00},
    {"nome": "Escova", "descricao": "Escova modeladora", "preco": 80.00},
    {"nome": "Tintura", "descricao": "Coloração de cabelos", "preco": 120.00},
]

for servico in servicos_basicos:
    Servico.objects.get_or_create(
        nome=servico["nome"],
        defaults={
            "descricao": servico["descricao"],
            "preco": servico["preco"]
        }
    )

print("Serviços básicos criados com sucesso.")
