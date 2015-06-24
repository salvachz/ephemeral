# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=20, null=True, db_column=b'usrCpf'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nascimento',
            field=models.DateTimeField(null=True, db_column=b'usrNascimento'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(default=b'masculino', max_length=20, db_column=b'usrSexo', choices=[(b'masculino', b'masculino'), (b'feminino', b'feminino')]),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(max_length=100, null=True, db_column=b'usrSobrenome'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=20, null=True, db_column=b'usrTelefone'),
        ),
    ]
