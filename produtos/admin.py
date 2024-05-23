from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'valor', 'data_ultima_atualizacao')
    search_fields = ('codigo', 'nome')
