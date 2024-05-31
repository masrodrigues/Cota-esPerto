from django.urls import path
from . import views

urlpatterns = [
    path('consultar/', views.consultar_produto, name='consultar_produto'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('atualizar/<str:codigo>/', views.atualizar_produto, name='atualizar_produto'),
    path('excluir/<str:codigo>/', views.excluir_produto, name='excluir_produto'),
]
