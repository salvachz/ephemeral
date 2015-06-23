from __future__ import unicode_literals

from django.db import models
from apps.generic.models import Produto

class Pedido(models.Model):
    id = models.AutoField(db_column='pedId', primary_key=True)
    produtos = models.ManyToManyField(Produto, through='ProdutoPedido')
    usuario = models.ForeignKey('Usuario', db_column='pedUsrId', blank=False, null=False, default='')
    status = models.CharField(db_column='pedStatus',
        choices=[(x,x) for x in ['aguardando pagamento','pago', 'enviado','entregue']],
        max_length=30, default='aguardando pagamento')
    forma_pagamento = models.CharField(db_column='pedFormPagamento',choices=[(x,x) for x in ['boleto','cartao']], max_length=10, default='boleto')
    last_update = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'Pedido'
 