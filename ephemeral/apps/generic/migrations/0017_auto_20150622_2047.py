# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0016_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, db_column='conId'),
        ),
    ]
