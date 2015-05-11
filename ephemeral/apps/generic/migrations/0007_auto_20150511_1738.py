# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0006_auto_20150511_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(db_column='proMarId', blank=True, to='generic.Marca', null=True),
        ),
    ]
