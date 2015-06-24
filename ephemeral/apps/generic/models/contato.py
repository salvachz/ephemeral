from __future__ import unicode_literals

from django.db import models

class Contato(models.Model):
    id = models.AutoField(db_column='conId', primary_key=True)
    nome = models.CharField(db_column='conNome', max_length=45)
    status = models.CharField(db_column='conStatus', max_length=45, choices=([x,x] for x in ('lido','nao-lido')), default='nao-lidow')
    email = models.CharField(db_column='conEmail', max_length=100)
    assunto = models.CharField(db_column='conAssunto', max_length=45)
    menssagem = models.TextField(db_column='conMensagem')


    class Meta:
        db_table = 'Contato'
