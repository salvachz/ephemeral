from __future__ import unicode_literals

from django.db import models

class Produto(models.Model):
    id = models.IntegerField(db_column='proId', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='proNome', max_length=255)  # Field name made lowercase.       
    descricao = models.TextField(db_column='proDesc', blank=True, null=True)  # Field name made lowercase.
    preco = models.DecimalField(db_column='proPreco', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.CharField(db_column='proQnt', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Produto'
