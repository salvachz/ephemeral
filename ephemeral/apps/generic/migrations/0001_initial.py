# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='catId')),
                ('nome', models.CharField(max_length=45, db_column='catNome')),
            ],
            options={
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='forId')),
                ('nome', models.CharField(max_length=45, db_column='forNome')),
            ],
            options={
                'db_table': 'Fornecedor',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='pedId')),
            ],
            options={
                'db_table': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='proId')),
                ('nome', models.CharField(max_length=255, db_column='proNome')),
                ('descricao', models.TextField(null=True, db_column='proDesc', blank=True)),
                ('preco', models.DecimalField(null=True, decimal_places=0, max_digits=2, db_column='proPreco', blank=True)),
                ('quantidade', models.CharField(max_length=45, null=True, db_column='proQnt', blank=True)),
            ],
            options={
                'db_table': 'Produto',
            },
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='prmId')),
                ('preco', models.DecimalField(decimal_places=0, max_digits=2, db_column='prmPreco')),
                ('quantidade', models.CharField(max_length=45, db_column='prmQnt')),
                ('produto', models.ForeignKey(to='generic.Produto', db_column='prmProId')),
            ],
            options={
                'db_table': 'Promocao',
            },
        ),
    ]
