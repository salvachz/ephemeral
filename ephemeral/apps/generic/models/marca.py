from __future__ import unicode_literals

from django.db import models


class Marca(models.Model):
    id = models.AutoField(db_column='marId', primary_key=True)
    nome = models.CharField(db_column='marNome', max_length=45)

    class Meta:
        db_table = 'Marca'

    def __unicode__(self):
        return self.nome

