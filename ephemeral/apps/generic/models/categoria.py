from __future__ import unicode_literals
from . import Produto
from django.db import models


class Categoria(models.Model):
    id = models.AutoField(db_column='catId', primary_key=True)
    nome = models.CharField(db_column='catNome', max_length=45)

    class Meta:
        db_table = 'Categoria'

    def __unicode__(self):
        return self.nome

    @staticmethod
    def get_quantified():
        field = 'categoria'
        result = Categoria.objects.all()
        quantified = {a[field]:a['total'] for a in Produto.objects.values(field).annotate(total=models.Count(field)).order_by('total')}
        for category in result:
            if category.id in quantified:
                category.total = quantified[category.id]
            else:
                category.total = 0
        return result