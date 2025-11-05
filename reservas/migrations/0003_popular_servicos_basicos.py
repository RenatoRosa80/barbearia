from django.db import migrations

def criar_servicos(apps, schema_editor):
    Servico = apps.get_model('reservas', 'Servico')
    servicos_basicos = [
        {"nome": "Corte a Tesoura", "descricao": "Corte tradicional com tesoura", "preco": 40.00},
        {"nome": "Corte a Máquina", "descricao": "Corte rápido com máquina", "preco": 30.00},
        {"nome": "Química", "descricao": "Tratamento químico para cabelos", "preco": 150.00},
        {"nome": "Escova", "descricao": "Escova modeladora", "preco": 80.00},
        {"nome": "Tintura", "descricao": "Coloração de cabelos", "preco": 120.00},
    ]
    for s in servicos_basicos:
        Servico.objects.get_or_create(nome=s["nome"], defaults={"descricao": s["descricao"], "preco": s["preco"]})

class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),  # ajuste se necessário
    ]

    operations = [
        migrations.RunPython(criar_servicos),
    ]
