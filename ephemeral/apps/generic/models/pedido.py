from __future__ import unicode_literals

from django.db import models
from apps.generic.models import Produto

class Pedido(models.Model):
    id = models.AutoField(db_column='pedId', primary_key=True)
    produtos = models.ManyToManyField(Produto, through='ProdutoPedido')
    usuario = models.ForeignKey('Usuario', db_column='pedUsrId', blank=False, null=False, default='')
    forma_pagamento = models.CharField(db_column='pedFormPagamento',choices=[(x,x) for x in ['boleto','cartao']], max_length=10, default='boleto')

    class Meta:
        db_table = 'Pedido'
 