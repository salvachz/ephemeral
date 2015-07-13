from __future__ import unicode_literals
from django.db import models
from apps.generic.models import Usuario


class Carrinho(models.Model):
    id = models.AutoField(db_column='carId', primary_key=True)
    usuario = models.ForeignKey(Usuario, db_column='carUsrId', null=True, blank=True)
    data = models.DateTimeField(db_column='carDate',null=True)


    class Meta:
        db_table = 'Carrinho'

    def __unicode__(self):
        return "%s-%s" % (self.usuario, self.data)

    @property
    def data_str(self):
        return self.data.strftime('%d/%m/%Y')
