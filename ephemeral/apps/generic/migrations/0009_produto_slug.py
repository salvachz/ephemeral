# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0008_auto_20150511_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(editable=False, blank=True),
        ),
    ]
