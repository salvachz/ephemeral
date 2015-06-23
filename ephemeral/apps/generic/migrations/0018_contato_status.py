# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0017_auto_20150622_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='status',
            field=models.CharField(default='nao-lido', max_length=45, db_column='conStatus', choices=[['lido', 'lido'], ['nao-lido', 'nao-lido']]),
        ),
    ]
