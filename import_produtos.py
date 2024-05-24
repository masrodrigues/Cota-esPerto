import csv
import os
import django
from decimal import Decimal
from datetime import datetime

# Configura as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perto.settings')
django.setup()

from produtos.models import Produto

# Caminho para o arquivo CSV
csv_file_path = 'produtos.csv'

# Função para importar produtos do CSV
def importar_produtos():
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            valor = Decimal(row['valor'].replace("R$", "").replace(",", "."))
            produto, created = Produto.objects.get_or_create(
                codigo=row['codigo'],
                defaults={
                    'nome': row['nome'],
                    'descricao_longa': row['descricao_longa'],
                    'valor': valor,
                    'data_ultima_atualizacao': datetime.now()
                }
            )
            if created:
                print(f'Produto {produto.nome} criado com sucesso.')
            else:
                print(f'Produto {produto.nome} já existe.')

# Executa a função de importação
if __name__ == '__main__':
    importar_produtos()
