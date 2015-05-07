from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    id = models.IntegerField(db_column='catId', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='catNome', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'Categoria'

