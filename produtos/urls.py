from django.urls import path
from . import views

urlpatterns = [
     path('', views.consultar_produto, name='consultar_produto'),
     path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
     path('atualizar/<str:codigo>/', views.atualizar_produto, name='atualizar_produto'),
]