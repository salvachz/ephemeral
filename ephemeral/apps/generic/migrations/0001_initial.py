# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps.generic.models.produto


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.CharField(unique=True, max_length=255, db_column=b'usrMail')),
                ('name', models.CharField(max_length=65, db_column=b'usrName')),
                ('linguaguem', models.CharField(default=b'Portugues', max_length=30, db_column=b'usrLanguage', choices=[(b'Portugues', b'Portugues'), (b'Inglish', b'Inglish')])),
                ('status', models.CharField(default=b'Ativo', max_length=30, db_column=b'usrStatus', choices=[(b'Ativo', b'Ativo'), (b'Inativo', b'Inativo')])),
                ('last_access_ip', models.CharField(max_length=45, db_column=b'usrLastAccessIP')),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='catId')),
                ('nome', models.CharField(max_length=45, db_column='catNome')),
            ],
            options={
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='conId')),
                ('nome', models.CharField(max_length=45, db_column='conNome')),
                ('status', models.CharField(default='nao-lidow', max_length=45, db_column='conStatus', choices=[['lido', 'lido'], ['nao-lido', 'nao-lido']])),
                ('email', models.CharField(max_length=100, db_column='conEmail')),
                ('assunto', models.CharField(max_length=45, db_column='conAssunto')),
                ('mensagem', models.TextField(db_column='conMensagem')),
            ],
            options={
                'db_table': 'Contato',
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
            name='Marca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='marId')),
                ('nome', models.CharField(max_length=45, db_column='marNome')),
            ],
            options={
                'db_table': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='pedId')),
                ('status', models.CharField(default='aguardando pagamento', max_length=30, db_column='pedStatus', choices=[('aguardando pagamento', 'aguardando pagamento'), ('pago', 'pago'), ('enviado', 'enviado'), ('entregue', 'entregue')])),
                ('forma_pagamento', models.CharField(default='boleto', max_length=10, db_column='pedFormPagamento', choices=[('boleto', 'boleto'), ('cartao', 'cartao')])),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='proId')),
                ('nome', models.CharField(max_length=255, db_column='proNome')),
                ('descricao', models.TextField(null=True, db_column='proDesc', blank=True)),
                ('preco', models.DecimalField(null=True, decimal_places=2, max_digits=10, db_column='proPreco', blank=True)),
                ('precoFor', models.DecimalField(null=True, decimal_places=2, max_digits=10, db_column='precoFor', blank=True)),
                ('quantidade', models.IntegerField(null=True, db_column='proQnt', blank=True)),
                ('image', models.ImageField(null=True, upload_to=apps.generic.models.produto.get_image_path, blank=True)),
                ('slug', models.SlugField(editable=False, blank=True)),
                ('categoria', models.ForeignKey(db_column='proCatId', blank=True, to='generic.Categoria', null=True)),
                ('marca', models.ForeignKey(db_column='proMarId', blank=True, to='generic.Marca', null=True)),
            ],
            options={
                'db_table': 'Produto',
            },
        ),
        migrations.CreateModel(
            name='ProdutoPedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.IntegerField(null=True, db_column='ppeProQnt', blank=True)),
                ('pedido', models.ForeignKey(to='generic.Pedido', db_column='ppePedId')),
                ('produto', models.ForeignKey(to='generic.Produto', db_column='ppeProId')),
            ],
            options={
                'db_table': 'ProdutoPedido',
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
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(to='generic.Produto', through='generic.ProdutoPedido'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(db_column='pedUsrId', default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
