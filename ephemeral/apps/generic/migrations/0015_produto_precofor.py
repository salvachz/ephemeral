# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0014_auto_20150515_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='precoFor',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=10, db_column='precoFor', blank=True),
        ),
    ]
