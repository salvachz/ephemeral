# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0021_auto_20150623_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(to='generic.Produto', through='generic.ProdutoPedido'),
        ),
    ]
