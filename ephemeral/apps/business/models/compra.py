from __future__ import unicode_literals
from django.db import models
from apps.generic.models import Usuario


class Compra(models.Model):
    id = models.AutoField(db_column='comId', primary_key=True)
    usuario = models.ForeignKey(Usuario, db_column='comUsrId', null=True, blank=True)
    data = models.DateTimeField(db_column='comDate',null=True)


    class Meta:
        db_table = 'Compra'

    def __unicode__(self):
        return "%s-%s" % (self.usuario, self.data)
