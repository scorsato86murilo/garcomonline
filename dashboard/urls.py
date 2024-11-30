from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/painel', views.dashboard, name='dashboard'),
    path('dashboard/cardapio', views.cardapio, name='cardapio'),
    path('dashboard/comandas', views.comandas, name='comandas'),
    path('dashboard/cadastrar_clientes', views.cadastrar_clientes, name='cadastrar_clientes'),
    path('dashboard/adicionar_produtos', views.adicionar_produtos, name='adicionar_produtos'),
]