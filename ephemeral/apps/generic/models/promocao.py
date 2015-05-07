from __future__ import unicode_literals

from django.db import models

class Promocao(models.Model):
    id = models.IntegerField(db_column='prmId', primary_key=True)  # Field name made lowercase.
    produto = models.ForeignKey('Produto', db_column='prmProId')  # Field name made lowercase.
    preco = models.DecimalField(db_column='prmPreco', max_digits=2, decimal_places=0)  # Field name made lowercase.
    quantidade = models.CharField(db_column='prmQnt', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'Promocao'

