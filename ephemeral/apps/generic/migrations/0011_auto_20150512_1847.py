# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0010_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='linguaguem',
            field=models.CharField(default=b'Portugues', max_length=30, db_column=b'usrLanguage', choices=[(b'Portugues', b'Portugues'), (b'Inglish', b'Inglish')]),
        ),
    ]
