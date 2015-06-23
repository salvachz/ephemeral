# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0019_auto_20150623_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='forma_pagament',
            field=models.CharField(default='boleto', max_length=10, db_column='pedFormPagamento', choices=[('boleto', 'boleto'), ('cartao', 'cartao')]),
        ),
    ]
