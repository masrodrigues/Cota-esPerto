from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=100)
    descricao_longa = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=4)
    numero_de_pecas = models.IntegerField(default=0)  # Novo campo
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    cotacao_efetivada = models.BooleanField(default=False)
    data_efetivacao = models.DateField(null=True, blank=True)
    codigo_fusofix = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome
