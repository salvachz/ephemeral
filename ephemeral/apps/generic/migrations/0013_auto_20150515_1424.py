# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0012_auto_20150512_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_admin',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='name',
        ),
    ]
