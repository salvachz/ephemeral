from __future__ import unicode_literals

from django.db import models

class Pedido(models.Model):
    id = models.IntegerField(db_column='pedId', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Pedido'

