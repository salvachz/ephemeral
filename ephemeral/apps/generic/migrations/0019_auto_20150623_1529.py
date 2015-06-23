# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0018_contato_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoPedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.IntegerField(null=True, db_column='ppeProQnt', blank=True)),
            ],
            options={
                'db_table': 'ProdutoPedido',
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(db_column='pedUsrId', default='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contato',
            name='status',
            field=models.CharField(default='nao-lidow', max_length=45, db_column='conStatus', choices=[['lido', 'lido'], ['nao-lido', 'nao-lido']]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(null=True, db_column='proQnt', blank=True),
        ),
        migrations.AddField(
            model_name='produtopedido',
            name='pedido',
            field=models.ForeignKey(to='generic.Pedido', db_column='ppePedId'),
        ),
        migrations.AddField(
            model_name='produtopedido',
            name='produto',
            field=models.ForeignKey(to='generic.Produto', db_column='ppeProId'),
        ),
    ]
