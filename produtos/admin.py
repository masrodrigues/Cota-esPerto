from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'codigo_fusofix', 'valor', 'cotacao_efetivada', 'data_efetivacao', 'data_ultima_atualizacao')
    # Remova 'nome' se ele não existir no modelo Produto
    search_fields = ('codigo', 'codigo_fusofix')
    list_filter = ('cotacao_efetivada', 'data_efetivacao')

admin.site.register(Produto, ProdutoAdmin)
