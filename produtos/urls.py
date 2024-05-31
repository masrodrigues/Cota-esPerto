from django.urls import path
from . import views


urlpatterns = [
     path('', views.consultar_produto, name='consultar_produto'),
     path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
     path('atualizar/<str:codigo>/', views.atualizar_produto, name='atualizar_produto'),
     path('listar/', views.listar_produtos, name='listar_produtos'),
     # Nova URL para listar produtos
     
]