# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0003_auto_20150624_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(db_column='proForId', blank=True, to='generic.Fornecedor', null=True),
        ),
    ]
