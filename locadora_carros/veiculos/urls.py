from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_veiculos, name='listar_veiculos'),
    path('veiculo/<int:veiculo_id>/', views.exibir_veiculo, name='exibir'),
    path('veiculo/novo/', views.criar_veiculo, name='criar'), 
    path('veiculo/editar/<int:veiculo_id>/', views.editar_veiculo, name='editar'), 
    path('veiculo/excluir/<int:veiculo_id>/', views.excluir_veiculo, name='excluir'),
]

