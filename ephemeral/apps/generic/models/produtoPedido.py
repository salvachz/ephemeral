from __future__ import unicode_literals

from django.db import models
from apps.generic.models import Produto

class ProdutoPedido(models.Model):
    pedido = models.ForeignKey('Pedido', db_column='ppePedId')
    produto = models.ForeignKey('Produto', db_column='ppeProId')
    quantidade = models.IntegerField(db_column='ppeProQnt', blank=True, null=True)

    class Meta:
        db_table = 'ProdutoPedido'

    def __unicode__(self):
       return "%s-%s" % (self.pedido.usuario,self.pedido)

 
