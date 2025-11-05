from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('agendamento/novo/', views.novo_agendamento, name='novo_agendamento'),
    path('agendamento/<int:pk>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamento/<int:pk>/cancelar/', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('agendamento/<int:pk>/pagar/', views.pagar_agendamento, name='pagar_agendamento'),
]
