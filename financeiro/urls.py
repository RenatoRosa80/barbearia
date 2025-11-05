from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_movimentos, name='lista_movimentos'),
    path('novo/', views.novo_movimento, name='novo_movimento_financeiro'),
]
