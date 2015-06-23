# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0015_produto_precofor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='conId')),
                ('nome', models.CharField(max_length=45, db_column='conNome')),
                ('email', models.CharField(max_length=100, db_column='conEmail')),
                ('assunto', models.CharField(max_length=45, db_column='conAssunto')),
                ('mensagem', models.TextField(db_column='conMensagem')),
            ],
            options={
                'db_table': 'Contato',
            },
        ),
    ]
