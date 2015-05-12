# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0011_auto_20150512_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.CharField(default=b'Ativo', max_length=30, db_column=b'usrStatus', choices=[(b'Ativo', b'Ativo'), (b'Inativo', b'Inativo')]),
        ),
    ]
