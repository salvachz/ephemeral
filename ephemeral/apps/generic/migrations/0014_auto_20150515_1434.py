# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0013_auto_20150515_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
