from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    id = models.AutoField(db_column='catId', primary_key=True)
    nome = models.CharField(db_column='catNome', max_length=45)

    class Meta:
        db_table = 'Categoria'

    def __unicode__(self):
        return self.nome