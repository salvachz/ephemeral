# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0005_auto_20150511_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(db_column='proCatId', to='generic.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(db_column='proMarId', to='generic.Marca', null=True),
        ),
    ]
