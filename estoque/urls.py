from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produto/novo/', views.novo_produto, name='novo_produto'),
    path('movimento/novo/', views.novo_movimento, name='novo_movimento'),
]
