from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.servicos),
    path('servicos/<int:id>/', views.servico_detalhado),
    path('agendamentos/', views.agendamentos),
    path('agendamentos/<int:id>/', views.agendamento_detalhado)
]
