from __future__ import unicode_literals

from django.db import models
from apps.generic.models import Produto

class Pedido(models.Model):
    id = models.IntegerField(db_column='pedId', primary_key=True)
    usuario = models.ForeignKey('Usuario', db_column='pedUsrId', blank=False, null=False, default='')

    class Meta:
        db_table = 'Pedido'
 