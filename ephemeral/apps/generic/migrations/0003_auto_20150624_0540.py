# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0002_auto_20150624_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='mensagem',
            new_name='menssagem',
        ),
    ]
