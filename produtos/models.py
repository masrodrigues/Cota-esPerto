from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_fusofix = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    descricao_longa = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=4)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    cotacao_efetivada = models.BooleanField(default=False)
    valor_efetivacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_efetivacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
