# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0024_pedido_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='last_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
