# produtos/management/commands/remove_duplicates.py
from django.core.management.base import BaseCommand
from produtos.models import Produto
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicates in codigo_fusofix field'

    def handle(self, *args, **kwargs):
        # Encontrar valores duplicados
        duplicados = Produto.objects.values('codigo_fusofix').annotate(count=Count('codigo_fusofix')).filter(count__gt=1)
        self.stdout.write(f"Duplicados encontrados: {duplicados}")

        # Corrigir valores duplicados
        for item in duplicados:
            produtos = Produto.objects.filter(codigo_fusofix=item['codigo_fusofix'])
            for i, produto in enumerate(produtos):
                if i > 0:  # Mantém o primeiro e altera os subsequentes
                    produto.codigo_fusofix = f"{produto.codigo_fusofix}_{i}"
                    produto.save()
                    self.stdout.write(f"Atualizado produto {produto.id} para {produto.codigo_fusofix}")
        self.stdout.write(self.style.SUCCESS('Duplicados corrigidos com sucesso'))
