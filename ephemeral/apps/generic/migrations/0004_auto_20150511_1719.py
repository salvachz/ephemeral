# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0003_auto_20150511_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=10, db_column='proPreco', blank=True),
        ),
    ]
