from django.contrib.auth.models import User
from .models import Servico

def run():
    print("🔹 Criando serviços padrão...")

    servicos = [
        {"nome": "Corte de Cabelo", "descricao": "Corte masculino ou feminino profissional.", "preco": 40.00},
        {"nome": "Barba", "descricao": "Aparar e modelar barba com toalha quente.", "preco": 30.00},
        {"nome": "Manicure", "descricao": "Limpeza e esmaltação de unhas.", "preco": 25.00},
        {"nome": "Pedicure", "descricao": "Cuidados com os pés e esmaltação.", "preco": 30.00},
        {"nome": "Coloração", "descricao": "Tintura completa ou parcial.", "preco": 70.00},
    ]

    for s in servicos:
        Servico.objects.get_or_create(nome=s["nome"], defaults={"descricao": s["descricao"], "preco": s["preco"]})
    
    print("✅ Serviços adicionados com sucesso!")

    # Criar um superusuário padrão se não existir
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@salao.com", "admin123")
        print("👑 Usuário admin criado (login: admin / senha: admin123)")
    else:
        print("👑 Usuário admin já existe.")
